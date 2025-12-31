# DP-023: DP with Pre-Commitment Penalties

## Problem Statement

You must declare target counts `t_i` for each action `i` before execution. After `n` steps, if the actual counts are `c_i`, you pay penalty `P * sum |c_i - t_i|`.

Choose both the targets and the action sequence to maximize total reward minus penalty.

## Input Format

- First line: integers `n`, `a`, `P`
- Next `a` lines: `reward_i`

## Output Format

- Single integer: maximum achievable score

## Constraints

- `1 <= n <= 60`
- `1 <= a <= 4`
- `0 <= P <= 10^6`
- `-10^6 <= reward_i <= 10^6`

## Clarifying Notes

- Targets `t_i` are non-negative integers summing to `n`.

## Example Input

```
3 2 2
5
4
```

## Example Output

```
13
```
