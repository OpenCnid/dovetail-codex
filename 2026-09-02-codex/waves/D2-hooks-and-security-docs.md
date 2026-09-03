# D2 Hooks, Permissions, Sandbox, and Security Docs

Comparison pin: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; survey date 2026-09-02.

### Sandbox_Mode_Control
- **surface**: `sandbox_mode = "read-only" | "workspace-write" | "danger-full-access"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:10916` — “The sandbox is the boundary that lets the agent act autonomously without giving it unrestricted access to your machine.”
- **does**: Defines the technical filesystem/network boundary for model-generated commands.
- **spark**: S=0 P=9 A=4 R=5 K=0
- **why**: P governs the agent's technical authority; A gates autonomous execution; R bounds reachable local resources
- **rent**: every_matching_call — the agent pays sandbox enforcement on each local command
- **composes**: [[Approval_Policy_Control]], [[Cross_Platform_Sandbox_Enforcement]]
- **confidence**: documented

### Approval_Policy
- **surface**: `approval_policy = "untrusted" | "on-request" | "never"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11076` — “The common approval policies are” followed by `untrusted`, `on-request`, and `never`.
- **does**: Determines when Codex pauses for authority before an action.
- **spark**: S=0 P=10 A=5 R=1 K=0
- **why**: P decides who must authorize action; A inserts an execution gate; R indirectly unlocks sandbox exceptions
- **rent**: every_matching_call — the user pays attention whenever the active policy surfaces a prompt
- **composes**: [[Sandbox_Mode_Control]], [[Automatic_Approval_Reviewer]], [[Command_Prefix_Rule]]
- **confidence**: documented

### Granular_Approval_Policy
- **surface**: `approval_policy = { granular = { sandbox_approval, rules, mcp_elicitations, request_permissions, skill_approval } }`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11397` — “allow or auto-reject specific prompt categories while keeping other prompts interactive.”
- **does**: Keeps selected approval categories interactive while failing other categories closed.
- **spark**: S=0 P=10 A=6 R=1 K=0
- **why**: P allocates decision authority by prompt class; A adds category-specific gates; R controls exception reach
- **rent**: every_matching_call — the agent evaluates the category for each approval-eligible request
- **composes**: [[Approval_Policy_Control]], [[PermissionRequest_Hook]]
- **confidence**: documented

### Automatic_Approval_Reviewer
- **surface**: `approvals_reviewer = "auto_review"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9781` — “Auto-review replaces manual approval at the sandbox boundary with a separate reviewer agent.”
- **does**: Routes eligible boundary-crossing requests to a separate reviewer agent.
- **spark**: S=1 P=10 A=8 R=1 K=1
- **why**: S adds automated risk review; P replaces the human reviewer; A delegates a gate to another agent; R exposes compact review evidence; K supplies policy context
- **rent**: every_matching_call — extra reviewer model calls consume Codex usage for each eligible request
- **composes**: [[Approval_Policy_Control]], [[Automatic_Review_Fail_Closed]], [[Managed_Reviewer_Policy]]
- **confidence**: documented

### No_Prompt_Sandboxed_Autonomy
- **surface**: `--ask-for-approval never` or `-a never`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9489` — “This option works with all `--sandbox` modes.”
- **does**: Suppresses approval prompts without removing the selected sandbox.
- **spark**: S=0 P=10 A=6 R=1 K=0
- **why**: P removes user interruption; A forces best-effort autonomy; R remains bounded by the sandbox
- **rent**: every_matching_call — the agent absorbs denied operations instead of asking the user
- **composes**: [[Sandbox_Mode_Control]], [[Approval_Policy_Control]]
- **confidence**: documented

