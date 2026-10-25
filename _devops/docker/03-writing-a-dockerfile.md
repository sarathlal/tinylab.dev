---
title: "Writing a Dockerfile you'd be happy to show a reviewer"
description: "Multi-stage builds, cache-friendly ordering, non-root users, ENTRYPOINT vs CMD, and the handful of rules that turn a working Dockerfile into a production one."
section: "Docker"
section_order: 2
order: 3
level: intermediate
reading_time: 12
date: 2026-10-26
---

A Dockerfile that works is easy. A Dockerfile that builds fast, stays small, runs safely and behaves predictably when stopped takes a few deliberate choices. This page walks through those choices on one real example, then gives you a checklist to run your own Dockerfiles against.

## The everyday picture

> **The everyday picture**
> A Dockerfile is a recipe for packing a lunchbox. A beginner packs everything in the kitchen "just in case" — the whole spice rack, the frying pan, the recipe book — and ends up with a lunchbox nobody can carry. A good cook does the cooking in the kitchen, packs only the finished meal and a fork, writes the reheating instructions on the lid, and labels it with a name, not "today's lunch".
>
> **Multi-stage builds** are the kitchen-versus-lunchbox split. **Layer ordering** is packing the things that don't change (the box, the fork) before the things that do (today's meal). **`ENTRYPOINT`/`CMD`** are the reheating instructions. The **non-root user** is making sure the lunchbox can't set the office microwave on fire.
{: .callout .callout-analogy}

## What it actually is

Here is a Node.js API packaged the way most tutorials show it, then the same thing done properly.

**The naive version** (works, ~1.1 GB, rebuilds dependencies on every change, runs as root):

```dockerfile
FROM node:22
COPY . .
RUN npm install
CMD npm start
```

**The production version** (~130 MB, dependency layer cached, non-root, handles signals):

```dockerfile
# syntax=docker/dockerfile:1

# ---- Stage 1: build ------------------------------------------------------
FROM node:22-bookworm-slim AS build
WORKDIR /app

# Dependencies first: this layer is reused until package*.json changes
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev

# Source last: changes here don't invalidate the dependency layer
COPY src ./src

# ---- Stage 2: runtime ----------------------------------------------------
FROM node:22-bookworm-slim AS runtime
ENV NODE_ENV=production
WORKDIR /app

# Create an unprivileged user and own only what the app needs
RUN groupadd --system app && useradd --system --gid app --home /app app
COPY --from=build --chown=app:app /app/node_modules ./node_modules
COPY --from=build --chown=app:app /app/src ./src
COPY --chown=app:app package.json ./

USER app
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD node -e "fetch('http://localhost:3000/healthz').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

# Exec form: node becomes PID 1 and receives SIGTERM directly
ENTRYPOINT ["node", "src/server.js"]
CMD []
```

What each decision buys you:

| Decision | Why it matters |
| --- | --- |
| `# syntax=docker/dockerfile:1` | Enables BuildKit features like cache mounts and build secrets |
| `-slim` base, two stages | Build tools and dev dependencies never reach the final image |
| `COPY package*.json` before `npm ci` | Dependency layer is cached until the lockfile changes |
| `--mount=type=cache` | npm's download cache persists across builds without ending up in a layer |
| `npm ci --omit=dev` | Reproducible install from the lockfile, no dev dependencies |
| `USER app` | A container escape or app bug does not start as root |
| `--chown` on `COPY` | Avoids a separate `RUN chown -R` that would duplicate every file into a new layer |
| `HEALTHCHECK` | Orchestrators and `docker ps` can tell "running" from "actually working" |
| `ENTRYPOINT` in exec form | The process is PID 1 and gets `SIGTERM` on `docker stop`; shell form wraps it in `sh -c`, which swallows signals |

### `ENTRYPOINT` vs `CMD`, once and for all

- `ENTRYPOINT` is the executable. `CMD` is its default arguments. `docker run image extra args` *replaces* `CMD` and *appends* to `ENTRYPOINT`.
- Use exec form (`["node", "server.js"]`), not shell form (`node server.js`). Shell form runs `/bin/sh -c "node server.js"`, so PID 1 is `sh`, and `sh` does not forward `SIGTERM`. Your app then gets killed with `SIGKILL` after the 10-second grace period, mid-request.
- If your process must be wrapped in a shell, or spawns children it cannot reap, add an init: `docker run --init` or `tini` as the `ENTRYPOINT`.

### `ARG` vs `ENV`

`ARG` exists only at build time and does not persist into the image config; `ENV` persists and is visible with `docker inspect`. Never pass secrets through either — they end up in layer metadata and `docker history`. Use `RUN --mount=type=secret,id=npmrc` and read the file during that one instruction.

## Try it yourself

