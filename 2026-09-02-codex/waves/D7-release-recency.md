### Desktop_Unified_Pinned_Threads
- **surface**: `sidebar pinned chats`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-08-20-app` — Desktop release 2026-08-20; target pin `26.820.9563.0`, surveyed 2026-09-02: “Unified pinned threads: Keep your pinned chats in sync between desktop and iOS.”
- **does**: Synchronizes pinned chats between desktop and iOS.
- **spark**: S=0 P=0 A=3 R=4 K=0
- **why**: A preserves an attention-ordering workflow across devices; R exposes the same pinned-thread state on two clients
- **rent**: every_turn — the service maintains shared pinned state for the user after the release
- **composes**: [[Desktop_Activity_View]], [[Remote_Connections]]
- **confidence**: documented

### Desktop_Setup_Import
- **surface**: `Settings > Import`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-08-11-app` — Desktop/CLI release 2026-08-11; target pin `26.820.9563.0`, surveyed 2026-09-02: “Import instructions, settings, skills, plugins, projects, and recent work from Claude Code, Claude Cowork, or Cursor into the ChatGPT desktop app.”
- **does**: Imports a supported agent setup into the desktop app.
- **spark**: S=2 P=0 A=6 R=5 K=3
- **why**: S transfers installed task abilities; A preserves an established working method; R brings configured extensions and projects within reach; K transfers instructions and recent-work context
- **rent**: once_at_install — the user pays a one-time import and review cost
- **composes**: [[CLI_Setup_Import]], [[Skill_System]], [[Plugin_System]], [[Project_System]]
- **confidence**: documented

### CLI_Setup_Import
- **surface**: `/import`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-08-11-app` — Desktop/CLI release 2026-08-11; target pin `codex-cli 0.150.0-alpha.8`, surveyed 2026-09-02: “In Codex CLI, use `/import` to bring supported setup and recent chats from Claude Code or Cursor into your local session.”
- **does**: Imports supported external-agent setup into a CLI session.
- **spark**: S=2 P=0 A=6 R=4 K=3
- **why**: S transfers installed task abilities; A preserves an established working method; R brings configured extensions within reach; K transfers recent-chat context
- **rent**: once_at_install — the user pays a one-time import and review cost
- **composes**: [[Desktop_Setup_Import]], [[Skill_System]], [[Plugin_System]]
- **confidence**: documented

### Multi_Repository_Combined_Review
- **surface**: `Review`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-07-30-app` — Desktop release 2026-07-30; target pin `26.820.9563.0`, surveyed 2026-09-02: “the desktop app shows every repository and the lines changed in each one. Select Review to inspect their diffs together.”
- **does**: Reviews diffs from every repository in a multi-folder project together.
- **spark**: S=3 P=0 A=6 R=5 K=0
- **why**: S enables cross-repository review; A consolidates a formerly fragmented inspection workflow; R exposes multiple repositories in one review surface
- **rent**: none — the user invokes the view without a persistent harness charge
- **composes**: [[Multi_Folder_Local_Project]], [[Code_Review]]
- **confidence**: documented

### Desktop_Activity_View
- **surface**: `sidebar bell > Activity`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-07-30-app` — Desktop release 2026-07-30; target pin `26.820.9563.0`, surveyed 2026-09-02: “The desktop app's new Activity view brings together chats you recently engaged with and work that needs your attention.”
- **does**: Aggregates recent chats with work requiring attention.
- **spark**: S=0 P=0 A=5 R=4 K=0
- **why**: A supplies a triage method for parallel work; R exposes attention state across chats
- **rent**: none — opening the view adds no continuing agent or user charge
- **composes**: [[Desktop_Unified_Pinned_Threads]], [[Parallel_Chat_Management]]
- **confidence**: documented

### Multi_Folder_Local_Project
- **surface**: `Edit project > add folders`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-07-23-app` — Desktop release 2026-07-23; target pin `26.820.9563.0`, surveyed 2026-09-02: “Local projects in the ChatGPT desktop app can now include multiple related folders.”
- **does**: Adds multiple related folders to one local project.
- **spark**: S=1 P=0 A=5 R=7 K=0
- **why**: S permits cross-folder project work; A centers related repositories in one project; R expands reachable filesystem scope
- **rent**: every_turn — configured folders remain project context available to later turns
- **composes**: [[Multi_Repository_Combined_Review]], [[Project_Primary_Folder]]
- **confidence**: documented

