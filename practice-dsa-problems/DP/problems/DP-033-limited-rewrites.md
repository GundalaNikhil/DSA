# DP-033: DP with Limited Rewrites

## Problem Statement

You build a sequence of `n` actions. After choosing the action for step `i`, you may rewrite any one of the previous `W` steps to a different action. You may perform at most `K` rewrites total.

Each action `j` yields reward `r_j` for the step it occupies. Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `W`, `K`
- Second line: `a` integers: rewards `r_1..r_a`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 50`
- `1 <= a <= 6`
- `1 <= W <= n`
- `0 <= K <= 10`

## Clarifying Notes

- A rewrite changes only the action choice, not the step order.

## Example Input

```
3 2 2 1
5 1
```

## Example Output

```
15
```
