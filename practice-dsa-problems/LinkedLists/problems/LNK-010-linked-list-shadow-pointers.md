# LNK-010: Linked List with Shadow Pointers

## Problem Statement

Each node stores a **shadow pointer** to the node that was immediately before it **at the time it was inserted**. Shadow pointers never change, even if nodes are moved or deleted.

Process operations:

- `INS u x`: insert value `x` after node `u` (new node's shadow = `u`)
- `DEL u`: delete node `u`
- `SHADOW u`: output the id of node `u`'s shadow, or `-1` if none

Node ids are assigned incrementally starting from 1 for the initial list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `SHADOW`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Total nodes created <= 300000

## Clarifying Notes

- If a shadow node is deleted, its id is still returned.
- The first node's shadow is `-1`.

## Example Input

```
2
5 6
4
INS 1 9
SHADOW 3
DEL 1
SHADOW 3
```

## Example Output

```
1
1
```