### Codex_Desktop_View_Migration
- **surface**: `ChatGPT desktop app > Codex`
- **evidence**: `https://learn.chatgpt.com/docs/changelog#codex-2026-07-09-app` — Desktop release 2026-07-09; target pin `26.820.9563.0`, surveyed 2026-09-02: “the Codex app merged into the ChatGPT desktop app for macOS and Windows. Codex keeps its dedicated coding experience.”
- **does**: Moves the dedicated Codex experience into the ChatGPT desktop app.
- **spark**: S=0 P=0 A=2 R=6 K=0
- **why**: A changes how users enter coding work; R relocates the Codex workspace into a shared desktop shell
- **rent**: none — the product-surface migration adds no recurring charge by itself
- **composes**: [[Desktop_Activity_View]], [[ChatGPT_Desktop_App]]
- **confidence**: documented

### CLI_Task_Management_Tools
- **surface**: `agent tools: read/create/message tasks`
- **evidence**: `https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.150.0-alpha.8` — Codex CLI `0.150.0-alpha.8`, released 2026-08-24; compared from `0.149.0`: 2026-08-24 commit “Add TUI tools for managing Codex tasks (#40308).”
- **does**: Lets an agent manage Codex tasks from a terminal session.
- **spark**: S=2 P=1 A=9 R=6 K=0
- **why**: S enables task-level control; P enables cross-task messaging; A enables explicit orchestration; R exposes other task records and controls
- **rent**: every_matching_call — each task-management call spends agent execution and context
- **composes**: [[CLI_Task_Mentions]], [[Codex_Agents_Dashboard]], [[Codex_Queue_Command]]
- **confidence**: documented

### CLI_Task_Mentions
- **surface**: `@ task mention in TUI composer`
- **evidence**: `https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.150.0-alpha.8` — Codex CLI `0.150.0-alpha.8`, released 2026-08-24; compared from `0.149.0`: 2026-08-24 commit “Add task mentions to the TUI composer (#40315).”
- **does**: References another Codex task from the terminal composer.
- **spark**: S=0 P=1 A=7 R=5 K=2
- **why**: P addresses work across task boundaries; A links parallel task workflows; R reaches another task; K brings named task context into the request
- **rent**: every_matching_call — each mention consumes prompt context for the agent
- **composes**: [[CLI_Task_Management_Tools]], [[Codex_Agents_Dashboard]]
- **confidence**: documented

### CLI_Copy_Target_Picker
- **surface**: `/copy`
- **evidence**: `https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.150.0-alpha.8` — Codex CLI `0.150.0-alpha.8`, released 2026-08-24; compared from `0.149.0`: 2026-08-21 commit “Add a response target picker to `/copy` (#39997).”
- **does**: Selects a full response, code block, or blockquote for copying.
- **spark**: S=2 P=0 A=2 R=3 K=0
- **why**: S enables granular response extraction; A shortens the selection workflow; R exposes structured response parts
- **rent**: none — copying a response fragment creates no continuing harness charge
- **composes**: [[TUI_Transcript]], [[Clipboard]]
- **confidence**: documented

### TUI_Permission_Mode_Cycling
- **surface**: `TUI permission-mode cycle keybindings`
- **evidence**: `https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.150.0-alpha.8` — Codex CLI `0.150.0-alpha.8`, released 2026-08-24; compared from `0.149.0`: 2026-08-21 commit “Add keybindings for cycling TUI permission modes (#39873).”
- **does**: Cycles terminal permission modes through keyboard shortcuts.
- **spark**: S=0 P=8 A=3 R=0 K=0
- **why**: P changes who authorizes tool reach; A makes authority-mode switching part of the terminal workflow
- **rent**: none — changing the mode has no separate recurring harness charge
- **composes**: [[Permission_Profile]], [[Tool_Approval]]
- **confidence**: documented

### Plan_Mode_Composer_Nudge_Removal
- **surface**: `Plan mode composer nudge`
- **evidence**: `https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.150.0-alpha.8` — Codex CLI `0.150.0-alpha.8`, released 2026-08-24; compared from `0.149.0`: 2026-08-23 commit “Remove the Plan mode composer nudge (#40200).”
- **does**: Removes the terminal composer nudge shown in Plan mode.
- **spark**: S=0 P=3 A=3 R=0 K=0
- **why**: P removes a user-facing steering prompt; A changes Plan-mode interaction guidance
- **rent**: none — the removed nudge no longer consumes interface attention
- **composes**: [[Plan_Mode]], [[TUI_Composer]]
- **confidence**: documented

### Codex_Agents_Dashboard
- **surface**: `codex agents`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`: “Added an interactive `codex agents` dashboard for searching, starting, opening, renaming, and stopping tasks.”
- **does**: Manages multiple tasks through an interactive terminal dashboard.
- **spark**: S=1 P=0 A=9 R=6 K=0
- **why**: S enables task administration; A centralizes parallel-task orchestration; R exposes task records and lifecycle controls
- **rent**: every_matching_call — dashboard operations spend local runtime only when invoked
- **composes**: [[CLI_Task_Management_Tools]], [[CLI_Task_Mentions]], [[Codex_Queue_Command]]
- **confidence**: documented

### TUI_Working_Directory_Commands
- **surface**: `/cd`, `/pwd`, `/cwd`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`: “Added `/cd`, `/pwd`, and `/cwd` commands for managing the working directory in TUI sessions.”
- **does**: Manages the working directory within a TUI session.
- **spark**: S=1 P=0 A=4 R=6 K=0
- **why**: S enables in-session directory control; A avoids restarting a session to relocate work; R changes reachable working-directory context
- **rent**: none — directory commands incur no persistent charge
- **composes**: [[Shell_Execution]], [[Project_Context]]
- **confidence**: documented

### Codex_Queue_Command
- **surface**: `codex queue`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`: “Added `codex queue` for sending messages to existing local or remote sessions.”
- **does**: Sends a message to an existing Codex session.
- **spark**: S=0 P=2 A=8 R=5 K=0
- **why**: P communicates across session boundaries; A coordinates ongoing work asynchronously; R reaches local or remote sessions
- **rent**: every_matching_call — each queued message consumes recipient-session context and execution
- **composes**: [[Codex_Agents_Dashboard]], [[CLI_Task_Management_Tools]], [[Remote_Session]]
- **confidence**: documented

### Codex_Doctor_Expanded_Diagnostics
- **surface**: `codex doctor`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`: “`codex doctor` now diagnoses endpoint protection, network/proxy failures, desktop app state, and update connectivity.”
- **does**: Diagnoses local Codex runtime health.
- **spark**: S=3 P=0 A=3 R=6 K=2
- **why**: S adds targeted troubleshooting; A standardizes the diagnostic workflow; R inspects host and app subsystems; K supplies interpreted failure state
- **rent**: every_matching_call — diagnostics consume local runtime only when invoked
- **composes**: [[Desktop_App_State]], [[Network_Proxy]], [[Windows_Sandbox]]
- **confidence**: documented

### Thread_Permission_Profile_Restoration
- **surface**: `resume or fork thread`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`: “Resumed and forked threads now restore their active permission profile instead of silently falling back to current defaults.”
- **does**: Restores a thread’s active permission profile after resume or fork.
- **spark**: S=0 P=9 A=4 R=0 K=0
- **why**: P preserves the user-authorized authority boundary; A makes resumed and forked execution consistent with prior thread state
- **rent**: every_turn — the active profile continues to constrain every later turn
- **composes**: [[Permission_Profile]], [[Thread_Resume]], [[Thread_Fork]]
- **confidence**: documented

### Windows_Terminal_Inline_History_Scrollback
- **surface**: `Windows Terminal scrollback`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`: “Inline TUI history now remains available in Windows Terminal scrollback.”
- **does**: Preserves inline TUI history in Windows Terminal scrollback.
- **spark**: S=0 P=0 A=2 R=5 K=0
- **why**: A preserves a terminal inspection workflow; R keeps prior terminal output reachable
- **rent**: every_turn — retained output occupies terminal scrollback during the session
- **composes**: [[TUI_Transcript]], [[Windows_Terminal]]
- **confidence**: documented

### Untrusted_Approval_Policy_Retirement
- **surface**: `untrusted approval policy`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`; changelog item: “Retire the untrusted approval policy (#39630).”
- **does**: Removes the legacy untrusted approval policy.
- **spark**: S=0 P=9 A=2 R=0 K=0
- **why**: P removes an authority regime; A changes the available approval workflow
- **rent**: none — the retired policy imposes no continuing context or execution charge
- **composes**: [[Approval_Policy]], [[Permission_Profile]]
- **confidence**: documented

### Deprecated_MCP_Server_Warning
- **surface**: `deprecated MCP server launch`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`; changelog item: “Warn when launching the deprecated MCP server (#39657).”
- **does**: Warns when a user launches the deprecated MCP server.
- **spark**: S=0 P=4 A=2 R=2 K=0
- **why**: P interrupts use of a deprecated surface; A directs migration away from the legacy path; R identifies a still-reachable but discouraged server
- **rent**: every_matching_call — the warning appears only when the deprecated server is launched
- **composes**: [[MCP_Server]], [[Deprecation_Warning]]
- **confidence**: documented

### PowerShell_Fail_Closed_Command_Lowering
- **surface**: `PowerShell command classification`
- **evidence**: `https://github.com/openai/codex/releases/tag/rust-v0.149.0` — Codex CLI `0.149.0`, released 2026-08-20 and preceding target `0.150.0-alpha.8`; changelog item: “Add a fail-closed Tree-sitter PowerShell lowerer (#39213).”
- **does**: Fails closed when PowerShell command classification cannot lower safely.
- **spark**: S=0 P=8 A=2 R=0 K=0
- **why**: P denies ambiguous authority rather than silently permitting it; A changes the Windows command-classification method
- **rent**: every_matching_call — PowerShell commands pay classification cost before execution
- **composes**: [[PowerShell_Command_Execution]], [[Tool_Approval]], [[Windows_Sandbox]]
- **confidence**: documented

### Elevated_Windows_Sandbox_Setup_Activation_Fix
- **surface**: `windows.sandbox = "elevated"`
- **evidence**: `https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.150.0-alpha.8` — Codex CLI `0.150.0-alpha.8`, released 2026-08-24; compared from `0.149.0`: 2026-08-21 commit “Fix elevated Windows sandbox setup activation (#39971).”
- **does**: Activates elevated Windows sandbox setup correctly.
- **spark**: S=0 P=7 A=2 R=4 K=0
- **why**: P restores the selected execution authority boundary; A repairs the Windows setup path; R restores access to the elevated sandbox resource
- **rent**: every_matching_call — sandbox startup and command isolation recur for matching executions
- **composes**: [[Windows_Sandbox]], [[PowerShell_Fail_Closed_Command_Lowering]]
- **confidence**: documented

## Uncovered
- The public release page does not map app build `26.820.9563.0` to a release artifact; Desktop rows therefore carry the pinned build as survey context and use only independently dated official release entries.
- The `0.150.0-alpha.8` prerelease page contains only its version label; alpha-specific rows use the official `0.149.0...0.150.0-alpha.8` comparison and omit commits whose titles do not establish user-visible semantics.
- Codex CLI `0.150.0` stable shipped on 2026-08-26 after the pinned prerelease and was not projected backward into this wave.
- macOS-only app changes, mobile-only releases, cloud-only changes, internal telemetry, test-only commits, and undated static capabilities were searched but excluded as outside the pinned Windows Desktop/CLI change scope.
