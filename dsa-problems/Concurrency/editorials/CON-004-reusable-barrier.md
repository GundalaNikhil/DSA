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
---

# Reusable Barrier

## Problem summary

We need a barrier for `N` threads:

- Each thread calls `barrier()` at the end of each phase.
- No one proceeds until all `N` have arrived.
- After release, the barrier resets so the same `N` threads can synchronize again.

The “reusable” part is where most bugs happen: you must prevent threads from phase `k+1` accidentally releasing threads from phase `k`.

## Real-world scenario

Parallel matrix computation in a lab assignment:

- Phase 1: each thread computes its chunk of rows.
- Barrier: ensure all chunks are done.
- Phase 2: each thread uses results from all chunks.

If barrier reuse is broken, phase 2 might start reading partially computed results.

### Correct design with condition variables: count + generation

Shared state under one mutex:

- `count`: number of threads currently arrived in this generation
- `generation`: integer that increments each time the barrier releases
- condition variable `cv`

Barrier procedure:

1) lock mutex
2) store `myGen = generation`
3) increment `count`
4) if `count == N`:
   - reset `count = 0`
   - `generation++`
   - broadcast(cv) to wake everyone
   - unlock mutex and return
5) else:
   - while `generation == myGen`: wait(cv, mutex)
   - unlock mutex and return

The generation variable is the phase separator.

## Why the wait must be a while-loop

Even if your OS never does spurious wakeups (some do), you still need the while-loop because:

- a broadcast could wake you, but before you run, the barrier could already be used for the next generation

Checking `generation` is the safe predicate: “Have we advanced to the next generation?”

## Semaphore-based alternative (two-turnstile barrier)

Another standard reusable barrier uses semaphores:

- A first turnstile that opens when all arrive
- A second turnstile that closes the first and resets for reuse

This is commonly described as “two-phase barrier”. It is more complex to derive but avoids condvar spurious wakeup concerns.

For interview purposes, generation + condvar is typically the cleanest explanation.

### Complexity

- Time per barrier call: O(1) (plus scheduler overhead)
- Space: O(1)

## Typical pitfalls (be explicit)

- Using only `count` without `generation` leads to reuse bugs.
- Using `signal` instead of `broadcast` deadlocks (only one thread wakes).
- Waiting on `if` instead of `while` breaks under spurious wakeups or timing races.
