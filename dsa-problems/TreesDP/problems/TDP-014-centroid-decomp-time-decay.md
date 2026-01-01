---
title: "Centroid Decomposition with Time-Decay Queries"
problem_id: TDP_CENTROID_TIME_DECAY__9247
display_id: TDP-014
difficulty: Hard
tags: [tree-dp, centroid-decomposition, time-decay, advanced]
slug: centroid-decomp-time-decay
time_limit: 2000
memory_limit: 256
---

## Problem Description

Weighted tree with node values and timestamps. Query: find minimum (distance × decay + value) to any marked node.

## Input Format

- Line 1: N D (nodes, decay constant)
- Next N-1 lines: u v w (edges)
- Next line: Q (queries)
- Q lines: type params

## Output Format

Per query output.

## Examples

### Example 1

**Input:**

```
3 1000
1 2 10
2 3 20
2
1 1 100 0
2 2 0
```

**Output:**

```
110
```

### Example 2

**Input:**

```
5 500
1 2 5
1 3 10
2 4 7
2 5 3
3
1 1 50 0
1 4 80 0
2 5 0
```

**Output:**

```
62
```

## Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ Q ≤ 100,000

## Solution Template

### Java


### Python


### C++


### JavaScript


## Hints

<details>
<summary>Hint 1</summary>
Use centroid decomposition for tree queries.
</details>
