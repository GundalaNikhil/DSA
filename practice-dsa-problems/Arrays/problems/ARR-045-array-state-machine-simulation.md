# ARR-045: Array State Machine Simulation

## Problem Statement

You are given a deterministic state machine with `S` states labeled `0..S-1` and a base `B`. A transition table `T` is provided where `T[s][b]` gives the next state from state `s` when the input bucket is `b`.

Given an array `a1..an`, process it left to right. For each element:

```
b = ((a_i % B) + B) % B
state = T[state][b]
```

You start in state `0`. Count how many times each state is visited (including the initial state before any elements). Output the visit counts for states `0..S-1`.

## Input Format

- First line: integers `n`, `S`, and `B`
- Second line: `n` integers `a1 a2 ... an`
- Next `S` lines: `B` integers each, the transition table `T`

## Output Format

- `S` integers: visit counts for states `0..S-1`

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 2000`
- `1 <= B <= 2000`
- `-10^9 <= a_i <= 10^9`
- `0 <= T[s][b] <= S-1`

## Clarifying Notes

- The initial state `0` counts as one visit before processing the array.
- The process is fully deterministic given the inputs.

## Example Input

```
5 3 2
1 2 3 4 5
1 2
2 0
0 1
```

## Example Output

```
2 2 2
```
