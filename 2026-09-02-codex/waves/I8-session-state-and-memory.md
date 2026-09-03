# I8 Session State and Memory

### Local_Rollout_JSONL_Store
- **surface**: `$CODEX_HOME/sessions/YYYY/MM/DD/rollout-<timestamp>-<session-id>.jsonl`
- **evidence**: `C:\Users\Darian\.codex\sessions` — 402 `.jsonl` files were enumerated; current paths use year/month/day directories and `rollout-...jsonl` names under Codex Desktop 26.820.9563.0 / codex-cli 0.150.0-alpha.8.
- **does**: Persists a session as a local JSONL rollout.
- **spark**: S=0 P=0 A=2 R=9 K=5
- **why**: A=2 preserves execution continuity; R=9 exposes durable local session state; K=5 retains prior interaction records.
- **rent**: every_turn — the runtime pays local serialization and storage cost as the session advances.
- **composes**: [[Rollout_Record_Envelope]], [[Session_Metadata_Record]], [[Turn_Context_Record]], [[Response_Item_Record]]
- **confidence**: observed

### Rollout_Record_Envelope
- **surface**: `{"timestamp", "ordinal", "type", "payload"}`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-17-36-01a06357-3a5e-7ba2-ba01-bce7260e407d.jsonl` — all 54 sampled records exposed `timestamp`, `ordinal`, `type`, and `payload` under Codex Desktop 26.820.9563.0.
- **does**: Orders typed session payloads in a common timestamped envelope.
- **spark**: S=0 P=0 A=3 R=7 K=3
- **why**: A=3 supplies replay order; R=7 makes heterogeneous state uniformly addressable; K=3 preserves record provenance.
- **rent**: every_matching_call — each persisted rollout record carries envelope metadata.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Thread_History_Projection_Cursor]]
- **confidence**: observed

### Session_Metadata_Record
- **surface**: `type: "session_meta"`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-17-36-01a06357-3a5e-7ba2-ba01-bce7260e407d.jsonl` — the sampled `session_meta` schema includes `id`, `session_id`, `cwd`, `cli_version`, `context_window`, `git`, `history_mode`, `source`, and parent/thread-source fields under codex-cli 0.150.0-alpha.8.
- **does**: Anchors a rollout to its session identity and creation environment.
- **spark**: S=0 P=0 A=2 R=7 K=5
- **why**: A=2 fixes execution lineage; R=7 exposes session metadata; K=5 records environment provenance.
- **rent**: every_spawn — one metadata record is charged to each newly persisted session.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Interactive_Session_Resume]], [[Interactive_Session_Fork]]
- **confidence**: observed

### Turn_Context_Record
- **surface**: `type: "turn_context"`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-17-36-01a06357-3a5e-7ba2-ba01-bce7260e407d.jsonl` — the sampled payload schema includes `turn_id`, `model`, `effort`, `cwd`, permission/sandbox fields, `comp_hash`, `summary`, date/timezone, and workspace roots under Codex Desktop 26.820.9563.0.
- **does**: Snapshots the execution context associated with a turn.
- **spark**: S=0 P=2 A=4 R=7 K=4
- **why**: P=2 retains authority context; A=4 preserves per-turn operating method; R=7 persists runtime settings; K=4 records environmental context.
- **rent**: every_turn — each turn pays for a context snapshot.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Thread_Turn_Projection]], [[Compacted_Rollout_Record]]
- **confidence**: observed

### Response_Item_Record
- **surface**: `type: "response_item"`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-17-36-01a06357-3a5e-7ba2-ba01-bce7260e407d.jsonl` — schema-only inspection found payload variants `message`, `reasoning`, `agent_message`, `custom_tool_call`, and `custom_tool_call_output`; no content values were emitted.
- **does**: Persists typed model and tool interaction items in the rollout.
- **spark**: S=0 P=0 A=3 R=8 K=6
- **why**: A=3 preserves execution trace structure; R=8 retains tool/message artifacts; K=6 makes prior interaction items available to history.
- **rent**: every_matching_call — each persisted response or tool item incurs serialization and storage.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Thread_Item_Projection]]
- **confidence**: observed

