# REC-054: Recursive Type Checker

## Problem Statement

You are given an expression tree with the following node types:

- `INT x`: integer literal
- `BOOL x`: boolean literal (`0` or `1`)
- `ADD a b`: integer addition
- `AND a b`: boolean and
- `EQ a b`: equality (both operands must have the same type)

Each node refers to its child indices. Determine the type of the root expression (`INT` or `BOOL`). If the expression is not well-typed, output `TYPE_ERROR`.

## Input Format

- First line: integer `n`
- Next `n` lines: a node description
  - Literals: `INT x` or `BOOL x`
  - Operators: `ADD a b`, `AND a b`, `EQ a b`

## Output Format

- `INT`, `BOOL`, or `TYPE_ERROR`

## Constraints

- `1 <= n <= 200000`
- Node indices are 1-based

## Clarifying Notes

- `ADD` requires both operands to be `INT`.
- `AND` requires both operands to be `BOOL`.
- `EQ` is valid only if both operands have the same type.

## Example Input

```
3
INT 5
INT 7
EQ 1 2
```

## Example Output

```
BOOL
```
