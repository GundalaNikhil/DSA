---
problem_id: TRE_SEMINAR_OPPOSITE_PARITY_ANCESTOR_GAP__9157
display_id: TRE-018
slug: seminar-opposite-parity-ancestor-gap
title: "Seminar Opposite-Parity Ancestor Gap"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - DFS
  - Prefix Min/Max
tags:
  - trees
  - dfs
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-018: Seminar Opposite-Parity Ancestor Gap

## Problem Statement

For each node, consider only ancestors whose depth parity is different from the node (one even, one odd). Compute the maximum absolute difference between a node's value and any such opposite-parity ancestor value.

Return the maximum difference over all nodes.

![Problem Illustration](../images/TRE-018/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: maximum absolute difference

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
5
8 1 2
3 3 -1
10 -1 4
1 -1 -1
14 -1 -1
```

**Output:**

```
5
```

**Explanation:**

At node `3` (odd depth), the opposite-parity ancestor is `8` (even depth) with difference 5, which is the maximum.

![Example Visualization](../images/TRE-018/example-1.png)

## Notes

- If a node has no opposite-parity ancestors, it contributes nothing.
- Track min and max values for each parity along the root-to-node path.
- An empty tree outputs 0.

## Related Topics

Tree DFS, Parity, Prefix Min/Max

---

## Solution Template

### Java


### Python


### C++


### JavaScript

