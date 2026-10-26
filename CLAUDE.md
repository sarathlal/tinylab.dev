# tinylab.dev — guide for writing tutorial pages

This repository is a Jekyll site with long-form learning tracks. Read this file before
writing or editing any tutorial page. `CONTRIBUTING.md` covers the site mechanics; this
file covers *what a page must be*.

## What the site is

A hands-on learning kit for ordinary people — not exam prep, not interview prep, not a
reference manual. Every page teaches one topic thoroughly enough that a reader who does
the exercises could use it at work the next day and explain it to a colleague.

## The writing standard

### 1. Depth: the complete picture of one topic

Each page covers its topic **completely** — everything a working engineer needs to know
about it, including the parts that are usually left out because they are hard. Aim for
2,500–5,000 words plus code. If a topic cannot be covered properly in that space, split it
into two pages in the curriculum rather than writing a shallow one.

"Complete" means the page answers, for its topic:
- What it is and what problem it solves
- How it works underneath — the real mechanism, named components, what talks to what
- How to use it day to day — the commands, files and options people actually use
- How it fails — the common errors, what they look like, and how to diagnose each
- The trade-offs and alternatives, and when *not* to use it
- The vocabulary a reader will meet in documentation and at work
- Where to read more — official documentation, specifications, the best deep-dive sources

The `covers:` list in a stub's front matter is the minimum; expand on it.

### 2. Accuracy: never state something you have not verified

This is the rule that matters most. Wrong information in a tutorial does real damage.

- **Run every command before you publish it.** Show real output, trimmed. If a command
  cannot be run in the writing environment, say so in the page ("on a Linux host this
  prints…") and keep it to commands you are certain of from official documentation.
- **Check every flag, file path, default value and version against the official
  documentation** for the tool, at the time of writing. Link to the page you checked.
- **Pin versions in examples** (`node:22-bookworm-slim`, `kubectl` 1.31) and say which
  version the page was written against in a note near the top. Tools change; a dated,
  versioned page is honest; an undated one is a trap.
- **Do not invent**: flags, error messages, config keys, statistics, benchmark numbers,
  history, quotes, or "best practices" nobody actually recommends. If you are not sure
  something is true, leave it out or mark it clearly as something to verify.
- **Do not copy** text from other tutorials or documentation. Read, understand, write in
  your own words. Short quoted definitions from specs are fine with attribution.
- **Distinguish fact from opinion.** "Alpine uses musl" is a fact. "Prefer distroless"
  is a recommendation — say why and when it does not apply.
- **Analogies must stay true.** An analogy that is memorable but misleading is worse than
  none. Stretch it only as far as it maps to the real mechanism, and say where it breaks.
- When a page is finished, re-read it as a sceptical expert looking for anything wrong.
  Fix or remove anything you cannot defend.

### 3. Plain language

Written for someone with no technical background who is willing to work. That means:
- One idea per paragraph; sentences under 25 words where possible.
- Define every term the first time it appears, in the sentence itself.
- One everyday analogy per page, early, then the real explanation.
- Prefer concrete examples to abstract statements. Show, then explain.
- No filler ("In this article we will…", "It is important to note that…").
- No exam, quiz-show or interview framing anywhere. The "Check your understanding"
  section at the end is for the reader's own benefit; its answers are in the page.

### 4. Hands-on

Every page has something the reader does, not just reads: commands to run, a file to
write, something to break and fix. Give the expected output so they know they succeeded.
Keep the lab self-contained — runnable on a laptop with Docker Desktop or a free-tier
cloud account, in under an hour.

## Page structure

Use `_templates/tutorial-page.md`. The sections, in order:

1. **Lead** — two to four sentences: what the page answers, why it matters, what you will
   be able to do afterwards. Plus a one-line "Written against: Docker 27.x, Ubuntu 24.04"
   note where versions matter.
2. **The everyday picture** — the analogy (callout `callout-analogy`).
3. **What it actually is** — the full explanation. This is the body of the page and may
   have several `###` subsections. Tables for comparisons, diagrams where structure has a
   shape (Mermaid fenced blocks are fine; keep them simple).
4. **How it is used in practice** — the day-to-day commands, files, patterns.
5. **Try it yourself** — the hands-on exercise (callout `callout-try` introducing it, then
   the steps with expected output).
6. **When it goes wrong** — the common failures and how to diagnose each.
7. **Common mistakes** — short `callout-mistake` blocks.
8. **Check your understanding** — 5–8 questions as `<details>` in a `check-list`, each
   answer two to four sentences drawn from the page.
9. **Further reading** — official documentation first, then specifications, then the best
   long-form sources. Only links you have opened.

Sections 4 and 6 can be folded into 3 for a small topic, but never skip 5, 7, 8 or 9.

## Front matter

```yaml
title: "Short title, a question or a noun phrase"
description: "One sentence, shown under the title and in search."
section: "Docker"        # must match the curriculum exactly
section_order: 4         # from the curriculum — do not change by hand
order: 6                 # from the curriculum — do not change by hand
level: foundation        # foundation | intermediate | advanced
reading_time: 14         # minutes; roughly words / 200
date: 2026-10-27         # last substantive update
```

Remove `draft: true`, `sitemap: false` and `covers:` when the page is written.

## Workflow for writing a page

1. `python3 scripts/scaffold.py devops --check` — confirm the structure is in sync.
2. Open the stub. Its `covers:` list is the brief. Read the previous and next pages in
   the section so the new page starts where the last one ended and does not repeat it.
3. Research: open the official documentation for everything the page touches. Note the
   version you are reading.
4. Write the page in the structure above.
5. Run every command. Paste real output. Fix anything that differs from what you wrote.
6. Re-read as a sceptical expert. Remove anything unverifiable.
7. Remove the draft fields, set `reading_time` and `date`.
8. Build locally if Jekyll is available (`bundle exec jekyll build`) and check the page
   renders: callouts, code blocks, the check-list, prev/next links.
9. Commit with a message like `devops/docker: write "Volumes — where your data lives"`.

Write one page per commit. Do not write several pages at once — depth suffers.

## Liquid gotchas

- Any `{{` in a code block (Go templates, Helm, Docker `--format`) must be wrapped in
  `{% raw %} … {% endraw %}` or Jekyll will try to evaluate it.
- Callouts are blockquotes followed by a kramdown attribute line: `{: .callout .callout-try}`.
- Headings get automatic ids; link to them with `#heading-text`.

## Adding or changing the structure

The curriculum lives in `_data/curriculum/<track>.yml`. Edit it, then run
`python3 scripts/scaffold.py <track>`. The script creates missing stubs and updates
navigation fields on existing pages; it never overwrites a page's body.
