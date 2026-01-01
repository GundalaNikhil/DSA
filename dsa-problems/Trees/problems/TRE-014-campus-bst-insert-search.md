---
problem_id: TRE_CAMPUS_BST_INSERT_SEARCH__2824
display_id: TRE-014
slug: campus-bst-insert-search
title: "Campus BST Insert & Search"
difficulty: Easy
difficulty_score: 30
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - insertion
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-014: Campus BST Insert & Search

## Problem Statement

Build a binary search tree (BST) by inserting values in the given order. Then search for a target value.

Output the inorder traversal of the final BST and the result of the search.

![Problem Illustration](../images/TRE-014/problem-illustration.png)

## Input Format

- First line: integer `n`, number of values to insert
- Second line: `n` integers, the insertion order
- Third line: integer `x`, the value to search

Duplicates, if any, must be inserted into the right subtree.

## Output Format

- Line 1: inorder traversal of the BST (space-separated)
- Line 2: `true` if `x` exists in the BST, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Values fit in 32-bit signed integers

## Example

**Input:**

```
5
4 2 6 1 3
5
```

**Output:**

```
1 2 3 4 6
false
```

**Explanation:**

After insertion, the BST inorder traversal is sorted. The value `5` is not present.

![Example Visualization](../images/TRE-014/example-1.png)

## Notes

- If `n=0`, the inorder traversal is empty and search is `false`.
- Inorder traversal of a BST is non-decreasing.
- Insertion uses standard BST rules with duplicates to the right.

## Related Topics

Binary Search Trees, Insertion, Traversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

