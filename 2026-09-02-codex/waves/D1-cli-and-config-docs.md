<!-- Documentary comparison pin: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; 2026-09-02. Primary manual snapshot refreshed 2026-09-02. -->

### Config_Layer_Precedence
- **surface**: `CLI flags / --config > .codex/config.toml > --profile > ~/.codex/config.toml > /etc/codex/config.toml > built-in defaults`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:13081` — “Codex resolves values in this order (highest precedence first)” followed by the six documented layers at lines 13085–13090.
- **does**: Resolves competing configuration values through a deterministic priority order.
- **spark**: S=0 P=0 A=7 R=2 K=0
- **why**: A because the layer order governs how runtime behavior is selected; R because higher layers can redirect configured resources.
- **rent**: every_turn — the effective configuration constrains each agent turn without repeated user input.
- **composes**: [[Trusted_Project_Config_Layers]], [[Named_Config_Profile_Layer]], [[One_Off_Config_Override]]
- **confidence**: documented

### Trusted_Project_Config_Layers
- **surface**: `.codex/config.toml`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:12004` — “Codex walks from the project root to your current working directory and loads every `.codex/config.toml` it finds”; line 12008 says untrusted projects ignore project `.codex/` layers.
- **does**: Applies directory-specific project configuration only after the project is trusted.
- **spark**: S=0 P=7 A=4 R=2 K=0
- **why**: P because trust decides whether repository-authored configuration receives authority; A because nearer directory layers specialize runtime behavior; R because loaded layers can change reachable surfaces.
- **rent**: every_turn — trusted project settings remain active across turns in that project.
- **composes**: [[Config_Layer_Precedence]], [[Project_Trust_Gate]]
- **confidence**: documented

### Named_Config_Profile
- **surface**: `codex --profile profile-name`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11923` — “When you pass `--profile profile-name`, Codex loads `~/.codex/config.toml`, then overlays `~/.codex/profile-name.config.toml`.” Lines 11951–11956 pin the separate-file behavior to Codex 0.134.0 and later, which includes target codex-cli 0.150.0-alpha.8.
- **does**: Overlays a named configuration file on the base user configuration for one invocation.
- **spark**: S=0 P=0 A=7 R=3 K=0
- **why**: A because profiles package reusable execution approaches; R because a profile can select different runtime resources.
- **rent**: every_turn — selected profile values govern every turn in the invocation.
- **composes**: [[Config_Layer_Precedence]], [[Default_Model_Config]], [[Model_Reasoning_Effort_Config]]
- **confidence**: documented

### One_Off_Config_Override
- **surface**: `-c key=value` / `--config key=value`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11958` — “Use `-c` / `--config` when you need to override an arbitrary key”; lines 11979–11981 document dot notation and TOML parsing.
- **does**: Overrides an arbitrary configuration key for a single CLI run.
- **spark**: S=0 P=0 A=6 R=3 K=0
- **why**: A because it changes the run method without editing persistent config; R because it can redirect configured resources.
- **rent**: every_turn — the override remains effective for the run's turns.
- **composes**: [[Config_Layer_Precedence]]
- **confidence**: documented

### Default_Model_Config
- **surface**: `model = "<model>"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:13108` — “Choose the model Codex uses by default in the CLI and IDE.”
- **does**: Selects the default model for local Codex sessions.
- **spark**: S=4 P=0 A=2 R=9 K=3
- **why**: S because model choice changes available reasoning capability; A because it changes the execution strategy baseline; R because it selects the model resource; K because models carry different learned knowledge.
- **rent**: every_turn — the selected model consumes usage on each model turn.
- **composes**: [[Model_Override_Flag]], [[Model_Slash_Command]], [[Model_Reasoning_Effort_Config]]
- **confidence**: documented

### Model_Reasoning_Effort_Config
- **surface**: `model_reasoning_effort = "minimal|low|medium|high|xhigh"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11558` — “Adjust reasoning effort for supported models (Responses API only; `xhigh` is model-dependent).” Lines 13325–13327 state that higher effort takes longer and uses more tokens.
- **does**: Sets the reasoning effort used by supported models.
- **spark**: S=3 P=0 A=8 R=1 K=0
- **why**: S because more reasoning can improve complex-task performance; A because effort directly changes the depth of the model's method; R because higher effort consumes more token budget.
- **rent**: every_turn — configured reasoning depth changes token and latency cost on supported model turns.
- **composes**: [[Default_Model_Config]], [[Model_Slash_Command]]
- **confidence**: documented

