# I6 Settings, Permissions, Guidance, and Hooks

Target: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; config root `C:\Users\Darian\.codex`; surveyed 2026-09-02 at repository commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`.

### User_Config_Toml_Layer
- **surface**: `~/.codex/config.toml`
- **evidence**: `C:\Users\Darian\.codex\config.toml` — Read structure only: top-level keys and tables were present; values were intentionally not emitted (codex-cli 0.150.0-alpha.8).
- **does**: Supplies user-level defaults across Codex projects.
- **spark**: S=0 P=1 A=5 R=2 K=0
- **why**: P shapes user-default interaction settings; A establishes a reusable configuration approach; R exposes a local control surface.
- **rent**: none — Codex loads the local file without a recurring user or agent charge.
- **composes**: [[Project_Config_Toml_Layer]], [[Named_Config_Profile]]
- **confidence**: observed

### Project_Config_Toml_Layer
- **surface**: `<repo>/.codex/config.toml`
- **evidence**: `https://learn.chatgpt.com/docs/config-file/config-basic#configuration-precedence` — “Project config files: `.codex/config.toml`” are ordered root-to-current-directory, closest first.
- **does**: Overrides broader configuration with trusted project-scoped settings.
- **spark**: S=0 P=2 A=7 R=2 K=0
- **why**: P makes trust a prerequisite; A layers settings by repository depth; R adds a repository-local surface.
- **rent**: none — Codex resolves the files at session startup.
- **composes**: [[Project_Trust_Gate]], [[User_Config_Toml_Layer]]
- **confidence**: documented

### Command_Line_Config_Override
- **surface**: `-c, --config <key=value>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` exposed dotted-path TOML overrides in codex-cli 0.150.0-alpha.8.
- **does**: Overrides one configuration value for a Codex invocation.
- **spark**: S=0 P=1 A=7 R=1 K=0
- **why**: P can alter authority-related settings; A enables one-run configuration steering; R exposes a CLI surface.
- **rent**: none — the override is parsed once for the invocation.
- **composes**: [[Configuration_Precedence]], [[Strict_Config_Validation]]
- **confidence**: observed

### Named_Config_Profile
- **surface**: `-p, --profile <CONFIG_PROFILE_V2>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` said it layers `$CODEX_HOME/<name>.config.toml` over base user config (codex-cli 0.150.0-alpha.8).
- **does**: Applies a named reusable configuration overlay.
- **spark**: S=0 P=1 A=7 R=2 K=0
- **why**: P can package authority defaults; A selects repeatable operating postures; R adds file-backed presets.
- **rent**: none — the profile is loaded once per invocation.
- **composes**: [[User_Config_Toml_Layer]], [[Approval_Policy]], [[Legacy_Sandbox_Mode]]
- **confidence**: observed

### Configuration_Precedence
- **surface**: `CLI > project .codex/config.toml > profile > user config > system config > defaults`
- **evidence**: `https://learn.chatgpt.com/docs/config-file/config-basic#configuration-precedence` — The page enumerates that six-level precedence order.
- **does**: Resolves conflicting configuration values by source priority.
- **spark**: S=0 P=2 A=8 R=1 K=0
- **why**: P resolves conflicting authority settings; A deterministically composes configuration layers; R joins several control surfaces.
- **rent**: none — resolution occurs during configuration loading.
- **composes**: [[Command_Line_Config_Override]], [[Project_Config_Toml_Layer]], [[Named_Config_Profile]]
- **confidence**: documented

### Strict_Config_Validation
- **surface**: `--strict-config`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` exposed “Error out” for unrecognized config fields (codex-cli 0.150.0-alpha.8).
- **does**: Rejects configuration containing fields unknown to the installed CLI.
- **spark**: S=0 P=0 A=6 R=1 K=0
- **why**: A makes config-version validation fail closed; R exposes a diagnostic control.
- **rent**: none — validation is a startup check.
- **composes**: [[User_Config_Toml_Layer]], [[Command_Line_Config_Override]]
- **confidence**: observed

### Project_Trust_Gate
- **surface**: `projects.<path>.trust_level`
- **evidence**: `https://learn.chatgpt.com/docs/config-file/config-reference#configtoml` — Untrusted projects skip project-local config, hooks, and rules.
- **does**: Gates loading of project-scoped Codex control files on project trust.
- **spark**: S=0 P=9 A=4 R=0 K=0
- **why**: P decides whether repository authors receive configuration authority; A gates three extension layers together.
- **rent**: none — trust is checked while loading project layers.
- **composes**: [[Project_Config_Toml_Layer]], [[Hook_Source_Layering]], [[Rules_Layer_Discovery]]
- **confidence**: documented

