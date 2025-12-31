# LNK-049: Linked List with Vector Clocks

## Problem Statement

Each update to a node carries a vector clock. Two updates are concurrent if neither clock dominates the other. Count the number of pairs of concurrent updates applied to the same position.

## Input Format

- First line: integers `q` and `d` (clock dimension)
- Next `q` lines: `pos v1 v2 ... vd` (update at position `pos` with vector clock)

## Output Format

- Single integer: number of concurrent pairs at the same position

## Constraints

- `1 <= q <= 200000`
- `1 <= d <= 8`
- `1 <= pos <= 200000`

## Clarifying Notes

- Clock `A` dominates `B` if all components `A[i] >= B[i]` and at least one is strict.

## Example Input

```
3 2
1 1 0
1 0 1
1 2 2
```

## Example Output

```
1
```
