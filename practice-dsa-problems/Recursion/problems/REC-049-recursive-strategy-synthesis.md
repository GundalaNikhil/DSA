# REC-049: Recursive Strategy Synthesis

## Problem Statement

You are given a game tree. Each node is controlled by Player A or Player B, and leaves are labeled as winning (`1`) or losing (`0`) for Player A.

Define recursive outcomes:

- At a Player A node, A may choose any child. The node is winning if any child is winning.
- At a Player B node, B chooses a child. The node is winning only if all children are winning.

If the root is winning, output one winning strategy for Player A as a sequence of chosen child indices (1-based) along the path taken by A at each of its turns. If multiple strategies exist, choose the lexicographically smallest sequence.

If the root is losing, output `LOSE`.

## Input Format

- First line: integer `n`
- Next `n` lines: `type value parent`
  - `type` is `A`, `B`, or `L` (leaf)
  - For leaves, `value` is `0` or `1`; otherwise `value` is ignored

## Output Format

- If losing: print `LOSE`
- If winning: print `WIN` on the first line, and the strategy sequence on the second line (space-separated indices, or empty if no A moves)

## Constraints

- `1 <= n <= 200000`
- Each internal node has at least one child

## Clarifying Notes

- Child indices are based on the order of input.
- The strategy sequence only records choices at Player A nodes.

## Example Input

```
5
A 0 0
B 0 1
L 1 2
L 0 2
L 1 1
```

## Example Output

```
WIN
2
```
