---
problem_id: CON_WORK_STEAL_POOL__B315
display_id: CON-008
slug: threadpool-work-stealing
title: "Thread Pool with Work Stealing"
difficulty: Medium
difficulty_score: 56
topics:
  - Concurrency
  - Thread Pools
  - Deques
  - Work Stealing
tags:
  - concurrency
  - threadpool
  - work-stealing
  - deque
  - medium
premium: true
subscription_tier: basic
time_limit: 3000
memory_limit: 256
---

# Thread Pool with Work Stealing

## Problem Statement

Design a thread pool that uses **work stealing**:

- There are `W` worker threads.
- Each worker owns a deque of tasks.
- The worker pushes/pops from the **head** (LIFO locally for cache locality).
- An idle worker (thief) steals from the **tail** (FIFO stealing for fairness).

You must design the data structures and synchronization strategy.

## Input Format

Given:

- `W` workers
- Up to `10^6` tasks
- Tasks can spawn additional tasks

## Output Format

Provide a design that includes:

1. Worker-local deque operations and their synchronization
2. Steal operation correctness under races
3. How workers sleep/wake when global work is exhausted
4. How you prevent contention on shared structures

## Constraints

- `1 <= W <= 10^4`
- Total tasks up to `10^6`
- Must scale under contention (avoid a single global lock if possible)

## Example

If tasks are unevenly distributed (one worker gets most tasks), work stealing should shift tasks to idle workers so completion times become balanced.

## Related Topics

Concurrency, Scheduling, Deques, Lock-free/Lock-based Design

