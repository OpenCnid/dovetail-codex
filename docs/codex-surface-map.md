# Codex surface map

This port was validated against Codex CLI `0.150.0-alpha.8` on Windows.
Observed behavior takes priority over documentary behavior; version-sensitive
claims should be verified again before they become standing instructions.

| Requirement | Native surface | Port decision |
|---|---|---|
| Package discovery | `Plugin_Manifest` at `.codex-plugin/plugin.json` | Declare `skills: "./skills/"`; remove copied-skill installation as the primary route. |
| Repository distribution | `Plugin_Marketplace_*` | Publish the repository-root plugin from `.agents/plugins/marketplace.json`. |
| Cheap routing | `Skill_Frontmatter_Name`, `Skill_Frontmatter_Description`, `Skill_Catalog_Context_Budget` | Keep descriptions short and discriminative because they consume every-turn catalog context. |
| Detailed procedure | `SKILL_Markdown_Instruction_Body`, `SKILL_Full_Read_Gate` | Keep complete workflow instructions in each selected skill body. |
| Conditional depth | `Routed_Skill_Reference_Loading`, `Skill_Relative_Path_Resolution` | Load references only for the active branch and resolve scripts relative to the skill source locator. |
| UI and invocation policy | `Skill_UI_Interface_Metadata`, `OpenAI_YAML_Implicit_Invocation_Policy` | Give every skill `agents/openai.yaml`; make `spark-steering` and `upsum` explicit-only. |
| Repository instructions | `AGENTS_Root_To_CWD_Chain`, `AGENTS_Context_Byte_Limit` | Use a compact root `AGENTS.md`; rely on closer files for subtree-specific rules. |
| Delegated context | `collaboration.spawn_agent`, `fork_turns` | Choose `"none"`, `"all"`, or a positive turn count according to the evidence boundary. |
| Delegated coordination | `collaboration.send_message`, `followup_task`, `wait_agent`, `interrupt_agent`, `list_agents` | Use native collaboration lifecycle operations rather than invented agent files or copied transcripts. |
| Shared state | `Shared_Working_Directory`, `Shared_Filesystem` | Treat prompt isolation and filesystem isolation as separate concerns; guard shared writes explicitly. |
| Permission and model inheritance | `Parent_Permission_Policy_Inheritance`, `Model_Override_Fork_Constraint` | Do not promise stronger isolation than the runtime provides; only override model/reasoning with a non-default fork. |
| Noninteractive evaluation | `codex exec`, `--json`, `--output-last-message`, `--output-schema`, `--ephemeral`, `--ignore-user-config` | Prefer deterministic CLI runs when an external harness is needed; native collaboration is the default for interactive composition. |

## Steering diagnosis

The original pack already had the desired capabilities. Its Codex path was an
installation bridge layered over Claude-oriented ownership and lifecycle
assumptions. On Spark Steering's axes this is primarily **A — approaches**:
the work belongs on different native surfaces. It is not **R — resources**;
Codex already exposes plugin discovery, skill activation, repository
instructions, subagent context control, and noninteractive execution.

The cheapest reliable move is therefore to name and use those surfaces once at
the correct lifecycle boundary. No MCP server, permission expansion, always-on
hook, or copied global skill directory is required.

## Prompt budget consequences

- The skill catalog is paid every turn, so frontmatter descriptions are routing
  keys rather than miniature manuals.
- A selected skill body is read in full, so it must contain the complete common
  path but can route rare branches to references.
- `AGENTS.md` is inherited root-to-CWD and shares a default 32 KiB combined
  budget, so repository guidance must stay compact and local overrides must
  carry local detail.
- UI starter prompts are interface affordances, not model policy. Behavioral
  requirements remain in `SKILL.md` or `AGENTS.md`.
