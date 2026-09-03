# I7 MCP and Tool Loading

Target: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; config root `C:\Users\Darian\.codex`; surveyed 2026-09-02; probe repository commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`.

### MCP_Server_Registration_Transport_Selector
- **surface**: `codex mcp add <NAME> (--url <URL> | -- <COMMAND>...)`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 `codex mcp add --help` displayed mutually exclusive URL and command forms.
- **does**: Registers one external MCP server over either supported transport.
- **spark**: S=1 P=0 A=2 R=8 K=0
- **why**: S exposes external-server registration; A selects a transport method; R adds a new tool endpoint.
- **rent**: once_at_install — the user pays one configuration action per registration.
- **composes**: [[MCP_STDIO_Transport_Config]], [[MCP_HTTP_Transport_Config]]
- **confidence**: documented

### MCP_STDIO_Server_Environment
- **surface**: `codex mcp add <NAME> --env <KEY=VALUE> -- <COMMAND>...`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 help says `--env` sets environment variables for stdio servers only.
- **does**: Passes configured environment values to a spawned stdio server.
- **spark**: S=0 P=0 A=1 R=6 K=0
- **why**: A parameterizes server startup; R supplies process-local configuration resources.
- **rent**: every_spawn — values are materialized for each server process.
- **composes**: [[MCP_Server_Registration_Transport_Selector]], [[MCP_STDIO_Transport_Config]]
- **confidence**: documented

### MCP_HTTP_Bearer_Token_Source
- **surface**: `--bearer-token-env-var <ENV_VAR>` / `mcp_servers.<name>.bearer_token_env_var`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 help names an environment variable as the bearer-token source for streamable HTTP servers.
- **does**: Sources HTTP bearer authentication from a named environment variable.
- **spark**: S=0 P=4 A=1 R=5 K=0
- **why**: P controls credential-bearing authority; A selects credential indirection; R unlocks authenticated endpoint reach.
- **rent**: every_spawn — Codex resolves the credential when connecting to the server.
- **composes**: [[MCP_HTTP_Transport_Config]], [[MCP_Server_Registration_Transport_Selector]]
- **confidence**: documented

### MCP_OAuth_Client_Registration_Strategy
- **surface**: `--oauth-client-registration <AUTO|CIMD|DCR>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 exposes `auto`, `cimd`, and `dcr` on `mcp add` and `mcp login`.
- **does**: Selects the OAuth client registration algorithm for one login attempt.
- **spark**: S=0 P=5 A=4 R=4 K=0
- **why**: P governs delegated authorization setup; A changes the registration workflow; R enables authenticated MCP reach.
- **rent**: every_matching_call — the choice applies to the invoked registration flow.
- **composes**: [[MCP_HTTP_Bearer_Token_Source]], [[MCP_HTTP_Transport_Config]]
- **confidence**: documented

### MCP_Server_List_CLI
- **surface**: `codex mcp list --json`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 returned one redacted record with keys `name,enabled,disabled_reason,transport,startup_timeout_sec,tool_timeout_sec,auth_status`.
- **does**: Lists configured MCP servers in structured JSON.
- **spark**: S=0 P=0 A=1 R=6 K=1
- **why**: A supports configuration inspection; R exposes the server registry; K reveals normalized registry state.
- **rent**: every_matching_call — the agent pays one local enumeration call.
- **composes**: [[MCP_Server_Get_CLI]], [[Local_STDIO_MCP_Registration]]
- **confidence**: observed

### MCP_Server_Get_CLI
- **surface**: `codex mcp get <NAME> --json`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 returned the redacted `node_repl` record with stdio transport keys and 15 environment-key names.
- **does**: Retrieves one server's normalized configuration in structured JSON.
- **spark**: S=0 P=0 A=1 R=6 K=2
- **why**: A supports targeted inspection; R reaches one registry entry; K reveals normalized server metadata.
- **rent**: every_matching_call — the agent pays one local lookup call.
- **composes**: [[MCP_Server_List_CLI]], [[Local_STDIO_MCP_Registration]]
- **confidence**: observed

