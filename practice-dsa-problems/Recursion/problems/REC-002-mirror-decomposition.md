# REC-002: Mirror Decomposition

## Problem Statement

Given a rooted binary tree, determine whether the tree is mirror-symmetric. The tree is mirror-symmetric if, for every node, its left subtree is the mirror of its right subtree.

## Input Format

- First line: integer `n`
- Next `n` lines: `value left right` where `left` and `right` are child ids (0 if null)

Root is node `1`.

## Output Format

- `YES` if the tree is mirror-symmetric, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- Node ids are 1-based
- Values are 32-bit signed integers

## Clarifying Notes

- Mirror comparison checks both structure and values.

## Example Input

```
3
1 2 3
2 0 0
2 0 0
```

## Example Output

```
YES
```
