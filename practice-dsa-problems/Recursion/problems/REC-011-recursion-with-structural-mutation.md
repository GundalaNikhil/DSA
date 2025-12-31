# REC-011: Recursion with Structural Mutation

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
