# I4 Skills Subsystem

Pinned target: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; config root `C:\Users\Darian\.codex`; survey date 2026-09-02; probe commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`.

### Skill_Package_Directory
- **surface**: `<skill-name>/SKILL.md`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the locally read Anatomy section defines a required `SKILL.md` plus optional `agents/`, `scripts/`, `references/`, and `assets/` members.
- **does**: Packages a reusable agent capability in one directory.
- **spark**: S=8 P=0 A=4 R=4 K=3
- **why**: S from adding task-specific behavior; A from encoding a reusable workflow; R from bundling callable files; K from carrying task-specific material.
- **rent**: once_at_install — the user pays storage and installation effort once.
- **composes**: [[SKILL_Markdown_Instruction_Body]], [[Routed_Skill_Reference_Loading]], [[Skill_Script_Reuse]], [[Skill_Asset_Reuse]]
- **confidence**: observed

### SKILL_Frontmatter_Name
- **surface**: `name: <skill-name>`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the read file's YAML frontmatter contains `name: skill-creator` and identifies `name` as required.
- **does**: Keys a skill's identity for discovery.
- **spark**: S=2 P=0 A=3 R=2 K=0
- **why**: S from making a capability addressable; A from routing selection; R from indexing the skill source.
- **rent**: every_turn — the name occupies the model-visible skill catalog.
- **composes**: [[Model_Visible_Skill_Catalog]], [[Explicit_Skill_Invocation]]
- **confidence**: observed

### SKILL_Frontmatter_Description
- **surface**: `description: <when this skill applies>`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the read file states that frontmatter description determines when a skill should be considered.
- **does**: Supplies the matching text for skill selection.
- **spark**: S=4 P=2 A=7 R=1 K=0
- **why**: S from exposing task-specific capability; P from mediating automatic versus user-directed selection; A from routing tasks by scope; R from locating a candidate skill.
- **rent**: every_turn — the description occupies the model-visible skill catalog.
- **composes**: [[Implicit_Skill_Invocation]], [[Skill_Catalog_Context_Budget]]
- **confidence**: observed

### SKILL_Markdown_Instruction_Body
- **surface**: `SKILL.md` Markdown body
- **evidence**: `C:\Users\Darian\.codex\skills\.system\openai-docs\SKILL.md` — this probe selected the advertised skill, read the entire body, then followed its docs-first workflow.
- **does**: Provides task instructions after skill selection.
- **spark**: S=9 P=1 A=8 R=2 K=5
- **why**: S from adding specialized behavior; P from carrying user-facing interaction rules; A from prescribing workflow; R from directing tool use; K from supplying domain guidance.
- **rent**: every_matching_call — the agent pays full instruction-context cost whenever the skill is used.
- **composes**: [[SKILL_Full_Read_Gate]], [[Routed_Skill_Reference_Loading]]
- **confidence**: observed

### Model_Visible_Skill_Catalog
- **surface**: `## Skills` / `### Available skills`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — ordinal 2 directly records 19 advertised entries, each with a name, description, and absolute file locator.
- **does**: Exposes available skills to the model before selection.
- **spark**: S=4 P=1 A=5 R=8 K=2
- **why**: S from advertising specialized abilities; P from exposing user-addressable names; A from enabling routing; R from providing source locators; K from supplying capability summaries.
- **rent**: every_turn — the agent pays prompt-context cost for the catalog.
- **composes**: [[SKILL_Frontmatter_Name]], [[SKILL_Frontmatter_Description]], [[Skill_Locator_Access_Dispatch]]
- **confidence**: observed

### Current_Session_Skill_Source_Locators
- **surface**: `(file: C:/Users/Darian/.codex/.../SKILL.md)`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — the 19-entry catalog points into `.codex/skills/.system`, `.codex/skills`, and versioned `.codex/plugins/cache` trees.
- **does**: Advertises skills from three installed locator families.
- **spark**: S=3 P=0 A=2 R=8 K=0
- **why**: S from making installed capabilities selectable; A from retaining source provenance; R from reaching three filesystem families.
- **rent**: every_turn — each absolute locator consumes catalog context.
- **composes**: [[Model_Visible_Skill_Catalog]], [[Skill_Locator_Access_Dispatch]]
- **confidence**: observed