### MCP_Server_Config_Table
- **surface**: `[mcp_servers.<server-name>]`
- **evidence**: `C:\Users\Darian\.codex\config.toml:52` — observed `[mcp_servers.node_repl]`; secret-bearing values were not emitted.
- **does**: Stores per-server MCP configuration in a named TOML table.
- **spark**: S=0 P=0 A=3 R=7 K=0
- **why**: A makes server setup declarative; R persists an external tool endpoint.
- **rent**: none — the table itself adds no per-call charge.
- **composes**: [[MCP_STDIO_Transport_Config]], [[MCP_Server_Startup_Policy]]
- **confidence**: observed

### MCP_STDIO_Transport_Config
- **surface**: `command`, `args`, `env`, `env_vars`, `cwd`, `experimental_environment`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 lists these stdio-server fields.
- **does**: Configures a local MCP server process.
- **spark**: S=0 P=0 A=3 R=8 K=0
- **why**: A defines process launch method; R supplies a local tool server.
- **rent**: every_spawn — launching the configured process consumes local runtime resources.
- **composes**: [[MCP_Server_Config_Table]], [[MCP_STDIO_Server_Environment]]
- **confidence**: documented

### MCP_HTTP_Transport_Config
- **surface**: `url`, `auth`, `bearer_token_env_var`, `http_headers`, `env_http_headers`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 lists streamable HTTP endpoint and authentication fields.
- **does**: Configures a streamable HTTP MCP endpoint.
- **spark**: S=0 P=2 A=3 R=8 K=0
- **why**: P selects authentication handling; A defines remote connection method; R supplies a network tool endpoint.
- **rent**: every_matching_call — remote transport work recurs when the endpoint is used.
- **composes**: [[MCP_Server_Config_Table]], [[MCP_HTTP_Bearer_Token_Source]]
- **confidence**: documented

### MCP_Server_Startup_Policy
- **surface**: `mcp_servers.<name>.enabled` / `mcp_servers.<name>.required`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 defines disabling without deletion and fatal startup on failed initialization.
- **does**: Governs whether an enabled server may fail initialization.
- **spark**: S=0 P=1 A=7 R=4 K=0
- **why**: P permits configuration authority over availability; A gates session startup; R controls endpoint presence.
- **rent**: every_spawn — the policy is evaluated during server initialization.
- **composes**: [[MCP_Server_Config_Table]], [[MCP_Server_Timeout_Policy]]
- **confidence**: documented

### MCP_Server_Timeout_Policy
- **surface**: `startup_timeout_sec` / `tool_timeout_sec`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 gives defaults of 10 seconds for startup and 60 seconds for tool execution.
- **does**: Bounds startup or tool execution time.
- **spark**: S=0 P=0 A=6 R=3 K=0
- **why**: A constrains lifecycle waiting; R limits runtime consumption.
- **rent**: every_matching_call — the relevant deadline is enforced on startup or invocation.
- **composes**: [[MCP_Server_Startup_Policy]], [[MCP_Tool_Filter_Policy]]
- **confidence**: documented

### MCP_Tool_Filter_Policy
- **surface**: `enabled_tools` / `disabled_tools`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 states that the deny list is applied after the allow list.
- **does**: Limits the tools exposed from one server.
- **spark**: S=0 P=5 A=5 R=7 K=0
- **why**: P governs available action authority; A applies ordered selection policy; R narrows tool reach.
- **rent**: every_spawn — filtering is applied when the server's tool surface is loaded.
- **composes**: [[MCP_Tool_Approval_Policy]], [[MCP_Tool_Namespace_Projection]]
- **confidence**: documented

### MCP_Tool_Approval_Policy
- **surface**: `default_tools_approval_mode` / `tools.<tool>.approval_mode`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 lists `auto`, `prompt`, `writes`, and `approve`, with per-tool override.
- **does**: Gates MCP tool execution through default or per-tool approval behavior.
- **spark**: S=0 P=9 A=4 R=2 K=0
- **why**: P decides who authorizes execution; A layers per-tool policy over a server default; R conditionally unlocks calls.
- **rent**: every_matching_call — the gate is evaluated for each matching tool invocation.
- **composes**: [[MCP_Tool_Filter_Policy]], [[MCP_Tool_Namespace_Projection]]
- **confidence**: documented

