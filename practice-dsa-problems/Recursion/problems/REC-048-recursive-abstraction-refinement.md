# REC-048: Recursive Abstraction Refinement

## Problem Statement

You are given an `N x N` grid, where `N` is a power of two. A square region is considered stable if the difference between its maximum and minimum values is at most `T`.

Define a recursive refinement:

- If a region is stable, stop.
- Otherwise, split it into four equal quadrants and refine each quadrant.

Compute the number of final regions (leaf regions) after full refinement.

## Input Format

- First line: integers `N` and `T`
- Next `N` lines: `N` integers each

## Output Format

- Single integer: number of leaf regions

## Constraints

- `1 <= N <= 512`
- `N` is a power of two
- `0 <= T <= 10^9`
- `-10^9 <= grid[i][j] <= 10^9`

## Clarifying Notes

- Refinement is recursive and must follow strict quadrants.
- A single cell is always stable.

## Example Input

```
2 0
1 2
1 2
```

## Example Output

```
4
```
