# REC-044: Recursive Memoization with Eviction

## Problem Statement

You are given a recursive function:

- `F(0) = A0`
- `F(1) = A1`
- `F(x) = F(x-1) + F(x-2) + C[x]` for `x >= 2`

You will answer a sequence of queries `Q`. For each query `x`, compute `F(x)` using memoization with an LRU cache of size `M`.

Count how many times `F(x)` is computed on a cache miss (including base cases). Output the total number of cache misses across all queries, and then the query answers modulo `1,000,000,007`.

## Input Format

- First line: integers `Q`, `M`
- Second line: integers `A0` and `A1`
- Third line: integer `N` (maximum index for `C`)
- Fourth line: `N+1` integers `C[0..N]` (values for `C[0]` and `C[1]` are ignored)
- Fifth line: `Q` integers `x1..xQ`

## Output Format

- First line: total cache misses
- Second line: `Q` integers, the results for each query modulo `1,000,000,007`

## Constraints

- `1 <= Q <= 200000`
- `1 <= M <= 200000`
- `0 <= N <= 200000`
- `0 <= x <= N`
- `0 <= A0, A1, C[i] <= 10^9`

## Clarifying Notes

- The cache stores computed values `F(x)`; LRU order updates on every access.
- A cache miss occurs when a needed `F(x)` is not stored and must be computed.

## Example Input

```
3 2
1 2
5
0 0 3 1 4 2
3 4 3
```

## Example Output

```
5
8 13 8
```
