# LNK-065: ZooKeeper Watch Mechanism

## Problem Statement

Nodes can be watched. A watch triggers when the node is modified, and then is removed.

Operations:

- `WATCH id pos`: register watch `id` on position `pos`
- `SET pos x`: set value at `pos`
- `GET pos`: output value or `-1`

For each `SET`, output the watch ids triggered in increasing order, or `0` if none.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `SET`, output triggered watch ids or `0`
- For each `GET`, output the value

## Constraints

- `1 <= n, q <= 200000`
- Watch ids are unique

## Clarifying Notes

- Watches are one-time triggers.

## Example Input

```
2
1 2
4
WATCH 5 2
SET 2 9
GET 2
SET 1 3
```

## Example Output

```
5
9
0
```
