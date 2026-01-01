---
problem_id: SEG_DYNAMIC_CONNECTIVITY_OFFLINE__6384
display_id: SEG-016
slug: dynamic-connectivity-offline
title: "Dynamic Connectivity Over Time (Offline)"
difficulty: Hard
difficulty_score: 78
topics:
  - Segment Tree
  - DSU Rollback
  - Offline Queries
tags:
  - segment-tree
  - dsu
  - offline
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-016: Dynamic Connectivity Over Time (Offline)

## Problem Statement

You are given a sequence of events on an undirected graph with `n` nodes. The events are:

- `ADD u v`: add edge `(u, v)`
- `REMOVE u v`: remove edge `(u, v)`
- `QUERY u v`: ask whether `u` and `v` are connected at this time

Answer all queries in order. You must process the events offline.

![Problem Illustration](../images/SEG-016/problem-illustration.png)

## Input Format

- First line: integers `n` and `m` (number of nodes and events)
- Next `m` lines: events `ADD`, `REMOVE`, or `QUERY`

## Output Format

- For each `QUERY`, print `true` if connected, otherwise `false`

## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 200000`
- `1 <= u, v <= n`

## Example

**Input:**

```
3 4
ADD 1 2
QUERY 1 2
REMOVE 1 2
QUERY 1 2
```

**Output:**

```
true
false
```

**Explanation:**

The first query is connected by edge (1,2). After removal, the nodes are disconnected.

![Example Visualization](../images/SEG-016/example-1.png)

## Notes

- Use a segment tree over time intervals
- Maintain a DSU with rollback to undo unions
- Map each edge to the active time intervals
- Process queries with depth-first traversal

## Related Topics

DSU Rollback, Offline Queries, Segment Tree

---

## Solution Template
### Java


### Python


### C++


### JavaScript

