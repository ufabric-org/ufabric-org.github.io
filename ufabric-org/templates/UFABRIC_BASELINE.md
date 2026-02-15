# uFabric Baseline Guidelines

This file is the canonical baseline for projects collaborating with uFabric.

## Scope

- Keep work public by default unless there is a legal or security reason not to.
- Document assumptions, constraints, and decisions in the repository.
- Prefer reproducible workflows (scripts, CI, and pinned tool versions when possible).

## Engineering

- Keep changes small, reviewable, and testable.
- Add or update tests when behavior changes.
- Use explicit versioning and changelogs for externally visible changes.
- Include rollback notes for risky changes.

## Documentation

- Maintain a `README.md` with setup, run, and test instructions.
- Keep architecture notes in `docs/` and update them with major changes.
- Record milestones and blockers in `ufabric-org/ufabric-progress.md`.

## Reporting

- Publish progress in `ufabric-org/ufabric-progress.md`.
- Update that file at least weekly.
- Use the template from:
  - `https://raw.githubusercontent.com/ufabric-org/ufabric.org/main/ufabric-org/templates/UFABRIC_PROGRESS_TEMPLATE.md`

## Compliance

- Respect the repository license and third-party licenses.
- Do not commit secrets.
- Follow responsible disclosure for vulnerabilities.
