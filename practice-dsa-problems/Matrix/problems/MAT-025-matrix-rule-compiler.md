# MAT-025: Matrix Rule Compiler

## Problem Statement

You are given an initial matrix and a set of declarative rules. The compiler must apply rules in the following canonical order, regardless of the order in input:

1. All `ROW_MUL r x` (multiply row `r` by `x`)
2. All `COL_MUL c x` (multiply column `c` by `x`)
3. All `ROW_ADD r x` (add `x` to row `r`)
4. All `COL_ADD c x` (add `x` to column `c`)
5. All `SET r c v` (set a single cell; if multiple, the last one in input wins)

Compute the final matrix after compiling and applying the rules.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `q` lines: one rule per line

## Output Format

- `n` lines with `m` integers: the final matrix

## Constraints

- `1 <= n, m <= 200`
- `1 <= q <= 200000`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- All multiplications and additions are applied to every cell in the specified row or column.
- `SET` rules are applied last and override previous results.

## Example Input

```
2 2 3
1 2
3 4
ROW_MUL 1 2
COL_ADD 2 5
SET 2 1 0
```

## Example Output

```
2 9
0 9
```
