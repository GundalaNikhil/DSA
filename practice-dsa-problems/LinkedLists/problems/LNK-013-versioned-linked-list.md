# LNK-013: Versioned Linked List

## Problem Statement

Maintain versions of a linked list. Version `0` is the initial list. Each update creates a new version.

Operations:

- `INS v pos x`: create a new version by inserting value `x` at position `pos` in version `v`
- `DEL v pos`: create a new version by deleting position `pos` in version `v`
- `GET v pos`: output the value at position `pos` in version `v`

Versions are numbered in order of creation (1, 2, 3, ...).

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total nodes across all versions <= 400000

## Clarifying Notes

- Positions are 1-based; inserting at `pos = length+1` appends.
- If `pos` is invalid in `GET`, output `-1`.

## Example Input

```
3
1 2 3
4
INS 0 2 9
GET 1 2
DEL 1 3
GET 2 3
```

## Example Output

```
9
3
```