### MCP_Server_Initialization_Instructions
- **surface**: MCP initialization response `instructions`
- **evidence**: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli` — official OpenAI documentation surveyed 2026-09-02 says Codex uses server instructions as server-wide guidance alongside tools.
- **does**: Injects server-wide guidance from the initialization response.
- **spark**: S=1 P=3 A=7 R=1 K=2
- **why**: S can teach server-specific usage; P can encode interaction constraints; A steers cross-tool workflows; R attaches guidance to a server; K supplies server context.
- **rent**: every_turn — server guidance occupies agent context while the surface remains active.
- **composes**: [[MCP_Server_Startup_Policy]], [[MCP_Tool_Namespace_Projection]]
- **confidence**: documented

### Codex_STDIO_MCP_Server
- **surface**: `codex mcp-server`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — codex-cli 0.150.0-alpha.8 help describes this command as `Start Codex as an MCP server (stdio)`.
- **does**: Runs Codex itself as a stdio MCP server.
- **spark**: S=2 P=0 A=4 R=8 K=0
- **why**: S makes Codex invocable by an MCP client; A reverses the usual client role; R exposes Codex as a tool server.
- **rent**: every_spawn — each server process consumes a Codex runtime.
- **composes**: [[MCP_STDIO_Transport_Config]]
- **confidence**: documented

### MCP_Resource_List_Tool
- **surface**: `list_mcp_resources({server?, cursor?})`
- **evidence**: delegated session tool call, Codex Desktop 26.820.9563.0 — an all-server call returned 28 resources, all from `codex_apps`; `server:"node_repl"` returned zero.
- **does**: Enumerates MCP resources across all servers or one named server.
- **spark**: S=0 P=0 A=2 R=8 K=4
- **why**: A supports server-scoped retrieval; R reaches server-provided resources; K reveals available context objects.
- **rent**: every_matching_call — each enumeration queries the MCP resource surface.
- **composes**: [[MCP_Resource_Read_Tool]], [[MCP_Resource_Template_List_Tool]]
- **confidence**: observed

### MCP_Resource_Template_List_Tool
- **surface**: `list_mcp_resource_templates({server?, cursor?})`
- **evidence**: delegated session tool call, Codex Desktop 26.820.9563.0 — the all-server call returned `resourceTemplates: []`.
- **does**: Enumerates parameterized MCP resource templates.
- **spark**: S=0 P=0 A=2 R=7 K=4
- **why**: A supports scoped retrieval; R reaches template surfaces; K reveals parameterized context entry points.
- **rent**: every_matching_call — each enumeration queries the MCP template surface.
- **composes**: [[MCP_Resource_List_Tool]], [[MCP_Resource_Read_Tool]]
- **confidence**: observed

### MCP_Resource_Read_Tool
- **surface**: `read_mcp_resource({server, uri})`
- **evidence**: delegated session tool schema, Codex Desktop 26.820.9563.0 — requires a configured server name and a URI returned by `list_mcp_resources`.
- **does**: Reads one previously listed resource from its named MCP server URI.
- **spark**: S=0 P=0 A=1 R=8 K=7
- **why**: A requires list-before-read addressing; R retrieves the resource; K adds its content to the session.
- **rent**: every_matching_call — each read queries one server resource.
- **composes**: [[MCP_Resource_List_Tool]]
- **confidence**: documented

### Deferred_Tool_Metadata_Catalog
- **surface**: `ALL_TOOLS`
- **evidence**: delegated session `functions.exec` environment, Codex Desktop 26.820.9563.0 — enumerated 140 enabled nested tools, including 125 `mcp__*` entries omitted from the initially declared nested-tool list.
- **does**: Enumerates metadata for enabled deferred nested tools.
- **spark**: S=0 P=0 A=6 R=9 K=3
- **why**: A enables discovery before selection; R exposes otherwise omitted tool surfaces; K supplies tool descriptions.
- **rent**: every_matching_call — catalog inspection is paid only when code queries it.
- **composes**: [[MCP_Tool_Namespace_Projection]], [[Codex_Apps_MCP_Tool_Namespace]]
- **confidence**: observed

### MCP_Tool_Namespace_Projection
- **surface**: `tools.<normalized_tool_name>(args)`
- **evidence**: delegated session `functions.exec` schema, Codex Desktop 26.820.9563.0 — states that nested tools are exposed on `tools`, including deferred entries listed in `ALL_TOOLS`.
- **does**: Exposes deferred tool functions through normalized `tools` members.
- **spark**: S=1 P=0 A=7 R=9 K=0
- **why**: S permits programmatic tool invocation; A supports in-code orchestration; R loads a selected callable surface.
- **rent**: every_matching_call — only invoked members execute their underlying tool.
- **composes**: [[Deferred_Tool_Metadata_Catalog]], [[MCP_Tool_Filter_Policy]]
- **confidence**: documented

### Codex_Apps_MCP_Tool_Namespace
- **surface**: `mcp__codex_apps__*`
- **evidence**: delegated session `ALL_TOOLS`, Codex Desktop 26.820.9563.0 — observed 122 entries grouped as GitHub 89, hotline 1, plugin management 4, safety settings 5, and Sites 23.
- **does**: Groups hosted app connector tools under one MCP namespace.
- **spark**: S=1 P=0 A=3 R=10 K=2
- **why**: S exposes connector-specific operations; A groups selection by provider surface; R reaches hosted app tools; K exposes provider schemas.
- **rent**: every_matching_call — a hosted connector is contacted only when its tool is invoked.
- **composes**: [[Deferred_Tool_Metadata_Catalog]], [[MCP_Tool_Namespace_Projection]]
- **confidence**: observed

### Node_REPL_MCP_Tool_Namespace
- **surface**: `mcp__node_repl__js` / `mcp__node_repl__js_add_node_module_dir` / `mcp__node_repl__js_reset`
- **evidence**: delegated session `ALL_TOOLS`, Codex Desktop 26.820.9563.0 — observed exactly three `mcp__node_repl__` tool schemas.
- **does**: Projects one configured stdio server into a server-qualified tool namespace.
- **spark**: S=3 P=0 A=3 R=8 K=0
- **why**: S adds JavaScript-kernel operations; A preserves server-qualified addressing; R exposes local MCP tools.
- **rent**: every_matching_call — the local MCP process handles each invoked tool.
- **composes**: [[Local_STDIO_MCP_Registration]], [[MCP_Tool_Namespace_Projection]]
- **confidence**: observed

### Local_STDIO_MCP_Registration
- **surface**: `[mcp_servers.node_repl]`
- **evidence**: `C:\Users\Darian\.codex\config.toml:52-72` — observed `command`, `args`, `startup_timeout_sec`, and an `env` subtable; `codex mcp list --json` reported it enabled with stdio transport and startup timeout 120.
- **does**: Registers the local `node_repl.exe` process as an enabled stdio MCP server.
- **spark**: S=1 P=0 A=3 R=8 K=0
- **why**: S enables JavaScript execution tools; A declares process startup; R adds a local tool server.
- **rent**: every_spawn — Codex starts the configured local server process.
- **composes**: [[MCP_Server_Config_Table]], [[Node_REPL_MCP_Tool_Namespace]]
- **confidence**: observed

## Uncovered
- No dedicated `tool_search` entry was present in this delegated session's 140-entry `ALL_TOOLS` catalog; deferred discovery was reached only through `ALL_TOOLS` plus normalized `tools` members.
- MCP resource-template enumeration was reached and empty; no template could be read or parameterized.
- `read_mcp_resource` was not exercised because all 28 listed resources were plugin or skill packaging records, assigned to I5 rather than I7.
- No server was added, removed, authenticated, restarted, disabled, or deliberately failed, so mutation paths, OAuth callbacks, reconnect behavior, required-server failure, and timeout enforcement remain unexercised.
- App-server protocol bindings were not generated because both schema generators require an output directory and this arm was authorized to write only this wave file.
- No project-scoped `.codex/config.toml` existed in the probe root, so trusted-project MCP scoping was not observed locally.
