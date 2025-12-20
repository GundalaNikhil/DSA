---
problem_id: CON_MS_QUEUE_SKETCH__E17B
display_id: CON-010
slug: lock-free-queue-sketch
title: "Lock-Free Queue Sketch"
difficulty: Medium
difficulty_score: 62
topics:
  - Concurrency
  - Lock-Free
  - Queues
  - Memory Reclamation
tags:
  - concurrency
  - lock-free
  - queue
  - hazard-pointers
  - epoch
  - medium
premium: true
subscription_tier: basic
---

# Lock-Free Queue Sketch (Michael–Scott)

## Problem summary

The Michael–Scott queue is a classic lock-free FIFO queue implemented as a linked list with:

- atomic `head`
- atomic `tail`
- a dummy (sentinel) node to simplify empty-case handling

Operations are built from CAS and “helping” (threads assist each other to move pointers forward).

## Data structure invariants

- The list always has at least the dummy node.
- `head` points to the dummy or a node before the first real element.
- `tail` points to the last node, but may lag behind temporarily.
- The true queue content is nodes reachable from `head.next`.

The key idea: allow `tail` to be slightly stale, and have threads help advance it.

## Enqueue sketch

Goal: append a new node at the end.

High-level steps:

1) Read `tail` and `tail.next`.
2) If `tail.next != null`, then `tail` is behind; help by CAS advancing `tail`.
3) Else `tail.next == null`: attempt to link new node with CAS on `tail.next`.
4) After linking succeeds, try to swing `tail` to new node (helping step; if it fails, someone else advanced it).

This design ensures progress even under contention.

## Dequeue sketch

Goal: remove the node after head (the first real element).

High-level steps:

1) Read `head`, `tail`, and `head.next`.
2) If `head.next == null`, queue is empty.
3) If `head == tail` but `head.next != null`, tail is behind; help move `tail` forward.
4) Else attempt to swing `head` to `head.next` using CAS.
   - if CAS succeeds, return the removed value.

Why it works: the successful CAS on `head` is the linearization point for dequeue.

## Why “helping” matters

Without helping:

- one thread could link nodes but never update tail due to preemption
- others would get stuck thinking tail is the end

Helping guarantees lock-free progress: some thread always completes an operation in finite steps (system-wide progress).

## The painful part: memory reclamation

Even if the algorithm is correct logically, you can still crash if you free nodes too early.

Problem:

- Thread T1 reads `head.next` into a local pointer.
- Thread T2 dequeues that node and frees it.
- T1 now dereferences freed memory: use-after-free.

This is not a “bug in your code”; it is a fundamental hazard in lock-free algorithms.

## One safe reclamation strategy (epoch-based)

Epoch-based reclamation (EBR) idea:

- Each thread announces when it is inside the queue operations (“active in epoch e”).
- When removing nodes, you put them into a retire list tagged with current epoch.
- You free retired nodes only when all threads have advanced past that epoch (meaning nobody can still hold references).

Tradeoffs:

- Very fast in steady state.
- Can delay freeing if a thread stalls for a long time (memory growth).

Alternative: hazard pointers provide more precise reclamation but add per-access overhead.

## What interviewers expect

You do not need to memorize every line of the algorithm, but you must:

- mention dummy node
- explain tail can lag and is advanced by helping
- identify the need for safe reclamation and name one correct technique

