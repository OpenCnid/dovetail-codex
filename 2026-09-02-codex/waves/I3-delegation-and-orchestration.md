# I3 Delegation and Orchestration

### Subagent_Spawn_Tool
- **surface**: `collaboration.spawn_agent({ task_name, message, fork_turns? })`
- **evidence**: `tool://collaboration.spawn_agent` — In the live Codex Desktop 26.820.9563.0 delegated-session namespace, the schema says: “Spawns an agent to work on the specified task”; this session arrived as `/root/i3_delegation` via `NEW_TASK` from `/root`.
- **does**: Spawns a bounded independent subagent alongside the caller.
- **spark**: S=0 P=0 A=9 R=6 K=0
- **why**: A via explicit work decomposition and parallel delegation; R via an additional agent execution slot.
- **rent**: every_spawn — each child incurs its own model work and context.
- **composes**: [[Subagent_Context_Fork_Control]], [[Subagent_Concurrency_Cap]], [[Subagent_Canonical_Task_Addressing]]
- **confidence**: observed

### Subagent_Context_Fork_Control
- **surface**: `fork_turns: "none" | "all" | "<positive integer>"`
- **evidence**: `tool://collaboration.spawn_agent` — The live Codex Desktop 26.820.9563.0 schema defines `none`, `all`, or a positive-integer string such as `"3"`; omission defaults to `all`.
- **does**: Selects how much completed conversation history seeds a child agent.
- **spark**: S=0 P=0 A=8 R=4 K=0
- **why**: A via deliberate context partitioning; R via controlled reach into parent-turn history.
- **rent**: every_spawn — inherited turns occupy the child’s input context.
- **composes**: [[Subagent_Spawn_Tool]], [[Subagent_Model_Override_Control]], [[Subagent_Reasoning_Effort_Override_Control]]
- **confidence**: documented

### Subagent_Model_Override_Control
- **surface**: `model` on `collaboration.spawn_agent`
- **evidence**: `tool://collaboration.spawn_agent` — The live Codex Desktop 26.820.9563.0 schema exposes model overrides and states that inherited parent-model use is preferred.
- **does**: Selects the model used by a spawned child when context-fork rules permit an override.
- **spark**: S=4 P=0 A=5 R=5 K=0
- **why**: S via changing the child’s model capability; A via per-workstream routing; R via access to the listed model pool.
- **rent**: every_spawn — the selected model meters the child’s work.
- **composes**: [[Subagent_Spawn_Tool]], [[Subagent_Context_Fork_Control]]
- **confidence**: documented

### Subagent_Reasoning_Effort_Override_Control
- **surface**: `reasoning_effort` on `collaboration.spawn_agent`
- **evidence**: `tool://collaboration.spawn_agent` — The live Codex Desktop 26.820.9563.0 schema lists per-model reasoning efforts and permits an override only with `fork_turns="none"` or a positive integer.
- **does**: Selects the reasoning effort used by a spawned child when context-fork rules permit an override.
- **spark**: S=2 P=0 A=5 R=4 K=0
- **why**: S via changing reasoning depth; A via per-workstream effort allocation; R via model-compute selection.
- **rent**: every_spawn — the selected effort meters reasoning work in the child.
- **composes**: [[Subagent_Spawn_Tool]], [[Subagent_Context_Fork_Control]]
- **confidence**: documented

### Subagent_Canonical_Task_Addressing
- **surface**: `task_name` returned by `collaboration.spawn_agent` and accepted by collaboration tools
- **evidence**: `tool://collaboration.list_agents` — The exercised call returned `/root`, `/root/i1_files_search`, `/root/i2_execution`, and `/root/i3_delegation` in the live Codex Desktop 26.820.9563.0 tree.
- **does**: Assigns each agent a hierarchical canonical task address.
- **spark**: S=0 P=0 A=6 R=2 K=0
- **why**: A via deterministic routing across a delegation tree; R via an addressable agent handle.
- **rent**: none — task addresses add no declared recurring charge.
- **composes**: [[Subagent_List_Tool]], [[Subagent_Message_Tool]], [[Subagent_Followup_Tool]], [[Subagent_Interrupt_Tool]]
- **confidence**: observed

