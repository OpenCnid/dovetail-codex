# Codex lever catalog

Use this catalog only after classifying the problem. Prefer an observed surface;
mark documentary-only surfaces and verify them before making them load-bearing.

## Knowledge

- Read repository files with `rg`, `rg --files`, and focused file inspection.
- Use an available connector or MCP resource for private semantic data.
- Browse primary sources for current public facts and version-sensitive docs.
- Use a bounded subagent for an independent evidence pass.

## Purpose

- Ask the user for the missing choice when alternatives materially change the
  outcome.
- Express acceptance conditions in the current task, not in standing config.
- Use a plan when three or more dependent implementation steps need visible
  state.

## State

- Repository state: files, git status, tests, and command output.
- Current collaboration state: `list_agents`, `wait_agent`, and returned reports.
- User-owned long-running state: Codex tasks and automations, only when the user
  requests those lifecycle changes.
- External state: purpose-built apps, connectors, APIs, or CLIs.

## Approaches

- `AGENTS.md`: compact standing repository invariants, inherited root-to-CWD.
- `SKILL.md`: reusable conditional workflow, read in full on activation.
- `references/`: rare or branch-specific depth.
- `agents/openai.yaml`: UI metadata and implicit/explicit invocation policy.
- `.codex-plugin/plugin.json`: package component discovery.
- marketplace: installation and availability.
- `collaboration.spawn_agent`: live bounded delegation.
- `fork_turns`: conversation-context boundary; it does not isolate files.
- `codex exec`: repeatable noninteractive runs and structured result capture.

## Resources

Add a new resource only when the existing inventory cannot perform the action:

- a script for deterministic local transformation;
- a connector or MCP server for an otherwise unreachable service;
- a plugin component for reusable packaged capability;
- an explicit permission change for an action already authorized by the user.

Never use resource acquisition to decide an unresolved purpose question.
