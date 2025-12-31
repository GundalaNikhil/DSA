# DP-013: Budgeted DP with Variable State Cost

## Problem Statement

You have `n` steps and `s` states. Each state `j` has a base cost `b_j` and a dynamic surcharge `u_j` (initially 0). At step `i`, choosing state `j` costs `b_j + u_j`.

After choosing state `j`, its surcharge increases by `inc_j` (capped at `U`), and all other surcharges decrease by `dec` (floored at 0).

You have a total budget `B`. Find the maximum number of steps you can complete within budget `B`.

## Input Format

- First line: integers `n`, `s`, `B`, `U`, `dec`
- Next `s` lines: `b_j inc_j`

## Output Format

- Single integer: maximum steps completed (0..n)

## Constraints

- `1 <= n <= 200`
- `1 <= s <= 4`
- `0 <= B <= 10^6`
- `0 <= U <= 10`
- `0 <= b_j, inc_j, dec <= 10`

## Clarifying Notes

- Surcharges are capped in `[0, U]`.

## Example Input

```
5 2 12 5 1
2 2
3 1
```

## Example Output

```
5
```