### World_State_Record
- **surface**: `type: "world_state"`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\02\rollout-2026-09-02T13-17-36-01a06357-3a5e-7ba2-ba01-bce7260e407d.jsonl` — the sampled record exposed only the schema keys `full` and `state`; payload values were not inspected.
- **does**: Stores a world-state payload in the session rollout.
- **spark**: S=0 P=0 A=2 R=7 K=4
- **why**: A=2 supports stateful continuation; R=7 exposes a durable state asset; K=4 retains environment state.
- **rent**: every_matching_call — storage is charged when a world-state snapshot is recorded.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Interactive_Session_Resume]]
- **confidence**: observed

### Archived_Rollout_Store
- **surface**: `$CODEX_HOME/archived_sessions/rollout-*.jsonl`
- **evidence**: `C:\Users\Darian\.codex\archived_sessions` — 45 archived `.jsonl` files were enumerated; a schema-only sample retained the same rollout envelope and record families as the active store under Codex Desktop 26.820.9563.0.
- **does**: Persists archived session rollouts separately from active dated rollouts.
- **spark**: S=0 P=0 A=3 R=8 K=5
- **why**: A=3 separates inactive lifecycle state; R=8 retains recoverable session assets; K=5 preserves archived history.
- **rent**: every_matching_call — an archived session continues to consume local storage.
- **composes**: [[Session_Archive_Command]], [[Session_Unarchive_Command]], [[Archived_Task_List_Tool]]
- **confidence**: observed

### Session_Name_Index
- **surface**: `$CODEX_HOME/session_index.jsonl`
- **evidence**: `C:\Users\Darian\.codex\session_index.jsonl` — 119 schema-only records shared keys `id`, `thread_name`, and `updated_at` under codex-cli 0.150.0-alpha.8.
- **does**: Maps persisted session identifiers to names and update timestamps.
- **spark**: S=0 P=0 A=1 R=7 K=4
- **why**: A=1 supports name-based selection; R=7 exposes a lookup index; K=4 retains task identity metadata.
- **rent**: every_matching_call — session naming or updates incur index maintenance.
- **composes**: [[Interactive_Session_Resume]], [[Session_Archive_Command]], [[Session_Delete_Command]]
- **confidence**: observed

### Thread_Writer_Lock
- **surface**: `$CODEX_HOME/thread-writer-locks/<thread-id>.lock`
- **evidence**: `C:\Users\Darian\.codex\thread-writer-locks` — 26 zero-byte `.lock` files were enumerated, including UUID-named locks plus `.coordination.lock`, under Codex Desktop 26.820.9563.0.
- **does**: Coordinates exclusive writers for persisted thread state.
- **spark**: S=0 P=0 A=6 R=4 K=0
- **why**: A=6 serializes concurrent persistence work; R=4 supplies local coordination tokens.
- **rent**: every_matching_call — active writers pay lock acquisition and coordination cost.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Thread_History_Projection_Cursor]]
- **confidence**: observed

### Compacted_Rollout_Record
- **surface**: `type: "compacted"`
- **evidence**: `C:\Users\Darian\.codex\sessions\2026\09\01\rollout-2026-09-01T10-10-44-01a05d85-cb84-7ac0-aa11-ecc802baebb5.jsonl` — three sampled compacted records expose `message`, `replacement_history`, `window_number`, `first_window_id`, `previous_window_id`, and `window_id`; marker search found 204 active and 24 archived rollout files.
- **does**: Replaces prior context with a window-linked compacted history payload.
- **spark**: S=0 P=0 A=8 R=5 K=7
- **why**: A=8 changes the continuation method at context boundaries; R=5 retains replacement artifacts; K=7 condenses prior interaction knowledge.
- **rent**: every_matching_call — compaction consumes summarization work and stores a replacement history.
- **composes**: [[Turn_Context_Record]], [[Interactive_Session_Resume]], [[Thread_Item_Projection]]
- **confidence**: observed

### Thread_Catalog_Table
- **surface**: `$CODEX_HOME/state_5.sqlite :: threads`
- **evidence**: `C:\Users\Darian\.codex\state_5.sqlite` — read-only SQLite schema exposes identity, rollout path, timestamps, source, cwd, title/name, model, token count, archived/pinned flags, Git fields, history/memory modes, section, project, and preview metadata under Codex Desktop 26.820.9563.0.
- **does**: Catalogs persisted threads and their lifecycle metadata.
- **spark**: S=0 P=0 A=3 R=9 K=6
- **why**: A=3 records lifecycle placement; R=9 centralizes thread reachability; K=6 retains execution and project provenance.
- **rent**: every_matching_call — thread creation and metadata changes incur catalog writes.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Project_Catalog_Tables]], [[Task_List_Tool]]
- **confidence**: observed

### Project_Catalog_Tables
- **surface**: `$CODEX_HOME/state_5.sqlite :: projects, project_roots`
- **evidence**: `C:\Users\Darian\.codex\state_5.sqlite` — `projects` stores id/name/metadata/order/timestamps; ordered `project_roots` rows reference projects with `ON DELETE CASCADE` under Codex Desktop 26.820.9563.0.
- **does**: Stores ordered project metadata with associated workspace roots.
- **spark**: S=0 P=0 A=3 R=8 K=5
- **why**: A=3 groups work by project; R=8 maps projects to local roots; K=5 preserves project identity metadata.
- **rent**: every_matching_call — project changes incur catalog maintenance.
- **composes**: [[Thread_Catalog_Table]], [[Desktop_Project_Assignment_State]]
- **confidence**: observed

### Thread_History_Projection_Cursor
- **surface**: `$CODEX_HOME/thread_history_1.sqlite :: thread_history_projection_state`
- **evidence**: `C:\Users\Darian\.codex\thread_history_1.sqlite` — read-only schema stores `thread_id`, `next_rollout_byte_offset`, and `next_rollout_ordinal` under codex-cli 0.150.0-alpha.8.
- **does**: Checkpoints how far each rollout has been projected into paginated history.
- **spark**: S=0 P=0 A=7 R=6 K=2
- **why**: A=7 enables incremental history projection; R=6 exposes durable projection cursors; K=2 records ingestion position.
- **rent**: every_matching_call — projection progress incurs cursor updates.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Thread_Turn_Projection]], [[Thread_Item_Projection]]
- **confidence**: observed

### Thread_Turn_Projection
- **surface**: `$CODEX_HOME/thread_history_1.sqlite :: thread_turns`
- **evidence**: `C:\Users\Darian\.codex\thread_history_1.sqlite` — read-only schema stores thread/turn ids, rollout ordinal, status/error, timing, first/final item ids, and rollout byte/ordinal boundaries under codex-cli 0.150.0-alpha.8.
- **does**: Projects rollout records into addressable turn summaries.
- **spark**: S=0 P=0 A=5 R=8 K=5
- **why**: A=5 structures history by turn; R=8 exposes paginated turn records; K=5 retains outcome and timing metadata.
- **rent**: every_turn — each projected turn incurs indexed storage.
- **composes**: [[Thread_History_Projection_Cursor]], [[Task_History_Read_Tool]]
- **confidence**: observed

### Thread_Item_Projection
- **surface**: `$CODEX_HOME/thread_history_1.sqlite :: thread_items`
- **evidence**: `C:\Users\Darian\.codex\thread_history_1.sqlite` — read-only schema stores thread/turn/item ids, rollout ordinal, timestamps, `item_json`, `item_type`, and update ordinal under codex-cli 0.150.0-alpha.8.
- **does**: Projects rollout items into typed addressable history entries.
- **spark**: S=0 P=0 A=5 R=8 K=6
- **why**: A=5 structures event replay; R=8 exposes item-level history; K=6 retains serialized interaction artifacts.
- **rent**: every_matching_call — each projected item incurs indexed storage.
- **composes**: [[Thread_History_Projection_Cursor]], [[Task_History_Read_Tool]], [[Compacted_Rollout_Record]]
- **confidence**: observed

### Stage1_Thread_Memory
- **surface**: `$CODEX_HOME/memories_1.sqlite :: stage1_outputs`
- **evidence**: `C:\Users\Darian\.codex\memories_1.sqlite` — read-only schema exposes per-thread `raw_memory`, `rollout_summary`, slug, source/generated timestamps, usage counters, and phase-two selection fields under Codex Desktop 26.820.9563.0.
- **does**: Stores generated per-thread memory candidates and usage metadata.
- **spark**: S=0 P=0 A=4 R=7 K=9
- **why**: A=4 stages memory processing; R=7 exposes a durable memory store; K=9 carries synthesized thread knowledge across later use.
- **rent**: every_matching_call — memory extraction and persisted candidates consume compute and storage.
- **composes**: [[Memory_Extraction_Job_State]], [[Local_Rollout_JSONL_Store]]
- **confidence**: observed

### Memory_Extraction_Job_State
- **surface**: `$CODEX_HOME/memories_1.sqlite :: jobs`
- **evidence**: `C:\Users\Darian\.codex\memories_1.sqlite` — read-only schema exposes job kind/key, status, worker/ownership, start/finish/lease/retry fields, error, and input/success watermarks under Codex Desktop 26.820.9563.0.
- **does**: Checkpoints retryable memory-processing jobs with leases and watermarks.
- **spark**: S=0 P=0 A=8 R=5 K=3
- **why**: A=8 coordinates resumable background processing; R=5 persists job-control state; K=3 records processing watermarks.
- **rent**: every_matching_call — memory jobs pay lease, retry, and checkpoint overhead.
- **composes**: [[Stage1_Thread_Memory]]
- **confidence**: observed

### Desktop_Local_Thread_Catalog
- **surface**: `$CODEX_HOME/sqlite/codex-dev.db :: local_thread_catalog`
- **evidence**: `C:\Users\Darian\.codex\sqlite\codex-dev.db` — user_version 32 schema stores host/thread ids, display metadata, cwd/source/model/Git fields, observation sequence, missing-candidate flag, project id, and conversation origin under Codex Desktop 26.820.9563.0.
- **does**: Reconciles task metadata across locally known task hosts.
- **spark**: S=0 P=0 A=5 R=9 K=5
- **why**: A=5 reconciles observations across hosts; R=9 provides a cross-host task catalog; K=5 retains source and project metadata.
- **rent**: every_matching_call — catalog observations and reconciliation incur local writes.
- **composes**: [[Task_List_Tool]], [[Archived_Task_List_Tool]], [[Desktop_Thread_Timeline_Ledger]]
- **confidence**: observed

### Desktop_Thread_Timeline_Ledger
- **surface**: `$CODEX_HOME/sqlite/codex-dev.db :: thread_timeline_ledger`
- **evidence**: `C:\Users\Darian\.codex\sqlite\codex-dev.db` — read-only user_version 32 schema keys records by host/thread/sequence, enforces unique record ids, and stores `payload_json` under Codex Desktop 26.820.9563.0.
- **does**: Stores an ordered deduplicated timeline ledger for each host task.
- **spark**: S=0 P=0 A=6 R=8 K=6
- **why**: A=6 orders and deduplicates timeline ingestion; R=8 exposes durable task events; K=6 retains event payload history.
- **rent**: every_matching_call — each timeline record incurs ledger storage and uniqueness checks.
- **composes**: [[Desktop_Local_Thread_Catalog]], [[Task_History_Read_Tool]]
- **confidence**: observed

### Desktop_Project_Assignment_State
- **surface**: `$CODEX_HOME/.codex-global-state.json`
- **evidence**: `C:\Users\Darian\.codex\.codex-global-state.json` — schema-only inspection found top-level `local-projects`, `selected-project`, `project-order`, `thread-project-assignments`, `thread-projectless-output-directories`, `thread-workspace-root-hints`, and `projectless-thread-ids` under Codex Desktop 26.820.9563.0.
- **does**: Persists Desktop task-to-project and workspace-placement metadata.
- **spark**: S=0 P=0 A=4 R=8 K=5
- **why**: A=4 organizes task placement; R=8 maps tasks to workspaces; K=5 preserves project association metadata.
- **rent**: every_matching_call — project or task-placement changes incur global-state writes.
- **composes**: [[Project_Catalog_Tables]], [[Desktop_Local_Thread_Catalog]]
- **confidence**: observed

### Interactive_Session_Resume
- **surface**: `codex resume [--last|--all|--include-non-interactive] [SESSION_ID] [PROMPT]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex resume --help` states that a UUID or session name resumes a prior interactive session; picker, newest-session, cwd-wide, and non-interactive inclusion modes are documented in codex-cli 0.150.0-alpha.8.
- **does**: Continues a persisted interactive session selected by picker, identifier, name, or recency.
- **spark**: S=1 P=0 A=7 R=8 K=6
- **why**: S=1 enables continuation; A=7 resumes an existing execution trajectory; R=8 reaches saved session state; K=6 restores prior interaction context.
- **rent**: none — selection itself has no recurring charge beyond the resumed session's normal turns.
- **composes**: [[Session_Name_Index]], [[Local_Rollout_JSONL_Store]], [[Compacted_Rollout_Record]]
- **confidence**: documented

### Noninteractive_Session_Resume
- **surface**: `codex exec resume [--last|--all] [--ephemeral] [SESSION_ID] [PROMPT]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec resume --help` documents resume by UUID/thread name or newest session, optional prompt/stdin, event JSONL, and ephemeral execution in codex-cli 0.150.0-alpha.8.
- **does**: Continues a persisted session through the noninteractive execution interface.
- **spark**: S=2 P=0 A=7 R=8 K=6
- **why**: S=2 enables scripted continuation; A=7 preserves an execution trajectory; R=8 reaches stored state; K=6 restores prior context.
- **rent**: none — invocation adds no persistent charge beyond the resumed run unless persistence remains enabled.
- **composes**: [[Interactive_Session_Resume]], [[Ephemeral_Execution_Mode]]
- **confidence**: documented

### Interactive_Session_Fork
- **surface**: `codex fork [--last|--all] [SESSION_ID] [PROMPT]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex fork --help` documents forking a prior conversation/session by UUID, picker, or newest session in codex-cli 0.150.0-alpha.8.
- **does**: Starts a new interactive session from persisted history.
- **spark**: S=1 P=0 A=8 R=8 K=6
- **why**: S=1 enables history-derived branching; A=8 creates an alternate execution trajectory; R=8 reaches saved state; K=6 copies prior context into the branch.
- **rent**: every_spawn — each fork creates another session lineage and store.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Session_Metadata_Record]], [[Task_Fork_Tool]]
- **confidence**: documented

### Session_Archive_Command
- **surface**: `codex archive <SESSION>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex archive --help` documents archiving a saved session by UUID or session name in codex-cli 0.150.0-alpha.8.
- **does**: Moves a saved session into archived lifecycle state.
- **spark**: S=0 P=0 A=5 R=7 K=2
- **why**: A=5 changes session lifecycle placement; R=7 manages retained session reachability; K=2 preserves identity during archival.
- **rent**: none — archival is a one-shot state transition.
- **composes**: [[Archived_Rollout_Store]], [[Session_Unarchive_Command]], [[Task_Archive_Toggle_Tool]]
- **confidence**: documented

### Session_Unarchive_Command
- **surface**: `codex unarchive <SESSION>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex unarchive --help` documents restoring a saved session by UUID or session name in codex-cli 0.150.0-alpha.8.
- **does**: Returns a saved session from archived lifecycle state.
- **spark**: S=0 P=0 A=5 R=7 K=2
- **why**: A=5 reverses lifecycle placement; R=7 restores active reachability; K=2 preserves archived identity.
- **rent**: none — unarchival is a one-shot state transition.
- **composes**: [[Archived_Rollout_Store]], [[Session_Archive_Command]], [[Task_Archive_Toggle_Tool]]
- **confidence**: documented

### Session_Delete_Command
- **surface**: `codex delete [--force] <SESSION>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex delete --help` says it permanently deletes by UUID or session name; `--force` skips prompting and requires a UUID in codex-cli 0.150.0-alpha.8.
- **does**: Permanently deletes a selected saved session.
- **spark**: S=0 P=2 A=5 R=8 K=1
- **why**: P=2 the prompt/force split governs user confirmation; A=5 terminates a session lifecycle; R=8 removes a durable resource; K=1 resolves its identity.
- **rent**: none — deletion is a one-shot destructive operation.
- **composes**: [[Session_Name_Index]], [[Local_Rollout_JSONL_Store]], [[Archived_Rollout_Store]]
- **confidence**: documented

### Ephemeral_Execution_Mode
- **surface**: `codex exec resume --ephemeral`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec resume --help` defines `--ephemeral` as running without persisting session files to disk in codex-cli 0.150.0-alpha.8.
- **does**: Suppresses on-disk session-file persistence for a noninteractive resumed run.
- **spark**: S=0 P=0 A=6 R=7 K=1
- **why**: A=6 changes the run's persistence method; R=7 withholds durable storage; K=1 limits retained history.
- **rent**: none — the mode explicitly avoids persistent session-file storage.
- **composes**: [[Noninteractive_Session_Resume]], [[Local_Rollout_JSONL_Store]]
- **confidence**: documented