### Skill_Catalog_Context_Budget
- **surface**: initial skills list prompt budget
- **evidence**: `https://learn.chatgpt.com/docs/build-skills` — fetched lines 832-834 specify at most 2% of the context window, or 8,000 characters when the window is unknown, with description shortening before omission.
- **does**: Caps the initial skill catalog's context footprint.
- **spark**: S=1 P=0 A=7 R=3 K=0
- **why**: S from preserving room for active capabilities; A from prioritizing catalog entries; R from rationing context capacity.
- **rent**: every_turn — the agent pays the bounded catalog token cost.
- **composes**: [[Model_Visible_Skill_Catalog]], [[SKILL_Frontmatter_Description]]
- **confidence**: documented

### Local_Skill_Discovery_Scopes
- **surface**: `$CWD/.agents/skills`, parent `.agents/skills`, `$REPO_ROOT/.agents/skills`, `$HOME/.agents/skills`, `/etc/codex/skills`, system bundle
- **evidence**: `https://learn.chatgpt.com/docs/build-skills` — fetched lines 875-891 document repository-to-root, user, admin, system scanning plus symlink following.
- **does**: Discovers local skills across a scoped location hierarchy.
- **spark**: S=5 P=0 A=4 R=9 K=0
- **why**: S from making contextual capabilities available; A from applying location scope; R from scanning multiple filesystem roots.
- **rent**: none — the documentation does not establish a user-visible recurring charge for scanning.
- **composes**: [[Model_Visible_Skill_Catalog]], [[Skill_Package_Directory]]
- **confidence**: documented

### Duplicate_Skill_Name_Selection
- **surface**: two `SKILL.md` files sharing one `name`
- **evidence**: `https://learn.chatgpt.com/docs/build-skills` — fetched line 877 states same-name skills are not merged and may both appear in selectors.
- **does**: Preserves same-name skills as separate selector entries.
- **spark**: S=2 P=3 A=6 R=3 K=0
- **why**: S from retaining both capabilities; P from leaving the choice visible to the user; A from avoiding precedence-based merging; R from preserving both sources.
- **rent**: every_turn — duplicate entries can consume catalog context.
- **composes**: [[Model_Visible_Skill_Catalog]], [[Explicit_Skill_Invocation]]
- **confidence**: documented

### Explicit_Skill_Invocation
- **surface**: `$SkillName` or a named available skill in the prompt
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — base instructions require use when the user names an available skill with `$SkillName` or plain text.
- **does**: Lets the user select an available skill for the turn.
- **spark**: S=6 P=8 A=5 R=3 K=0
- **why**: S from activating specialized behavior; P from giving the user selection authority; A from overriding automatic routing with an explicit mention; R from reaching the selected source.
- **rent**: every_matching_call — the agent pays the selected skill's instruction-context cost.
- **composes**: [[Model_Visible_Skill_Catalog]], [[SKILL_Full_Read_Gate]]
- **confidence**: observed

### Implicit_Skill_Invocation
- **surface**: task clearly matches an available skill's `description`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — base instructions required `openai-docs` for this Codex-skills survey; the skill was selected without a `$openai-docs` mention.
- **does**: Activates a skill when the task matches its description.
- **spark**: S=7 P=3 A=9 R=3 K=0
- **why**: S from adding matched capability; P from permitting system-initiated selection; A from description-based routing; R from reaching the matched source.
- **rent**: every_matching_call — the agent pays the matched skill's instruction-context cost.
- **composes**: [[SKILL_Frontmatter_Description]], [[SKILL_Full_Read_Gate]], [[OpenAI_YAML_Implicit_Invocation_Policy]]
- **confidence**: observed

