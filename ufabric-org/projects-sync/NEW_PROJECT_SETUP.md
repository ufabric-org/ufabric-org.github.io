# New Project Setup

Use this checklist to initialize a new uFabric project so it can be integrated into the `/projects/` feed.

## Repository profiles

| Profile | Repository type | Responsibilities | Must not do |
| --- | --- | --- | --- |
| `project repo profile (self-report only)` | Any single project repository | Maintain only project-local reporting docs under `ufabric-org/`. | Implement multi-project registry/snapshot/generation flows. |
| `aggregator repo profile (multi-project feed)` | `ufabric-org/ufabric.org` only | Register project rows, store snapshots, and generate `/projects/`. | Delegate multi-project aggregation ownership to project repos. |

## Step 1. Initialize required files in the project repository (`project repo profile (self-report only)`)

Create the `ufabric-org/` folder and add:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`

Use these templates:

- [UFABRIC_BASELINE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md)
- [UFABRIC_PROGRESS_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md)
- [UFABRIC_MAINTENANCE_RULES_TEMPLATE.md](https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_MAINTENANCE_RULES_TEMPLATE.md)

## Step 2. Add README links in the project repository (`project repo profile (self-report only)`)

Ensure README links to:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`

Project-repo scope rule:

- Keep only self-reporting content in project repos.
- If `sources.md` exists in the project repo, it must contain only one self row.

## Step 3. Register the project in this repository (`aggregator repo profile (multi-project feed)`)

Add one row to `ufabric-org/projects-sync/sources.md`.

Public project example:

```md
| project-name | ufabric-org/project-name | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/public/project-name.md | public |
```

Private project example:

```md
| project-name | ufabric-org/project-name | main | ufabric-org/ufabric-progress.md | ufabric-org/projects-sync/reports/private/project-name.md | private |
```

This step runs only in `ufabric-org/ufabric.org`.

## Step 4. Add snapshot markdown in this repository (`aggregator repo profile (multi-project feed)`)

- Public source snapshot: `ufabric-org/projects-sync/reports/public/project-name.md`
- Private sanitized snapshot: `ufabric-org/projects-sync/reports/private/project-name.md`

## Step 5. Rebuild and verify (`aggregator repo profile (multi-project feed)`)

From repository root:

```bash
make projects
```

Check generated output:

- `content/projects.md`

## Migration note (incorrectly initialized project repos)

If a project repo was initialized with aggregator artifacts:

1. Remove or archive `ufabric-org/projects-sync/` and cross-project snapshot files from that project repo.
2. Keep only project-local `ufabric-org/` reporting files.
3. If `sources.md` exists there, keep one self row only.
4. Move aggregation rows/snapshots into `ufabric-org/ufabric.org`.