### Approval_Policy
- **surface**: `approval_policy` / `--ask-for-approval <APPROVAL_POLICY>`
- **evidence**: `https://learn.chatgpt.com/docs/config-file/config-reference#configtoml` — The key “controls when Codex pauses for approval.”
- **does**: Selects when Codex asks before executing an action.
- **spark**: S=0 P=10 A=3 R=0 K=0
- **why**: P determines when the user retains decision authority; A gates action sequencing around approval.
- **rent**: every_matching_call — eligible actions may consume reviewer or user attention.
- **composes**: [[Approval_Reviewer_Routing]], [[Legacy_Sandbox_Mode]], [[Prefix_Command_Rule]]
- **confidence**: documented

### Granular_Approval_Policy
- **surface**: `approval_policy = { granular = { sandbox_approval, rules, mcp_elicitations, request_permissions, skill_approval } }`
- **evidence**: `https://learn.chatgpt.com/docs/config-file/config-reference#configtoml` — Each boolean allows its prompt category to surface instead of being auto-rejected.
- **does**: Enables approval prompts independently by request category.
- **spark**: S=0 P=10 A=5 R=0 K=0
- **why**: P assigns user authority per prompt class; A separates otherwise coupled approval flows.
- **rent**: every_matching_call — enabled categories may interrupt the user for a decision.
- **composes**: [[Approval_Policy]], [[PermissionRequest_Decision_Hook]]
- **confidence**: documented

### Approval_Reviewer_Routing
- **surface**: `approvals_reviewer = "user" | "auto_review"`
- **evidence**: `https://learn.chatgpt.com/docs/agent-approvals-security#automatic-approval-reviews` — Eligible interactive requests can route to the user or a reviewer agent.
- **does**: Chooses who reviews eligible approval requests.
- **spark**: S=0 P=10 A=4 R=0 K=0
- **why**: P transfers decision authority between human and reviewer agent; A inserts an automatic review step.
- **rent**: every_matching_call — the selected reviewer spends attention or model work.
- **composes**: [[Approval_Policy]], [[Guardian_Approval_Feature]]
- **confidence**: documented

### Legacy_Sandbox_Mode
- **surface**: `sandbox_mode = "read-only" | "workspace-write" | "danger-full-access"` / `--sandbox`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` listed all three modes in codex-cli 0.150.0-alpha.8.
- **does**: Selects the filesystem and network boundary for model-generated commands.
- **spark**: S=0 P=8 A=2 R=4 K=0
- **why**: P sets the agent's local authority boundary; A applies a consistent execution posture; R changes reachable local resources.
- **rent**: every_matching_call — the sandbox boundary is enforced for each local command.
- **composes**: [[Approval_Policy]], [[Sandbox_Command_Execution]]
- **confidence**: observed

### Permission_Profile_Selection
- **surface**: `default_permissions = "<profile>"`
- **evidence**: `https://learn.chatgpt.com/docs/permissions#define-and-select-a-profile` — Built-ins are `:read-only`, `:workspace`, and `:danger-full-access`.
- **does**: Selects one named filesystem-and-network permission posture.
- **spark**: S=0 P=9 A=4 R=3 K=0
- **why**: P chooses a reusable authority envelope; A unifies two policy dimensions; R changes command reach.
- **rent**: every_matching_call — the selected profile constrains every sandboxed command.
- **composes**: [[Permission_Profile_Filesystem_Policy]], [[Permission_Profile_Network_Policy]]
- **confidence**: documented

