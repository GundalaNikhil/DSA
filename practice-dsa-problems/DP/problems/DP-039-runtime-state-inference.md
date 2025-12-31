# DP-039: DP with Runtime State Inference

## Problem Statement

You traverse `n` steps. There are `s` possible hidden modes. At step `i`, you choose an action `a`. The system deterministically reveals the current mode based on `(i, a)` using a table, and the next mode is fixed. You then gain reward `R[i][mode]`.

Maximize total reward.

## Input Format

- First line: integers `n`, `s`, `a`
- Next `n` lines: `s` integers: rewards `R[i][1..s]`
- Next `n` lines: `a` integers: reveal table `mode(i, action)` (1..s)

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= s <= 10`
- `1 <= a <= 10`

## Clarifying Notes

- Mode revealed at step `i` is also the mode used for reward at step `i`.

## Example Input

```
2 2 2
5 1
2 4
1 2
2 1
```

## Example Output

```
9
```
