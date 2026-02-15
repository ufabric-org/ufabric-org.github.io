# New Project Setup

Use this checklist to initialize a new uFabric project so it can be integrated into the `/projects/` feed.

## Step 1. Initialize required files in the project repository

Create the `ufabric-org/` folder and add:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`

Use these templates:

- [UFABRIC_BASELINE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md)
- [UFABRIC_PROGRESS_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md)
- [UFABRIC_MAINTENANCE_RULES_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md)

## Step 2. Add README links in the project repository

Ensure README links to:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`

## Step 3. Register the project in this repository

Add one row to `ufabric-org/projects-sync/sources.md`.

Public project example:

```md
| project-name | ufabric-org/project-name | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/public/project-name.md | public |
```

Private project example:

```md
| project-name | ufabric-org/project-name | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/private/project-name.md | private |
```

## Step 4. Add snapshot markdown in this repository

- Public source snapshot: `ufabric-org/projects-sync/reports/public/project-name.md`
- Private sanitized snapshot: `ufabric-org/projects-sync/reports/private/project-name.md`

## Step 5. Rebuild and verify

From repository root:

```bash
make projects
```

Check generated output:

- `content/projects.md`
