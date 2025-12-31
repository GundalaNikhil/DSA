# HEP-001: Kth Largest Element with Volatility Window

## Problem Statement

You are given a stream of `n` integers `a1..an`. For every index `i` (1-based), define the active window as the longest suffix ending at `i` that satisfies both rules:

1. Its length is at most `W`.
2. For every consecutive pair inside the window, the volatility condition holds:
   `|a_j - a_{j-1}| <= T`.

Equivalently, let `last_bad` be the largest index `j` (1 < j <= i) such that `|a_j - a_{j-1}| > T`. Then the active window for `i` is:

```
L = max(1, i - W + 1, last_bad + 1)
window = [L, i]
```

For each `i`, output the `K`-th largest value within its active window. If the window size is less than `K`, output `-1` for that index.

## Input Format

- First line: integers `n`, `K`, `W`, `T`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n` integers separated by spaces: the answer for each index `i` from `1` to `n`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `1 <= W <= n`
- `0 <= T <= 10^9`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The active window is always a suffix ending at `i` and is contracted deterministically using `last_bad`.
- If `i = 1`, then `last_bad` is undefined and the window is `[1, 1]`.
- The `K`-th largest is defined by sorting the window values in descending order.

## Example Input

```
5 2 3 2
4 5 7 6 3
```

## Example Output

```
-1 4 5 6 -1
```
