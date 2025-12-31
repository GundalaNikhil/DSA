# LNK-040: Linked List with Quorum Reads

## Problem Statement

There are `R` replicas of a linked list. Updates can target any replica. A read returns a value only if at least `Q` replicas agree on that value at a position.

Operations:

- `SET r pos x`: set replica `r` at `pos` to `x`
- `READ pos Q`: output the agreed value if at least `Q` replicas match; otherwise output `CONFLICT`

## Input Format

- First line: integers `n`, `R`, `q`
- Second line: `n` integers: initial list values (all replicas start identical)
- Next `q` lines: operations

## Output Format

- For each `READ`, output the value or `CONFLICT`

## Constraints

- `1 <= n, q <= 200000`
- `1 <= R <= 20`

## Clarifying Notes

- If multiple values each reach quorum, choose the smallest value.

## Example Input

```
3 3 4
1 2 3
SET 1 2 9
SET 2 2 9
READ 2 2
READ 2 3
```

## Example Output

```
9
CONFLICT
```
