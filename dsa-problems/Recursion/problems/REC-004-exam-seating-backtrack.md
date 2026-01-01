---
problem_id: REC_EXAM_SEATING_BACKTRACK__6392
display_id: REC-004
slug: exam-seating-backtrack
title: "Exam Seating Backtrack"
difficulty: Medium
difficulty_score: 44
topics:
  - Recursion
  - Backtracking
  - Combinatorics
tags:
  - recursion
  - backtracking
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-004: Exam Seating Backtrack

## Problem Statement

An exam hall has `n` seats in a single row, indexed `0` to `n-1`. You must place exactly `k` students so that any two students have at least `d` empty seats between them.

Count how many valid arrangements are possible.

![Problem Illustration](../images/REC-004/problem-illustration.png)

## Input Format

- First line: three integers `n`, `k`, and `d`

## Output Format

- Single integer: number of valid arrangements

## Constraints

- `1 <= n <= 15`
- `0 <= k <= n`
- `0 <= d <= n`

## Example

**Input:**

```
5 2 2
```

**Output:**

```
3
```

**Explanation:**

With at least 2 empty seats between students, valid pairs are (0,3), (0,4), (1,4).

![Example Visualization](../images/REC-004/example-1.png)

## Notes

- If positions are `i < j`, then `j - i - 1 >= d`
- Use recursion to choose the next valid seat index
- Prune when remaining seats are insufficient
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinatorics, Recursion

---

## Solution Template
### Java


### Python


### C++


### JavaScript

