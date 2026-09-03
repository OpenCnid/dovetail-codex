# D5 MCP, Connectors, IDE, App, Cloud, and CI Docs

Target pin: Codex Desktop `26.820.9563.0`; codex-cli `0.150.0-alpha.8`; Windows NT `10.0.26200.0`; documentary date `2026-09-02`.

Primary evidence: fresh official OpenAI manual cached at `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md` on `2026-09-02`. All rows are documentary; no connection, authentication, task, or integration was exercised.

### MCP_Host_Configuration_Sharing
- **surface**: `~/.codex/config.toml` / `.codex/config.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25319-25323` — “desktop app, Codex CLI, and IDE extension ... share MCP configuration”
- **does**: Shares one host's MCP configuration across the desktop app, CLI, or IDE extension.
- **spark**: S=1 P=0 A=4 R=6 K=0
- **why**: S via consistent integration access; A via cross-client continuity; R via a common server inventory
- **rent**: none — the sharing layer itself adds no per-call charge
- **composes**: [[MCP_Stdio_Server_Transport]], [[MCP_Streamable_HTTP_Server_Transport]], [[IDE_Settings_Layer_Separation]]
- **confidence**: documented

### MCP_STDIO_Transport_Config
- **surface**: `[mcp_servers.<name>] command = "..."`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25415-25421` — “`command` (required): The command that starts the server.”
- **does**: Launches an MCP server as a local process over stdio.
- **spark**: S=2 P=0 A=1 R=8 K=0
- **why**: S via callable local integrations; A via process placement; R via a new tool endpoint
- **rent**: every_turn — the host starts or maintains the configured server for eligible sessions
- **composes**: [[MCP_Host_Configuration_Sharing]], [[MCP_Remote_Stdio_Placement]]
- **confidence**: documented

### MCP_Streamable_HTTP_Server_Transport
- **surface**: `[mcp_servers.<name>] url = "https://..."`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25435-25444` — “`url` (required): The server address.”
- **does**: Connects Codex to an addressable MCP server over streamable HTTP.
- **spark**: S=2 P=0 A=1 R=9 K=0
- **why**: S via remote integration calls; A via network placement; R via a remote endpoint
- **rent**: every_matching_call — network work occurs when the connection or its capabilities are used
- **composes**: [[MCP_HTTP_Authentication_Chain]], [[MCP_Host_Configuration_Sharing]]
- **confidence**: documented

### MCP_Tool_Exposure
- **surface**: MCP server `tools`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22824-22830` — “Tools (actions)”
- **does**: Exposes structured external actions for Codex to call.
- **spark**: S=6 P=0 A=0 R=9 K=0
- **why**: S via new executable actions; R via externally supplied tools
- **rent**: every_matching_call — each selected tool can incur server work
- **composes**: [[MCP_Tool_Exposure_Policy]], [[MCP_Tool_Approval_Policy]]
- **confidence**: documented

### MCP_Resource_Exposure
- **surface**: MCP server `resources`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:22824-22830` — “Resources (readable data)”
- **does**: Exposes external readable data as MCP resources.
- **spark**: S=1 P=0 A=0 R=8 K=7
- **why**: S via resource retrieval; R via reachable external data; K via supplied context
- **rent**: every_matching_call — resource reads consume server or network work
- **composes**: [[MCP_Streamable_HTTP_Server_Transport]], [[MCP_Stdio_Server_Transport]]
- **confidence**: documented