### Rollout_Migration_Inspector
- **surface**: `codex migrate-rollouts [--thread <THREAD_ID>] [--json] [--verbose]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex migrate-rollouts --help` says omission of `--apply` only reports legacy sessions eligible for paginated thread history in codex-cli 0.150.0-alpha.8.
- **does**: Inspects legacy rollout eligibility for paginated history without publishing migration changes.
- **spark**: S=1 P=0 A=6 R=7 K=4
- **why**: S=1 exposes migration diagnosis; A=6 stages migration behind explicit apply; R=7 reaches legacy and projected stores; K=4 reports per-thread eligibility.
- **rent**: none — dry-run inspection incurs no persistent migration charge.
- **composes**: [[Local_Rollout_JSONL_Store]], [[Thread_History_Projection_Cursor]]
- **confidence**: documented

### Task_List_Tool
- **surface**: `list_threads({limit?})`
- **evidence**: `tool namespace: mcp__codex_app.list_threads` — Codex Desktop 26.820.9563.0 schema documents all pinned tasks plus recency-ordered non-pinned tasks, including backing kind, status, project context, title, and concise retrieval summary.
- **does**: Lists current tasks across Codex and ChatGPT surfaces.
- **spark**: S=0 P=0 A=3 R=9 K=5
- **why**: A=3 supports task selection; R=9 exposes the task catalog; K=5 returns status and retrieval metadata.
- **rent**: none — listing is a read-only request.
- **composes**: [[Desktop_Local_Thread_Catalog]], [[Task_History_Read_Tool]], [[Archived_Task_List_Tool]]
- **confidence**: documented

