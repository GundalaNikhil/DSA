---
problem_id: REC_RECURSIVE_CIRCUIT_BREAKER__2898
display_id: NTB-REC-2898
slug: recursive-circuit-breaker
title: "Recursive Circuit Breaker"
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
  - recursive-circuit-breaker
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Circuit Breaker

## Problem Statement

You are given a rooted tree. Each node reports success (`1`) or failure (`0`). A recursive evaluation traverses children in increasing node index order. A circuit breaker trips when the number of failures seen in the current subtree reaches `F`. When tripped, the recursion stops and returns immediately without visiting remaining nodes in that subtree.

Compute how many successes are counted before the circuit breaker stops the traversal at the root.

## Input Format

- First line: integers `n` and `F`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- Single integer: number of successes counted

## Constraints

- `1 <= n <= 200000`
- `0 <= F <= 200000`
- `value` is `0` or `1`

## Clarifying Notes

- Failure count is local to each subtree call.
- If `F == 0`, the circuit breaker trips immediately and the answer is `0`.

## Example Input

```
5 2
1 0
0 1
1 1
0 2
1 2
```

## Example Output

```
2
```
