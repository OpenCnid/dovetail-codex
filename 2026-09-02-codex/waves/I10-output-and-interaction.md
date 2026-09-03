# I10 Output and User Interaction

Target: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; config root `C:\Users\Darian\.codex`; surveyed 2026-09-02; probe repository commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`.

### Commentary_Progress_Channel
- **surface**: assistant message with `channel: commentary`
- **evidence**: `session://codex-desktop/26.820.9563.0/interaction-contract` — The live delegated-session contract assigns ongoing updates to `commentary`; this arm emitted commentary before its first tool call and while surveying.
- **does**: Delivers concise progress updates while work remains active.
- **spark**: S=0 P=8 A=5 R=1 K=0
- **why**: P via continuous user-facing presence; A via visible progress checkpoints; R via a dedicated output channel.
- **rent**: every_turn — the interaction policy occupies agent context and may add progress-output tokens.
- **composes**: [[Final_Response_Channel]], [[Midturn_User_Steering]], [[Exec_Incremental_Yield_Helper]]
- **confidence**: observed

### Final_Response_Channel
- **surface**: assistant message with `channel: final`
- **evidence**: `session://codex-desktop/26.820.9563.0/interaction-contract` — The live contract says `final` yields to the user, ends the turn, and must remain self-contained because commentary is collapsed afterward.
- **does**: Returns the task outcome in a turn-ending self-contained response.
- **spark**: S=0 P=8 A=4 R=1 K=0
- **why**: P via explicit handoff to the user; A via a terminal response boundary; R via a dedicated output channel.
- **rent**: every_turn — every completed turn pays final-response tokens.
- **composes**: [[Commentary_Progress_Channel]], [[Blocking_Question_Final_Channel]], [[GitHub_Flavored_Markdown_Response]]
- **confidence**: documented

### Midturn_User_Steering
- **surface**: user message received while the assistant is working
- **evidence**: `session://codex-desktop/26.820.9563.0/interaction-contract` — The live contract requires new input to be classified as replacement, addition, or status question before work continues.
- **does**: Lets new user input redirect an active turn.
- **spark**: S=0 P=9 A=7 R=1 K=0
- **why**: P via user authority over active work; A via runtime replanning; R via an inbound midturn channel.
- **rent**: every_matching_call — only a midturn user message triggers reclassification and replanning.
- **composes**: [[Commentary_Progress_Channel]], [[Final_Response_Channel]]
- **confidence**: documented

### Blocking_Question_Final_Channel
- **surface**: clarifying or blocking question in `final`
- **evidence**: `session://codex-desktop/26.820.9563.0/interaction-contract` — The live contract forbids putting a final blocking question in commentary and reserves it for the final channel.
- **does**: Returns control to the user when continuation requires their answer.
- **spark**: S=0 P=9 A=5 R=0 K=0
- **why**: P via explicit user decision authority; A via a hard continuation gate.
- **rent**: every_matching_call — the gate consumes a turn only when user input is required.
- **composes**: [[Final_Response_Channel]], [[Structured_User_Input_Tool]]
- **confidence**: documented

### GitHub_Flavored_Markdown_Response
- **surface**: GitHub-flavored Markdown in assistant output
- **evidence**: `session://codex-desktop/26.820.9563.0/app-context` — The live app contract says responses may use GitHub-flavored Markdown and defines renderer-specific link and media conventions.
- **does**: Formats user-facing responses with the app's Markdown renderer.
- **spark**: S=1 P=3 A=1 R=3 K=0
- **why**: S via structured response composition; P via readable presentation; A via a common rendering method; R via the Markdown renderer.
- **rent**: every_turn — rendering guidance occupies the interaction prompt each turn.
- **composes**: [[Local_File_Markdown_Link]], [[Local_Media_Markdown_Rendering]], [[Web_URL_Markdown_Link]]
- **confidence**: documented

### Local_File_Markdown_Link
- **surface**: `[label](/absolute/path/file.ext:line)`
- **evidence**: `session://codex-desktop/26.820.9563.0/app-context` — The live contract requires absolute local-file targets, permits an optional line number, and requires angle brackets around targets containing spaces.
- **does**: Makes a local workspace file clickable at an optional line.
- **spark**: S=0 P=2 A=2 R=6 K=0
- **why**: P via a direct user handoff; A via precise artifact addressing; R via clickable local-file reach.
- **rent**: every_matching_call — link text and target are emitted only when a local artifact is referenced.
- **composes**: [[GitHub_Flavored_Markdown_Response]], [[Codex_File_Panel]]
- **confidence**: documented

