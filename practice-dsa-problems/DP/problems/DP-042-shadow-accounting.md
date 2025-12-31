# DP-042: DP with Shadow Accounting

## Problem Statement

Each action has a primary reward `r_i` and a shadow cost `s_i`. The shadow balance starts at 0 and must never drop below 0. When you take an action, shadow balance changes by `s_i`.

Maximize total primary reward over `n` steps.

## Input Format

- First line: integers `n`, `a`
- Next `a` lines: `r_i s_i`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 20`
- `-10 <= s_i <= 10`
- `-10^9 <= r_i <= 10^9`
- Shadow balance is capped at 200 for DP.

## Clarifying Notes

- If an action would make shadow balance negative, it cannot be chosen.

## Example Input

```
3 2
5 -1
2 1
```

## Example Output

```
9
```
