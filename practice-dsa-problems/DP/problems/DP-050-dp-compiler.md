# DP-050: DP Compiler Problem

## Problem Statement

You are given `n` DP variables `dp[1..n]` and `m` rules. Each rule defines how to compute a variable from previously computed ones:

```
TYPE i k j1 w1 j2 w2 ... jk wk
```

- `TYPE` is `MIN` or `MAX`.
- The rule sets `dp[i] = min/max(dp[jx] + wx)` over its `k` terms.

You are guaranteed the dependency graph is acyclic and that all `j` indices are less than `i`.

Compute all `dp[i]` and output `dp[n]`.

## Input Format

- First line: integer `n`
- Second line: integer `m`
- Next `m` lines: rules as described
- Last line: integer `dp[1]` (base value)

## Output Format

- Single integer: value of `dp[n]`

## Constraints

- `1 <= n <= 200000`
- `1 <= m <= 200000`
- `1 <= k <= 5`
- `-10^9 <= weights <= 10^9`

## Clarifying Notes

- Any `dp[i]` without a rule is treated as `+infinity` for MIN and `-infinity` for MAX.

## Example Input

```
3
2
MIN 2 1 1 5
MAX 3 1 2 2
0
```

## Example Output

```
7
```
