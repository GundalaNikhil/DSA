---
problem_id: CON_LOCK_CHOICE__A9F1
display_id: CON-001
slug: mutex-vs-spinlock-selection
title: "Mutex vs Spinlock Selection"
difficulty: Easy
difficulty_score: 28
topics:
  - Concurrency
  - Locks
  - Performance
tags:
  - concurrency
  - mutex
  - spinlock
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Mutex vs Spinlock Selection

## Problem Statement

You are reviewing a performance bug in a multi-threaded service. A shared counter/structure is protected by a lock. Based on rough timing estimates, decide whether a **mutex** (sleeping lock) or a **spinlock** (busy-wait lock) is more appropriate, and justify the choice.

This is a **reasoning** question: you should not write code; you should write a concise, technically correct justification.

## Input Format

- One line with two numbers:
  - `cs` = average critical section duration in microseconds (µs)
  - `w` = expected time a contending thread would wait before entering the critical section in microseconds (µs)

## Output Format

Print two lines:

1. `MUTEX` or `SPINLOCK`
2. A short justification (2–6 sentences) referencing CPU waste, context-switch overhead, and expected contention.

## Constraints

- `0 < cs <= 10^6`
- `0 <= w <= 10^9`
- Assume a modern OS where:
  - Mutex may park a thread and cause a context switch (non-trivial overhead)
  - Spinlocks burn CPU while waiting

## Examples

### Example 1

**Input:**
```
1 50
```

**Output:**
```
MUTEX
Expected wait (50µs) is far larger than the 1µs critical section, so spinning wastes CPU for ~50µs per contending thread. A mutex can block and let the CPU run other work, and the context-switch cost is justified by the long wait.
```

### Example 2

**Input:**
```
2 1
```

**Output:**
```
SPINLOCK
The expected wait is tiny (~1µs) and comparable to the critical section (2µs), so the lock is held briefly. Spinning for such a short time can be cheaper than parking/unparking (context switching) and avoids scheduler latency.
```

## Notes

- The best choice depends on **how long threads are expected to wait** and whether the system is **oversubscribed** (more runnable threads than CPU cores).
- In interview answers, explicitly mention: **CPU burning vs scheduler overhead**.

## Related Topics

Concurrency, Locks, Performance

---

## Answer Template (Recommended)

Use this structure in your solution:

1. Pick `MUTEX` or `SPINLOCK`
2. Compare `w` vs `cs`
3. Mention CPU waste (spinning) vs context-switch overhead (mutex)
4. Mention oversubscription / core count assumptions


## Solution Template

### Python

```python
def solve():
    return 0
if __name__ == "__main__":
    solve()
```

