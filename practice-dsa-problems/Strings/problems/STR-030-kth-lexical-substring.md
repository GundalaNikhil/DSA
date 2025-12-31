# STR-030: Kth Lexical Substring

## Problem Statement

Given a string `s` and an integer `K`, list all **distinct** substrings of `s` in lexicographic order and return the `K`-th one (1-based). If `K` exceeds the number of distinct substrings, output `-1`.

## Input Format

- First line: string `s`
- Second line: integer `K`

## Output Format

- The `K`-th substring, or `-1`

## Constraints

- `1 <= |s| <= 200000`
- `1 <= K <= 10^18`
- `s` contains only lowercase English letters

## Clarifying Notes

- Lexicographic order follows standard dictionary order.

## Example Input

```
abc
4
```

## Example Output

```
b
```
