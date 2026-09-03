# D3 Multi-Agent, Tasks, Projects, and Worktrees Docs

Documentary target pin: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; 2026-09-02. Evidence comes from the fresh official Codex manual cached on 2026-09-02. No capability was exercised.

### Parallel_Subagent_Workflow
- **surface**: `Delegate this work in parallel to subagents.`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:1989` — “ChatGPT Work and Codex can run subagent workflows by spawning specialized agents in parallel and then collecting their results in one response.”
- **does**: Delegates independent parts of a task to concurrently running agents.
- **spark**: S=2 P=0 A=10 R=3 K=0
- **why**: S adds delegated execution; A decomposes one task across parallel workers; R reaches additional model workers.
- **rent**: every_spawn — each subagent performs its own model and tool work, consuming additional tokens.
- **composes**: [[Subagent_Context_Isolation]], [[Subagent_Result_Consolidation]], [[Spawned_Agent_Thread_Limit]]
- **confidence**: documented

### Subagent_Context_Isolation
- **surface**: `Ask Codex to delegate independent parts of the work to subagents.`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2041` — “Subagent workflows help by moving noisy work off the main thread” and run specialized subagents for exploration, tests, or log analysis.
- **does**: Moves delegated intermediate work into separate agent threads.
- **spark**: S=0 P=0 A=9 R=2 K=0
- **why**: A isolates noisy execution from the coordinating thread; R provides a separate thread context.
- **rent**: every_spawn — each isolated thread carries its own model context.
- **composes**: [[Parallel_Subagent_Workflow]], [[Subagent_Result_Consolidation]], [[Subagent_Thread_Inspection]]
- **confidence**: documented

### Subagent_Result_Consolidation
- **surface**: `Wait for all agents, then summarize the findings.`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2134` — “When many agents are running, Codex waits until all requested results are available, then returns a consolidated response.”
- **does**: Collects requested subagent results into the main response.
- **spark**: S=2 P=0 A=9 R=1 K=0
- **why**: S synthesizes worker outputs; A coordinates the join barrier and final aggregation; R reaches returned child results.
- **rent**: every_spawn — consolidation follows the token-bearing work of every requested subagent.
- **composes**: [[Parallel_Subagent_Workflow]], [[Subagent_Context_Isolation]]
- **confidence**: documented

### Subagent_Thread_Inspection
- **surface**: `Open Subagents` / select a completed subagent
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2161` — “Open **Subagents** to see read-only **Active** and **Done** lists. Select a completed subagent to inspect its details and result.”
- **does**: Opens delegated agent status or result details for inspection.
- **spark**: S=0 P=1 A=6 R=5 K=0
- **why**: P exposes worker activity to user oversight; A makes delegated work inspectable; R reaches child-thread details.
- **rent**: none — inspection adds no documented recurring charge.
- **composes**: [[Subagent_Context_Isolation]], [[Subagent_Lifecycle_Control]]
- **confidence**: documented

### Subagent_Lifecycle_Control
- **surface**: `Ask Codex to steer a running subagent, stop it, or close completed subagent threads.`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2168` — “Ask Codex directly to steer a running subagent, stop it, or close completed subagent threads.”
- **does**: Applies a requested lifecycle action to a delegated agent thread.
- **spark**: S=0 P=6 A=8 R=2 K=0
- **why**: P keeps child execution interruptible by the user; A supports mid-work coordination; R addresses a running or completed child thread.
- **rent**: none — lifecycle control has no documented recurring charge.
- **composes**: [[Subagent_Thread_Inspection]], [[Parallel_Subagent_Workflow]]
- **confidence**: documented

### Agent_Thread_Switch_Command
- **surface**: `/agent`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2019` — “Use `/agent` to inspect and switch between agent threads while they run.”
- **does**: Switches the interactive CLI view among active agent threads.
- **spark**: S=0 P=1 A=7 R=5 K=0
- **why**: P lets the user choose the visible worker; A supports active coordination; R exposes another agent thread.
- **rent**: none — switching views has no documented recurring charge.
- **composes**: [[Subagent_Thread_Inspection]], [[Subagent_Lifecycle_Control]]
- **confidence**: documented