### Permission_Profile_Legacy_Exclusion
- **surface**: `default_permissions` versus `sandbox_mode` / `[sandbox_workspace_write]`
- **evidence**: `https://learn.chatgpt.com/docs/permissions` — “Permission profiles do not compose with the older sandbox settings.”
- **does**: Selects legacy sandbox settings instead of permission profiles when both are configured.
- **spark**: S=0 P=8 A=7 R=0 K=0
- **why**: P prevents ambiguous authority composition; A defines an exclusive configuration branch.
- **rent**: none — the branch is selected during configuration loading.
- **composes**: [[Permission_Profile_Selection]], [[Legacy_Sandbox_Mode]]
- **confidence**: documented

### Permission_Profile_Inheritance
- **surface**: `permissions.<name>.extends`
- **evidence**: `https://learn.chatgpt.com/docs/permissions#configuration-spec` — Profiles may extend `:read-only`, `:workspace`, or another profile, but not `:danger-full-access`.
- **does**: Derives a custom permission profile from a safer named baseline.
- **spark**: S=0 P=7 A=7 R=1 K=0
- **why**: P carries inherited authority constraints; A supports incremental policy composition; R reuses existing profiles.
- **rent**: none — inheritance resolves while loading configuration.
- **composes**: [[Permission_Profile_Selection]], [[Permission_Profile_Filesystem_Policy]]
- **confidence**: documented

### Permission_Profile_Filesystem_Policy
- **surface**: `[permissions.<name>.filesystem]` with `read | write | deny`
- **evidence**: `https://learn.chatgpt.com/docs/permissions#filesystem-permissions` — More-specific entries override broad ones; `deny` wins at equal specificity.
- **does**: Grants or denies sandboxed command access by filesystem path.
- **spark**: S=0 P=9 A=4 R=5 K=0
- **why**: P determines file authority; A supports broad grants with narrow carve-outs; R controls filesystem reach.
- **rent**: every_matching_call — each sandboxed file access is checked against the policy.
- **composes**: [[Permission_Profile_Selection]], [[Sandbox_Command_Execution]]
- **confidence**: documented

### Permission_Profile_Network_Policy
- **surface**: `[permissions.<name>.network.domains]` plus `features.network_proxy`
- **evidence**: `https://learn.chatgpt.com/docs/permissions#network-permissions` — Domain rules are enforced only when command network and the proxy are active.
- **does**: Filters sandboxed command destinations through domain allow and deny rules.
- **spark**: S=0 P=9 A=4 R=6 K=0
- **why**: P determines outbound authority; A requires coordinated permission and proxy gates; R controls network reach.
- **rent**: every_matching_call — proxied command traffic is checked by destination.
- **composes**: [[Permission_Profile_Selection]], [[Network_Proxy_Feature]]
- **confidence**: documented

### Prefix_Command_Rule
- **surface**: `prefix_rule(pattern=..., decision="allow"|"prompt"|"forbidden", ...)`
- **evidence**: `https://learn.chatgpt.com/docs/agent-configuration/rules#understand-rule-fields` — Multiple matches resolve `forbidden > prompt > allow`.
- **does**: Chooses allow, prompt, or block for matching command prefixes outside the sandbox.
- **spark**: S=0 P=10 A=6 R=0 K=0
- **why**: P encodes command-specific authority; A evaluates the most restrictive matching decision.
- **rent**: every_matching_call — command arguments are evaluated and prompts may consume user attention.
- **composes**: [[Approval_Policy]], [[Rules_Layer_Discovery]], [[PermissionRequest_Decision_Hook]]
- **confidence**: documented

### Rules_Layer_Discovery
- **surface**: `rules/*.rules` next to active config layers
- **evidence**: `https://learn.chatgpt.com/docs/agent-configuration/rules#create-a-rules-file` — Codex scans `rules/` under every active layer at startup.
- **does**: Loads command rules from user, team, and trusted project configuration layers.
- **spark**: S=0 P=8 A=6 R=2 K=0
- **why**: P admits multiple policy authors by scope; A composes rules from active layers; R exposes rule files.
- **rent**: none — discovery occurs at startup.
- **composes**: [[Prefix_Command_Rule]], [[Project_Trust_Gate]]
- **confidence**: documented