### Local_Media_Markdown_Rendering
- **surface**: `![alt](/absolute/path/to/media.ext)`
- **evidence**: `session://codex-desktop/26.820.9563.0/app-context` — The live contract routes local image, video, and audio display through Markdown image syntax and requires an absolute filesystem path.
- **does**: Renders a local media artifact inline from an absolute path.
- **spark**: S=1 P=3 A=2 R=7 K=0
- **why**: S via media presentation; P via inline user-facing delivery; A via one absolute-path convention; R via local media reach.
- **rent**: every_matching_call — media markup is emitted only when a local artifact is displayed.
- **composes**: [[GitHub_Flavored_Markdown_Response]], [[Exec_Image_Output_Helper]], [[Exec_Audio_Output_Helper]]
- **confidence**: documented

### Web_URL_Markdown_Link
- **surface**: `[label](https://example.com)`
- **evidence**: `session://codex-desktop/26.820.9563.0/app-context` — The live contract directs web URLs to be returned as Markdown links.
- **does**: Presents a web destination as a clickable labeled link.
- **spark**: S=0 P=2 A=1 R=5 K=0
- **why**: P via legible user presentation; A via a standard citation form; R via clickable web reach.
- **rent**: every_matching_call — the link is emitted only when a web destination is returned.
- **composes**: [[GitHub_Flavored_Markdown_Response]], [[Codex_Browser_Panel]]
- **confidence**: documented

### Exec_Text_Output_Helper
- **surface**: `text(value)` inside `functions.exec`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema says `text` appends a text item; this arm exercised it to return filesystem and tool-catalog results.
- **does**: Appends one scalar value to an exec call's output stream.
- **spark**: S=1 P=0 A=3 R=6 K=0
- **why**: S via programmatic output composition; A via ordered result assembly; R via the exec result stream.
- **rent**: every_matching_call — each appended item consumes tool-output capacity.
- **composes**: [[Exec_Incremental_Yield_Helper]], [[Exec_Notify_Helper]]
- **confidence**: observed

### Exec_Image_Output_Helper
- **surface**: `image(imageUrlOrItem, detail?)` inside `functions.exec`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema accepts a data URL, an image-content block, or an image object and appends an image item.
- **does**: Appends one image item to an exec result.
- **spark**: S=1 P=0 A=2 R=8 K=0
- **why**: S via multimodal result composition; A via in-script output assembly; R via an image-bearing result channel.
- **rent**: every_matching_call — each image consumes tool-output and model-input capacity.
- **composes**: [[Exec_Image_Detail_Override]], [[Generated_Image_Result_Helper]], [[Local_Media_Markdown_Rendering]]
- **confidence**: documented

### Exec_Image_Detail_Override
- **surface**: `detail: "auto" | "low" | "high" | "original"`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema exposes four detail levels and says an explicit second argument overrides detail embedded in the image item.
- **does**: Selects the fidelity used when forwarding an image item.
- **spark**: S=0 P=0 A=5 R=5 K=0
- **why**: A via per-item fidelity selection; R via control over image-resolution consumption.
- **rent**: every_matching_call — higher-fidelity forwarding can consume more multimodal context.
- **composes**: [[Exec_Image_Output_Helper]]
- **confidence**: documented

### Exec_Audio_Output_Helper
- **surface**: `audio(audioUrlOrItem)` inside `functions.exec`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema accepts a data URL, an audio-content block, or an audio object and appends an audio item.
- **does**: Appends one audio item to an exec result.
- **spark**: S=1 P=0 A=2 R=8 K=0
- **why**: S via multimodal result composition; A via in-script output assembly; R via an audio-bearing result channel.
- **rent**: every_matching_call — each audio item consumes tool-output and model-input capacity.
- **composes**: [[Local_Media_Markdown_Rendering]]
- **confidence**: documented

### Generated_Image_Result_Helper
- **surface**: `generatedImage({ image_url, output_hint? })` inside `functions.exec`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema says the helper appends an image-generation result and optional output hint and rejects HTTP(S) image URLs.
- **does**: Delivers an image-generation result from a non-HTTP image URL.
- **spark**: S=2 P=1 A=3 R=9 K=0
- **why**: S via generated-artifact delivery; P via a user-facing output hint; A via typed result routing; R via the generated-image display surface.
- **rent**: every_matching_call — each generated image consumes generation-result and multimodal capacity.
- **composes**: [[Exec_Image_Output_Helper]], [[Remote_Media_Preview_Routing]]
- **confidence**: documented

