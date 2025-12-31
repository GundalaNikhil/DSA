# REC-004: Recursive Frequency Limits

## Problem Statement

You are given a rooted tree. Each node has a label `L`. A recursive traversal counts how many times each label is visited. If a label is visited more than `K` times, traversal stops at that node and its children are not visited.

Compute the total number of visited nodes.

## Input Format

- First line: integers `n` and `K`
- Next `n` lines: `label parent` (parent is 0 for root)

## Output Format

- Single integer: total number of visited nodes

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= 200000`
- `0 <= label <= 200000`

## Clarifying Notes

- Traversal is pre-order from the root.
- Once the label count exceeds `K`, that node is not counted and its subtree is skipped.

## Example Input

```
5 2
1 0
1 1
2 1
1 2
2 2
```

## Example Output

```
4
```