### Managed_Requirements_Composition
- **surface**: `%ProgramData%\OpenAI\Codex\requirements.toml`, cloud requirements, legacy managed fields, MDM requirements
- **evidence**: `https://learn.chatgpt.com/docs/enterprise/managed-configuration#locations-and-precedence` — Requirements compose from four ordered administrator sources.
- **does**: Combines administrator-enforced constraints across supported delivery layers.
- **spark**: S=0 P=10 A=7 R=1 K=0
- **why**: P reserves policy authority for administrators; A merges ordered requirement sources; R adds system and cloud policy surfaces.
- **rent**: none — requirements compose during client configuration loading.
- **composes**: [[Managed_Permission_Profile_Allowlist]], [[Managed_Feature_Constraints]], [[Managed_Hooks_Only]]
- **confidence**: documented

### Managed_Permission_Profile_Allowlist
- **surface**: `allowed_permission_profiles.<name> = true | false`
- **evidence**: `https://learn.chatgpt.com/docs/permissions#define-and-select-a-profile` — Once present, omitted profiles are denied; supported from Codex 0.138.0 onward.
- **does**: Restricts which built-in or custom permission profiles a managed user may select.
- **spark**: S=0 P=10 A=3 R=0 K=0
- **why**: P prevents users from broadening administrator-approved authority; A turns omission into denial.
- **rent**: none — the allowlist constrains profile selection.
- **composes**: [[Managed_Requirements_Composition]], [[Permission_Profile_Selection]]
- **confidence**: documented

### Managed_Feature_Constraints
- **surface**: `[features]` in `requirements.toml`
- **evidence**: `https://learn.chatgpt.com/docs/enterprise/managed-configuration` — Requirements can pin feature values while omitted keys remain unconstrained.
- **does**: Pins selected Codex feature flags for managed clients.
- **spark**: S=1 P=8 A=5 R=0 K=0
- **why**: S can disable whole capabilities; P gives administrators final choice; A enforces consistent rollout posture.
- **rent**: none — pinned flags are resolved during configuration loading.
- **composes**: [[Managed_Requirements_Composition]], [[Feature_Flag_Inventory]]
- **confidence**: documented

### Managed_Config_Defaults
- **surface**: `~/.codex/managed_config.toml` on Windows
- **evidence**: `https://learn.chatgpt.com/docs/enterprise/managed-configuration#managed-defaults-managed_configtoml` — Managed defaults override user config and CLI overrides at startup.
- **does**: Applies administrator-selected startup defaults above user configuration.
- **spark**: S=0 P=9 A=6 R=1 K=0
- **why**: P gives managed defaults priority over user intent; A defines a higher-precedence startup layer; R adds a managed file surface.
- **rent**: none — defaults apply at client startup.
- **composes**: [[User_Config_Toml_Layer]], [[Command_Line_Config_Override]]
- **confidence**: documented

### Global_AGENTS_Guidance
- **surface**: `$CODEX_HOME/AGENTS.override.md` or `$CODEX_HOME/AGENTS.md`
- **evidence**: `https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance` — Global discovery uses only the first non-empty override-or-base file.
- **does**: Injects persistent global guidance into Codex runs.
- **spark**: S=1 P=3 A=5 R=0 K=7
- **why**: S can teach repeatable working behaviors; P steers interaction conventions; A standardizes method; K adds durable user context.
- **rent**: every_turn — loaded guidance consumes model input context.
- **composes**: [[Project_AGENTS_Guidance_Chain]], [[Prompt_Instruction_Hierarchy]]
- **confidence**: documented

### Project_AGENTS_Guidance_Chain
- **surface**: `AGENTS.md` from project root through current directory
- **evidence**: `https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance` — Codex concatenates root-to-current-directory files; closer guidance appears later.
- **does**: Layers repository guidance by directory specificity.
- **spark**: S=1 P=2 A=7 R=0 K=8
- **why**: S provides project working abilities; P can specialize collaboration norms; A resolves scope by depth; K adds repository context.
- **rent**: every_turn — the merged chain consumes model input context.
- **composes**: [[Global_AGENTS_Guidance]], [[Project_Trust_Gate]]
- **confidence**: documented