### Subagent_Permission_Inheritance
- **surface**: parent turn permission mode
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2181` — “Subagents inherit your current sandbox policy”; lines 2202–2205 add that parent-turn live sandbox and approval overrides are reapplied when a child is spawned.
- **does**: Applies the parent turn's live sandbox and approval policy to spawned agents.
- **spark**: S=0 P=10 A=4 R=1 K=0
- **why**: P preserves the user's authority boundary across delegation; A standardizes child execution policy; R constrains child reach.
- **rent**: none — policy inheritance itself has no documented recurring charge.
- **composes**: [[Parallel_Subagent_Workflow]], [[Custom_Agent_Config_Override]]
- **confidence**: documented

### Multi_Agent_Enable_Config
- **surface**: `agents.enabled`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2251` — “`agents.enabled` ... Enable or disable multi-agent tools”; line 2261 states that it defaults to `true`.
- **does**: Enables or disables Codex multi-agent tools globally.
- **spark**: S=0 P=4 A=9 R=5 K=0
- **why**: P governs whether delegated execution is permitted; A gates teamwork mechanisms; R gates the multi-agent tool surface.
- **rent**: none — the Boolean setting has no documented recurring charge.
- **composes**: [[Parallel_Subagent_Workflow]], [[Spawned_Agent_Thread_Limit]]
- **confidence**: documented

### Spawned_Agent_Thread_Limit
- **surface**: `agents.max_concurrent_threads_per_session`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2251` — “Cap concurrently open spawned-agent threads, excluding the primary.”
- **does**: Caps concurrently open spawned-agent threads per session.
- **spark**: S=0 P=3 A=9 R=5 K=0
- **why**: P lets the user bound delegation; A limits orchestration fan-out; R limits concurrent worker capacity.
- **rent**: none — the cap itself has no recurring charge.
- **composes**: [[Parallel_Subagent_Workflow]], [[Multi_Agent_Enable_Config]]
- **confidence**: documented

### Subagent_Model_Default
- **surface**: `agents.default_subagent_model`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2251` — “Set the default model for spawned agents”; line 2263 says explicit spawn values override it.
- **does**: Selects the default model used by spawned agents.
- **spark**: S=3 P=0 A=6 R=4 K=0
- **why**: S changes worker capability; A specializes delegated execution; R selects a model resource.
- **rent**: every_spawn — each spawned worker uses the selected model's token and latency profile.
- **composes**: [[Parallel_Subagent_Workflow]], [[Subagent_Reasoning_Default]], [[Custom_Agent_Config_Override]]
- **confidence**: documented

### Subagent_Reasoning_Default
- **surface**: `agents.default_subagent_reasoning_effort`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2251` — “Set the default reasoning effort for spawned agents”; lines 2101–2108 document parent inheritance and explicit overrides.
- **does**: Selects the default reasoning effort used by spawned agents.
- **spark**: S=3 P=0 A=6 R=3 K=0
- **why**: S changes worker reasoning depth; A tunes delegated roles; R changes per-worker compute use.
- **rent**: every_spawn — every spawned worker pays the selected reasoning-effort cost.
- **composes**: [[Parallel_Subagent_Workflow]], [[Subagent_Model_Default]], [[Custom_Agent_Config_Override]]
- **confidence**: documented

### Custom_Agent_File
- **surface**: `~/.codex/agents/<agent>.toml` / `.codex/agents/<agent>.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2220` — “Each file defines one custom agent”; lines 2229–2233 require `name`, `description`, and `developer_instructions`.
- **does**: Defines a named custom agent role for spawned sessions.
- **spark**: S=6 P=4 A=8 R=2 K=0
- **why**: S creates a specialized worker; P shapes its behavioral instructions; A adds a selectable team role; R registers a spawnable agent configuration.
- **rent**: every_spawn — the agent file loads as a configuration layer for each matching spawned session.
- **composes**: [[Custom_Agent_Scope]], [[Custom_Agent_Config_Override]], [[Parallel_Subagent_Workflow]]
- **confidence**: documented

### Custom_Agent_Scope
- **surface**: `~/.codex/agents/` / `.codex/agents/`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2220` — “add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents.”
- **does**: Scopes custom agent availability to a person or project.
- **spark**: S=0 P=3 A=7 R=4 K=0
- **why**: P separates personal control from shared project control; A determines which roles a project can coordinate; R governs configuration discovery reach.
- **rent**: every_spawn — matching scope determines which role configuration can load for each spawn.
- **composes**: [[Custom_Agent_File]], [[Project_Shared_Context]]
- **confidence**: documented

