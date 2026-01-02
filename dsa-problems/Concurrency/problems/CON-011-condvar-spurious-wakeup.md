---
problem_id: CON_CONDVAR_WAIT_LOOP__3A0D
display_id: CON-011
slug: condvar-spurious-wakeup
title: "Condition Variable Spurious Wakeup Handling"
difficulty: Easy
difficulty_score: 30
topics:
  - Concurrency
  - Condition Variables
  - Synchronization
tags:
  - concurrency
  - condvar
  - spurious-wakeup
  - easy
premium: true
subscription_tier: basic
time_limit: 1500
memory_limit: 256
---

# Condition Variable Spurious Wakeup Handling

## Problem Statement

Condition variables can wake up without a matching signal (**spurious wakeup**) and signals can be “missed” if you use them incorrectly (**lost wakeup**).

Show the correct wait-loop pattern for a condition variable, and explain:

- why you must check a predicate in a loop
- how to avoid lost wakeups

## Input Format

No strict input.

## Output Format

Provide:

1. The canonical `while (!predicate) wait()` pattern (pseudocode is fine)
2. A 3–6 sentence explanation of spurious wakeups and lost wakeups
3. One common bug pattern and why it fails

## Constraints

- N/A

## Example

Shared flag starts as `false`. Waiters block. A signaller sets it to `true` and signals. Correct code wakes waiters and they proceed only after seeing the flag is `true`.

## Related Topics

Concurrency, Condition Variables, Monitors


## Solution Template

### Python

```python
def solve():
    return 0
1. Canonical Wait Loop:
   ```python
   lock.acquire()
   while not predicate():
       cond.wait()  # Releases lock, sleeps, re-acquires lock upon wake
   # Check passed, proceed
   do_work()
   lock.release()
   ```

2. Spurious & Lost Wakeups:
   - **Spurious Wakeup**: A thread trapped in `cond.wait()` might wake up *without* a corresponding `signal()`/`notify()` call from another thread. This can happen due to OS scheduling quirks or signal handling. Using a `while` loop checks the predicate again; if false, it goes back to sleep.
   - **Lost Wakeup**: Occurs if a thread calls `signal()` *before* the waiter actually waits (and the signal isn't "saved"). Since Condition Variables differ from Semaphores (no state), signals meant for future waiters are lost. Ensuring the waiter checks the predicate *under the lock* before waiting prevents this race.

3. Common Bug:
   - Using `if` instead of `while`:
     ```python
     if not predicate:
         cond.wait()
     # Proceed assuming predicate is true
     ```
     - **Why it fails**: If a spurious wakeup occurs, the thread proceeds with the False predicate, potentially violating invariants (e.g., consuming from empty buffer).
     - Also fails if multiple threads wake up but only one unit of resource is available (Signal-Stealing).
""")

if __name__ == "__main__":
    solve()
```

