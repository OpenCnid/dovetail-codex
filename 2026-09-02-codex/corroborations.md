# Cross-arm corroborations

39 capabilities were found independently by more than one arm.
Each is one row in the index; the arms that also found it are listed in
`also_in`. Arms could not see each other, so these are genuine second
sightings rather than a shared prior.

- **Named_Config_Profile** — kept `I6-settings-permissions-hooks.md` (observed), also found by D1-cli-and-config-docs.md. vectors [0, 1, 7, 2, 0] vs [0, 0, 7, 3, 0]; max axis spread 1.
- **Strict_Config_Validation** — kept `I6-settings-permissions-hooks.md` (observed), also found by D1-cli-and-config-docs.md. vectors [0, 0, 6, 1, 0] vs [0, 0, 7, 1, 2]; max axis spread 2.
- **Doctor_Diagnostics_Command** — kept `I2-execution-and-sandbox.md` (observed), also found by D1-cli-and-config-docs.md. vectors [6, 0, 5, 5, 3] vs [1, 0, 4, 5, 7]; max axis spread 5.
- **Approval_Policy** — kept `D2-hooks-and-security-docs.md` (documented), also found by I2-execution-and-sandbox.md, I6-settings-permissions-hooks.md. vectors [0, 10, 5, 1, 0] vs [0, 10, 6, 0, 0] / [0, 10, 3, 0, 0]; max axis spread 2.
- **Granular_Approval_Policy** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [0, 10, 6, 1, 0] vs [0, 10, 5, 0, 0]; max axis spread 1.
- **Permission_Profile_Legacy_Exclusion** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [0, 8, 5, 4, 0] vs [0, 8, 7, 0, 0]; max axis spread 4.
- **Prefix_Command_Rule** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [0, 10, 6, 2, 0] vs [0, 10, 6, 0, 0]; max axis spread 2.
- **Hook_Source_Layering** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [7, 4, 8, 4, 1] vs [2, 4, 8, 5, 0]; max axis spread 5.
- **Hook_Matcher_Filter** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [3, 3, 8, 1, 0] vs [0, 2, 9, 0, 0]; max axis spread 3.
- **Hook_Command_Handler** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [8, 5, 8, 8, 1] vs [4, 4, 7, 7, 0]; max axis spread 4.
- **PreToolUse_Control_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [7, 10, 9, 5, 2] vs [1, 10, 9, 0, 0]; max axis spread 6.
- **PermissionRequest_Decision_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [6, 10, 9, 2, 1] vs [0, 10, 8, 0, 0]; max axis spread 6.
- **PostToolUse_Feedback_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [6, 6, 8, 4, 3] vs [1, 5, 8, 0, 2]; max axis spread 5.
- **UserPromptSubmit_Guard_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [6, 10, 8, 1, 7] vs [0, 10, 8, 0, 0]; max axis spread 7.
- **SessionStart_Context_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [5, 5, 7, 2, 8] vs [1, 3, 6, 1, 8]; max axis spread 4.
- **PreCompact_Gate_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [4, 7, 8, 1, 5] vs [0, 4, 9, 0, 1]; max axis spread 4.
- **PostCompact_Gate_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [4, 5, 8, 1, 6] vs [0, 4, 9, 0, 1]; max axis spread 5.
- **Stop_Continuation_Hook** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [5, 9, 9, 1, 4] vs [1, 7, 10, 0, 0]; max axis spread 4.
- **Managed_Permission_Profile_Allowlist** — kept `D2-hooks-and-security-docs.md` (documented), also found by I6-settings-permissions-hooks.md. vectors [0, 10, 6, 7, 0] vs [0, 10, 3, 0, 0]; max axis spread 7.
- **Multi_Folder_Local_Project** — kept `D3-subagents-and-teams-docs.md` (documented), also found by D7-release-recency.md. vectors [0, 0, 4, 10, 0] vs [1, 0, 5, 7, 0]; max axis spread 3.
- **SSH_Remote_Project_Execution** — kept `D5-mcp-and-integrations-docs.md` (documented), also found by D3-subagents-and-teams-docs.md. vectors [6, 2, 7, 10, 2] vs [3, 2, 4, 10, 0]; max axis spread 3.
- **Cross_Host_Chat_Handoff** — kept `D3-subagents-and-teams-docs.md` (documented), also found by D5-mcp-and-integrations-docs.md. vectors [1, 5, 9, 10, 0] vs [3, 2, 9, 8, 3]; max axis spread 3.
- **AGENTS_Context_Byte_Limit** — kept `I6-settings-permissions-hooks.md` (documented), also found by D4-skills-commands-memory-plugins-docs.md. vectors [0, 0, 3, 5, 4] vs [0, 1, 3, 4, 0]; max axis spread 4.
- **Explicit_Skill_Invocation** — kept `I4-skills-system.md` (observed), also found by D4-skills-commands-memory-plugins-docs.md. vectors [6, 8, 5, 3, 0] vs [8, 6, 3, 2, 2]; max axis spread 2.
- **Local_Skill_Discovery_Scopes** — kept `D4-skills-commands-memory-plugins-docs.md` (documented), also found by I4-skills-system.md. vectors [7, 4, 5, 6, 3] vs [5, 0, 4, 9, 0]; max axis spread 4.
- **Plugin_Package_Manifest** — kept `I5-commands-and-plugins.md` (observed), also found by D4-skills-commands-memory-plugins-docs.md. vectors [0, 0, 1, 6, 4] vs [3, 0, 5, 7, 1]; max axis spread 4.
- **MCP_STDIO_Transport_Config** — kept `D5-mcp-and-integrations-docs.md` (documented), also found by I7-mcp-and-tool-loading.md. vectors [2, 0, 1, 8, 0] vs [0, 0, 3, 8, 0]; max axis spread 2.
- **MCP_Server_Initialization_Instructions** — kept `I7-mcp-and-tool-loading.md` (documented), also found by D5-mcp-and-integrations-docs.md. vectors [1, 3, 7, 1, 2] vs [2, 1, 6, 0, 3]; max axis spread 2.
- **MCP_Tool_Filter_Policy** — kept `I7-mcp-and-tool-loading.md` (documented), also found by D5-mcp-and-integrations-docs.md. vectors [0, 5, 5, 7, 0] vs [0, 8, 2, 4, 0]; max axis spread 3.
- **MCP_Tool_Approval_Policy** — kept `I7-mcp-and-tool-loading.md` (documented), also found by D5-mcp-and-integrations-docs.md. vectors [0, 9, 4, 2, 0] vs [0, 10, 3, 1, 0]; max axis spread 1.
- **Agent_Internet_Access_Mode** — kept `D5-mcp-and-integrations-docs.md` (documented), also found by I9-web-and-browser.md. vectors [1, 9, 5, 8, 1] vs [0, 9, 2, 4, 0]; max axis spread 4.
- **Codex_GitHub_Action_Run** — kept `D5-mcp-and-integrations-docs.md` (documented), also found by D6-agent-sdk-docs.md. vectors [8, 2, 10, 8, 1] vs [7, 4, 9, 8, 0]; max axis spread 2.
- **GitHub_Action_Privilege_Strategy** — kept `D5-mcp-and-integrations-docs.md` (documented), also found by D6-agent-sdk-docs.md. vectors [0, 10, 6, 3, 0] vs [0, 10, 4, 4, 0]; max axis spread 2.
- **Exec_JSONL_Event_Output** — kept `D6-agent-sdk-docs.md` (documented), also found by I2-execution-and-sandbox.md. vectors [4, 0, 7, 5, 7] vs [1, 0, 7, 5, 0]; max axis spread 7.
- **Standalone_Scheduled_Task_Run** — kept `I11-time-and-autonomy.md` (documented), also found by D6-agent-sdk-docs.md. vectors [2, 2, 9, 3, 0] vs [1, 0, 9, 4, 0]; max axis spread 2.
- **Existing_Chat_Scheduled_Task** — kept `D6-agent-sdk-docs.md` (documented), also found by I11-time-and-autonomy.md. vectors [1, 3, 9, 3, 8] vs [2, 5, 9, 2, 5]; max axis spread 3.
- **Delegated_Never_Approval_Policy** — kept `I2-execution-and-sandbox.md` (observed), also found by I10-output-and-interaction.md. vectors [0, 10, 7, 0, 0] vs [0, 10, 6, 1, 0]; max axis spread 1.
- **Exec_Server_Stdin_Close_Lifetime** — kept `I11-time-and-autonomy.md` (documented), also found by I2-execution-and-sandbox.md. vectors [0, 0, 9, 4, 0] vs [0, 0, 8, 3, 0]; max axis spread 1.
- **UTC_Offset_Time_Lookup** — kept `I11-time-and-autonomy.md` (observed), also found by I9-web-and-browser.md. vectors [0, 0, 1, 6, 2] vs [1, 0, 0, 4, 4]; max axis spread 2.

