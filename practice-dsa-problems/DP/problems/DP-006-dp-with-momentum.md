# DP-006: DP with Momentum

## Problem Statement

You have `n` steps and `a` actions. Choosing the same action consecutively builds momentum. Let `streak` be the number of consecutive uses of the current action (capped at `M`). The reward for using action `i` is:

```
reward = base_i + bonus_i * streak
```

Switching actions resets streak to 1 and also applies a switch penalty `P` (subtracted from reward).

Maximize total reward over `n` steps.

## Input Format

- First line: integers `n`, `a`, `M`, `P`
- Next `a` lines: `base_i bonus_i`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 8`
- `1 <= M <= 10`
- `0 <= P <= 10^6`

## Clarifying Notes

- Streak is capped at `M`.

## Example Input

```
3 2 2 1
5 2
4 3
```

## Example Output

```
18
```