### Plan_Mode_Reasoning_Effort_Config
- **surface**: `plan_mode_reasoning_effort = "none|minimal|low|medium|high|xhigh"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11611` — “Plan-mode-specific reasoning override. When unset, Plan mode uses its built-in preset default.”
- **does**: Overrides reasoning effort specifically while Plan mode is active.
- **spark**: S=2 P=0 A=8 R=1 K=0
- **why**: S because plan quality can change with supported effort; A because it tunes the planning method independently; R because selected effort consumes model budget.
- **rent**: every_turn — the override applies to each Plan-mode model turn.
- **composes**: [[Plan_Mode_Slash_Command]], [[Model_Reasoning_Effort_Config]]
- **confidence**: documented

### Personality_Config
- **surface**: `personality = "none|friendly|pragmatic"`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11610` — “Default communication style for models that advertise `supportsPersonality`; can be overridden per thread/turn or via `/personality`.”
- **does**: Sets the default communication style for personality-capable models.
- **spark**: S=0 P=9 A=1 R=0 K=0
- **why**: P because the setting directly changes how the agent addresses the user; A because style can alter presentation method.
- **rent**: every_turn — personality instructions shape each supported response.
- **composes**: [[Personality_Slash_Command]], [[Default_Model_Config]]
- **confidence**: documented

### TUI_Keymap_Config
- **surface**: `[tui.keymap.<context>] <action> = <binding>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11649` — “Supported contexts include `global`, `chat`, `composer`, `editor`, `vim_normal`, `vim_operator`, `vim_text_object`, `pager`, `list`, and `approval`”; line 11650 documents empty-array unbinding.
- **does**: Assigns or removes keyboard bindings for context-specific TUI actions.
- **spark**: S=0 P=0 A=3 R=5 K=0
- **why**: A because bindings change the user's interaction method; R because they expose TUI actions through customized controls.
- **rent**: none — bindings incur no documented recurring agent charge.
- **composes**: [[Keymap_Slash_Command]], [[Interactive_TUI_Command]]
- **confidence**: documented

### Shell_Environment_Policy
- **surface**: `[shell_environment_policy]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:13202` — “Control which environment variables Codex forwards to spawned commands”; lines 11628–11634 document inheritance, filters, secret-name exclusions, and explicit values.
- **does**: Filters the environment inherited by processes Codex spawns.
- **spark**: S=0 P=2 A=3 R=8 K=0
- **why**: P because the policy decides what process context receives authority; A because it establishes a repeatable subprocess method; R because it controls access to environment-provided resources.
- **rent**: every_spawn — the policy is evaluated for each spawned process.
- **composes**: [[Spawned_Command_Execution]], [[Local_Shell_Command_Prefix]]
- **confidence**: documented

### CODEX_HOME_Environment_Variable
- **surface**: `CODEX_HOME`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11842` — “Sets the root for Codex state, including config, auth, logs, sessions, skills, and standalone package metadata.”
- **does**: Relocates the root directory used for Codex state.
- **spark**: S=0 P=0 A=2 R=8 K=0
- **why**: A because it changes state-location convention; R because it redirects configuration, credentials, logs, and sessions.
- **rent**: every_turn — the selected state root remains the backing store throughout the session.
- **composes**: [[Named_Config_Profile_Layer]], [[TUI_Keymap_Config]], [[Session_Resume_Command]]
- **confidence**: documented

