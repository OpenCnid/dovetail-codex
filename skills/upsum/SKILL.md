---
name: upsum
description: Close a work session by appending a durable record, rebuilding a fixed-size recency-weighted summary, carrying open work forward, and running repository checks. Invoke explicitly.
license: CC-BY-4.0
---

# Upsum

The record grows and never forgets. The summary stays bounded and forgets on
purpose. Run this ceremony only when explicitly invoked.

## Locate the project memory

Use existing repository conventions when present. Otherwise use:

| Path | Rule |
|---|---|
| `.upsum/RECORD.md` | append-only session record |
| `.upsum/SUMMARY.md` | rewritten whole, 250-word default budget |
| `TODO.md` | rewritten whole, human-visible open work |

## 1. Append one evidence-based record entry

Read the diff and repository state, then append:

```md
## {ISO_Date} · {Short_Session_Label}

**Did** — {Repository_Changes_Not_Conversation_Intent}
**Learned** — {New_Evidence_Or_Understanding}
**Decided** — {Decision_And_Owner}
**Left** — {Deliberately_Unfinished_Work_And_Reason}
```

Never edit earlier entries. If no work changed and no durable decision was made,
say so and stop instead of adding noise.

## 2. Rebuild the bounded summary

Derive `.upsum/SUMMARY.md` from the entire record. Keep the configured budget,
or 250 words when none exists. Allocate resolution by recency:

```text
oldest  {Collapsed_To_A_Label}
         {Outcome_Only}
         {Outcome_Plus_One_Distinguishing_Detail}
newest  {Nearly_Full_Detail_With_Redundancy_Trimmed}
```

Entries age by losing resolution, not by disappearing. Do not grow the budget
because the record grew.

## 3. Carry forward open work

Rewrite `TODO.md` from the record and current session. Each open item names the
blocking decision or condition and who can unblock it:

```md
- [ ] {Observable_Completion} — blocked on {Owner_And_Condition}
```

Remove completed items. `Left` records intentional incompletion; it is not an
apology field.

## 4. Run the shipped checks

Resolve this skill's directory from its source locator in the current skill
catalog, then run its script against the repository working directory:

```bash
python {upsum-skill-directory}/scripts/checks.py {repository-directory}
```

Do not assume the skill lives under a global config directory; plugins may run
from a repository scope or versioned cache. The script checks inside references,
repository state, skill health, and license/credit travel. `UNMEASURED` means the
check could not establish a result, not that it passed.

Exit codes describe measurement health:

- `0`: every check ran;
- `1`: at least one check could not be measured;
- `2`: the checker itself failed.

Act on findings or record why a finding is accepted. Do not merely narrate the
output.

## 5. Refresh publishing claims

Only when the session will commit, push, or release:

- test the documented install path from a clean location;
- verify that the README inventory matches the repository;
- verify that every stated limit still holds.

## Completion

Report which memory files changed, the summary budget, open blockers, check
results, and any unmeasured evidence. Preserve the append-only record exactly.
