# Good Default

Good Default is the Hugo-powered public site for `gooddefault.com`: a searchable catalog of better household defaults, comparison tools, and article guides formerly hosted on Substack.

This repo is the continuation of the older household product catalog project, with the site rebuilt around the Good Default name, domain, design, and catalog experience.

## Site Structure

- `hugo.toml` configures the Hugo site.
- `content/p/` contains migrated article posts at the former Substack `/p/...` slugs.
- `content/catalog/` and `content/compare/` define the catalog and comparison pages.
- `layouts/` contains the Hugo templates for the homepage, posts, catalog, compare, robots, and 404 pages.
- `static/llms.txt` provides an LLM-readable site summary.
- `static/CNAME` preserves the GitHub Pages custom domain.
- `dark-mode.css` adds `prefers-color-scheme: dark` support across the site.
- `data/products.csv` and `data/pfas-free-products.csv` contain the catalog seed data.
- `data/product-images.json` maps catalog rows to local product images in `assets/products/`.
- `scripts/sync-catalog-resources.py` mirrors catalog data into `assets/catalog/` for Hugo templates that render product picks.
- `scripts/check-internal-links.py` checks generated links, anchors, assets, and product-image references.

## Domains

- `gooddefault.com`: this static apex site.
- `www.gooddefault.com`: should point to the apex site.
- `blog.gooddefault.com`: should redirect or point to the Hugo site during final cutover so old `/p/...` paths continue to resolve.

The repo includes `static/CNAME` for GitHub Pages.

## Local Preview

Build with Hugo:

```sh
python3 scripts/sync-catalog-resources.py
hugo --cleanDestinationDir
hugo server --disableFastRender
```

Then open the local Hugo URL printed by the server.

## Checks

Run the generated-site link check before pushing:

```sh
python3 scripts/sync-catalog-resources.py
hugo --cleanDestinationDir --minify
CHECK_ROOT=public python3 scripts/check-internal-links.py
```

GitHub Actions builds the Hugo site, checks generated links, and deploys the `public/` artifact to GitHub Pages on pushes to `main`.
