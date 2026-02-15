# uFabric Projects Sync

This folder contains project synchronization operations and internal coordination artifacts.

Public website content lives in `content/`.
Sync sources, reports, and generation logic live here under `ufabric-org/projects-sync/`.

## Scope

- Source registry for projects feed.
- Public/private report snapshots.
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
