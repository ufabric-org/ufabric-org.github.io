# uFabric Projects Sync Maintenance Rules

These rules govern how project feed synchronization is operated.

## Repository profiles

| Profile | Repository type | Responsibilities | Must not do |
| --- | --- | --- | --- |
| `project repo profile (self-report only)` | Any single project repository | Keep only project-local reporting docs (`ufabric-org/ufabric-progress.md` and related files). | Host multi-project `projects-sync` assets or maintain cross-project rows. |
| `aggregator repo profile (multi-project feed)` | `ufabric-org/ufabric.org` only | Maintain cross-project registry/snapshots and generate `content/projects.md`. | Require project repos to run `make projects` for federation. |

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

Project repository scope rule:

- Project repos are self-report only and keep only their own `ufabric-org/ufabric-progress.md`.
- If a project repo has `sources.md`, it must contain exactly one self row.

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

## Migration note (incorrectly initialized project repos)

If a project repository contains aggregator assets, migrate it by:

1. Removing or archiving `ufabric-org/projects-sync/` and cross-project snapshots from that project repo.
2. Keeping only project-local docs under `ufabric-org/`.
3. Reducing any local `sources.md` to a single self row.
4. Managing all multi-project rows/snapshots exclusively in `ufabric-org/ufabric.org`.
