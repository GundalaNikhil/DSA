# STR-003: Text Normalization Check

## Problem Statement

Given a string `s`, determine if it reads the same forwards and backwards after normalization. Normalization rules:

- Ignore all characters that are not letters or digits.
- Compare letters case-insensitively.

Output `true` if the normalized string is a palindrome, otherwise `false`.

## Input Format

- Single line: string `s`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |s| <= 200000`
- `s` contains printable ASCII characters

## Clarifying Notes

- Digits are compared as-is.
- An empty normalized string is considered a palindrome.

## Example Input

```
A man, a plan, a canal: Panama
```

## Example Output

```
true
```
