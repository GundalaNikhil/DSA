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


## Solution Template

### Python

```python
def solve():
    return 0
1. Michael-Scott Queue Invariants:
   - Linked List of nodes.
   - `head` points to a dummy node (or valid head). `tail` points to last or near-last node.
   - `next` pointers are atomic.
   - Invariant: `tail` is reachable from `head`. List is always connected.

2. Enqueue(x):
   - Allocate Node `new(x)`.
   - Loop:
     - Read `tail` (T), `T.next` (N).
     - If `T` usually points to last, `N` should be Null.
     - If `N` != Null: `tail` is lagging. Help advance it: `CAS(tail, T -> N)`. Retry.
     - If `N` == Null: Try `CAS(T.next, Null -> new)`.
     - If success: `CAS(tail, T -> new)` (Advance tail). Return.
     - If fail: Retry.

3. Dequeue():
   - Loop:
     - Read `head` (H), `tail` (T), `H.next` (N).
     - If `H == T`:
       - If `N == Null`: Queue empty. Return.
       - Else: `tail` lagging. `CAS(tail, T -> N)`. Retry.
     - Read value from `N`.
     - Try `CAS(head, H -> N)`. (Swing head forward).
     - If success: Return value. (Old head H is reclaimed).

4. Memory Reclamation (ABA):
   - Issue: If `Dequeue` reads H, sleeps, then H is freed and reallocated as new node inserted at Tail... complex corruption.
   - **Mitigation (Epoch Based Reclamation)**:
     - Global `epoch`. Threads register into local epoch.
     - `Free(node)` doesn't delete immediately. Adds to `limbo` list for `current_epoch`.
     - When all threads have moved past `epoch e`, nodes in `limbo[e]` are safely deleted.
""")

if __name__ == "__main__":
    solve()
```