### CODEX_SQLITE_HOME_Environment_Variable
- **surface**: `CODEX_SQLITE_HOME`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11843` — “Sets where SQLite-backed state is stored. The `sqlite_home` config option takes precedence.”
- **does**: Relocates SQLite-backed CLI and app-server state.
- **spark**: S=0 P=0 A=1 R=6 K=0
- **why**: A because it changes persistence layout; R because it redirects the state database.
- **rent**: every_turn — the configured database location backs ongoing session state.
- **composes**: [[CODEX_HOME_Environment_Variable]], [[Session_Resume_Command]]
- **confidence**: documented

### CODEX_CA_CERTIFICATE_Environment_Variable
- **surface**: `CODEX_CA_CERTIFICATE`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11879` — “Points to a PEM CA bundle for environments with corporate TLS interception or private root certificates. Takes precedence over `SSL_CERT_FILE`.”
- **does**: Supplies the preferred certificate-authority bundle to Codex network clients.
- **spark**: S=0 P=0 A=1 R=7 K=0
- **why**: A because it changes TLS validation setup; R because it enables authenticated reachability through private trust roots.
- **rent**: every_matching_call — HTTPS, login, and WebSocket connections consult the configured trust bundle.
- **composes**: [[CLI_Network_Client]], [[Login_Command]]
- **confidence**: documented

### RUST_LOG_Environment_Variable
- **surface**: `RUST_LOG`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:11897` — “Controls Rust log filtering and verbosity”; lines 11899–11901 list global and target-specific filter forms.
- **does**: Selects diagnostic logging verbosity for the CLI and app server.
- **spark**: S=0 P=0 A=2 R=4 K=5
- **why**: A because it changes the troubleshooting method; R because it exposes diagnostic output; K because logs reveal runtime behavior.
- **rent**: every_matching_call — matching runtime events produce the configured diagnostic detail.
- **composes**: [[Doctor_Command]], [[Config_Diagnostics_Slash_Command]]
- **confidence**: documented

### Prompt_Editor_Environment_Selection
- **surface**: `VISUAL` / `EDITOR` with `Ctrl+G`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:16350` — “press Ctrl+G in the composer to open the editor configured by `VISUAL`, or `EDITOR` when `VISUAL` isn't set.”
- **does**: Opens long prompt text in the user's configured external editor.
- **spark**: S=0 P=0 A=4 R=5 K=0
- **why**: A because it provides an alternate prompt-authoring method; R because it reaches an external editor process.
- **rent**: every_matching_call — the editor is launched only when the shortcut is invoked.
- **composes**: [[Interactive_TUI_Command]]
- **confidence**: documented

### Interactive_TUI_Command
- **surface**: `codex [PROMPT]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14847` — “Running `codex` with no subcommand launches the interactive terminal UI (TUI).”
- **does**: Starts an interactive Codex terminal session with an optional initial prompt.
- **spark**: S=1 P=2 A=5 R=7 K=0
- **why**: S because it activates the coding agent; P because the TUI mediates ongoing user-agent exchange; A because it supports iterative steering; R because it exposes the local CLI harness.
- **rent**: every_turn — the interactive session mediates each user and agent turn.
- **composes**: [[Slash_Command_Popup]], [[Local_Shell_Command_Prefix]], [[Active_Turn_Instruction_Injection]]
- **confidence**: documented

### Working_Directory_Flag
- **surface**: `--cd <path>` / `-C <path>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14784` — “Set the working directory for the agent before it starts processing your request.”
- **does**: Selects the agent's initial working directory.
- **spark**: S=0 P=0 A=2 R=8 K=0
- **why**: A because it changes project resolution context; R because it selects the primary filesystem workspace.
- **rent**: every_turn — relative file and command resolution use the selected directory across the session.
- **composes**: [[Interactive_TUI_Command]], [[Trusted_Project_Config_Layers]]
- **confidence**: documented

### Initial_Image_Attachment_Flag
- **surface**: `--image <path[,path...]>` / `-i <path[,path...]>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14790` — “Attach one or more image files to the initial prompt.”
- **does**: Adds local image files to the first prompt of a CLI session.
- **spark**: S=2 P=0 A=2 R=7 K=0
- **why**: S because visual input enables image-grounded work; A because it changes the prompting method; R because it makes local image assets reachable to the model.
- **rent**: none — attachment occurs once at invocation.
- **composes**: [[Interactive_TUI_Command]], [[Prompt_Input]]
- **confidence**: documented

