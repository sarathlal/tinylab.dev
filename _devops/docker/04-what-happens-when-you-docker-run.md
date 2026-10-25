---
title: "What happens when you type docker run"
description: "The chain from the docker CLI through dockerd, containerd, runc and the kernel — the single most asked 'explain it step by step' question for container roles."
section: "Docker"
section_order: 2
order: 4
level: intermediate
reading_time: 11
date: 2026-10-26
---

You type `docker run nginx` and a web server is running a second later. Between the Enter key and that server, five separate programs hand the work to each other, and each one exists for a reason. Knowing the chain explains a lot of otherwise puzzling behaviour: why containers survive a Docker restart, why Kubernetes dropped Docker, and why the Docker socket is such a sensitive file.

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


## Common mistakes

> **Common mistake**
> "Docker runs the container." Docker *starts* it; the kernel runs it, supervised by containerd's shim. If you say the daemon is the parent of the process, expect the follow-up "then why does `live-restore` work?"
{: .callout .callout-mistake}

> **Common mistake**
> Mounting `/var/run/docker.sock` into a CI container for convenience. It hands root on the host to every job that runs there. Use rootless builders (BuildKit, Kaniko) or a dedicated build VM.
{: .callout .callout-mistake}

## Check your understanding

Every answer below is in this page. Try to answer before you open it.

<ul class="check-list">
<li><details><summary>Name the five components in order, and give each one a one-line job.</summary>
<p><strong>docker CLI</strong> — turns your command into an API request. <strong>dockerd</strong> — pulls images, sets up the network, volumes and writable layer, builds the OCI bundle. <strong>containerd</strong> — supervises containers, starts a shim per container. <strong>runc</strong> — makes the kernel calls to create the isolated process, then exits. <strong>Linux kernel</strong> — provides namespaces, cgroups, capabilities and seccomp.</p>
</details></li>
<li><details><summary>Which program is the parent of the running nginx process?</summary>
<p>The containerd shim — not dockerd and not runc. runc exits as soon as the process is started. This is why <code>live-restore</code> lets you restart or upgrade the daemon without stopping containers.</p>
</details></li>
<li><details><summary>Why is giving someone access to <code>/var/run/docker.sock</code> the same as giving them root?</summary>
<p>Anyone who can write to that socket can ask the daemon to run any container, including one with the host filesystem mounted and privileges enabled. The daemon runs as root and will do it.</p>
</details></li>
<li><details><summary>What is an OCI bundle?</summary>
<p>A directory with a <code>rootfs</code> (the mounted image layers) and a <code>config.json</code> describing namespaces, cgroups, mounts, capabilities, environment and the command. It is the standard input to any OCI runtime, which is why runc can be swapped for crun, gVisor or Kata.</p>
</details></li>
<li><details><summary>Why did Kubernetes stop supporting Docker Engine, and did that break Docker images?</summary>
<p>The kubelet only needs the Container Runtime Interface, which containerd and CRI-O implement directly; supporting Docker meant maintaining an extra adapter (dockershim). Images did not change at all — they follow the OCI image spec, which every runtime reads.</p>
</details></li>
</ul>

## Further reading

- [containerd architecture](https://containerd.io/docs/)
- [OCI runtime specification](https://github.com/opencontainers/runtime-spec) — the `config.json` runc reads
- [Kubernetes: Dockershim removal FAQ](https://kubernetes.io/blog/2022/02/17/dockershim-faq/)
- Next: storage — volumes, bind mounts and where your data actually lives.
