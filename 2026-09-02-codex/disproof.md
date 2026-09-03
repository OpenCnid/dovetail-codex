# Disproving arm — Codex axis-mass and dominance

**Target pin:** Codex Desktop 26.820.9563.0; Codex CLI 0.150.0-alpha.8; Windows NT 10.0.26200.0; 2026-09-02.

**Isolation:** This arm did not read `runs/2026-09-02-codex/waves`, any `ALL-PRIMITIVES*` or `stats*` output, or `runs/2026-07-28`. It therefore tests the measurement method without knowing the measured distribution.

## Claim attacked

> The SPARK axis-mass and dominance distribution produced by enumerating Codex surfaces is a reliable guide to which axes Codex supplies more or less of.

The strongest reading of “supplies” is total behavioral provision: explicit tools and settings plus defaults, policies, interpersonal behavior, authority relationships, and behavior available only in particular execution contexts. The weaker reading is the density of explicit, enumerable levers. The method can support the weaker claim substantially better than the stronger one.

## Evidence / method

I audited the measurement pipeline adversarially rather than inspecting its result. Evidence came from:

- `C:\Users\Darian\Desktop\codex\spark-probe\assets\probe-brief.md` and `C:\Users\Darian\Desktop\codex\spark-probe\references\emission-schema.md` (sampling rule, atomicity rule, axis meanings, authority-scoring warning, and confidence contract);
- `C:\Users\Darian\Desktop\codex\spark-probe\SKILL.md`, especially “The instrument is in the measurement” (surface visibility and shard confounds);
- `C:\Users\Darian\Desktop\codex\spark-probe\references\shard-plan.md` (blind arms, introspective/documentary overlap, delegate/top-level namespace differences, and the worked cut);
- `C:\Users\Darian\Desktop\codex\spark-probe\references\reconciliation.md`, `C:\Users\Darian\Desktop\codex\spark-probe\scripts\reconcile.py`, and `C:\Users\Darian\Desktop\codex\spark-probe\scripts\spark_stats.py` (actual merge and aggregation rules);
- direct read-only observation in the pinned build: `codex --version`, `codex --help`, `codex features list`, and the current delegated tool namespace.

The attack asks, for each possible distortion, whether it can change row inclusion, row count, or vector mass without a corresponding change in what Codex behaviorally supplies.

### 1. The estimator measures surfaced units, not total supply

`spark_stats.py` computes axis mass as the unweighted sum of each emitted row’s score. Sole and shared dominance are then counts over those same rows. There is no correction for semantic breadth, invocation frequency, behavioral reach, whether a capability is active by default, or whether one surface represents one narrow operation versus a system-wide policy. Consequently, the sampling frame and choice of atomic unit directly determine the statistic.

This is not merely hypothetical. The emission schema defines an atom by user intent and allows a multi-mode tool to be one primitive or several depending on whether users would reach for the modes separately. Fine-grained tool schemas therefore create many independently countable units. A default governing every response can create one row, or none if it has no inspectable surface. Ten narrow reachability operations can contribute ten times; one pervasive interpersonal default contributes at most once. The resulting mass is meaningful as *enumerated surface mass*, but it is not on a common cardinal scale of total axis supply.

### 2. Invisible and default behavior is missing-not-at-random

The method requires a current locator. That protects against hallucination, but the exclusion is axis-correlated. `SKILL.md` and `reconciliation.md` explicitly identify refusal, tone, deciding to ask, and defaults as moves that may have no surface. Those are disproportionately Personalities moves, including deference and authority negotiation. Their absence is therefore not random measurement noise; it systematically depresses P relative to axes realized as commands, schemas, files, and endpoints.

Direct observation reinforces the asymmetry. `codex features list` exposed 123 named feature rows in this build (45 true and 78 false; 35 were marked removed). It exposed `personality` as one stable enabled row, while tool, browser, plugin, MCP, shell, and execution concerns occupied many separately named rows. One `personality` switch does not bound the amount or variety of interpersonal behavior it controls. Conversely, an enumerable row—especially one marked false or removed—is not evidence that the current agent supplies the behavior. Enumerability and active behavioral provision are different variables.

### 3. Authority can be recovered only if scorers resist the surface’s spelling

