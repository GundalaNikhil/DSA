# LNK-012: Energy-Based Traversal List

## Problem Statement

You are given a linked list of `n` nodes. Each node has a traversal cost `w[i]` and an optional jump pointer `j[i]` (0 means no jump). Starting at the head (node 1), you may move either to `next` or `jump`. Moving to a node incurs its cost.

Given an energy budget `E`, determine the maximum node index reachable without exceeding total cost `E`. If the head cost exceeds `E`, output `0`.

## Input Format

- First line: integer `n`
- Second line: `n` integers: weights `w[1..n]`
- Third line: `n` integers: jump indices `j[1..n]` (0 if none)
- Fourth line: integer `q`
- Next `q` lines: budgets `E`

## Output Format

- For each query, output the maximum reachable node index

## Constraints

- `1 <= n, q <= 200000`
- `0 <= w[i] <= 10^9`
- `0 <= j[i] <= n`

## Clarifying Notes

- The list is 1 -> 2 -> ... -> n by next pointers.
- You may choose moves to maximize the reachable index.

## Example Input

```
5
2 3 5 1 4
3 0 5 0 0
3
2
6
10
```

## Example Output

```
1
2
5
```
