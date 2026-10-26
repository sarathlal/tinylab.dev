# tinylab.dev

Source for [tinylab.dev](https://tinylab.dev): plain-language tutorial tracks (DevOps, Linux, Python, Go, Rust, React) and a daily AI news brief, built with Jekyll.

- `bundle install && bundle exec jekyll serve` to run locally.
- One folder per subject (`_docker/`, `_kubernetes/`, …); every planned page exists as a stub file marked `draft: true`.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for site mechanics, [CLAUDE.md](CLAUDE.md) for the writing standard, and [docs/page-checklist.md](docs/page-checklist.md) for what "done" means. In Claude Code, `/write-page <path>` writes a page and `/review-page <path>` reviews it.