### Nested_Subagent_Spawning
- **surface**: `collaboration.spawn_agent` from a delegated task
- **evidence**: `tool://collaboration.spawn_agent` — The tool is present in this `/root/i3_delegation` session, and its live schema states that spawned agents “can also spawn their own subagents.”
- **does**: Makes recursive delegation available to child agents.
- **spark**: S=0 P=0 A=9 R=6 K=0
- **why**: A via recursive decomposition; R via additional descendant execution slots.
- **rent**: every_spawn — each descendant incurs its own model work and context.
- **composes**: [[Subagent_Spawn_Tool]], [[Subagent_Concurrency_Cap]]
- **confidence**: documented

### Subagent_Shared_Filesystem
- **surface**: shared workspace contract for `collaboration.spawn_agent`
- **evidence**: `tool://collaboration.spawn_agent` — The live delegated-session contract says all agents share the same current working directory and filesystem, making edits immediately visible across agents.
- **does**: Exposes one shared workspace state to every agent in the delegation tree.
- **spark**: S=0 P=0 A=4 R=8 K=0
- **why**: A via artifact-level collaboration; R via shared access to the same files.
- **rent**: none — the shared filesystem adds no declared prompt or installation charge.
- **composes**: [[Subagent_Spawn_Tool]], [[Subagent_List_Tool]]
- **confidence**: documented

### Subagent_Concurrency_Cap
- **surface**: four live collaboration slots
- **evidence**: `tool://collaboration.list_agents` — The live schema states “4 available concurrency slots, including you”; the exercised listing showed four running agents in the root tree.
- **does**: Caps the live delegation tree at four concurrent agents.
- **spark**: S=0 P=0 A=7 R=5 K=0
- **why**: A via bounded parallel scheduling; R via a fixed agent-slot pool.
- **rent**: none — the cap constrains consumption without adding a charge.
- **composes**: [[Subagent_Spawn_Tool]], [[Nested_Subagent_Spawning]], [[Subagent_List_Tool]]
- **confidence**: documented

### Subagent_Message_Tool
- **surface**: `collaboration.send_message({ target, message })`
- **evidence**: `tool://collaboration.send_message` — The live Codex Desktop 26.820.9563.0 schema says a message is queued to an existing agent, delivered promptly, and “does not trigger a new turn.”
- **does**: Delivers a message to an existing agent without starting an idle turn.
- **spark**: S=0 P=0 A=7 R=3 K=0
- **why**: A via asynchronous peer coordination; R via an inter-agent message channel.
- **rent**: every_matching_call — each message enters the recipient’s orchestration context.
- **composes**: [[Subagent_Canonical_Task_Addressing]], [[Subagent_Followup_Tool]]
- **confidence**: documented

### Subagent_Followup_Tool
- **surface**: `collaboration.followup_task({ target, message })`
- **evidence**: `tool://collaboration.followup_task` — The live Codex Desktop 26.820.9563.0 schema says it sends a follow-up and triggers a turn if the target is idle.
- **does**: Delivers a follow-up that starts an idle agent turn.
- **spark**: S=0 P=4 A=8 R=3 K=0
- **why**: P via authority to resume an idle agent; A via continuation scheduling; R via an inter-agent message channel.
- **rent**: every_matching_call — the follow-up can initiate another model turn.
- **composes**: [[Subagent_Canonical_Task_Addressing]], [[Subagent_Message_Tool]]
- **confidence**: documented

