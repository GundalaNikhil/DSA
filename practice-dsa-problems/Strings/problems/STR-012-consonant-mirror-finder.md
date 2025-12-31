# STR-012: Consonant Mirror Finder

## Problem Statement

Given a lowercase string `s`, find the longest substring whose consonant-only projection is a palindrome. The consonant-only projection is formed by removing all vowels (`a, e, i, o, u`) and keeping the remaining characters in order.

If multiple substrings share the maximum length, choose the one with the smallest starting index.

## Input Format

- Single line: string `s`

## Output Format

- The chosen substring (possibly the entire string)

## Constraints

- `1 <= |s| <= 200000`
- `s` contains only lowercase English letters

## Clarifying Notes

- Vowels are ignored only for palindrome checking, but they still count toward the substring length.
- A substring with zero or one consonant is always valid.

## Example Input

```
raceacar
```

## Example Output

```
raceacar
```