## Flagged for a human read

- Doctor_Diagnostics_Command: axis spread 5 across arms
- Permission_Profile_Legacy_Exclusion: axis spread 4 across arms
- Hook_Source_Layering: axis spread 5 across arms
- Hook_Matcher_Filter: axis spread 3 across arms
- Hook_Command_Handler: axis spread 4 across arms
- PreToolUse_Control_Hook: axis spread 6 across arms
- PermissionRequest_Decision_Hook: axis spread 6 across arms
- PostToolUse_Feedback_Hook: axis spread 5 across arms
- UserPromptSubmit_Guard_Hook: axis spread 7 across arms
- SessionStart_Context_Hook: axis spread 4 across arms
- PreCompact_Gate_Hook: axis spread 4 across arms
- PostCompact_Gate_Hook: axis spread 5 across arms
- Stop_Continuation_Hook: axis spread 4 across arms
- Managed_Permission_Profile_Allowlist: axis spread 7 across arms
- Multi_Folder_Local_Project: axis spread 3 across arms
- SSH_Remote_Project_Execution: axis spread 3 across arms
- Cross_Host_Chat_Handoff: axis spread 3 across arms
- AGENTS_Context_Byte_Limit: axis spread 4 across arms
- Local_Skill_Discovery_Scopes: axis spread 4 across arms
- Plugin_Package_Manifest: axis spread 4 across arms
- MCP_Tool_Filter_Policy: axis spread 3 across arms
- Agent_Internet_Access_Mode: axis spread 4 across arms
- Exec_JSONL_Event_Output: axis spread 7 across arms
- Existing_Chat_Scheduled_Task: axis spread 3 across arms