### Live_Web_Search_Flag
- **surface**: `--search`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14799` — “Enable live web search (sets `web_search = "live"` instead of the default `"cached"`).”
- **does**: Switches the current CLI run from cached search to live web retrieval.
- **spark**: S=1 P=0 A=2 R=9 K=4
- **why**: S because live retrieval enables current-information tasks; A because it changes retrieval method; R because it reaches live external pages; K because it supplies current external knowledge.
- **rent**: every_matching_call — live network retrieval occurs when the agent invokes search.
- **composes**: [[Interactive_TUI_Command]], [[Web_Search_Mode_Config]]
- **confidence**: documented

### Strict_Config_Validation
- **surface**: `--strict-config`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14800` — “Error when `config.toml` contains fields this Codex version does not recognize.”
- **does**: Converts unknown configuration fields into startup errors for supported runtime commands.
- **spark**: S=0 P=0 A=7 R=1 K=2
- **why**: A because it changes configuration validation from permissive to fail-fast; R because it gates startup; K because the error exposes version drift.
- **rent**: none — validation occurs during invocation setup.
- **composes**: [[Config_Layer_Precedence]], [[Doctor_Command]]
- **confidence**: documented

### Model_Override_Flag
- **surface**: `--model <model>` / `-m <model>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14792` — “Override the model set in configuration.”
- **does**: Selects a model for one CLI invocation.
- **spark**: S=4 P=0 A=2 R=9 K=3
- **why**: S because model choice changes reasoning capability; A because it changes the run's execution baseline; R because it selects a model resource; K because models carry different learned knowledge.
- **rent**: every_turn — the selected model serves each model turn in the invocation.
- **composes**: [[Default_Model_Config]], [[Config_Layer_Precedence]]
- **confidence**: documented

### OSS_Provider_Selection
- **surface**: `--oss [--local-provider lmstudio|ollama]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:14791` — `--local-provider` chooses the provider used with `--oss`; line 14794 says Codex otherwise uses configured `oss_provider` or prompts between LM Studio and Ollama.
- **does**: Routes a CLI run to a supported local open-source model provider.
- **spark**: S=2 P=0 A=3 R=9 K=1
- **why**: S because local-provider models may expose different capabilities; A because it changes model-serving strategy; R because it reaches a local provider; K because the chosen model supplies its own learned knowledge.
- **rent**: every_turn — the local provider serves each model turn.
- **composes**: [[Model_Override_Flag]], [[Custom_Model_Provider]]
- **confidence**: documented

### Doctor_Diagnostics_Command
- **surface**: `codex doctor [--all|--ascii|--json|--no-color|--summary]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15035` — “The report checks installation, configuration, authentication, runtime, Git, terminal, app-server, and thread inventory health.”
- **does**: Generates a local diagnostic report across major CLI dependencies.
- **spark**: S=1 P=0 A=4 R=5 K=7
- **why**: S because it adds installation diagnosis; A because it standardizes troubleshooting; R because it inspects multiple local subsystems; K because it reveals their health.
- **rent**: none — the report is produced only when invoked.
- **composes**: [[RUST_LOG_Environment_Variable]], [[Config_Diagnostics_Slash_Command]]
- **confidence**: documented

### Feature_Flag_Command
- **surface**: `codex features list|enable <feature>|disable <feature>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15050` — “The `enable` and `disable` commands persist changes so they apply to future sessions”; lines 15056–15060 document list, enable, and disable modes.
- **does**: Lists or persistently toggles known CLI feature flags.
- **spark**: S=1 P=1 A=6 R=5 K=2
- **why**: S because enabled features can add capabilities; P because toggles govern whether a capability may appear; A because flags select runtime behavior; R because listing exposes available gates; K because maturity and effective state become visible.
- **rent**: every_turn — persisted feature state affects future sessions until changed.
- **composes**: [[Config_Layer_Precedence]], [[Experimental_Feature_Slash_Command]]
- **confidence**: documented

