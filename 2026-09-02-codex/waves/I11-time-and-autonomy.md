# I11 Time and Autonomy

Pinned target: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; config root `C:\Users\Darian\.codex`; survey date 2026-09-02; repository commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`.

### Heartbeat_Automation_Create
- **surface**: `automation_update { kind: "heartbeat", mode: "create" | "suggested_create", ... }`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — The schema calls heartbeats proactive follow-ups attached to the current local thread by default and accepts `targetThreadId`.
- **does**: Creates a recurring follow-up attached to a chat.
- **spark**: S=2 P=3 A=9 R=3 K=0
- **why**: S enables scheduled continuation; P re-enters the user's conversation; A externalizes recurrence; R reaches the automation scheduler.
- **rent**: every_matching_call — each scheduled activation consumes agent runtime.
- **composes**: [[Existing_Chat_Scheduled_Task]], [[Automation_RRule_Schedule]], [[Automation_Run_State]]
- **confidence**: documented

### Cron_Automation_Create
- **surface**: `automation_update { kind: "cron", mode: "create" | "suggested_create", projectId, ... }`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — The schema defines cron automations as standalone local jobs against one project.
- **does**: Creates a standalone recurring project job.
- **spark**: S=2 P=1 A=9 R=4 K=0
- **why**: S enables scheduled project work; P separates runs from the current chat; A externalizes recurrence; R reaches a saved project.
- **rent**: every_matching_call — each scheduled activation consumes agent runtime.
- **composes**: [[Standalone_Scheduled_Task_Run]], [[Automation_RRule_Schedule]], [[Automation_Run_State]]
- **confidence**: documented

### Automation_Update
- **surface**: `automation_update { id, kind: "cron" | "heartbeat", mode: "update" | "suggested_update", ... }`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — Update mode requires the resolved id plus the full updated field set and instructs callers to preserve unchanged fields.
- **does**: Replaces the configuration of an existing scheduled task.
- **spark**: S=1 P=2 A=7 R=3 K=0
- **why**: S changes future automated behavior; P changes when the agent returns; A revises orchestration; R reaches stored automation state.
- **rent**: none — the update operation itself adds no recurring harness charge.
- **composes**: [[Automation_View]], [[Automation_RRule_Schedule]], [[Automation_Run_State]]
- **confidence**: documented

### Automation_View
- **surface**: `automation_update { id, mode: "view" }`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — View mode accepts only an automation id.
- **does**: Retrieves one scheduled task configuration.
- **spark**: S=0 P=0 A=2 R=6 K=1
- **why**: A supports inspection before lifecycle changes; R reaches stored automation state; K reveals the selected schedule configuration.
- **rent**: none — a read incurs no persistent charge.
- **composes**: [[Automation_Update]], [[Automation_Delete]]
- **confidence**: documented

### Automation_Delete
- **surface**: `automation_update { id, mode: "delete" }`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — Delete mode accepts only an automation id.
- **does**: Deletes one scheduled task.
- **spark**: S=0 P=3 A=6 R=2 K=0
- **why**: P ends future unsolicited re-entry; A terminates scheduled orchestration; R mutates stored automation state.
- **rent**: none — deletion ends rather than creates recurring work.
- **composes**: [[Automation_View]], [[Automation_Run_State]]
- **confidence**: documented

### Automation_RRule_Schedule
- **surface**: `rrule: string`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — Both cron and heartbeat create/update shapes require `rrule`; [Scheduled tasks](https://developers.openai.com/codex/app/automations.md) exposes advanced `RRULE` editing.
- **does**: Encodes the recurrence cadence for a scheduled task.
- **spark**: S=0 P=1 A=8 R=1 K=0
- **why**: P determines when the agent re-enters; A represents temporal orchestration; R stores the recurrence expression.
- **rent**: every_matching_call — every matching recurrence can trigger a run.
- **composes**: [[Heartbeat_Automation_Create]], [[Cron_Automation_Create]]
- **confidence**: documented

### Automation_Run_State
- **surface**: `status: "ACTIVE" | "PAUSED"`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — Every create/update shape requires the two-valued `status` field.
- **does**: Gates whether a scheduled task may run.
- **spark**: S=0 P=6 A=7 R=1 K=0
- **why**: P assigns the user authority over autonomous re-entry; A gates the recurring workflow; R persists the run state.
- **rent**: every_matching_call — active state permits future scheduled runs while paused state suppresses them.
- **composes**: [[Automation_Update]], [[Automation_View]]
- **confidence**: documented

### Automation_Notification_Policy
- **surface**: `notificationPolicy: "failed_runs_only" | null`
- **evidence**: `session tool schema: mcp__codex_app.automation_update (Codex Desktop 26.820.9563.0)` — The schema maps mute requests to `failed_runs_only`, maps unmute to null, and keeps notification preferences outside the prompt.
- **does**: Controls which scheduled-task outcomes notify the user.
- **spark**: S=0 P=9 A=3 R=1 K=0
- **why**: P governs interruption of the user; A filters run-result delivery; R stores notification preference.
- **rent**: every_matching_call — matching failed runs can produce a notification.
- **composes**: [[Scheduled_Task_Inbox]], [[Automation_Update]]
- **confidence**: documented

### Existing_Chat_Scheduled_Task
- **surface**: `Schedule a task inside a chat`
- **evidence**: [Scheduled tasks](https://developers.openai.com/codex/app/automations.md) — The section says the task uses the chat's existing context.
- **does**: Resumes an existing chat on a schedule.
- **spark**: S=2 P=5 A=9 R=2 K=5
- **why**: S enables scheduled continuation; P returns into an established conversation; A preserves an ongoing loop; R reaches the scheduler; K retains chat context.
- **rent**: every_matching_call — each scheduled continuation consumes agent runtime.
- **composes**: [[Heartbeat_Automation_Create]], [[Thread_Followup_Message]]
- **confidence**: documented

### Standalone_Scheduled_Task_Run
- **surface**: `Standalone scheduled task`
- **evidence**: [Scheduled tasks](https://developers.openai.com/codex/app/automations.md) — The management section states standalone tasks start a new chat for each scheduled run.
- **does**: Starts an independent chat for every scheduled execution.
- **spark**: S=2 P=2 A=9 R=3 K=0
- **why**: S enables background work; P separates delivery from the current chat; A isolates run context; R creates a task surface.
- **rent**: every_matching_call — each new run consumes agent runtime.
- **composes**: [[Cron_Automation_Create]], [[Scheduled_Task_Inbox]]
- **confidence**: documented

### Local_Scheduled_Task_Runtime
- **surface**: `Scheduled task with local project`
- **evidence**: [Scheduled tasks](https://developers.openai.com/codex/app/automations.md) — The page says, “Keep the computer on” for work that needs local files.
- **does**: Runs scheduled project work through the powered desktop host.
- **spark**: S=1 P=0 A=5 R=8 K=0
- **why**: S enables background local work; A binds execution to host availability; R consumes the project filesystem plus desktop runtime.
- **rent**: every_matching_call — every local run consumes host compute.
- **composes**: [[Cron_Automation_Create]], [[App_Server_Daemon_Start]]
- **confidence**: documented

### Scheduled_Task_Unattended_Permissions
- **surface**: `Scheduled task sandbox settings`
- **evidence**: [Scheduled tasks](https://developers.openai.com/codex/app/automations.md) — The permissions section specifies `approval_policy = "never"` when organization policy allows it.
- **does**: Runs scheduled work without interactive approval when policy permits.
- **spark**: S=0 P=10 A=6 R=2 K=0
- **why**: P governs who authorizes unattended actions; A removes an interactive gate from scheduled execution; R exposes the configured sandbox reach.
- **rent**: every_matching_call — the permission policy is applied on every scheduled run.
- **composes**: [[Cron_Automation_Create]], [[Heartbeat_Automation_Create]]
- **confidence**: documented

### Scheduled_Task_Inbox
- **surface**: `Scheduled`
- **evidence**: [Scheduled tasks](https://developers.openai.com/codex/app/automations.md) — The management section describes an “unread indicator” for runs needing attention.
- **does**: Surfaces background run results requiring user attention.
- **spark**: S=0 P=6 A=3 R=6 K=1
- **why**: P mediates when completed work interrupts the user; A collects asynchronous outcomes; R exposes stored runs; K reveals run findings.
- **rent**: every_matching_call — each reportable run deposits completion state.
- **composes**: [[Automation_Notification_Policy]], [[Standalone_Scheduled_Task_Run]]
- **confidence**: documented

### Thread_Followup_Message
- **surface**: `send_message_to_thread { threadId, prompt, model?, thinking? }`
- **evidence**: `session tool schema: mcp__codex_app.send_message_to_thread (Codex Desktop 26.820.9563.0)` — The tool sends a user-visible follow-up prompt to an existing Codex task or chat.
- **does**: Continues another task with a visible follow-up prompt.
- **spark**: S=1 P=6 A=8 R=3 K=0
- **why**: S triggers further work; P inserts user-visible speech into another task; A resumes an existing workflow; R reaches a selected task.
- **rent**: every_matching_call — each follow-up can trigger a model turn.
- **composes**: [[Existing_Chat_Scheduled_Task]], [[Desktop_Followup_Queue_Mode]]
- **confidence**: documented

### Cli_Thread_Message_Queue
- **surface**: `codex queue --thread <THREAD> --message <TEXT>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; `codex queue --help` says “Queue a message for an existing session” by UUID or exact name.
- **does**: Queues a follow-up message for an existing CLI session.
- **spark**: S=1 P=5 A=8 R=3 K=0
- **why**: S triggers further work; P inserts a message into another session; A defers follow-up delivery; R reaches a named session.
- **rent**: every_matching_call — each queued message can trigger a model turn.
- **composes**: [[Desktop_Followup_Queue_Mode]], [[Thread_Followup_Message]]
- **confidence**: documented

