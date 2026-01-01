---
problem_id: GRP_SHUTTLE_SEATING_FEASIBILITY__8362
display_id: GRP-015
slug: shuttle-seating-assignment-feasibility
title: "Shuttle Seating Assignment Feasibility"
difficulty: Medium
difficulty_score: 50
topics:
  - Topological Sort
  - Directed Acyclic Graph
  - Kahn's Algorithm
tags:
  - graph
  - topological-sort
  - dag
  - kahns-algorithm
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-015: Shuttle Seating Assignment Feasibility

## Problem Statement

Given `n` tasks (numbered 0 to n-1) with directed dependencies (represented as edges where `u → v` means task `u` must be completed before task `v`), determine:
1. Whether a valid ordering of tasks exists (i.e., the graph is a DAG with no cycles)
2. How many nodes had zero in-degree initially (i.e., could be started first)

Return these two pieces of information.

![Problem Illustration](../images/GRP-015/problem-illustration.png)

## Input Format

- First line: integer `n` (number of tasks)
- Second line: integer `m` (number of directed edges/dependencies)
- Next `m` lines: two integers `u v` representing "task u must be completed before task v"

## Output Format

- If a valid ordering exists: Two space-separated integers: `1 count`
  - `1` indicates ordering is possible
  - `count` is the number of tasks with initial in-degree 0
- If no valid ordering exists (cycle detected): `-1`

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`

## Example

**Input:**
```
4
3
0 2
1 2
2 3
```

**Output:**
```
1 2
```

**Explanation:**

Task dependencies:
- Task 0 must be done before task 2
- Task 1 must be done before task 2
- Task 2 must be done before task 3

In-degrees:
- Task 0: in-degree 0 (can start immediately)
- Task 1: in-degree 0 (can start immediately)
- Task 2: in-degree 2 (depends on tasks 0 and 1)
- Task 3: in-degree 1 (depends on task 2)

Valid orderings exist (e.g., [0, 1, 2, 3] or [1, 0, 2, 3]).
Initially, 2 tasks (0 and 1) had in-degree 0.

Output: `1 2`

![Example Visualization](../images/GRP-015/example-1.png)

## Notes

- Use Kahn's algorithm for topological sort
- Initialize in-degrees for all nodes
- Start with all nodes having in-degree 0
- Process nodes by reducing in-degrees of neighbors
- If all nodes are processed → valid ordering exists
- If some nodes remain unprocessed → cycle exists
- Count initial zero in-degree nodes before starting the algorithm
- Time complexity: O(n + m)

## Related Topics

Topological Sort, Kahn's Algorithm, DAG, In-Degree, Cycle Detection, Task Scheduling

---

## Solution Template

### Java


### Python


### C++


### JavaScript
