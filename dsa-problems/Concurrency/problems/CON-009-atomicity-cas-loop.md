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
time_limit: 2000
memory_limit: 256
---

# Atomicity with CAS Loop

## Problem Statement

You are implementing a concurrent counter without a mutex.

1) Show how to implement `atomicIncrement()` using a **compare-and-swap (CAS)** loop.

2) Explain the **ABA problem**: how it can break CAS-based algorithms even when “the value looks unchanged”.

3) Propose at least one mitigation strategy (tagged pointers/version counters, hazard pointers, epoch GC, etc.), and explain when it is needed.

## Input Format

No strict input. Assume:

- A shared atomic integer `x`
- Multiple threads calling `atomicIncrement()` concurrently

## Output Format

Your answer must include:

- A correct CAS-loop sketch for increment (pseudocode is fine)
- A crisp ABA explanation with a concrete example
- At least one mitigation and its tradeoffs

## Constraints

- Many threads
- You must assume preemption can happen between any two instructions

## Example

If `x = 0` initially and 3 threads call `atomicIncrement()` concurrently, the final value must be `3` (no lost increments).

## Related Topics

Concurrency, Atomic Operations, Lock-Free Programming


## Solution Template

### Python

```python
def solve():
    return 0
1. CAS Loop Sketch (Atomic Increment):
   ```python
   def atomic_increment(x):
       return 0
   ```

2. ABA Problem:
   - ABA occurs when a value changes from A to B and back to A.
   - A thread reads A, calculates, then tries CAS(A -> New). It succeeds because value is A, but it missed the intermediate B state.
   - **Example**: Stack Pop.
     - Stack: Top -> A -> B.
     - Thread 1 Reads Top (A), Next (B). Preempted.
     - Thread 2 Pops A, Pops B. Pushes A back. Stack: Top -> A.
     - Thread 1 resumes: CAS(Top, A -> B). Succeeds!
     - Stack is now Top -> B. BUT B was freed/gone! Stack is corrupted.

3. Mitigation Strategies:
   - **Tagged Pointers / Version Counting (Preferred for simple cases)**:
     - Store `(value, version)` in the atomic word.
     - CAS checks both. `A -> B -> A` becomes `(A, v1) -> (B, v2) -> (A, v3)`.
     - `CAS((A, v1), ...)` fails against `(A, v3)`.
   - **Hazard Pointers**: Threads publish "I am reading node P". Other threads cannot free P while published. Solves use-after-free inherent in ABA.
""")

if __name__ == "__main__":
    solve()
```

