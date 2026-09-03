---
name: judge-composition
description: Design and run reliable Codex judges with explicit rubrics, blinded evidence, calibration cases, and auditable verdicts.
license: CC-BY-4.0
---

# Judge Composition

A judge is an evidence procedure, not a persona. Define what is being judged,
what evidence is admissible, and how observations become a verdict before any
candidate output is scored.

## 1. Frame the decision

Write:

```text
Object: {Artifact_Or_Behavior_Under_Judgment}
Decision: {Pass_Fail_Rank_Or_Score}
Audience: {Who_Uses_The_Verdict}
Cost asymmetry: {False_Pass_Cost} versus {False_Fail_Cost}
```

The cost asymmetry determines thresholds and whether abstention is allowed.
Separate hard gates from preferences: a valid schema may be mandatory while
tone is graded.

## 2. Build an observable rubric

Each criterion needs four parts:

| Field | Meaning |
|---|---|
| `criterion` | One behavior or property |
| `evidence` | What the judge may inspect |
| `scale` | Anchored outcomes, not adjectives |
| `weight/gate` | Decision effect |

Prefer binary gates for objective constraints and short anchored scales for
quality. Avoid overlapping criteria that count the same defect twice. If a
criterion cannot point to observable evidence, revise or remove it.

Use `prompt-engineering` and `hypershot-protocol` when available to structure
the judge prompt without content-heavy answer examples. When those skills are
not available in the current session, disclose that once and use their shipped
source as the fallback.

## 3. Protect independence

The judge may receive:

- candidate artifact or stable path;
- task specification and admissible source material;
- rubric and output schema;
- case identifier and runtime metadata.

Do not supply the author's preferred verdict, suspected defect, hidden chain of
reasoning, or another judge's score. When using a delegated judge, spawn with
`fork_turns: "none"`. Remember that the filesystem remains shared; restrict
allowed paths and keep author notes elsewhere when blindness matters.

## 4. Calibrate before trusting

Use a compact calibration set:

- a clear pass;
- a clear fail;
- a boundary case;
- a case with tempting but irrelevant surface quality.

Concrete calibration examples belong to the evaluation data layer, not to a
standing skill or system instruction. Record disagreements. If two competent
judges read a criterion differently, the rubric is under-specified.

## 5. Execute and aggregate

Use one judge for cheap deterministic gates. Use multiple independent judges
when the criterion is subjective or the decision is costly. Judges must not see
one another's verdicts before returning.

Aggregate by criterion, not by rhetorical confidence:

1. Apply hard gates.
2. Compare evidence for disagreements.
3. Re-run only ambiguous criteria with a clarified rubric.
4. Report unresolved uncertainty instead of manufacturing consensus.

The parent agent owns the final synthesis and verifies any claim addressable by
files, tests, or primary sources.

## Output contract

```json
{
  "verdict": "pass|fail|abstain",
  "criteria": [
    {
      "name": "{Criterion}",
      "result": "{Anchored_Result}",
      "evidence": ["{Direct_Observation}"],
      "uncertainty": "{None_Or_Named_Gap}"
    }
  ],
  "blocking_failures": ["{Failed_Gate}"],
  "summary": "{Decision_Reason_Without_Hidden_Reasoning}"
}
```

Adapt the schema to the task, but preserve evidence per criterion and an
explicit abstention path when measurement can fail.

## Failure modes

- **Persona judging:** “be a strict expert” without operational criteria.
- **Expectation leakage:** telling the judge what it should discover.
- **Aesthetic substitution:** rewarding polish when correctness is the target.
- **Double counting:** multiple criteria penalize one underlying defect.
- **Context inheritance:** a supposedly independent judge receives the author's
  conversation or notes.
- **Unmeasured pass:** missing evidence is silently interpreted as success.
