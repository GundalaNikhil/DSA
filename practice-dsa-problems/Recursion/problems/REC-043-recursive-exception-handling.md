---
problem_id: REC_RECURSIVE_EXCEPTION_HANDLING__5988
display_id: NTB-REC-5988
slug: recursive-exception-handling
title: "Recursive Exception Handling"
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
  - recursive-exception-handling
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Exception Handling

## Problem Statement

You are given a rooted tree. Each node has a value `v` and an exception capacity `cap` (how many child exceptions it can catch).

Define `Eval(node)`:

- If `v[node] < 0`, the node throws an exception immediately.
- Otherwise evaluate children in order. If a child throws:
  - If the node still has remaining capacity, it catches the exception and continues.
  - Otherwise it throws an exception.
- If the node does not throw, it returns the sum of its own value and all successfully evaluated children.

Compute the root result, or output `EXCEPTION` if the root throws.

## Input Format

- First line: integer `n`
- Next `n` lines: `v cap parent` (parent is 0 for root)

## Output Format

- Single integer root sum, or `EXCEPTION`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= v <= 10^9`
- `0 <= cap <= 200000`

## Clarifying Notes

- Exception capacity applies only to child exceptions, not to the node's own failure.
- The evaluation order is fixed by node index.

## Example Input

```
4
5 1 0
-2 0 1
3 0 1
-1 0 3
```

## Example Output

```
8
```
