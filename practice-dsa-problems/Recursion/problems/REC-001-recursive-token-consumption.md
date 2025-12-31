# REC-001: Recursive Token Consumption

## Problem Statement

You are given a rooted tree. Entering a node consumes tokens of two types: `A` and `B`. After fully processing all of its children, the node grants a token refund. You may choose the order in which children are processed. A node can be visited only if the current token balances are sufficient for its entry costs.

Compute the maximum number of nodes that can be visited starting from the root.

## Input Format

- First line: integer `n`
- Second line: integers `A0` and `B0` (initial tokens)
- Next `n` lines: `costA costB gainA gainB`
- Next `n-1` lines: edges `u v` (tree edges, undirected)

Node `1` is the root.

## Output Format

- Single integer: maximum number of nodes that can be visited

## Constraints

- `1 <= n <= 200000`
- `0 <= A0, B0 <= 10^6`
- `0 <= costA, costB, gainA, gainB <= 10^6`

## Clarifying Notes

- You must pay `costA/costB` before entering a node.
- You receive `gainA/gainB` only after all children of that node have been processed.
- Visiting a node counts even if it has no children.

## Example Input

```
3
2 1
1 0 1 0
1 1 0 1
2 0 0 0
1 2
1 3
```

## Example Output

```
3
```
