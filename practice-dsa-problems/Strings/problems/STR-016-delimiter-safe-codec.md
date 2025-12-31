# STR-016: Delimiter-Safe Codec

## Problem Statement

You must implement a codec that safely encodes and decodes lists of strings using the delimiter `|` and escape character `\`.

Encoding rules:

1. In each string, replace `\` with `\\`.
2. Then replace `|` with `\|`.
3. Join encoded strings with `|`.

Decoding reverses the process by splitting on unescaped `|` and then unescaping `\|` and `\\`.

You are given `q` operations of two types:

- `ENCODE k` followed by `k` strings: output the encoded string.
- `DECODE encoded_string`: output the decoded list as `k` followed by the `k` strings separated by spaces.

## Input Format

- First line: integer `q`
- Next lines: operations as described

## Output Format

- For each operation, output one line with the result

## Constraints

- `1 <= q <= 200000`
- Each string is non-empty and contains printable ASCII characters except spaces
- Total input length <= 200000

## Clarifying Notes

- The encoding is deterministic and reversible.
- Strings do not contain spaces to keep output parsing unambiguous.

## Example Input

```
3
ENCODE 2
hello|world
x\y
DECODE hello\|world|x\\y
ENCODE 1
plain
```

## Example Output

```
hello\|world|x\\y
2 hello|world x\y
plain
```
