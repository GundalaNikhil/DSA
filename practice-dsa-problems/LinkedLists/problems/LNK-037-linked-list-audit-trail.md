# LNK-037: Linked List with Audit Trail

## Problem Statement

You are given a log of timestamped updates to a list. For each query `(pos, t)`, report the value at position `pos` at time `t`.

Operations:

- `SET pos x t`
- `INS pos x t`
- `DEL pos t`
- `QUERY pos t`

Times are non-decreasing.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values at time 0
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `QUERY`, output the value or `-1` if out of range at time `t`

## Constraints

- `1 <= n, q <= 200000`
- `0 <= t <= 10^9`

## Clarifying Notes

- Updates at time `t` are visible to queries with the same `t`.

## Example Input

```
2
7 8
3
SET 1 5 1
QUERY 1 1
QUERY 2 1
```

## Example Output

```
5
8
```
