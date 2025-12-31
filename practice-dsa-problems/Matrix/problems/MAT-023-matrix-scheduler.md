# MAT-023: Matrix Scheduler

## Problem Statement

Each cell is a task with a duration. You are given dependency edges between tasks. A task can start only after all its prerequisites finish. You have unlimited parallelism.

Compute the minimum total completion time (makespan).

## Input Format

- First line: integers `n`, `m`, `k`
- Next `n` lines: `m` integers (durations)
- Next `k` lines: `r1 c1 r2 c2` meaning task `(r2, c2)` depends on `(r1, c1)`

## Output Format

- Single integer: minimum completion time

## Constraints

- `1 <= n, m <= 200`
- `0 <= k <= 200000`
- `1 <= duration <= 10^9`

## Clarifying Notes

- If the dependency graph has a cycle, output `-1`.
- Indices are 1-based.

## Example Input

```
2 2 2
3 1
2 4
1 1 2 2
1 2 2 1
```

## Example Output

```
7
```
