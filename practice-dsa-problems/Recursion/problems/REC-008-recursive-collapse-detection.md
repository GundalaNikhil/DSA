# REC-008: Recursive Collapse Detection

## Problem Statement

You are given a directed graph with `n` nodes and a starting node `S`. A recursive traversal computes the sum of node values. If the traversal reaches a node that is already on the current recursion stack, that branch collapses and contributes 0 from that point onward.

Compute the total sum returned by this traversal.

## Input Format

- First line: integers `n`, `m`, `S`
- Second line: `n` integers: node values
- Next `m` lines: edges `u v`

## Output Format

- Single integer: total sum

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- Node values are 32-bit signed integers

## Clarifying Notes

- The traversal visits outgoing edges in increasing order of `v`.
- Each node's value is added once per entry into the node.

## Example Input

```
3 3 1
5 2 1
1 2
2 3
3 2
```

## Example Output

```
7
```
