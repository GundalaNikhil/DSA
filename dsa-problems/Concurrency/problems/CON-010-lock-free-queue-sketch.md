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
time_limit: 3000
memory_limit: 256
---

# Lock-Free Queue Sketch

## Problem Statement

Outline the **Michael–Scott lock-free queue** (a classic concurrent FIFO queue):

- Uses atomic `head` and `tail` pointers
- Supports `enqueue(x)` and `dequeue()` concurrently by many threads
- Must remain correct without a global lock

Additionally, discuss why **memory reclamation** is a hard part of lock-free queues and briefly describe one safe strategy:

- hazard pointers, or
- epoch-based reclamation (EBR), or
- reference counting with caveats

## Input Format

No strict input. Assume:

- Many threads
- A node-based linked list implementation

## Output Format

Your answer must include:

1. Key invariants for `head`/`tail` and the dummy node
2. How `enqueue` helps advance `tail`
3. How `dequeue` helps advance `tail` and moves `head`
4. Why ABA + reclamation matters and one mitigation

## Constraints

- Many threads and high contention
- Must be linearizable (operations appear atomic)

## Example

Sequence: enqueue A, B, C; then dequeue twice ⇒ outputs must be A then B.

## Related Topics

Concurrency, Lock-Free Data Structures, Atomics, Memory Reclamation

