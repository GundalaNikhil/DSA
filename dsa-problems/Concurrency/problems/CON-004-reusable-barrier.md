---
problem_id: CON_REUSABLE_BARRIER__61E2
display_id: CON-004
slug: reusable-barrier
title: "Reusable Barrier"
difficulty: Medium
difficulty_score: 52
topics:
  - Concurrency
  - Barriers
  - Condition Variables
tags:
  - concurrency
  - barrier
  - condition-variables
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Reusable Barrier

## Problem Statement

In parallel programming, a **barrier** is a synchronization point: no thread can proceed past the barrier until **all `N` threads** have arrived.

Design and implement a **reusable** barrier for `N` threads:

- The same threads will hit the barrier multiple times (phases).
- The barrier must release all threads together for each phase.
- It must reset correctly for the next phase.

You may use condition variables or semaphores.

## Input Format

Given:

- `N` (number of participating threads)
- A `barrier()` call executed by each of the `N` threads in each phase

## Output Format

Provide:

1. The algorithm (state + synchronization)
2. Why it is reusable (how phase separation works)
3. How you avoid lost wakeups and handle spurious wakeups

## Constraints

- `1 <= N <= 10^4`
- Many phases; threads can be preempted arbitrarily

## Example

For `N=3`, in each phase:

- Thread 1 reaches barrier
- Thread 2 reaches barrier
- Thread 3 reaches barrier

Only after the third arrival are all three released. In the next phase, the barrier behaves the same again.

## Related Topics

Concurrency, Barriers, Condition Variables, Semaphores