### Desktop_Followup_Queue_Mode
- **surface**: `[desktop] followUpQueueMode = "queue"`
- **evidence**: `C:\Users\Darian\.codex\config.toml:82` — Directly read `followUpQueueMode = "queue"` in the pinned local configuration.
- **does**: Queues desktop follow-ups behind active work.
- **spark**: S=0 P=4 A=8 R=1 K=0
- **why**: P controls when user input interrupts work; A serializes follow-up handling; R persists the desktop preference.
- **rent**: every_matching_call — the policy is consulted for every follow-up received during active work.
- **composes**: [[Thread_Followup_Message]], [[Cli_Thread_Message_Queue]]
- **confidence**: observed

### Multi_Thread_Wait
- **surface**: `wait_threads { targets[1..8], timeoutMs? }`
- **evidence**: `session tool schema: mcp__codex_app.wait_threads (Codex Desktop 26.820.9563.0)` — The tool waits for the first target to complete or need attention, accepts cursors, and returns compact timeout progress.
- **does**: Suspends coordination until one tracked task changes terminal attention state.
- **spark**: S=0 P=2 A=10 R=3 K=1
- **why**: P stops early for user-requiring attention; A coordinates asynchronous fan-in; R observes up to eight tasks; K returns compact progress.
- **rent**: none — waiting adds no persistent capability charge after return.
- **composes**: [[Thread_Followup_Message]], [[Scheduled_Task_Inbox]]
- **confidence**: documented

