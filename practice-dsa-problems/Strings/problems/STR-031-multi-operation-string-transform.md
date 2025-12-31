# STR-031: Multi-Operation String Transform

## Problem Statement

Given strings `A` and `B`, transform `A` into `B` with minimum cost. Allowed operations:

- `SWAP`: swap two adjacent characters in the current string (cost `cs`).
- `REPLACE`: replace one character with another (cost `cr`).
- `INSERT`: insert one character (cost `ci`).
- `DELETE`: delete one character (cost `cd`).

Find the minimum total cost.

## Input Format

- First line: string `A`
- Second line: string `B`
- Third line: integers `cs cr ci cd`

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= |A|, |B| <= 2000`
- `0 <= cs, cr, ci, cd <= 10^9`
- Strings contain only lowercase English letters

## Clarifying Notes

- All operations can be applied any number of times.

## Example Input

```
horse
ros
1 2 1 1
```

## Example Output

```
3
```
