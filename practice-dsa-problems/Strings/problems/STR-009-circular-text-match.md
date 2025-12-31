# STR-009: Circular Text Match

## Problem Statement

Given two strings `s1` and `s2`, determine if `s2` can be obtained by rotating `s1` left by some number of positions (possibly zero). Output `true` if yes, otherwise `false`.

## Input Format

- First line: string `s1`
- Second line: string `s2`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |s1|, |s2| <= 200000`
- Strings contain printable ASCII characters

## Clarifying Notes

- If lengths differ, the answer is `false`.

## Example Input

```
abcde
cdeab
```

## Example Output

```
true
```
