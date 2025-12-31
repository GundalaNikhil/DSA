# STR-021: Compression with Undo

## Problem Statement

You are given an initial string `s` and must process `q` operations. The current string changes over time.

Compression rule: replace each maximal run of identical characters with `<char><count>` where `count` is written in decimal without leading zeros. For example, `aaabb` becomes `a3b2`.

Operations:

- `C`: compress the current string using the rule above.
- `U k`: undo the last `k` compression operations (in reverse order). It is guaranteed that there are at least `k` previous compressions to undo.

After each operation, output the current string.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: operations `C` or `U k`

## Output Format

- After each operation, output the current string on its own line

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- Total length of all output strings <= 200000
- `s` contains only lowercase English letters

## Clarifying Notes

- Undo only affects compression operations, not previous undos.

## Example Input

```
aaa
3
C
C
U 1
```

## Example Output

```
a3
a13
a3
```
