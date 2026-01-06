---
problem_id: MAT_MATRIX_STATE_MACHINE__8579
display_id: NTB-MAT-8579
slug: matrix-state-machine
title: "Matrix State Machine"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - grids
  - matrix
  - matrix-state-machine
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix State Machine

## Problem Statement

You are given an `n x m` matrix with states in `0..S-1`. At each step, all cells update simultaneously:

1. Find the most frequent state among the 4-directional neighbors.
2. If there is a tie, choose the smallest state.
3. The new state is `(current_state + majority_state) mod S`.

Simulate the system until a previous state reappears.

- If the system reaches a fixed point, output the step count and the stable matrix.
- Otherwise, output the cycle length and the first matrix in the cycle.

## Input Format

- First line: integers `n`, `m`, `S`
- Next `n` lines: `m` integers (initial states)

## Output Format

- If fixed: `FIXED t` followed by the matrix at step `t`
- If cyclic: `CYCLE p` followed by the matrix at the first step of the cycle

## Constraints

- `1 <= n, m <= 10`
- `2 <= S <= 10`

## Clarifying Notes

- Step count `t` is 0 if the initial matrix is already fixed.
- Use hash or map to detect repeats.

## Example Input

```
2 2 3
0 1
2 0
```

## Example Output

```
CYCLE 2
0 1
2 0
```
