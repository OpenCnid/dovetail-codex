# I5 Plugins, Prompts, and Persistent Definitions

### Plugin_Catalog_List_Command
- **surface**: `codex plugin list [--marketplace <MARKETPLACE>] [--json] [--available]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, `codex plugin list --json` returned installed plugin IDs with `version`, `installed`, `enabled`, source paths, `installPolicy`, and `authPolicy`; `--help` says `--available` includes uninstalled marketplace plugins.
- **does**: Reports plugin availability and installation state from configured marketplaces.
- **spark**: S=0 P=0 A=1 R=6 K=4
- **why**: A=1 because marketplace filtering narrows inspection; R=6 because it exposes the plugin inventory surface; K=4 because it reports version, policy, and state metadata.
- **rent**: none — the read returns state without adding a persistent agent or user charge.
- **composes**: [[Marketplace_Manifest_Catalog]], [[Plugin_Add_Command]], [[Plugin_Remove_Command]]
- **confidence**: observed

### Marketplace_List_Command
- **surface**: `codex plugin marketplace list [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, the command returned `openai-primary-runtime`, `openai-bundled`, and `openai-curated` with their current absolute roots.
- **does**: Reports every marketplace source Codex is currently considering.
- **spark**: S=0 P=0 A=1 R=5 K=3
- **why**: A=1 because the source list guides later selection; R=5 because it exposes marketplace roots; K=3 because it identifies the active catalog set.
- **rent**: none — the read has no persistent charge.
- **composes**: [[Marketplace_Manifest_Catalog]], [[Marketplace_Add_Command]]
- **confidence**: observed

### Plugin_Add_Command
- **surface**: `codex plugin add <PLUGIN[@MARKETPLACE]> [--marketplace <MARKETPLACE>] [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, `plugin add --help` states: `Install a plugin from a configured marketplace snapshot.`
- **does**: Installs one selected plugin from a configured marketplace snapshot.
- **spark**: S=3 P=0 A=2 R=8 K=0
- **why**: S=3 because installation can add task capabilities; A=2 because the selector chooses a marketplace-scoped extension; R=8 because it expands the harness's reachable extension set.
- **rent**: once_at_install — the user pays the one-time bundle installation and local storage cost.
- **composes**: [[Plugin_Catalog_List_Command]], [[Versioned_Plugin_Cache]]
- **confidence**: documented

### Plugin_Remove_Command
- **surface**: `codex plugin remove <PLUGIN[@MARKETPLACE]> [--marketplace <MARKETPLACE>] [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, `plugin remove --help` states: `Remove an installed plugin from local config and cache.`
- **does**: Removes one selected plugin from local configuration and cache.
- **spark**: S=0 P=1 A=1 R=7 K=0
- **why**: P=1 because the user chooses which extension remains available; A=1 because marketplace scoping disambiguates the target; R=7 because removal contracts reachable plugin resources.
- **rent**: none — removal is a one-off action with no recurring charge.
- **composes**: [[Plugin_Catalog_List_Command]], [[Versioned_Plugin_Cache]]
- **confidence**: documented

### Marketplace_Add_Command
- **surface**: `codex plugin marketplace add <SOURCE> [--ref <REF>] [--sparse <PATH>] [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, help accepts a local path, `owner/repo[@ref]`, HTTPS Git URL, or SSH Git URL, with optional ref and repeated sparse paths.
- **does**: Registers one local or Git marketplace source.
- **spark**: S=1 P=0 A=3 R=8 K=3
- **why**: S=1 because registration enables later extension acquisition; A=3 because ref and sparse-path selection shape source acquisition; R=8 because it adds a new extension catalog; K=3 because the catalog supplies plugin metadata.
- **rent**: once_at_install — the user pays the one-time source registration and snapshot storage cost.
- **composes**: [[Marketplace_List_Command]], [[Marketplace_Manifest_Catalog]]
- **confidence**: documented

### Marketplace_Upgrade_Command
- **surface**: `codex plugin marketplace upgrade [MARKETPLACE_NAME] [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, help states that omitting the name refreshes all configured Git marketplace snapshots.
- **does**: Refreshes one or all configured Git marketplace snapshots.
- **spark**: S=0 P=0 A=2 R=6 K=4
- **why**: A=2 because the optional name scopes refresh; R=6 because it updates reachable catalog content; K=4 because it refreshes extension metadata.
- **rent**: every_matching_call — the user pays fetch and snapshot work on each explicit refresh.
- **composes**: [[Marketplace_Manifest_Catalog]], [[Plugin_Catalog_List_Command]]
- **confidence**: documented

### Marketplace_Remove_Command
- **surface**: `codex plugin marketplace remove <MARKETPLACE_NAME> [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, `marketplace remove --help` states: `Remove a configured marketplace source by name`.
- **does**: Removes one configured marketplace source.
- **spark**: S=0 P=1 A=1 R=6 K=0
- **why**: P=1 because the user controls which source remains trusted; A=1 because name selection scopes the action; R=6 because removal contracts the available catalogs.
- **rent**: none — source removal is a one-off action.
- **composes**: [[Marketplace_List_Command]]
- **confidence**: documented

### Marketplace_Manifest_Catalog
- **surface**: `.agents/plugins/marketplace.json`
- **evidence**: `C:\Users\Darian\.codex\.tmp\bundled-marketplaces\openai-bundled\.agents\plugins\marketplace.json` — The observed manifest has top-level keys `name`, `interface`, and `plugins`; `name` is `openai-bundled` and the `plugins` array contains seven local-source entries.
- **does**: Declares the named plugin entries supplied by one marketplace snapshot.
- **spark**: S=0 P=0 A=2 R=5 K=6
- **why**: A=2 because entries bind plugin names to selected sources; R=5 because the catalog makes packages addressable; K=6 because it records package categories and policies.
- **rent**: none — the declarative snapshot adds no per-turn charge by itself.
- **composes**: [[Marketplace_Installation_Policy]], [[Marketplace_Authentication_Policy]], [[Plugin_Package_Manifest]]
- **confidence**: observed

### Marketplace_Installation_Policy
- **surface**: `plugins[].policy.installation`
- **evidence**: `C:\Users\Darian\.codex\.tmp\bundled-marketplaces\openai-bundled\.agents\plugins\marketplace.json` — Observed plugin entries declare `"installation": "AVAILABLE"`.
- **does**: Declares how a marketplace plugin may enter the installed set.
- **spark**: S=0 P=7 A=3 R=1 K=0
- **why**: P=7 because installation policy governs extension authority; A=3 because it gates the acquisition path; R=1 because the resulting policy affects reach only downstream.
- **rent**: none — policy declaration itself has no recurring charge.
- **composes**: [[Plugin_Add_Command]], [[Plugin_Catalog_List_Command]]
- **confidence**: observed

### Marketplace_Authentication_Policy
- **surface**: `plugins[].policy.authentication`
- **evidence**: `C:\Users\Darian\.cache\codex-runtimes\codex-primary-runtime\plugins\openai-primary-runtime\.agents\plugins\marketplace.json` — Observed entries declare `"authentication": "ON_USE"`; bundled entries at `C:\Users\Darian\.codex\.tmp\bundled-marketplaces\openai-bundled\.agents\plugins\marketplace.json` declare `"authentication": "ON_INSTALL"`.
- **does**: Declares when a plugin's authentication boundary is encountered.
- **spark**: S=0 P=8 A=3 R=1 K=0
- **why**: P=8 because the policy determines when the user is asked for authority; A=3 because it gates installation or first use; R=1 because access is the downstream effect.
- **rent**: none — the policy value itself adds no recurring charge.
- **composes**: [[Plugin_Add_Command]], [[App_Connection_Flow]]
- **confidence**: observed

### Plugin_Package_Manifest
- **surface**: `.codex-plugin/plugin.json`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\.codex-plugin\plugin.json` — The versioned manifest declares `name: browser`, `version: 26.820.71523`, description, author, license, keywords, contribution paths, and interface metadata.
- **does**: Identifies one versioned plugin package to Codex.
- **spark**: S=0 P=0 A=1 R=6 K=4
- **why**: A=1 because contribution pointers organize loading; R=6 because the manifest makes the package discoverable; K=4 because it describes identity and version.
- **rent**: none — parsing static package metadata is not a recurring capability charge.
- **composes**: [[Plugin_Skill_Root_Declaration]], [[Plugin_App_Manifest_Declaration]], [[Plugin_Interface_Metadata]]
- **confidence**: observed

### Plugin_Skill_Root_Declaration
- **surface**: `.codex-plugin/plugin.json:skills`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-primary-runtime\documents\26.826.12353\.codex-plugin\plugin.json` — The manifest contains `"skills": "./skills/"`.
- **does**: Points Codex at a plugin's skill-definition root.
- **spark**: S=2 P=0 A=1 R=7 K=1
- **why**: S=2 because loading the referenced definitions can add task ability; A=1 because the pointer participates in contribution discovery; R=7 because it exposes a package resource tree; K=1 because domain content is downstream.
- **rent**: none — this declaration adds no charge; skill loading and its rent belong to I4.
- **composes**: [[Skill_Discovery]], [[Plugin_Package_Manifest]]
- **confidence**: observed

### Plugin_App_Manifest_Declaration
- **surface**: `.codex-plugin/plugin.json:apps`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\sites\0.1.43\.codex-plugin\plugin.json` — The manifest contains `"apps": "./.app.json"`.
- **does**: Points Codex at a plugin's app declaration.
- **spark**: S=0 P=0 A=1 R=8 K=0
- **why**: A=1 because the pointer participates in contribution discovery; R=8 because it links the plugin to an external-app surface.
- **rent**: none — the pointer itself adds no recurring charge; app-call mechanics belong to I7.
- **composes**: [[App_Connector_Manifest]], [[Plugin_Package_Manifest]]
- **confidence**: observed

### Plugin_Interface_Metadata
- **surface**: `.codex-plugin/plugin.json:interface`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\visualize\1.0.22\.codex-plugin\plugin.json` — The observed interface declares `displayName`, short and long descriptions, category, capabilities, URLs, icons, brand color, screenshots, and `defaultPrompt` entries.
- **does**: Supplies user-facing presentation metadata for a plugin.
- **spark**: S=0 P=3 A=2 R=3 K=2
- **why**: P=3 because names, prompts, and descriptions frame interaction; A=2 because capability labels and prompt suggestions steer selection; R=3 because icons and links populate discovery surfaces; K=2 because descriptive metadata explains the package.
- **rent**: none — interface metadata is presented without recurring agent context charge.
- **composes**: [[Plugin_Catalog_List_Command]], [[Agent_Interface_Default_Prompt]]
- **confidence**: observed

### Versioned_Plugin_Cache
- **surface**: `%CODEX_HOME%\plugins\cache\<source>\<plugin>\<version>\`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache` — The observed tree stores bundled, curated-remote, and primary-runtime packages under provider/plugin/version paths; `chrome\latest` is a junction to `chrome\26.820.71523`.
- **does**: Persists version-addressed plugin bundles on local disk.
- **spark**: S=0 P=0 A=2 R=7 K=1
- **why**: A=2 because source and version partition package selection; R=7 because cached bundles make extension assets locally reachable; K=1 because versions retain provenance metadata.
- **rent**: once_at_install — the user pays local disk storage when a bundle is materialized.
- **composes**: [[Plugin_Package_Manifest]], [[Remote_Plugin_Origin_Marker]]
- **confidence**: observed

### Remote_Plugin_Origin_Marker
- **surface**: `.codex-remote-plugin-install.json`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-curated-remote\plugin-management\.codex-remote-plugin-install.json` — The observed marker contains `"schema_version": 1` and remote plugin ID `plugin_connector_1p_b3438d6beb9081918fba3625bc988128`.
- **does**: Associates one cached remote plugin bundle with its catalog identifier.
- **spark**: S=0 P=0 A=2 R=5 K=4
- **why**: A=2 because the mapping joins two install representations; R=5 because it connects local content to remote identity; K=4 because it preserves origin provenance.
- **rent**: once_at_install — the user pays a small persistent marker at materialization time.
- **composes**: [[Remote_Plugin_Catalog_Cache]], [[Versioned_Plugin_Cache]]
- **confidence**: observed

### Remote_Plugin_Catalog_Cache
- **surface**: `%CODEX_HOME%\cache\remote_plugin_catalog\*.json`
- **evidence**: `C:\Users\Darian\.codex\cache\remote_plugin_catalog\6c467d3b1134c502.json` — Schema version 1 was fetched at `2026-09-02T17:54:13.586709500Z` and contains 3,525 plugin records with identity, scope, discoverability, installation/authentication policy, status, and release metadata.
- **does**: Caches a remotely fetched plugin-discovery catalog locally.
- **spark**: S=0 P=0 A=2 R=6 K=8
- **why**: A=2 because policy and status support selection; R=6 because the cache exposes remotely cataloged extensions; K=8 because it stores thousands of structured plugin records.
- **rent**: none — inspecting the existing cache adds no recurring charge.
- **composes**: [[Remote_Plugin_Origin_Marker]], [[Plugin_Catalog_List_Command]]
- **confidence**: observed

### Plugin_Slash_Command_Definition
- **surface**: `/<command-name>` from `plugins/<plugin>/commands/*.md`
- **evidence**: `C:\Users\Darian\.codex\.tmp\plugins\plugins\figma\commands\implement-from-figma.md` — The observed file begins `# /implement-from-figma`, defines named arguments and workflow steps, and says to delegate substantial work to `figma-implementation-agent`.
- **does**: Stores a reusable named workflow as a plugin-provided slash command.
- **spark**: S=5 P=0 A=7 R=2 K=4
- **why**: S=5 because invocation supplies a task workflow; A=7 because the file fixes sequencing and escalation; R=2 because it references plugin resources; K=4 because it carries domain-specific argument and procedure knowledge.
- **rent**: every_matching_call — the agent pays the command workflow context when the slash command is invoked.
- **composes**: [[Plugin_Agent_Instruction_Definition]], [[Plugin_Add_Command]]
- **confidence**: observed

### Plugin_Agent_Instruction_Definition
- **surface**: `plugins/<plugin>/agents/<agent-name>.md`
- **evidence**: `C:\Users\Darian\.codex\.tmp\plugins\plugins\figma\agents\figma-implementation-agent.md` — The observed reusable definition specifies a purpose, mandatory rules, component-reuse behavior, deviation reporting, and a five-part output format.
- **does**: Persists role instructions for a named plugin-provided agent.
- **spark**: S=6 P=3 A=8 R=1 K=4
- **why**: S=6 because the role specializes implementation behavior; P=3 because explicit reporting rules shape address to the user; A=8 because mandatory flow and output structure govern execution; R=1 because referenced tools are downstream; K=4 because the file embeds Figma-specific implementation guidance.
- **rent**: every_spawn — the spawned agent pays the definition's instruction context.
- **composes**: [[Plugin_Slash_Command_Definition]], [[Subagent_Spawn]]
- **confidence**: observed

### Agent_Interface_Default_Prompt
- **surface**: `plugins/<plugin>/agents/openai.yaml:interface.default_prompt`
- **evidence**: `C:\Users\Darian\.codex\.tmp\plugins\plugins\figma\agents\openai.yaml` — The observed interface defines display name `Figma`, a short description, two icon paths, and default prompt `Use Figma to inspect the target design and translate it into implementable UI decisions.`
- **does**: Supplies a reusable starting prompt for a plugin's agent-facing interface.
- **spark**: S=1 P=4 A=4 R=1 K=2
- **why**: S=1 because the prompt activates an existing plugin ability; P=4 because it frames how the agent is presented; A=4 because it seeds a specific inspect-then-translate method; R=1 because icons populate the selection surface; K=2 because the prompt identifies the design domain.
- **rent**: every_matching_call — the agent pays the prompt context when the default prompt is selected.
- **composes**: [[Plugin_Interface_Metadata]], [[Plugin_Agent_Instruction_Definition]]
- **confidence**: observed

## Uncovered
- Personal marketplace configuration was searched through `codex plugin marketplace list` and `C:\Users\Darian\.codex\.tmp\marketplaces`; only the three OpenAI-provided marketplaces were listed and the personal snapshot directory was empty.
- Personal custom definitions were searched at `C:\Users\Darian\.codex\prompts`, `C:\Users\Darian\.codex\commands`, `C:\Users\Darian\.codex\agents`, and `C:\Users\Darian\.codex\.agents`; none of these paths existed, so no personal prompt, command, or reusable-agent primitive was emitted.
- Plugin installation, removal, marketplace mutation, authentication, connection, and command/agent invocation were not exercised because this arm was read-only; their help text or file definitions remain documented/observed rather than runtime-validated.
- Skill internals, MCP/app execution mechanics, AGENTS.md, settings, and hooks were intentionally not surveyed because they belong to I4, I7, and I6.