### Session_Resume_Command
- **surface**: `codex resume [--last|--all] [SESSION_ID]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15208` — “Continue an interactive session by ID or resume the most recent chat”; lines 15212–15216 document working-directory choice and `tui.resume_cwd` precedence.
- **does**: Restores a saved interactive session into the TUI.
- **spark**: S=0 P=1 A=5 R=7 K=4
- **why**: P because it restores the prior user-agent relationship context; A because it continues an existing workflow; R because it reaches saved session state; K because it restores the transcript.
- **rent**: every_turn — resumed history remains in the session context.
- **composes**: [[CODEX_HOME_Environment_Variable]], [[Working_Directory_Flag]]
- **confidence**: documented

### Session_Fork_Command
- **surface**: `codex fork [--last|--all] [SESSION_ID]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15225` — “Fork a previous interactive session into a new chat”; line 15227 says the original transcript is preserved.
- **does**: Creates a new chat branch from a saved interactive session.
- **spark**: S=0 P=0 A=9 R=5 K=3
- **why**: A because it enables parallel exploration from a common history; R because it accesses saved session state; K because the fork inherits the transcript.
- **rent**: none — branching is a one-time session operation.
- **composes**: [[Session_Resume_Command]], [[Prior_Message_Edit_Fork_Shortcut]]
- **confidence**: documented

### Local_Shell_Command_Prefix
- **surface**: `!<shell command>`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15293` — “Prefix a line with `!` to run a local shell command under the current approval and sandbox settings.”
- **does**: Executes an explicit local shell command from the interactive composer.
- **spark**: S=1 P=3 A=3 R=9 K=0
- **why**: S because it exposes direct command execution; P because approval policy governs authority; A because it bypasses model generation for a user-specified command; R because it reaches local compute and filesystem resources.
- **rent**: every_matching_call — compute is consumed only for prefixed commands.
- **composes**: [[Interactive_TUI_Command]], [[Shell_Environment_Policy]], [[Approval_Policy]]
- **confidence**: documented

### Queued_Followup_Shortcut
- **surface**: `Tab while Codex is working`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15294` — “Press Tab while Codex is working to queue a follow-up prompt, slash command, or shell command for the next turn.”
- **does**: Queues user input to run after the active turn finishes.
- **spark**: S=0 P=5 A=8 R=1 K=0
- **why**: P because the user retains control over the next interaction without interrupting current work; A because input is explicitly sequenced after the active turn; R because the queue stores pending input.
- **rent**: every_matching_call — queued input consumes a later turn when dispatched.
- **composes**: [[Interactive_TUI_Command]], [[Slash_Command_Popup]]
- **confidence**: documented

### Active_Turn_Instruction_Injection
- **surface**: `Enter while Codex is working`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15295` — “Press Enter while Codex is working to inject new instructions into the current turn.”
- **does**: Injects new user instructions into an active agent turn.
- **spark**: S=0 P=9 A=6 R=0 K=0
- **why**: P because it lets the user redirect ongoing work immediately; A because it changes the active execution path.
- **rent**: every_matching_call — each injection adds input to the active turn.
- **composes**: [[Interactive_TUI_Command]], [[Turn_Steering]]
- **confidence**: documented

### Prior_Message_Edit_Fork_Shortcut
- **surface**: `Esc Esc with an empty composer`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:15296` — “Press Esc twice with an empty composer to edit the previous user message and fork the chat from that point.”
- **does**: Branches a chat by editing its preceding user message.
- **spark**: S=0 P=2 A=9 R=3 K=2
- **why**: P because the user revises the instruction boundary; A because it creates an alternate approach from earlier history; R because it uses stored transcript state; K because it preserves preceding context.
- **rent**: none — the fork operation itself has no documented recurring charge.
- **composes**: [[Session_Fork_Command]], [[Interactive_TUI_Command]]
- **confidence**: documented

