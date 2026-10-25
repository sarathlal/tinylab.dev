---
title: "What happens when you type docker run"
description: "The chain from the docker CLI through dockerd, containerd, runc and the kernel — the single most asked 'explain it step by step' question for container roles."
section: "Docker"
section_order: 2
order: 4
level: senior
reading_time: 11
date: 2026-10-26
---

"Walk me through what happens when you run `docker run nginx`" is the container equivalent of "what happens when you type a URL into a browser". It is asked because the answer reveals whether you know the moving parts or just the CLI. There are five of them, and each exists for a reason.

## The everyday picture

> **The everyday picture**
> Ordering food at a large restaurant. You (the `docker` command) tell the waiter what you want. The waiter (`dockerd`) checks whether the kitchen has the ingredients, fetches them from the supplier if not, and writes the order ticket. The head chef (`containerd`) takes the ticket, lays out the ingredients on a station, and hands it to a line cook. The line cook (`runc`) actually cooks the dish and then leaves — the dish stays on the station. The station itself, with its burners and ventilation and the rule that cooks don't wander into each other's stations, is the kernel.
>
> The restaurant is split up this way for the same reason a real one is: the waiter can be replaced without retraining the chefs, the chefs can serve other waiters (Kubernetes talks to `containerd` directly, skipping `dockerd`), and the line cook's job is small enough to be standardised across the industry — that standard is the OCI runtime spec.
{: .callout .callout-analogy}

## What it actually is

Here is the chain, in order, for `docker run -d -p 8080:80 nginx:1.27`.

### 1. The CLI talks to the daemon

The `docker` binary is only a client. It turns your flags into a JSON request and sends it over the Unix socket `/var/run/docker.sock` to `dockerd`'s REST API. This is why adding a user to the `docker` group is equivalent to giving them root: whoever can write to that socket can ask the daemon to run anything, including a container with the host filesystem mounted.

### 2. dockerd resolves the image

`dockerd` checks its local image store for `nginx:1.27`. If it is missing, it contacts the registry (Docker Hub by default), fetches the **manifest** for your CPU architecture, and downloads each **layer** it does not already have, verifying every blob against its SHA-256 digest. Layers are stored once, unpacked, under `/var/lib/docker/overlay2/`.

### 3. dockerd prepares the container and hands off to containerd

`dockerd` creates the container's writable layer, sets up the network namespace and attaches it to the `bridge` network (creating a `veth` pair: one end inside the container, one end plugged into the `docker0` bridge), allocates an IP from the bridge's subnet, and writes iptables rules so that host port 8080 is DNAT-ed to the container's port 80. It then builds an **OCI runtime bundle** — a directory with a `rootfs` (the overlay mount) and a `config.json` describing namespaces, cgroups, mounts, capabilities, environment and the command — and asks `containerd` over gRPC to start it.

### 4. containerd starts a shim and calls runc

`containerd` is the long-running supervisor. For each container it starts a tiny **shim** process (`containerd-shim-runc-v2`) that will own the container's lifecycle, stdio and exit code. The shim invokes `runc create` and `runc start` with the bundle.

### 5. runc asks the kernel for isolation, then exits

`runc` is a short-lived binary that does the actual kernel work: it calls `clone()` with flags for new PID, network, mount, UTS, IPC (and optionally user) namespaces; writes the resource limits into the container's **cgroup**; `pivot_root`s into the overlay `rootfs`; drops **capabilities**; applies the **seccomp** profile and any AppArmor/SELinux label; and finally `exec`s `nginx`. Then `runc` exits. The nginx process is now a child of the shim, isolated by the kernel, and nothing called "Docker" is in its process tree.

This is why you can stop or upgrade `dockerd` without stopping running containers (the `live-restore` option): the containers belong to the shims and the kernel, not to the daemon.

### Why the split matters

