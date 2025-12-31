# ARR-038: Subarray Cost = sum x gcd

## Problem Statement

Given an array `a1..an`, define the cost of a subarray as:

```
cost = (sum of elements in the subarray) * (gcd of elements in the subarray)
```

Find the maximum cost over all subarrays.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum subarray cost

## Constraints

- `1 <= n <= 200000`
- `1 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- GCD is computed over the absolute values of elements.

## Example Input

```
3
2 4 6
```

## Example Output

```
36
```