### Slash_Command_Popup
- **surface**: `/` in the TUI composer
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17571` — “Type `/` in the composer to open the slash popup”; lines 17584–17585 say typing filters the built-in command list.
- **does**: Opens a keyboard-filterable menu of built-in session commands.
- **spark**: S=0 P=1 A=4 R=7 K=1
- **why**: P because it exposes user control of the session; A because it provides a keyboard-first control method; R because it reaches built-in commands; K because filtering reveals available controls.
- **rent**: none — opening the menu has no documented recurring charge.
- **composes**: [[Model_Slash_Command]], [[Plan_Mode_Slash_Command]], [[Config_Diagnostics_Slash_Command]]
- **confidence**: documented

### Model_Slash_Command
- **surface**: `/model`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:13309` — “In an interactive CLI session, use `/model` to switch models or adjust reasoning effort.”
- **does**: Changes the active model or its reasoning effort within a CLI session.
- **spark**: S=4 P=0 A=5 R=9 K=3
- **why**: S because model choice changes reasoning capability; A because it retunes the current session without restart; R because it selects a model resource; K because models carry different learned knowledge.
- **rent**: every_turn — the chosen model and effort apply to subsequent turns.
- **composes**: [[Default_Model_Config]], [[Model_Reasoning_Effort_Config]], [[Session_Status_Slash_Command]]
- **confidence**: documented

### Fast_Mode_Slash_Command
- **surface**: `/fast`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17664` — “Type `/fast` to turn the current model's Fast service tier on”; lines 17669–17673 say the selection persists and the command is hidden when the model catalog does not advertise a Fast tier.
- **does**: Toggles the catalog-supported Fast service tier for the active model.
- **spark**: S=1 P=0 A=5 R=6 K=0
- **why**: S because the tier changes response performance; A because it changes the serving strategy; R because it selects a distinct model service tier.
- **rent**: every_turn — the saved tier applies to subsequent model turns.
- **composes**: [[Model_Slash_Command]], [[Status_Line_Slash_Command]]
- **confidence**: documented

### Personality_Slash_Command
- **surface**: `/personality`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17675` — “Use `/personality` to change how Codex communicates without rewriting your prompt”; lines 17685–17688 list `friendly`, `pragmatic`, and `none` and document model-dependent visibility.
- **does**: Changes the communication style for later responses in the active chat.
- **spark**: S=0 P=10 A=2 R=0 K=0
- **why**: P because the command directly changes interpersonal presentation; A because it changes response style without changing task instructions.
- **rent**: every_turn — the selected style shapes later responses.
- **composes**: [[Personality_Config]], [[Default_Model_Config]]
- **confidence**: documented

### Plan_Mode_Slash_Command
- **surface**: `/plan [prompt]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17690` — “Type `/plan` and press Enter to switch the active chat into plan mode”; lines 17694–17700 document inline prompts, attachments, and unavailability while Codex is already working.
- **does**: Switches the active chat into a planning-first execution mode.
- **spark**: S=1 P=2 A=10 R=0 K=0
- **why**: S because it enables explicit plan generation; P because the user selects when implementation is deferred; A because it changes the work method to planning-first.
- **rent**: every_turn — Plan mode governs subsequent turns until the mode changes.
- **composes**: [[Plan_Mode_Reasoning_Effort_Config]], [[Interactive_TUI_Command]]
- **confidence**: documented

### Chat_Compaction_Slash_Command
- **surface**: `/compact`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17970` — “Codex replaces earlier turns with a concise summary, freeing context while keeping critical details.”
- **does**: Replaces earlier visible turns with a context-preserving summary.
- **spark**: S=0 P=0 A=7 R=5 K=5
- **why**: A because it changes the context-management method; R because it frees context-window capacity; K because it retains a compressed representation of prior chat knowledge.
- **rent**: every_turn — the compacted summary occupies context on later turns.
- **composes**: [[Interactive_TUI_Command]], [[Session_Resume_Command]]
- **confidence**: documented

### Session_Status_Slash_Command
- **surface**: `/status`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17869` — “Review the output for the active model, approval policy, writable roots, and current token usage”; line 17874 adds remote address and server version for remote TUI connections.
- **does**: Displays the effective runtime configuration and current session capacity.
- **spark**: S=0 P=2 A=3 R=5 K=7
- **why**: P because approval policy visibility clarifies authority; A because the summary supports runtime verification; R because it reveals writable roots and remaining capacity; K because it reports active configuration.
- **rent**: none — status is read only and produced on demand.
- **composes**: [[Model_Slash_Command]], [[Working_Directory_Flag]], [[Approval_Policy]]
- **confidence**: documented

