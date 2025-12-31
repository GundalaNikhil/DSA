# STR-023: Fixed-Length Frequency Ranking

## Problem Statement

Given a string `s`, an integer `L`, and an integer `K`, count the frequency of every substring of length `L`. Output the top `K` substrings by frequency (descending). Break ties by lexicographically smaller substring.

## Input Format

- First line: string `s`
- Second line: integers `L` and `K`

## Output Format

- One line per reported substring: `<substring> <count>`
- If there are fewer than `K` distinct substrings of length `L`, output all of them

## Constraints

- `1 <= |s| <= 200000`
- `1 <= L <= |s|`
- `1 <= K <= 200000`
- `s` contains only lowercase English letters

## Clarifying Notes

- Output order must follow the ranking rules.

## Example Input

```
ababcabc
2 2
```

## Example Output

```
ab 2
bc 2
```