The schema correctly warns that permission rules, approval modes, bypass switches, invocation gating, and interruption controls decide who may authorize action and should therefore carry P rather than defaulting to R. The pinned CLI visibly exposes `--ask-for-approval`, `--approve-for-me`, `--dangerously-bypass-approvals-and-sandbox`, and sandbox-selection controls. Thus P is not wholly invisible: Codex has explicit authority levers.

But this creates a calibration dependency. These levers look like configuration and execution plumbing, so independent scorers can place their mass on R unless they apply the semantic correction consistently. Meanwhile, the default decision to defer, interrupt, ask, or proceed may be imposed by the runtime instruction envelope rather than by a user-facing schema. Enumeration can therefore both misclassify visible authority as R and omit unsurfaced authority behavior. Confidence labels do not correct either error; they describe evidence proximity, not construct validity.

### 4. Granularity can manufacture dominance

The atomicity rule is principled but non-metric: “one invocation surface maps to one capability statement,” qualified by separate user intents. Tool schemas tend to enumerate methods and parameters at high resolution. Personality and broad approach policies tend to be prose or defaults at low resolution. Because the statistic gives every primitive equal opportunity to add up to ten points per axis, a finer decomposition increases an axis’s possible headcount and mass without increasing capability.

The stats implementation recognizes one symptom through `headcount_gap`, described as the signature of an axis inflated by finely cut surfaces, but it does not normalize or correct the reported mass. Sole/shared dominance also remains granularity-sensitive: splitting one R-heavy compound capability into three atomic intents can turn one dominance event into three.

### 5. Sharding changes both inclusion probability and duplication risk

The worked cut in `shard-plan.md` is organized mainly by surface family: files, command execution, delegation, skills, settings, MCP, persistence, outward reach, user-facing output, and automation. Those strata are not neutral with respect to SPARK. Most naturally expose reachability or methods, so R and A receive many high-resolution search regions. Interpersonal behavior appears partly inside settings, permissions, user-facing output, and one documentary persona scope; its unsurfaced remainder has no equivalent sampling stratum.

The plan deliberately overlaps introspective and documentary arms to cross-check the build against its documentation. That improves evidence quality but creates duplicate opportunities concentrated on well-documented, named surfaces. The plan itself says overlap becomes two rows unless reconciliation recognizes the semantic identity, while gaps resemble true absence.

### 6. Documentation duplication is only partly removed mechanically

`reconcile.py` groups duplicates by a normalization of the emitted name: lowercase, underscores converted to spaces, and whitespace collapsed. It cannot discover two different names for the same capability. `reconciliation.md` correctly assigns that expensive semantic merge to a human, but any missed alias remains two mass-bearing rows. Named CLI/tool/config capabilities are more likely than tacit defaults to be described in several places and rediscovered live, so residual duplication is plausibly axis-correlated.

There is also a smaller aggregation effect: among same-name rows with equal confidence, the reconciler selects the row with the larger total vector (`sum(r["v"])`). That is a defensible tie-breaker for retaining a substantive row, but it is mechanically upward-biased in total mass whenever scorers disagree. It does not by itself prove a particular axis is inflated, but it prevents the merged statistic from being a neutral average of scoring uncertainty.

### 7. Delegate and top-level namespaces sample different products

`shard-plan.md` states that background delegation may replace requested inheritance with a fixed built-in roster and that some actions—asking the user, publishing, and sending a file—are top-level only. It explicitly says an introspective absence means “not reachable from a background delegate,” not “not in this build.” This matters most to a distribution because the missing top-level surfaces are not a random slice: user interaction and authority-bearing actions can carry P, while publishing and file delivery can carry R.

The prescribed reconciler-added top-level rows reduce this bias, but only if the top-level session performs an explicit paired census. A delegated survey cannot infer the size of its own missing namespace. Documentary substitution also changes confidence and may count availability in the product rather than active reachability in this run. Without separate top-level and delegate strata, one aggregate mixes two harness configurations.

## Counter-case

The artifact argument does **not** show that the distribution is arbitrary or that an R-heavy result, if obtained, must be false.

