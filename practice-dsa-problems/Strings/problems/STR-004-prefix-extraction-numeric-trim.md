# STR-004: Prefix Extraction (Numeric Trim)

## Problem Statement

Given `n` strings, first remove any trailing digits from each string. After trimming, find the longest common prefix among all trimmed strings. If there is no common prefix, output an empty line.

## Input Format

- First line: integer `n`
- Next `n` lines: one string per line

## Output Format

- A single line containing the longest common prefix (possibly empty)

## Constraints

- `1 <= n <= 200000`
- `1 <= |s_i| <= 200000`
- Total length of all strings <= 200000
- Strings contain printable ASCII characters

## Clarifying Notes

- Only trailing digits `0-9` are removed. Digits in the middle are not removed.
- If all strings become empty after trimming, output an empty line.

## Example Input

```
3
function123
function456
function789
```

## Example Output

```
function
```