### Subagent_Interrupt_Tool
- **surface**: `collaboration.interrupt_agent({ target })`
- **evidence**: `tool://collaboration.interrupt_agent` — The live Codex Desktop 26.820.9563.0 schema says it interrupts the current turn, returns the previous status, and leaves the agent available.
- **does**: Stops an agent’s active turn while retaining the agent for later work.
- **spark**: S=0 P=8 A=5 R=1 K=0
- **why**: P via explicit authority over another agent’s continuation; A via cancellation without destroying the worker; R via returned status.
- **rent**: none — interruption stops work and declares no recurring charge.
- **composes**: [[Subagent_Canonical_Task_Addressing]], [[Subagent_Followup_Tool]], [[Subagent_List_Tool]]
- **confidence**: documented

### Subagent_Wait_Tool
- **surface**: `collaboration.wait_agent({ timeout_ms? })`
- **evidence**: `tool://collaboration.wait_agent` — Exercising `timeout_ms: 10000` in Codex Desktop 26.820.9563.0 returned `{"message":"Wait timed out.","timed_out":true}`; the schema permits 10,000–3,600,000 ms.
- **does**: Suspends coordination until agent activity arrives or a bounded timeout expires.
- **spark**: S=0 P=0 A=6 R=2 K=0
- **why**: A via event-driven synchronization; R via access to child completion signals.
- **rent**: none — waiting creates no additional agent turn.
- **composes**: [[Subagent_List_Tool]], [[Subagent_Spawn_Tool]]
- **confidence**: observed

### Subagent_List_Tool
- **surface**: `collaboration.list_agents({ path_prefix? })`
- **evidence**: `tool://collaboration.list_agents` — The exercised Codex Desktop 26.820.9563.0 call returned four live agents with canonical names and `running` statuses; the schema accepts an optional task-path prefix.
- **does**: Returns live agent statuses for the root delegation tree.
- **spark**: S=0 P=0 A=5 R=4 K=0
- **why**: A via orchestration-state inspection; R via access to the live agent registry.
- **rent**: none — this is a read-only status query.
- **composes**: [[Subagent_Canonical_Task_Addressing]], [[Subagent_Wait_Tool]], [[Subagent_Concurrency_Cap]]
- **confidence**: observed

### Task_Plan_Update_Tool
- **surface**: `update_plan({ explanation?, plan: [{ step, status }] })`
- **evidence**: `tool://update_plan` — The live schema defines `pending`, `in_progress`, and `completed` statuses and requires at most one in-progress step.
- **does**: Stores an ordered task plan with lifecycle status per step.
- **spark**: S=0 P=0 A=8 R=2 K=0
- **why**: A via explicit sequencing and progress tracking; R via mutable plan state.
- **rent**: none — the schema declares no installation or recurring charge.
- **composes**: [[Goal_Creation_Tool]], [[Goal_Read_Tool]]
- **confidence**: documented

### Goal_Creation_Tool
- **surface**: `create_goal({ objective, token_budget? })`
- **evidence**: `tool://create_goal` — The live schema requires an explicit user or system/developer request, rejects replacement of an unfinished goal, and starts a new goal from an objective.
- **does**: Starts one concrete active goal under explicit authorization.
- **spark**: S=0 P=6 A=7 R=1 K=0
- **why**: P via explicit-authority gating; A via durable objective tracking; R via one active-goal slot.
- **rent**: every_turn — active goal tracking meters token and elapsed usage across continuing goal turns.
- **composes**: [[Goal_Token_Budget]], [[Goal_Read_Tool]], [[Goal_State_Update_Tool]]
- **confidence**: documented

### Goal_Token_Budget
- **surface**: `token_budget` on `create_goal`
- **evidence**: `tool://create_goal` — The live schema accepts a positive optional `token_budget` only when the request explicitly supplies a budget; `tool://get_goal` reports token usage and remaining budget.
- **does**: Attaches a positive token budget to an explicitly budgeted goal.
- **spark**: S=0 P=4 A=5 R=6 K=0
- **why**: P via user-controlled budget authority; A via a stopping-accountability constraint; R via metered token allocation.
- **rent**: every_turn — continuing goal turns consume the configured token budget.
- **composes**: [[Goal_Creation_Tool]], [[Goal_Read_Tool]], [[Goal_State_Update_Tool]]
- **confidence**: documented

