# DP-044: DP on Multi-Scale Time

## Problem Statement

You have `n` steps grouped into blocks of size `K` (n is divisible by K). At the start of each block, you choose a slow action `s` that sets a multiplier `m_s` for the entire block. Each step in the block chooses a fast action `f` with base reward `r_f`. The reward for a step is `m_s * r_f`.

Maximize total reward.

## Input Format

- First line: integers `n`, `K`, `S`, `F`
- Second line: `S` integers: multipliers `m_s`
- Third line: `F` integers: rewards `r_f`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= K <= n`, `n % K == 0`
- `1 <= S, F <= 10`
- `-10 <= m_s, r_f <= 10`

## Clarifying Notes

- Multipliers and rewards can be negative.

## Example Input

```
4 2 2 2
2 -1
3 1
```

## Example Output

```
8
```
