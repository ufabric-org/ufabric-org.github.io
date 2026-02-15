# uFabric Maintenance Rules (Project Repository)

This file defines how this repository stays aligned with uFabric baseline and reporting.

## Required files

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md` (this file)

## Baseline update rule

- Baseline source:
  - `https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_BASELINE.md`
- Update `ufabric-org/UFABRIC_BASELINE.md` when requested by maintainers or when the agent detects drift.

## Progress update rule

- Update `ufabric-org/ufabric-progress.md` at least weekly.
- Required sections:
  - Done
  - In Progress
  - Next
  - Blockers
  - Links

## Status meaning

- `on-track`: planned work is progressing with no critical blockers.
- `at-risk`: delivery risk exists and needs mitigation.
- `blocked`: progress cannot continue until dependency is resolved.

## Private reporting rule

If this repository is private and reports to a public uFabric feed:

- Keep the canonical report private in `ufabric-org/ufabric-progress.md`.
- Publish a sanitized snapshot markdown (without secrets) to the public aggregator repository.
- Ensure that public snapshot excludes private infrastructure details and internal links.

## Agent trigger phrases

Use one of these prompts in this repository:

- `Refresh ufabric-org/UFABRIC_BASELINE.md from ufabric.org template`
- `Update ufabric-org/ufabric-progress.md for the current reporting period`
- `Check repo against uFabric maintenance rules and propose required edits`

## README links rule

README must always link to:

- `ufabric-org/UFABRIC_BASELINE.md`
- `ufabric-org/ufabric-progress.md`
- `ufabric-org/UFABRIC_MAINTENANCE_RULES.md`
