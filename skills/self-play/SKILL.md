---
name: self-play
description: Evaluate prompts, skills, policies, or generated artifacts through clean-room Codex runs, adversarial cases, and evidence-backed revision.
license: CC-BY-4.0
---

# Self-Play

Self-play separates creation from evaluation. The author produces a candidate;
an evaluator receives only the ground needed to test it; the parent revises from
evidence rather than from the evaluator's confidence.

## Choose the evaluation boundary

Use `collaboration.spawn_agent` with `fork_turns: "none"` for a clean
conversation. This prevents the evaluator from inheriting the discussion that
created the candidate.

It does not hide the filesystem. All collaborating agents share the same
working directory, repository instructions, and live edits. Before calling a
run “blind,” audit whether the candidate, expected result, or author notes are
already readable from named paths. Give the evaluator a read-only boundary and
the minimum allowed paths. If genuine filesystem isolation is required, ask the
user whether to create a separate worktree task; do not silently claim it.

## The five moves

### 1. Define the property

State one falsifiable property and its evidence:

```text
Property: {Behavior_That_Must_Hold}
Pass evidence: {Observable_Result}
Failure evidence: {Counterexample_Or_Missing_Result}
```

Test behavior, not prose similarity. “The prompt is clear” is not falsifiable;
“three independent runs return valid JSON matching the schema” is.

### 2. Build the case set

Use the smallest set that spans the risk:

- one ordinary case;
- one boundary or ambiguous case;
- one adversarial case that pressures the suspected failure mode;
- one negative control when false positives matter.

Do not put the expected finding into the case prompt. Ground may include input,
provenance, paths, and the scoring contract—only what lets the evaluator look.

### 3. Run independent trials

For interactive evaluation, spawn bounded evaluators with `fork_turns: "none"`.
Give each the same candidate and case contract, without earlier verdicts. Use
parallel agents only when the trials are independent and slots are available.

For repeatable batch evaluation, use `codex exec` with an explicit working
directory and, when useful, `--ephemeral`, `--ignore-user-config`, `--json`,
`--output-last-message`, or `--output-schema`. Record the CLI version and exact
configuration because these surfaces are version-sensitive.

### 4. Judge evidence

Score each run against the declared property. Preserve:

- case identity;
- candidate version or hash;
- runtime and context configuration;
- raw result or stable artifact path;
- pass/fail reason tied to observable output.

Do not let later evaluators see earlier scores. For high-stakes or subjective
criteria, compose a rubric with `judge-composition` and keep the judge blind to
the author's preferred answer.

### 5. Revise one cause at a time

Change the smallest instruction or surface that explains the failure. Re-run
the failing case plus a regression control. A revision is supported only when
the targeted behavior changes without breaking an already-passing property.

## Ten disciplines

1. **Separation:** author and evaluator contexts are distinct.
2. **Grounding:** prompts contain lookup ground, not expected findings.
3. **Falsifiability:** every property has failure evidence.
4. **Coverage:** cases span ordinary, boundary, adversarial, and control behavior.
5. **Repeatability:** versions, configuration, and candidate identity are recorded.
6. **Independence:** trials do not inherit prior verdicts.
7. **Minimal revision:** change one causal lever at a time.
8. **Regression:** protect a previously passing case.
9. **Consolidation:** the parent compares evidence and owns the conclusion.
10. **Honest isolation:** conversation cleanliness is never mislabeled as
    filesystem or policy isolation.

## Prompt frame

```text
Objective: Evaluate whether {Candidate_Identifier} satisfies {Property}.
Ground: Read only {Allowed_Path_Or_Inline_Candidate}. Use {Case_Set}.
Method: Produce the requested outputs, then score only against {Rubric}.
Constraints: Do not inspect {Author_Notes_Or_Expected_Answer_Locations}.
Return: {Per_Case_Evidence_Then_One_Verdict_With_Uncertainty}.
```

## Stop conditions

Stop and report the limitation when the evaluator cannot be kept independent,
the property is not falsifiable, the case set cannot represent the risk, or the
runtime differs so much between trials that results are not comparable.
