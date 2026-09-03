# I9 Web, Browser, and Outward Reach

- **target**: Codex Desktop 26.820.9563.0; codex-cli 0.150.0-alpha.8; Windows NT 10.0.26200.0; config root `C:\Users\Darian\.codex`; probed 2026-09-02; repository commit `744846342d33dbe4fd0d5ad324d738a657e61c9f`

### Web_Search_Query
- **surface**: `web.run search_query[{q, domains?, recency?}]`
- **evidence**: `https://developers.openai.com/codex/use-cases` — On 2026-09-02, a scoped search for Codex browser/computer-use documentation returned ranked official pages before any page was opened.
- **does**: Searches the public web with optional domain and recency filters.
- **spark**: S=1 P=0 A=1 R=8 K=6
- **why**: S adds a retrieval operation; A supports source-first investigation; R reaches a public search index; K returns indexed web knowledge.
- **rent**: none — the read-only lookup installs no persistent component.
- **composes**: [[Web_Page_Open]], [[Web_Page_Find]]
- **confidence**: observed

### Web_Page_Open
- **surface**: `web.run open[{ref_id, lineno?}]`
- **evidence**: `https://learn.chatgpt.com/use-cases` — Opening the search result on 2026-09-02 returned addressable page lines and numbered links.
- **does**: Fetches a URL or prior web result into a line-addressable reading view.
- **spark**: S=1 P=0 A=1 R=8 K=5
- **why**: S adds page retrieval; A enables evidence inspection; R reaches public pages; K exposes page text.
- **rent**: none — the read-only fetch has no continuing charge after it returns.
- **composes**: [[Web_Page_Find]], [[Web_Link_Click]], [[Pdf_Page_Screenshot]]
- **confidence**: observed

### Web_Page_Find
- **surface**: `web.run find[{ref_id, pattern}]`
- **evidence**: `https://learn.chatgpt.com/use-cases` — Finding `Create browser-based games` on 2026-09-02 returned the matching passage with line locators.
- **does**: Locates a text pattern inside a fetched page.
- **spark**: S=1 P=0 A=3 R=3 K=4
- **why**: S adds in-page search; A supports targeted verification; R addresses fetched content; K isolates relevant text.
- **rent**: none — the lookup leaves no persistent state.
- **composes**: [[Web_Page_Open]]
- **confidence**: observed

### Web_Link_Click
- **surface**: `web.run click[{ref_id, id}]`
- **evidence**: `https://learn.chatgpt.com/use-cases/browser-games` — Clicking numbered link 492 on 2026-09-02 opened the linked browser-games page without a live browser session.
- **does**: Follows a numbered link from a fetched page.
- **spark**: S=1 P=0 A=2 R=7 K=4
- **why**: S adds link traversal; A supports evidence navigation; R reaches the linked resource; K exposes its content.
- **rent**: none — the navigation creates no durable agent state.
- **composes**: [[Web_Page_Open]], [[Web_Page_Find]]
- **confidence**: observed

### Pdf_Page_Screenshot
- **surface**: `web.run screenshot[{ref_id, pageno}]`
- **evidence**: `https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf` — Opening the one-page PDF and requesting page 0 on 2026-09-02 returned an image content block.
- **does**: Renders one indexed PDF page as an image.
- **spark**: S=2 P=0 A=1 R=6 K=2
- **why**: S adds visual PDF inspection; A supports layout verification; R reaches a selected document page; K exposes visual content.
- **rent**: none — the rendering call leaves no persistent component.
- **composes**: [[Web_Page_Open]]
- **confidence**: observed

### Finance_Market_Lookup
- **surface**: `web.run finance[{ticker, type, market?}]`
- **evidence**: `https://www.microsoft.com/en-us/Investor` — The 2026-09-02 `MSFT` equity lookup returned current price, change, intraday range, volume, market cap, P/E, EPS, and trade time.
- **does**: Retrieves a structured market snapshot for a named asset.
- **spark**: S=1 P=0 A=0 R=7 K=6
- **why**: S adds market lookup; R reaches finance data; K supplies structured asset facts.
- **rent**: none — the lookup installs nothing and has no continuing charge.
- **composes**: [[Web_Search_Query]]
- **confidence**: observed