### MCP_Server_Initialization_Instructions
- **surface**: MCP initialize response `instructions`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25337-25339` — “uses it as server-wide guidance alongside the server's tools”
- **does**: Injects server-wide operating guidance for the MCP tool set.
- **spark**: S=2 P=1 A=6 R=0 K=3
- **why**: S via tool-use constraints; P via server-authored direction; A via cross-tool workflow guidance; K via rate-limit or workflow context
- **rent**: every_turn — guidance occupies decision context while the server is active
- **composes**: [[MCP_Tool_Exposure]]
- **confidence**: documented

### MCP_HTTP_Authentication_Chain
- **surface**: `bearer_token_env_var`, `http_headers`, `env_http_headers`, `auth = "oauth" | "chatgpt"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25437-25448` — “Authentication to try after configured bearer tokens and authorization headers.”
- **does**: Resolves credentials for an HTTP MCP server through configured authentication sources.
- **spark**: S=0 P=8 A=2 R=5 K=0
- **why**: P via identity-bound authority; A via ordered credential fallback; R via authenticated endpoint access
- **rent**: every_matching_call — credentials accompany matching connection attempts
- **composes**: [[MCP_Streamable_HTTP_Server_Transport]], [[Connector_Service_Authentication]]
- **confidence**: documented

### MCP_Remote_Stdio_Placement
- **surface**: `mcp_servers.<name>.experimental_environment = "remote"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11502-11503` — “`remote` starts stdio servers through a remote executor environment”
- **does**: Starts a stdio MCP server through an available remote executor.
- **spark**: S=1 P=0 A=7 R=8 K=0
- **why**: S via remote-hosted local-process tools; A via explicit placement; R via remote compute
- **rent**: every_turn — the remote server lifecycle is attached to eligible sessions
- **composes**: [[MCP_Stdio_Server_Transport]], [[Remote_Host_Capability_Inheritance]]
- **confidence**: documented

### MCP_Tool_Filter_Policy
- **surface**: `mcp_servers.<name>.enabled_tools` / `disabled_tools`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25454-25457` — “Tool deny list (applied after `enabled_tools`).”
- **does**: Filters the MCP tools exposed from a configured server.
- **spark**: S=0 P=8 A=2 R=4 K=0
- **why**: P via callable-tool authority; A via ordered allow-then-deny evaluation; R via bounded tool reach
- **rent**: every_turn — filtered tool schemas shape each eligible session
- **composes**: [[MCP_Tool_Exposure]], [[MCP_Tool_Approval_Policy]]
- **confidence**: documented

### MCP_Tool_Approval_Policy
- **surface**: `default_tools_approval_mode` / `tools.<tool>.approval_mode`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:25458-25461` — “Per-tool approval behavior override.”
- **does**: Selects approval behavior for MCP tool calls at server or tool scope.
- **spark**: S=0 P=10 A=3 R=1 K=0
- **why**: P via user-interruption authority; A via layered policy resolution; R via gated tool use
- **rent**: every_matching_call — matching calls can pause for review
- **composes**: [[MCP_Tool_Exposure_Policy]], [[MCP_Elicitation_Prompt_Gate]]
- **confidence**: documented

### MCP_Elicitation_Prompt_Gate
- **surface**: `approval_policy.granular.mcp_elicitations`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11397-11398` — “MCP elicitation prompts are allowed to surface instead of being auto-rejected.”
- **does**: Allows or suppresses user-facing MCP elicitation prompts.
- **spark**: S=0 P=10 A=4 R=1 K=0
- **why**: P via control of who may answer; A via prompt gating; R via gated continuation
- **rent**: every_matching_call — only eliciting calls create a user-interaction cost
- **composes**: [[MCP_Tool_Approval_Policy]]
- **confidence**: documented

### Connector_MCP_Backend
- **surface**: installed connector tool
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:29984-29990` — “They're also the services behind connectors.”
- **does**: Backs connector tools with MCP services that perform external actions.
- **spark**: S=5 P=0 A=1 R=9 K=4
- **why**: S via service-specific actions; A via structured integration; R via external systems; K via returned structured data
- **rent**: every_matching_call — the connector service handles each matching invocation
- **composes**: [[MCP_Tool_Exposure]], [[Connector_Service_Authentication]]
- **confidence**: documented

### Connector_Service_Authentication
- **surface**: connector sign-in prompt
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:30133-30141` — “Connectors still require their own sign-in and access.”
- **does**: Uses the external service's authentication boundary for connector access.
- **spark**: S=0 P=9 A=1 R=6 K=0
- **why**: P via service-owned identity authority; A via separate access control; R via authenticated service reach
- **rent**: every_matching_call — connector requests use the service connection
- **composes**: [[Connector_MCP_Backend]], [[App_Tool_Governance]]
- **confidence**: documented

