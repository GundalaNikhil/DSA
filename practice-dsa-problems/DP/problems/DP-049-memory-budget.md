# DP-049: DP with Memory Budget

## Problem Statement

You have `n` steps and `a` actions. Each action adds a value `v_i`. The DP state is the current sum. After each step, you may keep at most `K` states; all others are discarded. The objective is to maximize the final sum after `n` steps given optimal pruning.

## Input Format

- First line: integers `n`, `a`, `K`
- Second line: `a` integers: values `v_1..v_a`

## Output Format

- Single integer: maximum reachable sum after `n` steps

## Constraints

- `1 <= n <= 60`
- `1 <= a <= 10`
- `1 <= K <= 2000`
- `-10^6 <= v_i <= 10^6`

## Clarifying Notes

- If multiple states have the same sum, keep only one.

## Example Input

```
3 2 2
5 -1
```

## Example Output

```
15
```
