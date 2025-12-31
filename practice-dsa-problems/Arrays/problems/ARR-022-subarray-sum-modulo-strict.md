# ARR-022: Subarray Sum Modulo M (Strict)

## Problem Statement

Given an array `a1..an`, an integer `M`, and a minimum length `L`, count how many subarrays have:

- length >= `L`, and
- sum % `M` == 0

## Input Format

- First line: integers `n`, `M`, and `L`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: number of qualifying subarrays

## Constraints

- `1 <= n <= 200000`
- `1 <= M <= 200000`
- `1 <= L <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- Modulo for negative sums should be normalized into `[0, M-1]`.

## Example Input

```
5 3 2
1 2 3 4 1
```

## Example Output

```
3
```
