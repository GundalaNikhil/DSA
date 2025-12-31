# LNK-021: Transactional Linked List

## Problem Statement

Maintain a linked list with transactional support. Operations inside an active transaction are staged until commit.

Operations:

- `BEGIN`: start a new transaction (can be nested)
- `COMMIT`: commit the most recent transaction
- `ROLLBACK`: discard the most recent transaction
- `INS pos x`: insert value `x` at position `pos`
- `DEL pos`: delete node at position `pos`
- `GET pos`: output value at position `pos` in the current visible state

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total nodes across all committed states <= 400000

## Clarifying Notes

- `COMMIT` with no active transaction is ignored.
- `ROLLBACK` with no active transaction is ignored.
- Nested transactions commit into their parent, not directly into the base list.

## Example Input

```
3
1 2 3
6
BEGIN
INS 2 9
GET 2
ROLLBACK
GET 2
COMMIT
```

## Example Output

```
9
2
```
