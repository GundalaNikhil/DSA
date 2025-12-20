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

