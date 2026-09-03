### Exec_Command_Tool
- **surface**: `tools.exec_command({cmd})`
- **evidence**: `tool://functions.exec/tools.exec_command` — On Codex Desktop 26.820.9563.0, `Write-Output ('shell=' + $PSVersionTable.PSEdition)` returned `shell=Core` with `exit_code: 0`.
- **does**: Launches one shell command as a child process.
- **spark**: S=4 P=0 A=2 R=9 K=0
- **why**: S enables arbitrary installed command-line programs; A makes execution an invocable step; R exposes local compute and processes.
- **rent**: every_matching_call — process runtime and returned output are charged to the agent invocation.
- **composes**: [[Exec_Command_Shell_Selector]], [[Exec_Command_Working_Directory]], [[Exec_Command_Result_Envelope]]
- **confidence**: observed

### Exec_Command_Shell_Selector
- **surface**: `tools.exec_command({shell})`
- **evidence**: `tool://functions.exec/tools.exec_command` — Explicit `shell: "powershell.exe"` returned `shell=Core`; explicit `shell: "cmd.exe"` returned `shell=cmd` in this delegated session.
- **does**: Selects the shell executable used to interpret `cmd`.
- **spark**: S=1 P=0 A=4 R=7 K=0
- **why**: S permits shell-specific syntax; A selects an execution method; R reaches distinct installed interpreters.
- **rent**: every_matching_call — the selected interpreter incurs process startup and runtime.
- **composes**: [[Exec_Command_Tool]]
- **confidence**: observed

### Exec_Command_Working_Directory
- **surface**: `tools.exec_command({workdir})`
- **evidence**: `tool://functions.exec/tools.exec_command` — With `workdir: "C:\\Users\\Darian\\Desktop\\codex\\spark-probe"`, `Get-Location` returned that exact path.
- **does**: Sets the spawned command's working directory.
- **spark**: S=0 P=0 A=4 R=5 K=0
- **why**: A scopes command resolution to a chosen project context; R makes that directory the process context.
- **rent**: none — selecting a directory adds no persistent charge.
- **composes**: [[Exec_Command_Tool]]
- **confidence**: observed

### Exec_Command_Login_Mode
- **surface**: `tools.exec_command({login})`
- **evidence**: `tool://functions.exec/tools.exec_command` — The session tool schema states that `login` controls `-l/-i` shell semantics, defaults to true, and accepts false to disable them.
- **does**: Controls whether the launched shell uses login semantics.
- **spark**: S=0 P=0 A=4 R=3 K=0
- **why**: A chooses shell initialization behavior; R changes which inherited shell environment is reachable.
- **rent**: every_matching_call — login initialization is paid during matching shell startups.
- **composes**: [[Exec_Command_Tool]], [[Exec_Command_Shell_Selector]]
- **confidence**: documented

### Exec_Command_Pseudo_Terminal
- **surface**: `tools.exec_command({tty: true})`
- **evidence**: `tool://functions.exec/tools.exec_command` — A PowerShell call with `tty: true` emitted terminal control sequences plus a terminal-title sequence before yielding.
- **does**: Allocates a pseudo-terminal for the command.
- **spark**: S=2 P=0 A=6 R=7 K=0
- **why**: S supports terminal-dependent programs; A changes interaction style; R exposes a PTY device.
- **rent**: every_matching_call — PTY allocation and terminal-control output are charged to the call.
- **composes**: [[Exec_Command_Early_Yield]], [[Write_Stdin_Input]]
- **confidence**: observed

### Exec_Command_Early_Yield
- **surface**: `tools.exec_command({yield_time_ms})`
- **evidence**: `tool://functions.exec/tools.exec_command` — A 12-second PTY command with `yield_time_ms: 10000` returned after 10.0156064 seconds with `session_id: 39012` and only the pre-wait output.
- **does**: Yields an unfinished command as a resumable execution session.
- **spark**: S=0 P=0 A=8 R=5 K=0
- **why**: A permits bounded waiting and later continuation; R preserves access to the live process.
- **rent**: every_matching_call — waiting time and the retained live process are charged until completion.
- **composes**: [[Exec_Command_Pseudo_Terminal]], [[Write_Stdin_Poll]]
- **confidence**: observed

