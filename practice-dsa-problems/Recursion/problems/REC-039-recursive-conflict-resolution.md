# REC-039: Recursive Conflict Resolution

## Problem Statement

You are given a rooted tree. Each node proposes a value and has a priority. A node resolves conflicts by selecting the proposal with the highest priority from itself and all of its descendants.

Define `Resolve(node)` as returning the pair `(priority, value)` with the highest priority among:

- the node's own proposal `(p[node], v[node])`
- all results returned by its children

If priorities tie, choose the proposal with the smaller node index.

Compute the resolved value at the root.

## Input Format

- First line: integer `n`
- Next `n` lines: `v p parent` (parent is 0 for root)

## Output Format

- Single integer: resolved value at the root

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= v <= 10^9`
- `0 <= p <= 10^9`

## Clarifying Notes

- Ties are broken by node index only, regardless of depth.
- The resolution is deterministic for each subtree.

## Example Input

```
4
5 2 0
7 1 1
3 3 1
9 3 2
```

## Example Output

```
3
```
