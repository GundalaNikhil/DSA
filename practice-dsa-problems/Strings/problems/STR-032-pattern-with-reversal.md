# STR-032: Pattern with Reversal

## Problem Statement

Given a text `T` and a pattern `P`, determine if there exists an index range in `T` that matches `P` after reversing at most one contiguous segment of `P`.

Formally, choose indices `l` and `r` with `1 <= l <= r <= |P|`, reverse `P[l..r]`, and check if the resulting string appears as a substring in `T`. You may also choose an empty reversal (no change).

Output `true` if such a match exists, otherwise `false`.

## Input Format

- First line: string `T`
- Second line: string `P`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |T|, |P| <= 200000`
- Strings contain only lowercase English letters

## Clarifying Notes

- Reversal is applied to the pattern once at most.

## Example Input

```
abcdefghi
fed
```

## Example Output

```
true
```
