# DP-035: DP with Structural Mutation

## Problem Statement

You traverse a graph of `m` nodes for `n` steps. Each action moves along an edge and yields reward. Some edges are **fragile** and disappear permanently after being used once.

Maximize total reward.

## Input Format

- First line: integers `n`, `m`, `e`
- Next `e` lines: `u v reward fragile` (fragile is 0 or 1)

## Output Format

- Single integer: maximum total reward starting from node 1

## Constraints

- `1 <= n <= 20`
- `1 <= m <= 12`
- `1 <= e <= 50`
- `-10^9 <= reward <= 10^9`

## Clarifying Notes

- You can traverse an edge in either direction only if it exists.
- State includes current node and which fragile edges remain.

## Example Input

```
3 3 3
1 2 5 1
2 3 4 0
1 3 2 1
```

## Example Output

```
11
```
