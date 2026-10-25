---
title: "Images, layers and why your image is 1.2 GB"
description: "An image is a stack of read-only layers plus a bit of metadata. Understanding the stack explains caching, image size, and half of all Dockerfile mistakes."
section: "Docker"
section_order: 2
order: 2
level: foundation
reading_time: 10
date: 2026-10-26
---

A Docker image is not a disk file like a `.iso`. It is a list of **layers** — each one a compressed folder of files — plus a small JSON document saying how to stack them and how to start the process. Once you see it that way, image size, build caching and the "why did my secret end up in the image?" problem all make sense.

## The everyday picture

> **The everyday picture**
> Imagine a stack of transparent sheets, like the overhead-projector slides teachers once used. The bottom sheet has the outline of a map. The next sheet adds roads. The next adds town names. Looking down from the top you see one complete map, but each sheet is separate and never changes.
>
> If you want a map with the same roads but different town names, you keep the bottom two sheets and swap only the top one. That is a **layer cache**: anything below the sheet you changed is reused.
>
> Now the catch: if someone drew a secret on sheet three and then "erased" it by putting an opaque white patch on sheet four, the secret is still on sheet three. Anyone who lifts off sheet four can read it. That is exactly how deleting a file in a later `RUN` step fails to remove it from the image.
{: .callout .callout-analogy}

## What it actually is

Every instruction in a Dockerfile that changes the filesystem (`FROM`, `RUN`, `COPY`, `ADD`) produces a layer. A layer is a tarball of the files that instruction *added or changed*. Layers are read-only and identified by the SHA-256 digest of their contents, so two images built from the same base share those layers on disk and in the registry.

When a container starts, the runtime stacks the layers with a **union filesystem** (overlay2 on modern Linux) and adds one thin **writable layer** on top. Writes go there; reads fall through to the first layer below that has the file. Deleting a file in the writable layer creates a "whiteout" marker — the file is hidden, not removed from the lower layers.

Three consequences follow directly:

1. **Size adds up, never down.** A layer that installs 300 MB of build tools and a later layer that deletes them still leaves a 300 MB image. Delete in the *same* `RUN` instruction, or use a multi-stage build so the tools never reach the final image.
2. **The cache works top-down.** Docker reuses a cached layer only if the instruction and every layer above it are unchanged. Put things that change rarely (base image, system packages, dependency manifests) early, and things that change often (your source code) late.
3. **Secrets written to any layer are in the image forever**, even if a later step deletes them. Use build secrets (`--mount=type=secret`) or multi-stage builds instead.

The image's metadata — the **manifest** — lists the layer digests and points at a **config** JSON with environment variables, the default command, the working directory and the user. A **tag** like `nginx:1.27` is a mutable name pointing at a manifest digest; the digest `nginx@sha256:…` is immutable. This is why production deployments pin digests.

## Try it yourself

> **Try it yourself**
> Watch a deleted file survive in the image, then fix it.
{: .callout .callout-try}

Create this Dockerfile in an empty folder:

```dockerfile
FROM alpine:3.20
RUN dd if=/dev/zero of=/big.bin bs=1M count=100
RUN rm /big.bin
```

```bash
docker build -t layer-demo .
docker image ls layer-demo          # ~ 110 MB even though /big.bin is "gone"
docker history layer-demo           # see each layer and its size
```

Now change it so the file is created and removed in one instruction:

```dockerfile
FROM alpine:3.20
RUN dd if=/dev/zero of=/big.bin bs=1M count=100 && rm /big.bin
```

```bash
docker build -t layer-demo-fixed .
docker image ls layer-demo-fixed    # ~ 8 MB
```

Finally, look inside a real image's manifest:

```bash
docker manifest inspect alpine:3.20 | head -40
docker image inspect alpine:3.20 --format '{% raw %}{{json .RootFS.Layers}}{% endraw %}'
```

## In the interview

> **In the interview**
> **Question they ask:** "My image is 1.2 GB. How would you get it under 100 MB?"
>
> **What they are really checking:** whether you understand layers well enough to diagnose, not just whether you know the word "alpine".
>
> **A strong answer:** "First I'd run `docker history` to see which layers are big. Usually it's one of four things: build tools or package caches left in the final image — fix with a multi-stage build and `--no-install-recommends` / cleaning the cache in the same `RUN`; the whole repository copied in, including `.git` and `node_modules` — fix with `.dockerignore`; a heavy base image where `-slim` or distroless would do; or dependencies installed after copying source, so every code change re-downloads them and bloats the cache. I'd also pin the base image by digest so the size stays predictable."
>
> **Follow-ups to expect:** "Why doesn't `rm` in a later step help?" (Whiteouts; lower layers are immutable.) "Alpine vs distroless?" (Alpine uses musl, which can bite some binaries; distroless has no shell, which is good for security and bad for debugging — use `docker debug` or an ephemeral container.)
{: .callout .callout-interview}

## Common mistakes

> **Common mistake**
> `COPY . .` before `RUN npm install` (or `pip install`). Every source change invalidates the dependency layer and re-installs everything. Copy the manifest files first, install, then copy the source.
{: .callout .callout-mistake}

> **Common mistake**
> Using `latest`. It is a tag, not a version. Two builds a week apart can produce different images with the same name, and a rollback to "latest" rolls back to nothing. Pin a version tag for humans and a digest for machines.
{: .callout .callout-mistake}

## Further reading

- [Docker docs: Image layers](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/)
- [OCI image specification](https://github.com/opencontainers/image-spec) — the manifest and config formats every registry speaks
- Next page: turning this knowledge into a Dockerfile you would be happy to show a reviewer.
