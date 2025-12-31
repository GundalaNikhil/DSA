# LNK-041: Linked List State Machine

## Problem Statement

Each node is a state in `0..S-1`. A list is **valid** if for every adjacent pair `(u, v)`, the transition `u -> v` is allowed by a given transition matrix.

You must process updates and output whether the list is valid after each update.

Operations:

- `SET pos x`: set the state at position `pos` to `x`

## Input Format

- First line: integers `n` and `S`
- Second line: `n` integers: initial states
- Next `S` lines: `S` integers (0/1) transition matrix
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- After each update, output `VALID` or `INVALID`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= S <= 50`

## Clarifying Notes

- A list with one node is always valid.

## Example Input

```
3 2
0 1 0
1 1
0 1
2
SET 2 0
SET 3 1
```

## Example Output

```
VALID
INVALID
```
