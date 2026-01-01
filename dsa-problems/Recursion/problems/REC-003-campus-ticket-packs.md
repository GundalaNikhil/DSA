---
problem_id: REC_CAMPUS_TICKET_PACKS__2187
display_id: REC-003
slug: campus-ticket-packs
title: "Campus Ticket Packs"
difficulty: Medium
difficulty_score: 46
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - combinations
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-003: Campus Ticket Packs

## Problem Statement

A ticket system has `n` values `v[i]`. For each value you may take either `0` tickets or exactly `p[i]` tickets (a fixed pack size). List all unique combinations of ticket values that sum exactly to `target`.

Output each combination as a space-separated list of ticket values in nondecreasing order. If no combination exists, output `NONE`.

![Problem Illustration](../images/REC-003/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `v[i]`
- Third line: `n` space-separated integers `p[i]`
- Fourth line: integer `target`

## Output Format

- Each valid combination on its own line (values space-separated)
- Output `NONE` if no solution exists

## Constraints

- `1 <= n <= 15`
- `1 <= target <= 200`
- `1 <= v[i] <= 50`
- `1 <= p[i] <= 10`

## Example

**Input:**

```
2
2 3
2 1
7
```

**Output:**

```
2 2 3
```

**Explanation:**

Choose two 2s and one 3 to reach 7.

![Example Visualization](../images/REC-003/example-1.png)

## Notes

- Decide for each value whether to take its full pack or not
- Sort values to keep combinations ordered
- Prune when current sum exceeds target
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinations, Pruning

---

## Solution Template
### Java


### Python


### C++


### JavaScript

