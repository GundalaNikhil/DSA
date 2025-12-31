# DP-036: DP with Conflict Resolution

## Problem Statement

You have a DAG with a unique start node `S` and end node `T`. Each edge has a reward. When multiple paths merge at a node, their requirements (bitmasks) are combined by AND. A path is valid if its final requirement mask equals `target_mask`.

Find the maximum reward among valid paths from `S` to `T`.

## Input Format

- First line: integers `n`, `m`, `b`
- Second line: integers `S`, `T`, `target_mask` (0..(1<<b)-1)
- Next `m` lines: `u v reward mask` (mask is the requirement bitmask for the edge)

## Output Format

- Single integer: maximum reward, or `-1` if no valid path

## Constraints

- `1 <= n <= 200`
- `1 <= m <= 5000`
- `1 <= b <= 10`

## Clarifying Notes

- Requirements along a path are combined by bitwise AND.

## Example Input

```
3 2 2
1 3 1
1 2 5 3
2 3 4 1
```

## Example Output

```
9
```