### Remote_Media_Preview_Routing
- **surface**: app or connector `preview` / `display` tool for generated media at a remote URL
- **evidence**: `session://codex-desktop/26.820.9563.0/app-context` — The live contract requires the generating app's preview or display tool for remote media instead of embedding the remote URL in Markdown.
- **does**: Routes remotely generated media through its provider's display surface.
- **spark**: S=0 P=2 A=7 R=6 K=0
- **why**: P via app-native user presentation; A via provider-aware output routing; R via the provider's preview surface.
- **rent**: every_matching_call — the provider display tool is invoked only for matching remote media.
- **composes**: [[Generated_Image_Result_Helper]], [[Local_Media_Markdown_Rendering]]
- **confidence**: documented

### Exec_Notify_Helper
- **surface**: `notify(value)` inside `functions.exec`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema says `notify` immediately injects an extra `custom_tool_call_output` and stringifies values like `text`.
- **does**: Emits an immediate custom output event from an active exec call.
- **spark**: S=0 P=6 A=6 R=5 K=0
- **why**: P via an immediate visible event; A via out-of-band progress signaling; R via a custom tool-output channel.
- **rent**: every_matching_call — each notification adds a tool-output event.
- **composes**: [[Exec_Text_Output_Helper]], [[Exec_Incremental_Yield_Helper]], [[Commentary_Progress_Channel]]
- **confidence**: documented

### Exec_Incremental_Yield_Helper
- **surface**: `yield_control()` inside `functions.exec`
- **evidence**: `tool://functions.exec` — The live Codex Desktop 26.820.9563.0 schema says the helper yields accumulated output immediately while the script keeps running.
- **does**: Flushes accumulated exec output before script completion.
- **spark**: S=0 P=3 A=8 R=5 K=0
- **why**: P via earlier progress visibility; A via incremental long-call delivery; R via a partial-result channel.
- **rent**: every_matching_call — each flush adds an intermediate output delivery.
- **composes**: [[Exec_Text_Output_Helper]], [[Exec_Notify_Helper]], [[Commentary_Progress_Channel]]
- **confidence**: documented

### Structured_User_Input_Tool
- **surface**: `request_user_input({ questions: [...] })`
- **evidence**: `tool://functions.request_user_input` — The live Codex Desktop 26.820.9563.0 schema permits one to three short questions in Plan mode, requires two or three mutually exclusive choices, and adds a free-form Other choice automatically.
- **does**: Presents a bounded structured choice request to the user.
- **spark**: S=0 P=10 A=7 R=4 K=0
- **why**: P via explicit user decision authority; A via choice-gated planning; R via a structured response widget.
- **rent**: every_matching_call — each request consumes user attention and a continuation boundary.
- **composes**: [[Blocking_Question_Final_Channel]], [[Midturn_User_Steering]]
- **confidence**: documented

### Command_Approval_Question
- **surface**: `exec_command({ sandbox_permissions: "require_escalated", justification })`
- **evidence**: `tool://functions.exec_command` — The live Codex Desktop 26.820.9563.0 / codex-cli 0.150.0-alpha.8 schema defines `justification` as the user-facing approval question for an unsandboxed command.
- **does**: Requests user authorization for one unsandboxed command.
- **spark**: S=0 P=10 A=5 R=3 K=0
- **why**: P via user control over command authority; A via an execution gate; R via conditional unsandboxed reach.
- **rent**: every_matching_call — each escalated command may incur an approval interaction.
- **composes**: [[Reusable_Command_Approval_Prefix]], [[Never_Approval_Policy]]
- **confidence**: documented

### Reusable_Command_Approval_Prefix
- **surface**: `prefix_rule: ["command", "prefix"]`
- **evidence**: `tool://functions.exec_command` — The live Codex Desktop 26.820.9563.0 / codex-cli 0.150.0-alpha.8 schema exposes a reusable approval prefix only with `sandbox_permissions: "require_escalated"`.
- **does**: Extends one command approval to later commands sharing an exact prefix.
- **spark**: S=0 P=9 A=7 R=2 K=0
- **why**: P via reusable delegated authority; A via prefix-based approval reuse; R via conditional command reach.
- **rent**: every_matching_call — the prefix rule is evaluated for each later matching command.
- **composes**: [[Command_Approval_Question]], [[Never_Approval_Policy]]
- **confidence**: documented

