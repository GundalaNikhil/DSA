---
problem_id: CON_PRIO_QUEUE_AGING__C4B7
display_id: CON-002
slug: producer-consumer-priority-aging
title: "Producer-Consumer with Priority and Aging"
difficulty: Medium
difficulty_score: 55
topics:
  - Concurrency
  - Condition Variables
  - Producer Consumer
  - Priority Queue
tags:
  - concurrency
  - producer-consumer
  - condition-variables
  - priority-queue
  - medium
premium: true
subscription_tier: basic
time_limit: 3000
memory_limit: 256
---

# Producer-Consumer with Priority and Aging

## Problem Statement

Design a **bounded, thread-safe priority queue** that supports **multiple producers** and **multiple consumers**:

- Higher integer priority means “more important”.
- When the queue is full, producers **block** until space is available.
- When the queue is empty, consumers **block** until an item is available.
- To prevent starvation, items **age** logically: after each full `T` milliseconds spent waiting in the queue, an item’s effective priority increases by `+1`.
- Your design must avoid **lost wakeups** and must be safe under spurious wakeups (common with condition variables).

You must provide a clear design (data structures + synchronization protocol). Code is optional; correctness reasoning is required.

## Input Format

This is a design problem. For evaluation, assume these parameters are given:

- `capacity` (max elements in the buffer), up to `10^6`
- `T` in milliseconds (aging period)
- Multiple producer/consumer threads calling:
  - `put(item, basePriority)`
  - `take() -> item`

## Output Format

Write a design that includes:

1. The shared state and data structures (what is stored per item)
2. Which concurrency primitives you use (mutex/monitor, condition variables, semaphores, etc.)
3. Exact wait conditions and wake-up rules to avoid lost wakeups
4. How you compute effective priority with aging efficiently
5. Why starvation is prevented

## Constraints

- `1 <= capacity <= 10^6`
- `1 <= T <= 10^9` (ms)
- Many threads (assume tens to thousands)
- Must be safe under:
  - spurious wakeups
  - thread preemption at any point

## Example

**Scenario:**

- `capacity = 2`, `T = 100ms`
- Producer inserts items in order (arrival times shown):
  - at `t=0ms`: item A with priority 1
  - at `t=10ms`: item B with priority 5
  - at `t=20ms`: item C with priority 2 (blocks because full)
- Consumer performs `take()` at `t=30ms`, then again at `t=110ms`, then again at `t=120ms`

**Expected dequeue order (one correct outcome):**

- At `t=30ms`: B (priority 5)
- At `t=110ms`: A has waited 110ms ⇒ aged by +1 ⇒ effective priority 2; C may have entered after space freed
- Overall: priorities observed like `[5, 2, 2]` for B, then A (aged), then C (base 2)

## Notes

- “Aging” must not require scanning the entire queue on every operation at large scale.
- Avoid designs that rely on “signal without holding the lock” (classic lost-wakeup bug).

## Related Topics

Concurrency, Condition Variables, Producer-Consumer, Priority Queue