### AGENTS_Override_And_Fallback_Order
- **surface**: `AGENTS.override.md > AGENTS.md > project_doc_fallback_filenames`
- **evidence**: `https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance` — Each directory contributes at most one file in that order.
- **does**: Chooses the most specific eligible guidance filename in each directory.
- **spark**: S=0 P=2 A=8 R=1 K=5
- **why**: P lets an override supersede normal guidance; A defines deterministic per-directory selection; R supports custom filenames; K selects instruction content.
- **rent**: none — filename selection occurs when the instruction chain is built.
- **composes**: [[Project_AGENTS_Guidance_Chain]]
- **confidence**: documented

### AGENTS_Context_Byte_Limit
- **surface**: `project_doc_max_bytes`
- **evidence**: `https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance` — Codex stops adding files at 32 KiB by default.
- **does**: Caps the combined project-guidance bytes added to model context.
- **spark**: S=0 P=0 A=3 R=5 K=4
- **why**: A truncates discovery deterministically; R budgets prompt context; K limits durable project knowledge.
- **rent**: every_turn — retained guidance consumes context on model requests.
- **composes**: [[Project_AGENTS_Guidance_Chain]], [[Context_Window]]
- **confidence**: documented

### Hook_Source_Layering
- **surface**: `hooks.json` or inline `[hooks]` beside active config layers
- **evidence**: `https://learn.chatgpt.com/docs/hooks#where-codex-looks-for-hooks` — All matching sources load; hooks from higher layers do not replace lower-layer hooks.
- **does**: Aggregates lifecycle handlers from active hook sources.
- **spark**: S=2 P=4 A=8 R=5 K=0
- **why**: S adds event-driven automation; P admits hooks only from active authority scopes; A composes all matches; R reaches scripts and connected tools.
- **rent**: every_matching_call — each matching source can launch work.
- **composes**: [[Project_Trust_Gate]], [[Hook_Event_Registry]], [[Plugin_Hook_Bundle]]
- **confidence**: documented

### Hook_Definition_Trust
- **surface**: `/hooks` trust review keyed to hook-definition hash
- **evidence**: `https://learn.chatgpt.com/docs/hooks#review-and-trust-hooks` — Changed non-managed definitions are skipped until their new hash is trusted.
- **does**: Requires explicit review before a non-managed hook definition can run.
- **spark**: S=0 P=10 A=5 R=0 K=0
- **why**: P keeps execution authority with the user; A gates lifecycle automation by content hash.
- **rent**: once_at_install — the user reviews each new or changed definition once.
- **composes**: [[Hook_Source_Layering]], [[Project_Trust_Gate]]
- **confidence**: documented

### Hook_Event_Registry
- **surface**: `hooks.<Event>`
- **evidence**: `https://learn.chatgpt.com/docs/hooks` — Events span tool use, approvals, compaction, prompts, sessions, subagents, and turn stop.
- **does**: Registers handlers at named Codex lifecycle points.
- **spark**: S=2 P=3 A=9 R=2 K=0
- **why**: S enables lifecycle automation; P includes authority-sensitive events; A inserts deterministic event gates; R connects configured handlers.
- **rent**: every_matching_call — each event checks registered handlers.
- **composes**: [[Hook_Matcher_Filter]], [[Hook_Command_Handler]], [[Hook_MCP_Tool_Handler]]
- **confidence**: documented

### Hook_Matcher_Filter
- **surface**: `hooks.<Event>[].matcher`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#matcher-patterns` — The field is regex; `*`, empty, or omission matches all supported occurrences.
- **does**: Filters hook invocation by event-specific attributes.
- **spark**: S=0 P=2 A=9 R=0 K=0
- **why**: P scopes authority-sensitive hooks; A routes lifecycle events through regex predicates.
- **rent**: every_matching_call — every eligible event is tested against the regex.
- **composes**: [[Hook_Event_Registry]]
- **confidence**: documented

