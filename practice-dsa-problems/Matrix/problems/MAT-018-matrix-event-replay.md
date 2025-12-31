# MAT-018: Matrix Event Replay

## Problem Statement

You are given an initial matrix, a final matrix, and an event log. Replay the events and verify consistency.

Operations:

- `SET r c v`
- `ADD r c v`
- `SWAPROW r1 r2`
- `SWAPCOL c1 c2`

If any operation is out of bounds, it is invalid.

Output:

- The index of the first invalid operation, or
- `q + 1` if all operations are valid but the final matrix does not match, or
- `0` if the replay matches the final matrix.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `n` lines: `m` integers (target final matrix)
- Next `q` lines: operations

## Output Format

- Single integer as described

## Constraints

- `1 <= n, m <= 200`
- `1 <= q <= 200000`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Indices are 1-based.

## Example Input

```
2 2 2
1 2
3 4
1 2
4 3
SWAPROW 1 2
SWAPCOL 1 2
```

## Example Output

```
0
```
