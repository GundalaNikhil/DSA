# DP-019: DP with Maintenance Windows

## Problem Statement

You have `n` time slots. In each slot you may perform a task earning reward `v_i`, or do maintenance earning 0. You must schedule maintenance so that there is **at least one maintenance slot in every window of length `W`**.

Maximize total reward.

## Input Format

- First line: integers `n` and `W`
- Second line: `n` integers: rewards `v_1..v_n`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200000`
- `1 <= W <= n`
- `-10^9 <= v_i <= 10^9`

## Clarifying Notes

- This is equivalent to choosing maintenance positions to satisfy sliding-window constraints.

## Example Input

```
5 3
5 4 3 2 1
```

## Example Output

```
9
```