### Hook_Command_Handler
- **surface**: `hooks.<Event>[].hooks[] { type = "command", command = ... }`
- **evidence**: `https://learn.chatgpt.com/docs/hooks` — Command handlers run with the session current working directory.
- **does**: Runs a configured process when a hook event matches.
- **spark**: S=4 P=4 A=7 R=7 K=0
- **why**: S adds arbitrary scripted checks; P may gate agent actions; A inserts an external step; R reaches local executables.
- **rent**: every_matching_call — each match consumes a process invocation and possible user attention.
- **composes**: [[Hook_Event_Registry]], [[Exec_Command_Tool]]
- **confidence**: documented

### Hook_MCP_Tool_Handler
- **surface**: `hooks.<Event>[].hooks[] { type = "mcp_tool", server = ..., tool = ..., input = ... }`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#mcp-tool-hooks` — It calls an already-connected server synchronously without starting or reconnecting it.
- **does**: Calls a connected MCP tool when a lifecycle event matches.
- **spark**: S=3 P=4 A=7 R=8 K=0
- **why**: S adds external validation actions; P lets results block supported flows; A inserts a synchronous gate; R reaches connected MCP tools.
- **rent**: every_matching_call — each match consumes an MCP tool invocation.
- **composes**: [[Hook_Event_Registry]], [[MCP_Server_Connection]]
- **confidence**: documented

### Hook_Handler_Type_Gating
- **surface**: `hooks.<Event>[].hooks[].type`
- **evidence**: `https://learn.chatgpt.com/docs/hooks` — `command` and `mcp_tool` run; `prompt` and `agent` are parsed but skipped.
- **does**: Restricts executable hook handlers to the supported command and MCP tool types.
- **spark**: S=0 P=3 A=8 R=0 K=0
- **why**: P prevents unsupported handler authority; A gates parsed definitions by implementation status.
- **rent**: none — unsupported handler types are skipped.
- **composes**: [[Hook_Command_Handler]], [[Hook_MCP_Tool_Handler]]
- **confidence**: documented

### PreToolUse_Control_Hook
- **surface**: `hooks.PreToolUse`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#pretooluse` — The event can intercept Bash, apply-patch edits, MCP calls, and local function tools.
- **does**: Blocks or rewrites supported tool input before execution.
- **spark**: S=1 P=10 A=9 R=0 K=0
- **why**: S adds policy transformation; P decides whether an action may proceed; A gates execution before side effects.
- **rent**: every_matching_call — matching handlers run before each supported tool call.
- **composes**: [[Hook_Matcher_Filter]], [[Hook_Command_Handler]], [[Apply_Patch_Tool]]
- **confidence**: documented

### PermissionRequest_Decision_Hook
- **surface**: `hooks.PermissionRequest`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#permissionrequest` — It may allow, deny, or defer to the normal approval prompt.
- **does**: Decides an approval request before it reaches the normal reviewer.
- **spark**: S=0 P=10 A=8 R=0 K=0
- **why**: P directly controls approval authority; A inserts a policy decision into the approval lifecycle.
- **rent**: every_matching_call — the hook runs for each approval-bound request.
- **composes**: [[Approval_Policy]], [[Approval_Reviewer_Routing]], [[Prefix_Command_Rule]]
- **confidence**: documented

### PostToolUse_Feedback_Hook
- **surface**: `hooks.PostToolUse`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#posttooluse` — It runs after tool output and “can't undo side effects.”
- **does**: Replaces model-visible tool feedback after a supported tool finishes.
- **spark**: S=1 P=5 A=8 R=0 K=2
- **why**: S adds post-execution validation; P can stop normal result processing; A gates continuation after execution; K changes the result shown to the model.
- **rent**: every_matching_call — matching handlers run after supported tool calls.
- **composes**: [[Hook_Matcher_Filter]], [[Tool_Call_Result]]
- **confidence**: documented

