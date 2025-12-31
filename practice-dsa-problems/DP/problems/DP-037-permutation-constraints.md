# DP-037: DP on Permutation with Constraints

## Problem Statement

You must build a permutation of `1..n` under forbidden adjacency constraints. You are given a matrix `forbid[i][j]` where `1` means `i` cannot be immediately followed by `j`.

Find the maximum total score, where score is the sum of weights `w[i][position]` for placing value `i` at that position.

## Input Format

- First line: integer `n`
- Next `n` lines: `n` integers: weights `w[i][1..n]`
- Next `n` lines: `n` integers: forbid matrix

## Output Format

- Single integer: maximum score, or `-1` if impossible

## Constraints

- `1 <= n <= 15`
- `-10^9 <= w[i][pos] <= 10^9`

## Clarifying Notes

- This is a bitmask DP over permutations.

## Example Input

```
3
3 2 1
2 3 1
1 2 3
0 1 0
0 0 1
0 0 0
```

## Example Output

```
8
```