### Dangerous_Full_Access_Bypass
- **surface**: `--dangerously-bypass-approvals-and-sandbox` or `--yolo`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9557` — “No sandbox; no approvals.”
- **does**: Runs the invocation with unrestricted authority.
- **spark**: S=0 P=10 A=7 R=10 K=0
- **why**: P delegates unrestricted authority; A removes execution gates; R exposes host filesystem plus network reach
- **rent**: every_matching_call — the user bears the risk of every unrestricted action
- **composes**: [[Sandbox_Mode_Control]], [[Approval_Policy_Control]]
- **confidence**: documented

### Permission_Profile_System
- **surface**: `default_permissions = "<profile>"` plus `[permissions.<profile>]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:10178` — “A profile is a named policy that combines filesystem rules” with network rules.
- **does**: Applies a reusable least-privilege policy to local sandboxed commands.
- **spark**: S=0 P=9 A=4 R=7 K=0
- **why**: P defines delegated command authority; A standardizes an execution posture; R bounds filesystem/network resources
- **rent**: every_matching_call — every sandboxed command inherits the active profile
- **composes**: [[Filesystem_Access_Rule_Precedence]], [[Command_Network_Access_Toggle]]
- **confidence**: documented

### Permission_Profile_Legacy_Exclusion
- **surface**: `default_permissions` versus `sandbox_mode` / `sandbox_workspace_write`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:10162` — “Configure either `default_permissions` and `[permissions]`, or `sandbox_mode` / `sandbox_workspace_write`, but not both.”
- **does**: Makes legacy sandbox settings take precedence over local permission profiles.
- **spark**: S=0 P=8 A=5 R=4 K=0
- **why**: P resolves which authority system governs; A selects one policy path; R determines the effective resource boundary
- **rent**: every_turn — Codex resolves the active policy system when loading a session
- **composes**: [[Permission_Profile_System]], [[Sandbox_Mode_Control]]
- **confidence**: documented

### Filesystem_Access_Rule_Precedence
- **surface**: `[permissions.<profile>.filesystem]` values `read`, `write`, or `deny`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:10357` — “More specific entries override broader entries” with “`deny` takes precedence over `write`.”
- **does**: Resolves per-path command access through specificity plus deny-first precedence.
- **spark**: S=0 P=9 A=4 R=8 K=0
- **why**: P authorizes reads or mutations by path; A evaluates layered rules; R precisely bounds filesystem reach
- **rent**: every_matching_call — path authorization runs for each sandboxed filesystem access
- **composes**: [[Permission_Profile_System]], [[Filesystem_Deny_Read_Globs]]
- **confidence**: documented

### Filesystem_Deny_Read_Globs
- **surface**: `"**/*.env" = "deny"` plus `glob_scan_max_depth`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:10451` — “`deny` glob patterns are supported as deny-read rules.”
- **does**: Removes matching sensitive files from broader readable or writable roots.
- **spark**: S=0 P=9 A=3 R=7 K=0
- **why**: P withholds read authority; A carves exceptions from broad grants; R blocks credential-bearing resources
- **rent**: every_turn — Linux, WSL, and native Windows may pre-expand globs before sandbox startup
- **composes**: [[Filesystem_Access_Rule_Precedence]], [[Managed_Deny_Read_Requirement]]
- **confidence**: documented

### Command_Network_Access_Toggle
- **surface**: `permissions.<profile>.network.enabled = true`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:10343` — “Enables network access for commands in the profile. It does not start the network proxy.”
- **does**: Grants outbound network access to commands in the active profile.
- **spark**: S=0 P=9 A=2 R=9 K=0
- **why**: P grants network authority; A changes execution posture; R opens outbound resources
- **rent**: every_matching_call — each command may use the granted network path
- **composes**: [[Command_Network_Proxy_Enforcement]], [[Network_Domain_Pattern_Rules]]
- **confidence**: documented

### Command_Network_Proxy_Enforcement
- **surface**: `features.network_proxy = true` or `[features.network_proxy] enabled = true`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9337` — “The feature changes how enabled network access is enforced; it does not grant network access by itself.”
- **does**: Routes enabled command traffic through the configured destination policy.
- **spark**: S=0 P=8 A=4 R=8 K=0
- **why**: P enforces destination authority; A inserts a network gate; R constrains outbound reach
- **rent**: every_matching_call — proxy policy applies to each sandboxed network request
- **composes**: [[Command_Network_Access_Toggle]], [[Network_Domain_Pattern_Rules]]
- **confidence**: documented

### Network_Domain_Pattern_Rules
- **surface**: `[permissions.<profile>.network.domains]` or `features.network_proxy.domains`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9377` — “Domain rules are allowlist-first” and “`deny` always wins over `allow`.”
- **does**: Filters command destinations with exact hosts plus scoped wildcard patterns.
- **spark**: S=0 P=9 A=4 R=9 K=0
- **why**: P decides which destinations receive authority; A applies ordered policy; R narrows network reach
- **rent**: every_matching_call — the proxy matches every outbound command destination
- **composes**: [[Command_Network_Proxy_Enforcement]], [[Local_Private_Network_Guard]]
- **confidence**: documented

### Local_Private_Network_Guard
- **surface**: `allow_local_binding = false`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9391` — “blocks loopback, link-local, and private destinations.”
- **does**: Blocks local/private destinations unless an exact local target is intentionally allowed.
- **spark**: S=0 P=9 A=3 R=8 K=0
- **why**: P withholds authority to local services; A adds a rebinding guard; R prevents private-network reach
- **rent**: every_matching_call — each proxied destination receives local/private classification
- **composes**: [[Network_Domain_Pattern_Rules]]
- **confidence**: documented

