---
problem_id: REC_RECURSIVE_PHASE_TRANSITIONS__3225
display_id: NTB-REC-3225
slug: recursive-phase-transitions
title: "Recursive Phase Transitions"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-phase-transitions
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Phase Transitions

## Problem Statement

You are given an array `a[1..n]` and a recursion that processes segments. The recursion has two phases:

- Phase 0: split a segment into two halves.
- Phase 1: split a segment into three parts as evenly as possible (sizes differ by at most 1).

Phase switches from 0 to 1 when the recursion depth first reaches `D`.

Define the value of a segment as the sum of its elements. The recursion value is the sum of values of all segments processed.

Compute the recursion value.

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers: array values

## Output Format

- Single integer: recursion value

## Constraints

- `1 <= n <= 200000`
- `0 <= D <= 60`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A segment of length 1 is not split further.
- Depth of the root segment is 0.

## Example Input

```
4 1
1 2 3 4
```

## Example Output

```
20
```
