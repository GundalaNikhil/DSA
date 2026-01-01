---
problem_id: GRB_DSU_BASICS__1728
display_id: GRB-012
slug: dsu-basics
title: "Disjoint Set Union Basics"
difficulty: Easy
difficulty_score: 30
topics:
  - Graphs
  - DSU
  - Connectivity
tags:
  - graphs-basics
  - dsu
  - connectivity
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-012: Disjoint Set Union Basics

## Problem Statement

Maintain a set of `n` nodes under two operations:

- `union u v`: connect the sets containing `u` and `v`
- `find u v`: report whether `u` and `v` are in the same set

Answer all queries in order.

![Problem Illustration](../images/GRB-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Next `q` lines: queries in one of two forms:
  - `union u v`
  - `find u v`

## Output Format

- For each `find` query, print `true` or `false` on its own line

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 3
union 0 1
union 2 3
find 0 3
```

**Output:**

```
false
```

**Explanation:**

Nodes 0 and 3 are in different sets after the two unions.

![Example Visualization](../images/GRB-012/example-1.png)

## Notes

- Use DSU with path compression and union by rank/size.
- The graph is implicit; queries are dynamic.
- Output only for `find` queries.

## Related Topics

Disjoint Set Union, Connectivity Queries

---

## Solution Template

### Java


### Python


### C++


### JavaScript