### App_Tool_Governance
- **surface**: `apps._default.*`, `apps.<id>.*`, `apps.<id>.tools.<tool>.*`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11404-11416` — “Per-tool enabled override for an app tool”
- **does**: Governs connector tool availability through default, app, or per-tool policy layers.
- **spark**: S=0 P=10 A=4 R=4 K=0
- **why**: P via approval or risk authority; A via layered overrides; R via bounded connector reach
- **rent**: every_matching_call — matching app calls evaluate the effective policy
- **composes**: [[Connector_MCP_Backend]], [[Connector_Service_Authentication]]
- **confidence**: documented

### IDE_Automatic_Open_File_Context
- **surface**: open files in Codex IDE extension
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:3281-3285` — “The IDE extension automatically includes your open files as context.”
- **does**: Supplies currently open editor files to the agent as prompt context.
- **spark**: S=1 P=0 A=3 R=5 K=5
- **why**: S via context-aware edits; A via automatic context assembly; R via editor state; K via source context
- **rent**: every_turn — attached editor context consumes the turn's context budget
- **composes**: [[IDE_Settings_Layer_Separation]]
- **confidence**: documented

### IDE_Settings_Layer_Separation
- **surface**: `config.toml` versus editor `chatgpt.*` settings
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16665-16672` — “The Codex IDE extension has two settings layers”
- **does**: Separates shared agent configuration from editor-specific extension behavior.
- **spark**: S=0 P=1 A=7 R=3 K=0
- **why**: P via shared permission defaults; A via two configuration planes; R via editor controls
- **rent**: none — configuration separation adds no per-turn work by itself
- **composes**: [[MCP_Host_Configuration_Sharing]], [[IDE_Run_Location_Commands]]
- **confidence**: documented

### IDE_Run_Location_Commands
- **surface**: `/local`, `/worktree`, `/cloud`, `/cloud-environment`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16726-16741` — “Run the chat in the cloud”
- **does**: Selects the execution location for a Codex IDE chat.
- **spark**: S=1 P=1 A=9 R=8 K=0
- **why**: S via location-specific execution; P via user placement choice; A via mode switching; R via local or hosted compute
- **rent**: every_matching_call — the chosen runtime bears each task's compute cost
- **composes**: [[Cloud_Container_Repository_Checkout]], [[Desktop_Worktree_Setup_Script]]
- **confidence**: documented

### Desktop_Worktree_Setup_Script
- **surface**: local environment setup script
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17239-17252` — “Setup scripts run automatically when Codex creates a new worktree”
- **does**: Initializes a newly created desktop worktree with project setup commands.
- **spark**: S=4 P=0 A=7 R=6 K=0
- **why**: S via reproducible environment setup; A via automatic sequencing; R via local command execution
- **rent**: every_matching_call — each new worktree pays the setup runtime
- **composes**: [[IDE_Run_Location_Commands]], [[Desktop_Git_Controls]]
- **confidence**: documented

### Desktop_Project_Action
- **surface**: local environment `Actions`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17254-17258` — “define common tasks like starting your app's development server”
- **does**: Runs a configured project command from the desktop app top bar.
- **spark**: S=5 P=0 A=4 R=6 K=0
- **why**: S via reusable project operations; A via a named shortcut; R via the integrated terminal
- **rent**: every_matching_call — each action consumes local command runtime
- **composes**: [[Desktop_Worktree_Setup_Script]], [[Built_In_Browser_Isolated_Profile]]
- **confidence**: documented

### Desktop_Git_Controls
- **surface**: desktop diff pane Git controls
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17270-17276` — “stage or revert individual chunks ... commit changes, push a branch”
- **does**: Exposes common Git operations beside local projects or worktrees.
- **spark**: S=6 P=3 A=4 R=7 K=0
- **why**: S via Git mutation operations; P via user review of diffs; A via in-app workflow; R via repository state
- **rent**: every_matching_call — only invoked Git operations consume work
- **composes**: [[Desktop_Worktree_Setup_Script]], [[GitHub_PR_Comment_Review]]
- **confidence**: documented

### Built_In_Browser_Isolated_Profile
- **surface**: `@Browser`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15464-15471` — “uses a browser profile that is separate from your regular browser”
- **does**: Gives the desktop agent an isolated browser profile for shared page interaction.
- **spark**: S=6 P=1 A=3 R=9 K=2
- **why**: S via page interaction; P via user-visible shared view; A via profile isolation; R via browser state; K via rendered page context
- **rent**: every_matching_call — browsing consumes tool execution or network work
- **composes**: [[Browser_Website_Permission_Gate]], [[Browser_Extension_Existing_Session_Control]]
- **confidence**: documented