### Exec_Command_Output_Token_Cap
- **surface**: `tools.exec_command({max_output_tokens})`
- **evidence**: `tool://functions.exec/tools.exec_command` — With `max_output_tokens: 80`, 200 lines produced a warning, `original_token_count: 2200`, and a head/tail result with `2120 tokens truncated` in the middle.
- **does**: Caps returned command output while preserving boundary context.
- **spark**: S=0 P=0 A=6 R=4 K=0
- **why**: A bounds observation cost; R retains selected process output within the cap.
- **rent**: every_matching_call — returned output consumes agent context up to the requested cap.
- **composes**: [[Exec_Command_Result_Envelope]]
- **confidence**: observed

### Exec_Command_Result_Envelope
- **surface**: `tools.exec_command(...) -> {output, exit_code, wall_time_seconds, original_token_count, chunk_id, session_id?}`
- **evidence**: `tool://functions.exec/tools.exec_command` — Completed calls returned `output`, `exit_code`, `wall_time_seconds`, `original_token_count`, and `chunk_id`; the unfinished call returned `session_id` instead of `exit_code`. A command ending with `exit 7` returned `exit_code: 7` plus `Write-Error: probe-stderr`.
- **does**: Returns a structured execution result envelope.
- **spark**: S=0 P=0 A=6 R=5 K=1
- **why**: A exposes completion and continuation state for control flow; R returns captured process telemetry; K reveals the command's directly produced evidence.
- **rent**: none — the envelope adds no persistent charge beyond the execution call.
- **composes**: [[Exec_Command_Tool]], [[Exec_Command_Early_Yield]]
- **confidence**: observed

### Write_Stdin_Input
- **surface**: `tools.write_stdin({session_id, chars})`
- **evidence**: `tool://functions.exec/tools.write_stdin` — Sending `probe-input\r` to PTY session 31409 caused `[Console]::In.ReadLine()` to return it and the process to print `stdin=probe-input` before exiting 0.
- **does**: Writes characters into an existing execution session.
- **spark**: S=3 P=0 A=6 R=7 K=0
- **why**: S enables interaction with input-driven programs; A continues a suspended process; R reaches the process input stream.
- **rent**: every_matching_call — transmitted input and continued process runtime are charged to the call.
- **composes**: [[Exec_Command_Pseudo_Terminal]], [[Exec_Command_Early_Yield]]
- **confidence**: observed

### Write_Stdin_Poll
- **surface**: `tools.write_stdin({session_id, chars: ""})`
- **evidence**: `tool://functions.exec/tools.write_stdin` — An empty-input poll of session 39012 returned `phase=after` with `exit_code: 0` after the yielded process completed.
- **does**: Polls an existing execution session for new output or completion.
- **spark**: S=0 P=0 A=8 R=5 K=0
- **why**: A supports asynchronous command sequencing; R retrieves later process output and status.
- **rent**: every_matching_call — polling wait time and returned output are charged to the call.
- **composes**: [[Exec_Command_Early_Yield]], [[Exec_Command_Result_Envelope]]
- **confidence**: observed

### Exec_Cell_Yield_Control
- **surface**: `yield_control()`
- **evidence**: `tool://functions.exec/yield_control` — A JavaScript exec cell emitted `cell-phase=before`, called `yield_control()`, and immediately returned `Script running with cell ID 16` while its nested command continued.
- **does**: Yields accumulated cell output while the orchestration script continues running.
- **spark**: S=0 P=0 A=9 R=4 K=0
- **why**: A separates progress delivery from background completion; R retains the live orchestration cell.
- **rent**: every_matching_call — the live cell continues consuming execution time after yielding.
- **composes**: [[Exec_Cell_Wait]], [[Exec_Command_Tool]]
- **confidence**: observed