### SessionStart_Context_Hook
- **surface**: `hooks.SessionStart`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#sessionstart` — Handler output can add extra developer context for startup, resume, clear, or compact.
- **does**: Injects developer context when a session starts or resumes after compaction.
- **spark**: S=1 P=3 A=6 R=1 K=8
- **why**: S can install session-specific procedures; P can steer interaction; A runs at session entry; R reads handler output; K adds dynamic context.
- **rent**: every_matching_call — injected context consumes tokens on the next model request.
- **composes**: [[Session_Lifecycle]], [[Compaction]], [[Prompt_Instruction_Hierarchy]]
- **confidence**: documented

### UserPromptSubmit_Guard_Hook
- **surface**: `hooks.UserPromptSubmit`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#userpromptsubmit` — The event can add developer context or block the submitted prompt.
- **does**: Rejects a user prompt before model submission.
- **spark**: S=0 P=10 A=8 R=0 K=0
- **why**: P interposes policy between user intent and the model; A gates the turn before model execution.
- **rent**: every_matching_call — every submitted prompt can invoke configured handlers.
- **composes**: [[Prompt_Submission]], [[Hook_Command_Handler]]
- **confidence**: documented

### PreCompact_Gate_Hook
- **surface**: `hooks.PreCompact`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#precompact` — A matching handler can stop before manual or automatic compaction.
- **does**: Gates conversation compaction before it occurs.
- **spark**: S=0 P=4 A=9 R=0 K=1
- **why**: P lets policy prevent a context rewrite; A inserts a pre-compaction gate; K protects existing conversation state.
- **rent**: every_matching_call — handlers run for matching compaction attempts.
- **composes**: [[Compaction]], [[Hook_Matcher_Filter]]
- **confidence**: documented

### PostCompact_Gate_Hook
- **surface**: `hooks.PostCompact`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#postcompact` — A matching handler can stop continuation after compaction.
- **does**: Gates model continuation after conversation compaction.
- **spark**: S=0 P=4 A=9 R=0 K=1
- **why**: P lets policy halt continuation; A inserts a post-compaction gate; K reacts to rewritten conversation state.
- **rent**: every_matching_call — handlers run after matching compactions.
- **composes**: [[Compaction]], [[SessionStart_Context_Hook]]
- **confidence**: documented

### Stop_Continuation_Hook
- **surface**: `hooks.Stop`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#stop` — A block decision creates a new continuation prompt from the hook reason.
- **does**: Continues a stopped turn with a hook-supplied user prompt.
- **spark**: S=1 P=7 A=10 R=0 K=0
- **why**: S adds automatic completion enforcement; P lets policy defer turn completion; A creates another model step.
- **rent**: every_matching_call — continuation consumes another model turn.
- **composes**: [[Turn_Lifecycle]], [[Prompt_Submission]]
- **confidence**: documented

### Background_Hook_Mode
- **surface**: `hooks.<Event>[].hooks[].async = true`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#run-hooks-in-the-background` — Background handlers cannot block, approve, or rewrite the triggering operation.
- **does**: Runs a command hook without delaying its triggering operation.
- **spark**: S=0 P=2 A=9 R=2 K=0
- **why**: P removes synchronous control authority; A decouples handler completion; R permits up to eight concurrent background hooks per session.
- **rent**: every_matching_call — each match consumes a background process slot.
- **composes**: [[Hook_Command_Handler]], [[Hook_Event_Registry]]
- **confidence**: documented

### Hook_Additional_Context_Limit
- **surface**: `hooks.<Event>[].hooks[].additionalContextLimit`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#large-hook-output` — The default threshold is about 2500 tokens; oversized context is saved with a shorter preview.
- **does**: Limits how much hook-provided additional context enters the model directly.
- **spark**: S=0 P=0 A=3 R=7 K=4
- **why**: A applies per-handler output shaping; R budgets context and disk spill; K limits injected hook knowledge.
- **rent**: every_matching_call — retained context consumes model tokens and oversized output may consume disk.
- **composes**: [[Hook_Command_Handler]], [[Context_Window]]
- **confidence**: documented