### Browser_Extension_Existing_Session_Control
- **surface**: `@Chrome`, `@Edge`, `@Brave Browser`, `@Opera`, `@Vivaldi`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15714-15721` — “read or act on sites where you're already signed in”
- **does**: Operates supported regular-browser tabs through the ChatGPT browser extension.
- **spark**: S=7 P=2 A=2 R=10 K=3
- **why**: S via signed-in web actions; P via user-selected browser mentions; A via extension mediation; R via existing tabs or sessions; K via page context
- **rent**: every_matching_call — each browser operation consumes extension execution
- **composes**: [[Browser_Website_Permission_Gate]], [[Computer_Use_GUI_Control]]
- **confidence**: documented

### Browser_Website_Permission_Gate
- **surface**: `Allow once` / `Allow for this site` / `Allow for all sites` / `Decline`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15802-15813` — “ChatGPT asks before it interacts with each new website.”
- **does**: Gates browser interaction by website host through user decisions.
- **spark**: S=0 P=10 A=3 R=3 K=0
- **why**: P via user-granted site authority; A via host-scoped policy; R via gated browsing
- **rent**: every_matching_call — a new or unapproved site can interrupt the task
- **composes**: [[Built_In_Browser_Isolated_Profile]], [[Browser_Extension_Existing_Session_Control]]
- **confidence**: documented

### Computer_Use_GUI_Control
- **surface**: `@Computer` / `@AppName`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16984-16993` — “see and operate graphical user interfaces on macOS or Windows”
- **does**: Operates an allowed desktop graphical interface through visual interaction.
- **spark**: S=9 P=2 A=3 R=10 K=2
- **why**: S via GUI manipulation; P via explicit target selection; A via visual execution; R via desktop apps; K via screen state
- **rent**: every_matching_call — visual steps consume screenshots or control actions
- **composes**: [[Computer_Use_App_Approval]], [[Windows_Computer_Use_Foreground]]
- **confidence**: documented

### Computer_Use_App_Approval
- **surface**: `Settings > Computer Use > Always allow`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17072-17084` — “asks for your permission before it can use an app”
- **does**: Grants per-app authority for Computer Use sessions.
- **spark**: S=0 P=10 A=3 R=3 K=0
- **why**: P via user-held app authority; A via reusable approval state; R via gated GUI reach
- **rent**: every_matching_call — unapproved apps prompt during matching tasks
- **composes**: [[Computer_Use_GUI_Control]]
- **confidence**: documented

### Windows_Computer_Use_Foreground
- **surface**: Computer Use on Windows
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17041-17050` — “runs on the active desktop ... take over the foreground”
- **does**: Runs Windows Computer Use in the active foreground desktop session.
- **spark**: S=1 P=7 A=5 R=4 K=0
- **why**: S via visible UI execution; P via interruption of the user's desktop; A via foreground-only scheduling; R via the active session
- **rent**: every_matching_call — the user yields foreground control while it runs
- **composes**: [[Computer_Use_GUI_Control]], [[Device_Remote_Control]]
- **confidence**: documented

### Cloud_Container_Repository_Checkout
- **surface**: cloud chat environment selection
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16367-16375` — “creates a container and checks out your repo”
- **does**: Runs a cloud chat against a selected repository revision in a fresh container.
- **spark**: S=5 P=0 A=8 R=9 K=2
- **why**: S via isolated coding execution; A via reproducible task staging; R via hosted compute; K via repository context
- **rent**: every_matching_call — each cloud task consumes container compute
- **composes**: [[Cloud_Setup_Script]], [[Cloud_Agent_Internet_Access]]
- **confidence**: documented

