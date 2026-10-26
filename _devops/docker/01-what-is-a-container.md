---
title: What is a container?
description: A container is just a normal Linux process that has been told a convincing lie about the machine it is running on. Here is the lie, who tells it, and why it matters.
section: Docker
section_order: 4
order: 1
level: foundation
reading_time: 9
date: 2026-10-26
---

Everyone says "containers are lightweight virtual machines". They are not, and the difference matters as soon as you try to understand why containers start instantly, why they can't run Windows on Linux, or what a container can and cannot see. A container is an ordinary process — the same kind of process as your text editor — that the Linux kernel has walled off so it cannot see the rest of the machine.

## The everyday picture

> **The everyday picture**
> Think of a large shared office building. A **virtual machine** is like renting a whole separate building next door: you get your own electricity, plumbing, security desk and reception. It is completely yours, but it is expensive and takes weeks to set up.
>
> A **container** is like renting one office *inside* the shared building. You get your own locked door, your own desk, your own name plate on the directory, and you cannot walk into anyone else's office. But the building's electricity, plumbing and security are shared with everyone else. Moving in takes minutes, and the building can hold hundreds of offices.
>
> The building is the Linux kernel. The locked door, name plate and "you can't see other offices" rules are kernel features called *namespaces*. The rule that says "your office may only use this much electricity" is a feature called *cgroups*.
{: .callout .callout-analogy}

## What it actually is

A container is a process (or a tree of processes) started with three kinds of kernel restrictions:

| Kernel feature | What it does | Office analogy |
| --- | --- | --- |
| **Namespaces** | Give the process its own view of process IDs, network interfaces, mount points, hostname, users and inter-process communication | Your own locked office and name plate |
| **cgroups** (control groups) | Limit and account for CPU, memory, disk I/O and process count | The electricity meter on your office |
| **Capabilities, seccomp, LSMs** | Remove dangerous privileges from the process even if it runs as root inside | The building rules about what tenants may do |

There is no separate operating system inside a container. When you run an "Ubuntu container" on a Fedora laptop, both are using the Fedora kernel. The Ubuntu part is only files — `/bin/bash`, `/usr/lib`, the package database — unpacked into a directory and shown to the process as if it were the root of the filesystem.

This is why containers start in milliseconds (it is just a process starting) and why a container cannot run a different kernel or a different operating system family. Linux containers on macOS or Windows run inside a hidden Linux virtual machine; Docker Desktop manages that VM for you.

A virtual machine, by contrast, runs a complete guest kernel on top of a hypervisor. It is more isolated (a kernel bug in the guest does not affect the host) and more expensive (gigabytes of memory, seconds to minutes to boot).

## Try it yourself

> **Try it yourself**
> Prove that a container is a normal process you can see from the host.
{: .callout .callout-try}

```bash
# Start a container that just sleeps
docker run -d --name demo alpine sleep 600

# From the HOST, find that sleep process. It is a plain process.
ps -ef | grep "sleep 600" | grep -v grep

# Inside the container, the same process thinks it is PID 1
docker exec demo ps -ef
```

Expected: on the host you see `sleep 600` with an ordinary PID like 48213; inside the container the same process shows as PID 1. Same process, two different views — that is the PID namespace at work.

```bash
# See the namespaces the container's process lives in
PID=$(docker inspect --format '{% raw %}{{.State.Pid}}{% endraw %}' demo)
sudo ls -l /proc/$PID/ns

# Compare with your own shell's namespaces
ls -l /proc/$$/ns

docker rm -f demo
```

The numbers in square brackets are namespace IDs. Where they differ, the container has its own; where they match, it shares yours.


## Common mistakes

> **Common mistake**
> Saying "the container has its own OS". It has its own *filesystem image* containing an OS's files, but it runs on the host's kernel. There is no "Ubuntu kernel" inside the container.
{: .callout .callout-mistake}

> **Common mistake**
> Assuming root inside a container equals root on the host. By default it is close — which is exactly why running as a non-root user and dropping capabilities matters, and why rootless Docker exists. Later pages cover both.
{: .callout .callout-mistake}

## Check your understanding

Every answer below is in this page. Try to answer before you open it.

<ul class="check-list">
<li><details><summary>Does a container have its own operating system?</summary>
<p>No. It has its own <em>filesystem image</em> containing an operating system's files, but it runs on the host's kernel. An "Ubuntu container" on a Fedora laptop uses the Fedora kernel; only the files are Ubuntu's.</p>
</details></li>
<li><details><summary>Which two kernel features do most of the isolation work, and what does each do?</summary>
<p><strong>Namespaces</strong> give the process its own view of process IDs, network interfaces, mount points, hostname, users and IPC — the locked office. <strong>cgroups</strong> limit and account for CPU, memory, disk I/O and process count — the electricity meter.</p>
</details></li>
<li><details><summary>Why does the same process show as PID 48213 on the host but PID 1 inside the container?</summary>
<p>Because of the PID namespace. The process is one real process; the namespace gives it a private numbering where it is the first process. The host sees the real number.</p>
</details></li>
<li><details><summary>Why do containers start in milliseconds while a virtual machine takes seconds or minutes?</summary>
<p>Starting a container is just starting a process with some restrictions. A virtual machine has to boot an entire guest kernel on top of a hypervisor.</p>
</details></li>
<li><details><summary>Why do Linux containers on a Mac or Windows laptop feel different?</summary>
<p>They run inside a hidden Linux virtual machine, because the host kernel is not Linux. Docker Desktop manages that VM for you.</p>
</details></li>
</ul>

## Further reading

- [Docker docs: What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- `man 7 namespaces` and `man 7 cgroups` on any Linux machine
- Next page: how the filesystem the process sees is assembled from *image layers*.
