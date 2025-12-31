# LNK-036: Multi-Tenant Linked List

## Problem Statement

A single linked list is shared by multiple tenants. Each node is owned by exactly one tenant. Each tenant has a maximum allowed node count.

Operations:

- `INS t pos x`: insert value `x` for tenant `t` at position `pos`
- `DEL t pos`: delete node at position `pos` if it belongs to tenant `t`
- `COUNT t`: output current node count of tenant `t`

Invalid operations are ignored.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers: initial list values
- Third line: `n` integers: tenant ids in order
- Next `T` lines: `limit_t` for each tenant
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `COUNT`, output one integer

## Constraints

- `1 <= n, q <= 200000`
- `1 <= T <= 200000`

## Clarifying Notes

- Insertions are rejected if they would exceed the tenant's limit.

## Example Input

```
3 2
1 2 3
1 2 1
2
2
3
INS 1 2 9
COUNT 1
```

## Example Output

```
2
```
