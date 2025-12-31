# LNK-043: Linked List Consensus Protocol

## Problem Statement

For each round, multiple replicas propose a value to set at a position. A value is **committed** if it receives at least `M` votes (majority threshold). If multiple values reach `M`, choose the smallest value.

Output the committed value for each round, or `-1` if no value reaches threshold.

## Input Format

- First line: integers `R` and `M`
- Second line: integer `t` (number of rounds)
- For each round:
  - Line: integer `p` (number of proposals)
  - Next `p` lines: `replica_id value`

## Output Format

- `t` lines: committed value per round or `-1`

## Constraints

- `1 <= R <= 200000`
- `1 <= M <= R`
- Total proposals <= 200000

## Clarifying Notes

- A replica may propose at most one value per round.

## Example Input

```
3 2
2
3
1 5
2 5
3 7
2
1 4
2 6
```

## Example Output

```
5
-1
```
