# LNK-031: Linked List with Read Replicas

## Problem Statement

You have a primary linked list and `R` read-only replicas. Updates are applied to the primary immediately and to each replica after a fixed delay `D` (in time units).

Operations:

- `SET pos x t`: update primary at time `t`
- `GET r pos t`: read from replica `r` at time `t`

A replica reflects all primary updates with `time <= t - D`.

## Input Format

- First line: integers `n`, `R`, `D`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output the value at `pos` in replica `r`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= R <= 10`
- Timestamps are non-decreasing

## Clarifying Notes

- If `t < D`, replicas show the initial state.

## Example Input

```
3 1 5
1 2 3
3
SET 2 9 3
GET 1 2 6
GET 1 2 7
```

## Example Output

```
2
9
```
