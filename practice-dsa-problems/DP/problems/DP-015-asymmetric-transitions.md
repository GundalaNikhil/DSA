# DP-015: DP with Asymmetric Transitions

## Problem Statement

You are on a line of positions `1..m`. You must take exactly `n` moves starting at position 1. A move can be:

- Forward: `i -> i+1` with cost `f_i`
- Backward: `i -> i-1` with penalty `b_i`

Forward costs and backward penalties are different. Minimize total cost to end at position `m` after exactly `n` moves.

## Input Format

- First line: integers `n` and `m`
- Second line: `m-1` integers: forward costs `f_1..f_{m-1}`
- Third line: `m-1` integers: backward penalties `b_2..b_m`

## Output Format

- Single integer: minimum total cost, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `2 <= m <= 50`
- `0 <= costs <= 10^6`

## Clarifying Notes

- Backward penalties `b_i` apply when moving from `i` to `i-1`.

## Example Input

```
4 3
1 2
5 4
```

## Example Output

```
4
```