### Archived_Task_List_Tool
- **surface**: `list_archived_threads({hostId?, limit?, cursor?})`
- **evidence**: `tool namespace: mcp__codex_app.list_archived_threads` — Codex Desktop 26.820.9563.0 schema documents paginated archived task summaries for a selected or current host.
- **does**: Lists archived tasks with cursor pagination.
- **spark**: S=0 P=0 A=3 R=8 K=5
- **why**: A=3 supports archived-task selection; R=8 reaches archived catalog entries; K=5 returns archived task metadata.
- **rent**: none — listing is a read-only request.
- **composes**: [[Archived_Rollout_Store]], [[Task_Archive_Toggle_Tool]], [[Task_History_Read_Tool]]
- **confidence**: documented

### Task_History_Read_Tool
- **surface**: `read_thread({threadId, hostId?, cursor?, turnLimit?, includeOutputs?, maxOutputCharsPerItem?})`
- **evidence**: `tool namespace: mcp__codex_app.read_thread` — Codex Desktop 26.820.9563.0 schema documents recent task status/turn summaries, older-turn cursors, and bounded inclusion of command/tool outputs.
- **does**: Reads bounded recent or paginated older history for one task.
- **spark**: S=0 P=0 A=4 R=9 K=8
- **why**: A=4 supports paginated inspection; R=9 reaches task history and optional outputs; K=8 retrieves prior turn state.
- **rent**: none — reading adds no persistent state.
- **composes**: [[Thread_Turn_Projection]], [[Thread_Item_Projection]], [[Desktop_Thread_Timeline_Ledger]]
- **confidence**: documented

