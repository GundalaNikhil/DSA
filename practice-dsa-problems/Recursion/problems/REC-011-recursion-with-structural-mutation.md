---
problem_id: REC_RECURSION_WITH_STRUCTURAL_MUTATION__1777
display_id: NTB-REC-1777
slug: recursion-with-structural-mutation
title: "Recursion with Structural Mutation"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursion-with-structural-mutation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursion with Structural Mutation

## Problem Statement

You are given a rooted binary tree. A recursive traversal mutates the tree while it runs:

- If a node's value is even, its right child is removed before any recursive calls.
- If a node's value is odd, its left and right children are swapped before any recursive calls.

After mutations, the traversal visits left child then right child (if they exist). Compute the sum of values visited.

## Input Format

- First line: integer `n`
- Next `n` lines: `value left right` (child ids, 0 if null)

Root is node `1`.

## Output Format

- Single integer: sum of visited values

## Constraints

- `1 <= n <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- Mutations affect all future recursive calls.
- Removed children are never visited.

## Example Input

```
3
2 2 3
1 0 0
1 0 0
```

## Example Output

```
3
```
