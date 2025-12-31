# LNK-024: Linked List Scheduler

## Problem Statement

Each node represents a task with a start time and duration. A task is active at time `t` if `start <= t < start + duration`.

Process queries to count active tasks in a sublist.

## Input Format

- First line: integer `n`
- Next `n` lines: `value start duration` for each node in list order
- Next line: integer `q`
- Next `q` lines: `l r t` queries (1-based positions)

## Output Format

- For each query, output the count of active tasks in positions `[l, r]` at time `t`

## Constraints

- `1 <= n, q <= 200000`
- `0 <= start, duration, t <= 10^9`

## Clarifying Notes

- Duration can be 0, which means the task is never active.

## Example Input

```
3
10 0 5
20 3 2
30 4 10
2
1 3 4
2 3 6
```

## Example Output

```
3
1
```
