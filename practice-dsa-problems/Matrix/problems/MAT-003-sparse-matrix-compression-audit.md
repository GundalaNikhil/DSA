# MAT-003: Sparse Matrix Compression Audit

## Problem Statement

You are given an original dense matrix `A` and a sequence of `k` compression steps. Each step provides:

1. A sparse list (COO format) claiming to represent all non-zero entries of `A`.
2. A decompressed dense matrix claiming to be the result of decompressing that sparse list.

A step is valid if:

- The sparse list matches **exactly** the non-zero entries of `A` (including positions and values).
- The decompressed matrix is identical to `A`.

Report the first invalid step and the stage where it fails. If all steps are valid, output `OK`.

## Input Format

- First line: integers `n`, `m`, `k`
- Next `n` lines: `m` integers (original matrix `A`)
- For each step `i` from 1 to `k`:
  - Line: integer `s` (number of sparse entries)
  - Next `s` lines: `r c val` (1-based indices)
  - Next `n` lines: `m` integers (decompressed matrix)

## Output Format

- `OK` if all steps are valid, otherwise
- `COMPRESS i` if step `i` has an invalid sparse list
- `DECOMPRESS i` if step `i` has a valid sparse list but invalid decompressed matrix

## Constraints

- `1 <= n, m <= 200`
- `0 <= k <= 50`
- `-10^9 <= A[r][c], val <= 10^9`

## Clarifying Notes

- A value is considered non-zero if it is not equal to 0.
- Sparse entries may appear in any order but must be unique.

## Example Input

```
2 2 1
1 0
0 2
2
1 1 1
2 2 2
1 0
0 2
```

## Example Output

```
OK
```
