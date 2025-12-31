# STR-039: Overlap Graph Assembly

## Problem Statement

You are given `n` strings (`n <= 15`). Build the shortest superstring that contains every given string as a substring. If multiple shortest superstrings exist, output the lexicographically smallest one.

## Input Format

- First line: integer `n`
- Next `n` lines: one string per line

## Output Format

- Single line: the shortest superstring

## Constraints

- `1 <= n <= 15`
- `1 <= |s_i| <= 200`
- Total length of all strings <= 2000
- Strings contain only lowercase English letters

## Clarifying Notes

- If a string is a substring of another, it still must be considered present but does not need extra length.

## Example Input

```
5
catg
ctaagt
gcta
ttca
atgcatc
```

## Example Output

```
ctaagttcatgcatc
```
