# STR-033: Weighted Bracket Optimization

## Problem Statement

You are given a string `s` consisting of lowercase letters and parentheses `(` and `)`. Each character has a deletion cost. Your task is to delete characters with minimum total cost so that the remaining string is a valid parentheses sequence containing only `(` and `)`.

Output the minimum total deletion cost.

## Input Format

- First line: string `s`
- Second line: 28 integers: deletion costs for `a` to `z`, then for `(`, then for `)`

## Output Format

- Single integer: minimum total deletion cost

## Constraints

- `1 <= |s| <= 200000`
- `0 <= cost <= 10^9`
- `s` contains only lowercase English letters and parentheses

## Clarifying Notes

- The empty string is considered a valid parentheses sequence.
- All remaining characters must be parentheses.

## Example Input

```
((a)b)c)
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2
```

## Example Output

```
3
```