### Exec_Cell_Wait
- **surface**: `functions.wait({cell_id, yield_time_ms, max_tokens, terminate?})`
- **evidence**: `tool://functions.wait` — Waiting on cell 16 returned only the new `cell-phase=after` output and closed the cell after script completion.
- **does**: Resumes observation of a yielded exec cell.
- **spark**: S=0 P=0 A=9 R=4 K=0
- **why**: A synchronizes with background orchestration; R retrieves subsequent cell output.
- **rent**: every_matching_call — wait latency and newly returned tokens are charged to the caller.
- **composes**: [[Exec_Cell_Yield_Control]]
- **confidence**: observed

### Exec_Command_Escalation_Request
- **surface**: `tools.exec_command({sandbox_permissions: "require_escalated", justification, prefix_rule?})`
- **evidence**: `tool://functions.exec/tools.exec_command` — The session schema defines `require_escalated` as unsandboxed execution, requires a user-facing approval question, and permits a reusable command-prefix rule.
- **does**: Requests unsandboxed command authority through user approval.
- **spark**: S=0 P=10 A=5 R=3 K=0
- **why**: P decides who may authorize elevated execution; A gates the execution path; R conditionally unlocks unsandboxed process reach.
- **rent**: every_matching_call — each unmatched escalation may charge user attention and approval latency.
- **composes**: [[Exec_Command_Tool]], [[Delegated_Never_Approval_Policy]]
- **confidence**: documented

### Delegated_Danger_Full_Access_Mode
- **surface**: `sandbox_mode: danger-full-access`
- **evidence**: `session://permissions` — The delegated session declares `danger-full-access`, unrestricted filesystem access, and enabled network; `codex doctor --summary` independently reported `filesystem unrestricted · network enabled` under codex-cli 0.150.0-alpha.8.
- **does**: Executes session commands without a filesystem sandbox.
- **spark**: S=0 P=10 A=2 R=5 K=0
- **why**: P fixes the authority boundary for every command; A removes sandbox routing; R exposes host filesystem and network reach.
- **rent**: every_turn — the unsandboxed authority posture applies throughout the delegated session.
- **composes**: [[Exec_Command_Tool]], [[Delegated_Never_Approval_Policy]]
- **confidence**: observed

### Delegated_Never_Approval_Policy
- **surface**: `approval policy: never`
- **evidence**: `session://permissions` — The delegated session states `Approval policy is currently never`, forbids escalation requests, and says commands using `sandbox_permissions` will be rejected.
- **does**: Suppresses approval prompts for delegated command execution.
- **spark**: S=0 P=10 A=7 R=0 K=0
- **why**: P removes the user's per-command authorization role; A routes failures directly back to the agent.
- **rent**: every_turn — the authority rule governs every delegated turn.
- **composes**: [[Exec_Command_Escalation_Request]], [[Exec_Command_Tool]]
- **confidence**: observed

### Cli_Sandbox_Mode
- **surface**: `codex --sandbox <read-only|workspace-write|danger-full-access>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` on codex-cli 0.150.0-alpha.8 lists the three values as policies for model-generated shell commands.
- **does**: Selects the sandbox policy for model-generated shell commands.
- **spark**: S=0 P=9 A=4 R=4 K=0
- **why**: P defines command authority; A selects isolation strategy; R bounds filesystem reach.
- **rent**: every_matching_call — sandbox setup is incurred when protected commands execute.
- **composes**: [[Cli_Approval_Policy]], [[Restricted_Token_Sandbox_Command]]
- **confidence**: documented

### Approval_Policy
- **surface**: `codex --ask-for-approval <on-request|never>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` on codex-cli 0.150.0-alpha.8 says `on-request` lets the model decide when to ask and `never` immediately returns execution failures to the model.
- **does**: Selects when model-generated commands require human approval.
- **spark**: S=0 P=10 A=6 R=0 K=0
- **why**: P assigns approval initiative; A gates execution or failure return.
- **rent**: every_matching_call — approval prompts charge user attention only when the selected mode requests them.
- **composes**: [[Cli_Sandbox_Mode]], [[Cli_Automatic_Approval_Review]]
- **confidence**: observed

