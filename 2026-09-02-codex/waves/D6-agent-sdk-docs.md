# D6 App Server, SDK, Noninteractive, GitHub Action, and Scheduled Tasks Docs

Target pin: Codex Desktop `26.820.9563.0`; `codex-cli 0.150.0-alpha.8`; Windows NT `10.0.26200.0`; documentary survey date `2026-09-02`. Evidence comes from the fresh official OpenAI manual cached at `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md`; no server, SDK, action, scheduled task, or agent workflow was executed.

### App_Server_Deep_Client_Interface
- **surface**: `codex app-server`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30295` — “Use it when you want a deep integration inside your own product: authentication, conversation history, approvals, and streamed agent events.”
- **does**: Exposes Codex as a protocol surface for rich custom clients.
- **spark**: S=3 P=4 A=3 R=9 K=0
- **why**: S from enabling embedded Codex workflows; P from mediating approvals; A from external lifecycle control; R from exposing the agent runtime to another product
- **rent**: every_turn — each agent turn consumes the user’s configured Codex service usage
- **composes**: [[App_Server_Initialization_Handshake]], [[App_Server_Item_Event_Stream]], [[App_Server_Command_Approval_Handshake]]
- **confidence**: documented

### App_Server_Transport_Selection
- **surface**: `codex app-server --listen {stdio://|ws://IP:PORT|unix://|off}`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30351` — “Supported transports” are stdio JSONL, experimental WebSocket, Unix-socket WebSocket, and `off`.
- **does**: Selects how a client exchanges app-server protocol messages.
- **spark**: S=0 P=0 A=2 R=8 K=0
- **why**: A from choosing a client/server deployment topology; R from exposing local stream, socket, or WebSocket connectivity
- **rent**: none — transport selection adds no persistent prompt or model cost
- **composes**: [[App_Server_JSON_RPC_Message_Model]], [[App_Server_WebSocket_Authentication]]
- **confidence**: documented

### App_Server_WebSocket_Authentication
- **surface**: `--ws-auth {capability-token|signed-bearer-token}`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30379` — the manual lists capability-token and signed-bearer-token flags and says authentication is enforced before JSON-RPC `initialize`.
- **does**: Gates a WebSocket app-server connection on a configured bearer credential.
- **spark**: S=0 P=9 A=1 R=2 K=0
- **why**: P from deciding which client may reach the server; A from placing an authentication gate before initialization; R from conditionally exposing a remote transport
- **rent**: none — the authentication check does not add model context or service usage
- **composes**: [[App_Server_Transport_Selection]], [[App_Server_Initialization_Handshake]]
- **confidence**: documented

### App_Server_Overload_Backpressure
- **surface**: `JSON-RPC error -32001 "Server overloaded; retry later."`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30395` — bounded WebSocket queues reject ingress with `-32001`; clients should retry with exponential delay and jitter.
- **does**: Signals transient app-server saturation to programmatic clients.
- **spark**: S=0 P=0 A=5 R=2 K=1
- **why**: A from requiring a retry strategy; R from exposing bounded request capacity; K from revealing the overload state
- **rent**: every_matching_call — only rejected saturated requests incur client retry latency
- **composes**: [[App_Server_Transport_Selection]], [[App_Server_JSON_RPC_Message_Model]]
- **confidence**: documented

### App_Server_JSON_RPC_Message_Model
- **surface**: `{ "method": ..., "params": ..., "id": ... }`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30400` — requests carry `method`, `params`, and `id`; responses carry the same `id` plus `result` or `error`; notifications omit `id`.
- **does**: Correlates bidirectional app-server requests and responses while distinguishing notifications.
- **spark**: S=1 P=0 A=3 R=7 K=1
- **why**: S from enabling a client implementation; A from defining asynchronous message coordination; R from providing the wire contract; K from exposing result and error state
- **rent**: none — message framing itself carries no recurring model charge
- **composes**: [[App_Server_Transport_Selection]], [[App_Server_Item_Event_Stream]]
- **confidence**: documented

### App_Server_Version_Matched_Schema_Generation
- **surface**: `codex app-server generate-{ts|json-schema} --out ./schemas`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30424` — “Each output is specific to the Codex version you ran, so the generated artifacts match that version exactly.”
- **does**: Generates a TypeScript or JSON Schema contract matched to the invoked Codex binary.
- **spark**: S=4 P=0 A=2 R=5 K=7
- **why**: S from enabling typed client generation; A from supporting contract-driven integration; R from producing reusable schema assets; K from materializing the exact version’s protocol vocabulary
- **rent**: none — generation is a local one-shot operation
- **composes**: [[App_Server_JSON_RPC_Message_Model]], [[App_Server_Experimental_API_Opt_In]]
- **confidence**: documented

### App_Server_Initialization_Handshake
- **surface**: `initialize` then `initialized`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30505` — clients must initialize once per transport connection; pre-initialization requests receive `Not initialized`, and repeats receive `Already initialized`.
- **does**: Establishes one identified client session before other app-server methods run.
- **spark**: S=0 P=3 A=7 R=3 K=0
- **why**: P from requiring client identity metadata; A from enforcing connection lifecycle order; R from unlocking the method surface
- **rent**: none — the handshake adds no model call
- **composes**: [[App_Server_Client_Capability_Negotiation]], [[App_Server_Experimental_API_Opt_In]]
- **confidence**: documented

### App_Server_Client_Capability_Negotiation
- **surface**: `initialize.params.capabilities`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30511` — capabilities include exact notification opt-outs, attestation requests, and OpenAI-form MCP elicitation.
- **does**: Declares optional client behaviors for one app-server connection.
- **spark**: S=1 P=3 A=5 R=4 K=0
- **why**: S from enabling optional host behaviors; P from negotiating attestation and elicitation support; A from tailoring server/client coordination; R from selectively exposing protocol features
- **rent**: none — capability declaration is connection metadata
- **composes**: [[App_Server_Initialization_Handshake]], [[App_Server_Item_Event_Stream]]
- **confidence**: documented

### App_Server_Experimental_API_Opt_In
- **surface**: `capabilities.experimentalApi: true`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30560` — experimental methods and fields are rejected unless the client opts in.
- **does**: Gates experimental app-server methods and fields per connection.
- **spark**: S=0 P=7 A=3 R=3 K=0
- **why**: P from deciding whether the client accepts unstable authority surfaces; A from segmenting stable and experimental workflows; R from conditionally unlocking additional methods
- **rent**: none — opt-in has no direct usage charge
- **composes**: [[App_Server_Initialization_Handshake]], [[App_Server_Dynamic_Tool_Bridge]]
- **confidence**: documented

### App_Server_Model_Capability_Discovery
- **surface**: `model/list`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30683` — entries expose supported/default reasoning effort, upgrade metadata, visibility, input modalities, personality support, and default status.
- **does**: Lists models and their client-relevant capabilities for selector construction.
- **spark**: S=0 P=1 A=2 R=5 K=8
- **why**: P from surfacing personality support; A from informing model-selection flow; R from exposing the model catalog; K from revealing per-model capability metadata
- **rent**: none — this is a catalog read
- **composes**: [[App_Server_Turn_Start]], [[App_Server_Feature_Lifecycle_Discovery]]
- **confidence**: documented

### App_Server_Feature_Lifecycle_Discovery
- **surface**: `experimentalFeature/list`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30723` — the endpoint returns feature flags with lifecycle stages including beta, under-development, stable, deprecated, and removed.
- **does**: Lists feature flags with current enablement and lifecycle stage metadata.
- **spark**: S=0 P=0 A=2 R=4 K=8
- **why**: A from supporting staged client behavior; R from exposing runtime feature controls; K from revealing lifecycle and enablement state
- **rent**: none — this is a metadata read
- **composes**: [[App_Server_Experimental_API_Opt_In]], [[App_Server_Model_Capability_Discovery]]
- **confidence**: documented

### App_Server_Thread_Start
- **surface**: `thread/start`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30780` — the request starts a fresh conversation with optional model, working directory, approval policy, sandbox, personality, and service name.
- **does**: Creates a new configurable Codex conversation for later turns.
- **spark**: S=2 P=4 A=6 R=6 K=0
- **why**: S from creating a usable agent session; P from setting approval and personality behavior; A from beginning a persistent workflow; R from binding model and workspace resources
- **rent**: every_turn — subsequent thread turns consume user service usage
- **composes**: [[App_Server_Turn_Start]], [[App_Server_Thread_Resume]], [[App_Server_Thread_Fork]]
- **confidence**: documented

### App_Server_Thread_Resume
- **surface**: `thread/resume`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30830` — resume continues a recorded thread ID and accepts the same configuration overrides as start.
- **does**: Reloads a stored Codex conversation for additional turns.
- **spark**: S=1 P=2 A=7 R=5 K=4
- **why**: S from restoring an agent workflow; P from permitting behavior overrides; A from continuing prior execution; R from reaching persisted session state; K from restoring accumulated conversation context
- **rent**: every_turn — resumed turns consume user service usage
- **composes**: [[App_Server_Thread_Start]], [[App_Server_Turn_Start]], [[App_Server_Read_Without_Resume]]
- **confidence**: documented

### App_Server_Thread_Fork
- **surface**: `thread/fork`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30886` — forking creates a new thread ID, can copy history through `lastTurnId`, and can be made ephemeral.
- **does**: Branches stored conversation history into a new Codex thread.
- **spark**: S=1 P=0 A=9 R=4 K=4
- **why**: S from enabling an alternate agent continuation; A from creating a branch in workflow history; R from creating a new session resource; K from copying selected prior context
- **rent**: every_turn — the fork’s later turns consume user service usage
- **composes**: [[App_Server_Thread_Start]], [[App_Server_Thread_History_Pagination]]
- **confidence**: documented

### App_Server_Read_Without_Resume
- **surface**: `thread/read`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30930` — the method returns stored thread data without loading it or subscribing the client to its events.
- **does**: Reads a persisted thread without activating its runtime session.
- **spark**: S=0 P=0 A=2 R=6 K=7
- **why**: A from separating inspection from continuation; R from reaching stored thread records; K from exposing summary or turn history
- **rent**: none — the read performs no agent turn
- **composes**: [[App_Server_Thread_Resume]], [[App_Server_Thread_History_Pagination]]
- **confidence**: documented

### App_Server_Thread_History_Pagination
- **surface**: `thread/turns/list` and `thread/items/list`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30944` — experimental endpoints page stored turns or items without resuming the thread and offer omitted, summary, or full item views.
- **does**: Pages persisted conversation history at turn or item granularity.
- **spark**: S=0 P=0 A=3 R=6 K=8
- **why**: A from enabling incremental history loading; R from exposing persisted turn and item stores; K from returning selectable history detail
- **rent**: none — pagination performs no model call
- **composes**: [[App_Server_Read_Without_Resume]], [[App_Server_Thread_Fork]]
- **confidence**: documented

### App_Server_Thread_Compaction
- **surface**: `thread/compact/start`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31130` — the request returns immediately while progress streams as normal turn/item events including a `contextCompaction` item.
- **does**: Starts manual history compaction for a thread.
- **spark**: S=2 P=0 A=7 R=3 K=4
- **why**: S from maintaining a usable long conversation; A from inserting a context-management phase; R from consuming a model/runtime operation; K from transforming retained conversation context
- **rent**: every_matching_call — each requested compaction consumes runtime and possibly model usage
- **composes**: [[App_Server_Item_Event_Stream]], [[App_Server_Thread_Resume]]
- **confidence**: documented

### App_Server_Turn_Start
- **surface**: `turn/start`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31204` — turn input accepts text, remote image, and local image items, with per-turn model, effort, personality, working-directory, sandbox, and summary overrides.
- **does**: Begins agent work from multimodal input inside a thread.
- **spark**: S=7 P=4 A=6 R=7 K=0
- **why**: S from invoking the coding agent on text or images; P from setting personality and approval behavior; A from advancing the conversation lifecycle; R from binding model, files, and sandbox resources
- **rent**: every_turn — each invocation consumes user service usage
- **composes**: [[App_Server_Thread_Start]], [[App_Server_Turn_Structured_Output]], [[App_Server_Item_Event_Stream]]
- **confidence**: documented

### App_Server_Turn_Structured_Output
- **surface**: `turn/start.params.outputSchema`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31212` — `outputSchema` applies only to the current turn; the example supplies a JSON object schema.
- **does**: Constrains one app-server turn’s final response to a supplied schema.
- **spark**: S=7 P=0 A=4 R=1 K=1
- **why**: S from producing machine-consumable agent results; A from enforcing a downstream contract; R from using the model’s structured-output surface; K from encoding requested output fields
- **rent**: every_matching_call — schema enforcement is charged with the turn that uses it
- **composes**: [[App_Server_Turn_Start]], [[Exec_Output_Schema]]
- **confidence**: documented

### App_Server_Turn_Steering
- **surface**: `turn/steer`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31299` — steering appends user input to the active turn, requires the expected active turn ID, and creates no new turn.
- **does**: Injects additional user direction into an in-flight turn.
- **spark**: S=1 P=8 A=8 R=1 K=0
- **why**: S from redirecting ongoing agent work; P from giving the user mid-turn control; A from changing execution without a new turn; R from reaching the active generation
- **rent**: every_matching_call — each steering message adds context to the active turn
- **composes**: [[App_Server_Turn_Start]], [[App_Server_Turn_Interruption]]
- **confidence**: documented

### App_Server_Turn_Interruption
- **surface**: `turn/interrupt`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31332` — a successful interrupt finishes the addressed turn with `status: "interrupted"`.
- **does**: Requests cancellation of an in-flight app-server turn.
- **spark**: S=0 P=9 A=7 R=1 K=0
- **why**: P from giving the client cancellation authority; A from terminating active work; R from controlling a live generation
- **rent**: none — interruption stops rather than adds model work
- **composes**: [[App_Server_Turn_Start]], [[App_Server_Turn_Steering]]
- **confidence**: documented

### App_Server_Sandboxed_Command_Execution
- **surface**: `command/exec`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31442` — the method runs one argv-array command under the server sandbox without creating a thread.
- **does**: Executes a standalone command under an explicit app-server sandbox policy.
- **spark**: S=5 P=6 A=2 R=8 K=0
- **why**: S from running a system command; P from bounding its authority; A from bypassing conversation creation; R from exposing process and filesystem resources
- **rent**: every_matching_call — each command consumes host compute
- **composes**: [[App_Server_Admin_Requirements_Read]], [[App_Server_Approval_Handshake]]
- **confidence**: documented

### App_Server_Item_Event_Stream
- **surface**: `turn/*`, `item/*`, and `serverRequest/resolved` notifications
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31537` — server notifications stream thread, turn, item, and resolved-request lifecycle state; completed items are authoritative.
- **does**: Streams incremental and final agent-work state to subscribed clients.
- **spark**: S=1 P=1 A=7 R=7 K=7
- **why**: S from enabling responsive client rendering; P from exposing resolved user gates; A from reporting lifecycle transitions; R from opening a live event surface; K from revealing commands, edits, messages, plans, and tool outcomes
- **rent**: every_turn — event volume recurs across every streamed agent turn
- **composes**: [[App_Server_JSON_RPC_Message_Model]], [[App_Server_Turn_Start]], [[App_Server_Approval_Handshake]]
- **confidence**: documented

### App_Server_Approval_Handshake
- **surface**: `item/commandExecution/requestApproval` and `item/fileChange/requestApproval`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31635` — app-server sends client requests for command or file-change decisions and resumes or declines work after the response.
- **does**: Delegates approval decisions for proposed execution or edits to the client.
- **spark**: S=0 P=10 A=7 R=1 K=2
- **why**: P from assigning action authority to the user-facing client; A from gating work on a response; R from conditionally unlocking commands or writes; K from presenting the proposed action
- **rent**: every_matching_call — each gated action requires a decision round trip
- **composes**: [[App_Server_Item_Event_Stream]], [[App_Server_Sandboxed_Command_Execution]]
- **confidence**: documented

### App_Server_Admin_Requirements_Read
- **surface**: `configRequirements/read`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:31466` — the method returns effective requirements from `requirements.toml` and/or MDM, or `null` when none are configured.
- **does**: Reads administrator-enforced approval, sandbox, feature, and network constraints.
- **spark**: S=0 P=8 A=3 R=2 K=7
- **why**: P from exposing non-user-overridable authority bounds; A from informing compliant client setup; R from describing allowed runtime reach; K from returning effective managed policy
- **rent**: none — this is a policy read
- **composes**: [[App_Server_Sandboxed_Command_Execution]], [[Scheduled_Task_Unattended_Permission_Model]]
- **confidence**: documented

### TypeScript_Codex_SDK_Thread_Lifecycle
- **surface**: `new Codex().startThread()`, `thread.run()`, `resumeThread(id)`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32752` — the server-side Node.js library starts, continues, and resumes local Codex threads.
- **does**: Controls persistent local Codex threads from a TypeScript application.
- **spark**: S=6 P=0 A=8 R=8 K=2
- **why**: S from embedding coding-agent work; A from sequencing and resuming tasks; R from exposing Codex to Node applications; K from retaining thread context
- **rent**: once_at_install — the user installs `@openai/codex-sdk`; each run separately consumes Codex usage
- **composes**: [[App_Server_Thread_Start]], [[App_Server_Thread_Resume]]
- **confidence**: documented

### Python_Codex_SDK_App_Server_Client
- **surface**: `pip install openai-codex`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32801` — the Python SDK controls local app-server over JSON-RPC and published builds include a pinned Codex CLI runtime dependency.
- **does**: Provides a Python client with a version-pinned Codex runtime.
- **spark**: S=5 P=0 A=5 R=8 K=1
- **why**: S from enabling Python-hosted Codex tasks; A from wrapping thread lifecycle; R from bundling client access and a runtime dependency; K from pinning protocol/runtime compatibility
- **rent**: once_at_install — the user installs the SDK and bundled runtime
- **composes**: [[App_Server_JSON_RPC_Message_Model]], [[App_Server_Version_Matched_Schema_Generation]]
- **confidence**: documented

### Python_Codex_SDK_Sandbox_Presets
- **surface**: `Sandbox.{read_only|workspace_write|full_access}`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32851` — presets apply at thread creation or a later turn and then remain defaults for later turns.
- **does**: Selects filesystem authority for Python SDK turns.
- **spark**: S=0 P=9 A=3 R=3 K=0
- **why**: P from defining write authority; A from persisting a turn-level policy as a thread default; R from bounding filesystem reach
- **rent**: every_turn — the selected policy is applied to later turns
- **composes**: [[Python_Codex_SDK_App_Server_Client]], [[App_Server_Turn_Start]]
- **confidence**: documented

### Codex_GitHub_Action_Run
- **surface**: `uses: openai/codex-action@v1`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32610` — the action installs Codex CLI, starts a Responses API proxy when given an API key, and runs `codex exec` with specified permissions.
- **does**: Runs a Codex task inside a GitHub Actions job.
- **spark**: S=7 P=4 A=9 R=8 K=0
- **why**: S from automating code review or patch work; P from applying workflow permissions; A from inserting Codex into CI/CD; R from provisioning CLI and API proxy access
- **rent**: every_matching_call — each workflow invocation consumes runner and Codex service usage
- **composes**: [[Codex_Exec_Noninteractive_Run]], [[GitHub_Action_Privilege_Strategy]], [[GitHub_Action_Final_Message_Output]]
- **confidence**: documented

### GitHub_Action_Privilege_Strategy
- **surface**: `safety-strategy`, `unprivileged-user`, `sandbox`, `read-only`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32701` — default `drop-sudo` irreversibly removes sudo for the job; Windows requires `unsafe`; sandbox separately limits Codex filesystem and network access.
- **does**: Configures the operating-system and Codex-level privilege boundary for an action run.
- **spark**: S=0 P=10 A=4 R=4 K=0
- **why**: P from deciding the action’s effective authority; A from layering runner and agent isolation; R from constraining filesystem, network, and privilege reach
- **rent**: every_matching_call — the chosen boundary applies to each action run
- **composes**: [[Codex_GitHub_Action_Run]], [[GitHub_Action_Trigger_Allowlist]]
- **confidence**: documented

### GitHub_Action_Trigger_Allowlist
- **surface**: `allow-users` and `allow-bots`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32703` — trigger inputs default to users with write access and can explicitly add trusted users or bots.
- **does**: Restricts which GitHub identities may trigger a Codex workflow.
- **spark**: S=0 P=10 A=3 R=1 K=0
- **why**: P from assigning invocation authority; A from gating workflow entry; R from conditionally opening CI execution
- **rent**: none — blocked identities create no Codex run
- **composes**: [[Codex_GitHub_Action_Run]], [[GitHub_Action_Privilege_Strategy]]
- **confidence**: documented

### GitHub_Action_Final_Message_Output
- **surface**: `steps.<id>.outputs.final-message` and `output-file`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32711` — the action emits the last Codex message as `final-message`; `output-file` can persist output for artifacts.
- **does**: Exposes the final agent response to later workflow steps or files.
- **spark**: S=3 P=0 A=7 R=5 K=3
- **why**: S from making agent output reusable; A from connecting pipeline stages; R from exposing a job output and file artifact; K from carrying the agent’s result
- **rent**: none — consuming the completed output adds no agent call
- **composes**: [[Codex_GitHub_Action_Run]], [[Exec_Output_Schema]]
- **confidence**: documented

### Codex_Exec_Noninteractive_Run
- **surface**: `codex exec "<prompt>"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32877` — non-interactive mode runs Codex in scripts and CI without opening the TUI.
- **does**: Invokes one unattended Codex task from a process pipeline.
- **spark**: S=7 P=1 A=8 R=7 K=0
- **why**: S from performing coding-agent work; P from using preset rather than interactive authority; A from fitting scripts and pipelines; R from exposing Codex as a command process
- **rent**: every_matching_call — each invocation consumes host and Codex service usage
- **composes**: [[Exec_JSONL_Event_Stream]], [[Exec_Output_Schema]], [[Exec_Session_Resume]]
- **confidence**: documented

### Exec_Output_Channel_Separation
- **surface**: `codex exec` stdout/stderr contract
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32903` — progress streams to stderr while only the final agent message is printed to stdout.
- **does**: Separates human-readable execution progress from pipeable final output.
- **spark**: S=2 P=0 A=6 R=3 K=1
- **why**: S from supporting downstream shell consumption; A from separating pipeline data and diagnostics; R from exposing two process channels; K from isolating the final result
- **rent**: none — channel routing adds no agent work
- **composes**: [[Codex_Exec_Noninteractive_Run]], [[GitHub_Action_Final_Message_Output]]
- **confidence**: documented

### Exec_JSONL_Event_Output
- **surface**: `codex exec --json`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32942` — stdout becomes JSONL containing thread, turn, item, and error events.
- **does**: Emits machine-readable execution lifecycle events as newline-delimited JSON.
- **spark**: S=4 P=0 A=7 R=5 K=7
- **why**: S from enabling programmatic consumers; A from exposing ordered lifecycle progression; R from providing a structured stream; K from carrying commands, edits, messages, tools, plans, errors, and usage
- **rent**: every_turn — event serialization recurs throughout the run
- **composes**: [[Codex_Exec_Noninteractive_Run]], [[App_Server_Item_Event_Stream]]
- **confidence**: documented

### Exec_Output_Schema
- **surface**: `codex exec --output-schema ./schema.json`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32966` — the flag requests a final response conforming to a supplied JSON Schema.
- **does**: Constrains noninteractive final output to a machine-defined JSON shape.
- **spark**: S=8 P=0 A=5 R=1 K=2
- **why**: S from producing stable structured results; A from enforcing a downstream automation contract; R from exposing schema-conditioned output; K from defining required result fields
- **rent**: every_matching_call — schema enforcement is charged with the Codex run
- **composes**: [[Codex_Exec_Noninteractive_Run]], [[GitHub_Action_Final_Message_Output]], [[App_Server_Turn_Structured_Output]]
- **confidence**: documented

### Exec_Session_Resume
- **surface**: `codex exec resume {--last|SESSION_ID}`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33053` — noninteractive execution can continue the last or a specifically addressed prior session.
- **does**: Continues a previous noninteractive Codex session in a later process stage.
- **spark**: S=2 P=0 A=8 R=4 K=6
- **why**: S from continuing agent work; A from enabling multi-stage pipelines; R from addressing stored sessions; K from restoring prior conversation context
- **rent**: every_matching_call — each resumed run consumes Codex service usage
- **composes**: [[Codex_Exec_Noninteractive_Run]], [[App_Server_Thread_Resume]]
- **confidence**: documented

### Scheduled_Task_Background_Run
- **surface**: `Scheduled` task with prompt and cadence
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33268` — scheduled tasks run recurring work in the background; desktop tasks can work with local projects.
- **does**: Replays a saved agent task on a recurring background cadence.
- **spark**: S=5 P=2 A=10 R=6 K=1
- **why**: S from performing repeated work; P from running unattended; A from time-driven execution; R from reaching a selected project; K from reusing the saved prompt
- **rent**: every_spawn — each scheduled run consumes local resources and Codex usage
- **composes**: [[Scheduled_Task_Project_Execution_Mode]], [[Scheduled_Task_Unattended_Permission_Model]]
- **confidence**: documented

### Standalone_Scheduled_Task_Run
- **surface**: `Standalone scheduled task`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33377` — standalone tasks start a new chat for each run and can run across one or more projects.
- **does**: Starts each scheduled occurrence as an independent chat.
- **spark**: S=1 P=0 A=9 R=4 K=0
- **why**: S from running a fresh agent instance; A from isolating run histories; R from targeting multiple projects
- **rent**: every_spawn — every occurrence creates a new run and consumes Codex usage
- **composes**: [[Scheduled_Task_Background_Run]], [[Scheduled_Task_Chat_Continuation]]
- **confidence**: documented

### Existing_Chat_Scheduled_Task
- **surface**: `Schedule a task inside a chat`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33418` — an in-chat schedule returns to that chat and uses its existing context.
- **does**: Re-enters an existing conversation on a schedule.
- **spark**: S=1 P=3 A=9 R=3 K=8
- **why**: S from continuing ongoing work; P from returning to the user’s existing conversation; A from timed continuation; R from reaching the thread; K from retaining accumulated chat context
- **rent**: every_spawn — each wake adds a turn to the persistent chat
- **composes**: [[Scheduled_Task_Background_Run]], [[Scheduled_Task_Standalone_Run]]
- **confidence**: documented

### Scheduled_Task_Event_Trigger
- **surface**: `Gmail`, `Slack`, or `GitHub` event trigger
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33312` — eligible web/mobile tasks can run on supported incoming mail, channel-message, or pull-request events; this is unavailable in desktop, CLI, and IDE.
- **does**: Starts a saved scheduled task when a supported connected-app event matches.
- **spark**: S=3 P=4 A=10 R=7 K=2
- **why**: S from reacting to external work events; P from requiring connected-app authorization; A from event-driven invocation; R from reaching Gmail, Slack, or GitHub signals; K from exposing matched event content
- **rent**: every_spawn — each matched or coalesced event run consumes service usage
- **composes**: [[Scheduled_Task_Background_Run]], [[App_Connector_Authorization]]
- **confidence**: documented

### Scheduled_Task_Project_Execution_Mode
- **surface**: `local project` or `new worktree`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33350` — Git projects can run locally or in a background worktree; non-version-controlled projects run directly in the directory.
- **does**: Selects whether a local scheduled run shares the checkout or uses an isolated Git worktree.
- **spark**: S=0 P=3 A=9 R=7 K=0
- **why**: P from choosing whether unattended work may touch active files; A from selecting shared or isolated execution; R from allocating a checkout or worktree
- **rent**: every_spawn — each worktree-mode run can allocate persistent disk state
- **composes**: [[Scheduled_Task_Background_Run]], [[Git_Worktree_Isolation]]
- **confidence**: documented

### Scheduled_Task_Unattended_Permission_Model
- **surface**: scheduled task sandbox plus `approval_policy = "never"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33466` — scheduled tasks run unattended with default sandbox settings and use `never` only when organization policy allows it, otherwise falling back to the selected permission mode.
- **does**: Applies sandbox and managed-policy constraints to unattended task execution.
- **spark**: S=0 P=10 A=8 R=4 K=0
- **why**: P from determining unattended action authority; A from removing interactive approval while honoring fallback policy; R from bounding file, network, and app access
- **rent**: every_spawn — the authority profile is evaluated for every scheduled run
- **composes**: [[Scheduled_Task_Background_Run]], [[App_Server_Admin_Requirements_Read]]
- **confidence**: documented

### Codex_MCP_Server_Deprecation
- **surface**: `codex mcp-server`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33499` — “`codex mcp-server` is deprecated. Use the Codex app server instead.”
- **does**: Retains a deprecated MCP compatibility surface for existing integrations.
- **spark**: S=1 P=0 A=2 R=4 K=1
- **why**: S from preserving legacy orchestration; A from signaling migration toward app-server; R from exposing Codex as MCP tools; K from documenting compatibility status
- **rent**: none — deprecation itself adds no recurring charge
- **composes**: [[App_Server_Deep_Client_Interface]], [[Codex_MCP_Conversation_Tools]]
- **confidence**: documented

### Codex_MCP_Conversation_Tools
- **surface**: MCP tools `codex` and `codex-reply`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33523` — `codex` starts a configured session; `codex-reply` continues it using `threadId` and a new prompt.
- **does**: Starts or continues a Codex conversation through legacy MCP tool calls.
- **spark**: S=6 P=4 A=8 R=8 K=4
- **why**: S from invoking coding-agent work; P from passing approval and sandbox overrides; A from maintaining a multi-call conversation; R from exposing Codex to MCP clients; K from carrying thread context
- **rent**: every_matching_call — each MCP call can consume Codex usage
- **composes**: [[Codex_MCP_Server_Deprecation]], [[Agents_SDK_MCP_Stdio_Integration]]
- **confidence**: documented

### Agents_SDK_MCP_Stdio_Integration
- **surface**: `MCPServerStdio(command="codex", args=["mcp-server"])`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33604` — Agents SDK launches Codex CLI as an MCP server and keeps it alive across multiple agent turns.
- **does**: Mounts a long-lived Codex process as an Agents SDK tool server.
- **spark**: S=6 P=0 A=9 R=8 K=2
- **why**: S from giving Agents SDK agents coding capabilities; A from coordinating repeated calls through one process; R from exposing Codex tools over stdio; K from preserving conversation continuity
- **rent**: every_turn — the long-lived server services repeated agent turns
- **composes**: [[Codex_MCP_Conversation_Tools]], [[Agents_SDK_Handoff_Orchestration]]
- **confidence**: documented

### Agents_SDK_Handoff_Orchestration
- **surface**: `Agent(..., handoffs=[...])` with `Runner.run(...)`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33705` — the documented workflow assigns scoped agents, gates transitions on artifacts, and coordinates handoffs through a project-manager agent.
- **does**: Orchestrates specialized Agents SDK roles around Codex-backed work.
- **spark**: S=5 P=2 A=10 R=6 K=3
- **why**: S from combining role-specific capabilities; P from defining inter-agent transfer behavior; A from explicit delegation and artifact gates; R from sharing the Codex MCP server; K from passing workflow artifacts between roles
- **rent**: every_spawn — each delegated agent run consumes model and Codex usage
- **composes**: [[Agents_SDK_MCP_Stdio_Integration]], [[Agents_SDK_Execution_Traces]]
- **confidence**: documented

### Agents_SDK_Execution_Traces
- **surface**: OpenAI `Traces dashboard`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:33901` — Codex records prompts, tool calls, handoffs, files, and durations for Agents SDK workflow inspection.
- **does**: Records an inspectable execution timeline for an orchestrated Codex workflow.
- **spark**: S=1 P=1 A=6 R=5 K=8
- **why**: S from enabling workflow debugging; P from exposing handoff behavior; A from reconstructing orchestration; R from providing a trace asset; K from retaining prompts, calls, artifacts, and timing
- **rent**: every_matching_call — each traced workflow produces service-side trace data
- **composes**: [[Agents_SDK_Handoff_Orchestration]], [[Agents_SDK_MCP_Stdio_Integration]]
- **confidence**: documented

## Uncovered
- The app-server endpoint catalog was bounded to core protocol, thread/turn lifecycle, execution, events, approvals, and managed policy; auth/account operations, filesystem watchers, skills/plugins/apps RPCs, external-agent import, feedback, rate-limit reset, and experimental process/background-terminal APIs were read but not emitted individually.
- GitHub Action workflow execution, SDK packages, `codex exec`, scheduled tasks, and Agents SDK examples were not exercised because this arm was explicitly documentary and authorized no services, tasks, actions, installations, or agent workflows.
- Scheduled-task plan entitlement, workspace rollout, and live Windows behavior were not verified; the fresh manual documents availability as plan- and policy-dependent and does not bind every statement to Codex Desktop `26.820.9563.0` or CLI `0.150.0-alpha.8`.
- Ordinary CLI/TUI flags, app/IDE/cloud integration UX, and multi-agent desktop UX were excluded by the D1, D5, and D3 scope boundaries.
