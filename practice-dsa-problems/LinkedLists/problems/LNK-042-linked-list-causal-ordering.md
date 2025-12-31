# LNK-042: Linked List with Causal Ordering

## Problem Statement

You are given a log of operations with dependency ids. Each operation `i` may list prerequisite operation ids that must appear earlier in the log. Determine the first operation that violates causal ordering.

## Input Format

- First line: integer `q`
- Next `q` lines: `k dep1 dep2 ... depk` (the dependency list for operation i)

## Output Format

- The 1-based index of the first violation, or `0` if none

## Constraints

- `1 <= q <= 200000`
- Total number of dependencies <= 200000

## Clarifying Notes

- Dependencies refer to operation indices.

## Example Input

```
3
0
1 1
1 3
```

## Example Output

```
3
```
