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
---

# Thread Pool with Work Stealing

## Problem summary

Goal: build a thread pool that stays balanced without a single global queue bottleneck:

- each worker has its own deque of tasks
- worker runs local tasks from the head (fast path, low contention)
- idle workers steal from the tail of other workers (slow path, occasional contention)

This is a standard interview-quality design because it tests: scheduling, data-structure concurrency, and performance under contention.

## Real-world scenario

Parallel build system / compiler:

- one module compilation can spawn many sub-tasks
- some modules are heavy, some light
- you want all CPU cores busy, not one core overloaded while others idle

Work stealing naturally balances.

### Core architecture

Components:

- `W` workers (threads)
- each worker has:
  - local deque (double-ended queue)
  - run loop
- a global “sleep/wake” mechanism when no work is available anywhere

Operations:

- owner:
  - `pushHead(task)` when it spawns new work
  - `popHead()` to execute next local task
- thief:
  - `stealTail()` from another worker

## Synchronization strategy (simple and correct)

Two practical levels:

### Level 1: Lock-based deques (easier, acceptable)

Each worker deque has its own mutex.

- owner operations lock the deque mutex briefly
- steal operations lock the victim deque mutex briefly

This avoids a global lock and performs well enough for many cases.

Correctness is straightforward, but there is still contention if many thieves target the same victim.

### Level 2: Chase–Lev lock-free deque (advanced)

Owner operations are mostly lock-free; steals use CAS.

This is high-end and easy to get wrong. For a practice set aimed at interviews, you can describe it at high level without fully implementing.

Strong interview answers mention:

- why the owner uses one end and thieves use the other (reduces races)
- why steals are rarer than local pops (most work stays local)

## How to pick a victim (avoid herd behavior)

If all idle threads steal from the same victim, you create contention.

Use randomized victim selection:

- choose a random worker
- try a bounded number of attempts
- if all fail, go to sleep

## Sleeping and waking (global condition variable)

You need a way to avoid busy-spinning when no tasks exist.

Typical approach:

- global atomic `activeTaskCount` (or a global queue length)
- global mutex + condition variable `workAvailable`

When a worker pushes a task into an empty system, it signals `workAvailable`.
Idle workers wait on `workAvailable`.

This is where lost wakeups occur if implemented incorrectly. Use the standard `while` predicate pattern.

### Correctness and progress arguments

- Safety: tasks are executed exactly once because removal from deque is protected by mutex/CAS.
- Progress: if there is work anywhere, some worker will either pop locally or steal and run it.

Starvation is unlikely with randomized stealing, but strict fairness is not guaranteed unless you enforce it.

### Complexity

- Local push/pop: O(1) with minimal contention.
- Steal: O(1) per attempt, but may retry across victims.
- Space: O(number of tasks).

## What interviewers look for

- Understanding that global queue becomes a bottleneck.
- Correct division: owner head, thief tail.
- A strategy for sleeping (no hot spinning when empty).
- Mention of contention and victim selection.

