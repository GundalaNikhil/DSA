# STR-019: Mirror Subsequence Count

## Problem Statement

Given a string `s` and a modulus `M`, count the number of palindromic subsequences in `s`. Subsequence counting is based on index choices, so identical strings from different index sets are counted separately.

Output the count modulo `M`.

## Input Format

- First line: string `s`
- Second line: integer `M`

## Output Format

- Single integer: count modulo `M`

## Constraints

- `1 <= |s| <= 2000`
- `1 <= M <= 10^9 + 7`
- `s` contains only lowercase English letters

## Clarifying Notes

- The empty subsequence is not counted.
- A single character is a palindrome.

## Example Input

```
aba
1000000007
```

## Example Output

```
5
```