### Custom_Agent_Config_Override
- **surface**: custom agent TOML keys such as `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2235` — custom-agent model settings take precedence; lines 2243–2245 state that omitted session settings inherit from the parent; line 2275 lists supported override examples.
- **does**: Applies a role-specific Codex session configuration to a spawned agent.
- **spark**: S=6 P=5 A=8 R=7 K=0
- **why**: S changes role capabilities; P can narrow a child's sandbox; A specializes worker behavior; R selects tools, skills, servers, and models.
- **rent**: every_spawn — each matching spawn loads the configured model, tools, and instructions.
- **composes**: [[Custom_Agent_File]], [[Subagent_Permission_Inheritance]], [[Subagent_Model_Default]], [[Subagent_Reasoning_Default]]
- **confidence**: documented

### Project_Shared_Context
- **surface**: `Projects` > project > `Chats` / `Sources`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2446` — a project's Chats and Sources sections hold chats and connected context, while “Project instructions apply across its chats.”
- **does**: Makes project files, instructions, and sources available across related chats.
- **spark**: S=0 P=0 A=4 R=9 K=1
- **why**: A coordinates related outcomes through shared context; R exposes shared files, instructions, and sources; K adds durable project-specific reference context.
- **rent**: every_turn — shared project instructions and selected context can accompany work in project chats.
- **composes**: [[Chat_Transcript_Isolation]], [[Local_Project_Folder_Set]], [[Primary_Project_Folder]]
- **confidence**: documented

### Chat_Transcript_Isolation
- **surface**: `New chat` within a project
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2470` — “Start a separate chat for each distinct outcome so its messages and results stay focused while the project keeps related work organized”; lines 2493–2496 state that each chat keeps its own transcript.
- **does**: Keeps each project chat's transcript separate from sibling chats.
- **spark**: S=0 P=0 A=8 R=3 K=0
- **why**: A isolates distinct outcomes within shared project coordination; R provides separate conversation contexts.
- **rent**: every_turn — each chat maintains its own model context.
- **composes**: [[Project_Shared_Context]], [[Chat_Fork]], [[Parallel_Goal_Context_Isolation]]
- **confidence**: documented

### Multi_Folder_Local_Project
- **surface**: `Edit project` > `Add folder`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2544` — “Select **Add folder** to attach multiple folders. ChatGPT can read and change files in every attached folder.”
- **does**: Attaches multiple local folders to one Codex project.
- **spark**: S=0 P=0 A=4 R=10 K=0
- **why**: A groups related repositories for one body of work; R expands project file reach to every attached folder.
- **rent**: none — folder attachment has no documented recurring charge.
- **composes**: [[Project_Shared_Context]], [[Primary_Project_Folder]], [[Worktree_Chat_Isolation]]
- **confidence**: documented

### Primary_Project_Folder
- **surface**: `Edit project` > folder > `Make primary`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2549` — “To change the default working directory, point to a folder and select **Make primary**”; lines 2554–2558 make it the default for new chats, Git, and automatic project-file discovery.
- **does**: Selects the default working directory and discovery root for a local project.
- **spark**: S=0 P=0 A=5 R=9 K=0
- **why**: A anchors project execution in one folder; R determines default file, Git, and configuration reach.
- **rent**: every_turn — new project chats inherit this working-directory and discovery choice.
- **composes**: [[Local_Project_Folder_Set]], [[Project_Shared_Context]], [[Worktree_Starting_Branch]]
- **confidence**: documented

