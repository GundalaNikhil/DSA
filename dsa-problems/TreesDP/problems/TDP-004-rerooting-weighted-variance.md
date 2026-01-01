---
title: Rerooting for Weighted Distance Variance
problem_id: TDP_REROOTING_WEIGHTED_VARIANCE__5927
display_id: TDP-004
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Rerooting Technique
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: rerooting-weighted-variance
---

# Rerooting for Weighted Distance Variance

## Problem Description

You are given a tree with `n` nodes, where each node `i` has a weight `w[i]`. Your task is to find the node that minimizes the **weighted sum of squared distances**:

`cost(i) = sum_j=1^n w[j] x dist(i, j)^2`

where `dist(i, j)` is the number of edges in the shortest path between nodes `i` and `j`.

Return the node number (1-indexed) that minimizes this cost. If there are multiple such nodes, return the smallest node number.

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers representing `w[1], w[2], ..., w[n]`
- Next `n-1` lines: each contains two integers `u v` representing an edge between nodes `u` and `v`

## Output Format

- Single integer: the node number that minimizes the weighted sum of squared distances

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= w[i] <= 10^6`
- `1 <= u, v <= n`
- The graph forms a valid tree (connected, acyclic, n-1 edges)

## Example 1

**Input:**

```
3
1 2 1
1 2
2 3
```

**Output:**

```
2
```

**Explanation:**
Tree structure: 1 -- 2 -- 3

Cost for node 1: w[1]×0² + w[2]×1² + w[3]×2² = 1×0 + 2×1 + 1×4 = 6
Cost for node 2: w[1]×1² + w[2]×0² + w[3]×1² = 1×1 + 2×0 + 1×1 = 2 ✓ (minimum)
Cost for node 3: w[1]×2² + w[2]×1² + w[3]×0² = 1×4 + 2×1 + 1×0 = 6

Node 2 has the minimum cost.

## Example 2

**Input:**

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
```

**Output:**

```
2
```

**Explanation:**
Tree structure:

```
    1
   / \
  2   3
 / \
4   5
```

Cost calculations:

- Node 1: 0 + 20×1 + 30×1 + 40×4 + 50×4 = 470
- Node 2: 10×1 + 0 + 30×4 + 40×1 + 50×1 = 220 ✓ (minimum)
- Node 3: 10×1 + 20×4 + 0 + 40×9 + 50×9 = 900
- Node 4: 10×4 + 20×1 + 30×9 + 0 + 50×4 = 540
- Node 5: 10×4 + 20×1 + 30×9 + 40×4 + 0 = 580

Node 2 minimizes the cost.

## Solution Template

### Java


### Python


### C++


### JavaScript


## Notes

- The problem requires rerooting DP technique to achieve O(n) time complexity
- Naive approach of computing cost for each root separately would be O(n²)
- Be careful with integer overflow - use long/long long for intermediate calculations
- The squared distance means we need special handling in the DP transition
