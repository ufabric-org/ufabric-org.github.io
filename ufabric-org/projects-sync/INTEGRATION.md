# Projects Integration

Use this guide to connect any uFabric repository to the public `/projects/` page.

## 1. Baseline and reporting in each project repo

Required paths in project repositories:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`

Canonical templates:

- [UFABRIC_BASELINE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md)
- [UFABRIC_PROGRESS_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md)
- [UFABRIC_MAINTENANCE_RULES_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md)

## 2. Register project source in this repository

Edit `ufabric-org/projects-sync/sources.md` and add one row.

Public repository example:

```md
| My Project | ufabric-org/my-project | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/public/my-project.md | public |
```

Private repository example:

```md
| My Private Project | ufabric-org/my-private-project | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/private/my-private-project.md | private |
```

## 3. Rebuild public page

From repository root:

```bash
make projects
```

This regenerates `content/projects.md`.

## 4. Private repository reporting

Private repositories cannot expose raw report markdown publicly.
Use a sanitized snapshot workflow:

1. Keep canonical report in the private repo: `ufabric-org/ufabric-progress.md`.
2. Create sanitized snapshot markdown with no secrets.
3. Store snapshot in this repo under `ufabric-org/projects-sync/reports/private/`.
4. Set `visibility` to `private` in `sources.md`.
5. Rebuild `content/projects.md`.
