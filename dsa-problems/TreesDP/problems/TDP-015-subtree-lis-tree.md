---
title: "DP for Subtree LIS on Tree"
problem_id: TDP_SUBTREE_LIS__7392
display_id: TDP-015
difficulty: Hard
tags: [tree-dp, lis, coordinate-compression, fenwick]
slug: subtree-lis-tree
time_limit: 2000
memory_limit: 256
---

## Problem Description

For each node, compute LIS length of values along root-to-node path.

## Input Format

- Line 1: N
- Line 2: N node values
- Next N-1 lines: u v (edges)

## Output Format

N integers: LIS length for each node's root path.

## Examples

### Example 1

**Input:**

```
3
2 1 3
1 2
1 3
```

**Output:**

```
1 1 2
```

### Example 2

**Input:**

```
5
1 5 2 4 3
1 2
1 3
2 4
2 5
```

**Output:**

```
1 2 2 3 3
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

## Solution Template

### Java


### Python


### C++


### JavaScript


## Hints

<details>
<summary>Hint 1</summary>
Use DFS with LIS data structure that supports add/remove.
</details>