### Chat_Fork
- **surface**: `/fork`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18019` — “Codex clones the current chat into a new chat with a fresh ID, leaving the original transcript untouched so you can explore an alternative approach in parallel.”
- **does**: Branches the current transcript into a separate persistent chat.
- **spark**: S=0 P=0 A=9 R=4 K=0
- **why**: A supports parallel alternative approaches without altering the source; R creates a separately addressable chat context.
- **rent**: none — the fork operation has no documented recurring charge.
- **composes**: [[Chat_Transcript_Isolation]], [[Ephemeral_Side_Chat]], [[Worktree_Chat_Isolation]]
- **confidence**: documented

### Ephemeral_Side_Chat
- **surface**: `/side` / `/btw`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18038` — “Use `/side` to start an ephemeral fork from the current chat”; lines 18046–18048 state that its transcript is separate while the parent status remains visible.
- **does**: Opens a temporary transcript-isolated detour from the current chat.
- **spark**: S=0 P=0 A=9 R=4 K=0
- **why**: A separates a focused follow-up without disrupting main work; R provides a temporary forked context.
- **rent**: every_matching_call — model work in the side chat consumes its own turn context.
- **composes**: [[Chat_Fork]], [[Chat_Transcript_Isolation]]
- **confidence**: documented

### Worktree_Chat_Isolation
- **surface**: new chat > `Worktree`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18489` — “Worktrees let Codex run multiple independent chats in the same project without interfering with each other”; line 18500 explains that each worktree has its own file checkout.
- **does**: Gives a chat an independent Git checkout within the same project.
- **spark**: S=1 P=0 A=10 R=9 K=0
- **why**: S permits isolated code changes; A prevents parallel chat interference; R supplies a separate repository checkout.
- **rent**: every_spawn — each worktree chat allocates another repository copy plus any dependencies or caches.
- **composes**: [[Chat_Transcript_Isolation]], [[Worktree_Starting_Branch]], [[Worktree_Local_Handoff]], [[Local_Environment_Setup_Script]]
- **confidence**: documented

### Worktree_Starting_Branch
- **surface**: new worktree chat > branch selector
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18523` — the user chooses the Git branch that bases the worktree, including the current branch with unstaged local changes; line 18529 states that Codex creates the worktree from that selection in detached HEAD by default.
- **does**: Selects the Git state used to initialize a new worktree chat.
- **spark**: S=0 P=2 A=6 R=8 K=0
- **why**: P lets the user choose the execution baseline; A establishes an isolated branch of work; R exposes the selected repository state.
- **rent**: none — selecting a base adds no charge beyond worktree creation.
- **composes**: [[Worktree_Chat_Isolation]], [[Primary_Project_Folder]]
- **confidence**: documented

### Worktree_Local_Handoff
- **surface**: chat header > `Hand off` > `Local` / `Worktree`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18556` — “select **Hand off** in the chat header and move it to **Local**”; lines 18562–18566 say Codex moves the chat safely and returns it to the same associated worktree later.
- **does**: Moves a chat and its Git work between its local checkout and associated worktree.
- **spark**: S=1 P=3 A=9 R=8 K=0
- **why**: S preserves executable work across environments; P makes location user-selectable; A moves work between foreground and background; R transfers chat and Git state.
- **rent**: none — handoff has no documented recurring charge.
- **composes**: [[Worktree_Chat_Isolation]], [[Cross_Host_Chat_Handoff]], [[Permanent_Worktree_Project]]
- **confidence**: documented

### Permanent_Worktree_Project
- **surface**: project three-dot menu > create permanent worktree
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18572` — “create a permanent worktree from the three-dot menu on a project in the sidebar. This creates a new permanent worktree as its own project.”
- **does**: Promotes a worktree into a long-lived project shared by multiple chats.
- **spark**: S=0 P=2 A=8 R=8 K=0
- **why**: P makes persistence an explicit user choice; A supports continuing coordinated work; R retains a dedicated checkout as a project.
- **rent**: once_at_install — creating the permanent worktree allocates a long-lived repository checkout.
- **composes**: [[Worktree_Chat_Isolation]], [[Worktree_Local_Handoff]], [[Project_Shared_Context]]
- **confidence**: documented

