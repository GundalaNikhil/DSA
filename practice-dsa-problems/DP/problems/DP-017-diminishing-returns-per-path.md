# DP-017: DP with Diminishing Returns per Path

## Problem Statement

You have `p` paths. Choosing path `i` for the `k`-th time yields reward `R[i][k]` (non-increasing in `k`). You must make exactly `n` choices.

Maximize total reward.

## Input Format

- First line: integers `n` and `p`
- Next `p` lines: `n` integers: reward table for each path (rewards for the 1st..n-th use)

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= p <= 10`
- `-10^9 <= R[i][k] <= 10^9`

## Clarifying Notes

- Each path can be chosen at most `n` times.

## Example Input

```
3 2
5 3 1
4 2 2
```

## Example Output

```
11
```
