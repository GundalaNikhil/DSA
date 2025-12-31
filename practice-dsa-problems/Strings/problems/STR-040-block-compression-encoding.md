# STR-040: Block Compression Encoding

## Problem Statement

Given a string `s`, you may encode repeated blocks using the format `k(x)` where `x` is a non-empty string and `k >= 2` is the number of repetitions of `x`. The encoded length counts digits of `k` plus 2 parentheses plus the length of `x` (after encoding it recursively).

Find a shortest encoded string for `s`. If multiple shortest encodings exist, output the lexicographically smallest.

## Input Format

- Single line: string `s`

## Output Format

- The chosen encoded string

## Constraints

- `1 <= |s| <= 2000`
- `s` contains only lowercase English letters

## Clarifying Notes

- You may choose to leave parts unencoded if that is shorter.
- Recursive encoding is allowed.

## Example Input

```
ababababcdcd
```

## Example Output

```
4(ab)2(cd)
```
