# LNK-017: Linked List with Cyclic Regions

## Problem Statement

You are given a list defined by `next` pointers from a head node. The list may contain one or more cycles. Normalize the list by breaking every cycle at the node with the smallest id in that cycle (set its `next` to 0).

Output the number of links removed and the resulting list from the head.

## Input Format

- First line: integers `n` and `head`
- Next `n` lines: `value next_id` for node `1..n` (`0` means null)

## Output Format

- First line: integer `removed` (number of links set to 0)
- Second line: list values from head to null after normalization

## Constraints

- `1 <= n <= 200000`
- `1 <= head <= n`

## Clarifying Notes

- If the head is inside a cycle, the cycle is still broken by smallest id.
- Output traversal stops at null.

## Example Input

```
3 1
5 2
6 3
7 2
```

## Example Output

```
1
5 6 7
```
