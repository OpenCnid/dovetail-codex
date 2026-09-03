# Codex SPARK Probe run — 2026-09-02

This run prepares a Codex-specific capability corpus for Dovetail calibration.

- `MAP.md` — reconciled interpretation and calibration handoff
- `ALL-PRIMITIVES.json` — 531 unique machine-readable primitives
- `stats.json` — aggregate axis mass, dominance, confidence, rent, and per-wave shares
- `sensitivity.json` — observed/documented and introspective/documentary strata
- `corroborations.md` — 39 blind cross-arm corroborations plus human scoring resolutions
- `disproof.md` — independent methodological challenge; verdict `Partly_Both`
- `reconciliation-overrides.json` — 16 reproducible human scoring decisions
- `waves/*.md` — 18 blind arm files plus one orchestrator-only addendum

The corpus is pinned to Codex Desktop `26.820.9563.0`, codex-cli
`0.150.0-alpha.8`, Windows NT `10.0.26200.0`, and survey date `2026-09-02`.

Rebuild the reconciled index and statistics with:

```powershell
python scripts/build_index.py runs/2026-09-02-codex/waves -o runs/2026-09-02-codex/ALL-PRIMITIVES.raw.json
python scripts/reconcile.py runs/2026-09-02-codex/ALL-PRIMITIVES.raw.json -o runs/2026-09-02-codex/ALL-PRIMITIVES.json
python scripts/apply_overrides.py runs/2026-09-02-codex/ALL-PRIMITIVES.json runs/2026-09-02-codex/reconciliation-overrides.json
python scripts/spark_stats.py runs/2026-09-02-codex/ALL-PRIMITIVES.json --json runs/2026-09-02-codex/stats.json
```

The raw waves intentionally retain duplicate sightings for auditability. The
override file applies the mechanism-level resolutions explained in
`corroborations.md` after generic reconciliation.