### Protected_Workspace_Control_Paths
- **surface**: default `workspace-write` protection for `/.git`, `/.agents`, and `/.codex`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9479` — “writable roots still include protected paths” whose protection “is recursive.”
- **does**: Keeps repository-control directories read-only inside writable roots.
- **spark**: S=0 P=9 A=3 R=7 K=0
- **why**: P withholds mutation authority over control state; A preserves a default guardrail; R limits filesystem reach
- **rent**: every_matching_call — writes beneath protected paths are denied
- **composes**: [[Sandbox_Mode_Control]], [[Filesystem_Access_Rule_Precedence]]
- **confidence**: documented

### Command_Network_Proxy_Scope
- **surface**: `features.network_proxy`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9441` — “It does not filter web search, app or connector tool calls, MCP server connections, browser or Computer Use activity.”
- **does**: Limits proxy enforcement to local command traffic inside the sandbox.
- **spark**: S=0 P=8 A=3 R=8 K=0
- **why**: P delineates which actions the policy governs; A separates capability controls; R identifies the bounded network surface
- **rent**: every_matching_call — only sandboxed command traffic pays proxy enforcement
- **composes**: [[Command_Network_Proxy_Enforcement]]
- **confidence**: documented

### Cloud_Setup_Agent_Phase_Boundary
- **surface**: Codex cloud environment internet/secrets settings
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9291` — “Secrets configured for cloud environments are available only during setup and are removed before the agent phase starts.”
- **does**: Separates networked dependency setup from the default-offline agent phase.
- **spark**: S=0 P=8 A=6 R=8 K=0
- **why**: P constrains agent-phase authority; A stages execution into two phases; R removes secrets plus default network reach from the agent
- **rent**: every_turn — each cloud task pays the two-phase environment transition
- **composes**: [[Command_Network_Proxy_Scope]]
- **confidence**: documented

### Cross_Platform_Sandbox_Enforcement
- **surface**: `codex sandbox macos|linux|windows`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:9616` — “macOS uses Seatbelt,” “Linux uses `bwrap` plus `seccomp`,” while native Windows uses a Windows sandbox.
- **does**: Enforces the selected local sandbox through platform-specific OS mechanisms.
- **spark**: S=0 P=8 A=4 R=7 K=0
- **why**: P makes authority OS-enforced; A selects a platform implementation; R constrains host resources
- **rent**: every_matching_call — each local command runs through the platform sandbox
- **composes**: [[Sandbox_Mode_Control]], [[Native_Windows_Sandbox_Implementation]]
- **confidence**: documented

### Native_Windows_Sandbox_Implementation
- **surface**: `[windows] sandbox = "elevated" | "unelevated"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:39379` — “`elevated` is the preferred native Windows sandbox” while “`unelevated` is the fallback.”
- **does**: Selects the stronger dedicated-user sandbox or the restricted-token fallback on native Windows.
- **spark**: S=0 P=9 A=5 R=8 K=0
- **why**: P selects the Windows authority boundary; A chooses the enforcement path; R constrains filesystem plus network access
- **rent**: every_matching_call — Windows commands run under the selected implementation
- **composes**: [[Cross_Platform_Sandbox_Enforcement]], [[Native_Windows_Private_Desktop]]
- **confidence**: documented

