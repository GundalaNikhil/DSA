---
problem_id: DP_EXAMS_COOLDOWN_GAP__7731
display_id: DP-016
slug: exams-with-cooldown-gap
title: "Exams With Cooldown Gap"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Scheduling
  - Binary Search
tags:
  - dp
  - intervals
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-016: Exams With Cooldown Gap

## Problem Statement

You are given `n` exams, each with start time `start[i]`, end time `end[i]`, and score `score[i]`. If you take two exams `A` then `B`, you must leave at least `g` units of time between them: `start[B] >= end[A] + g`.

Select a subset of exams maximizing total score while respecting the cooldown gap.

![Problem Illustration](../images/DP-016/problem-illustration.png)

## Input Format

- First line: two integers `n` and `g`
- Next `n` lines: three integers `start`, `end`, `score` for each exam

## Output Format

- Single integer: maximum achievable total score.

## Constraints

- `1 <= n <= 100000`
- `0 <= g <= 10^9`
- `0 <= start[i] < end[i] <= 10^9`
- `0 <= score[i] <= 10^9`
- Use 64-bit integers for all sums.

## Example

**Input:**
```
3 1
1 3 5
4 6 6
6 10 5
```

**Output:**
```
11
```

**Explanation:**

Take exams 1 and 2 (score 5 + 6 = 11). Exam 3 starts at 6, but with `g = 1` you need `start >= 7` after exam 2, so you cannot add it.

![Example Visualization](../images/DP-016/example-1.png)

## Notes

- If `g = 0`, this reduces to classic weighted interval scheduling.
- Sorting by end time and binary searching the latest compatible exam yields an efficient solution.
- Overlapping exams are allowed in input; you choose a non-conflicting subset.

## Related Topics

Dynamic Programming, Binary Search, Scheduling

---

## Solution Template

### Java


### Python


### C++


### JavaScript

