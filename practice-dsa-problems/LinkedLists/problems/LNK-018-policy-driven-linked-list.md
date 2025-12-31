# LNK-018: Policy-Driven Linked List

## Problem Statement

Nodes belong to segments. You are given per-segment operation limits: maximum insertions and deletions allowed. Process operations and reject any that would violate limits.

Operations:

- `INS s pos x`: insert value `x` at position `pos` within segment `s`
- `DEL s pos`: delete node at position `pos` within segment `s`
- `COUNT s`: output current size of segment `s`

## Input Format

- First line: integers `n` and `S`
- Second line: `n` integers: node values
- Third line: `n` integers: segment ids in order
- Fourth line: `S` lines: `max_ins max_del` for each segment
- Fifth line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `1 <= S <= n`

## Clarifying Notes

- Insert/delete counters are per segment and include only successful operations.
- Invalid operations are ignored.

## Example Input

```
4 2
1 2 3 4
1 1 2 2
1 0
1 1
3
INS 1 2 9
DEL 2 1
COUNT 2
```

## Example Output

```
1
```