### Delegated_Never_Approval_Policy
- **surface**: `approval policy: never`
- **evidence**: `session://codex-desktop/26.820.9563.0/permissions` — This delegated session's live permission contract states `Approval policy is currently never`, forbids supplying `sandbox_permissions`, and says such commands will be rejected.
- **does**: Suppresses interactive command-approval requests in this session.
- **spark**: S=0 P=10 A=6 R=1 K=0
- **why**: P via removal of agent authority to solicit escalation; A via fail-closed execution routing; R via constrained command reach.
- **rent**: every_matching_call — the policy is checked when a command would seek escalation.
- **composes**: [[Command_Approval_Question]], [[Reusable_Command_Approval_Prefix]]
- **confidence**: documented

### Codex_File_Panel
- **surface**: `open_in_codex({ target: { type: "file", path, line? }, placement? })`
- **evidence**: `tool://mcp__codex_app.open_in_codex` — The live Codex Desktop 26.820.9563.0 schema opens a workspace file in a Codex panel and accepts an optional line number.
- **does**: Opens a local file at an optional line in a Codex panel.
- **spark**: S=1 P=2 A=3 R=8 K=0
- **why**: S via artifact inspection; P via direct UI presentation; A via line-targeted handoff; R via the Codex file viewer.
- **rent**: every_matching_call — each invocation creates or focuses a panel tab.
- **composes**: [[Codex_Panel_Placement]], [[Cross_Thread_Panel_Delivery]], [[Local_File_Markdown_Link]]
- **confidence**: documented

### Codex_Browser_Panel
- **surface**: `open_in_codex({ target: { type: "browser", url? | tabId? }, placement? })`
- **evidence**: `tool://mcp__codex_app.open_in_codex` — The live Codex Desktop 26.820.9563.0 schema opens a URL or existing browser tab in a Codex panel.
- **does**: Opens a browser destination in a Codex panel.
- **spark**: S=0 P=2 A=3 R=8 K=0
- **why**: P via direct UI presentation; A via URL-or-tab addressing; R via the in-app browser panel.
- **rent**: every_matching_call — each invocation creates or focuses a browser panel tab.
- **composes**: [[Codex_Panel_Placement]], [[Cross_Thread_Panel_Delivery]], [[Web_URL_Markdown_Link]]
- **confidence**: documented

### Codex_Terminal_Panel
- **surface**: `open_in_codex({ target: { type: "terminal", sessionId? }, placement? })`
- **evidence**: `tool://mcp__codex_app.open_in_codex` — The live Codex Desktop 26.820.9563.0 schema opens a local thread's terminal, optionally by session ID, in a Codex panel.
- **does**: Opens a local terminal session in a Codex panel.
- **spark**: S=1 P=2 A=3 R=8 K=0
- **why**: S via terminal-state inspection; P via direct UI presentation; A via session-addressed handoff; R via the terminal panel.
- **rent**: every_matching_call — each invocation creates or focuses a terminal panel tab.
- **composes**: [[Codex_Panel_Placement]], [[Cross_Thread_Panel_Delivery]]
- **confidence**: documented

### Codex_Review_Panel
- **surface**: `open_in_codex({ target: { type: "review", view?, path?, baseBranch? }, placement? })`
- **evidence**: `tool://mcp__codex_app.open_in_codex` — The live Codex Desktop 26.820.9563.0 schema exposes `last-turn`, `branch`, `unstaged`, and `staged` review views and requires a resolvable revision for `baseBranch` comparisons.
- **does**: Opens a selected repository-change view in a Codex review panel.
- **spark**: S=1 P=2 A=6 R=8 K=0
- **why**: S via change inspection; P via direct UI presentation; A via review-scope selection; R via the Codex review surface.
- **rent**: every_matching_call — each invocation creates or focuses a review panel tab.
- **composes**: [[Codex_Panel_Placement]], [[Cross_Thread_Panel_Delivery]], [[Inline_Code_Comment_Directive]]
- **confidence**: documented