### Weather_Forecast_Lookup
- **surface**: `web.run weather[{location, start?, duration?}]`
- **evidence**: `https://www.weather.gov/lot/` — A 2026-09-02 Chicago lookup returned current conditions and an hourly forecast for the requested day.
- **does**: Retrieves current conditions and a bounded forecast for a location.
- **spark**: S=1 P=0 A=0 R=7 K=6
- **why**: S adds weather lookup; R reaches forecast data; K supplies time-bounded conditions.
- **rent**: none — the lookup leaves no persistent state.
- **composes**: [[Web_Search_Query]]
- **confidence**: observed

### Sports_Standings_Lookup
- **surface**: `web.run sports[{tool:"sports", fn:"standings", league, ...}]`
- **evidence**: `https://www.nba.com/standings` — A 2026-09-02 NBA standings call returned Eastern and Western conference records.
- **does**: Retrieves structured standings for a supported sports league.
- **spark**: S=1 P=0 A=0 R=7 K=6
- **why**: S adds standings lookup; R reaches sports data; K supplies league records.
- **rent**: none — the lookup leaves no persistent state.
- **composes**: [[Web_Search_Query]]
- **confidence**: observed

### Utc_Offset_Time_Lookup
- **surface**: `web.run time[{utc_offset}]`
- **evidence**: `https://www.timeanddate.com/time/zone/timezone/utc-5` — The `-05:00` lookup returned `Sep 2, 2026, 1:20:11 PM` during this run.
- **does**: Resolves the current civil time at a UTC offset.
- **spark**: S=1 P=0 A=0 R=4 K=4
- **why**: S adds time resolution; R reaches a clock source; K supplies current offset time.
- **rent**: none — the lookup leaves no persistent state.
- **composes**: [[Weather_Forecast_Lookup]]
- **confidence**: observed

### In_App_Browser_Selector
- **surface**: `agent.browsers.get("iab")`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — Codex Desktop 26.820.9563.0 selected `Codex In-app Browser` and returned its live API documentation on 2026-09-02.
- **does**: Selects the Codex-hosted browser as a controllable live-browser backend.
- **spark**: S=2 P=2 A=4 R=9 K=1
- **why**: S enables browser automation; P binds actions to a user-visible session; A routes work to an explicit browser family; R reaches a live browser; K exposes its control schema.
- **rent**: every_matching_call — a browser-control task pays skill and bootstrap context; no user fee was established.
- **composes**: [[Browser_User_Tab_Claiming]], [[Browser_Playwright_DOM_Inspection]], [[Browser_Temporary_Tab_Lifecycle]]
- **confidence**: observed

### Browser_User_Tab_Claiming
- **surface**: `browser.user.openTabs()` then `browser.user.claimTab(tab)`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The selected IAB API documents enumeration of user-owned top-level tabs and explicit claiming of one returned tab; neither method was invoked.
- **does**: Converts a selected user-owned browser tab into a controllable agent tab.
- **spark**: S=2 P=7 A=3 R=9 K=2
- **why**: S enables tab automation; P governs takeover of user session state; A requires an explicit claim workflow; R reaches an existing browser tab; K can expose visible page state.
- **rent**: every_matching_call — claiming requires live browser-control context for that task.
- **composes**: [[In_App_Browser_Selector]], [[Browser_Playwright_DOM_Inspection]]
- **confidence**: documented

### Browser_Playwright_DOM_Inspection
- **surface**: `tab.playwright.domSnapshot()` and locator read methods
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB API lists DOM snapshots, semantic locators, visibility, text, attributes, and read-only evaluation; these page methods were not invoked.
- **does**: Inspects a live page through semantic DOM state.
- **spark**: S=6 P=0 A=4 R=8 K=4
- **why**: S adds structured browser inspection; A favors semantic targeting; R reaches live DOM state; K reveals visible page content.
- **rent**: every_matching_call — page inspection requires an active browser task.
- **composes**: [[Browser_Dom_CUA_Control]], [[Browser_Console_Log_Read]]
- **confidence**: documented

