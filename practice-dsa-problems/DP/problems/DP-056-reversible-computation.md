# DP-056: DP on Reversible Computation

## Problem Statement

You have `n` steps and states `0..S-1`. Each action moves from state `u` to state `v` with cost `c`. Every action has a reverse action with cost `c_rev`.

Find the minimum total cost to start at state 0 and return to state 0 after exactly `n` steps.

## Input Format

- First line: integers `n`, `S`, `a`
- Next `a` lines: `u v c c_rev`

## Output Format

- Single integer: minimum cost, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= S <= 50`
- `1 <= a <= 2000`

## Clarifying Notes

- Reverse actions are not automatic; you must choose them explicitly.

## Example Input

```
2 2 1
0 1 3 1
```

## Example Output

```
4
```
