---
problem_id: REC_CAMPUS_COURSE_ORDERING__5184
display_id: REC-011
slug: campus-course-ordering
title: "Campus Course Ordering"
difficulty: Medium
difficulty_score: 55
topics:
  - Recursion
  - Backtracking
  - Graphs
tags:
  - recursion
  - topological-sort
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-011: Campus Course Ordering

## Problem Statement

A student must take `n` courses labeled `0` to `n-1`. You are given prerequisite pairs `(u, v)` meaning course `u` must be taken before course `v`.

List all possible valid course orderings.

![Problem Illustration](../images/REC-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: two integers `u` and `v`

## Output Format

- Each valid ordering on its own line as space-separated course IDs
- Output `NONE` if no ordering exists

## Constraints

- `1 <= n <= 8`
- `0 <= m <= 15`
- Course IDs are in `[0, n-1]`

## Example

**Input:**

```
3 2
0 1
0 2
```

**Output:**

```
0 1 2
0 2 1
```

**Explanation:**

Course 0 must come before both 1 and 2, so both orders are valid.

![Example Visualization](../images/REC-011/example-1.png)

## Notes

- Use backtracking with indegree counts
- Choose any zero-indegree node at each step
- Prune if no available node exists
- Time complexity can be O(n!) in worst case

## Related Topics

Topological Sort, Backtracking, Graphs

---

## Solution Template
### Java


### Python


### C++


### JavaScript