### Task_Archive_Toggle_Tool
- **surface**: `set_thread_archived({archived, threadId?, hostId?})`
- **evidence**: `tool namespace: mcp__codex_app.set_thread_archived` — Codex Desktop 26.820.9563.0 schema documents background archive or unarchive of the current or selected task.
- **does**: Sets a task's archived lifecycle state.
- **spark**: S=0 P=0 A=5 R=8 K=2
- **why**: A=5 changes task lifecycle placement; R=8 manages catalog reachability; K=2 retains task identity.
- **rent**: none — the toggle is a one-shot state update.
- **composes**: [[Archived_Task_List_Tool]], [[Session_Archive_Command]], [[Session_Unarchive_Command]]
- **confidence**: documented

### Task_Fork_Tool
- **surface**: `fork_thread({threadId?, environment?})`
- **evidence**: `tool namespace: mcp__codex_app.fork_thread` — Codex Desktop 26.820.9563.0 schema documents same-directory or worktree forks containing completed history only; worktree setup may return a client thread id.
- **does**: Creates a child task from the completed history of a source task.
- **spark**: S=1 P=0 A=9 R=8 K=6
- **why**: S=1 enables history-derived branching; A=9 creates an alternate task trajectory; R=8 creates a task/worktree resource; K=6 carries completed history.
- **rent**: every_spawn — each fork creates a new task and possibly a worktree.
- **composes**: [[Interactive_Session_Fork]], [[Task_History_Read_Tool]]
- **confidence**: documented