### Handoff_Status_Long_Poll
- **surface**: `get_handoff_status { operationId, afterRevision?, waitMs? }`
- **evidence**: `session tool schema: mcp__codex_app.get_handoff_status (Codex Desktop 26.820.9563.0)` — The schema supports revision-gated waits up to 60,000 ms while the UI continues showing progress.
- **does**: Waits for progress changes in an asynchronous task handoff.
- **spark**: S=0 P=1 A=8 R=3 K=1
- **why**: P avoids noisy unchanged updates; A coordinates background completion; R reaches operation state; K returns the changed revision.
- **rent**: none — a status wait creates no persistent charge.
- **composes**: [[Multi_Thread_Wait]]
- **confidence**: documented

### Turn_Ended_Notification_Hook
- **surface**: `notify = [<command>, "turn-ended"]`
- **evidence**: `C:\Users\Darian\.codex\config.toml:1` — Directly read a command array ending in `"turn-ended"` in the pinned local configuration.
- **does**: Invokes a configured notifier when an agent turn ends.
- **spark**: S=0 P=7 A=4 R=4 K=0
- **why**: P controls post-turn user interruption; A attaches behavior to lifecycle completion; R reaches a local notification executable.
- **rent**: every_turn — the configured hook is eligible after every completed turn.
- **composes**: [[Scheduled_Task_Inbox]], [[Automation_Notification_Policy]]
- **confidence**: observed

### App_Server_Daemon_Start
- **surface**: `codex app-server daemon start`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; daemon help documents starting the local app-server if it is not running.
- **does**: Starts the local app-server daemon idempotently.
- **spark**: S=0 P=0 A=5 R=8 K=0
- **why**: A establishes a persistent serving process; R exposes local app-server runtime.
- **rent**: every_turn — a running daemon remains available across task turns.
- **composes**: [[Local_Scheduled_Task_Runtime]], [[App_Server_Daemon_Stop]]
- **confidence**: documented