### Browser_Dom_CUA_Control
- **surface**: `tab.dom_cua.{get_visible_dom,click,double_click,keypress,scroll,type}`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB API documents node-id UI control over the visible DOM; no input method was invoked.
- **does**: Drives browser UI elements by visible DOM node identifiers.
- **spark**: S=7 P=3 A=5 R=8 K=1
- **why**: S enables browser interaction; P can act in the user's session; A uses DOM-grounded control; R reaches interactive page state; K exposes node metadata.
- **rent**: every_matching_call — control requires an active browser task and its safety policy.
- **composes**: [[Browser_Playwright_DOM_Inspection]], [[Browser_Coordinate_CUA_Control]]
- **confidence**: documented

### Browser_Coordinate_CUA_Control
- **surface**: `tab.cua.{click,double_click,drag,keypress,move,scroll,type}`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB API documents pointer, keyboard, drag, and scroll operations in viewport coordinates; none was invoked.
- **does**: Drives a live browser page through coordinate-level input.
- **spark**: S=7 P=3 A=3 R=8 K=0
- **why**: S enables low-level browser interaction; P can act in the user's session; A provides a fallback interaction method; R reaches the rendered viewport.
- **rent**: every_matching_call — control requires an active browser task and its safety policy.
- **composes**: [[Browser_Tab_Screenshot]], [[Browser_Dom_CUA_Control]]
- **confidence**: documented

### Browser_Tab_Screenshot
- **surface**: `tab.screenshot({fullPage?, clip?})`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB API documents viewport, full-page, and clipped screenshot capture; it was not invoked.
- **does**: Captures a live browser tab as image bytes.
- **spark**: S=3 P=1 A=2 R=7 K=2
- **why**: S adds visual capture; P can observe user-session UI; A supports visual verification; R reaches rendered pixels; K exposes page appearance.
- **rent**: every_matching_call — capture requires an active browser task.
- **composes**: [[Browser_Coordinate_CUA_Control]]
- **confidence**: documented

### Browser_Temporary_Tab_Lifecycle
- **surface**: `browser.tabs.new()`, `tab.markDeliverable()`, `tab.markHandoff()`, `tab.close()`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB documentation says agent-created tabs close at turn end unless marked deliverable or handoff; no tab was created.
- **does**: Controls whether an agent-created browser tab closes or survives the current turn.
- **spark**: S=2 P=4 A=6 R=5 K=0
- **why**: S adds tab lifecycle control; P determines what remains in the user's browser; A gates cross-turn continuation; R manages a live tab.
- **rent**: every_matching_call — a surviving tab consumes browser-session state on each marked turn.
- **composes**: [[In_App_Browser_Selector]], [[Local_Web_App_Browser_Testing]]
- **confidence**: documented

### Browser_Page_Content_Export
- **surface**: `tab.content.{export,exportGsuite,exportYouTubeTranscript}`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB API documents generic page export, typed Google Workspace export, and YouTube transcript export; none was invoked.
- **does**: Exports supported live-page content to a local artifact.
- **spark**: S=5 P=1 A=2 R=8 K=5
- **why**: S adds content extraction; P can read user-session material; A selects a content-specific export; R bridges browser content to local artifacts; K exposes document or transcript text.
- **rent**: every_matching_call — export requires an active browser task.
- **composes**: [[Browser_User_Tab_Claiming]]
- **confidence**: documented

