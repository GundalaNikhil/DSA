# LNK-066: Linked List with Quantum Superposition

## Problem Statement

Each node stores two possible values `(a, b)` and a collapse rule. On read at time `t`, the value collapses to:

- `a` if `t` is even
- `b` if `t` is odd

Once a node collapses, it remains at that value for all future reads.

Operations:

- `READ pos t`: output the collapsed value at position `pos` at time `t`

## Input Format

- First line: integer `n`
- Next `n` lines: `a b` for each node
- Next line: integer `q`
- Next `q` lines: `pos t`

## Output Format

- For each `READ`, output the value

## Constraints

- `1 <= n, q <= 200000`
- `0 <= t <= 10^9`

## Clarifying Notes

- Collapse is deterministic based on parity of `t`.

## Example Input

```
2
5 7
1 9
3
1 1
1 2
2 3
```

## Example Output

```
7
7
9
```
