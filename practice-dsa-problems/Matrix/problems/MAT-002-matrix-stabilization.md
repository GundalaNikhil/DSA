# MAT-002: Matrix Stabilization

## Problem Statement

You are given a binary matrix (values 0 or 1). At each step, all cells update simultaneously using this rule:

- Let `d` be the number of 4-directional neighbors (up, down, left, right) whose value differs from the cell.
- If `d >= 2`, the cell changes to the **majority value among its neighbors**.
- If there is a tie among neighbor values, the cell becomes `0`.
- If `d < 2`, the cell remains unchanged.

Repeat until a previous state reappears. If the process reaches a fixed point, report it as stable. Otherwise, report the cycle length and the first state in the cycle.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` characters each (`0` or `1`)

## Output Format

- If stable: output `STABLE t` where `t` is the number of steps taken, then the matrix
- If cyclic: output `CYCLE p` where `p` is the cycle length, then the first matrix in the cycle

## Constraints

- `1 <= n, m <= 15`

## Clarifying Notes

- Step count `t` is 0 if the initial matrix is already stable.
- Neighbor counts use only in-bounds cells.

## Example Input

```
3 3
101
010
101
```

## Example Output

```
STABLE 2
000
000
000
```
