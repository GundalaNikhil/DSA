# LNK-002: List with Soft Deletes

## Problem Statement

You maintain a singly linked list. Nodes can be **soft-deleted**: marked as deleted but kept in the list. Queries can either skip deleted nodes or include them.

Operations:

- `DEL u`: mark node `u` as deleted
- `RESTORE u`: unmark node `u`
- `KTH k mode`: output the value of the k-th node under the chosen mode
  - `mode = 0`: count only non-deleted nodes
  - `mode = 1`: count all nodes, including deleted

If the k-th node does not exist under the selected mode, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values in order
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `KTH` operation, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- Node ids are 1-based in initial order.
- Deleted nodes remain in position.

## Example Input

```
5
10 20 30 40 50
5
DEL 2
KTH 2 0
KTH 2 1
RESTORE 2
KTH 2 0
```

## Example Output

```
30
20
20
```
