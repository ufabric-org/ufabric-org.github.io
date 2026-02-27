# Agent Instructions

This repository contains the sources for the https://ufabric.org website.
It follows the `AGENTS.md` convention described at https://agents.md/.

## Start here

- Project overview: `README.md`
- Website content: `content/`
- Projects feed aggregation: `ufabric-org/projects-sync/`
- Operations/playbook: `docs/UFABRIC_PROJECT_SYNC_PLAYBOOK.md`
- Polaris alignment pin + sync notes: `POLARIS_REVISION`
- Vendored skills (upstream-managed copies):
  - Codex: `./.agents/skills/`
  - Antigravity: `./.agent/skills/`
  - Claude Code: `./.claude/skills/`

## Quick commands

- Serve locally (Docsify): `make serve`
- Rebuild projects feed: `make projects`
- Script help: `python3 ufabric-org/projects-sync/scripts/build_projects_page.py --help`

## Conventions (repo-specific)

- Language: English-first for long-lived docs, folder names, and filenames.
- Upstream-managed rule: do not edit vendored skills locally; update Polaris first, then re-copy/sync (see `POLARIS_REVISION`).
- Safety: never introduce secrets; avoid destructive operations unless explicitly requested.

## Repository map (high level)

- `content/`: website Markdown content (includes generated `content/projects.md`)
- `ufabric-org/projects-sync/`: scripts + docs for aggregating public project reports
- `docs/`: operational docs and playbooks

## Derived agent artifacts (optional)

If this repo maintains derived agent-facing docs (for example under `agentic/`), keep them in sync with the human sources of truth and document the refresh procedure.

