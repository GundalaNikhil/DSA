---
problem_id: CON_MVCC_BASICS__A20E
display_id: CON-016
slug: mvcc-basics
title: "Multiversion Concurrency Control (MVCC) Basics"
difficulty: Medium
difficulty_score: 58
topics:
  - Concurrency
  - Databases
  - MVCC
  - Transactions
tags:
  - concurrency
  - mvcc
  - transactions
  - isolation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Multiversion Concurrency Control (MVCC) Basics

## Problem Statement

Many databases use MVCC to let **readers avoid blocking writers** (and vice versa) by keeping multiple versions of rows/records.

Explain MVCC at a fundamental level:

- What version metadata is stored (timestamps/transaction ids)
- How reads pick a visible version (snapshot rules)
- How writes create new versions
- How write-write conflicts are handled

Your answer should be framed as if explaining to a student preparing for interviews (correct but practical).

## Input Format

No strict input.

## Output Format

Include:

1. Snapshot read rules (visibility)
2. Commit rules for writers
3. How write-write conflicts are detected/resolved
4. One note on garbage collection (vacuum) of old versions

## Constraints

- N/A (conceptual)

## Example

Two concurrent transactions:

- `T1` starts and reads `X`
- `T2` starts and writes `X` and commits

Under MVCC, `T1` continues to see the old version of `X` (its snapshot), while new transactions see `T2`’s version.

## Related Topics

Concurrency Control, Transactions, Isolation Levels


## Solution Template

### Python

```python
def solve():
    return 0
1. Snapshot Rules (Read Visibility):
   - A transaction T (start timestamp TS_S) reads a row version V if:
     - V.created < TS_S (Created before T started).
     - V.deleted > TS_S (Not deleted before T started, or not deleted at all).
     - V is committed.
   - **Result**: Readers see a consistent snapshot of the DB at `TS_S`, ignoring active writes by other txns (Non-blocking reads).

2. Commit Rules:
   - Writes create NEW versions of rows (append-only logic or diffs).
   - On commit, new versions become visible to future transactions.
   - Update Transaction timestamp to Current.

3. Write-Write Conflicts:
   - If T1 wants to update Row R, but R was updated by T2 (which committed AFTER T1 started, or is active):
   - **Detection**: T1 checks if the latest version of R is visible to it. If latest version > T1.start, Conflict.
   - **Resolution**: T1 Aborts (First-Committer-Wins) OR T1 waits for T2 to commit/abort (in blocking databases like Postgres, picking up the new version if Isolation allows).

4. Garbage Collection (Vacuum):
   - Old versions that are no longer visible to ANY active transaction snapshot (Created < Oldest_Active_Start) must be cleaned up to reclaim space.
""")

if __name__ == "__main__":
    solve()
```

