# Projects Integration

Use this guide to connect any uFabric repository to the public `/projects/` page.

## Repository profiles

| Profile | Repository type | Responsibilities | Must not do |
| --- | --- | --- | --- |
| `project repo profile (self-report only)` | Any single project repository | Maintain only its own baseline/maintenance/progress docs. | Host multi-project aggregation assets or run federation workflows. |
| `aggregator repo profile (multi-project feed)` | `ufabric-org/ufabric.org` only | Maintain cross-project registry, snapshots, and generated projects page. | Push aggregation responsibilities into project repos. |

## 1. Baseline and reporting in each project repo (`project repo profile (self-report only)`)

Required paths in project repositories:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`

Canonical templates:

- [UFABRIC_BASELINE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md)
- [UFABRIC_PROGRESS_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md)
- [UFABRIC_MAINTENANCE_RULES_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md)

Project-repo scope rule:

- Keep reporting self-contained to the current repository only.
- If a project repository has `sources.md`, it must contain exactly one self row.

## 2. Register project source in this repository (`aggregator repo profile (multi-project feed)`)

Edit `ufabric-org/projects-sync/sources.md` and add one row.

Public repository example:

```md
| My Project | ufabric-org/my-project | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/public/my-project.md | public |
```

Private repository example:

```md
| My Private Project | ufabric-org/my-private-project | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/private/my-private-project.md | private |
```

This step is only performed in `ufabric-org/ufabric.org`.

## 3. Rebuild public page (`aggregator repo profile (multi-project feed)`)

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

## Migration note (incorrectly initialized project repos)

If a project repository was initialized as if it were an aggregator:

1. Remove or archive `ufabric-org/projects-sync/` and any cross-project snapshot files.
2. Keep only the project's own `ufabric-org/ufabric-progress.md` and companion docs.
3. If `sources.md` exists in the project repo, reduce it to one self row.
4. Move all multi-project aggregation rows/files to `ufabric-org/ufabric.org`.
