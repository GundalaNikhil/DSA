# LNK-029: Linked List with Affinity Groups

## Problem Statement

Each node belongs to an affinity group. Operations can only be applied within a single group.

Operations:

- `SWAP u v`: swap two nodes if they are in the same group
- `MOVE u v`: move node `u` after node `v` if same group
- `COUNT g`: output the number of nodes in group `g`

Invalid operations are ignored.

## Input Format

- First line: integer `n`
- Second line: `n` integers: values
- Third line: `n` integers: group ids
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- Group ids are integers in `1..n`

## Clarifying Notes

- `SWAP` and `MOVE` require both nodes in the same group.

## Example Input

```
4
1 2 3 4
1 2 1 2
3
MOVE 3 1
COUNT 1
SWAP 2 4
```

## Example Output

```
2
```
