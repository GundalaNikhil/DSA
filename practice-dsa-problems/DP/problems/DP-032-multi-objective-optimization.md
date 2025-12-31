# DP-032: DP with Multi-Objective Optimization

## Problem Statement

You must choose one action per step for `n` steps. Action `i` yields reward `r_i` and fatigue `f_i`.

Maximize total reward. If multiple sequences achieve the same maximum reward, choose the one with minimum total fatigue.

Output both values.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `r_i f_i`

## Output Format

- Two integers: maximum reward and corresponding minimum fatigue

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 20`
- `-10^9 <= r_i, f_i <= 10^9`

## Clarifying Notes

- Tie-breaking is applied only after maximizing reward.

## Example Input

```
2 2
5 3
5 1
```

## Example Output

```
10 2
```