### Prefix_Command_Rule
- **surface**: `prefix_rule(pattern = [...], decision = ..., justification = ...)`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28676` — “Use rules to control which commands Codex can run outside the sandbox.”
- **does**: Matches an argument-prefix policy against a requested command escalation.
- **spark**: S=0 P=10 A=6 R=2 K=0
- **why**: P determines command authority; A inserts a reusable policy gate; R unlocks only matched command execution
- **rent**: every_matching_call — requested commands are compared with active prefix rules
- **composes**: [[Approval_Policy_Control]], [[Command_Rule_Decision_Precedence]]
- **confidence**: documented

### Command_Rule_Decision_Precedence
- **surface**: `decision = "allow" | "prompt" | "forbidden"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28731` — “Codex applies the most restrictive decision” in the order “`forbidden` > `prompt` > `allow`.”
- **does**: Resolves overlapping command rules through a restrictive decision lattice.
- **spark**: S=0 P=10 A=6 R=1 K=0
- **why**: P selects who may authorize a command; A deterministically merges policy gates; R controls the matched escape
- **rent**: every_matching_call — multiple matches are reduced for each candidate command
- **composes**: [[Command_Prefix_Rule]], [[Managed_Restrictive_Command_Rules]]
- **confidence**: documented

### Shell_Compound_Command_Decomposition
- **surface**: rules applied to `bash -lc`, `bash -c`, `zsh`, or `sh` wrappers
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28748` — Codex “splits it into individual commands before applying your rules” when the script is a safe linear chain.
- **does**: Evaluates safely parseable compound shell commands as separate rule subjects.
- **spark**: S=1 P=9 A=7 R=1 K=0
- **why**: S parses shell structure; P prevents smuggled authority; A decomposes the command before policy evaluation; R protects the escape surface
- **rent**: every_matching_call — wrapped shell scripts pay parsing plus per-command rule evaluation
- **composes**: [[Command_Prefix_Rule]], [[Command_Rule_Decision_Precedence]]
- **confidence**: documented

### Managed_Restrictive_Command_Rules
- **surface**: `[rules] prefix_rules = [{ pattern = ..., decision = "prompt" | "forbidden" }]` in `requirements.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36800` — “requirements rules must specify `decision`” as “`prompt` or `forbidden` (not `allow`).”
- **does**: Merges administrator-enforced restrictive prefix rules with regular rule files.
- **spark**: S=0 P=10 A=7 R=1 K=0
- **why**: P reserves command authority to administrators or users; A composes enforced gates; R restricts outside-sandbox execution
- **rent**: every_matching_call — enforced rules participate in every command decision
- **composes**: [[Command_Prefix_Rule]], [[Requirements_Enforced_Constraints]]
- **confidence**: documented

### Hook_Source_Layering
- **surface**: `hooks.json` or inline `[hooks]` beside active config layers
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23146` — “If more than one hook source exists, Codex loads all matching hooks.”
- **does**: Aggregates lifecycle hooks across active trusted configuration layers.
- **spark**: S=7 P=4 A=8 R=4 K=1
- **why**: S adds lifecycle-script abilities; P requires trusted project layers; A composes enforcement sources; R reaches scripts plus tools; K can inject context
- **rent**: every_turn — Codex discovers hook sources at startup
- **composes**: [[Hook_Hash_Trust_Review]], [[Hook_Matcher_Filter]]
- **confidence**: documented

### Hook_Hash_Trust_Review
- **surface**: `/hooks`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23178` — “Codex records trust against the hook's current hash” so changed hooks are “skipped until trusted.”
- **does**: Gates non-managed hook execution on review of the exact current definition.
- **spark**: S=0 P=10 A=7 R=2 K=0
- **why**: P assigns execution authority to the user; A adds a hash-bound trust gate; R controls script/tool reach
- **rent**: once_at_install — the user reviews each new or changed hook definition
- **composes**: [[Hook_Source_Layering]], [[Hook_Trust_Bypass]]
- **confidence**: documented

### Hook_Trust_Bypass
- **surface**: `--dangerously-bypass-hook-trust`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23192` — “run enabled hooks without requiring persisted hook trust for that invocation.”
- **does**: Bypasses persisted trust checks for enabled hooks in one invocation.
- **spark**: S=0 P=10 A=6 R=6 K=0
- **why**: P removes user review authority; A bypasses the trust gate; R exposes hook script/tool reach
- **rent**: every_matching_call — the user bears risk from every hook run in the bypassed invocation
- **composes**: [[Hook_Hash_Trust_Review]]
- **confidence**: documented

### Hook_Matcher_Filter
- **surface**: hook-group `matcher = "<regex>"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23519` — “The `matcher` field is a regex string that filters when hooks fire.”
- **does**: Filters supported lifecycle events by event-specific values.
- **spark**: S=3 P=3 A=8 R=1 K=0
- **why**: S targets hook behavior; P scopes enforcement authority; A conditions lifecycle execution; R selects event data
- **rent**: every_matching_call — each supported event is tested against configured regexes
- **composes**: [[Hook_Source_Layering]], [[PreToolUse_Hook]], [[PermissionRequest_Hook]]
- **confidence**: documented

### Hook_Command_Handler
- **surface**: `type = "command"` with `command`, `command_windows`, `timeout`, and `statusMessage`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23294` — “`timeout` is in seconds” while “Commands run with the session `cwd`.”
- **does**: Runs an external command handler for a matching lifecycle event.
- **spark**: S=8 P=5 A=8 R=8 K=1
- **why**: S adds arbitrary scripted checks; P lets handlers gate supported events; A inserts code into lifecycle; R reaches local execution; K can return context
- **rent**: every_matching_call — the agent pays command execution for each matching event
- **composes**: [[Hook_Matcher_Filter]], [[Hook_Concurrent_Matching_Handlers]]
- **confidence**: documented

