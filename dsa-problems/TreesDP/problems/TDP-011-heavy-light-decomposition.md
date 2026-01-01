---
title: "Heavy-Light Decomposition Basics"
problem_id: TDP_HEAVY_LIGHT_DECOMP__8154
display_id: TDP-011
difficulty: Medium
tags: [tree-dp, heavy-light-decomposition, path-queries, segment-tree]
slug: heavy-light-decomposition
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given a weighted tree, preprocess it to answer path sum queries efficiently. Use Heavy-Light Decomposition to partition the tree into chains.

---

## Input Format

- Line 1: N (number of nodes)
- Line 2: N integers (node values)
- Next N-1 lines: u, v (edges)
- Next line: Q (number of queries)
- Next Q lines: u, v (query sum on path from u to v)

---

## Output Format

For each query, print the sum of values on the path from u to v.

---

## Examples

### Example 1

**Input:**

```
5
1 2 3 4 5
1 2
1 3
2 4
2 5
3
1 4
3 5
4 5
```

**Output:**

```
7
11
11
```

### Example 2

**Input:**

```
3
10 20 30
1 2
2 3
2
1 3
1 2
```

**Output:**

```
60
30
```

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

---

## Solution Template

### Java


### Python


### C++


### JavaScript


---

## Hints

<details>
<summary>Hint 1</summary>
Partition tree into heavy chains where heavy child has largest subtree.
</details>

<details>
<summary>Hint 2</summary>
Build segment tree over chain positions for range sum queries.
</details>