### Per_Turn_Skill_Activation
- **surface**: `Do not carry skills across turns unless re-mentioned.`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — the current session's base instructions explicitly impose turn-local activation.
- **does**: Expires skill activation after the current turn.
- **spark**: S=2 P=5 A=8 R=0 K=0
- **why**: S from bounding specialized behavior; P from requiring renewed user mention for explicit reuse; A from resetting routing each turn.
- **rent**: every_matching_call — a later turn must pay selection and loading cost again.
- **composes**: [[Explicit_Skill_Invocation]], [[Implicit_Skill_Invocation]]
- **confidence**: observed

### SKILL_Full_Read_Gate
- **surface**: read selected `SKILL.md` completely before task actions
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — the base instructions require the main agent to read a selected skill completely, continuing through truncation or pagination to EOF.
- **does**: Gates task actions on complete entrypoint loading.
- **spark**: S=5 P=1 A=10 R=5 K=4
- **why**: S from applying the whole specialized capability; P from delaying action until its constraints are known; A from enforcing a loading sequence; R from requiring full source access; K from preventing partial instruction knowledge.
- **rent**: every_matching_call — the agent pays the full entrypoint context cost before acting.
- **composes**: [[SKILL_Markdown_Instruction_Body]], [[Routed_Skill_Reference_Loading]]
- **confidence**: observed

### Skill_Locator_Access_Dispatch
- **surface**: file, aliased path, executor package, orchestrator package, or custom-resource locator
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — ordinal 2 describes locator ownership classes; base instructions map them to filesystem, owning environment, or skills-provider reads.
- **does**: Dispatches skill loading through the locator's owning access mechanism.
- **spark**: S=3 P=0 A=8 R=9 K=0
- **why**: S from enabling non-file skills; A from selecting the correct loader; R from reaching multiple storage authorities.
- **rent**: every_matching_call — the agent pays source-access and instruction-context cost when selected.
- **composes**: [[Model_Visible_Skill_Catalog]], [[SKILL_Full_Read_Gate]]
- **confidence**: observed

### Skill_Relative_Path_Resolution
- **surface**: relative links inside `SKILL.md`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — base instructions resolve filesystem-backed relative paths against the directory containing `SKILL.md`.
- **does**: Resolves supporting-file links against the skill entrypoint directory.
- **spark**: S=2 P=0 A=6 R=8 K=0
- **why**: S from making packaged helpers usable; A from deterministic resolution; R from locating supporting files.
- **rent**: every_matching_call — path resolution occurs only when a selected skill routes to support material.
- **composes**: [[Routed_Skill_Reference_Loading]], [[Skill_Script_Reuse]], [[Skill_Asset_Reuse]]
- **confidence**: observed

### Routed_Skill_Reference_Loading
- **surface**: `references/` links routed from `SKILL.md`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the read file keeps conditional documentation under `references/` and directs the agent to load only material relevant to the current mode.
- **does**: Loads task-relevant supporting documentation on demand.
- **spark**: S=5 P=0 A=9 R=5 K=8
- **why**: S from supplying specialized guidance; A from progressive routing; R from reaching packaged references; K from adding conditional domain material.
- **rent**: every_matching_call — the agent pays context only for references routed by the selected task.
- **composes**: [[SKILL_Markdown_Instruction_Body]], [[Skill_Relative_Path_Resolution]]
- **confidence**: observed

### Skill_Script_Reuse
- **surface**: `scripts/`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the read file defines executable helpers for repeated or deterministic logic; the same directory contains `init_skill.py`, `quick_validate.py`, and `generate_openai_yaml.py`.
- **does**: Reuses packaged executable helpers for skill work.
- **spark**: S=8 P=0 A=7 R=6 K=0
- **why**: S from adding deterministic operations; A from replacing regenerated mechanics with a stable procedure; R from exposing executable resources.
- **rent**: every_matching_call — execution cost is paid only when the selected workflow uses a helper.
- **composes**: [[Skill_Package_Directory]], [[Skill_Relative_Path_Resolution]]
- **confidence**: observed

