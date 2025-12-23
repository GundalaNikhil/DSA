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
---


# Condition Variable Spurious Wakeup Handling

## Problem Summary

Condition variables can wake up without a matching signal (**spurious wakeup**) and signals can be “missed” if you use them incorrectly (**lost wakeup**).

## The canonical pattern

Condition variables do not store “events”. They coordinate waiting on a shared predicate protected by a mutex.

Correct pattern:

```
lock(mutex)
while (!predicate):
  wait(cv, mutex)   // atomically: release mutex + sleep; then re-acquire mutex
// predicate is true here
unlock(mutex)
```

Signaller pattern:

```
lock(mutex)
predicate = true
signal(cv) or broadcast(cv)
unlock(mutex)
```

## Why the loop is mandatory

Two reasons:

1) Spurious wakeups:
   - the thread can wake up even if nobody signaled
   - if you used `if`, you would proceed with predicate still false

2) Wakeups are not “permissions”:
   - a signal means “something may have changed”
   - by the time you wake and re-acquire the lock, another thread could have consumed the condition again

So you must re-check the predicate under the lock.

## What is a lost wakeup (and how to avoid it)

Lost wakeup happens when:

- thread checks predicate (false)
- before it actually sleeps, another thread sets predicate true and signals
- waiter then goes to sleep and misses the signal, possibly sleeping forever

Proper `wait(cv, mutex)` prevents this because it releases the lock and sleeps atomically. The signaller cannot set predicate+signal in the “gap” while the waiter holds the lock.

## One common buggy pattern

Bug:

```
if (!predicate) wait(cv, mutex)
```

Why it fails:

- spurious wakeup makes you proceed incorrectly
- signal can wake multiple waiters; only one might be able to proceed; others must keep waiting

Another bug: calling `signal()` without holding the lock while updating predicate. That can create lost wakeups or visibility issues depending on memory model.

## Takeaway

Condition variables are about shared state + a predicate, not about sending messages.
Always:

- protect predicate with mutex
- wait in a while loop