### Cli_Automatic_Approval_Review
- **surface**: `codex --approve-for-me`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` on codex-cli 0.150.0-alpha.8 says approval requests are routed through automatic review using the workspace-write sandbox.
- **does**: Routes command approvals through automatic review.
- **spark**: S=0 P=10 A=7 R=1 K=0
- **why**: P delegates the user's approval role to a reviewer; A inserts an automatic gate; R fixes workspace-write reach.
- **rent**: every_matching_call — automatic review work is charged on commands requiring approval.
- **composes**: [[Cli_Approval_Policy]], [[Cli_Sandbox_Mode]]
- **confidence**: documented

### Cli_Approval_And_Sandbox_Bypass
- **surface**: `codex --dangerously-bypass-approvals-and-sandbox`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` on codex-cli 0.150.0-alpha.8 labels the flag `EXTREMELY DANGEROUS` and limits its intended use to externally sandboxed environments.
- **does**: Enables unrestricted unconfirmed command execution.
- **spark**: S=0 P=10 A=3 R=5 K=0
- **why**: P removes both authorization barriers; A bypasses enforcement routing; R exposes unsandboxed execution reach.
- **rent**: every_turn — the bypass governs the full CLI invocation.
- **composes**: [[Cli_Approval_Policy]], [[Cli_Sandbox_Mode]]
- **confidence**: documented

### Cli_Additional_Writable_Root
- **surface**: `codex --add-dir <DIR>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex --help` on codex-cli 0.150.0-alpha.8 defines repeatable additional writable directories beside the primary workspace.
- **does**: Grants workspace-write authority to another directory.
- **spark**: S=0 P=8 A=2 R=6 K=0
- **why**: P expands the write boundary; A scopes execution to explicit extra roots; R exposes additional filesystem assets.
- **rent**: every_turn — the added write authority persists for the CLI invocation.
- **composes**: [[Cli_Sandbox_Mode]]
- **confidence**: documented

### Restricted_Token_Sandbox_Command
- **surface**: `codex sandbox -- <COMMAND>...`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, `codex sandbox -- cmd.exe /c ver` exited 0; `codex sandbox -- cmd.exe /c "whoami & whoami /priv"` ran as `desktop-9976713\codexsandboxoffline` with only enabled `SeChangeNotifyPrivilege`.
- **does**: Runs a command under the Windows restricted-token sandbox.
- **spark**: S=3 P=8 A=6 R=7 K=0
- **why**: S provides isolated command execution; P enforces a reduced process identity; A wraps commands in isolation; R exposes sandboxed local compute.
- **rent**: every_matching_call — restricted-token setup and child-process runtime are charged per command.
- **composes**: [[Sandbox_State_Json]], [[Sandbox_Permission_Profile]]
- **confidence**: observed

### Sandbox_State_Json
- **surface**: `codex sandbox --sandbox-state-json <JSON>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex sandbox --help` on codex-cli 0.150.0-alpha.8 accepts a JSON value from `codex/sandbox-state-meta` for direct application.
- **does**: Applies an explicit sandbox state to a command.
- **spark**: S=0 P=8 A=6 R=4 K=0
- **why**: P supplies the command's authority envelope; A selects an explicit isolation state; R fixes accessible resources.
- **rent**: every_matching_call — state parsing and sandbox setup occur for each invocation.
- **composes**: [[Restricted_Token_Sandbox_Command]], [[Sandbox_State_Readable_Root]], [[Sandbox_State_Network_Disable]]
- **confidence**: documented

### Sandbox_State_Readable_Root
- **surface**: `codex sandbox --sandbox-state-readable-root <PATH>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex sandbox --help` on codex-cli 0.150.0-alpha.8 says the repeatable flag adds readable roots to the supplied sandbox state.
- **does**: Adds a readable root to supplied sandbox state.
- **spark**: S=0 P=8 A=3 R=6 K=0
- **why**: P expands read authority; A refines the isolation state; R exposes another filesystem root.
- **rent**: every_matching_call — root policy resolution occurs when the sandbox launches.
- **composes**: [[Sandbox_State_Json]], [[Restricted_Token_Sandbox_Command]]
- **confidence**: documented

