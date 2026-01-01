---
problem_id: TRE_CAMPUS_DIRECTORY_MULTI_TREE__4813
display_id: TRE-001
slug: campus-directory-multi-tree
title: "Campus Directory Multi-Tree Comparison"
difficulty: Easy
difficulty_score: 28
topics:
  - Trees
  - Traversal
  - Comparison
tags:
  - trees
  - traversal
  - comparison
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-001: Campus Directory Multi-Tree Comparison

## Problem Statement

You are given two binary trees `T1` and `T2`. For each tree, output its preorder, inorder, and postorder traversals.

Then determine whether the two trees are structurally identical (ignoring node values). Also report which traversal types match exactly between the two trees.

![Problem Illustration](../images/TRE-001/problem-illustration.png)

## Input Format

- First line: integer `n1` (number of nodes in `T1`)
- Next `n1` lines: `value left right` for nodes `0..n1-1`
- Next line: integer `n2` (number of nodes in `T2`)
- Next `n2` lines: `value left right` for nodes `0..n2-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` in each tree. If `n=0`, the tree is empty.

## Output Format

- Line 1: preorder of `T1`
- Line 2: inorder of `T1`
- Line 3: postorder of `T1`
- Line 4: preorder of `T2`
- Line 5: inorder of `T2`
- Line 6: postorder of `T2`
- Line 7: `true` or `false` for structural identity
- Line 8: traversal names that match exactly (`preorder`, `inorder`, `postorder`) separated by spaces, or `NONE`

## Constraints

- `0 <= n1, n2 <= 100000`
- Node values fit in 32-bit signed integers
- Input trees are valid (no cycles)

## Example

**Input:**

```
3
2 1 2
1 -1 -1
3 -1 -1
3
1 -1 1
2 -1 2
3 -1 -1
```

**Output:**

```
2 1 3
1 2 3
1 3 2
1 2 3
1 2 3
3 2 1
false
inorder
```

**Explanation:**

Both trees have inorder traversal `1 2 3`, but their structures differ, so `structural_identity=false`.

![Example Visualization](../images/TRE-001/example-1.png)

## Notes

- Structural identity ignores values and checks only left/right child positions.
- Output a blank line for an empty traversal (tree with `n=0`).
- Traversal matching compares sequences of values for the same traversal type.

## Related Topics

Tree Traversals, Tree Comparison, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

