# ARR-027: Dynamic Median Cost Array

## Problem Statement

Given an array `a1..an` and a window size `W`, compute the cost of every window as:

```
cost = sum(|a_i - median|) over the window
```

The median is the lower middle element when the window is sorted (for even `W`). Output the cost for each window from left to right.

## Input Format

- First line: integers `n` and `W`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n - W + 1` integers separated by spaces: the cost for each window

## Constraints

- `1 <= n <= 200000`
- `1 <= W <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- For even `W`, use the lower of the two middle values as the median.
- Costs fit in 64-bit signed integers.

## Example Input

```
5 3
1 3 2 6 4
```

## Example Output

```
2 4 4
```
