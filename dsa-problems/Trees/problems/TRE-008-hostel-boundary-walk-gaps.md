---
problem_id: TRE_HOSTEL_BOUNDARY_WALK_GAPS__3187
display_id: TRE-008
slug: hostel-boundary-walk-gaps
title: "Hostel Boundary Walk with Gaps"
difficulty: Medium
difficulty_score: 44
topics:
  - Trees
  - Boundary Traversal
  - DFS
tags:
  - trees
  - traversal
  - boundary
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-008: Hostel Boundary Walk with Gaps

## Problem Statement

Return the boundary traversal of a binary tree but skip any boundary node whose value is negative. The boundary traversal includes:

1. Root
2. Left boundary (excluding leaves)
3. All leaves (left to right)
4. Right boundary (excluding leaves) in reverse

Preserve order while skipping negative-valued nodes.

![Problem Illustration](../images/TRE-008/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: boundary traversal values separated by spaces
- If the tree is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
-5 3 -1
15 -1 -1
2 -1 -1
```

**Output:**

```
10 2 15
```

**Explanation:**

Boundary nodes are `10`, `-5`, `2`, and `15`. Skipping the negative value `-5` yields `10 2 15`.

![Example Visualization](../images/TRE-008/example-1.png)

## Notes

- Avoid duplicates when root or leaves appear in multiple boundary parts.
- Skipping applies only to boundary nodes, not to traversal structure.
- Use DFS to collect left boundary, leaves, and right boundary.

## Related Topics

Boundary Traversal, DFS, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

