# REC-003: Recursive Layer Validation

## Problem Statement

You are given a rooted tree and a list of layer rules. At depth `d` (root at depth 0), the sum of node values at that depth must satisfy:

```
sum_d % K_d == 0
```

All depth rules must hold. Determine if the tree is valid.

## Input Format

- First line: integers `n` and `H`
- Next `n` lines: `value parent` (parent is 0 for root)
- Next line: `H+1` integers `K_0..K_H`

`H` is the maximum depth to validate; depths greater than `H` are ignored.

## Output Format

- `YES` if all rules pass, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `0 <= H <= 200000`
- `1 <= K_d <= 10^9`

## Clarifying Notes

- If a depth `d` has no nodes, its sum is 0.

## Example Input

```
4 1
3 0
2 1
1 1
4 2
3 5
```

## Example Output

```
YES
```
