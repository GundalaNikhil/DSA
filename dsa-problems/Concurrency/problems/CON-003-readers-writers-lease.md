---
problem_id: CON_RW_LEASE__D08C
display_id: CON-003
slug: readers-writers-lease
title: "Readers-Writers with Lease Expiry"
difficulty: Medium
difficulty_score: 58
topics:
  - Concurrency
  - Readers Writers
  - Scheduling
  - Fairness
tags:
  - concurrency
  - readers-writers
  - fairness
  - medium
premium: true
subscription_tier: basic
time_limit: 3000
memory_limit: 256
---

# Readers-Writers with Lease Expiry

## Problem Statement

You are building an in-memory cache used by many threads:

- Readers are frequent and should be fast.
- Writers are less frequent but must not starve.

Design a **readers-writers lock** variant where each reader acquires a **lease time `L`**:

- A reader may hold the lock only until its lease expires.
- Before expiry, it may **renew** the lease (if safe) or must **release**.
- A writer that arrives should eventually proceed: it may wait for active reader leases to expire or be released, but readers should also not be permanently blocked (no deadlock/livelock).

Provide an algorithm-level design.

## Input Format

Given:

- Lease duration `L` (milliseconds)
- `lockRead()`, `renewRead()`, `unlockRead()`
- `lockWrite()`, `unlockWrite()`

## Output Format

Describe:

1. State variables (reader count, writer intent flag, timestamps, etc.)
2. Waiting rules for readers and writers
3. How renewals are decided (e.g., blocked once a writer is waiting)
4. How the writer ensures it will not starve
5. Any assumptions about time source and drift

## Constraints

- Many threads (assume high contention)
- Lease times up to seconds (`L <= 10^4 ms` is typical, but design should be general)
- Must handle:
  - reader crash/forgetting to release (lease expiry is the safety net)
  - frequent renewals without starving writers

## Example

**Scenario:**

- Readers acquire at `t=0ms` with `L=50ms`
- A writer arrives at `t=20ms`
- Readers attempt to renew at `t=40ms`

**Expected behavior (high-level):**

- The writer should not starve: once a writer is waiting, renewals should be restricted so existing reader leases naturally drain.
- The writer proceeds after the last active lease expires (or readers release earlier), then releases and readers can proceed again.

## Notes

- The “lease” is a safety mechanism for slow/crashed readers, but it introduces a new design point: **renewal policy**.
- To prevent writer starvation, most correct designs treat “writer waiting” as a **gate** that blocks new readers and prevents renewal past the current lease window.

## Related Topics

Concurrency, Readers-Writers Locks, Fairness, Timing

## Solution Template

### Python

```python
def solve():
    return 0
1. State Variables:
   - `active_readers`: count of readers currently holding the lease.
   - `writer_waiting`: boolean/count, true if a writer is waiting.
   - `max_lease_expiry`: timestamp of the furthest lease expiry among active readers.
   - `mutex`: protects state.
   - `cond_read`: for readers to wait.
   - `cond_write`: for writers to wait.

2. Waiting Rules:
   - **Reader Entry**: Can proceed if `!writer_waiting`. If valid, increments `active_readers`, sets local lease expiry `now + L`.
   - **Reader Renewal**: Can renew if `!writer_waiting`. Updates local lease and global `max_lease_expiry`.
   - **Writer Entry**: Sets `writer_waiting = true`. Waits on `cond_write` until `active_readers == 0`.

3. Renewal Policy:
   - If a writer arrives (`writer_waiting` becomes true), NEW readers are blocked.
   - EXISTING readers attempting to renew are *also* blocked (or told to release). This allows the active leases to naturally expire within at most `L` time, preventing writer starvation.

4. Writer Starvation Prevention:
   - The `writer_waiting` flag acts as a gate. Once set, no new read leases (or renewals) are granted.
   - The system drains active readers.
   - Writer proceeds after the last reader leaves.
   - Upon exit, writer clears `writer_waiting` and wakes all readers/writers.

5. Assumptions:
   - Readers cooperate (check renewal or release).
   - Clocks are reasonably synchronized or monotonic for `L`. Lease expiry is a failsafe.
""")

if __name__ == "__main__":
    solve()
```

