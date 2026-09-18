# staple and go

A coloring picture site for my brother, served on GitHub Pages.

## Layout

- Sticky header ("staple and go")
- Coloring books section (click a cover to flip through and print it)
- Coloring pages section (click a page to view and print it, no book nav)

Each book or page opens a big print-ready view:
- **print book** — prints every page of the book
- **print page** — prints just the current page (`ctrl+p` works too)
- books have prev/next arrows; pages don't

## Serving on GitHub Pages

Enable Pages in the repo's **Settings → Pages** (source: branch, path `/`).
The site is plain static files, so it works from an `index.html` on
`gh-pages` or `main`, or from a `docs/` folder.

## Adding your own pictures

Drop photos into the `photos/` folders, then add one line to `data.js`:

- New book: add to `books` with a `cover` and `pages` array.
- New page: add to `pages` with a `name` and `src`.

Placeholder line-drawings live in `photos/` and can be regenerated with:

    python3 tools/gen_placeholders.py