### Cloud_Setup_Script
- **surface**: cloud environment setup script
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16371-16374` — “runs your setup script”
- **does**: Prepares the cloud container before the agent phase.
- **spark**: S=4 P=0 A=8 R=7 K=0
- **why**: S via dependency installation; A via pre-agent sequencing; R via setup compute
- **rent**: every_matching_call — an uncached environment pays setup runtime
- **composes**: [[Cloud_Container_Repository_Checkout]], [[Cloud_Setup_Only_Secrets]]
- **confidence**: documented

### Cloud_Setup_Only_Secrets
- **surface**: cloud environment `Secrets`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16389-16397` — “only available to setup scripts ... removed before the agent phase”
- **does**: Restricts configured cloud secrets to pre-agent setup execution.
- **spark**: S=0 P=9 A=6 R=3 K=0
- **why**: P via secret authority boundaries; A via phase-scoped injection; R via setup-only credentials
- **rent**: every_matching_call — secrets are decrypted only for matching setup phases
- **composes**: [[Cloud_Setup_Script]]
- **confidence**: documented

### Agent_Internet_Access_Mode
- **surface**: cloud environment `Internet access` with domain allowlist or HTTP methods
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15345-15364` — “configured on a per-environment basis”
- **does**: Controls agent-phase internet reach per cloud environment.
- **spark**: S=1 P=9 A=5 R=8 K=1
- **why**: S via network-dependent execution; P via administrator or user authorization; A via allowlist or method policy; R via outbound network; K via retrievable internet content
- **rent**: every_matching_call — allowed requests consume network access
- **composes**: [[Cloud_Container_Repository_Checkout]], [[Cloud_Outbound_Proxy]]
- **confidence**: documented

### Cloud_Outbound_Proxy
- **surface**: cloud environment HTTP/HTTPS egress
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16439-16443` — “All outbound internet traffic passes through this proxy.”
- **does**: Routes cloud-environment HTTP or HTTPS egress through a managed proxy.
- **spark**: S=0 P=4 A=6 R=6 K=0
- **why**: P via centrally enforced egress; A via mandatory routing; R via proxied network access
- **rent**: every_matching_call — outbound requests traverse the proxy
- **composes**: [[Cloud_Agent_Internet_Access]]
- **confidence**: documented

### Device_Remote_Control
- **surface**: `Settings > Connections > Control this Mac or PC`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17292-17308` — “access work running on another device or machine”
- **does**: Starts or steers host-resident chats from a paired device.
- **spark**: S=5 P=5 A=6 R=9 K=1
- **why**: S via remote steering; P via remote approvals; A via device handoff; R via host resources; K via remote outputs
- **rent**: every_matching_call — each remote interaction uses the relay or host
- **composes**: [[Remote_Host_Capability_Inheritance]], [[Windows_Computer_Use_Foreground]]
- **confidence**: documented

### Remote_Host_Capability_Inheritance
- **surface**: paired Remote host
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17417-17431` — “MCP servers, skills, browser access, and Computer Use come from that host's configuration.”
- **does**: Uses the connected host's configured projects, tools, credentials, or controls.
- **spark**: S=3 P=3 A=6 R=10 K=2
- **why**: S via host-local capabilities; P via inherited controls; A via host-bound execution; R via host files or tools; K via host context
- **rent**: every_matching_call — the connected host supplies each task's runtime
- **composes**: [[Device_Remote_Control]], [[MCP_Remote_Stdio_Placement]], [[SSH_Remote_Project_Execution]]
- **confidence**: documented