### Local_Environment_Setup_Script
- **surface**: local environment setup script selected for a worktree chat
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17239` — “Setup scripts run automatically when Codex creates a new worktree at the start of a new chat.”
- **does**: Initializes each new worktree with project-specific setup commands.
- **spark**: S=5 P=0 A=5 R=8 K=0
- **why**: S prepares a runnable project environment; A standardizes chat setup; R reaches shell commands, dependencies, and generated files.
- **rent**: every_spawn — the script runs for every newly created worktree chat.
- **composes**: [[Worktree_Chat_Isolation]], [[Worktree_Starting_Branch]]
- **confidence**: documented

### Remote_Chat_Control
- **surface**: mobile app > `Remote` > connected host chat
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17301` — Remote can start or continue host chats, send follow-ups, steer work, approve actions, and review outputs; lines 17417–17431 say the host supplies the execution environment.
- **does**: Controls a Codex chat running on a paired host from another device.
- **spark**: S=2 P=7 A=6 R=10 K=0
- **why**: S enables remote task interaction; P carries prompts, approvals, and steering from the user; A coordinates work across devices; R reaches the host's projects, files, credentials, and tools.
- **rent**: every_matching_call — remote work consumes the connected host's compute and tools when invoked.
- **composes**: [[Remote_SSH_Project]], [[Cross_Host_Chat_Handoff]], [[Subagent_Thread_Inspection]]
- **confidence**: documented

### SSH_Remote_Project_Execution
- **surface**: `Settings > Connections` > SSH host > remote project folder
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17447` — “add remote projects from an SSH host and run chats against the remote filesystem and shell.”
- **does**: Runs project chats against a configured SSH host's filesystem and shell.
- **spark**: S=3 P=2 A=4 R=10 K=0
- **why**: S enables remote development work; P requires an explicitly configured host; A relocates project execution; R reaches remote files, shell, dependencies, and compute.
- **rent**: every_matching_call — commands and file operations use the remote host for each matching call.
- **composes**: [[Remote_Chat_Control]], [[Cross_Host_Chat_Handoff]], [[Project_Shared_Context]]
- **confidence**: documented

### Cross_Host_Chat_Handoff
- **surface**: chat footer run location > destination host > `Hand off`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17484` — “Handoff moves an existing chat and its Git state between your local computer and a connected remote host”; lines 17503–17509 document worktree creation or reuse, interruption of a running response, and no cloud handoff.
- **does**: Transfers an existing chat and matching Git state between connected hosts.
- **spark**: S=1 P=5 A=9 R=10 K=0
- **why**: S preserves ongoing code work; P requires the user's destination choice; A continues one task across machines; R transfers conversation and repository state to another host.
- **rent**: none — transfer has no documented recurring charge after completion.
- **composes**: [[Remote_Chat_Control]], [[Remote_SSH_Project]], [[Worktree_Local_Handoff]]
- **confidence**: documented

### Personality_Default_Setting
- **surface**: `Settings > Personalization` > `Friendly` / `Pragmatic` / `None`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14715` — “A personality changes how ChatGPT communicates; it doesn't change what the model can do.”
- **does**: Sets the default communication style for supported models.
- **spark**: S=0 P=10 A=0 R=0 K=0
- **why**: P directly shapes interpersonal communication style.
- **rent**: every_turn — the selected default style applies to supported model responses.
- **composes**: [[Personality_Thread_Override]], [[Custom_Agent_File]]
- **confidence**: documented

### Personality_Thread_Override
- **surface**: `/personality` or per-thread/per-turn `personality`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11610` — `personality` accepts `none | friendly | pragmatic` and “can be overridden per thread/turn or via `/personality`.”
- **does**: Overrides communication style for a thread or turn.
- **spark**: S=0 P=10 A=1 R=0 K=0
- **why**: P changes the model's interaction style at the active conversation scope; A scopes that choice to current work.
- **rent**: every_turn — the override applies to each response in its selected scope.
- **composes**: [[Personality_Default_Setting]], [[Chat_Transcript_Isolation]]
- **confidence**: documented

