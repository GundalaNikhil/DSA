---
problem_id: GRP_COURSE_PLAN_MANDATORY__5183
display_id: GRP-007
slug: course-plan-mandatory-pairs
title: "Course Plan with Mandatory Pairs"
difficulty: Medium
difficulty_score: 55
topics:
  - Topological Sort
  - Directed Acyclic Graph
  - Graph Contraction
tags:
  - graph
  - topological-sort
  - dag
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-007: Course Plan with Mandatory Pairs

## Problem Statement

You are given `n` courses (numbered 0 to n-1) with prerequisite relationships forming a Directed Acyclic Graph (DAG). Additionally, you have pairs of courses that must appear adjacent to each other (in any order) in the final schedule.

Produce a topological ordering of courses that:
1. Respects all prerequisite constraints (if A is a prerequisite of B, A must come before B)
2. Ensures that for each mandatory pair (u, v), courses u and v are adjacent in the final ordering

Return the valid schedule as a list of course numbers. If no valid schedule exists, return an empty list.

![Problem Illustration](../images/GRP-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of courses)
- Second line: integer `m` (number of prerequisite edges)
- Next `m` lines: two integers `u v` representing "course u must be taken before course v"
- Next line: integer `p` (number of mandatory adjacent pairs)
- Next `p` lines: two integers `a b` representing "courses a and b must be adjacent in the schedule"

## Output Format

- If valid ordering exists: space-separated integers representing the course schedule
- If no valid ordering exists: print `-1`

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= p <= 10^5`
- `0 <= u, v, a, b < n`
- The prerequisite graph is guaranteed to be a DAG (no cycles)

## Example

**Input:**
```
4
2
0 2
1 2
1
2 3
```

**Output:**
```
0 1 2 3
```

**Explanation:**

Prerequisites:
- Course 0 must come before course 2
- Course 1 must come before course 2

Mandatory adjacent pair:
- Courses 2 and 3 must be adjacent

One valid ordering is: [0, 1, 2, 3]
- Satisfies 0 → 2 (0 before 2)
- Satisfies 1 → 2 (1 before 2)
- Courses 2 and 3 are adjacent

Another valid ordering would be: [1, 0, 2, 3]

![Example Visualization](../images/GRP-007/example-1.png)

## Notes

- First, verify that prerequisite constraints allow the adjacency pairs (e.g., if A must come before both B and C, then B and C cannot be in an adjacency pair unless one depends on the other)
- One approach: contract each adjacency pair into a super-node, then run topological sort on the contracted graph
- When expanding super-nodes back to individual courses, ensure the pair ordering respects prerequisites
- Use Kahn's algorithm or DFS-based topological sort
- Time complexity: O(n + m + p)

## Related Topics

Topological Sort, DAG, Graph Contraction, Scheduling, Kahn's Algorithm

---

## Solution Template

### Java


### Python


### C++


### JavaScript

