# ARR-005: Zero Compression

## Problem Statement

Given an array `a1..an`, compress zeros and move them to the end:

1. A **zero block** is a maximal consecutive sequence of zeros in the original array.
2. Remove all zeros, keeping the relative order of non-zero elements.
3. Append exactly one zero for each zero block.

Output the resulting array.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- First line: integer `m`, the length of the resulting array
- Second line: `m` integers: the compressed array

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The output length can be smaller than `n` when zero blocks exist.
- Non-zero elements remain in their original order.

## Example Input

```
10
1 0 0 2 0 3 0 0 0 4
```

## Example Output

```
7
1 2 3 4 0 0 0
```