### Task_Pin_Tool
- **surface**: `set_thread_pinned({threadId, pinned})`
- **evidence**: `tool namespace: mcp__codex_app.set_thread_pinned` — Codex Desktop 26.820.9563.0 schema documents background pin or unpin for a selected task.
- **does**: Sets a task's pinned catalog state.
- **spark**: S=0 P=0 A=3 R=6 K=1
- **why**: A=3 changes task prioritization; R=6 changes catalog placement; K=1 retains the pinned flag.
- **rent**: none — pinning is a one-shot metadata update.
- **composes**: [[Task_List_Tool]], [[Thread_Catalog_Table]]
- **confidence**: documented

### Task_Title_Tool
- **surface**: `set_thread_title({threadId?, title})`
- **evidence**: `tool namespace: mcp__codex_app.set_thread_title` — Codex Desktop 26.820.9563.0 schema documents background rename of the current or selected task.
- **does**: Persists a user-supplied task title.
- **spark**: S=0 P=0 A=2 R=5 K=3
- **why**: A=2 aids later task selection; R=5 updates catalog metadata; K=3 preserves a human-readable identity.
- **rent**: none — renaming is a one-shot metadata update.
- **composes**: [[Task_List_Tool]], [[Session_Name_Index]], [[Thread_Catalog_Table]]
- **confidence**: documented

## Uncovered
- Resume, fork, archive, unarchive, delete, pin, rename, and migration-apply mutations were not exercised because this arm was read-only; destructive deletion semantics beyond CLI help remain unverified.
- Rollout, memory, timeline, and catalog payload values were intentionally not inspected; only filenames, counts, record types, keys, and database DDL were examined to protect unrelated conversation content.
- Cloud/remote backing-store internals were not reachable from local schemas. Scheduling/background wake is delegated to I11, child-agent orchestration to I3, and user-facing output behavior to I10.