### Skill_Asset_Reuse
- **surface**: `assets/`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the read file defines assets as templates, images, fonts, icons, boilerplate, or other files adapted into output; its directory contains two UI image assets.
- **does**: Reuses packaged output resources for skill work.
- **spark**: S=6 P=0 A=4 R=8 K=0
- **why**: S from enabling template-backed production; A from directing reuse; R from exposing concrete output resources.
- **rent**: every_matching_call — access cost is paid only when a selected workflow uses an asset.
- **composes**: [[Skill_Package_Directory]], [[Skill_Relative_Path_Resolution]]
- **confidence**: observed

### OpenAI_YAML_Implicit_Invocation_Policy
- **surface**: `policy.allow_implicit_invocation: false`
- **evidence**: `C:\Users\Darian\.codex\skills\.system\skill-creator\SKILL.md` — the locally read policy section says `false` removes automatic context selection while retaining explicit `$skill-name` invocation.
- **does**: Restricts a skill to explicit invocation.
- **spark**: S=3 P=8 A=7 R=0 K=0
- **why**: S from retaining explicitly requested capability; P from reserving activation authority to the user; A from disabling the implicit routing path.
- **rent**: none — the flag avoids implicit loading cost until the user invokes the skill.
- **composes**: [[Explicit_Skill_Invocation]], [[Implicit_Skill_Invocation]]
- **confidence**: observed

### Skills_Config_Enabled_Flag
- **surface**: `[[skills.config]] path = "/path/to/skill/SKILL.md" enabled = false`
- **evidence**: `https://learn.chatgpt.com/docs/build-skills` — fetched lines 908-916 document path-addressed disabling without deletion and require a restart after the config change.
- **does**: Disables one local skill without deleting its files.
- **spark**: S=2 P=7 A=4 R=2 K=0
- **why**: S from removing one capability from availability; P from giving the user activation authority; A from gating discovery by path; R from preserving the installed resource.
- **rent**: none — a disabled skill avoids catalog and instruction loading cost.
- **composes**: [[Local_Skill_Discovery_Scopes]], [[Model_Visible_Skill_Catalog]]
- **confidence**: documented

### Skill_UI_Interface_Metadata
- **surface**: `agents/openai.yaml interface`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.826.12353\skills\spreadsheets\agents\openai.yaml` — the read file supplies `display_name`, `short_description`, icons, `brand_color`, and `default_prompt` for the skill interface.
- **does**: Defines user-facing presentation metadata for a skill.
- **spark**: S=1 P=5 A=1 R=3 K=0
- **why**: S from making the capability legible; P from shaping the user's invocation surface; A from supplying a default entry prompt; R from linking icon assets.
- **rent**: every_turn — UI metadata is available wherever the skill is presented.
- **composes**: [[Model_Visible_Skill_Catalog]], [[Skill_Asset_Reuse]]
- **confidence**: observed

### Missing_Skill_Fallback
- **surface**: named skill unavailable or unreadable
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-07-40-01a0634e-2147-77f0-b4e2-e62479fe5519.jsonl` — base instructions require a brief disclosure followed by the best available fallback when a named skill cannot be loaded.
- **does**: Continues with a disclosed fallback after skill-loading failure.
- **spark**: S=4 P=6 A=8 R=2 K=0
- **why**: S from preserving partial task capability; P from informing the user of degraded execution; A from defining the failure branch; R from falling back when the intended source is unreachable.
- **rent**: every_matching_call — fallback handling is charged only on a failed requested invocation.
- **composes**: [[Explicit_Skill_Invocation]], [[SKILL_Full_Read_Gate]]
- **confidence**: observed

## Uncovered
- The Desktop Skills sidebar and `/skills` interactive selector were not opened because this delegated arm had no safe semantic UI surface for them.
- Repository, user-home `.agents/skills`, and admin discovery roots were searched for this workspace and were absent; precedence behavior was therefore not exercised.
- Symlink following, duplicate-name selection, description truncation, catalog omission warnings, hot change detection, enable/disable restart behavior, unreadable-skill fallback, non-file skill locators, and explicit-only policy enforcement were not mutated or exercised under the read-only constraint.
- Installed plugin/marketplace acquisition mechanics and custom prompts were excluded as I5 scope; general configuration layering was excluded as I6 scope.
