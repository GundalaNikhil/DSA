# DP-063: Database Query Optimizer DP

## Problem Statement

You must join `n` tables. For any subset of tables, the cost to join two subsets `A` and `B` is:

```
cost(A,B) = size(A) * size(B) + join_cost[A][B]
```

Sizes for single tables are given, and `join_cost` is provided for any pair of tables. Find the minimum total cost to join all tables.

## Input Format

- First line: integer `n`
- Second line: `n` integers: sizes of each table
- Next `n` lines: `n` integers: join cost matrix (0 on diagonal)

## Output Format

- Single integer: minimum join cost

## Constraints

- `1 <= n <= 12`
- `0 <= sizes, join_cost <= 10^6`

## Clarifying Notes

- Use subset DP over join orders.

## Example Input

```
3
2 3 4
0 1 2
1 0 3
2 3 0
```

## Example Output

```
27
```
