# STR-026: Maximum Unique Partitioning

## Problem Statement

Given a string `s`, split it into the maximum number of contiguous substrings such that all substrings are distinct. You must output one optimal partition.

## Input Format

- Single line: string `s`

## Output Format

- First line: integer `k`, the maximum number of substrings
- Second line: the `k` substrings separated by spaces

## Constraints

- `1 <= |s| <= 30`
- `s` contains only lowercase English letters

## Clarifying Notes

- If multiple optimal partitions exist, output any one.

## Example Input

```
ababccc
```

## Example Output

```
5
a b ab c cc
```
