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
