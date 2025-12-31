# DP-022: DP on Weighted History

## Problem Statement

You have `n` steps and choose one of `a` actions each step. The reward for choosing action `i` at step `t` is:

```
base_i - w_i * H_i
```

where `H_i` is the exponentially decayed count of past uses of action `i`:

```
H_i(t) = sum_{k < t and action_k = i} alpha^{t-k}
```

You are given `alpha` as a fraction `p/q`. Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `p`, `q`
- Next `a` lines: `base_i w_i`

## Output Format

- Single integer: maximum total reward multiplied by `q^n`

## Constraints

- `1 <= n <= 20`
- `1 <= a <= 5`
- `0 <= p <= q <= 5`
- `0 <= base_i, w_i <= 10`

## Clarifying Notes

- Use exact arithmetic; scale rewards by `q^n` to keep integers.

## Example Input

```
2 1 1 2
4 1
```

## Example Output

```
12
```
