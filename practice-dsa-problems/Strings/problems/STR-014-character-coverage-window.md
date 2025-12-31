# STR-014: Character Coverage Window

## Problem Statement

Given a string `s`, a required string `r`, and an integer `F`, find the shortest substring of `s` that contains every distinct character in `r` at least `F` times. If no such substring exists, output `-1`.

If multiple substrings have the same minimum length, choose the one with the smallest starting index.

## Input Format

- First line: string `s`
- Second line: string `r`
- Third line: integer `F`

## Output Format

- The chosen substring, or `-1` if impossible

## Constraints

- `1 <= |s| <= 200000`
- `1 <= |r| <= 200000`
- `1 <= F <= 200000`
- Strings contain only uppercase English letters

## Clarifying Notes

- Only distinct characters from `r` are required.
- The substring must be contiguous.

## Example Input

```
ADOBECODEBANC
ABC
1
```

## Example Output

```
BANC
```
