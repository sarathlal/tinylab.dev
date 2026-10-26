#!/usr/bin/env python3
"""
Generate stub tutorial pages from a curriculum file.

    python3 scripts/scaffold.py devops          # create missing stubs for _devops/
    python3 scripts/scaffold.py devops --check  # report drift, write nothing

Reads _data/curriculum/<track>.yml and, for every page it lists, ensures a
file exists at _<track>/<folder>/NN-<slug>.md. Existing files are NEVER
overwritten; only their navigation fields (section, section_order, order)
are updated so the site order always follows the curriculum.

A stub page has `draft: true`. The site shows drafts as "coming soon"
(no link) and leaves them out of search and the sitemap. Writing the page
means replacing the stub body and removing `draft: true`.

Requires PyYAML (pip install pyyaml).
"""
import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def load_curriculum(track):
    path = ROOT / "_data" / "curriculum" / f"{track}.yml"
    if not path.exists():
        sys.exit(f"No curriculum at {path}")
    return yaml.safe_load(path.read_text())


def stub_body(page, section):
    covers = page.get("covers") or []
    lines = [
        "This page has not been written yet. Here is what it will cover when it is:",
        "",
    ]
    for c in covers:
        lines.append(f"- {c}")
    if not covers:
        lines.append("- (outline to be added)")
    lines += [
        "",
        "> **Note**",
        "> Want this page sooner? Open an issue or a pull request on "
        "[GitHub](https://github.com/sarathlal/tinylab.dev) — the outline above is the brief.",
        "{: .callout .callout-note}",
        "",
    ]
    return "\n".join(lines)


def front_matter(page, section, section_order, order, track):
    fm = {
        "title": page["title"],
        "description": page.get("description", ""),
        "section": section["name"],
        "section_order": section_order,
        "order": order,
        "level": page.get("level", "foundation"),
        "draft": True,
        "sitemap": False,
        "date": date.today().isoformat(),
    }
    if page.get("lab"):
        fm["lab"] = True
    if page.get("covers"):
        fm["covers"] = page["covers"]
    return fm


def dump_fm(fm):
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000).rstrip() + "\n---\n"


def update_nav_fields(text, section, section_order, order):
    """Rewrite only section/section_order/order in an existing file's front matter."""
    m = FM_RE.match(text)
    if not m:
        return text, False
    fm = yaml.safe_load(m.group(1)) or {}
    new = dict(fm)
    new["section"] = section["name"]
    new["section_order"] = section_order
    new["order"] = order
    if new == fm:
        return text, False
    return dump_fm(new) + text[m.end():], True


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    track = sys.argv[1]
    check = "--check" in sys.argv
    cur = load_curriculum(track)
    base = ROOT / f"_{track}"
    base.mkdir(exist_ok=True)

    created, updated, kept = [], [], []
    seen = set()

    for s_idx, section in enumerate(cur["sections"], start=1):
        folder = base / section["folder"]
        folder.mkdir(exist_ok=True)
        for p_idx, page in enumerate(section["pages"], start=1):
            slug = page["slug"]
            # find an existing file for this slug regardless of its NN- prefix
            existing = sorted(folder.glob(f"*-{slug}.md")) + sorted(folder.glob(f"{slug}.md"))
            if existing:
                path = existing[0]
                text = path.read_text()
                new_text, changed = update_nav_fields(text, section, s_idx, p_idx)
                if changed:
                    updated.append(path)
                    if not check:
                        path.write_text(new_text)
                else:
                    kept.append(path)
            else:
                path = folder / f"{p_idx:02d}-{slug}.md"
                created.append(path)
                if not check:
                    fm = front_matter(page, section, s_idx, p_idx, track)
                    path.write_text(dump_fm(fm) + "\n" + stub_body(page, section))
            seen.add(path.resolve())

    # files on disk that the curriculum doesn't mention
    orphans = [
        p for p in base.rglob("*.md")
        if p.resolve() not in seen and p.name != "index.md"
    ]

    verb = "would create" if check else "created"
    print(f"{verb}: {len(created)}  nav-updated: {len(updated)}  unchanged: {len(kept)}  orphans: {len(orphans)}")
    for p in created:
        print(f"  + {p.relative_to(ROOT)}")
    for p in updated:
        print(f"  ~ {p.relative_to(ROOT)}")
    for p in orphans:
        print(f"  ? {p.relative_to(ROOT)}  (not in curriculum)")


if __name__ == "__main__":
    main()
