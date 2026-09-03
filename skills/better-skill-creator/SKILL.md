---
name: better-skill-creator
description: Create or revise Codex skills with precise routing, progressive disclosure, UI metadata, native validation, and behavior-focused evaluation.
license: CC-BY-4.0
---

# Better Skill Creator

Create a Codex-native skill whose routing is cheap, procedure is complete, and
behavior can be verified. A skill is a directory with `SKILL.md` and optional
`agents/`, `references/`, `scripts/`, and `assets/`.

## 1. Define the routing boundary

Write one sentence for each:

- **Use when:** observable requests or situations that need this procedure.
- **Do not use when:** the nearest competing capability or simpler path.
- **Outcome:** the artifact or decision the skill reliably produces.

The frontmatter `description` is a routing key visible in the every-turn skill
catalog. Keep it concise and discriminative. Put the workflow in the body,
which Codex reads in full only after the skill is selected.

## 2. Create the package

Required `SKILL.md` frontmatter:

```yaml
---
name: {lowercase-hyphen-name}
description: {When_To_Route_Here_And_What_Outcome_It_Produces}
---
```

The directory name and `name` must match. Use lowercase letters, digits, and
single hyphens. Keep the common path in `SKILL.md`; route conditional depth to:

- `references/` for material read only on a named branch;
- `scripts/` for repeatable deterministic operations;
- `assets/` for templates or files copied into outputs;
- `agents/openai.yaml` for UI metadata and invocation policy.

Resolve every relative path from the skill directory identified by the current
session's skill source locator. Do not assume a global `~/.codex/skills` path:
plugins may run from versioned caches or repository scopes.

## 3. Write for progressive disclosure

Order the body by execution:

1. decisive routing or safety rule;
2. common workflow;
3. branch table naming exact references or scripts;
4. output contract;
5. failure and stop conditions.

Name native Codex primitives instead of copying their schemas into prose.
Prefer one precise instruction over repeated reminders. Put information at the
narrowest lifecycle that reaches its consumer: catalog description every turn,
body on activation, references on demand, dependencies at install, calls on use.

When authoring prompt bytes, apply `prompt-engineering` and
`hypershot-protocol` if available. If either is unavailable, say so once and use
the shipped source as the fallback.

## 4. Add UI metadata

Create `agents/openai.yaml`:

```yaml
interface:
  display_name: "{Human_Facing_Name}"
  short_description: "{Twenty_Five_To_Sixty_Four_Character_Summary}"
  default_prompt: "Use ${skill-name} to {Representative_Task}."
policy:
  allow_implicit_invocation: true
```

Quote strings. The default prompt must explicitly mention `$skill-name`.
Set `allow_implicit_invocation: false` only when the skill is a deliberate
ceremony, dangerous operation, or explicit diagnostic that should not volunteer
itself.

## 5. Validate structure

When the bundled creator is available, run its validator against the skill:

```bash
python {skill-creator-source}/scripts/quick_validate.py {skill-directory}
```

Also check:

- every path named in `SKILL.md` exists;
- scripts run from a working directory outside the skill;
- output contains no unresolved placeholders unless they are intentional
  template variables;
- implicit policy matches the routing intent;
- no platform claim depends on an unpinned or unverified Codex version.

## 6. Evaluate behavior

Use `self-play` for consequential or subtle skills. Define routing and outcome
cases before revising:

- positive requests that should activate the skill;
- neighboring requests that should not;
- a normal execution case;
- a boundary or adversarial case;
- one regression case for behavior already working.

For clean evaluators, use `collaboration.spawn_agent` with
`fork_turns: "none"`. Filesystem state remains shared, so provide exact allowed
paths and do not call the run blind when author notes are visible. For
repeatable external trials, adapt a harness around `codex exec` with explicit
working directory, version, JSON/output-schema options, and isolated config as
the test requires.

Measure observable behavior, not whether the response says the skill name.
A routed skill can still fail its task, and a good answer may be produced without
the intended skill.

## 7. Iterate economically

For each failure:

1. locate it in routing, instruction, resource, or evaluation;
2. change the smallest owned surface;
3. rerun the failing case and one regression control;
4. remove redundant prompt text made obsolete by the change.

If editing an installed plugin, remember that Codex may be reading a versioned
cache. Validate the source, update or reinstall through the marketplace flow,
and test in a new session before concluding the edit had no effect.

## Handoff

Return the skill path, changed surfaces, invocation policy, validation commands
and results, behavioral evidence, and any version-sensitive limitation. Do not
claim success from schema validity alone.
