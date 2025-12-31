# DP-001: Accumulation Threshold DP

## Problem Statement

You have `n` steps and `m` progress meters. Each step you choose exactly one action. Action `i` yields reward `r_i` and adds a vector of progress `g_i[1..m]`. Meter `k` has threshold `T_k`. When a meter reaches its threshold, a corresponding action becomes unlocked and can be used in later steps.

All progress values are capped at their thresholds: any value above `T_k` is treated as `T_k`.

Find the maximum total reward achievable after exactly `n` steps.

## Input Format

- First line: integers `n`, `m`, `a`, `u`
- Second line: `m` integers: thresholds `T_1..T_m`
- Next `a` lines: base actions `r_i` followed by `m` gains
- Next `u` lines: unlocked actions, each line has: `meter_index`, `r_i`, then `m` gains

Each unlocked action is tied to exactly one meter and becomes available only after that meter reaches its threshold.

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= m <= 6`
- `1 <= a <= 12`
- `0 <= u <= 6`
- `0 <= T_k <= 20`
- `-10^9 <= r_i <= 10^9`
- `0 <= g_i[k] <= 20`

## Clarifying Notes

- An unlocked action tied to meter `k` is available only from the first step after progress on meter `k` reaches `T_k`.
- Progress is tracked per meter and capped at its threshold.

## Example Input

```
3 2 2 1
2 2
5 1 0
1 0 1
1 10 1 1
```

## Example Output

```
16
```
