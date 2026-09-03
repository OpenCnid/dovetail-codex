---
name: spark-steering
description: Diagnose a stuck or drifting Codex workflow by locating the wrong control surface, lifecycle, or owner before adding tools or permissions. Invoke explicitly.
license: CC-BY-4.0
---

# Spark Steering

Find the smallest native lever that changes the system at the layer where the
problem actually lives.

## Start with one identification

Before proposing a fix, state in one sentence:

> `{Observed symptom}` is primarily a `{K|P|S|A|R}` problem because
> `{evidence that separates it from the neighboring axes}`.

The axes are:

- **K — knowledge:** the necessary facts are missing or unreliable.
- **P — purpose:** the desired outcome, tradeoff, or acceptance condition is
  unresolved.
- **S — state:** the system cannot observe or persist the relevant current state.
- **A — approaches:** the work is owned, routed, sequenced, or checked wrongly.
- **R — resources:** no available primitive can perform the work within the
  current permissions and environment.

Do not call a problem R until you have inventoried the current Codex surfaces.
Most apparent resource gaps are A: a capability exists but sits at the wrong
lifecycle or has the wrong owner.

## Inventory the native surfaces

Use the surface names, not an imagined replacement system:

| Need | First surface to inspect |
|---|---|
| Repository-wide standing guidance | root-to-CWD `AGENTS.md` chain |
| Reusable conditional procedure | plugin skill `SKILL.md` |
| Skill UI or explicit-only routing | `agents/openai.yaml` |
| Package discovery and distribution | `.codex-plugin/plugin.json`, marketplace |
| One-turn execution | current prompt plus available tools |
| Parallel bounded investigation | `collaboration.spawn_agent` |
| Clean conversation context | `fork_turns: "none"` |
| Continuity with prior turns | `fork_turns: "all"` or a positive turn count |
| Long-lived user-owned work | a separate Codex task, only when requested |
| External account or service | an available app, connector, CLI, or MCP server |
| Deterministic batch evaluation | `codex exec` with structured output options |

Read `references/steer-1-levers.md` only when the choice between surfaces is
unclear. Read `references/steer-3-costs.md` only when comparing prompt rent,
installation cost, or operational risk.

## Apply the cheapest sufficient move

Use this order:

1. **Ask.** If purpose or authority is unresolved, request the missing decision.
2. **Name.** Refer to an existing primitive explicitly so Codex can select it.
3. **Route.** Move instructions to the correct owner or lifecycle.
4. **Compose.** Combine existing tools or delegate a bounded subproblem.
5. **Extend.** Add a plugin component, connector, or script only when the
   inventory proves the existing surfaces insufficient.

For every proposed move, state:

- the chosen surface;
- when its cost is paid: every turn, on skill activation, at install, or on use;
- what evidence will show that it worked;
- how to remove or reverse it.

## Lifecycle test

Put information at the narrowest lifecycle that still reaches every consumer:

- **Every turn:** only compact repository invariants and skill routing metadata.
- **On activation:** full procedures and routed references.
- **At install:** plugin discovery and declared dependencies.
- **On use:** external calls, delegated runs, and expensive validation.

If the same instruction is copied across prompts, move it to one owned surface.
If a standing instruction affects only one rare task, move it down into a skill.

## Close the loop

1. Reproduce the symptom or identify the missing decision.
2. Apply one lever.
3. Measure the expected change.
4. Remove redundant scaffolding made obsolete by the move.
5. Record version-sensitive evidence with its Codex build or CLI version.

The output should be a diagnosis and a minimal intervention, not a catalog of
possible machinery.
