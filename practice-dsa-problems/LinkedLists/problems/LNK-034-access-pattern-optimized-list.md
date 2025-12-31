# LNK-034: Access-Pattern Optimized List

## Problem Statement

Each `ACCESS pos` operation increases the access count of that node. A `REORDER` operation stably sorts the list by decreasing access count, preserving relative order among ties.

Process operations and output the final list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: list values
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- One line: final list values

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Access counts start at 0.
- `ACCESS` refers to current list positions.

## Example Input

```
4
10 20 30 40
5
ACCESS 2
ACCESS 2
ACCESS 4
REORDER
ACCESS 1
```

## Example Output

```
20 40 10 30
```
