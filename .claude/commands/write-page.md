---
description: Write one tutorial page completely, to the site's standard. Usage: /write-page _docker/running/01-volumes-and-data.md
---

Write the tutorial page at `$ARGUMENTS` — one page, completely, to the standard in
`CLAUDE.md` and the definition of done in `docs/page-checklist.md`. Read both files first.

Work through these phases in order. Do not skip a phase, and do not start writing
before phase 3 is complete.

## Phase 1 — Understand the brief (no writing yet)

1. Read the stub at `$ARGUMENTS`. Its `covers:` list is the minimum the page must
   explain; the finished page goes well beyond it.
2. Read the subject's outline in `_data/curriculum/<subject>.yml` and the stubs or
   pages immediately before and after this one in the same section, so the page starts
   where the previous one ends and does not repeat what the next one will cover.
3. Read one already-written page (for example `_docker/foundations/01-what-is-a-container.md`)
   to match the voice and structure.
4. Write down, as a list, every sub-topic a reader would need to go from knowing nothing
   about this topic to being able to explain it to a colleague and debug it at work:
   the problem, the mechanism, every mode/option/type, configuration, failure modes,
   limits, alternatives, security, vocabulary, version changes, and one expert-level
   section. This list is the outline. Show it before continuing.

## Phase 2 — Research (official sources only)

5. Open the official documentation for everything on the outline — the project's own
   docs, reference pages, specifications, man pages. Use web search or fetch; note the
   URL and the documented version for each. Do not rely on memory for any flag, default,
   path, config key or error message.
6. Where the docs are thin, read the project's source or changelog, and well-known
   long-form sources (the project's own blog, a maintainer's talk). Do not copy text.
7. Record what version of the tool you are documenting; this goes in the page's
   "Written against:" line.

## Phase 3 — Run everything

8. Set up what the page needs (Docker, a kind cluster, a VM — whatever applies) and run
   every command the page will show. Capture real output. If something cannot be run
   here, decide now whether to keep it (marked "not run here; from the official docs")
   or drop it.
9. Reproduce at least two of the failure modes the page will describe, so the error text
   and diagnosis are real.

## Phase 4 — Write

10. Write the page in the structure from `CLAUDE.md`: lead with "Written against:",
    everyday picture, what it actually is (the long part, with `###` subsections for each
    outline item), how it is used in practice, try it yourself, when it goes wrong, common
    mistakes, check your understanding (5–8 questions answered from the page), further
    reading (official docs first; only links you opened).
11. Plain language throughout: define every term where it first appears, one idea per
    paragraph, show before explain. No exam or interview framing.
12. Fill in front matter: one-sentence `description`, `reading_time` (words ÷ 200),
    today's `date`. Remove `draft: true`, `sitemap: false` and `covers:`. Do not change
    `section`, `section_order` or `order`.

## Phase 5 — Verify

13. Re-read the whole page as a sceptical expert whose job is to find something wrong.
    For every factual claim ask "where did I verify this?". Remove or fix anything you
    cannot defend. Check every code block for `{{` that needs `{% raw %}`.
14. Go through `docs/page-checklist.md` item by item against the finished page. Fix
    anything unticked. If coverage would need more than ~6,000 words, stop and propose a
    split in the curriculum instead of writing a shallow page.
15. If Jekyll is available (`bundle exec jekyll build`), build and open the page's HTML
    to confirm callouts, code blocks, the check-list and prev/next render.

## Phase 6 — Report and commit

16. Commit only this page (and the curriculum file if `description` was added there),
    with a message like `docker: write "Volumes — where your data actually lives"`.
17. Finish with the report described in section F of the checklist: versions used,
    commands not run, what the sceptical re-read removed, anything you are unsure of,
    and the checklist with every box marked.

Write one page per invocation. If asked to write several, do them one at a time, each
with all six phases.
