# MAT-019: Matrix with Directional Gravity

## Problem Statement

You are given a binary matrix where `1` denotes a block and `0` denotes empty space. The matrix is split into four quadrants by its middle row and column:

- NW: rows `1..mid_r`, cols `1..mid_c`
- NE: rows `1..mid_r`, cols `mid_c+1..m`
- SW: rows `mid_r+1..n`, cols `1..mid_c`
- SE: rows `mid_r+1..n`, cols `mid_c+1..m`

Gravity directions:

- NW: down
- NE: left
- SW: right
- SE: up

Within each quadrant, blocks slide in the gravity direction until they are packed against the boundary. Blocks never leave their quadrant.

Output the final matrix.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` characters (`0` or `1`)

## Output Format

- `n` lines with `m` characters (`0` or `1`)

## Constraints

- `1 <= n, m <= 200`

## Clarifying Notes

- `mid_r = n / 2`, `mid_c = m / 2` (integer division).
- Packing preserves the number of blocks in each quadrant.

## Example Input

```
3 4
1001
0100
0010
```

## Example Output

```
0011
0100
1000
```
