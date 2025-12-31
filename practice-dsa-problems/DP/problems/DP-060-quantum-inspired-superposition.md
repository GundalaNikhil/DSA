# DP-060: DP with Quantum-Inspired Superposition

## Problem Statement

Your system has two possible states `A` and `B` with amplitudes `(x, y)` (integers). Each action applies a linear transform:

```
(x', y') = (a*x + b*y, c*x + d*y)
```

At a measurement step, the state collapses to `A` if `x >= y`, otherwise to `B`. After collapse, amplitudes reset to `(1,0)` for `A` or `(0,1)` for `B`.

You must choose actions over `n` steps, and you may measure at any step. Reward is 1 each time the system collapses to `A` and 0 otherwise. Maximize total reward.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `a b c d` (transform matrix)

## Output Format

- Single integer: maximum reward

## Constraints

- `1 <= n <= 30`
- `1 <= a <= 6`
- `-5 <= a,b,c,d <= 5`

## Clarifying Notes

- You may measure at most once per step (either measure or apply a transform).
- This is deterministic; collapse rule is based on `x` and `y`.

## Example Input

```
2 1
1 1 0 1
```

## Example Output

```
2
```
