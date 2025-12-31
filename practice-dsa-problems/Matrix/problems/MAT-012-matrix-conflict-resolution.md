# MAT-012: Matrix Conflict Resolution

## Problem Statement

Multiple sources propose values for cells in a matrix. A global strategy determines how to resolve conflicts for each cell.

Strategies:

- `1` (priority): highest priority wins; tie by earliest timestamp; then smaller source id
- `2` (timestamp): earliest timestamp wins; tie by highest priority; then smaller source id
- `3` (majority): most frequent value wins; tie by highest priority, then earliest timestamp, then smaller source id

Compute the final matrix after resolving all proposals.

## Input Format

- First line: integers `n`, `m`, `p`, `S`
- Next `p` lines: `r c value priority time source_id`

## Output Format

- `n` lines with `m` integers: the resolved matrix (cells with no proposals are 0)

## Constraints

- `1 <= n, m <= 500`
- `0 <= p <= 200000`
- `1 <= S <= 3`
- `-10^9 <= value <= 10^9`
- `0 <= priority, time, source_id <= 10^9`

## Clarifying Notes

- All indices are 1-based.
- Proposals for different cells are independent.

## Example Input

```
2 2 3 1
1 1 5 2 10 7
1 1 8 1 5 3
2 2 4 9 1 2
```

## Example Output

```
5 0
0 4
```
