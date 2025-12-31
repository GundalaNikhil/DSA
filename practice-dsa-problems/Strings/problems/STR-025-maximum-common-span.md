# STR-025: Maximum Common Span

## Problem Statement

Given two strings `s1` and `s2`, find the longest common contiguous substring. If multiple substrings tie for maximum length, choose the one with the smallest starting index in `s1`. If still tied, choose the one with the smallest starting index in `s2`.

## Input Format

- First line: string `s1`
- Second line: string `s2`

## Output Format

- The chosen substring (possibly empty)

## Constraints

- `1 <= |s1|, |s2| <= 200000`
- Strings contain only lowercase English letters

## Clarifying Notes

- If there is no common substring, output an empty line.

## Example Input

```
abcdef
xbcdy
```

## Example Output

```
bcd
```
