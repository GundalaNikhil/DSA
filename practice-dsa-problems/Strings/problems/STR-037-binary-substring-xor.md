# STR-037: Binary Substring XOR

## Problem Statement

Given a binary string `s` and `q` queries, each query specifies a range `[l, r]` (1-based). For each query, consider **all** substrings fully contained in `s[l..r]`. Interpret each substring as a binary number with the leftmost bit as the most significant bit. Output the bitwise XOR of all these substring values.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: integers `l r`

## Output Format

- For each query, output the XOR value on its own line

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- `1 <= l <= r <= |s|`
- `r - l + 1 <= 30`
- `s` contains only `0` and `1`

## Clarifying Notes

- All substring values fit within 32-bit signed integers due to the length limit.

## Example Input

```
1011
1
2 4
```

## Example Output

```
6
```