### Hook_Concurrent_Matching_Handlers
- **surface**: multiple matching hook groups for one event
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23131` — “Multiple matching command hooks for the same event are launched concurrently.”
- **does**: Launches all matching command hooks for one event concurrently.
- **spark**: S=1 P=3 A=9 R=3 K=0
- **why**: S supports multiple checks; P means no hook can prevent peers from starting; A parallelizes event handling; R consumes concurrent local execution
- **rent**: every_matching_call — every matching handler consumes process resources
- **composes**: [[Command_Hook_Handler]], [[Hook_Matcher_Filter]]
- **confidence**: documented

### PreToolUse_Control_Hook
- **surface**: `hooks.PreToolUse`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23853` — “`PreToolUse` can intercept Bash, file edits performed through `apply_patch`, MCP tool calls, and other local function tools.”
- **does**: Blocks or rewrites a supported tool call before execution.
- **spark**: S=7 P=10 A=9 R=5 K=2
- **why**: S adds programmable interception; P authorizes or denies tool use; A gates pre-execution flow; R controls tool reach; K can add model-visible context
- **rent**: every_matching_call — synchronous handlers run before each matched tool call
- **composes**: [[Hook_Matcher_Filter]], [[Command_Hook_Handler]]
- **confidence**: documented

### PermissionRequest_Decision_Hook
- **surface**: `hooks.PermissionRequest`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23935` — “It can allow the request, deny the request, or decline to decide and let the normal approval prompt continue.”
- **does**: Adjudicates an approval request before the normal prompt surfaces.
- **spark**: S=6 P=10 A=9 R=2 K=1
- **why**: S adds programmable approval policy; P may replace the user's decision; A inserts a pre-prompt gate; R controls an escalation; K reads request context
- **rent**: every_matching_call — hooks execute for each matched approval request
- **composes**: [[Approval_Policy_Control]], [[PreToolUse_Hook]]
- **confidence**: documented

### PostToolUse_Feedback_Hook
- **surface**: `hooks.PostToolUse`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23995` — “It can't undo side effects from a tool that already ran.”
- **does**: Replaces completed tool feedback before subsequent model processing.
- **spark**: S=6 P=6 A=8 R=4 K=3
- **why**: S adds result validation; P controls what feedback advances; A gates post-execution flow; R receives tool output; K injects review context
- **rent**: every_matching_call — handlers inspect every matched tool result
- **composes**: [[Hook_Matcher_Filter]], [[PreToolUse_Hook]]
- **confidence**: documented

### UserPromptSubmit_Guard_Hook
- **surface**: `hooks.UserPromptSubmit`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:24098` — “Plain text on `stdout` is added as extra developer context” and a block decision can reject the prompt.
- **does**: Mediates a submitted prompt before model delivery.
- **spark**: S=6 P=10 A=8 R=1 K=7
- **why**: S adds prompt scanning; P can veto user input; A gates prompt submission; R reads the prompt; K injects policy context
- **rent**: every_matching_call — every submitted prompt triggers configured handlers
- **composes**: [[Command_Hook_Handler]], [[Hook_Output_Spilling]]
- **confidence**: documented

### SessionStart_Context_Hook
- **surface**: `hooks.SessionStart`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23753` — “Plain text on `stdout` is added as extra developer context.”
- **does**: Injects developer context when a session starts, resumes, clears, or continues after compaction.
- **spark**: S=5 P=5 A=7 R=2 K=8
- **why**: S adds startup initialization; P influences agent framing; A runs before model continuation; R can read session assets; K supplies persistent context
- **rent**: every_turn — startup-like session transitions execute matching handlers
- **composes**: [[Hook_Matcher_Filter]], [[PreCompact_Hook]], [[PostCompact_Hook]]
- **confidence**: documented

