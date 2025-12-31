# STR-041: Single-Edit Longest Common Subsequence

## Problem Statement

Given two strings `A` and `B`, you may change **at most one** character in `A` to any other character for free. After this optional edit, compute the length of the longest common subsequence of `A` and `B`.

Output the maximum possible LCS length.

## Input Format

- First line: string `A`
- Second line: string `B`

## Output Format

- Single integer: maximum LCS length

## Constraints

- `1 <= |A|, |B| <= 2000`
- Strings contain only lowercase English letters

## Clarifying Notes

- The free edit can be skipped.

## Example Input

```
abcdef
azcdef
```

## Example Output

```
6
```
