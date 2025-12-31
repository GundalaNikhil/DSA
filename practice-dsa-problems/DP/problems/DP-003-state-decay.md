# DP-003: DP with State Decay

## Problem Statement

You have `m` states and must choose one state per step for `n` steps. Each state `s` has a base value `v_s`. If a state has not been chosen for `t` steps, its effective value decays to `max(0, v_s - d * t)`.

When you choose a state, you gain its current effective value and its decay timer resets to 0. Other states' timers increase by 1 (capped at `D`).

Maximize total gained value.

## Input Format

- First line: integers `n`, `m`, `d`, `D`
- Second line: `m` integers: base values `v_1..v_m`

## Output Format

- Single integer: maximum total gain

## Constraints

- `1 <= n <= 30`
- `1 <= m <= 6`
- `0 <= d <= 10`
- `1 <= D <= 10`
- `0 <= v_s <= 50`

## Clarifying Notes

- Decay timers are capped at `D` for state space reduction.
- Initial timers are 0 for all states.

## Example Input

```
3 2 2 3
5 4
```

## Example Output

```
13
```
