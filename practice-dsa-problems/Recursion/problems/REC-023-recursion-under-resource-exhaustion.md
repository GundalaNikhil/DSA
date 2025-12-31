# REC-023: Recursion under Resource Exhaustion

## Problem Statement

You are given a rooted tree. Each node has a reward `val` and a frame cost `mem`. A recursive traversal follows a single root-to-leaf path. The total `mem` on the call stack may never exceed a global budget `B` at any point.

Find the maximum possible sum of `val` along any root-to-leaf path that never exceeds the memory budget while descending.

## Input Format

- First line: integers `n` and `B`
- Next `n` lines: `val mem parent` (parent is 0 for root)

## Output Format

- Single integer: maximum valid path sum, or `0` if no root-to-leaf path is valid

## Constraints

- `1 <= n <= 200000`
- `0 <= B <= 10^9`
- `-10^9 <= val <= 10^9`
- `0 <= mem <= 10^9`

## Clarifying Notes

- The memory budget is checked on every prefix of the path, not just at leaves.
- The traversal must start at the root and end at a leaf.

## Example Input

```
5 7
5 3 0
4 4 1
6 2 1
1 5 2
3 2 2
```

## Example Output

```
15
```
