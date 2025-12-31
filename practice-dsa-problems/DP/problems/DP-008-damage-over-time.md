# DP-008: DP with Damage Over Time

## Problem Statement

You have `n` turns and `a` actions. Action `i` applies immediate damage `d_i` and a DoT effect that lasts `t_i` turns, dealing `s_i` damage per turn.

DoT effects stack independently. At each turn, all active effects deal damage before the new action is chosen.

Maximize total damage after `n` turns.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `d_i t_i s_i`

## Output Format

- Single integer: maximum total damage

## Constraints

- `1 <= n <= 25`
- `1 <= a <= 6`
- `0 <= d_i, s_i <= 50`
- `0 <= t_i <= 5`

## Clarifying Notes

- Effects with `t_i = 0` have only immediate damage.
- State tracks remaining durations of active effects (capped by `t_i`).

## Example Input

```
2 2
3 1 2
1 2 1
```

## Example Output

```
7
```