### Windows_Hook_Command_Override
- **surface**: `commandWindows` / `command_windows`
- **evidence**: `https://learn.chatgpt.com/docs/hooks` — The handler may provide a Windows-only command override.
- **does**: Replaces a hook command specifically on Windows.
- **spark**: S=1 P=0 A=6 R=2 K=0
- **why**: S supports platform-specific execution; A selects the native command by OS; R reaches Windows executables.
- **rent**: every_matching_call — the selected Windows process runs for each match.
- **composes**: [[Hook_Command_Handler]]
- **confidence**: documented

### Managed_Hooks_Only
- **surface**: `allow_managed_hooks_only = true`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#managed-hooks-from-requirementstoml` — The setting ignores user, project, session, and plugin hooks while retaining administrator hooks.
- **does**: Restricts lifecycle automation to managed hook definitions.
- **spark**: S=0 P=10 A=6 R=0 K=0
- **why**: P reserves hook authority for administrators; A filters hook-source composition by management status.
- **rent**: none — source eligibility is resolved while loading hooks.
- **composes**: [[Managed_Requirements_Composition]], [[Hook_Source_Layering]]
- **confidence**: documented

### Hooks_Feature_Gate
- **surface**: `features.hooks = true | false`
- **evidence**: `https://learn.chatgpt.com/docs/hooks#turn-hooks-off` — Hooks are enabled by default and this canonical flag can turn them off.
- **does**: Enables or disables lifecycle hook loading and execution.
- **spark**: S=2 P=8 A=8 R=0 K=0
- **why**: S toggles lifecycle automation; P globally admits or denies hook authority; A gates the hook subsystem.
- **rent**: none — the flag itself has no recurring charge when hooks are disabled.
- **composes**: [[Hook_Source_Layering]], [[Managed_Feature_Constraints]]
- **confidence**: documented

### Feature_Flag_Inventory
- **surface**: `codex features list`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — In codex-cli 0.150.0-alpha.8 the command returned feature name, stage, and effective state; `hooks` was stable and enabled.
- **does**: Reports known feature flags with maturity stage and effective state.
- **spark**: S=0 P=0 A=3 R=5 K=2
- **why**: A supports rollout inspection; R exposes runtime feature controls; K reveals installed-build state.
- **rent**: none — the read-only command returns once.
- **composes**: [[Hooks_Feature_Gate]], [[Managed_Feature_Constraints]]
- **confidence**: observed

### Per_Invocation_Feature_Override
- **surface**: `--enable <FEATURE>` / `--disable <FEATURE>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` mapped these to `features.<name>=true|false` (codex-cli 0.150.0-alpha.8).
- **does**: Overrides one feature flag for the current invocation.
- **spark**: S=2 P=2 A=7 R=1 K=0
- **why**: S can expose or suppress a capability; P may alter authority-sensitive features; A supports one-run experiments; R exposes a CLI toggle.
- **rent**: none — the override applies only to the invocation.
- **composes**: [[Feature_Flag_Inventory]], [[Command_Line_Config_Override]]
- **confidence**: observed

### Guardian_Approval_Feature
- **surface**: `features.guardian_approval`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex features list` reported `guardian_approval` stable and enabled in codex-cli 0.150.0-alpha.8.
- **does**: Gates availability of automatic approval review.
- **spark**: S=0 P=9 A=5 R=0 K=0
- **why**: P controls delegated approval authority; A gates the reviewer step.
- **rent**: every_matching_call — enabled automatic reviews consume reviewer-model work.
- **composes**: [[Approval_Reviewer_Routing]], [[Managed_Feature_Constraints]]
- **confidence**: observed

## Uncovered
- No hook was executed and no setting was changed; lifecycle behavior remains documented rather than exercised.
- The bounded known-path check found no user `hooks.json`, project `.codex` config/hooks, profile file, Windows system `requirements.toml`, or Windows managed-config file; cloud-delivered requirements and MDM policy were not inspectable locally.
- The global `C:\Users\Darian\.codex\AGENTS.md` existed but was empty, and no project `AGENTS.md` existed at the repository root; effective guidance content therefore could not be attributed to those local files.
- User config values and all credential-bearing state were deliberately excluded; only key and table structure was inspected.
- Hook internals bundled inside plugins were left to I4/I5, MCP server configuration was left to I7, and command/sandbox enforcement execution was left to I2.
