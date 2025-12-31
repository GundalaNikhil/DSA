# REC-007: Recursion with One-Time Override

## Problem Statement

You are given a rooted tree. A node is valid if its value lies within `[L, R]`. The tree is valid if every node is valid.

You are allowed to override validity **once**: you may treat one invalid node as valid. Determine if the tree can be valid under this rule.

## Input Format

- First line: integers `n`, `L`, `R`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- `YES` if the tree can be valid with at most one override, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= value, L, R <= 10^9`

## Clarifying Notes

- The override can be unused.

## Example Input

```
3 2 5
1 0
3 1
6 1
```

## Example Output

```
YES
```