### Plan_Mode
- **surface**: `/plan` or `Shift+Tab`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:1787` — “Plan mode lets Codex gather context, ask clarifying questions, and build a stronger plan before implementation.”
- **does**: Switches Codex into pre-implementation planning behavior.
- **spark**: S=1 P=4 A=10 R=2 K=0
- **why**: S adds structured planning; P invites clarifying user input; A gates implementation behind an explicit approach; R permits context gathering.
- **rent**: every_matching_call — planning consumes a model turn when invoked.
- **composes**: [[Persisted_Goal]]
- **confidence**: documented

### Persisted_Goal
- **surface**: `/goal`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2899` — “The goal text becomes both the first prompt and the completion criteria for the task.”
- **does**: Sets a persistent task objective with completion criteria.
- **spark**: S=1 P=2 A=10 R=1 K=0
- **why**: S adds ongoing completion tracking; P preserves the user's declared outcome; A drives multi-step continuation toward a terminal condition; R stores goal state for the chat.
- **rent**: every_turn — the goal remains active across automatic continuations and steering turns.
- **composes**: [[Goal_Lifecycle_Control]], [[Parallel_Goal_Context_Isolation]], [[Goal_Permission_Boundary]], [[Plan_Mode]]
- **confidence**: documented

### Goal_Lifecycle_Control
- **surface**: goal progress row > pause / resume / edit / clear
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2927` — the desktop goal progress row lets the user “pause or resume work, edit the goal, or clear it”; follow-up messages can adjust context or constraints.
- **does**: Applies a user-selected lifecycle operation to a running goal.
- **spark**: S=0 P=8 A=9 R=1 K=0
- **why**: P keeps long-running work interruptible and revisable; A supports steering a persistent workflow; R addresses the active goal state.
- **rent**: none — control actions have no documented recurring charge.
- **composes**: [[Persisted_Goal]], [[Goal_Permission_Boundary]]
- **confidence**: documented

### Parallel_Goal_Context_Isolation
- **surface**: run `/goal` in separate chats
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2960` — “Each chat keeps its own context, messages, results, and goal. Run chats concurrently”; worktrees give parallel coding chats separate checkouts.
- **does**: Runs concurrent goals in independently scoped chat contexts.
- **spark**: S=1 P=0 A=10 R=6 K=0
- **why**: S supports multiple long-running outcomes; A isolates concurrently progressing goals; R provides distinct chat contexts and optional worktree checkouts.
- **rent**: every_turn — every concurrent goal consumes its own model turns and context.
- **composes**: [[Persisted_Goal]], [[Chat_Transcript_Isolation]], [[Worktree_Chat_Isolation]]
- **confidence**: documented

### Goal_Permission_Boundary
- **surface**: `/goal` under the active sandbox and approval policy
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:2954` — “Starting a goal doesn't grant ChatGPT broader access. It keeps the same sandbox and approval policy and pauses when it needs a decision.”
- **does**: Preserves the current authority boundary throughout goal execution.
- **spark**: S=0 P=10 A=5 R=1 K=0
- **why**: P keeps permissions and decisions under the existing user policy; A gates continuation on required decisions; R prevents goal mode from expanding reach.
- **rent**: none — preserving the boundary has no documented recurring charge.
- **composes**: [[Persisted_Goal]], [[Goal_Lifecycle_Control]], [[Subagent_Permission_Inheritance]]
- **confidence**: documented

## Uncovered
- Session-store paths, transcript serialization, database internals, worktree snapshot internals, and deletion implementation were not inspected because they belong to I8.
- General CLI flags and command-line option inventory were not surveyed because they belong to D1; only multi-agent, chat-fork, plan, goal, and personality commands intrinsic to this scope were retained.
- Scheduled tasks and recurring autonomy were not surveyed because they belong to D6; only their exclusion from the worktree survey was noted.
- No documentary claim was exercised at runtime because this arm was explicitly documentary and prohibited runtime mutation.
- The official manual did not document a distinct user-configurable “team” object beyond projects, chats, subagents, and custom agent roles; that region was searched and empty.
