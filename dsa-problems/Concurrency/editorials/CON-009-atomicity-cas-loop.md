---
problem_id: CON_CAS_INC_ABA__4CE0
display_id: CON-009
slug: atomicity-cas-loop
title: "Atomicity with CAS Loop"
difficulty: Medium
difficulty_score: 53
topics:
  - Concurrency
  - Atomics
  - Compare And Swap
tags:
  - concurrency
  - atomics
  - cas
  - aba
  - medium
premium: true
subscription_tier: basic
---

# Atomicity with CAS Loop

## Problem summary

We want to increment a shared counter safely without using a mutex.

The tool is CAS (compare-and-swap):

- “If memory still equals expected, replace it with new value; otherwise fail.”

The CAS loop is the standard pattern for building lock-free updates.

### CAS-loop increment (pseudocode)

```
atomicIncrement(x):
  while true:
    old = x.load()
    new = old + 1
    if x.compare_exchange(old, new):
      return
```

Key point: `old` must be the expected value passed to CAS, and CAS must be atomic.

Why the loop:

- if two threads race, one wins CAS, the other sees failure and retries with the new value.

## Why this guarantees correctness for increments

For increments, each successful CAS moves the value forward by exactly 1, and failures retry.

So you never lose an increment:

- each thread returns only after it successfully applied its `+1`.

This is linearizable: you can pretend each successful CAS is the “instant” where the increment happened.

## Where students get it wrong

- Reading `old`, computing `new`, and then writing without CAS is not atomic (lost update).
- Doing `if CAS failed then return` is wrong; you must retry.

## The ABA problem (brutally clear)

CAS checks “does the value equal expected right now?”

ABA is when the value changes from A → B → A between your read and CAS.

To the CAS operation, it looks unchanged (still A), so CAS succeeds, but the system state may have changed in a way that breaks correctness.

### Concrete example (stack pointer)

Consider a lock-free stack using a pointer `top`.

- Thread T1 reads `top = A` (node A)
- Thread T2 pops A (top becomes B), then pops B, then pushes A back (top becomes A again)
- Thread T1 now does CAS(top, expected=A, new=next(A))
  - CAS succeeds because top == A
  - But the “A” that is now on top may be a different logical version; intermediate pops happened.

Result: nodes can be lost or structure corrupted.

For a simple integer counter, ABA usually does not matter because the integer increasing makes returning to the same value unlikely (unless overflow). But for pointers and reclamation, ABA is a real bug.

## Mitigations (choose one and explain when needed)

### 1) Version tagging (tagged pointers)

Store `(pointer, version)` together in one atomic word:

- every update increments version
- CAS checks both pointer and version

Then A → B → A still changes version, so CAS fails when it should.

### 2) Hazard pointers

Used for memory reclamation safety:

- before reading a pointer, a thread “publishes” it as a hazard
- other threads do not free nodes that are currently hazards

This prevents use-after-free, and also reduces ABA risk by ensuring the node memory isn’t reused too early.

### 3) Epoch-based reclamation (EBR)

Threads enter an epoch while accessing shared nodes.

- Nodes removed are not freed until all active threads have moved past that epoch.

This prevents memory reuse during concurrent access, which helps with ABA related to reuse.

## What interviewers look for

- You can write the CAS loop.
- You explain ABA with a pointer-based structure, not with vague words.
- You understand that mitigation is usually about pointer structures and memory reclamation, not basic counters.
