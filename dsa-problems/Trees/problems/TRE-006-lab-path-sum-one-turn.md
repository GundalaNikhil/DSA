---
problem_id: TRE_LAB_PATH_SUM_ONE_TURN__8046
display_id: TRE-006
slug: lab-path-sum-one-turn
title: "Lab Path Sum with Exactly One Turn"
difficulty: Medium
difficulty_score: 52
topics:
  - Trees
  - DFS
  - Prefix Sums
tags:
  - trees
  - dfs
  - path-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-006: Lab Path Sum with Exactly One Turn

## Problem Statement

Given a binary tree and a target sum `T`, determine whether there exists a downward path that starts at any node and moves only left, then only right (exactly one direction change). The path can end at any node and does not need to reach a leaf.

Return `true` if such a path exists, otherwise `false`.

![Problem Illustration](../images/TRE-006/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`
- Last line: integer `T`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if a valid path exists, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- `-10^9 <= value <= 10^9`
- `-10^14 <= T <= 10^14`

## Example

**Input:**

```
5
5 1 2
3 3 4
8 -1 -1
2 -1 -1
1 -1 -1
9
```

**Output:**

```
true
```

**Explanation:**

Path `3 -> 2 -> 1` goes left then right and sums to 6. Another valid path is `5 -> 3 -> 1` which sums to 9, so the answer is true.

![Example Visualization](../images/TRE-006/example-1.png)

## Notes

- The path must move downward and change direction exactly once.
- The path can start at any node, not necessarily the root.
- Use 64-bit integers for sums.

## Related Topics

Tree Paths, DFS, Prefix Sums

---

## Solution Template

### Java


### Python


### C++


### JavaScript

