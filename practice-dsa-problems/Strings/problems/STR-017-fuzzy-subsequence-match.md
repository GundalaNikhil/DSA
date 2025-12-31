# STR-017: Fuzzy Subsequence Match

## Problem Statement

Given a text string `t`, a pattern string `p`, and an integer `X`, determine whether `p` can be matched as a subsequence of `t` with at most `X` mismatches.

A mismatch occurs when a chosen character from `t` does not equal the corresponding character in `p`.

## Input Format

- First line: string `t`
- Second line: string `p`
- Third line: integer `X`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |t| <= 200000`
- `1 <= |p| <= 200000`
- `0 <= X <= |p|`
- Strings contain only lowercase English letters

## Clarifying Notes

- The indices chosen in `t` must be strictly increasing.
- If `|p| > |t|`, the answer is `false`.

## Example Input

```
abcdefg
ace
1
```

## Example Output

```
true
```
