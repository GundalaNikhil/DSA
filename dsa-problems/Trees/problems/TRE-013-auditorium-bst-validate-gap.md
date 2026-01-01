---
problem_id: TRE_AUDITORIUM_BST_VALIDATE_GAP__6370
display_id: TRE-013
slug: auditorium-bst-validate-gap
title: "Auditorium BST Validate with Gap"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - BST
  - Validation
tags:
  - trees
  - bst
  - validation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-013: Auditorium BST Validate with Gap

## Problem Statement

Validate that a binary tree is a binary search tree (BST) and that every parent-child edge also satisfies a strict gap rule:

`|parent.value - child.value| >= G`

Return `true` if both conditions hold, otherwise `false`.

![Problem Illustration](../images/TRE-013/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`
- Last line: integer `G`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if the tree is a valid BST with the gap rule, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Node values fit in 64-bit signed integers
- `0 <= G <= 10^12`

## Example

**Input:**

```
3
5 1 2
1 -1 -1
7 -1 -1
2
```

**Output:**

```
true
```

**Explanation:**

The tree is a BST, and both edges have gaps at least 2.

![Example Visualization](../images/TRE-013/example-1.png)

## Notes

- The BST property uses strict ordering (`left < node < right`).
- Gap rule applies only to parent-child edges.
- Use DFS with min/max bounds for validation.

## Related Topics

Binary Search Trees, Validation, DFS

---

## Solution Template

### Java


### Python


### C++


### JavaScript

