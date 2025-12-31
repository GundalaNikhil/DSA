# DP-030: DP with Global Invariant

## Problem Statement

You must choose one value per step from a set of actions. Each action `i` adds `v_i` to a running sum and yields reward `r_i`. After `n` steps, the running sum must satisfy `sum % M = 0`.

Maximize total reward while respecting the invariant.

## Input Format

- First line: integers `n`, `a`, `M`
- Next `a` lines: `v_i r_i`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 2000`
- `1 <= a <= 20`
- `1 <= M <= 2000`
- `-10^9 <= v_i, r_i <= 10^9`

## Clarifying Notes

- The invariant is checked only at the end.

## Example Input

```
3 2 5
2 4
3 1
```

## Example Output

```
6
```
