# LNK-020: Linked List as Event Log

## Problem Statement

Each node is an event of type `+` or `-` with a value. Starting from 0, replaying events adds or subtracts the value.

Operations:

- `APPEND t v`: append event (`t` is `+` or `-`)
- `COMPACT`: merge consecutive events of the same type by summing their values
- `REPLAY l r`: output the replay result of the sublist from position `l` to `r`

## Input Format

- First line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `REPLAY`, output one integer

## Constraints

- `1 <= q <= 200000`
- `1 <= value <= 10^9`
- Total list size <= 200000

## Clarifying Notes

- `COMPACT` applies to the entire current list.
- Positions in `REPLAY` are 1-based in the current list.

## Example Input

```
6
APPEND + 5
APPEND - 2
APPEND - 3
COMPACT
REPLAY 1 2
REPLAY 1 1
```

## Example Output

```
0
5
```
