# STR-028: Block Edit Distance

## Problem Statement

Given two strings `A` and `B` and an integer `L`, transform `A` into `B` with minimum operations. Allowed operations (each costs 1):

- Insert a single character.
- Delete a single character.
- Replace a contiguous substring of length `len` (1 <= len <= L) in `A` with any other string of the same length.

Find the minimum number of operations required.

## Input Format

- First line: string `A`
- Second line: string `B`
- Third line: integer `L`

## Output Format

- Single integer: minimum operations

## Constraints

- `1 <= |A|, |B| <= 2000`
- `1 <= L <= 50`
- Strings contain only lowercase English letters

## Clarifying Notes

- The replacement operation can change all characters in the chosen block at once.

## Example Input

```
abcdef
azef
3
```

## Example Output

```
1
```
