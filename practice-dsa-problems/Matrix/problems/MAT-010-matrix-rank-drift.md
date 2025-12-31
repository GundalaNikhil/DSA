# MAT-010: Matrix Rank Drift

## Problem Statement

You are given an `n x m` integer matrix. Process `q` operations and report the matrix rank after each operation. Rank is defined over the real numbers.

Operations:

- `SWAP r1 r2`: swap two rows
- `SET r v1 v2 ... vm`: replace row `r` with given values
- `ADD r1 r2`: set row `r1 = row r1 + row r2`

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `q` lines: one operation per line

## Output Format

- After each operation, output the current rank on its own line

## Constraints

- `1 <= n, m <= 50`
- `1 <= q <= 500`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Row indices are 1-based.
- Row swaps do not change rank, but other operations can.

## Example Input

```
2 2 2
1 2
2 4
ADD 1 2
SET 2 0 1
```

## Example Output

```
1
2
```