## Human-reviewed scoring resolutions

The automated `kept` choices above are confidence/sum tie-breaks, not final
scoring judgments. The reconciled `ALL-PRIMITIVES.json` supersedes those choices
for the following rows after reading both mechanisms:

- `Permission_Profile_Legacy_Exclusion` keeps I6 `[0,8,7,0,0]`: the surface chooses an authority/configuration branch; downstream resource reach is not the primitive.
- `Approval_Policy` keeps I2 `[0,10,6,0,0]` at `observed`: CLI 0.150.0-alpha.8 help was exercised and exposed only `on-request` and `never`; D2's fresh manual still listed the retired `untrusted` mode, and D7 dates that removal to CLI 0.149.0.
- `Hook_Source_Layering` keeps I6 `[2,4,8,5,0]`: layering primarily changes approach and reachable configuration, not task skill.
- `Hook_Matcher_Filter` keeps I6 `[0,2,9,0,0]`: regex selection changes dispatch approach.
- `Hook_Command_Handler` keeps I6 `[4,4,7,7,0]`: process reach is not itself arbitrary task ability.
- `PreToolUse_Control_Hook` keeps I6 `[1,10,9,0,0]`: pre-execution authority and sequencing dominate.
- `PermissionRequest_Decision_Hook` keeps I6 `[0,10,8,0,0]`: it decides authority before the ordinary reviewer.
- `PostToolUse_Feedback_Hook` keeps I6 `[1,5,8,0,2]`: it gates continuation and alters model-visible feedback after execution.
- `SessionStart_Context_Hook` keeps I6 `[1,3,6,1,8]`: persistent context injection, rather than broad task skill, is the mechanism.
- `PreCompact_Gate_Hook` and `PostCompact_Gate_Hook` keep I6 `[0,4,9,0,1]`: these are lifecycle gates, not broad skill or knowledge stores.
- `Stop_Continuation_Hook` keeps I6 `[1,7,10,0,0]`: it overrides stopping and creates a continuation turn.
- `Managed_Permission_Profile_Allowlist` keeps I6 `[0,10,3,0,0]`: it constrains selectable authority profiles, not direct resource reach.
- `SSH_Remote_Project_Execution` keeps D3 `[3,2,4,10,0]`: the primitive's primary mechanism is remote reach; task-specific ability remains secondary.
- `Local_Skill_Discovery_Scopes` keeps I4 `[5,0,4,9,0]`: filesystem/package reach dominates discovery.
- `Exec_JSONL_Event_Output` keeps I2 `[1,0,7,5,0]`: serialization exposes execution flow without inheriting the knowledge content of each event.

Other flagged winners were retained after review because their selected vector's
mechanism was directly supported. In particular, `UserPromptSubmit_Guard_Hook`
retains Knowledge mass for documented developer-context injection, while
`Agent_Internet_Access_Mode` retains Resources mass for the actual network gate.
