# uFabric Project Sync Playbook

This document captures the operational order and prompts to run for project sync.

## Scope

- Central aggregator repository: `ufabric-org/ufabric.org`
- Project repositories: public existing, public new, and private

All official uFabric documentation must be in English.

## Recommended execution order

1. Run the appropriate prompt in each project repository.
2. For private projects, extract and sanitize the public snapshot markdown.
3. Update the central aggregator repository (`ufabric.org`) with source rows and snapshots.
4. Regenerate `content/projects.md`.
5. Review diff, then commit/push.

## Prompt A: Existing public project repository

```text
Align this existing public repository with uFabric project sync standards.

Hard requirements:
- All official uFabric documentation MUST be in English.
- Use `ufabric-org/` for uFabric standards (not `docs/`).

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
4. Refresh `ufabric-org/ufabric-progress.md` for the current reporting period.
5. Validate markdown consistency and show final diff.

Do not commit.
```

## Prompt B: New public project repository

```text
Initialize this new public repository for uFabric project sync.

Hard requirements:
- All official uFabric documentation MUST be in English.
- Use `ufabric-org/` for uFabric standards (not `docs/`).

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

## Prompt C: Private project repository

```text
Align this private repository with uFabric private-reporting standards and prepare sanitized public sync output.

Hard requirements:
- All official uFabric documentation MUST be in English.
- Use `ufabric-org/` for uFabric standards (not `docs/`).
- Never expose secrets, internal endpoints, credentials, or internal-only links.

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

## Prompt D: Central aggregator repository (`ufabric-org/ufabric.org`)

```text
Update the uFabric projects public feed from project sync sources.

Hard requirements:
- All official uFabric documentation MUST be in English.
- Keep website content (`content/`) separated from sync operations (`ufabric-org/projects-sync/`).

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

## Operational notes

- Public site page is generated at: `content/projects.md`
- Sync source of truth is: `ufabric-org/projects-sync/sources.md`
- Generator script: `ufabric-org/projects-sync/scripts/build_projects_page.py`
- New project setup guide: `ufabric-org/projects-sync/NEW_PROJECT_SETUP.md`
