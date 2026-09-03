### AGENTS_Global_File_Precedence
- **surface**: `~/.codex/AGENTS.override.md` / `~/.codex/AGENTS.md`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22502` ([official page](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md), snapshot 2026-09-02) — “reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`.”
- **does**: Selects one non-empty global instruction file before work begins.
- **spark**: S=2 P=6 A=7 R=0 K=2
- **why**: S supplies reusable behavioral constraints; P sets persistent user authority preferences; A establishes a global working method; K contributes project-independent guidance
- **rent**: every_turn — the selected guidance remains in the session context
- **composes**: [[AGENTS_Project_Path_Scoping]], [[AGENTS_Root_To_CWD_Merge_Order]]
- **confidence**: documented

### AGENTS_Project_Path_Scoping
- **surface**: `AGENTS.override.md` / `AGENTS.md` from project root to `$CWD`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22505` ([official page](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md), snapshot 2026-09-02) — “Codex walks down to your current working directory.”
- **does**: Discovers at most one applicable project instruction file per directory on the root-to-CWD path.
- **spark**: S=2 P=4 A=8 R=1 K=3
- **why**: S specializes behavior by work area; P scopes whose local guidance controls; A maps directory position to method; R reaches repository guidance files; K supplies local project facts
- **rent**: every_turn — discovered project guidance remains in the session context
- **composes**: [[AGENTS_Global_File_Precedence]], [[AGENTS_Root_To_CWD_Merge_Order]]
- **confidence**: documented

### AGENTS_Root_To_CWD_Merge_Order
- **surface**: concatenated `AGENTS.md` instruction chain
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22506` ([official page](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md), snapshot 2026-09-02) — “Files closer to your current directory override earlier guidance.”
- **does**: Gives later directory-local guidance precedence over broader earlier guidance.
- **spark**: S=1 P=7 A=8 R=0 K=2
- **why**: S refines task behavior; P resolves instruction authority; A defines deterministic precedence; K prioritizes local knowledge
- **rent**: every_turn — the merged ordering governs the session context
- **composes**: [[AGENTS_Project_Path_Scoping]]
- **confidence**: documented

### AGENTS_Context_Byte_Limit
- **surface**: `project_doc_max_bytes`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22508` ([official page](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md), snapshot 2026-09-02) — “32 KiB by default.”
- **does**: Stops adding project instruction files when their combined byte budget is reached.
- **spark**: S=0 P=1 A=3 R=4 K=0
- **why**: P bounds how much durable guidance can govern; A imposes a loading policy; R budgets prompt context
- **rent**: every_turn — loaded instruction bytes occupy session context
- **composes**: [[AGENTS_Project_Path_Scoping]], [[Codex_Config_TOML]]
- **confidence**: documented

### AGENTS_Run_Start_Rebuild
- **surface**: Codex run or TUI session start
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22632` ([official page](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md), snapshot 2026-09-02) — “Codex rebuilds the instruction chain on every run.”
- **does**: Rebuilds the applicable instruction chain once when a run starts.
- **spark**: S=0 P=1 A=6 R=2 K=1
- **why**: P reapplies current guidance; A fixes refresh timing; R rereads instruction files; K refreshes project context
- **rent**: every_turn — the rebuilt chain persists for the run
- **composes**: [[AGENTS_Global_File_Precedence]], [[AGENTS_Project_Path_Scoping]]
- **confidence**: documented

