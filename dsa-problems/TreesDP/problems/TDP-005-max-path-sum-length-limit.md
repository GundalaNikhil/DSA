---
title: Max Path Sum with Length Limit
problem_id: TDP_MAX_PATH_SUM_LENGTH_LIMIT__6382
display_id: TDP-005
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Path Algorithms
  - Constrained Optimization
categories:
  - Algorithms
  - Data Structures
slug: max-path-sum-length-limit
---

# Max Path Sum with Length Limit

## Problem Description

You are given a tree with `n` nodes where each node has a value (possibly negative). Find the maximum path sum where the path uses **at most `L` edges**.

A path is a sequence of distinct nodes where consecutive nodes are connected by an edge. The path sum is the sum of all node values in the path.

## Input Format

- First line: two integers `n` and `L` (number of nodes and maximum path length in edges)
- Second line: `n` space-separated integers representing node values `value[1], value[2], ..., value[n]`
- Next `n-1` lines: each contains two integers `u v` representing an edge between nodes `u` and `v`

## Output Format

- Single integer: the maximum path sum using at most `L` edges

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= L <= n-1`
- `-10^9 <= value[i] <= 10^9`
- The graph forms a valid tree

## Example 1

**Input:**

```
3 2
1 -2 3
1 2
1 3
```

**Output:**

```
4
```

**Explanation:**
Tree structure:

```
    1 (val=1)
   / \
  2   3
(val=-2) (val=3)
```

Possible paths with at most 2 edges:

- Single nodes: 1, -2, 3 → max = 3
- Path 1-2: 1 + (-2) = -1
- Path 1-3: 1 + 3 = 4 ✓ (maximum)
- Path 2-1-3: -2 + 1 + 3 = 2 (uses 2 edges)

Maximum sum is 4 (path from node 1 to node 3).

## Example 2

**Input:**

```
5 3
10 -5 20 -10 30
1 2
1 3
2 4
2 5
```

**Output:**

```
45
```

**Explanation:**
Tree structure:

```
      1(10)
     / \
  2(-5) 3(20)
   / \
4(-10) 5(30)
```

Best path with at most 3 edges:

Possible paths:

- Just node 5: 30
- Path 1-3: 10 + 20 = 30
- Path 5-2-1: 30 + (-5) + 10 = 35
- Path 5-2-1-3: 30 + (-5) + 10 + 20 = 55 (uses 3 edges) ✓

Maximum is 55 (path from node 5 through nodes 2, 1, to node 3).

## Solution Template

### Java


### Python


### C++


### JavaScript


## Notes

- Path length is measured in edges, not nodes
- Values can be negative - don't prematurely optimize by ignoring negative paths
- A single node is a valid path (0 edges)
- Use long/long long to avoid overflow
- DP state: dp[node][length] = max sum using exactly 'length' edges from this node downward
