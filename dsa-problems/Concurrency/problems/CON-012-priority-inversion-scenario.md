---
problem_id: CON_PRIORITY_INVERSION__8F42
display_id: CON-012
slug: priority-inversion-scenario
title: "Priority Inversion Scenario"
difficulty: Medium
difficulty_score: 50
topics:
  - Concurrency
  - Scheduling
  - Real-Time Systems
tags:
  - concurrency
  - scheduling
  - priority-inversion
  - medium
premium: true
subscription_tier: basic
time_limit: 1500
memory_limit: 256
---

# Priority Inversion Scenario

## Problem Statement

Describe a concrete scenario of **priority inversion**:

- A high-priority thread is blocked waiting for a lock held by a low-priority thread.
- A medium-priority thread runs and prevents the low-priority thread from making progress.
- Result: high-priority thread is indirectly delayed by the medium-priority thread.

Then propose and explain mitigation:

- **priority inheritance**, and/or
- **priority ceiling protocol**

## Input Format

No strict input.

## Output Format

Your answer must include:

1. Timeline with 3 threads: `H` (high), `M` (medium), `L` (low)
2. Where the lock is acquired and where blocking happens
3. Mitigation explanation and what changes in scheduling
4. One limitation or caveat

## Constraints

- N/A (conceptual)

## Related Topics

Concurrency, Scheduling, Locks, Real-Time Systems


## Solution Template

### Python

```python
def solve():
    return 0
1. Scenario Timeline:
   - **T1 (Low)** starts, acquires Lock `L`.
   - **T2 (High)** starts, preempts T1, tries to acquire Lock `L`. Blocks.
   - **T3 (Medium)** starts. Since `Priority(T3) > Priority(T1)`, T3 preempts T1.
   - T1 cannot run (CPU hogged by T3). T1 holds `L`.
   - T2 is waiting for `L`.
   - Result: T2 (High) is waiting for T3 (Medium) to finish, which is an inversion of priority.

2. Mitigation Strategies:
   - **Priority Inheritance Protocol (PIP)**:
     - When T2 (High) blocks on `L` held by T1 (Low), T1 temporarily inherits T2's high priority.
     - Now `Priority(T1) > Priority(T3)`, so T1 runs, finishes critical section, releases `L`.
     - T1 returns to low priority. T2 acquires `L` and runs.
   - **Priority Ceiling Protocol (PCP)**:
     - Assign a "Ceiling Priority" to each mutex (max priority of any thread that *might* lock it).
     - A task can lock a mutex only if its dynamic priority is higher than the ceiling of any currently locked mutex (system-wide).
     - Prevents deadlock and chaining.

3. Limitation:
   - Complexity to implement in kernel/user-space.
   - Does not prevent waiting entirely, just bounds the inversion time to the length of the critical section.
""")

if __name__ == "__main__":
    solve()
```

