---
title: "Binary Lifting for K-th Ancestor with Color Filter"
problem_id: TDP_KTH_ANCESTOR_COLOR__3741
display_id: TDP-012
difficulty: Medium
tags: [tree-dp, binary-lifting, ancestor-queries, color-filter]
slug: kth-ancestor-color-filter
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given tree where each node has a color, answer queries: find k-th ancestor of node v with color c.

## Input Format

- Line 1: N
- Line 2: N colors
- Next N-1 lines: edges u v
- Next line: Q queries
- Next Q lines: v c k

## Output Format

For each query, print k-th ancestor with color c, or -1 if doesn't exist.

## Examples

### Example 1

**Input:**

```
5
1 2 1 2 1
1 2
1 3
2 4
2 5
3
4 2 1
5 1 2
3 1 1
```

**Output:**

```
2
1
1
```

### Example 2

**Input:**

```
3
1 1 2
1 2
2 3
2
3 1 1
3 1 2
```

**Output:**

```
2
1
```

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ color[i] ≤ 10

## Solution Template

### Java


### Python


### C++


### JavaScript


## Hints

<details>
<summary>Hint 1</summary>
Use binary lifting to jump ancestors quickly.
</details>

<details>
<summary>Hint 2</summary>
Track color count along ancestor path.
</details>