### Browser_Console_Log_Read
- **surface**: `tab.dev.logs({filter?, levels?, limit?})`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\browser\26.820.71523\scripts\browser-client.mjs` — The live IAB API documents filtered console log retrieval with level, timestamp, and optional source URL; it was not invoked.
- **does**: Reads captured console messages from a controlled browser tab.
- **spark**: S=4 P=0 A=4 R=7 K=4
- **why**: S adds front-end diagnostics; A supports evidence-based debugging; R reaches browser runtime logs; K reveals console events.
- **rent**: every_matching_call — log capture and retrieval require an active browser task.
- **composes**: [[Local_Web_App_Browser_Testing]], [[Browser_Playwright_DOM_Inspection]]
- **confidence**: documented

### Chrome_Browser_Family_Selector
- **surface**: `agent.browsers.get("chrome")`
- **evidence**: `C:\Users\Darian\.codex\config.toml` — Codex Desktop 26.820.9563.0 config declares `BROWSER_USE_AVAILABLE_BACKENDS = "chrome,iab"`; `C:\Users\Darian\.codex\plugins\cache\openai-bundled\chrome\26.820.71523\skills\control-chrome\SKILL.md` requires the stable `chrome` selector.
- **does**: Selects the user's Chrome family as the browser-control backend.
- **spark**: S=2 P=3 A=5 R=9 K=0
- **why**: S enables Chrome automation; P binds work to a user browser; A routes to an explicit family; R reaches an external browser extension.
- **rent**: every_matching_call — Chrome tasks pay plugin instruction and connection context.
- **composes**: [[Chrome_User_Session_Reach]], [[Browser_Playwright_DOM_Inspection]]
- **confidence**: documented

### Chrome_User_Session_Reach
- **surface**: `browser.user.openTabs()` and `browser.user.claimTab(tab)` on the `chrome` binding
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\chrome\26.820.71523\skills\control-chrome\SKILL.md` — Version 26.820.71523 describes Chrome control for existing tabs, logged-in sessions, and extensions while forbidding cookie, storage, profile, password, and session-store inspection.
- **does**: Reuses explicitly selected visible Chrome tab state without reading browser storage.
- **spark**: S=3 P=7 A=4 R=9 K=2
- **why**: S enables session-aware automation; P governs access to user browser state; A requires browser selection and tab claiming; R reaches the user's Chrome session; K can expose visible signed-in page content.
- **rent**: every_matching_call — session-aware Chrome work requires a connected extension and safety context.
- **composes**: [[Chrome_Browser_Family_Selector]], [[Browser_User_Tab_Claiming]]
- **confidence**: documented

### Windows_Computer_Use
- **surface**: `@oai/sky` via `sky`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\computer-use\26.820.71523\skills\computer-use\SKILL.md` — Version 26.820.71523 documents Windows app automation through SendInput, UI Automation, and Windows.Graphics.Capture; no Windows UI action was invoked.
- **does**: Controls Microsoft Windows application interfaces.
- **spark**: S=8 P=4 A=3 R=9 K=1
- **why**: S adds general desktop automation; P can act through user applications; A provides a non-browser UI method; R reaches Windows apps; K exposes UI state.
- **rent**: every_matching_call — Windows-control tasks pay Computer Use instructions and runtime context.
- **composes**: [[Occluded_Window_Capture]]
- **confidence**: documented

### Occluded_Window_Capture
- **surface**: `Windows.Graphics.Capture` through `@oai/sky`
- **evidence**: `C:\Users\Darian\.codex\plugins\cache\openai-bundled\computer-use\26.820.71523\skills\computer-use\SKILL.md` — Version 26.820.71523 states that screenshots work even when target windows are occluded; capture was not exercised.
- **does**: Captures Windows application pixels while another window occludes the target.
- **spark**: S=4 P=1 A=2 R=8 K=2
- **why**: S adds resilient visual inspection; P observes user-application UI; A avoids foreground-only workflows; R reaches occluded window pixels; K exposes visual state.
- **rent**: every_matching_call — capture requires the Computer Use runtime for that task.
- **composes**: [[Windows_Computer_Use]]
- **confidence**: documented

### Local_Web_App_Browser_Testing
- **surface**: `agent.documentation.get("local-web-development")` plus a controlled browser tab
- **evidence**: `https://learn.chatgpt.com/use-cases/browser-games` — The official page opened on 2026-09-02 describes building and testing in a live browser; the selected IAB API advertises a `local-web-development` guide, but no dev server was started.
- **does**: Tests a locally served web application in a controlled live browser.
- **spark**: S=6 P=0 A=7 R=7 K=2
- **why**: S adds browser-based app testing; A joins server execution with UI verification; R reaches a localhost page and browser runtime; K exposes rendered behavior.
- **rent**: every_matching_call — local testing requires both a running server and browser-control context.
- **composes**: [[Browser_Temporary_Tab_Lifecycle]], [[Browser_Console_Log_Read]], [[Browser_Playwright_DOM_Inspection]]
- **confidence**: documented

