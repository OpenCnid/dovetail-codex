### PowerShell_Get_Content_Raw_File_Read
- **surface**: `Get-Content -Raw -LiteralPath <absolute-path>`
- **evidence**: `C:\Users\Darian\Desktop\codex\spark-probe\assets\probe-brief.md` at probe commit `744846342d33dbe4fd0d5ad324d738a657e61c9f` — under Codex Desktop 26.820.9563.0 / codex-cli 0.150.0-alpha.8, PowerShell 7.6.4 read 4,839 characters and returned the exact opening heading on Windows 10.0.26200.
- **does**: Reads one complete text file from a literal local path.
- **spark**: S=1 P=0 A=0 R=7 K=0
- **why**: S permits exact text ingestion; R exposes local filesystem contents.
- **rent**: none — the read leaves no installed or recurring charge for the agent or user.
- **composes**: [[Exec_Command_Tool]], [[Filesystem_Read_Authority]]
- **confidence**: observed

### Apply_Patch_Create_File
- **surface**: `*** Add File: <path>` inside `apply_patch`
- **evidence**: `C:\Users\Darian\Desktop\codex\spark-probe\runs\2026-09-02-codex\waves\I1-file-and-search-tools.md` — the session's freeform `apply_patch` call created this file under Codex Desktop 26.820.9563.0; official schema also describes file creation at `https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses`.
- **does**: Creates a new local text file from a patch document.
- **spark**: S=5 P=0 A=3 R=7 K=0
- **why**: S authors a persistent artifact; A uses a structured diff workflow; R reaches writable workspace state.
- **rent**: none — creation changes the requested file once without an ongoing agent or user charge.
- **composes**: [[Filesystem_Write_Authority]], [[Apply_Patch_Freeform_Input]]
- **confidence**: observed

### Apply_Patch_Update_File
- **surface**: `*** Update File: <path>` inside `apply_patch`
- **evidence**: `C:\Users\Darian\Desktop\codex\spark-probe\runs\2026-09-02-codex\waves\I1-file-and-search-tools.md` — a follow-up `*** Update File` hunk replaced this evidence line in the same Codex Desktop 26.820.9563.0 session; the official schema describes updating files at `https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses`.
- **does**: Replaces matched hunks in an existing local text file.
- **spark**: S=6 P=0 A=4 R=7 K=0
- **why**: S performs targeted source modification; A applies contextual hunks; R mutates reachable workspace state.
- **rent**: none — the update has no recurring agent or user charge after application.
- **composes**: [[Filesystem_Write_Authority]], [[Apply_Patch_Freeform_Input]]
- **confidence**: observed

### Apply_Patch_Freeform_Input
- **surface**: `apply_patch(<raw patch text>)`
- **evidence**: `C:\Users\Darian\Desktop\codex\spark-probe\runs\2026-09-02-codex\waves\I1-file-and-search-tools.md` — the Codex Desktop 26.820.9563.0 session schema labels `apply_patch` FREEFORM, and the accepted create call used raw patch text without a JSON wrapper.
- **does**: Accepts a patch document as direct tool input.
- **spark**: S=1 P=0 A=6 R=3 K=0
- **why**: S enables diff submission; A determines the edit invocation method; R connects patch text to the filesystem editor.
- **rent**: none — the input convention adds no continuing charge for the agent or user.
- **composes**: [[Apply_Patch_Create_File]], [[Apply_Patch_Update_File]]
- **confidence**: observed

### Ripgrep_Content_Search
- **surface**: `rg -n --fixed-strings <pattern> <path>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\69b0fa6fcdec2587\rg.exe` — bundled ripgrep 15.2.0 returned `1:# Atomic conceptual primitive — emission schema` for the exact pattern in `C:\Users\Darian\Desktop\codex\spark-probe\references\emission-schema.md` at probe commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`.
- **does**: Locates exact text occurrences inside local files.
- **spark**: S=3 P=0 A=2 R=8 K=0
- **why**: S performs targeted content matching; A narrows inspection before reading; R exposes matching local content.
- **rent**: none — each read-only search ends without an installed or recurring agent or user charge.
- **composes**: [[Exec_Command_Tool]], [[PowerShell_Get_Content_Raw_File_Read]]
- **confidence**: observed

### Ripgrep_Path_Search
- **surface**: `rg --files <root>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\69b0fa6fcdec2587\rg.exe` — bundled ripgrep 15.2.0 enumerated the probe repository's file paths at commit `744846342d33dbe4fd0d5ad324d738a657e61c9f` in the Codex Desktop 26.820.9563.0 session.
- **does**: Enumerates searchable file paths beneath a local root.
- **spark**: S=2 P=0 A=2 R=7 K=0
- **why**: S discovers candidate inputs; A supports inspect-before-open sequencing; R exposes the local path set.
- **rent**: none — enumeration leaves no installed or recurring agent or user charge.
- **composes**: [[Exec_Command_Tool]], [[Ripgrep_Glob_Filter]]
- **confidence**: observed

### Ripgrep_Glob_Filter
- **surface**: `rg --files <root> -g <include> -g <exclude>`
- **evidence**: `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\69b0fa6fcdec2587\rg.exe` — `-g '*.md' -g '!runs/2026-07-28/**' -g '!runs/2026-09-02-codex/**'` returned six Markdown paths at probe commit `744846342d33dbe4fd0d5ad324d738a657e61c9f` while excluding both run trees with ripgrep 15.2.0.
- **does**: Restricts path enumeration through ordered glob rules.
- **spark**: S=2 P=0 A=4 R=5 K=0
- **why**: S selects relevant path classes; A constrains search scope before inspection; R filters the reachable path listing.
- **rent**: none — glob filtering adds no persistent agent or user charge.
- **composes**: [[Ripgrep_Path_Search]], [[Exec_Command_Tool]]
- **confidence**: observed

### View_Image_Local_File
- **surface**: `view_image({ path: <absolute-local-path> })`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-primary-runtime\documents\26.826.12353\assets\icon.png` — `view_image` rendered the blue document icon from this local PNG in Codex Desktop 26.820.9563.0.
- **does**: Exposes a local raster image for visual inspection.
- **spark**: S=3 P=0 A=0 R=8 K=0
- **why**: S enables visual examination; R exposes local image pixels to the agent.
- **rent**: none — inspection leaves no installed or recurring agent or user charge.
- **composes**: [[Filesystem_Read_Authority]], [[View_Image_Detail_Control]]
- **confidence**: observed

### View_Image_Detail_Control
- **surface**: `detail: "high" | "original"` in `view_image`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-primary-runtime\documents\26.826.12353\assets\icon.png` — the Codex Desktop 26.820.9563.0 tool returned `detail: "high"` when omitted and `detail: "original"` when explicitly requested; the session schema states that `original` preserves exact resolution.
- **does**: Selects the resolution treatment for local-image inspection.
- **spark**: S=1 P=0 A=3 R=5 K=0
- **why**: S tunes visual fidelity; A chooses the inspection strategy; R controls pixel-detail reach.
- **rent**: none — the per-call detail choice creates no recurring agent or user charge.
- **composes**: [[View_Image_Local_File]]
- **confidence**: observed

## Uncovered
- No standalone `read_file`, `write_file`, `search_files`, or `find_files` tool was exposed in the live namespace; local text reads and searches therefore used execution-backed PowerShell 7.6.4 and bundled ripgrep 15.2.0 without emitting command-execution primitives.
- Patch deletion was not exercised because creating the assigned wave file was the only permitted state change; no deletion primitive is emitted from recall.
- `runs/2026-07-28` was deliberately excluded from path searches and was not inspected.
