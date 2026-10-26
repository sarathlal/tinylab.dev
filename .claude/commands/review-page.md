---
description: Independently review a written tutorial page for accuracy, completeness and readability. Usage: /review-page _docker/running/01-volumes-and-data.md
---

Review the tutorial page at `$ARGUMENTS` as a demanding expert in its subject who did
not write it and has no stake in it. Your job is to find what is wrong, missing or
unclear — not to praise it. Read `CLAUDE.md` and `docs/page-checklist.md` first.

Do the review in this order and report findings under these headings.

## 1. Accuracy (most important)

- For every command on the page, run it. Compare the real output with what the page
  shows. Report any difference, however small.
- For every flag, option, default, path, config key and error message, check the
  official documentation for the version named in the page's "Written against:" line.
  Report anything that does not match, is deprecated, or does not exist.
- For every factual statement about how the thing works, ask whether it is true as
  written. Report overstatements, half-truths and anything that is true only in some
  versions or configurations without saying so.
- Check the analogy: does it map to the mechanism? Does the page say where it breaks?
- Open every link in Further reading. Report dead or non-official links.

List each problem as: **location** (heading or quoted phrase) → **what is wrong** →
**what it should say** (with the source you checked).

## 2. Completeness

Using section A of `docs/page-checklist.md`, list what a reader would still not know
about this topic after finishing the page. Be specific: name the option, failure mode,
alternative, term or version change that is missing. Compare against the official
documentation's table of contents for the topic — anything there that the page does not
mention is a candidate.

## 3. Readability for a non-technical reader

- Mark any term used before it is defined.
- Mark any paragraph that carries more than one idea, or any sentence a careful
  non-technical reader would need to read twice.
- Mark any exam, quiz or interview framing.
- Check that the "Try it yourself" steps can be followed exactly as written on a
  laptop, with the expected output shown.

## 4. Structure and mechanics

Check sections C, D and E of the checklist: section order, check-your-understanding
questions answered from the page, front matter complete and draft fields removed,
`{% raw %}` where needed, links to neighbouring pages correct.

## 5. Verdict

End with one of:
- **Ready** — no accuracy problems; completeness gaps, if any, are minor and listed.
- **Fix and re-review** — accuracy problems found (list them first) or major gaps.

Then, if asked to fix: make only the changes your review calls for, re-run any command
you changed, and report what changed. Do not rewrite sections that were correct.
