# DP-061: Cache Replacement Policy DP

## Problem Statement

You are given an access sequence of `n` keys and a cache of capacity `C`. On each access, you may choose which key to evict if the cache is full. A miss costs 1, a hit costs 0. Compute the minimum possible total misses.

## Input Format

- First line: integers `n` and `C`
- Second line: `n` integers: access sequence

## Output Format

- Single integer: minimum possible misses

## Constraints

- `1 <= n <= 200`
- `1 <= C <= 6`
- Keys are 32-bit signed integers

## Clarifying Notes

- Cache state is a set; order does not matter.
- This is an optimal offline policy DP.

## Example Input

```
5 2
1 2 3 2 1
```

## Example Output

```
4
```
