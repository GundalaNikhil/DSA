---
problem_id: SEG_RANGE_SUM_POINT_UPDATES_UNDO__5472
display_id: SEG-001
slug: range-sum-point-updates-undo
title: "Range Sum with Point Updates and Undo"
difficulty: Medium
difficulty_score: 52
topics:
  - Segment Tree
  - Fenwick Tree
  - Rollback
tags:
  - segment-tree
  - fenwick
  - rollback
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-001: Range Sum with Point Updates and Undo
## Problem Statement
You maintain an array `a` under three operations:
- `UPDATE i x`: set `a[i] = x`
- `QUERY l r`: output the sum of `a[l..r]` modulo `M`
- `UNDO k`: revert the last `k` update operations (queries do not count)
Process all operations in order and output answers for each `QUERY`.
![Problem Illustration](../images/SEG-001/problem-illustration.png)
## Input Format
- First line: integers `n`, `q`, and `M`
- Second line: `n` space-separated integers (initial array)
- Next `q` lines: one operation (`UPDATE`, `QUERY`, or `UNDO`)
## Output Format
- For each `QUERY`, print one line with the sum modulo `M`
## Constraints
- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= M <= 10^9+7`
- `0 <= k <= 100`
## Example
**Input:**
```
5 5 1000
1 2 3 4 5
QUERY 1 3
UPDATE 2 10
QUERY 0 4
UNDO 1
QUERY 0 4
```
**Output:**
```
9
22
15
```
**Explanation:**
Sums are computed modulo 1000, and `UNDO 1` restores `a[2]` from 10 back to 3.
![Example Visualization](../images/SEG-001/example-1.png)
## Notes
- Keep a history stack of point updates to undo
- Segment tree or Fenwick tree supports point updates and range sums
- Each `UNDO` replays at most 100 updates
- Total time: O((n + q) log n)
## Related Topics
Segment Tree, Fenwick Tree, Rollback
---
## Solution Template
### Java
### Python
### C++
### JavaScript
