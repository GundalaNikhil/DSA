# ARR-030: Array Transformation with Limited Swaps

## Problem Statement

You are given two arrays `A` and `B` of length `n` and an integer `K`. In one operation, you may swap two **adjacent** elements in `A`. Determine whether you can transform `A` into `B` using at most `K` adjacent swaps.

If the transformation is possible within `K` swaps, output `YES`. Otherwise, output `NO`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `A1 A2 ... An`
- Third line: `n` integers `B1 B2 ... Bn`

## Output Format

- `YES` or `NO`

## Constraints

- `1 <= n <= 200000`
- `0 <= K <= 10^12`
- `-10^9 <= A_i, B_i <= 10^9`

## Clarifying Notes

- If `A` and `B` do not have the same multiset of values, the answer is `NO`.
- Adjacent swap count is the minimum number required to match the ordering.

## Example Input

```
4 1
1 2 1 3
1 1 2 3
```

## Example Output

```
YES
```
