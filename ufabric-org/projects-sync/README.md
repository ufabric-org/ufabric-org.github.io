# uFabric Projects Sync

This folder contains multi-project synchronization operations and internal coordination artifacts.

Public website content lives in `content/`.
Sync sources, reports, and generation logic live here under `ufabric-org/projects-sync/`.

This stack is only for `ufabric-org/ufabric.org` (`aggregator repo profile (multi-project feed)`).
Project repositories use `project repo profile (self-report only)` and maintain only their own `ufabric-org/ufabric-progress.md`.
If a project repository has `sources.md`, it must contain only one row for itself.

## Repository profiles

| Profile | Repository type | Responsibilities |
| --- | --- | --- |
| `project repo profile (self-report only)` | Any single project repository | Maintain project-local docs and its own `ufabric-org/ufabric-progress.md` only. |
| `aggregator repo profile (multi-project feed)` | `ufabric-org/ufabric.org` only | Maintain multi-project registry/snapshots and generate `content/projects.md`. |

## Scope

- Multi-project source registry for projects feed (`ufabric-org/ufabric.org` only).
- Public/private report snapshots managed by the aggregator.
- Generation script for `content/projects.md`.
- Operational docs for maintainers.

## Files

- `sources.md`: canonical registry consumed by the generator.
- `ufabric-org/projects-sync/scripts/build_projects_page.py`: builds `content/projects.md`.
- `reports/public/`: local public report snapshots.
- `reports/private/`: sanitized snapshots for private repos.
- `INTEGRATION.md`: integration model and onboarding notes.
- `MAINTENANCE_RULES.md`: ongoing operation rules.
- `NEW_PROJECT_SETUP.md`: checklist to initialize new projects.

## Run

From repository root:

```bash
make projects
```

This command applies to the `aggregator repo profile (multi-project feed)` only.
