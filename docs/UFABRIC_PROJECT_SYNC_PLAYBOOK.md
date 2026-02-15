# uFabric Project Sync Playbook

This document captures the operational order and prompts to run for project sync.

## Scope

- Only `ufabric-org/ufabric.org` runs multi-project aggregation.
- Every project repository uses the `project repo profile (self-report only)`.
- A project repository maintains only its own `ufabric-org/ufabric-progress.md`.
- If a project repository has `sources.md`, it must contain exactly one row for itself.
- All official uFabric documentation must be in English.

## Repository profiles

| Profile | Repository type | Responsibilities | Must not do |
| --- | --- | --- | --- |
| `project repo profile (self-report only)` | Any single project repository (for example `ufabric-org/project-pulsar`) | Maintain `ufabric-org/UFABRIC_BASELINE.md`, `ufabric-org/ufabric-progress.md`, and `ufabric-org/UFABRIC_MAINTENANCE_RULES.md` for itself only. | Implement multi-project aggregation (`ufabric-org/projects-sync/`, multi-project `sources.md`, cross-project snapshots, `make projects` for federation). |
| `aggregator repo profile (multi-project feed)` | `ufabric-org/ufabric.org` only | Maintain `ufabric-org/projects-sync/sources.md`, keep public/private snapshots, and generate `content/projects.md`. | Treat project repositories as aggregator clones or require them to host cross-project sync assets. |

## Recommended execution order

1. Run the appropriate prompt in each project repository (Prompt A/B/C) using `project repo profile (self-report only)`.
2. For private projects, extract and sanitize the public snapshot markdown.
3. Update `ufabric-org/ufabric.org` (Prompt D) using `aggregator repo profile (multi-project feed)`.
4. Regenerate `content/projects.md` in `ufabric-org/ufabric.org`.
5. Review diff, then commit/push.

## Prompt A: Existing public project repository (`project repo profile (self-report only)`)

```text
Use the project repo profile (self-report only).
Align this existing public repository with uFabric project-reporting standards.

Hard requirements:
- Profile: `project repo profile (self-report only)`.
- All official uFabric documentation MUST be in English.
- Use `ufabric-org/` for uFabric standards (not `docs/`).
- Do not implement aggregator stack assets (`ufabric-org/projects-sync/`, cross-project snapshots, or multi-project generators).
- If `sources.md` exists in this repository, keep only one row for this repository.

Tasks:
1. Ensure these files exist and are up to date:
   - `ufabric-org/UFABRIC_BASELINE.md`
   - `ufabric-org/ufabric-progress.md`
   - `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`
2. Update those files using canonical templates from:
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md
3. Ensure `README.md` links to:
   - `ufabric-org/UFABRIC_BASELINE.md`
   - `ufabric-org/ufabric-progress.md`
   - `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`
4. Refresh this repository's own `ufabric-org/ufabric-progress.md` for the current reporting period.
5. Validate markdown consistency and show final diff.

Do not commit.
```

## Prompt B: New public project repository (`project repo profile (self-report only)`)

```text
Use the project repo profile (self-report only).
Initialize this new public repository for uFabric project reporting.

Hard requirements:
- Profile: `project repo profile (self-report only)`.
- All official uFabric documentation MUST be in English.
- Use `ufabric-org/` for uFabric standards (not `docs/`).
- Do not implement aggregator stack assets (`ufabric-org/projects-sync/`, cross-project snapshots, or multi-project generators).
- If `sources.md` exists in this repository, keep only one row for this repository.

Tasks:
1. Create `ufabric-org/` and add:
   - `ufabric-org/UFABRIC_BASELINE.md`
   - `ufabric-org/ufabric-progress.md`
   - `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`
2. Populate files from canonical templates:
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md
3. Fill initial project metadata in `ufabric-org/ufabric-progress.md`.
4. Update `README.md` to include links to the 3 files in `ufabric-org/`.
5. Validate markdown consistency and show final diff.

Do not commit.
```

## Prompt C: Private project repository (`project repo profile (self-report only)`)

```text
Use the project repo profile (self-report only).
Align this private repository with uFabric private-reporting standards and prepare sanitized public sync output.

Hard requirements:
- Profile: `project repo profile (self-report only)`.
- All official uFabric documentation MUST be in English.
- Use `ufabric-org/` for uFabric standards (not `docs/`).
- Never expose secrets, internal endpoints, credentials, or internal-only links.
- Do not implement aggregator stack assets (`ufabric-org/projects-sync/`, cross-project snapshots, or multi-project generators).
- If `sources.md` exists in this repository, keep only one row for this repository.

Tasks (inside the private repository):
1. Ensure these files exist and are up to date:
   - `ufabric-org/UFABRIC_BASELINE.md`
   - `ufabric-org/ufabric-progress.md` (canonical full private report)
   - `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`
2. Sync content from canonical templates:
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md
   - https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md
3. Update `README.md` links to these files under `ufabric-org/`.
4. Create a sanitized public snapshot markdown named `<project-name>.md` (no secrets) suitable for publication in:
   - `ufabric-org/projects-sync/reports/private/<project-name>.md` (in ufabric.org repo)
5. Add a "Sanitization checklist" section in the snapshot confirming sensitive data was removed.
6. Show:
   - final diff in this private repo
   - final sanitized snapshot content ready to copy to ufabric.org repo

Do not commit.
```

## Prompt D: Central aggregator repository (`aggregator repo profile (multi-project feed)`)

```text
Use the aggregator repo profile (multi-project feed).
Update the uFabric projects public feed from project sync sources.

Hard requirements:
- Profile: `aggregator repo profile (multi-project feed)`.
- All official uFabric documentation MUST be in English.
- Keep website content (`content/`) separated from sync operations (`ufabric-org/projects-sync/`).
- This is the only repository allowed to maintain multi-project `sources.md` and run `make projects` for cross-project aggregation.

Tasks:
1. Review and update `ufabric-org/projects-sync/sources.md`.
2. For public projects, update snapshots under:
   - `ufabric-org/projects-sync/reports/public/`
3. For private projects, update sanitized snapshots under:
   - `ufabric-org/projects-sync/reports/private/`
4. Run `make projects`.
5. Verify generated output in `content/projects.md`.
6. Show final diff and validations.

Do not commit.
```

## Migration note (for incorrectly initialized repositories)

If a project repository was initialized with aggregator artifacts, migrate it to `project repo profile (self-report only)`:

1. Remove or archive cross-project assets (`ufabric-org/projects-sync/`, cross-project snapshots, multi-project generator scripts).
2. Keep only project-local reporting docs under `ufabric-org/`.
3. If `sources.md` exists in the project repo, reduce it to a single self row.
4. Move multi-project rows and snapshots to `ufabric-org/ufabric.org`, then run `make projects` there.

## Operational notes

- Public site page is generated at: `content/projects.md`
- Sync source of truth is: `ufabric-org/projects-sync/sources.md`
- Generator script: `ufabric-org/projects-sync/scripts/build_projects_page.py`
- New project setup guide: `ufabric-org/projects-sync/NEW_PROJECT_SETUP.md`
- Project repositories are self-report only and do not host multi-project aggregation.
