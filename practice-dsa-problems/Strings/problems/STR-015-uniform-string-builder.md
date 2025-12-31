# STR-015: Uniform String Builder

## Problem Statement

Given a string `s` and an integer `K`, find the length of the longest substring that can be converted into a string of identical characters by replacing at most `K` characters.

## Input Format

- First line: string `s`
- Second line: integer `K`

## Output Format

- Single integer: the maximum achievable length

## Constraints

- `1 <= |s| <= 200000`
- `0 <= K <= |s|`
- `s` contains only uppercase English letters

## Clarifying Notes

- Replacements can change a character into any other uppercase letter.

## Example Input

```
AABABBA
1
```

## Example Output

```
4
```