### SSH_Remote_Project_Execution
- **surface**: `Settings > Connections` SSH host project
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17447-17451` — “run chats against the remote filesystem and shell”
- **does**: Executes project chats against an SSH host's filesystem or shell.
- **spark**: S=6 P=2 A=7 R=10 K=2
- **why**: S via remote coding commands; P via SSH identity; A via remote placement; R via host filesystem or shell; K via remote project context
- **rent**: every_matching_call — the SSH host performs matching task work
- **composes**: [[Remote_Host_Capability_Inheritance]], [[Cross_Host_Chat_Handoff]]
- **confidence**: documented

### Cross_Host_Chat_Handoff
- **surface**: chat footer run location > `Hand off`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17484-17509` — “transfers the chat and Git state”
- **does**: Moves an existing chat's Git state to a matching connected host.
- **spark**: S=3 P=2 A=9 R=8 K=3
- **why**: S via continued execution; P via destination confirmation; A via cross-host migration; R via destination compute; K via transferred history
- **rent**: every_matching_call — each handoff performs transfer or worktree setup
- **composes**: [[SSH_Remote_Project_Execution]], [[Desktop_Git_Controls]]
- **confidence**: documented

### GitHub_PR_Comment_Review
- **surface**: `@codex review`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28310-28317` — “Codex posts a review on the pull request”
- **does**: Triggers a Codex cloud review from a GitHub pull-request comment.
- **spark**: S=7 P=2 A=7 R=8 K=3
- **why**: S via code review; P via teammate-style feedback; A via comment-driven delegation; R via GitHub or cloud; K via diff context
- **rent**: every_matching_call — each review consumes a cloud task
- **composes**: [[GitHub_Automatic_PR_Review]], [[GitHub_Comment_Cloud_Task]]
- **confidence**: documented

### GitHub_Automatic_PR_Review
- **surface**: Codex settings `Automatic reviews`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28319-28324` — “post a review whenever someone opens a new PR”
- **does**: Runs Codex review automatically for new eligible GitHub pull requests.
- **spark**: S=7 P=2 A=9 R=8 K=3
- **why**: S via automatic review; P via repository-authorized posting; A via event-triggered execution; R via GitHub or cloud; K via pull-request context
- **rent**: every_matching_call — each matching pull request starts review work
- **composes**: [[GitHub_PR_Comment_Review]]
- **confidence**: documented

### GitHub_Comment_Cloud_Task
- **surface**: GitHub PR comment `@codex <task>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28408-28424` — “starts a cloud chat with the pull request as context”
- **does**: Starts a cloud coding task from a non-review GitHub pull-request mention.
- **spark**: S=8 P=2 A=8 R=9 K=3
- **why**: S via branch-changing coding work; P via repository comment authority; A via event delegation; R via cloud or GitHub; K via pull-request context
- **rent**: every_matching_call — each mention starts cloud work
- **composes**: [[GitHub_PR_Comment_Review]], [[Cloud_Container_Repository_Checkout]]
- **confidence**: documented

### GitLab_MR_Event_Integration
- **surface**: `Enable Codex activity from GitLab` / `@codex review`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28517-28525` — “project webhook ... delivers merge request, comment, and issue events”
- **does**: Delivers GitLab merge-request activity to Codex through a project webhook.
- **spark**: S=6 P=4 A=9 R=8 K=3
- **why**: S via review or coding triggers; P via webhook installation authority; A via event-driven execution; R via GitLab or cloud; K via merge-request context
- **rent**: every_matching_call — each delivered event can trigger Codex work
- **composes**: [[Cloud_Container_Repository_Checkout]], [[GitLab_Service_Account_Connector]]
- **confidence**: documented

### GitLab_Service_Account_Connector
- **surface**: `Codex Cloud > Settings > Connectors > Set up service account`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:28469-28485` — “service account with a personal access token with the `api` scope”
- **does**: Gives Codex a scoped GitLab service identity for configured projects or groups.
- **spark**: S=0 P=10 A=4 R=8 K=0
- **why**: P via workspace-admin identity authority; A via group or project scoping; R via GitLab API access
- **rent**: every_matching_call — GitLab actions use the service identity
- **composes**: [[GitLab_MR_Event_Integration]], [[Connector_Service_Authentication]]
- **confidence**: documented

