# LNK-033: Linked List with Undo/Redo Stacks

## Problem Statement

Maintain a list with undo/redo support for insertions and deletions.

Operations:

- `INS pos x`
- `DEL pos`
- `UNDO`
- `REDO`
- `GET pos`

Undo reverts the last successful `INS` or `DEL`. Redo reapplies the last undone operation. Any new `INS` or `DEL` clears the redo stack.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- `UNDO` or `REDO` with empty stack is ignored.
- Positions are 1-based at the time of operation.

## Example Input

```
3
1 2 3
5
INS 2 9
GET 2
UNDO
GET 2
REDO
```

## Example Output

```
9
2
```
