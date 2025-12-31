# LNK-019: Concurrent Modification Audit

## Problem Statement

You are given an initial list and a log of operations. Each operation includes the **expected** predecessor and successor ids. An operation is valid only if the current list matches the expected neighbors at the time of execution.

Operations:

- `INS u x prev next`: insert new node with value `x` between `prev` and `next` (u is new id)
- `DEL u prev next`: delete node `u` which is expected to be between `prev` and `next`

Report the index (1-based) of the first invalid operation, or `0` if all are valid.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers: node values in order
- Next `q` lines: operations

## Output Format

- Single integer: index of first invalid op, or `0`

## Constraints

- `1 <= n, q <= 200000`
- New ids `u` are unique and > n

## Clarifying Notes

- `prev` or `next` may be `0` to indicate list boundaries.
- Operations are applied in order until an invalid one occurs.

## Example Input

```
3 2
1 2 3
DEL 2 1 3
INS 4 9 1 3
```

## Example Output

```
0
```
