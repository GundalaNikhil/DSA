---
problem_id: TRE_SHUTTLE_BST_KTH_SMALLEST_RANGE__4916
display_id: TRE-015
slug: shuttle-bst-kth-smallest-range
title: "Shuttle BST Kth Smallest in Range"
difficulty: Medium
difficulty_score: 52
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - kth-smallest
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-015: Shuttle BST Kth Smallest in Range

## Problem Statement

Build a BST by inserting values in the given order. Given a range `[L, R]` and an integer `k`, return the k-th smallest value within the range (1-indexed among in-range values).

If fewer than `k` values fall in the range, output `-1`.

![Problem Illustration](../images/TRE-015/problem-illustration.png)

## Input Format

- First line: integer `n`, number of values to insert
- Second line: `n` integers, the insertion order
- Third line: integers `L` and `R`
- Fourth line: integer `k`

Duplicates, if any, must be inserted into the right subtree.

## Output Format

- Single integer: the k-th smallest value in `[L, R]`, or `-1` if not enough values

## Constraints

- `1 <= n <= 100000`
- Values fit in 64-bit signed integers
- `1 <= k <= n`

## Example

**Input:**

```
5
2 4 5 7 9
4 8
2
```

**Output:**

```
5
```

**Explanation:**

Values in the range `[4, 8]` are `[4, 5, 7]`. The 2nd smallest is 5.

![Example Visualization](../images/TRE-015/example-1.png)

## Notes

- Use inorder traversal and skip values outside the range.
- Stop early once `k` elements are counted.
- If `n=0`, output `-1`.

## Related Topics

BST, Inorder Traversal, Range Queries

---

## Solution Template

### Java


### Python


### C++


### JavaScript

