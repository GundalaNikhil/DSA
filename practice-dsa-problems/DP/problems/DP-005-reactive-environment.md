# DP-005: DP with Reactive Environment

## Problem Statement

You have `n` steps and choose one action per step. Each action `i` has immediate cost `c_i` and adds `e_i` to a global environment index `E`. The cost paid for action `i` is:

```
cost = c_i + p * E
```

where `E` is the environment index before taking the action. `E` starts at 0.

Find the minimum total cost after `n` steps.

## Input Format

- First line: integers `n`, `a`, `p`
- Next `a` lines: `c_i e_i`

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 10`
- `0 <= p <= 10`
- `0 <= c_i <= 10^6`
- `0 <= e_i <= 10`
- `E` is capped at `E_max = 2000`

## Clarifying Notes

- The DP state includes step and current `E` (capped at `E_max`).

## Example Input

```
3 2 1
3 2
2 0
```

## Example Output

```
7
```
