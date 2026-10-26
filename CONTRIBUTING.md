# Writing for TinyLab

## Site structure

```
_config.yml          site settings; one `collections:` entry per learning track
_data/navigation.yml header links
_data/tracks.yml     learning tracks shown on /learn/ (title, tagline, status)
_devops/             the DevOps track (a Jekyll collection)
  index.md           track landing page (no `section` → treated as the index)
  docker/01-….md     one page per topic, grouped by `section`
_ai_news/            daily AI brief (collection)
_posts/              ordinary blog posts
_layouts/tutorial.html   sidebar + content + prev/next for track pages
_includes/           sidebar, pager, toc, callouts, track grid
_templates/          copy-and-fill page template
assets/css/site.css  site styles (on top of Pico CSS)
assets/css/syntax.css code highlighting for light and dark themes
search.json/search.md client-side search over all tracks
```

## The curriculum is the source of truth

Each track's structure lives in `_data/curriculum/<track>.yml`: sections, pages, levels and
a `covers:` outline per page. `python3 scripts/scaffold.py <track>` generates a stub for every
page that does not exist yet (`draft: true`, shown on the site as "coming soon" with its
outline) and keeps navigation fields in sync. It never overwrites a written page.

To add a page or section, edit the curriculum file and run the script. To write a page,
replace the stub's body and remove `draft: true` / `sitemap: false` / `covers:`.
See `CLAUDE.md` for the writing standard every page must meet.

## Adding a page to an existing track

1. Add it to `_data/curriculum/<track>.yml` and run `python3 scripts/scaffold.py <track>`
   (or copy `_templates/tutorial-page.md` by hand for a track without a curriculum file).
2. Fill in the front matter. The three fields that control navigation:
   - `section` — sidebar group. Must match other pages in the section exactly.
   - `section_order` — position of the section in the track. Same value on every page of the section.
   - `order` — position of the page inside its section.
3. Keep the five-part shape: everyday picture → what it actually is → try it → common mistakes → check your understanding.
4. Callouts are blockquotes with a kramdown class:

   ```markdown
   > **Try it yourself**
   > Commands here.
   {: .callout .callout-try}
   ```

   Types: `callout-analogy`, `callout-try`, `callout-check`, `callout-mistake`, `callout-note`.
5. If a code block contains `{{` (Go templates, Helm), wrap it in `{% raw %} … {% endraw %}` or Liquid will try to render it.

The file name prefix (`01-`) only keeps files sorted in your editor; the site orders by front matter.

## Adding a new track (Python, Go, Rust, React, Linux …)

1. Create `_data/curriculum/<track>.yml` (copy the DevOps one as a model) and the folder `_<track>/` with an `index.md` (no `section` field; set `permalink: /learn/<track>/`; include `{% raw %}{% include track-contents.html track="<track>" %}{% endraw %}`).
2. In `_config.yml`, add the collection and a default:

   ```yaml
   collections:
     python:
       output: true
       permalink: /learn/python/:path/
   defaults:
     - scope: { path: "", type: python }
       values: { layout: tutorial, track: python }
   ```

3. In `_data/tracks.yml`, set the track's `status` to `active` (or add it).
4. Run `python3 scripts/scaffold.py <track>`. The sidebar, contents, prev/next, learn hub and search pick it up automatically.

## Levels

- `foundation` — assumes nothing beyond basic terminal use.
- `intermediate` — assumes the foundation pages; what you need to use the tool well at work.
- `advanced` — internals, design and scale; for when you want to know *why*, not just *how*.

The site is a learning kit, not exam or interview material. Never frame a page around "what they ask you"; explain the thing, let the reader try it, then ask questions whose answers are in the page.

## Running locally

```bash
bundle install
bundle exec jekyll serve --livereload
# open http://localhost:4000
```

## Style

- Short sentences. One idea per paragraph. Plain words over jargon; when a term is unavoidable, define it the first time.
- One analogy per page, stretched only as far as it stays true.
- Every command shown should have been run. Show expected output where it helps.
- Prefer official documentation in "Further reading".