### SessionEnd_Hook
- **surface**: `hooks.SessionEnd`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:23786` — “`SessionEnd` lets you run a command when a session ends” while its output “won't steer Codex or keep the thread open.”
- **does**: Runs advisory finalization work when the main session ends.
- **spark**: S=6 P=1 A=7 R=6 K=3
- **why**: S adds end-of-session automation; P is advisory only; A attaches work to termination; R reaches local persistence; K can save final notes
- **rent**: every_turn — one synchronous handler run is charged at session end
- **composes**: [[Command_Hook_Handler]]
- **confidence**: documented

### PreCompact_Gate_Hook
- **surface**: `hooks.PreCompact`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:24062` — “If a matching `PreCompact` hook returns `continue: false`, Codex stops before compacting.”
- **does**: Gates chat compaction before it occurs.
- **spark**: S=4 P=7 A=8 R=1 K=5
- **why**: S adds compaction policy; P authorizes context transformation; A intercepts lifecycle; R reads session metadata; K protects retained context
- **rent**: every_matching_call — each manual or automatic compaction runs matching hooks
- **composes**: [[PostCompact_Hook]], [[SessionStart_Hook]]
- **confidence**: documented

### PostCompact_Gate_Hook
- **surface**: `hooks.PostCompact`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:24080` — “`PostCompact` runs after Codex compacts the chat.”
- **does**: Runs lifecycle policy immediately after chat compaction.
- **spark**: S=4 P=5 A=8 R=1 K=6
- **why**: S adds post-compaction processing; P can stop after transformation; A attaches work to lifecycle completion; R reads event data; K can restore context
- **rent**: every_matching_call — each manual or automatic compaction runs matching hooks
- **composes**: [[PreCompact_Hook]], [[SessionStart_Hook]]
- **confidence**: documented

### Stop_Continuation_Hook
- **surface**: `hooks.Stop`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:24170` — a block decision “tells Codex to continue and automatically creates a new continuation prompt.”
- **does**: Converts a would-be turn stop into a policy-supplied continuation prompt.
- **spark**: S=5 P=9 A=9 R=1 K=4
- **why**: S adds completion enforcement; P overrides the agent's stop decision; A creates a new continuation turn; R reads the last message; K supplies continuation rationale
- **rent**: every_matching_call — each attempted stop can trigger more model work
- **composes**: [[Command_Hook_Handler]]
- **confidence**: documented

### Requirements_Enforced_Constraints
- **surface**: `requirements.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36311` — “Requirements constrain security-sensitive settings” and conflicting values fall back to a compatible value.
- **does**: Enforces administrator constraints that local users cannot override.
- **spark**: S=0 P=10 A=8 R=6 K=0
- **why**: P reserves authority to administrators; A normalizes conflicting configuration; R constrains security-sensitive surfaces
- **rent**: every_turn — clients compose requirements during startup
- **composes**: [[Requirements_Layer_Precedence]], [[Managed_Hook_Enforcement]], [[Managed_Restrictive_Command_Rules]]
- **confidence**: documented

### Requirements_Layer_Precedence
- **surface**: system, cloud, legacy managed, and MDM `requirements.toml` layers
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36324` — “Higher-precedence layers override ordinary scalar and list values” while tables merge by key.
- **does**: Composes administrator requirements through documented source precedence.
- **spark**: S=0 P=9 A=8 R=3 K=0
- **why**: P resolves which administrator owns a conflict; A layers multiple policy sources; R determines effective constrained surfaces
- **rent**: every_turn — clients resolve all requirement layers at startup
- **composes**: [[Requirements_Enforced_Constraints]], [[Cloud_Managed_Requirements_Fail_Closed]]
- **confidence**: documented

### Cloud_Managed_Requirements_Fail_Closed
- **surface**: cloud-managed `requirements.toml` bundle
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36387` — without a valid cache, load failure “returns an error rather than silently starting without the cloud-managed requirements layer.”
- **does**: Refuses startup when applicable cloud policy cannot be resolved from network or cache.
- **spark**: S=0 P=10 A=8 R=2 K=0
- **why**: P preserves administrator authority; A fails startup closed; R relies on a signed policy cache
- **rent**: every_turn — startup pays cache validation plus possible network retrieval
- **composes**: [[Requirements_Layer_Precedence]]
- **confidence**: documented

