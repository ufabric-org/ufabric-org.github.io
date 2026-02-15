# uFabric Projects Sync Maintenance Rules

These rules govern how project feed synchronization is operated.

## Source of truth

- Registry: `ufabric-org/projects-sync/sources.md`
- Generator: `ufabric-org/projects-sync/scripts/build_projects_page.py`
- Public output: `content/projects.md`

## Registry schema

`ufabric-org/projects-sync/sources.md` must include these columns:

- `name`
- `repo`
- `branch`
- `report_path`
- `local_path`
- `visibility` (`public` or `private`)

## Refresh triggers

Rebuild `content/projects.md` when any of the following happens:

- A tracked project updates `ufabric-org/ufabric-progress.md`.
- A row is added/edited/removed in `sources.md`.
- A private snapshot is updated.
- A maintainer requests manual sync.

## Standard procedure

1. Update `ufabric-org/projects-sync/sources.md` and/or snapshot files.
2. Run `make projects`.
3. Review `content/projects.md` output.
4. Commit source changes and generated output together.

## Validation

- `python3 -m py_compile ufabric-org/projects-sync/scripts/build_projects_page.py`
- `make projects`

## Private project constraints

For `visibility=private` entries:

- `local_path` must point to a sanitized snapshot in this repo.
- Snapshot must not include secrets, internal endpoints, or internal-only links.
- Keep the canonical full report only in the private repository.