| Component | Role | Can be swapped for |
| --- | --- | --- |
| `docker` CLI | User interface | `nerdctl`, `podman` |
| `dockerd` | Image building, networking, volumes, API | Podman (daemonless), Kubernetes talks past it |
| `containerd` | Container supervisor, image store, snapshots | CRI-O |
| `runc` | OCI runtime: creates the isolated process | `crun`, `gVisor (runsc)`, `Kata`, `youki` |
| Linux kernel | Namespaces, cgroups, capabilities, seccomp | — |

Kubernetes removed Docker Engine support (dockershim) in v1.24 because the kubelet only needs the **Container Runtime Interface**, which `containerd` and CRI-O implement directly. Your images did not change; only the top of the stack did.

## Try it yourself

> **Try it yourself**
> Watch every layer of the stack take part in a single `docker run`.
{: .callout .callout-try}

```bash
# 1. The API call the CLI makes
docker --debug run --rm alpine true 2>&1 | grep -i "POST\|GET" | head

# 2. Pull progress shows manifest then layers
docker pull nginx:1.27

# 3. containerd's view of the container (requires root; path may differ on Docker Desktop)
docker run -d --name web -p 8080:80 nginx:1.27
sudo ctr --namespace moby containers ls
sudo ctr --namespace moby tasks ls

# 4. The shim and the process tree
ps -ef --forest | grep -B2 -A2 "nginx: master" | head -20

# 5. The iptables rule dockerd added for -p 8080:80
sudo iptables -t nat -L DOCKER -n | grep 8080

# 6. The OCI bundle runc was given
sudo ls /run/containerd/io.containerd.runtime.v2.task/moby/$(docker inspect --format '{% raw %}{{.Id}}{% endraw %}' web)/
sudo cat /run/containerd/io.containerd.runtime.v2.task/moby/$(docker inspect --format '{% raw %}{{.Id}}{% endraw %}' web)/config.json | python3 -m json.tool | head -60

docker rm -f web
```

If `ctr` is not on your path, it ships with Docker Engine on Linux; on Docker Desktop you would run these inside the Desktop VM.

## In the interview

> **In the interview**
> **Question they ask:** "Walk me through what happens when I run `docker run nginx`."
>
> **What they are really checking:** whether you know the components (CLI → dockerd → containerd → shim → runc → kernel), what each one is for, and where the kernel features from the first page fit.
>
> **A strong answer** in under two minutes: "The CLI sends an API request over the Docker socket to dockerd. dockerd checks the local image store and, if needed, pulls the manifest and layers from the registry, verifying digests. It creates the writable layer, sets up the network namespace, veth pair and port-mapping iptables rules, builds an OCI bundle, and asks containerd over gRPC to run it. containerd spawns a shim per container and calls runc. runc makes the kernel calls — clone with new namespaces, cgroup limits, pivot_root into the overlay rootfs, drop capabilities, apply seccomp — then execs nginx and exits. From then on the container is a kernel-isolated process owned by the shim, which is why the daemon can restart without killing containers."
>
> **Follow-ups to expect:** "Why did Kubernetes drop Docker?" (CRI; it only ever needed containerd.) "What's the security implication of the Docker socket?" (Root-equivalent.) "Where does the image end and the container begin?" (The writable layer.)
{: .callout .callout-interview}

## Common mistakes

> **Common mistake**
> "Docker runs the container." Docker *starts* it; the kernel runs it, supervised by containerd's shim. If you say the daemon is the parent of the process, expect the follow-up "then why does `live-restore` work?"
{: .callout .callout-mistake}

> **Common mistake**
> Mounting `/var/run/docker.sock` into a CI container for convenience. It hands root on the host to every job that runs there. Use rootless builders (BuildKit, Kaniko) or a dedicated build VM.
{: .callout .callout-mistake}

## Further reading

- [containerd architecture](https://containerd.io/docs/)
- [OCI runtime specification](https://github.com/opencontainers/runtime-spec) — the `config.json` runc reads
- [Kubernetes: Dockershim removal FAQ](https://kubernetes.io/blog/2022/02/17/dockershim-faq/)
- Next: storage — volumes, bind mounts and where your data actually lives.
