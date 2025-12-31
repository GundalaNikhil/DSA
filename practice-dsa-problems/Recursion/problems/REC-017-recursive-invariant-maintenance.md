# REC-017: Recursive Invariant Maintenance

## Problem Statement

You are given a rooted tree. Each node has value `v_u`. Define `subsum(u)` as the sum of values in its subtree. The tree is valid if for every node:

```
subsum(u) >= v_u
```

Determine if the invariant holds for all nodes.

## Input Format

- First line: integer `n`
- Next `n` lines: `v_u parent` (parent is 0 for root)

## Output Format

- `YES` if valid, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= v_u <= 10^9`

## Clarifying Notes

- `subsum(u)` includes `v_u` itself.

## Example Input

```
3
2 0
-1 1
1 1
```

## Example Output

```
YES
```
