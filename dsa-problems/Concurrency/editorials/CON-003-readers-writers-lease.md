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
---

# Readers-Writers with Lease Expiry

## Problem summary

We want a readers-writers lock with a twist:

- Readers acquire a read lock with a lease time `L`.
- After `L`, the reader must either renew or release.
- Writers should not starve (eventual progress).

This is a realistic “production-grade” constraint: leases are a safety mechanism when you cannot fully trust every reader to release promptly (crashes, bugs, long GC pauses).

## What makes this harder than standard RW-locks

Standard RW-locks assume:

- readers release when they are done

Leased readers add:

- time-driven state changes (expiry)
- a renewal protocol
- a fairness policy that interacts with renewals

If you allow unlimited renewals while a writer is waiting, you have recreated writer starvation.

## Real-world scenario

Think of a shared in-memory index:

- Readers: look up student records frequently.
- Writers: update records occasionally (fee payment, course enrollment).

If readers can renew forever, an update (writer) might never happen under heavy read traffic. In real systems, stale data or stuck writers becomes a correctness problem (not just performance).

## Design goal (the non-negotiables)

1) Readers can proceed concurrently when no writer is waiting.
2) Once a writer arrives, the system must enter a “drain readers” mode:
   - no new readers
   - no renewals that would extend beyond a bounded window
3) Writer proceeds after all active leases expire or readers release.
4) After writer finishes, readers can flow again.

## One clean algorithm (writer-intent gate + lease tracking)

Shared state (under a single mutex):

- `activeReaders`: number of currently active readers
- `writerActive`: boolean
- `writerWaiting`: number of waiting writers (or a boolean `writerPending`)
- `leaseExpiryMinHeap`: a min-heap of expiry timestamps for active readers (or equivalent tracking)
- condition variables:
  - `canRead`
  - `canWrite`

Why the heap: a writer needs to know when the next lease expires so it can wait efficiently (timed wait).

### Read lock acquire

Reader can enter if:

- no writer is active, and
- no writer is waiting (fairness gate)

Protocol:

- lock mutex
- while `writerActive || writerWaiting > 0`: wait(canRead)
- activeReaders++
- push `now + L` into heap
- unlock mutex

### Read lease renewal

This is the key fairness point.

Rule:

- Renewal is allowed only if `writerWaiting == 0`.

If a writer is waiting:

- renewal is denied (or allowed only if it does not extend beyond the current expiry, which is pointless)
- reader must finish quickly and release before its existing lease expires

Renew protocol:

- lock mutex
- if `writerWaiting > 0`: return “renew denied”
- update this reader’s expiry to `now + L` (update heap entry)
- unlock mutex

Implementation note: updating a heap entry requires an index or removing and reinserting; in many designs you store per-reader records.

### Read unlock

- lock mutex
- activeReaders--
- remove this reader’s expiry from heap
- if `activeReaders == 0`: signal(canWrite)
- unlock mutex

### Write lock acquire (timed waiting on leases)

Writer arrival:

- lock mutex
- writerWaiting++
- while `writerActive`: wait(canWrite)

Now we need to wait until no active readers remain OR their leases expire.

While `activeReaders > 0`:

- let `t = minExpiry` from heap
- timed wait until `t` (or until signaled by a reader unlock)
- when woken, remove any expired leases from tracking and decrement `activeReaders` accordingly (depending on your model)

Once `activeReaders == 0`:

- writerWaiting--
- writerActive = true
- unlock mutex

### Write unlock

- lock mutex
- writerActive = false
- if `writerWaiting > 0`: signal(canWrite) else broadcast(canRead)
- unlock mutex

## Important correctness notes

### 1) You cannot “force unlock” safely in general

Lease expiry does not magically make it safe to unlock a mutex held by a crashed thread. In real OS primitives, you cannot take a lock away like that without risking corrupted shared state.

So in a real implementation, lease-based reads are typically used when:

- readers are “logical” (they hold a token, not a raw OS lock), and
- the protected data structure supports safe reclamation / versioning (copy-on-write, RCU-like approaches), or
- reads are designed to be idempotent and safe under retry.

For an interview/design question, it’s fine to treat “lease expiry” as “reader promises it will stop reading and will not access shared data after expiry”.

State that assumption explicitly.

### 2) Fairness policy is the heart of the solution

The simplest correct fairness rule:

- When any writer is waiting, block new readers and deny renewals.

This guarantees writer progress after at most `L` (plus scheduler delays) because existing readers can’t extend their leases.

### C++omplexity

- Lock/unlock operations are O(log R) if you manage expiry with a heap of `R` readers.
- If you do not need exact min-expiry (e.g., you just sleep for `L` and recheck), you can reduce complexity but may increase latency.

## What interviewers look for

- You mention denying renewals when writers are waiting (writer starvation fix).
- You use a monotonic clock and timed waits.
- You acknowledge that “force releasing” threads is unsafe; leases are a protocol contract.

