# REC-036: Recursive Dependency Tracking

## Problem Statement

You are given a directed graph of recursive subproblems. Each node `i` has a base value `base[i]` and depends on a list of other nodes. Define:

`Solve(i) = base[i] + sum(Solve(dep))` for all dependencies `dep` of `i`.

If the dependency graph contains a cycle reachable from the start node `S`, the recursion is invalid.

Compute `Solve(S)` or report `CYCLE`.

## Input Format

- First line: integers `n`, `m`, and `S`
- Second line: `n` integers `base[1..n]`
- Next `m` lines: directed edges `u v` meaning `u` depends on `v`

## Output Format

- If a cycle is reachable from `S`, print `CYCLE`
- Otherwise print `Solve(S)`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `1 <= S <= n`
- `-10^9 <= base[i] <= 10^9`

## Clarifying Notes

- Only cycles reachable from `S` invalidate the recursion.
- Dependencies are evaluated with memoization; each node is computed once if valid.

## Example Input

```
4 3 1
5 2 3 1
1 2
2 3
1 4
```

## Example Output

```
11
```