### Goal_Read_Tool
- **surface**: `get_goal({})`
- **evidence**: `tool://get_goal` — The exercised call returned `{"goal":null,"remainingTokens":null,"completionBudgetReport":null}` in this delegated session; the live schema covers status, budgets, token usage, elapsed-time usage, and remaining budget.
- **does**: Reports the current thread goal and its budget state.
- **spark**: S=0 P=0 A=4 R=4 K=0
- **why**: A via progress-accounting visibility; R via read access to goal telemetry.
- **rent**: none — this is a read-only state query.
- **composes**: [[Goal_Creation_Tool]], [[Goal_Token_Budget]], [[Goal_State_Update_Tool]]
- **confidence**: observed

### Goal_State_Update_Tool
- **surface**: `update_goal({ status: "complete" | "blocked" })`
- **evidence**: `tool://update_goal` — The live schema permits only `complete` or `blocked`; blocking requires the same impediment for three consecutive goal turns, while budget exhaustion alone cannot justify completion.
- **does**: Terminates an active goal as complete or genuinely blocked.
- **spark**: S=0 P=7 A=8 R=1 K=0
- **why**: P via constrained authority to terminate tracked work; A via explicit terminal-state policy; R via goal-state mutation.
- **rent**: none — the transition ends rather than perpetuates goal tracking.
- **composes**: [[Goal_Creation_Tool]], [[Goal_Token_Budget]], [[Goal_Read_Tool]]
- **confidence**: documented

### Multi_Agent_Feature_Flag
- **surface**: `--enable multi_agent`, `--disable multi_agent`, or `features.multi_agent`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; exercised `codex features list` reported `multi_agent stable true`, and `codex --help` maps `--enable/--disable` to `features.<name>`.
- **does**: Enables or disables the stable multi-agent runtime feature.
- **spark**: S=0 P=6 A=7 R=2 K=0
- **why**: P via invocation gating for delegation; A via selecting multi-agent execution; R via exposing the collaboration surface.
- **rent**: every_turn — when enabled, collaboration schemas and policies occupy agent context.
- **composes**: [[Subagent_Spawn_Tool]], [[Subagent_List_Tool]]
- **confidence**: observed

### Goals_Feature_Flag
- **surface**: `--enable goals`, `--disable goals`, or `features.goals`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe` — `codex-cli 0.150.0-alpha.8`; exercised `codex features list` reported `goals stable true`, and `codex --help` maps `--enable/--disable` to `features.<name>`.
- **does**: Enables or disables stable goal tracking.
- **spark**: S=0 P=6 A=6 R=2 K=0
- **why**: P via invocation gating for persistent goal state; A via selecting goal-oriented execution; R via exposing goal tools.
- **rent**: every_turn — when enabled, goal schemas and policies occupy agent context.
- **composes**: [[Goal_Creation_Tool]], [[Goal_Read_Tool]], [[Goal_State_Update_Tool]]
- **confidence**: observed

## Uncovered
- Mutating collaboration controls (`spawn_agent`, `send_message`, `followup_task`, `interrupt_agent`) were not exercised because this arm was forbidden to alter orchestration; their live schemas are recorded as documented, except spawning observed indirectly through this delegated session.
- Mutating plan and goal writers were not exercised because no explicit goal authorization was present and the probe permits only its output write.
- `codex agents`, `codex queue`, and `codex fork` identify saved user-owned session management in `codex-cli 0.150.0-alpha.8`; deeper treatment belongs to I8/I11 and is excluded here.
- The installed registry was searched for adjacent names: `multi_agent_v2` and `token_budget` are disabled under-development flags, while `collaboration_modes`, `enable_fanout`, `multi_agent_mode`, `send_async_message`, and `steer` are marked removed; inert or removed names were not emitted as capabilities.
- Official Codex documentation search exposed no page for these Desktop collaboration tool names; the retrieved multi-agent page concerns the Responses API beta, so it was excluded from this Codex-runtime inventory.