### Config_Diagnostics_Slash_Command
- **surface**: `/debug-config`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17889` — “Review the output for config layer order (lowest precedence first), on/off state, and policy sources”; line 17899 says it explains effective-setting differences.
- **does**: Prints configuration-layer and policy-source diagnostics for the active session.
- **spark**: S=0 P=2 A=4 R=4 K=9
- **why**: P because policy-source reporting exposes who controls behavior; A because it supports precedence debugging; R because it reveals configured subsystems; K because it reports effective layers and constraints.
- **rent**: none — diagnostics are generated only when requested.
- **composes**: [[Config_Layer_Precedence]], [[Session_Status_Slash_Command]], [[Doctor_Command]]
- **confidence**: documented

### Status_Line_Slash_Command
- **surface**: `/statusline`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17901` — “The footer status line updates immediately and persists to `tui.status_line` in `config.toml`”; lines 17909–17911 enumerate model, context, limits, Git, token, session, directory, and version items.
- **does**: Selects and orders persistent informational fields in the TUI footer.
- **spark**: S=0 P=0 A=2 R=5 K=4
- **why**: A because it customizes monitoring workflow; R because it exposes session resources in the footer; K because it surfaces runtime state.
- **rent**: every_turn — selected fields are rendered throughout later TUI turns.
- **composes**: [[Fast_Mode_Slash_Command]], [[Session_Status_Slash_Command]]
- **confidence**: documented

### Keymap_Slash_Command
- **surface**: `/keymap`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17940` — “Use `/keymap` to inspect, update, and persist keyboard shortcut bindings for the TUI”; line 17948 says changes write to `tui.keymap` in `config.toml`.
- **does**: Interactively remaps persistent TUI keyboard shortcuts.
- **spark**: S=0 P=0 A=5 R=5 K=1
- **why**: A because it changes the user's control method; R because it maps keys to TUI capabilities; K because it exposes current bindings.
- **rent**: none — persisted bindings have no documented recurring agent charge.
- **composes**: [[TUI_Keymap_Config]], [[Interactive_TUI_Command]]
- **confidence**: documented

### New_Chat_Slash_Command
- **surface**: `/new [name]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:17993` — “Codex starts a fresh chat in the same CLI session”; lines 18000–18002 document optional naming and distinguish it from `/clear`.
- **does**: Starts a new chat without leaving the current CLI process.
- **spark**: S=0 P=1 A=6 R=3 K=0
- **why**: P because the user establishes a fresh interaction boundary; A because it resets task context while retaining the terminal session; R because it creates a new session record.
- **rent**: none — chat creation is a one-time operation.
- **composes**: [[Interactive_TUI_Command]], [[Session_Resume_Command]]
- **confidence**: documented

### Side_Chat_Slash_Command
- **surface**: `/side [prompt]` / `/btw [prompt]`
- **evidence**: `C:\Users\Darian\AppData\Local\Temp\openai-docs-cache\codex-manual.md:18038` — “Use `/side` to start an ephemeral fork from the current chat without switching away from the main chat”; lines 18046–18050 describe its separate transcript and availability limits.
- **does**: Opens an ephemeral branch for a focused detour from the main chat.
- **spark**: S=0 P=2 A=10 R=3 K=2
- **why**: P because the user can ask a detour without redirecting the main interaction; A because it enables parallel conversational exploration; R because it creates a separate transcript; K because the branch inherits parent context.
- **rent**: every_turn — side-chat turns consume their own model usage while active.
- **composes**: [[Session_Fork_Command]], [[Interactive_TUI_Command]]
- **confidence**: documented

## Uncovered
- No CLI or TUI behavior was exercised because this arm was explicitly documentary; every behavioral primitive remains `documented`, not `observed`.
- Exhaustive normalization of lower-materiality flags, cosmetic slash commands, installer-only variables, and authentication variants was not reached in order to keep the arm bounded to the most material directly evidenced primitives.
- Hooks, approval/sandbox security depth, skills, plugins, MCP, app-server, SDK, and noninteractive execution were intentionally excluded because they belong to D2, D4/D5, or D6.
