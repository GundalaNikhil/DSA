---
problem_id: GRP_EXAM_SEATING_VIP__3928
display_id: GRP-012
slug: exam-seating-rooms-vip
title: "Exam Seating Rooms with VIP Isolation"
difficulty: Medium
difficulty_score: 40
topics:
  - Union-Find
  - Connected Components
  - Disjoint Set Union
tags:
  - graph
  - union-find
  - dsu
  - connected-components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-012: Exam Seating Rooms with VIP Isolation

## Problem Statement

You are given an undirected graph where nodes represent students who prefer to sit together (connected by edges). Some students are designated as VIPs.

**Constraint**: No connected component can contain more than one VIP.

Your task is to remove the minimum number of edges such that no component contains more than one VIP, then return the size of the largest remaining connected component.

![Problem Illustration](../images/GRP-012/problem-illustration.png)

## Input Format

- First line: integer `n` (number of students/nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an edge between students `u` and `v`
- Last line: space-separated integers representing VIP student IDs

## Output Format

- Single integer: the size of the largest connected component after edge removals

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- Number of VIPs `<= n`

## Example

**Input:**
```
5
3
0 1
1 2
3 4
2 3
```

**Output:**
```
3
```

**Explanation:**

Edges: (0,1), (1,2), (3,4)
VIPs: {2, 3}

Initial components:
- Component 1: {0, 1, 2} (contains VIP 2)
- Component 2: {3, 4} (contains VIP 3)

Since VIPs 2 and 3 are already in different components, no edges need to be removed.

Final components:
- Component 1: {0, 1, 2} → size 3
- Component 2: {3, 4} → size 2

Largest component size = 3

![Example Visualization](../images/GRP-012/example-1.png)

## Notes

- Use Disjoint Set Union (DSU / Union-Find) to track components
- Track which components contain VIPs
- When processing an edge (u, v):
  - If both components already have a VIP, skip the edge
  - Otherwise, union the components
- After processing all valid edges, find the maximum component size
- Time complexity: O(m × α(n)) where α is the inverse Ackermann function (nearly constant)

## Related Topics

Union-Find, DSU, Connected Components, Graph Constraints, Component Tracking

---

## Solution Template

### Java


### Python


### C++


### JavaScript
