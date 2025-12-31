# REC-019: Recursion with Depth-Dependent Semantics

## Problem Statement

You are given an expression tree with operators `+` and `*` and integer leaves. The meaning of operators depends on depth:

- At even depth, `+` means max, `*` means min.
- At odd depth, `+` means min, `*` means max.

Compute the value of the expression.

## Input Format

- First line: integer `n`
- Next `n` lines: `type value left right`

`type` is `0` for leaf (value is used) and `1` for operator (value is `+` or `*`). Children are 0 for null.

Root is node `1`.

## Output Format

- Single integer: expression value

## Constraints

- `1 <= n <= 200000`
- Leaf values are 32-bit signed integers

## Clarifying Notes

- Depth of root is 0.

## Example Input

```
3
1 + 2 3
0 5 0 0
0 2 0 0
```

## Example Output

```
5
```
