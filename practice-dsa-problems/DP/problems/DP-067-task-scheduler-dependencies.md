# DP-067: Task Scheduler with Dependencies DP

## Problem Statement

You have `n` tasks with durations `t_i` and dependencies forming a DAG. You have one processor and can execute one task at a time once all its dependencies are completed.

Minimize total completion time.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: durations
- Next `m` lines: `u v` meaning task `u` must finish before task `v`

## Output Format

- Single integer: minimum completion time

## Constraints

- `1 <= n <= 20`
- `0 <= m <= 200`
- `1 <= t_i <= 10^9`

## Clarifying Notes

- This is a DP over subsets of completed tasks.

## Example Input

```
3 2
3 2 4
1 3
2 3
```

## Example Output

```
9
```
