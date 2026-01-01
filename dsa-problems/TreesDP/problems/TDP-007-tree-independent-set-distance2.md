---
title: Distance-2 Independent Set on Tree
problem_id: TDP_DISTANCE2_INDEPENDENT_SET__8395
display_id: TDP-007
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Independent Set
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: tree-independent-set-distance2
---

# Distance-2 Independent Set on Tree

## Problem Description

Given a tree with `n` nodes where each node `i` has a weight `w[i]`, find the maximum total weight of a subset of nodes such that any two chosen nodes are at distance **at least 3**.

Two nodes are at distance at least 3 if they are not adjacent AND do not share a common neighbor.

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `w[1], w[2], ..., w[n]`
- Next `n-1` lines: edges `u v`

## Output Format

- Single integer: maximum total weight

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= w[i] <= 10^9`

## Example 1

**Input:**

```
3
1 2 3
1 2
1 3
```

**Output:**

```
3
```

**Explanation:** Can only pick node 3 (or any single node). Nodes 2 and 3 share neighbor 1, so can't pick both.

## Example 2

**Input:**

```
5
10 20 30 40 50
1 2
2 3
3 4
4 5
```

**Output:**

```
60
```

**Explanation:** Pick nodes 1 and 4 (or 2 and 5): 10+50=60 or 20+40=60.

## Solution Template

### Java


### Python


### C++


### JavaScript


## Notes

- dp[u][0] = u not selected, no child selected
- dp[u][1] = u not selected, some child selected
- dp[u][2] = u selected (all children must be in state 0)
