# DP-070: Branch Prediction DP

## Problem Statement

You are given a sequence of branch outcomes `0/1` of length `n`. You may use one of `k` prediction strategies. Strategy `i` has a state machine with `s_i` states, a prediction for each state, and a deterministic next-state function based on the actual outcome.

You may switch strategies at any time with cost `C`. A misprediction costs 1.

Minimize total cost (mispredictions + switch costs).

## Input Format

- First line: integers `n`, `k`, `C`
- Second line: string of length `n` (branch outcomes)
- For each strategy `i`:
  - Line: integer `s_i`
  - Line: `s_i` integers: prediction for each state (0 or 1)
  - Next `s_i` lines: two integers: next state for outcome 0 and outcome 1

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 2000`
- `1 <= k <= 5`
- `1 <= s_i <= 10`
- `0 <= C <= 10^6`

## Clarifying Notes

- Each strategy starts in state 0 when first used.

## Example Input

```
3 1 0
010
2
0 1
0 1
1 0
```

## Example Output

```
1
```
