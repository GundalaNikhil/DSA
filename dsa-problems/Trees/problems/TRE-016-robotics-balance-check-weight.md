---
problem_id: TRE_ROBOTICS_BALANCE_CHECK_WEIGHT__6280
display_id: TRE-016
slug: robotics-balance-check-weight
title: "Robotics Balance Check with Weight Limit"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - DFS
  - Balance
tags:
  - trees
  - balance
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-016: Robotics Balance Check with Weight Limit

## Problem Statement

Each node has a weight. A tree is balanced if, at every node:

1. The height difference between left and right subtrees is at most 1.
2. The absolute difference between total weights of left and right subtrees is at most `W`.

Return `true` if the tree is balanced, otherwise `false`.

![Problem Illustration](../images/TRE-016/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `weight left right` for nodes `0..n-1`
- Last line: integer `W`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if the tree is balanced, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- `1 <= weight <= 10^9`
- `0 <= W <= 10^12`

## Example

**Input:**

```
3
1 1 2
2 -1 -1
1 -1 -1
1
```

**Output:**

```
true
```

**Explanation:**

The tree has equal heights and the subtree weight difference at the root is 1.

![Example Visualization](../images/TRE-016/example-1.png)

## Notes

- Use postorder DFS to compute height and subtree weight.
- Stop early when an imbalance is detected.
- An empty tree is considered balanced.

## Related Topics

Balanced Trees, DFS, Tree Properties

---

## Solution Template

### Java


### Python


### C++


### JavaScript

