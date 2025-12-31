# LNK-053: Linked List with Capability Tokens

## Problem Statement

Operations on the list require capability tokens. Each token grants access to a range of positions `[l, r]` and expires at time `t_expire`.

Operations:

- `INS token pos x t`
- `DEL token pos t`
- `GET pos t`

An operation is valid only if `t <= t_expire` and `pos` lies in the token's range. Invalid operations are ignored.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: integer `k` (tokens)
- Next `k` lines: `token_id l r t_expire`
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output value or `-1`

## Constraints

- `1 <= n, q <= 200000`
- Token ids are unique
- Timestamps are non-decreasing

## Clarifying Notes

- `GET` does not require a token.

## Example Input

```
3
1 2 3
1
5 1 2 10
3
INS 5 2 9 1
GET 2 1
DEL 5 3 2
```

## Example Output

```
9
```