### Custom_Prompt_Explicit_Slash_Command
- **surface**: `~/.codex/prompts/*.md` → `/prompts:<name>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22651-22656` ([official page](https://learn.chatgpt.com/docs/custom-prompts.md), snapshot 2026-09-02) — “Custom prompts are deprecated” and “require explicit invocation.”
- **does**: Exposes a top-level Markdown prompt as an explicitly invoked CLI or IDE slash command.
- **spark**: S=5 P=0 A=6 R=2 K=0
- **why**: S adds a reusable prompt action; A packages a repeatable method; R reaches local prompt files
- **rent**: every_matching_call — expanded prompt text enters context only when invoked
- **composes**: [[Custom_Prompt_Argument_Expansion]], [[Skill_Explicit_Invocation]]
- **confidence**: documented

### Custom_Prompt_Command_Metadata
- **surface**: YAML `description:` / `argument-hint:` in `~/.codex/prompts/*.md`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22682-22689` ([official page](https://learn.chatgpt.com/docs/custom-prompts.md), snapshot 2026-09-02) — “Shown under the command name in the popup.”
- **does**: Annotates a custom prompt command with menu description and expected-argument hints.
- **spark**: S=1 P=1 A=3 R=1 K=0
- **why**: S improves command usability; P communicates invocation expectations; A declares the command interface; R exposes metadata in the menu
- **rent**: every_matching_call — metadata is consulted when selecting the command
- **composes**: [[Custom_Prompt_Explicit_Slash_Command]]
- **confidence**: documented

### Custom_Prompt_Argument_Expansion
- **surface**: `$1`…`$9`, `$ARGUMENTS`, `$KEY`, `$$`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22688-22690` ([official page](https://learn.chatgpt.com/docs/custom-prompts.md), snapshot 2026-09-02) — “`$1` through `$9` expand from space-separated arguments.”
- **does**: Substitutes positional, aggregate, named, or escaped-dollar placeholders into an invoked prompt.
- **spark**: S=4 P=0 A=5 R=1 K=0
- **why**: S parameterizes reusable instructions; A turns a static prompt into a callable template; R injects user-supplied values
- **rent**: every_matching_call — expansion adds the resulting prompt text to that call
- **composes**: [[Custom_Prompt_Explicit_Slash_Command]]
- **confidence**: documented

### Skill_Package_Format
- **surface**: `<skill-directory>/SKILL.md`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21687` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “must include `name` and `description`.”
- **does**: Defines a reusable skill from a directory containing a named, described `SKILL.md` file.
- **spark**: S=9 P=1 A=6 R=2 K=3
- **why**: S adds task-specific capability; P can encode interaction rules; A packages a workflow; R exposes adjacent resources; K supplies domain instructions
- **rent**: every_matching_call — full skill instructions load when selected
- **composes**: [[Skill_Progressive_Disclosure]], [[Skill_Supporting_Resource_Layout]]
- **confidence**: documented

### Skill_Progressive_Disclosure
- **surface**: skill `name` + `description` + path → full `SKILL.md`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21675-21685` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “load the full `SKILL.md` instructions when they decide to use that skill.”
- **does**: Defers full skill instruction loading until Codex selects the skill.
- **spark**: S=7 P=0 A=7 R=6 K=4
- **why**: S activates specialized ability on demand; A stages context loading; R preserves prompt capacity; K retrieves detailed skill knowledge only when relevant
- **rent**: every_matching_call — only selected skills pay full instruction-token cost
- **composes**: [[Skill_Initial_List_Context_Budget]], [[Skill_Explicit_Invocation]], [[Skill_Implicit_Description_Matching]]
- **confidence**: documented

### Skill_Initial_List_Context_Budget
- **surface**: initial Codex skills list
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21679-21683` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “at most 2% of the model's context window, or 8,000 characters.”
- **does**: Caps initial skill discovery metadata by shortening descriptions before omitting skills with a warning.
- **spark**: S=1 P=0 A=5 R=7 K=0
- **why**: S preserves discoverability under load; A defines degradation order; R budgets model context
- **rent**: every_turn — the bounded list occupies initial session context
- **composes**: [[Skill_Progressive_Disclosure]]
- **confidence**: documented

### Explicit_Skill_Invocation
- **surface**: `/skills` or `$<skill>` in Codex CLI / IDE
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21691-21695` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “run `/skills` or type `$` to mention a skill.”
- **does**: Lets the user select a skill directly for the current request.
- **spark**: S=8 P=6 A=3 R=2 K=2
- **why**: S activates a task-specific workflow; P gives the user invocation authority; A chooses the method explicitly; R reaches the skill package; K loads its instructions
- **rent**: every_matching_call — selected skill instructions enter that request context
- **composes**: [[Skill_Progressive_Disclosure]], [[Skill_Implicit_Invocation_Policy]]
- **confidence**: documented

### Skill_Implicit_Description_Matching
- **surface**: `description:` in `SKILL.md` front matter
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21696-21701` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “choose a skill when your task matches the skill `description`.”
- **does**: Lets Codex select a skill when the request semantically matches its description.
- **spark**: S=8 P=3 A=7 R=2 K=3
- **why**: S activates specialized behavior; P delegates invocation choice to the model; A routes requests by declared scope; R reaches the matched package; K loads its domain guidance
- **rent**: every_matching_call — matched skill instructions enter that request context
- **composes**: [[Skill_Progressive_Disclosure]], [[Skill_Implicit_Invocation_Policy]]
- **confidence**: documented

### Skill_Repo_Path_Discovery
- **surface**: `.agents/skills` from `$CWD` through `$REPO_ROOT`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21732-21734` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “scans `.agents/skills` in every directory.”
- **does**: Discovers repository skills at every directory from the working directory up to the repository root.
- **spark**: S=6 P=1 A=6 R=5 K=3
- **why**: S makes scoped workflows available; P permits repository authors to contribute behavior; A maps directory scope to workflow availability; R reaches checked-in packages; K supplies local guidance
- **rent**: every_turn — discovered skill metadata enters the initial skills list
- **composes**: [[Skill_Progressive_Disclosure]], [[Skill_Initial_List_Context_Budget]]
- **confidence**: documented

### Local_Skill_Discovery_Scopes
- **surface**: `$HOME/.agents/skills`, `/etc/codex/skills`, Codex-bundled skills
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21736-21748` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “repository, user, admin, and system locations.”
- **does**: Discovers skills from user, administrator, system, or repository scopes.
- **spark**: S=7 P=4 A=5 R=6 K=3
- **why**: S expands task workflows; P distributes contribution authority across scopes; A layers availability sources; R reaches multiple package roots; K exposes packaged expertise
- **rent**: every_turn — discovered metadata participates in the initial skill list
- **composes**: [[Skill_Repo_Path_Discovery]], [[Skill_Initial_List_Context_Budget]]
- **confidence**: documented

### Skill_Implicit_Invocation_Policy
- **surface**: `agents/openai.yaml` → `policy.allow_implicit_invocation`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21807-21819` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “explicit `$skill` invocation still works.”
- **does**: Disables model-initiated skill selection without disabling explicit user invocation.
- **spark**: S=2 P=9 A=5 R=0 K=0
- **why**: S preserves manual access; P gates who may invoke the workflow; A changes routing policy
- **rent**: none — the policy changes eligibility without loading the full skill
- **composes**: [[Skill_Explicit_Invocation]], [[Skill_Implicit_Description_Matching]]
- **confidence**: documented

### Skill_Local_Enable_Override
- **surface**: `[[skills.config]]` → `path`, `enabled = false`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21782-21792` ([official page](https://learn.chatgpt.com/docs/build-skills.md), snapshot 2026-09-02) — “disable a skill without deleting it.”
- **does**: Disables a specific local skill by absolute `SKILL.md` path after restart.
- **spark**: S=1 P=8 A=3 R=2 K=0
- **why**: S removes one task workflow from availability; P gives the user activation authority; A filters discovery; R targets a package path
- **rent**: none — a disabled skill adds no full instruction cost
- **composes**: [[Codex_Config_TOML]], [[Skill_Discovery_Scopes]]
- **confidence**: documented

### Skill_Supporting_Resource_Layout
- **surface**: `references/`, `assets/`, `scripts/` beside `SKILL.md`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:21908-21919` ([official page](https://developers.openai.com/plugins/build/skills.md), snapshot 2026-09-02) — “Reference supporting files from `SKILL.md` and explain when to load or run them.”
- **does**: Routes detailed guidance, reusable assets, or deterministic helpers into purpose-specific sibling directories.
- **spark**: S=7 P=0 A=7 R=7 K=5
- **why**: S adds deterministic or specialized support; A separates workflow control from supporting material; R exposes scripts and assets; K provides selectively loaded references
- **rent**: every_matching_call — only resources requested by the selected workflow are loaded or run
- **composes**: [[Skill_Package_Format]], [[Skill_Progressive_Disclosure]]
- **confidence**: documented

### Plugin_Package_Manifest
- **surface**: `.codex-plugin/plugin.json`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26556-26565` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “Every plugin has a manifest at `.codex-plugin/plugin.json`.”
- **does**: Gives an installable plugin a required identity and contribution entry point.
- **spark**: S=3 P=0 A=5 R=7 K=1
- **why**: S groups contributed capabilities; A declares package composition; R makes the bundle discoverable and installable; K identifies package metadata
- **rent**: once_at_install — the host reads package identity during discovery and installation
- **composes**: [[Plugin_Skills_Contribution_Path]], [[Plugin_Install_Surface_Metadata]]
- **confidence**: documented

### Plugin_Skills_Contribution_Path
- **surface**: `.codex-plugin/plugin.json` → `skills: "./skills/"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26620-26630` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “`skills` ... point[s] to bundled components relative to the plugin root.”
- **does**: Registers a plugin-root-relative directory of bundled skills.
- **spark**: S=9 P=1 A=6 R=6 K=3
- **why**: S installs task-specific workflows; P lets package publishers contribute behavior; A binds workflows into one bundle; R exposes packaged skill files; K supplies bundled guidance
- **rent**: every_turn — installed skill descriptors join session discovery metadata
- **composes**: [[Plugin_Manifest_Entry_Point]], [[Skill_Progressive_Disclosure]]
- **confidence**: documented

### Plugin_Install_Surface_Metadata
- **surface**: `.codex-plugin/plugin.json` → `interface`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26633-26642` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “`interface` controls how install surfaces present the plugin.”
- **does**: Controls a plugin listing’s descriptive copy, publisher data, legal links, prompts, or visual presentation.
- **spark**: S=1 P=2 A=2 R=5 K=1
- **why**: S exposes starter prompts; P communicates publisher identity and terms; A shapes install-time presentation; R supplies discovery metadata and assets; K labels capability intent
- **rent**: once_at_install — listing metadata is paid during discovery or installation
- **composes**: [[Plugin_Manifest_Entry_Point]], [[Universal_Plugin_Directory]]
- **confidence**: documented

### Plugin_Manifest_Relative_Path_Rules
- **surface**: `./`-prefixed paths in `.codex-plugin/plugin.json`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26644-26651` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “Keep manifest paths relative to the plugin root.”
- **does**: Constrains manifest contribution paths to explicit plugin-root-relative locations.
- **spark**: S=0 P=0 A=4 R=6 K=0
- **why**: A standardizes package resolution; R bounds contribution reach to the plugin bundle
- **rent**: once_at_install — paths resolve while the package is loaded
- **composes**: [[Plugin_Manifest_Entry_Point]]
- **confidence**: documented

### Universal_Plugin_Directory
- **surface**: ChatGPT/Codex **Plugins** directory; Codex CLI `/plugins`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:29942-29949` ([official page](https://learn.chatgpt.com/docs/plugins.md), snapshot 2026-09-02) — “Both products use one universal plugin directory.”
- **does**: Publishes the same public plugin listings to supported ChatGPT and Codex surfaces.
- **spark**: S=5 P=0 A=2 R=9 K=2
- **why**: S makes packaged workflows installable; A unifies distribution; R exposes a shared public catalog; K supplies listing descriptions
- **rent**: none — browsing the catalog does not itself install a package
- **composes**: [[Plugin_Install_Surface_Metadata]], [[Codex_CLI_Plugin_Browser]]
- **confidence**: documented

### Local_Plugin_Marketplace_Catalog
- **surface**: `$REPO_ROOT/.agents/plugins/marketplace.json` / `~/.agents/plugins/marketplace.json`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26533-26543` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “A plugin marketplace is a JSON catalog of plugins.”
- **does**: Defines a private repository or personal catalog for plugin authoring, testing, or distribution.
- **spark**: S=4 P=3 A=6 R=8 K=2
- **why**: S distributes reusable workflows; P lets repository or personal owners curate availability; A organizes private distribution; R exposes local catalog sources; K provides listing metadata
- **rent**: none — catalog presence alone does not install its entries
- **composes**: [[Marketplace_Entry_Install_Policy]], [[Marketplace_Installed_Copy_Cache]]
- **confidence**: documented

### Marketplace_Entry_Install_Policy
- **surface**: `plugins[].policy.installation` / `plugins[].policy.authentication`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26468-26473` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “`AVAILABLE`, `INSTALLED_BY_DEFAULT`, or `NOT_AVAILABLE`.”
- **does**: Declares each marketplace entry’s installation availability and authentication timing.
- **spark**: S=1 P=9 A=4 R=3 K=0
- **why**: S gates packaged capabilities; P assigns install and authentication authority; A establishes rollout policy; R controls catalog reachability
- **rent**: once_at_install — authentication may be charged at install or deferred to first use
- **composes**: [[Local_Plugin_Marketplace_Catalog]]
- **confidence**: documented

### Plugin_Marketplace_Source_Commands
- **surface**: `codex plugin marketplace add|list|upgrade|remove`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26234-26264` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “add and track a marketplace source.”
- **does**: Registers, inspects, refreshes, or removes local and Git-backed marketplace sources from the CLI.
- **spark**: S=2 P=4 A=5 R=8 K=1
- **why**: S changes available plugin supply; P gives the user catalog-source authority; A manages source lifecycle; R reaches local or remote marketplaces; K reports resolved source roots
- **rent**: none — source management has no per-turn cost until plugins contribute context
- **composes**: [[Local_Plugin_Marketplace_Catalog]], [[Marketplace_Allowed_Source_Requirements]]
- **confidence**: documented

### Marketplace_Installed_Copy_Cache
- **surface**: `~/.codex/plugins/cache/$MARKETPLACE_NAME/$PLUGIN_NAME/$VERSION/`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:26545-26549` ([official page](https://developers.openai.com/plugins/build/plugins.md), snapshot 2026-09-02) — “loads the installed copy from that cache path.”
- **does**: Copies an installed marketplace plugin into a versioned Codex cache used at runtime.
- **spark**: S=1 P=0 A=4 R=8 K=0
- **why**: S materializes the package for use; A separates source from installed state; R provides the runtime plugin files
- **rent**: once_at_install — installation creates the cached package copy
- **composes**: [[Local_Plugin_Marketplace_Catalog]], [[Plugin_New_Session_Activation]]
- **confidence**: documented

### Codex_CLI_Plugin_Browser
- **surface**: `/plugins`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30110-30122` ([official page](https://learn.chatgpt.com/docs/plugins.md), snapshot 2026-09-02) — “install or uninstall marketplace entries” and “turn it on or off.”
- **does**: Browses marketplace-grouped plugin details with install, uninstall, enable, or disable controls.
- **spark**: S=4 P=8 A=3 R=8 K=1
- **why**: S changes the active capability set; P puts plugin activation under user control; A provides a management workflow; R reaches catalog entries and installed bundles; K displays plugin details
- **rent**: none — browser management itself does not add recurring context
- **composes**: [[Universal_Plugin_Directory]], [[Plugin_New_Session_Activation]]
- **confidence**: documented

### Plugin_New_Session_Activation
- **surface**: new Codex chat or CLI session after plugin installation
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:29961-29963` ([official page](https://learn.chatgpt.com/docs/plugins.md), snapshot 2026-09-02) — “start a new session before using its bundled skills or tools.”
- **does**: Makes newly installed plugin contributions available only after a new session starts.
- **spark**: S=4 P=0 A=6 R=5 K=1
- **why**: S activates installed workflows; A defines the activation boundary; R refreshes bundled capability discovery; K refreshes bundled instructions
- **rent**: every_turn — activated plugin descriptors participate in subsequent session context
- **composes**: [[Codex_CLI_Plugin_Browser]], [[Plugin_Skills_Contribution_Path]]
- **confidence**: documented

### Plugin_Uninstall_Bundle_Scope
- **surface**: plugin browser → **Uninstall plugin**
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30152-30161` ([official page](https://learn.chatgpt.com/docs/plugins.md), snapshot 2026-09-02) — “bundled connectors stay connected until you manage them in ChatGPT.”
- **does**: Removes the plugin bundle without disconnecting connector accounts created through it.
- **spark**: S=2 P=8 A=3 R=5 K=0
- **why**: S removes bundled workflows; P separates uninstall authority from account-connection authority; A defines teardown scope; R removes local package reach while leaving external connections
- **rent**: none — removing the bundle ends its package-context cost
- **composes**: [[Codex_CLI_Plugin_Browser]], [[Connector_Connection_Management]]
- **confidence**: documented

### Plugin_Requirements_Kill_Switch
- **surface**: `requirements.toml` → `features.plugins = false`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36851-36863` ([official page](https://learn.chatgpt.com/docs/enterprise/security.md), snapshot 2026-09-02) — “turn off plugins in supported local clients.”
- **does**: Disables plugin availability for managed local Codex clients.
- **spark**: S=1 P=10 A=4 R=3 K=0
- **why**: S removes installed workflows; P assigns organization-level capability authority; A enforces a managed availability policy; R blocks plugin reach
- **rent**: none — disabled plugins contribute no runtime capability
- **composes**: [[Managed_Requirements]], [[Codex_CLI_Plugin_Browser]]
- **confidence**: documented

### Marketplace_Allowed_Source_Requirements
- **surface**: `requirements.toml` → `[marketplaces] restrict_to_allowed_sources` / `[marketplaces.allowed_sources.*]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36865-36903` ([official page](https://learn.chatgpt.com/docs/enterprise/security.md), snapshot 2026-09-02) — “reject unmatched marketplace add, plugin install, and configured Git marketplace refresh operations.”
- **does**: Restricts user-configured marketplace operations to approved Git repositories, host patterns, or absolute local paths.
- **spark**: S=1 P=10 A=6 R=5 K=0
- **why**: S gates installable workflows; P gives administrators source-approval authority; A enforces source matching at lifecycle operations; R bounds reachable catalogs
- **rent**: none — requirements gate operations without adding prompt context
- **composes**: [[Managed_Requirements]], [[Plugin_Marketplace_Source_Commands]], [[Local_Plugin_Marketplace_Catalog]]
- **confidence**: documented

## Uncovered
- No installation, enablement, or plugin/skill invocation was exercised because this arm was documentary-only; every primitive is therefore `documented`, not `observed`.
- The official manual snapshot is current to 2026-09-02, but it does not label each cited page with Codex Desktop `26.820.9563.0` or `codex-cli 0.150.0-alpha.8`; build-specific conformance remains unverified.
- MCP transport/tool/auth mechanics were excluded for D5, general configuration layering was excluded for D1, and hook behavior was excluded for D2.
- Memory guidance was searched only for inseparable coupling; no directly inseparable D4 capability was established, so no memory primitive was emitted.
- Plugin submission portal validation, public-review policy, and workspace GitHub-sync operations were not exhaustively decomposed because the requested bound was the most material architecture, manifest, catalog, and install-control surfaces.