### Codex_Panel_Placement
- **surface**: `placement: "right" | "bottom"`
- **evidence**: `tool://mcp__codex_app.open_in_codex` — The live Codex Desktop 26.820.9563.0 schema exposes right-side or bottom placement for file, browser, terminal, and review panels.
- **does**: Selects where a Codex panel opens.
- **spark**: S=0 P=3 A=5 R=2 K=0
- **why**: P via user-visible layout choice; A via per-open presentation routing; R via two panel regions.
- **rent**: every_matching_call — placement is applied only when opening a panel.
- **composes**: [[Codex_File_Panel]], [[Codex_Browser_Panel]], [[Codex_Terminal_Panel]], [[Codex_Review_Panel]]
- **confidence**: documented

### Cross_Thread_Panel_Delivery
- **surface**: `open_in_codex({ threadId, target })`
- **evidence**: `tool://mcp__codex_app.open_in_codex` — The live Codex Desktop 26.820.9563.0 schema defaults to the calling task; an explicitly targeted hidden task queues the tab until that task is shown in the same window without navigating there.
- **does**: Routes a panel tab to an explicitly selected Codex task.
- **spark**: S=0 P=7 A=6 R=5 K=0
- **why**: P via explicit cross-task UI authority; A via task-scoped delivery; R via another task's panel host.
- **rent**: every_matching_call — each cross-task delivery creates or queues one tab.
- **composes**: [[Codex_File_Panel]], [[Codex_Browser_Panel]], [[Codex_Terminal_Panel]], [[Codex_Review_Panel]], [[Codex_Task_Navigation]]
- **confidence**: documented

### Codex_Task_Navigation
- **surface**: `navigate_to_codex_page({ threadId })`
- **evidence**: `tool://mcp__codex_app.navigate_to_codex_page` — The live Codex Desktop 26.820.9563.0 schema navigates the most recently focused main app window to a named task or chat only when the user asks to open or show it.
- **does**: Navigates the main Codex window to a selected task.
- **spark**: S=0 P=8 A=4 R=4 K=0
- **why**: P via user-authorized visible navigation; A via explicit task selection; R via access to the main-window task route.
- **rent**: every_matching_call — each invocation changes the visible task route.
- **composes**: [[Cross_Thread_Panel_Delivery]], [[Immutable_Task_Share_Link]]
- **confidence**: documented

### Immutable_Task_Share_Link
- **surface**: `share_thread({ threadId?, hostId? })`
- **evidence**: `tool://mcp__codex_app.share_thread` — The live Codex Desktop 26.820.9563.0 schema creates an immutable share link for the current or another accessible task and can discover accessible tasks across hosts.
- **does**: Creates an immutable external share link for an accessible Codex task.
- **spark**: S=0 P=9 A=2 R=7 K=0
- **why**: P via authority to expose a task externally; A via optional task and host targeting; R via a durable share URL.
- **rent**: every_matching_call — each invocation creates a persistent externally consumable link.
- **composes**: [[Final_Response_Channel]], [[Codex_Task_Navigation]]
- **confidence**: documented

### Inline_Code_Comment_Directive
- **surface**: `::code-comment{title="..." body="..." file="/absolute/path" start=N end=N priority=0..3}`
- **evidence**: `session://codex-desktop/26.820.9563.0/app-context` — The live app contract defines one directive per actionable inline comment, requires title, body, and file, and permits tight one-based line ranges plus priority 0–3.
- **does**: Attaches actionable review feedback to a precise code location.
- **spark**: S=1 P=8 A=5 R=4 K=0
- **why**: S via structured review annotation; P via direct feedback to the user; A via line-scoped issue reporting; R via the inline review UI.
- **rent**: every_matching_call — each actionable finding adds one rendered review annotation.
- **composes**: [[Codex_Review_Panel]], [[Local_File_Markdown_Link]], [[Final_Response_Channel]]
- **confidence**: documented

## Uncovered
- `request_user_input` was not exercised because it is Plan-mode-only and this probe was forbidden to solicit input merely for testing.
- Approval prompts and reusable prefix grants were not exercised because this delegated session's `never` approval policy rejects escalation requests.
- File, browser, terminal, review, cross-task panel, navigation, and share mutations were not exercised; their live schemas were sufficient, and the probe forbade consequential interaction with other user-owned tasks.
- `notify()` was present only as an exec `custom_tool_call_output` injector; no general Codex Desktop toast, operating-system notification, or notification-center API was exposed in this session.
- Automation notification policy belongs to I11, task listing/history/persistence belongs to I8, and browser page operation belongs to I9; those adjacent surfaces were deliberately excluded.
- No audio-generation tool or remote generated-audio preview tool was exposed; only generic audio-result forwarding and absolute-path local audio rendering were found.
