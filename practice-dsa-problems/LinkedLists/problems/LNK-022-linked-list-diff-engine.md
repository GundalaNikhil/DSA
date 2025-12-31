# LNK-022: Linked List Diff Engine

## Problem Statement

Given two lists `A` and `B`, compute the minimum cost to transform `A` into `B` using these operations:

- Insert a value (cost `ci`)
- Delete a value (cost `cd`)
- Replace a value (cost `cr`)

Order must be preserved.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: list `A`
- Third line: `m` integers: list `B`
- Fourth line: integers `ci`, `cd`, `cr`

## Output Format

- Single integer: minimum cost

## Constraints

- `1 <= n, m <= 2000`
- `0 <= ci, cd, cr <= 10^9`

## Clarifying Notes

- Replacing a value changes it to any other value.

## Example Input

```
3 2
1 3 4
1 4
1 1 2
```

## Example Output

```
1
```