### Sandbox_State_Network_Disable
- **surface**: `codex sandbox --sandbox-state-disable-network`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex sandbox --help` on codex-cli 0.150.0-alpha.8 says the flag disables direct network access in the supplied sandbox state.
- **does**: Disables direct network access in supplied sandbox state.
- **spark**: S=0 P=9 A=3 R=4 K=0
- **why**: P removes network authority; A refines the isolation state; R restricts external reach.
- **rent**: every_matching_call — network policy enforcement is incurred by matching sandboxed commands.
- **composes**: [[Sandbox_State_Json]], [[Restricted_Token_Sandbox_Command]]
- **confidence**: documented

### Sandbox_Permission_Profile
- **surface**: `codex sandbox --permission-profile <NAME>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex sandbox --help` on codex-cli 0.150.0-alpha.8 defines a named permissions profile from the active configuration stack.
- **does**: Selects a named permission profile for sandbox execution.
- **spark**: S=0 P=10 A=5 R=3 K=0
- **why**: P chooses the authority policy; A selects a reusable enforcement approach; R determines the profile's reachable resources.
- **rent**: every_matching_call — profile resolution and enforcement occur for each matching sandbox invocation.
- **composes**: [[Restricted_Token_Sandbox_Command]]
- **confidence**: documented

### Noninteractive_Exec_Command
- **surface**: `codex exec [OPTIONS] [PROMPT]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec --help` on codex-cli 0.150.0-alpha.8 describes `exec` as running Codex non-interactively.
- **does**: Launches a noninteractive Codex agent run.
- **spark**: S=4 P=0 A=8 R=7 K=0
- **why**: S makes model-driven command work scriptable; A removes interactive TUI control; R reaches model and local tool resources.
- **rent**: every_matching_call — model tokens, tool calls, and process runtime are charged per run.
- **composes**: [[Exec_Prompt_Stdin]], [[Exec_JSONL_Event_Output]], [[Exec_Last_Message_File]], [[Exec_Response_Schema]]
- **confidence**: documented

### Exec_Prompt_Stdin
- **surface**: `codex exec -`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec --help` on codex-cli 0.150.0-alpha.8 says omitted or `-` prompts read stdin; piped stdin accompanying an argument is appended as a `<stdin>` block.
- **does**: Supplies noninteractive instructions through standard input.
- **spark**: S=2 P=0 A=6 R=5 K=0
- **why**: S permits generated instruction payloads; A composes shell pipelines with agent execution; R exposes the standard-input stream.
- **rent**: every_matching_call — supplied prompt tokens are charged to the agent run.
- **composes**: [[Noninteractive_Exec_Command]]
- **confidence**: documented

### Exec_JSONL_Event_Output
- **surface**: `codex exec --json`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec --help` on codex-cli 0.150.0-alpha.8 states that events are printed to stdout as JSONL.
- **does**: Streams noninteractive run events as JSONL.
- **spark**: S=1 P=0 A=7 R=5 K=0
- **why**: S enables machine consumption; A exposes event-level automation flow; R returns structured execution events.
- **rent**: every_matching_call — event serialization and output volume are charged per run.
- **composes**: [[Noninteractive_Exec_Command]]
- **confidence**: documented

### Exec_Last_Message_File
- **surface**: `codex exec --output-last-message <FILE>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec --help` on codex-cli 0.150.0-alpha.8 says the agent's last message is written to the specified file.
- **does**: Writes the final agent message to a chosen file.
- **spark**: S=1 P=0 A=5 R=5 K=0
- **why**: S makes final output consumable by scripts; A separates final output from the event stream; R reaches a caller-selected file.
- **rent**: every_matching_call — one output-file write is charged per run using the flag.
- **composes**: [[Noninteractive_Exec_Command]]
- **confidence**: documented

### Exec_Response_Schema
- **surface**: `codex exec --output-schema <FILE>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec --help` on codex-cli 0.150.0-alpha.8 accepts a JSON Schema file describing the model's final response shape.
- **does**: Constrains the final response to a caller-supplied JSON Schema.
- **spark**: S=2 P=0 A=8 R=4 K=0
- **why**: S enables typed automation outputs; A imposes a validation-oriented response method; R reads the schema asset.
- **rent**: every_matching_call — schema tokens and structured generation are charged to matching runs.
- **composes**: [[Noninteractive_Exec_Command]]
- **confidence**: documented

### Doctor_Diagnostics_Command
- **surface**: `codex doctor [--summary] [--ascii] [--no-color] [--json]`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — On codex-cli 0.150.0-alpha.8, `codex doctor --summary --ascii --no-color` produced grouped installation, environment, configuration, desktop, connectivity, and server checks; it returned exit code 1 with `1 fail failed`. Help says `--json` emits a redacted machine-readable report.
- **does**: Diagnoses local Codex installation and runtime health.
- **spark**: S=6 P=0 A=5 R=5 K=3
- **why**: S adds a purpose-built health check; A standardizes diagnostic procedure; R inspects local runtime surfaces; K returns installation-specific health facts.
- **rent**: every_matching_call — checks, connectivity probes, and report output are charged per diagnostic run.
- **composes**: [[Exec_Command_Tool]]
- **confidence**: observed

### Standalone_Exec_Server
- **surface**: `codex exec-server`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec-server --help` on codex-cli 0.150.0-alpha.8 labels the command experimental and describes it as a standalone exec-server service.
- **does**: Serves command execution through a standalone process.
- **spark**: S=4 P=0 A=7 R=9 K=0
- **why**: S exposes execution as a service; A decouples execution from the caller; R publishes local execution capacity.
- **rent**: every_matching_call — server compute and child-command runtime are charged per served request.
- **composes**: [[Exec_Server_Concurrency_Limit]], [[Exec_Server_Transport]], [[Exec_Server_Stdin_Close_Lifetime]]
- **confidence**: documented

