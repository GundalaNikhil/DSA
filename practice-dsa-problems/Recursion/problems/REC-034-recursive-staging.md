# REC-034: Recursive Staging

## Problem Statement

You are given a rooted tree and a sequence of stage thresholds `T[1..S]`. Each node has a value `v`.

For each stage `s`, define the stage value of a node as:

- `stageValue(node, s) = v[node] + sum(stageValue(child, s))`

A node passes stage `s` if `stageValue(node, s) >= T[s]`. A node may attempt stage `s+1` only if it passes stage `s`.

Compute the maximum stage that the root can pass.

## Input Format

- First line: integers `n` and `S`
- Second line: `S` integers `T[1..S]`
- Next `n` lines: `v parent` (parent is 0 for root)

## Output Format

- Single integer: maximum stage passed by the root (0 if it fails stage 1)

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 60`
- `-10^9 <= v <= 10^9`
- `-10^15 <= T[s] <= 10^15`

## Clarifying Notes

- The same stage threshold is used for all nodes at stage `s`.
- A node that fails stage `s` does not contribute to higher stages.

## Example Input

```
3 2
5 12
4 0
3 1
2 1
```

## Example Output

```
2
```
