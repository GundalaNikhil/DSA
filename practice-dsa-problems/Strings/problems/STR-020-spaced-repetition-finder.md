# STR-020: Spaced Repetition Finder

## Problem Statement

Given a string `s` and an integer `D`, find the longest substring that appears at least twice with starting indices differing by at least `D`.

If multiple answers have the same maximum length, choose the one with the smallest starting index of its first occurrence.

## Input Format

- First line: string `s`
- Second line: integer `D`

## Output Format

- The chosen substring, or an empty line if no repeated substring exists

## Constraints

- `1 <= |s| <= 200000`
- `0 <= D <= |s|`
- `s` contains only lowercase English letters

## Clarifying Notes

- The two occurrences may overlap if the index distance condition is satisfied.

## Example Input

```
abcabc
3
```

## Example Output

```
abc
```