### Linear_Issue_Delegation
- **surface**: assign issue to Codex / Linear comment `@Codex`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:29688-29716` — “Codex creates a cloud chat and replies with progress and results.”
- **does**: Delegates a Linear issue or comment thread to a Codex cloud chat.
- **spark**: S=7 P=3 A=9 R=8 K=4
- **why**: S via issue-driven coding; P via assignee or mention interaction; A via delegated cloud execution; R via Linear or cloud; K via issue context
- **rent**: every_matching_call — each assignment or mention starts cloud work
- **composes**: [[Cloud_Container_Repository_Checkout]], [[Connector_Service_Authentication]]
- **confidence**: documented

### Linear_Local_MCP_Connection
- **surface**: `codex mcp add linear --url https://mcp.linear.app/mcp`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:29759-29775` — “access Linear issues locally, configure the Linear ... MCP server”
- **does**: Gives local Codex clients authenticated access to Linear issues through MCP.
- **spark**: S=5 P=5 A=2 R=9 K=6
- **why**: S via issue operations; P via Linear sign-in; A via shared local-client setup; R via Linear; K via issue content
- **rent**: every_matching_call — Linear MCP requests consume service work
- **composes**: [[MCP_Streamable_HTTP_Server_Transport]], [[MCP_HTTP_Authentication_Chain]]
- **confidence**: documented

### Slack_Thread_Delegation
- **surface**: Slack mention `@Codex <prompt>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:29789-29811` — “Codex creates a cloud chat and replies with the results.”
- **does**: Delegates Slack channel or thread context to a Codex cloud chat.
- **spark**: S=7 P=4 A=9 R=8 K=4
- **why**: S via coding task execution; P via thread interaction; A via mention-driven delegation; R via Slack or cloud; K via thread history
- **rent**: every_matching_call — each mention starts cloud work
- **composes**: [[Cloud_Container_Repository_Checkout]], [[Connector_Service_Authentication]]
- **confidence**: documented

### Codex_GitHub_Action_Run
- **surface**: `uses: openai/codex-action@v1`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32610-32621` — “runs `codex exec` under the permissions you specify”
- **does**: Runs Codex noninteractively inside a GitHub Actions job.
- **spark**: S=8 P=2 A=10 R=8 K=1
- **why**: S via automated coding or review; P via workflow permissions; A via CI orchestration; R via runner compute; K via checked-out repository context
- **rent**: every_matching_call — each workflow invocation consumes runner or model work
- **composes**: [[GitHub_Action_Safety_Strategy]], [[GitHub_Action_CLI_Version_Pin]]
- **confidence**: documented

### GitHub_Action_Privilege_Strategy
- **surface**: `safety-strategy: drop-sudo | unprivileged-user | unsafe`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32701-32709` — “`drop-sudo` removes `sudo` before running Codex.”
- **does**: Selects the runner privilege-reduction strategy for a Codex action job.
- **spark**: S=0 P=10 A=6 R=3 K=0
- **why**: P via execution authority; A via irreversible job hardening; R via constrained runner access
- **rent**: every_matching_call — the strategy applies to each action job
- **composes**: [[GitHub_Action_Codex_Execution]]
- **confidence**: documented

### GitHub_Action_CLI_Version_Pin
- **surface**: `codex-version`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:32689-32699` — “Pin a specific CLI release.”
- **does**: Pins the Codex CLI release installed by the GitHub Action.
- **spark**: S=0 P=0 A=8 R=3 K=0
- **why**: A via deterministic CI version selection; R via a selected CLI artifact
- **rent**: every_matching_call — each job installs or resolves the pinned release
- **composes**: [[GitHub_Action_Codex_Execution]]
- **confidence**: documented

## Uncovered
- Live MCP server negotiation, resource enumeration, tool calls, OAuth callbacks, elicitation, connector sign-ins, IDE commands, browser control, Computer Use, cloud tasks, remote pairing, SSH execution, GitHub or GitLab events, Linear or Slack triggers, and GitHub Action jobs were not exercised because this arm was documentary-only.
- Plugin packaging and plugin lifecycle were excluded to D4; app-server methods, SDK surfaces, and general noninteractive behavior were excluded to D6; general CLI configuration was excluded to D1.
- The manual documents current surfaces but does not bind each claim to Codex Desktop `26.820.9563.0` or codex-cli `0.150.0-alpha.8`; compatibility with those exact binaries was not runtime-verified.
