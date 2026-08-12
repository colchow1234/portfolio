# Colin Chow Portfolio — Site Conventions

Plain static HTML site (no build step, no framework). Each page is a
self-contained `.html` file with its own `<style>` and `<script>`.

## Page structure patterns

- `index.html` and `credits.html` use `<base href="/">` so all
  relative paths resolve from the site root regardless of URL.
  Individual project pages (under `project pages/`) do not — their
  asset paths are relative to their own file location.
- Pretty URLs (`/home`, `/credits`, `/sketchbook`) are backed by
  rewrites in both `vercel.json` (production) and `dev-server.py`
  (local preview) — add both when introducing a new pretty URL.
- Nav (`Work / About / Credits / Sketchbook`) and the mobile menu are
  duplicated per-page (no shared partial/include). Keep them in sync
  when adding a nav item.
