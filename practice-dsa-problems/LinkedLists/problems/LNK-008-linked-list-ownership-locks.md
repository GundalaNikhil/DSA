# LNK-008: Linked List with Ownership Locks

## Problem Statement

Some nodes are locked and cannot be modified. Process operations and reject any that touch a locked node.

Operations:

- `INS u x`: insert value `x` immediately after node `u`
- `DEL u`: delete node `u`
- `REVERSE l r`: reverse the sublist from position `l` to `r`

An operation is invalid if it modifies or reorders any locked node.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values in order
- Third line: integer `k` (number of locked nodes)
- Fourth line: `k` integers: node indices that are locked
- Fifth line: integer `q`
- Next `q` lines: operations

## Output Format

- First line: number of invalid operations
- Second line: final list values

## Constraints

- `1 <= n, q <= 200000`
- `0 <= k <= n`

## Clarifying Notes

- Locked nodes remain locked after operations.
- For `REVERSE`, the entire range must be unlocked.

## Example Input

```
5
1 2 3 4 5
1
3
3
DEL 2
REVERSE 2 4
INS 5 9
```

## Example Output

```
1
1 2 3 4 5 9
```