### App_Server_Daemon_Restart
- **surface**: `codex app-server daemon restart`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; daemon help lists a restart subcommand.
- **does**: Restarts the managed local app-server daemon.
- **spark**: S=0 P=0 A=5 R=7 K=0
- **why**: A resets a persistent service lifecycle; R controls local app-server runtime.
- **rent**: every_turn — the restarted daemon remains available across task turns.
- **composes**: [[App_Server_Daemon_Start]], [[App_Server_Daemon_Stop]]
- **confidence**: documented

### App_Server_Daemon_Stop
- **surface**: `codex app-server daemon stop`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; daemon help lists stopping the local app-server daemon.
- **does**: Stops the managed local app-server daemon.
- **spark**: S=0 P=2 A=6 R=5 K=0
- **why**: P restores user control over persistent service reachability; A terminates the service lifecycle; R withdraws local app-server runtime.
- **rent**: none — stopping the daemon ends its recurring host use.
- **composes**: [[App_Server_Daemon_Start]], [[App_Server_Daemon_Restart]]
- **confidence**: documented

### App_Server_Daemon_Remote_Control_Toggle
- **surface**: `codex app-server daemon enable-remote-control | disable-remote-control`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; daemon help documents toggling future starts plus the currently managed daemon.
- **does**: Gates remote control for the managed app-server daemon.
- **spark**: S=0 P=8 A=4 R=4 K=0
- **why**: P controls who may remotely direct the daemon; A changes persistent service behavior; R gates remote reachability.
- **rent**: every_turn — the enabled gate remains in force across future starts.
- **composes**: [[App_Server_Daemon_Start]]
- **confidence**: documented

### App_Server_Daemon_Version_Query
- **surface**: `codex app-server daemon version`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; daemon help says the command prints local CLI plus running app-server versions as JSON.
- **does**: Reports version alignment between the CLI and running daemon.
- **spark**: S=0 P=0 A=2 R=5 K=2
- **why**: A supports lifecycle diagnosis; R observes the daemon endpoint; K reveals both version identities.
- **rent**: none — a version query has no persistent charge.
- **composes**: [[App_Server_Daemon_Start]]
- **confidence**: documented

### Exec_Server_Stdin_Close_Lifetime
- **surface**: `codex exec-server --exit-on-stdin-close`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; exec-server help says the service exits when its parent-owned standard-input pipe closes.
- **does**: Binds exec-server lifetime to its parent input pipe.
- **spark**: S=0 P=0 A=9 R=4 K=0
- **why**: A couples background-service termination to parent liveness; R controls a local service process.
- **rent**: every_turn — the liveness binding remains active while the service runs.
- **composes**: [[App_Server_Daemon_Stop]]
- **confidence**: documented

### UTC_Offset_Time_Lookup
- **surface**: `web.run { time: [{ utc_offset: "+/-HH:MM" }] }`
- **evidence**: `session tool schema and result: web.run time (2026-09-02)` — Invoking offset `-05:00` returned `Sep 2, 2026, 1:25:02 PM`.
- **does**: Returns current wall-clock time for a UTC offset.
- **spark**: S=0 P=0 A=1 R=6 K=2
- **why**: A supports time-aware sequencing; R reaches a clock service; K reveals offset-localized current time.
- **rent**: none — a clock lookup leaves no persistent charge.
- **composes**: [[Automation_RRule_Schedule]]
- **confidence**: observed

## Uncovered
- No automation was created, updated, deleted, paused, resumed, or manually triggered because the assignment prohibited persistent scheduler mutations.
- No existing automation could be viewed because `C:\Users\Darian\.codex\automations` was absent; no automation list surface was exposed in the session namespace.
- Heartbeat wake-up delivery, cron execution, notification delivery, queued-message delivery, task waiting, handoff polling, and background completion were not exercised because doing so required mutating or waking user-owned tasks.
- Daemon bootstrap/start/restart/stop, remote-control toggles, pairing, exec-server launch, and parent-pipe termination were not exercised because launching or altering long-running services was prohibited.
- Child-agent orchestration, user-owned thread persistence, and shell process semantics were intentionally excluded as I3, I8, and I2 responsibilities respectively.
- Calendar/timezone lookup by named location, monotonic timers, sleep primitives, missed-run policy, retry/backoff policy, concurrency policy, run timeout policy, daylight-saving behavior, and catch-up semantics were not exposed by the inspected schemas or first-party scheduled-task page.
