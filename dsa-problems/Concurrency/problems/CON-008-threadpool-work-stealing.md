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


## Solution Template

### Python

```python
def solve():
    return 0
1. Worker-Local Deque:
   - Each worker `i` has a Deque `D_i`.
   - **Local Ops (Push/Pop)**: Worker `i` pushes new tasks to `D_i` bottom (Tail). Pops from `D_i` bottom (Tail). This is LIFO (Stack-like) for locality.
   - **Steal Ops**: Thief `j` steals from `D_i` top (Head). This is FIFO for fairness and to avoid conflict with local ops at the other end.
   - **Synchronization**:
     - Use a heavy lock? No, performance.
     - Use CAS on `top` and `bottom` indices.
     - Chase-Lev Deque is the standard lock-free structure.
     - Minimal locking: Use a standard Mutex/Spinlock per deque if simplest, but Lock-Free is standard description.

2. Steal Correctness:
   - If `D_i` has many items, Local Pop and Steal don't conflict (different ends).
   - Conflict only when Deque has 1 item (or becomes empty).
   - Use CAS/Atomic loop. If Local Pop sees size 0 or conflict, it handles empty/contention.
   - If Thief sees conflict or empty, it retries or moves to next victim.

3. Sleep/Wake Strategy:
   - If Worker local deque is empty AND steal attempts fail (all other queues empty):
     - Worker enters "Parked" state.
     - Increments `idle_workers` count.
     - Waits on a global Condition Variable or Semaphore.
   - When a task is added (globally or locally):
     - If `idle_workers > 0`, signal one sleeper.

4. Preventing Contention:
   - Randomized Stealing: Thief picks a random victim rather than iterating 0..W leads to less contention.
   - Backoff: If failed to steal, yield/sleep briefly before retry.
   - Local LIFO: keeps hot data in local cache, avoiding true sharing.
""")

if __name__ == "__main__":
    solve()
```