### Managed_Permission_Profile_Allowlist
- **surface**: `[allowed_permission_profiles]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36466` — “omitted or set to `false`” profiles are denied, “including built-ins added in future Codex versions.”
- **does**: Defines the complete administrator-approved set of selectable permission profiles.
- **spark**: S=0 P=10 A=6 R=7 K=0
- **why**: P controls user-selectable authority; A applies an allowlist; R limits available resource boundaries
- **rent**: every_turn — profile selection is validated against managed policy
- **composes**: [[Permission_Profile_System]], [[Requirements_Enforced_Constraints]]
- **confidence**: documented

### Managed_Network_Requirements
- **surface**: `[experimental_network]` in `requirements.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36608` — these requirements “can configure sandbox networking without that feature flag” but “don't grant command network access.”
- **does**: Enforces administrator-owned command-network proxy policy independently of the user proxy feature toggle.
- **spark**: S=0 P=10 A=7 R=9 K=0
- **why**: P reserves destination authority to admins; A installs managed enforcement; R constrains command network reach
- **rent**: every_matching_call — managed proxy policy applies to sandboxed command traffic
- **composes**: [[Command_Network_Access_Toggle]], [[Network_Domain_Pattern_Rules]], [[Requirements_Enforced_Constraints]]
- **confidence**: documented

### Managed_Reviewer_Policy
- **surface**: `allowed_approvals_reviewers` plus `guardian_policy_config`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36707` — managed `guardian_policy_config` “takes precedence over local `[auto_review].policy`.”
- **does**: Enforces the organization's automatic-review regime.
- **spark**: S=1 P=10 A=8 R=1 K=6
- **why**: S customizes automated review; P controls reviewer authority; A enforces the review route; R governs escalations; K supplies organization risk rules
- **rent**: every_matching_call — each eligible approval pays reviewer inference under managed policy
- **composes**: [[Automatic_Approval_Reviewer]], [[Requirements_Enforced_Constraints]]
- **confidence**: documented

### Managed_Deny_Read_Requirement
- **surface**: `[permissions.filesystem] deny_read = [...]` in `requirements.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36734` — “Users can't weaken these requirements with local configuration.”
- **does**: Enforces administrator-owned filesystem read denials.
- **spark**: S=0 P=10 A=6 R=8 K=0
- **why**: P reserves read authority to administrators; A overrides local policy; R blocks sensitive filesystem resources
- **rent**: every_matching_call — enforceable file reads are checked against managed denials
- **composes**: [[Filesystem_Deny_Read_Globs]], [[Requirements_Enforced_Constraints]]
- **confidence**: documented

### Managed_Hook_Enforcement
- **surface**: `[hooks]`, `[features] hooks = true`, and `allow_managed_hooks_only = true` in `requirements.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:36756` — managed-only mode “skips hooks from user, project, session, and plugin sources” while loading managed hooks.
- **does**: Restricts lifecycle enforcement to administrator-managed hooks.
- **spark**: S=7 P=10 A=9 R=7 K=2
- **why**: S adds mandatory policy scripts; P reserves hook authority to admins; A inserts enforced lifecycle handlers; R executes managed scripts; K can inject managed context
- **rent**: every_matching_call — every matched lifecycle event runs enforced handlers
- **composes**: [[Requirements_Enforced_Constraints]], [[Hook_Source_Layering]], [[Hook_Hash_Trust_Review]]
- **confidence**: documented

## Uncovered
- Runtime behavior was not exercised because this arm was explicitly documentary-only; all 46 primitives therefore remain `documented`.
- Subagent lifecycle semantics were left to D3, while MCP/plugin packaging and tool governance were left to D4/D5; only their hook-facing composition edges are named here.
- Codex Security scanning-product documentation was excluded because it is a separate product surface rather than the local harness authority boundary.
- The manual is fresh on 2026-09-02 but is not release-stamped to Codex Desktop 26.820.9563.0 or codex-cli 0.150.0-alpha.8; exact build wire formats and runtime parity remain unverified.
- Hook coverage is explicitly non-exhaustive: the manual says specialized tool paths can opt out and calls tool hooks a guardrail rather than a complete enforcement boundary.
