---
problem_id: CON_PRIORITY_INVERSION__8F42
display_id: CON-012
slug: priority-inversion-scenario
title: "Priority Inversion Scenario"
difficulty: Medium
difficulty_score: 50
topics:
  - Concurrency
  - Scheduling
  - Real-Time Systems
tags:
  - concurrency
  - scheduling
  - priority-inversion
  - medium
premium: true
subscription_tier: basic
---


# Priority Inversion Scenario

## Problem Summary

Describe a concrete scenario of **priority inversion**:

- A high-priority thread is blocked waiting for a lock held by a low-priority thread.
- A medium-priority thread runs and prevents the low-priority thread from making progress.
- Result: high-priority thread is indirectly delayed by the medium-priority thread.

## What priority inversion means

Priority inversion occurs when a high-priority thread is blocked behind a low-priority thread, and meanwhile medium-priority threads run and prevent the low-priority thread from running.

So the high-priority thread is indirectly delayed by medium-priority work it should have preempted.

This is a real bug class in real-time systems.

### Concrete timeline example (H, M, L)

Assume preemptive priority scheduling:

- `L` (low) starts and acquires a mutex `lock`.
- `H` (high) becomes runnable and tries to acquire `lock`:
  - `H` blocks because `L` holds the lock.
- `M` (medium) becomes runnable:
  - `M` preempts `L` because `M` has higher priority than `L`.
  - `L` cannot run, so it cannot release `lock`.
- Result:
  - `H` is blocked waiting for `L`
  - `L` is prevented from running by `M`
  - effectively `M` delays `H` even though `H` has higher priority

This is the inversion: medium outranks low, but ends up outranking high indirectly.

## Mitigation 1: Priority inheritance

Idea:

- If `L` holds a lock needed by `H`, temporarily boost `L`’s priority to match `H`.

Effect:

- Once `H` blocks on `lock`, `L` inherits high priority.
- Then `L` can preempt `M`, run, and release the lock.
- After releasing, `L` returns to low priority.

This bounds the inversion time to the duration of the critical section (plus scheduling overhead).

## Mitigation 2: Priority ceiling protocol

Idea:

- Each lock is assigned a priority ceiling (max priority of threads that can lock it).
- When a thread acquires the lock, its priority is immediately raised to that ceiling.

Effect:

- Prevents certain deadlocks and bounds inversion more aggressively.

### Caveats (what to say to be accurate)

- Priority inheritance can chain: if `L` is blocked on another lock held by `X`, the boost can propagate.
- This is not free: boosting priorities increases scheduler complexity and can reduce overall throughput.
- In general-purpose OSes, many mutexes are not priority-inheriting by default.

## Takeaway

If you are in any system where priorities matter (real-time threads, multimedia pipelines, robotics), you must consider priority inversion and use the right mutex protocol.
