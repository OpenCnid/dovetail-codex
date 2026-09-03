# Codex SPARK map for Dovetail calibration

## Build pin

- **Codex Desktop:** `26.820.9563.0` (`OpenAI.Codex_26.820.9563.0_x64__2p2nqsd0c76g0`)
- **Codex CLI:** `0.150.0-alpha.8`
- **CLI binary:** `C:\Users\Darian\AppData\Local\OpenAI\Codex\bin\d5f4c71927a04589\codex.exe`
- **Host:** Windows NT `10.0.26200.0`, PowerShell Core
- **Configuration root:** `C:\Users\Darian\.codex`
- **Survey date:** `2026-09-02` (`America/Chicago`)
- **Probe repository:** `744846342d33dbe4fd0d5ad324d738a657e61c9f`
- **Official documentation snapshot:** refreshed `2026-09-02` into the OpenAI Docs local manual cache

Every conclusion below is relative to this build, host, configuration, and
documentation snapshot.

## Method and corpus

The run used eleven blind introspective arms, seven blind documentary arms, one
independent disproving arm, and a five-row orchestrator addendum for top-level
Desktop surfaces that delegated arms could not safely exercise. Arms received
their scope, the shared probe brief, the emission schema, and the build pin;
they were not told expected findings, counts, axis lean, or prior conclusions.
The prior repository corpus targets Claude Code and was excluded from all arms.

The raw waves contain 571 sightings. Semantic reconciliation collapsed 39
independently rediscovered capabilities, including one three-arm group, into
531 unique primitives. The final confidence mix is **117 observed / 414
documented / 0 inferred**. All 531 rows have a unique `Capitalized_Snake_Case`
name, a five-axis integer vector, confidence, rent, and an evidence-bearing wave
file. Thirty-nine rows retain `also_in` provenance for their blind corroboration.

## Enumerated surface distribution

| Axis | Mass | Percent | Mean | Sole dominant | Shared dominant | Zero on |
|---|---:|---:|---:|---:|---:|---:|
| Skills (S) | 730 | 8.7% | 1.37 | 9 | 13 | 286 |
| Personalities (P) | 1686 | 20.0% | 3.18 | 122 | 139 | 228 |
| Approaches (A) | 2721 | 32.3% | 5.12 | 161 | 186 | 9 |
| Resources (R) | 2625 | 31.1% | 4.94 | 186 | 214 | 38 |
| Knowledge (K) | 672 | 8.0% | 1.27 | 16 | 18 | 342 |

This is **enumerated surface mass**, not capability importance and not total
behavioral supply. A and R form one high-density cluster; their 1.2-point
percentage separation is too small to treat as a robust ordering. R has more
sole and shared winners, while A carries slightly more summed mass. P is a real
third cluster because Codex exposes authority, approval, interruption, persona,
and user-deference controls as explicit surfaces. S and K have fewer atomic
levers, but that does not establish that Codex lacks skill or knowledge: broad
model behavior is coarser and less surface-addressable than tools and workflow
controls.

The evidence strata make the installation/product distinction visible:

| Stratum | N | S | P | A | R | K |
|---|---:|---:|---:|---:|---:|---:|
| Observed behavior | 117 | 9.5% | 9.8% | 29.8% | 37.2% | 13.7% |
| Documented behavior | 414 | 8.4% | 22.5% | 32.9% | 29.6% | 6.6% |
| Introspective primary wave | 290 | 7.1% | 18.6% | 32.9% | 32.7% | 8.7% |
| Documentary primary wave | 241 | 10.3% | 21.4% | 31.6% | 29.5% | 7.2% |

Observed rows lean more strongly toward R because this installed delegated
runtime exercised concrete reach. Documentation contributes many P-heavy policy
and authority surfaces that were unsafe or consequential to exercise. Dovetail
must not collapse those strata into a single notion of active supply.

## Cross-corrections and calibration ceiling

The 39 blind corroborations are the run's empirical scoring calibration. Their
full vectors and maximum axis spreads are recorded in `corroborations.md`.
Twenty-four groups exceeded the default two-point tolerance and were read
manually. Fifteen provisional tie-breaks were replaced in the final index after
review of their mechanisms, principally to avoid converting reachability into
task skill or downstream resource access into authority.

