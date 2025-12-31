# STR-018: Lexical Minimizer with Swaps

## Problem Statement

Given a string `s` and an integer `K`, you may perform at most `K` adjacent swaps. Return the lexicographically smallest string that can be obtained.

## Input Format

- First line: string `s`
- Second line: integer `K`

## Output Format

- The lexicographically smallest achievable string

## Constraints

- `1 <= |s| <= 200000`
- `0 <= K <= 10^12`
- `s` contains only lowercase English letters

## Clarifying Notes

- Adjacent swaps are swaps of positions `i` and `i+1`.

## Example Input

```
dcba
2
```

## Example Output

```
bdca
```
