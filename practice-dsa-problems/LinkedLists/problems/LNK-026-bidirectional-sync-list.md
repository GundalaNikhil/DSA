# LNK-026: Bidirectional Sync List

## Problem Statement

Two linked lists `A` and `B` must remain synchronized. A fixed offset `D` defines the transformation between values:

```
value_in_B = value_in_A + D
```

Operations on one list must be mirrored on the other at the same position using this rule.

Operations:

- `INS A pos x`
- `INS B pos y`
- `DEL A pos`
- `DEL B pos`
- `GET A pos` / `GET B pos`

For `INS B pos y`, the inserted value in `A` is `y - D`.

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers: initial list `A`
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output the value at the position in the requested list, or `-1` if out of range

## Constraints

- `1 <= n, q <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- All operations are valid if the position exists in the target list at the time of operation.
- The two lists always have the same length.

## Example Input

```
3 5
1 2 3
4
GET B 2
INS A 2 10
GET B 2
DEL B 3
```

## Example Output

```
7
15
```
