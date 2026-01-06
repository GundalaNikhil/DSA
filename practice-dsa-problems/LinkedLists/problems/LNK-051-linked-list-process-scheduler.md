---
problem_id: LNK_LINKED_LIST_PROCESS_SCHEDULER__3498
display_id: NTB-LNK-3498
slug: linked-list-process-scheduler
title: "Linked List as Process Scheduler"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-process-scheduler
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List as Process Scheduler

## Problem Statement

Each node is a process with `id`, `arrival`, and `burst`. Processes are stored in a linked list in order of arrival time. Simulate Round Robin scheduling with time quantum `Q`.

At time `t`, all processes with `arrival <= t` that are not finished are eligible. The ready queue preserves list order among eligible processes. Execute the head of the ready queue for `min(Q, remaining_burst)` time, then reappend it if unfinished.

Output each process's completion time.

## Input Format

- First line: integers `n` and `Q`
- Next `n` lines: `id arrival burst`

## Output Format

- `n` lines: `id completion_time` in order of input

## Constraints

- `1 <= n <= 200000`
- `1 <= Q <= 10^9`
- `0 <= arrival, burst <= 10^9`

## Clarifying Notes

- If the ready queue is empty, time jumps to the next arrival.

## Example Input

```
3 2
1 0 3
2 1 2
3 2 1
```

## Example Output

```
1 5
2 4
3 6
```