### Delegated_Session_Public_Network_Reach
- **surface**: session `network access: enabled` plus `web.run`
- **evidence**: `https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf` — This delegated Codex Desktop 26.820.9563.0 session fetched and rendered a public W3C PDF on 2026-09-02, directly demonstrating outbound public-web reach.
- **does**: Reaches public Internet resources from the delegated session.
- **spark**: S=0 P=2 A=0 R=9 K=3
- **why**: P reflects session-granted network authority; R supplies outward connectivity; K permits retrieval of public content.
- **rent**: none — the permission is session state and the read created no persistent installation.
- **composes**: [[Web_Page_Open]], [[In_App_Browser_Selector]]
- **confidence**: observed

### Agent_Internet_Access_Mode
- **surface**: environment Internet access `Off` or `On`
- **evidence**: `https://learn.chatgpt.com/docs/cloud/internet-access` — Official documentation fetched 2026-09-02 states that agent Internet access is configured per environment, with Off blocking access and On permitting it.
- **does**: Grants or blocks agent-phase Internet access for one environment.
- **spark**: S=0 P=9 A=2 R=4 K=0
- **why**: P decides whether the agent has outward authority; A changes environment execution policy; R gates Internet reach.
- **rent**: none — the mode itself adds no recurring agent component.
- **composes**: [[Internet_Domain_Allowlist]], [[Internet_HTTP_Method_Restriction]]
- **confidence**: documented

### Internet_Domain_Allowlist
- **surface**: Internet access preset `None`, `Common dependencies`, or `All (unrestricted)` plus additional domains
- **evidence**: `https://learn.chatgpt.com/docs/cloud/internet-access` — Official documentation fetched 2026-09-02 lists the three presets and allows extra domains with the first two.
- **does**: Restricts agent Internet requests to selected domains.
- **spark**: S=0 P=8 A=3 R=4 K=0
- **why**: P sets the boundary of allowed external reach; A supports least-privilege configuration; R scopes reachable hosts.
- **rent**: none — the policy has no documented per-turn charge.
- **composes**: [[Agent_Internet_Access_Mode]], [[Internet_HTTP_Method_Restriction]]
- **confidence**: documented

### Internet_HTTP_Method_Restriction
- **surface**: allowed methods `GET`, `HEAD`, and `OPTIONS`
- **evidence**: `https://learn.chatgpt.com/docs/cloud/internet-access` — Official documentation fetched 2026-09-02 says environments can restrict requests to these read-oriented methods while blocking `POST`, `PUT`, `PATCH`, `DELETE`, and others.
- **does**: Limits agent network requests to configured HTTP methods.
- **spark**: S=0 P=8 A=3 R=3 K=0
- **why**: P governs whether outward requests may mutate remote state; A enforces a read-oriented method; R narrows network operations.
- **rent**: none — the policy has no documented per-turn charge.
- **composes**: [[Agent_Internet_Access_Mode]], [[Internet_Domain_Allowlist]]
- **confidence**: documented

## Uncovered
- Chrome was not connected and no user tabs, history, storage, profiles, passwords, or signed-in content were inspected; Chrome findings are schema/config backed only.
- Computer Use was not initialized because even read-only window discovery would expose private desktop state; its consequential UI surface is documented from the pinned plugin schema.
- No dev server was started and no localhost page was opened, so the local-web testing lifecycle is documented rather than exercised.
- Browser typing, form submission, downloads, uploads, WebMCP calls, CDP, clipboard access, visibility changes, viewport overrides, and durable tab handoff were intentionally not exercised.
- Only NBA standings were probed; sports schedules and other supported leagues remain untested.
- Web PDF screenshots were exercised, but local file/media artifact production is assigned to I10 and MCP registration is assigned to I7.