> **Try it yourself**
> See the signal problem for yourself; it is the most common "my container takes 10 seconds to stop" bug.
{: .callout .callout-try}

```dockerfile
# Dockerfile.shellform
FROM alpine:3.20
CMD sleep 300
```

```dockerfile
# Dockerfile.execform
FROM alpine:3.20
CMD ["sleep", "300"]
```

```bash
docker build -f Dockerfile.shellform -t sig-shell .
docker build -f Dockerfile.execform  -t sig-exec .

docker run -d --name a sig-shell && time docker stop a   # ~10 s: SIGTERM ignored, SIGKILL after timeout
docker run -d --name b sig-exec  && time docker stop b   # fast: sleep gets SIGTERM directly
docker rm a b
```

Then add a `.dockerignore` to any project you have and compare `docker build` context size before and after (`Sending build context to Docker daemon …` or BuildKit's `transferring context` line):

```
.git
node_modules
*.log
.env
```


## Common mistakes

> **Common mistake**
> `RUN apt-get update` in one instruction and `RUN apt-get install …` in the next. The `update` layer gets cached, so weeks later `install` runs against a stale package list and fails or installs old versions. Always `apt-get update && apt-get install -y --no-install-recommends … && rm -rf /var/lib/apt/lists/*` in one `RUN`.
{: .callout .callout-mistake}

> **Common mistake**
> `VOLUME` in the Dockerfile. It silently creates an anonymous volume on every run, surprises everyone, and cannot be undone by later instructions. Declare volumes at run time or in Compose, where they are visible.
{: .callout .callout-mistake}

## Checklist for your own Dockerfiles

- [ ] Pinned base image (`node:22.9-bookworm-slim`, or a digest in CI)
- [ ] Multi-stage build; no compilers or dev dependencies in the final stage
- [ ] Dependency manifests copied and installed before source
- [ ] `.dockerignore` present
- [ ] Package caches cleaned in the same `RUN` that created them
- [ ] Non-root `USER`
- [ ] Exec-form `ENTRYPOINT`; `--init` or `tini` if the process can't handle signals or children
- [ ] `HEALTHCHECK` defined
- [ ] No secrets via `ARG`, `ENV` or `COPY`
- [ ] `EXPOSE` documents the port; labels (`org.opencontainers.image.*`) document the source

## Check your understanding

Every answer below is in this page. Try to answer before you open it.

<ul class="check-list">
<li><details><summary>What does a multi-stage build achieve, in one sentence?</summary>
<p>It does the building (compilers, dev dependencies, caches) in one stage and copies only the finished result into a clean final stage, so none of the build-time tooling ends up in the image you ship.</p>
</details></li>
<li><details><summary>Why does <code>CMD npm start</code> make <code>docker stop</code> take ten seconds?</summary>
<p>It is shell form, so PID 1 is <code>/bin/sh -c</code>, and <code>sh</code> does not forward <code>SIGTERM</code> to the child. The app never hears the stop request, so Docker waits for the grace period and then sends <code>SIGKILL</code>. Use exec form (<code>["node", "src/server.js"]</code>) so the real process is PID 1.</p>
</details></li>
<li><details><summary>What is the difference between <code>ENTRYPOINT</code> and <code>CMD</code>?</summary>
<p><code>ENTRYPOINT</code> is the executable; <code>CMD</code> is its default arguments. Extra arguments on <code>docker run</code> replace <code>CMD</code> and are appended to <code>ENTRYPOINT</code>.</p>
</details></li>
<li><details><summary>Why is it unsafe to pass a secret with <code>ARG</code> or <code>ENV</code>?</summary>
<p><code>ENV</code> values persist in the image config and show in <code>docker inspect</code>; <code>ARG</code> values appear in layer metadata and <code>docker history</code>. Use <code>RUN --mount=type=secret</code> so the secret exists only during that one instruction and never lands in a layer.</p>
</details></li>
<li><details><summary>Why do <code>apt-get update</code> and <code>apt-get install</code> belong in the same <code>RUN</code>?</summary>
<p>If they are separate, the <code>update</code> layer gets cached. Weeks later the <code>install</code> step runs against a stale package list and fails or installs old versions.</p>
</details></li>
<li><details><summary>Why use <code>COPY --chown</code> instead of a later <code>RUN chown -R</code>?</summary>
<p>A <code>RUN chown -R</code> changes every file's metadata, which copies every file into a new layer — doubling that part of the image. <code>--chown</code> sets ownership as the files are written.</p>
</details></li>
</ul>

## Further reading

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Docker docs: Best practices for writing Dockerfiles](https://docs.docker.com/build/building/best-practices/)
- [Docker docs: Build secrets](https://docs.docker.com/build/building/secrets/)
- Next page: what happens inside the kernel when `docker run` is executed.