First, the pinned build visibly supplies a large number of genuinely distinct reachability surfaces. `codex --help` exposes commands for execution, review, login, MCP, plugins, app/server operation, sandboxing, session management, cloud work, feature inspection, and more. The current namespace likewise contains operation-specific execution, filesystem, web, media, thread, automation, and collaboration schemas. These are not mere documentation duplicates; many are directly callable and separately useful. A conclusion that Codex exposes many Resources levers has independent observational support.

Second, the method contains unusually explicit defenses: it distinguishes reachability from ability and authority; requires locators; separates observed, documented, and inferred confidence; calls for semantic duplicate review; adds top-level-only rows at reconciliation; reports sole and shared dominance; reports per-wave shares and a granularity-sensitive headcount gap; and mandates this disproof arm. Applied rigorously, these controls can preserve broad ordinal conclusions, especially large separations between explicit R supply and axes with few explicit levers.

Third, some P and A supply is surfaced rather than tacit. Approval policies, sandbox/permission controls, delegation, collaboration, and the enabled `personality` feature are enumerable. A careful semantic scorer need not make P or A vanish merely because their mechanisms are represented as flags or tools.

The counter-case therefore supports a narrower claim: the distribution can be a reliable guide to the *relative density of explicit, evidence-addressable Codex levers in this configuration*, particularly when differences are large and survive alternative grouping choices.

## Verdict

**Partly_Both**

The result holds as a census of exposed, atomicized surfaces and may robustly reveal that Codex offers many concrete reachability levers. It is partly an artifact when interpreted as which axes Codex supplies more or less of in total. Surface-correlated visibility, unequal semantic granularity, residual documentation duplication, scoring of authority-shaped configuration, and delegate/top-level namespace differences all act before aggregation and can systematically alter both mass and dominance.

Accordingly, exact percentages, close rankings, and “undersupplied axis” steering claims are not reliable without sensitivity analysis. A large, stable ordinal separation may hold; an absence or small mass—especially for P—cannot be read as behavioral scarcity.

## Calibration implications

1. Label the primary statistic **enumerated surface mass**, not axis supply or importance.
2. Publish separate distributions for top-level observed, delegate observed, documented-but-unobserved, and inactive/removed surfaces. Do not collapse these into one notion of “supplied.”
3. Add a behavior-first calibration stratum for defaults that have no surface: fixed scenarios testing ask/proceed, defer/override, refuse/comply, interrupt/wait, tone, and authority escalation. Report this beside, not mixed silently into, the surface census.
4. Run granularity sensitivity analysis: recompute after collapsing primitives into semantic capability families and after splitting disputed compound intents. Treat rankings that change as non-robust.
5. Audit duplicates semantically across live and documentary arms. Report unresolved alias candidates. Replace the equal-confidence “larger total vector wins” tie-break with explicit adjudication or a reported score range when calculating mass.
6. Report coverage denominators and unknowns. “No located surface” must remain unknown for invisible behavior, not become zero supply.
7. Keep sole and shared dominance, per-wave shares, and headcount gap, but add leave-one-shard-out results. A ranking driven by one surface-family shard is a property of the cut.
8. Use paired top-level/delegate probes with the same checklist. Namespace deltas should be findings and calibration strata, not absences silently absorbed into the aggregate.
9. Reserve steering advice for conclusions that survive at least the confidence, granularity, duplicate, activity-state, and namespace stratifications above.

## Limitations

- Isolation prevents this arm from saying whether the actual 2026-09-02 distribution is large, close, reversed under calibration, or dominated by any particular wave. The verdict concerns the inference from distribution to supply, not the unseen numbers.
- CLI help, feature rows, and the present delegated namespace are one installed/configured snapshot. Feature names marked false or removed demonstrate the presence-versus-activity problem but are not asserted to have entered the corpus.
- No side-effectful configuration changes or behavioral counterfactuals were run, consistent with the probe’s read-only discipline. The proposed default/personality calibration remains to be executed.
- SPARK scores and semantic-family boundaries still require judgment. Sensitivity ranges can expose that judgment but cannot eliminate it.
- The top-level/delegate difference is established by the survey method’s own recorded constraint; this arm cannot see the orchestrator’s private roster and therefore cannot quantify the missing surface set.
