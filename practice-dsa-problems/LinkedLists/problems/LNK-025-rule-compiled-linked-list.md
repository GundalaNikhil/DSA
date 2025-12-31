# LNK-025: Rule-Compiled Linked List

## Problem Statement

You are given a linked list and a set of high-level rules. Rules are applied in the following fixed order:

1. All `FILTER_LT x`: delete nodes with value < `x`
2. All `FILTER_EQ x`: delete nodes with value = `x`
3. All `INSERT_AFTER v x`: for each node with value `v`, insert a new node with value `x` immediately after it

If multiple rules of the same type exist, apply them in input order.

Compute the final list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: list values
- Third line: integer `q`
- Next `q` lines: rules

## Output Format

- One line: final list values (empty line if list is empty)

## Constraints

- `1 <= n, q <= 200000`
- Total nodes after insertions <= 300000

## Clarifying Notes

- `INSERT_AFTER` applies to the list state after all filters have completed.

## Example Input

```
4
1 2 3 2
3
FILTER_LT 2
FILTER_EQ 3
INSERT_AFTER 2 9
```

## Example Output

```
2 9 2 9
```
