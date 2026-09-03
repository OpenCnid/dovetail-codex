# I0 Orchestrator-only Codex Desktop surfaces

These rows were emitted during reconciliation because the top-level Codex
Desktop namespace contains user-owned task and voice surfaces that delegated
probe arms could not safely exercise.

### Task_Create_Tool
- **surface**: `create_thread({ target, prompt, title?, model?, thinking? })`
- **evidence**: `tool://mcp__codex_app.create_thread` — The live Codex Desktop 26.820.9563.0 top-level schema creates a separate user-owned task only on explicit user request, supports project, projectless, or ChatGPT Work cloud targets, and chooses local versus worktree execution for saved projects.
- **does**: Creates a separate user-owned Codex task in a selected execution environment.
- **spark**: S=1 P=8 A=9 R=8 K=0
- **why**: S enables a new agent run; P reserves creation authority to the user; A isolates work into a separate task; R selects project, host, and worktree resources.
- **rent**: every_spawn — every created task consumes a new agent run and may allocate a worktree.
- **composes**: [[Task_List_Tool]], [[Worktree_Chat_Isolation]], [[Task_Fork_Tool]]
- **confidence**: documented

### Task_Handoff_Tool
- **surface**: `handoff_thread({ threadId, destinationHostId?, followUpPrompt? })`
- **evidence**: `tool://mcp__codex_app.handoff_thread` — The live Codex Desktop 26.820.9563.0 top-level schema interrupts another running task and moves its associated Git state between its checkout and Codex worktree or to a matching saved-project worktree on another host.
- **does**: Moves another Codex task and its Git state to a different execution placement.
- **spark**: S=1 P=8 A=10 R=10 K=0
- **why**: S preserves active work across placement; P requires authority over another task; A changes execution topology; R moves the task's checkout, worktree, or host reach.
- **rent**: every_matching_call — each handoff performs task interruption and filesystem or host coordination.
- **composes**: [[Handoff_Status_Long_Poll]], [[Cross_Host_Chat_Handoff]]
- **confidence**: documented

### Usage_Reset_Credit_Redemption
- **surface**: `consume_usage_reset({ idempotencyKey })`
- **evidence**: `tool://mcp__codex_app.consume_usage_reset` — The live Codex Desktop 26.820.9563.0 top-level schema redeems one existing usage-reset credit only after explicit user authorization and requires the same idempotency key for an uncertain retry.
- **does**: Redeems an authorized Codex usage-reset credit idempotently.
- **spark**: S=0 P=10 A=5 R=7 K=0
- **why**: P reserves spend/reset authority to the user; A makes retries idempotent; R restores an account usage resource when a credit exists.
- **rent**: every_matching_call — each logical redemption consumes at most one available credit.
- **composes**: [[Usage_Limit_Status]], [[Task_Create_Tool]]
- **confidence**: documented

### Foreground_Codex_Screen_Context
- **surface**: `capture_screen_context()`
- **evidence**: `tool://mcp__codex_app.capture_screen_context` — The live Codex Desktop 26.820.9563.0 top-level schema is voice-chat-only and reads the foreground Codex page plus right-sidebar state, explicitly excluding other applications.
- **does**: Reads foreground Codex application context during an active voice chat.
- **spark**: S=2 P=5 A=3 R=7 K=5
- **why**: S enables screen-grounded assistance; P limits capture to an active user conversation; A gates use by voice-chat state; R reaches Codex UI state; K supplies the visible page context.
- **rent**: every_matching_call — each capture reads the current foreground Codex state.
- **composes**: [[Voice_Chat_Termination]], [[Codex_Task_Navigation]]
- **confidence**: documented

### Voice_Chat_Termination
- **surface**: `end_realtime_voice_call()`
- **evidence**: `tool://mcp__codex_app.end_realtime_voice_call` — The live Codex Desktop 26.820.9563.0 top-level schema ends the current voice chat only when the user explicitly asks.
- **does**: Ends the active Codex voice conversation on explicit user request.
- **spark**: S=0 P=10 A=4 R=1 K=0
- **why**: P gives the user exclusive termination authority; A closes the realtime interaction lifecycle; R releases the active voice session.
- **rent**: none — termination ends rather than adds a recurring component.
- **composes**: [[Foreground_Codex_Screen_Context]], [[Final_Response_Channel]]
- **confidence**: documented

## Uncovered
- These consequential top-level surfaces were not exercised because doing so would create or move a user-owned task, redeem an account credit, capture live voice UI state, or terminate a voice call.
- Plugin-install suggestion, plugin uninstall, sharing, navigation, and panel-delivery schemas were already represented by I5 or I10 and were not duplicated here.
