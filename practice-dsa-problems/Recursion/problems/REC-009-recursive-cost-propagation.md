# REC-009: Recursive Cost Propagation

## Problem Statement

You are given a rooted tree. Each node `u` has a base cost `w_u` and a parameter `k_u`. The cost returned by a node is defined recursively:

- If `u` is a leaf, `cost(u) = w_u`.
- Otherwise, sort the costs of all children in descending order and set:

```
cost(u) = w_u + sum of the largest k_u child costs
```

Compute the cost of the root.

## Input Format

- First line: integer `n`
- Next `n` lines: `w_u k_u parent` (parent is 0 for root)

## Output Format

- Single integer: cost of the root

## Constraints

- `1 <= n <= 200000`
- `0 <= k_u <= degree(u)`
- `-10^9 <= w_u <= 10^9`

## Clarifying Notes

- If `k_u = 0`, then `cost(u) = w_u` regardless of children.

## Example Input

```
3
5 1 0
2 0 1
4 0 1
```

## Example Output

```
9
```