One version-shadowed correction is especially important: the fresh manual still
listed the `untrusted` approval policy, while exercised CLI `0.150.0-alpha.8`
help exposed only `on-request` and `never`; the release arm dates retirement of
`untrusted` to CLI `0.149.0`. The final `Approval_Policy` row therefore keeps the
installed CLI evidence. Other useful corrections include selecting the
authority/approach-heavy hook vectors over broader documentary scores and
selecting the observed plugin manifest over its higher-mass documentary twin.

The corpus does not claim a count of “present but undocumented.” There are 111
observed rows without an exact documentary corroboration, but absence of a
semantic join is not proof that documentation is absent. They remain because
they carry direct runtime or filesystem locators.

## Disproof verdict

**Partly_Both.** The independent arm, isolated from all waves and statistics,
found that the map reliably measures the relative density of explicit,
evidence-addressable Codex levers. It does not measure total SPARK supply.
Invisible defaults, personality and authority behavior without schemas, unequal
primitive granularity, documentation duplication, surface-family sharding, and
delegate/top-level namespace differences can systematically change mass and
dominance.

The counter-case also holds: the pinned runtime visibly exposes many genuinely
distinct execution, file, web, MCP, plugin, thread, automation, and UI surfaces,
so a conclusion that Codex has dense A/R reach is not merely a documentary
artifact. Exact percentages, close rankings, and low-axis scarcity claims are
the unsafe interpretations.

## Dovetail calibration handoff

Use `ALL-PRIMITIVES.json` as the machine corpus and apply these rules:

1. For calibration against **this installed Codex runtime**, begin with
   `conf == "observed"`; treat `documented` rows as an availability prior, not
   proof of active reach.
2. Preserve `also_in` as independent corroboration metadata. Do not count those
   sightings again.
3. Use `rent` when choosing interventions: `every_turn` and `every_matching_call`
   surfaces impose recurring context, attention, compute, or runtime cost.
4. Treat A and R as a tied high-density cluster. Do not steer from their small
   aggregate difference without a task-local signal.
5. Do not interpret low S or K mass as an undersupply verdict. Add behavior-first
   calibration scenarios before using those axes for steering.
6. Calibrate P separately with fixed ask/proceed, defer/override,
   refuse/comply, interrupt/wait, tone, and escalation scenarios. Surface
   enumeration misses some of these behaviors by construction.
7. Keep top-level Desktop and delegated-agent reach distinct. The five I0 rows
   establish user-owned task, handoff, account-reset, and voice-only surfaces
   visible only to the reconciler.
8. Pin all downstream results to this build. Do not silently project stable
   documentation or post-pin releases backward onto CLI `0.150.0-alpha.8`.

`sensitivity.json` contains the confidence- and source-stratified percentages
and dominance counts for programmatic calibration.

## Not reached

- Consequential mutations were intentionally not exercised: approvals and
  bypasses, hooks, plugin or MCP install/auth, automation creation, task moves,
  account reset, voice capture, archive/delete operations, and long-running
  daemon lifecycle.
- Chrome user state, other application windows, private conversation payloads,
  credentials, connector accounts, OAuth callbacks, cloud task execution,
  remote SSH work, CI jobs, and signed-in integrations were not inspected.
- The official manual is fresh but not stamped to every exact Desktop or CLI
  binary; exact wire/runtime parity remains unknown where no live evidence won.
- Unix sandbox implementations and non-Windows Desktop behavior were outside the
  pinned host.
- Public release history does not map Desktop build `26.820.9563.0` to an exact
  release artifact, and the CLI prerelease page lacks detailed alpha notes.
- Invisible default behavior, tone, refusals, and authority choices remain a
  required behavior-first calibration stratum rather than zeros in this corpus.

## Self-check

```text
Build: Codex Desktop 26.820.9563.0 / codex-cli 0.150.0-alpha.8 / Windows NT 10.0.26200.0 / 2026-09-02
Arms: 11 introspective / 7 documentary / 1 disproving / 1 five-row orchestrator addendum
Corpus: 531 primitives — observed 117 / documented 414 / inferred 0
Contamination check: nothing about expected findings, counts, axis lean, or prior conclusions
Cross-corrections: 39 corroborated groups; Approval_Policy corrected from stale manual enum to installed CLI evidence
Present-but-undocumented: not asserted; 111 observed rows lack an exact documentary corroboration, which is insufficient to prove absence from docs
Disproof verdict: Partly_Both — stated in this map beside the distribution
Not reached: consequential mutations, private UI/account state, remote/cloud execution, non-Windows behavior, and invisible defaults
Drift vs prior: N/A — no prior Codex corpus; the retained prior run targets Claude Code and is not a compatible drift baseline
```
