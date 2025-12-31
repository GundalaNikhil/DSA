# LNK-045: Linked List with Merkle Verification

## Problem Statement

The list is divided into segments of equal size `K` (last segment may be smaller). For each segment, you are given a claimed hash value. The hash is defined as:

```
hash = (sum of values in segment) mod 1,000,000,007
```

Verify each segment and report the first invalid segment index, or `0` if all are valid.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers: list values
- Third line: `ceil(n / K)` integers: claimed hashes

## Output Format

- Single integer: index of first invalid segment (1-based), or `0`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- Values are 32-bit signed integers

## Clarifying Notes

- Use modulo `1,000,000,007` with non-negative result.

## Example Input

```
5 2
1 2 3 4 5
3 7 5
```

## Example Output

```
0
```