### Exec_Server_Concurrency_Limit
- **surface**: `codex exec-server --concurrent-requests <COUNT>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec-server --help` on codex-cli 0.150.0-alpha.8 defines the maximum requests processed concurrently per connection and defaults it to 1.
- **does**: Caps concurrent execution requests per connection.
- **spark**: S=0 P=0 A=9 R=4 K=0
- **why**: A governs scheduling and backpressure; R bounds simultaneous execution capacity.
- **rent**: every_matching_call — admitted concurrent requests consume server compute while active.
- **composes**: [[Standalone_Exec_Server]]
- **confidence**: documented

### Exec_Server_Transport
- **surface**: `codex exec-server --listen <ws://IP:PORT|stdio|stdio://>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec-server --help` on codex-cli 0.150.0-alpha.8 lists WebSocket and stdio endpoints, with `ws://IP:PORT` as the default form.
- **does**: Selects the exec-server transport endpoint.
- **spark**: S=0 P=0 A=6 R=8 K=0
- **why**: A chooses process-pipe or socket integration; R exposes the service through distinct transports.
- **rent**: every_matching_call — transport I/O is charged to each served request.
- **composes**: [[Standalone_Exec_Server]]
- **confidence**: documented

### Exec_Server_Stdin_Close_Lifetime
- **surface**: `codex exec-server --exit-on-stdin-close`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex exec-server --help` on codex-cli 0.150.0-alpha.8 says the server exits when its parent-owned standard-input pipe closes.
- **does**: Couples exec-server lifetime to the parent stdin pipe.
- **spark**: S=0 P=0 A=8 R=3 K=0
- **why**: A provides parent-driven lifecycle control; R observes the standard-input pipe as a liveness resource.
- **rent**: every_turn — the liveness watch persists for the server process lifetime.
- **composes**: [[Standalone_Exec_Server]], [[Exec_Server_Transport]]
- **confidence**: documented

## Uncovered
- Escalation, automatic approval, dangerous bypass, added writable roots, supplied sandbox state, readable-root expansion, permission profiles, and network-disable enforcement were not exercised because this delegated session forbids approval requests and the probe permits only read-only diagnostics.
- `codex exec` model runs and `codex exec-server` service startup were not exercised because they can persist sessions or leave a listening process; their rows are limited to CLI help text.
- Configuration keys, execution-policy rule files, and lifecycle hooks were intentionally excluded as I6 territory.
- Unix sandbox implementations were unavailable on the pinned Windows NT 10.0.26200.0 target.
