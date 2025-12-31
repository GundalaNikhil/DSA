# DP-055: DP with Partial Observability

## Problem Statement

There are `s` hidden modes. You maintain a belief distribution over modes. At each step you choose an action; each action has a deterministic observation function that reveals a symbol depending on the current mode. You are given the transition matrix for modes.

Compute the maximum expected reward over `n` steps.

## Input Format

- First line: integers `n`, `s`, `a`, `o`
- Second line: `s` integers: initial probabilities scaled by 1000
- Next `a` blocks:
  - `s` integers: reward per mode
  - `s` integers: observation symbol per mode (0..o-1)
- Next `s` lines: `s` integers: transition probabilities scaled by 1000

## Output Format

- Single integer: maximum expected reward scaled by 1000^n

## Constraints

- `1 <= n <= 10`
- `1 <= s <= 6`
- `1 <= a <= 4`
- `1 <= o <= 6`

## Clarifying Notes

- Use exact arithmetic with scaled probabilities.

## Example Input

```
1 2 1 2
500 500
10 0
0 1
1000 0
0 1000
```

## Example Output

```
5000
```
