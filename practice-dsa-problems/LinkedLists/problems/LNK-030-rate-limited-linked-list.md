# LNK-030: Rate-Limited Linked List

## Problem Statement

Each node has a cooldown `C` (global). Any modification to a node is allowed only if at least `C` time units have passed since its last modification.

Each operation provides a timestamp `t`.

Operations:

- `SET pos x t`: set value at position `pos` to `x` if cooldown allows
- `DEL pos t`: delete node at position `pos` if cooldown allows
- `GET pos`: output value at position `pos` or `-1`

If a modification is blocked by cooldown, it is ignored.

## Input Format

- First line: integers `n` and `C`
- Second line: `n` integers: list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `0 <= C <= 10^9`
- Timestamps are non-decreasing

## Clarifying Notes

- Deleting a node counts as a modification to that node.
- After deletion, the node is gone and cooldown is irrelevant.

## Example Input

```
3 5
1 2 3
4
SET 2 9 1
SET 2 8 3
GET 2
SET 2 7 7
```

## Example Output

```
9
```
