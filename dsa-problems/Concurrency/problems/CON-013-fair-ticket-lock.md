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
time_limit: 2500
memory_limit: 256
---

# Fair Ticket Lock

## Problem Statement

Implement a fair lock using the **ticket lock** idea:

- `nextTicket` is an atomic counter that hands out ticket numbers.
- `nowServing` is an atomic counter indicating which ticket may enter.

A thread:

1. Fetches a ticket number.
2. Spins (or waits) until `nowServing` matches its ticket.
3. On unlock, increments `nowServing`.

Additionally, discuss cache contention and how ticket locks behave under high core counts.

## Input Format

No strict input.

## Output Format

Provide:

1. Pseudocode for `lock()` and `unlock()`
2. Why this is FIFO fair
3. Cache-coherence contention discussion (everyone reading `nowServing`)
4. One improvement idea (e.g., MCS lock) and when it’s better

## Constraints

- Many threads / many cores

## Related Topics

Concurrency, Locks, Fairness, Atomics


## Solution Template

### Python

```python
def solve():
    return 0
1. Pseudocode:
   ```python
   class TicketLock:
       def __init__(self):
           return 0
       def lock(self):
           return 0
       def unlock(self):
           return 0
   ```

2. Fairness (FIFO):
   - Tickets are handed out in strictly increasing order (0, 1, 2...).
   - The thread with ticket `k` is ONLY allowed to enter when `nowServing == k`.
   - Since `nowServing` increments by 1 on unlock, threads enter strictly in ticket order. No barge-in possible.

3. Cache Contention:
   - **Thundering Herd / Cache Thrashing**: All waiting threads spin on the SAME `nowServing` cache line.
   - When `nowServing` updates, the line is invalidated for ALL caches. All N threads re-read. O(N) bus traffic per unlock.
   - Poor scalability for high N.

4. Improvement (MCS Lock):
   - **MCS Lock** builds a queue of nodes (linked list) in memory.
   - Each thread spins on its OWN node's flag (`is_locked`).
   - Unlocker only notifies the NEXT thread (writes to next node's cache line).
   - O(1) bus traffic per unlock. Better for high contention/high core count.
""")

if __name__ == "__main__":
    solve()
```

