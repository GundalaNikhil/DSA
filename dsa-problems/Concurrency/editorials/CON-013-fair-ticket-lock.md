---
problem_id: CON_TICKET_LOCK__55D9
display_id: CON-013
slug: fair-ticket-lock
title: "Fair Ticket Lock"
difficulty: Medium
difficulty_score: 57
topics:
  - Concurrency
  - Locks
  - Atomics
  - Fairness
tags:
  - concurrency
  - ticket-lock
  - fairness
  - cache-coherence
  - medium
premium: true
subscription_tier: basic
---

# Fair Ticket Lock

## Problem summary

Ticket locks provide FIFO fairness:

- Each thread gets a ticket number.
- Threads wait until their ticket is “now serving”.

This prevents starvation that can happen with unfair spinlocks.

## The algorithm (pseudocode)

Shared atomics:

- `nextTicket` (initial 0)
- `nowServing` (initial 0)

Lock:

```
lock():
  my = fetch_add(nextTicket, 1)
  while (nowServing.load() != my):
    spin
```

Unlock:

```
unlock():
  nowServing.fetch_add(1)
```

## Why it is fair

- Tickets are handed out in increasing order.
- `nowServing` increases by 1 on each unlock.
- So threads enter the critical section in ticket order (FIFO).

Assuming:

- each thread eventually runs (scheduler fairness)
- the lock holder eventually unlocks

## The performance downside: cache-coherence contention

In the spin loop, every waiting thread repeatedly reads `nowServing`.

On many-core systems, `nowServing` becomes a hot cache line:

- unlock writes to `nowServing` (invalidates caches)
- all spinners refetch it

This can cause heavy cache-coherence traffic and degrade scalability.

This is why ticket locks can perform poorly at high core counts under contention, even though they are fair.

## Improvements (what to mention)

### 1) Use a blocking lock (mutex) when waits are long

Ticket locks are busy-wait locks. If your waits are long or oversubscribed, sleeping is better.

### 2) MCS / CLH locks (queue-based spinlocks)

Queue locks make each thread spin on a local flag instead of one global variable:

- far less cache bouncing
- better scalability under contention

In interviews: “Ticket lock is fair but contends on a single cache line; MCS scales better because each thread spins locally.”

## Takeaway

Ticket locks are a clean fair lock primitive, but fairness alone is not performance. Under high contention, the memory subsystem becomes the bottleneck.
