# Definition of done for a tutorial page

A page is finished only when every box below is ticked. `/write-page` works through this
list; `/review-page` checks it independently. Copy the list into the final report and
mark each item.

## A. Coverage — zero to expert on this one topic

The reader who finishes this page knows everything a working engineer knows about the
topic. Check each against the page:

- [ ] **Problem** — what the topic exists to solve, with a concrete before/after.
- [ ] **Mechanism** — how it works underneath: every named component, what calls what,
      what is stored where, what happens step by step. No hand-waving ("Docker handles it").
- [ ] **Everyday use** — the commands, files, flags and options people actually use,
      each shown with real output.
- [ ] **Every option that matters** — the full set of modes/types/strategies for the
      topic (e.g. for volumes: named, anonymous, bind, tmpfs, drivers), not just the
      common one, with when to use each.
- [ ] **Configuration** — the config keys, defaults, and where they live.
- [ ] **Failure modes** — the errors the reader will actually hit, the exact message
      text where known, the cause of each, and how to diagnose it.
- [ ] **Limits and trade-offs** — what it cannot do, where it is slow, what it costs,
      and when not to use it.
- [ ] **Alternatives** — the other tools/approaches for the same job and how they differ.
- [ ] **Security** — any security implication of the topic (permissions, exposure,
      secrets, escapes), stated plainly.
- [ ] **Vocabulary** — every term the reader will meet in official docs for this topic
      is defined on the page.
- [ ] **History/versions** — what changed in recent versions that affects the reader
      (deprecated flags, renamed features), with the version noted.
- [ ] **Expert corner** — at least one section that goes deeper than most tutorials
      (internals, edge cases, performance, "how would you know if…").
- [ ] **Every item in the stub's `covers:` list** is covered, and the page goes beyond it.

## B. Accuracy — nothing on the page is unverified

- [ ] **Every command was run** in the writing environment, and the output shown is
      real (trimmed is fine, invented is not). Commands that could not be run are
      marked "not run here; from the official documentation" in the page.
- [ ] **Every flag, option, path, default and config key** was checked against the
      official documentation, and the page notes the version checked.
- [ ] **A "Written against:" line** near the top names the tool version(s) used.
- [ ] **No invented** error messages, numbers, benchmarks, history, quotes or
      "best practices". Anything uncertain was removed or marked as unverified.
- [ ] **Facts and opinions are separated** — recommendations say why and when not.
- [ ] **The analogy is true** — it maps to the mechanism and the page says where it breaks.
- [ ] **Further reading links were opened** and are the official docs first.
- [ ] **A sceptical re-read was done** at the end, looking for anything wrong, and the
      report lists what was changed or removed as a result.

## C. Readability — a non-technical reader can follow it

- [ ] Opens with 2–4 sentences on what the page answers and what the reader will be able
      to do.
- [ ] One everyday analogy early, then the real mechanism.
- [ ] Every term defined in the sentence where it first appears.
- [ ] Sentences mostly under 25 words; one idea per paragraph; no filler.
- [ ] Show-then-explain: concrete example before the abstract rule.
- [ ] No exam, quiz-show or interview framing anywhere.

## D. Hands-on

- [ ] A "Try it yourself" exercise the reader can do on a laptop in under an hour, with
      expected output at each step.
- [ ] At least one "break it and fix it" step.
- [ ] A "When it goes wrong" section walking through real failures.

## E. Structure and mechanics

- [ ] Sections in the order given in `CLAUDE.md`; none of 5, 7, 8, 9 skipped.
- [ ] "Check your understanding": 5–8 `<details>` questions whose answers come from the page.
- [ ] Front matter complete: `title`, `description` (one sentence), `section`,
      `section_order`, `order` (unchanged from the stub), `level`, `reading_time`, `date`.
- [ ] `draft: true`, `sitemap: false` and `covers:` removed.
- [ ] Any `{{` inside code is wrapped in `{% raw %}…{% endraw %}`.
- [ ] Links to neighbouring pages use the site's URL layout (`/learn/<subject>/<section>/NN-slug/`).
- [ ] Word count is at least 2,500 excluding code. If the topic needed more than ~6,000
      words, the report proposes a split instead of a shallow page.

## F. Report

The final message of a writing session lists:
1. The version(s) the page was written against.
2. Commands that could not be run, and why.
3. Anything removed in the sceptical re-read.
4. Anything the writer is still unsure about (so the owner can check it).
5. This checklist with every box marked.
