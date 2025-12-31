# DP-040: DP with Compositional State

## Problem Statement

Your state is a pair `(x, y)` where `x` in `[0..X]` and `y` in `[0..Y]`. Each action updates `x` and `y` by different deltas and yields reward `r`.

Find the maximum total reward after exactly `n` steps, starting from `(0, 0)` and staying within bounds.

## Input Format

- First line: integers `n`, `X`, `Y`, `a`
- Next `a` lines: `dx dy r`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `0 <= X, Y <= 50`
- `-10^9 <= r <= 10^9`

## Clarifying Notes

- `dx` and `dy` can be negative but bounds must be respected.

## Example Input

```
2 2 2 2
1 0 3
0 1 4
```

## Example Output

```
7
```
