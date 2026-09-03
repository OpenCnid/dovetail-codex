# Codex intervention costs

Compare levers by when and where their cost is paid.

| Surface | Cost timing | Main risk | Removal |
|---|---|---|---|
| Current prompt | once | local verbosity or ambiguity | end the turn |
| `AGENTS.md` | every turn in scope | context rent and unintended reach | delete or narrow the instruction |
| Skill description | every turn in catalog | routing noise; catalog truncation | shorten or sharpen routing terms |
| Selected `SKILL.md` | on activation | full-body context cost | compress common path; route branches |
| Skill reference | on branch read | delayed context cost | stop routing to it or remove it |
| Plugin manifest | install/discovery | stale cache or packaging mismatch | update/reinstall or uninstall |
| Delegated agent | on use | context handoff, slot, coordination, merge | interrupt or stop spawning |
| `codex exec` harness | on run and maintenance | version drift, config variance, API cost | remove harness or pin/update adapter |
| Connector/MCP | install/auth/use | permissions, external dependency, latency | disconnect or uninstall |
| Permission expansion | for affected actions | wider blast radius | restore the narrower policy |

## Prompt rent

The pinned probe documents a model-visible skill catalog budget of roughly two
percent of context or 8,000 characters, with description shortening before
omission. Treat frontmatter descriptions as indexed routing labels.

The selected skill body is read in full. Put the complete common path there, but
move rare detail into routed references. Do not split the common path so finely
that every invocation must load every reference.

The root-to-CWD `AGENTS.md` chain has a default combined 32 KiB budget. A rule
that applies only to one subtree belongs in a closer file; a rule that applies
only to one kind of task belongs in a skill.

## Operational risk

Ask four questions:

1. Can the intervention change files, external state, permissions, or other
   people's systems?
2. Is the target explicit and recoverable?
3. Does the intervention persist beyond this task?
4. Which evidence will distinguish success from a plausible-looking response?

Prefer the lever with the narrowest scope and lifecycle that still reaches all
required consumers.
