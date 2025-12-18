# Concurrency Primitives & Patterns Practice Set (16 Questions)

This folder now follows the same structure as other topics:

- `problems/` problem statements
- `editorials/` student-focused explanations
- `testcases/` YAML samples/public/hidden
- `quizzes/` (reserved for later, same naming pattern)
- `images/` (reserved for later, same naming pattern)

Content note (DMCA / originality): the problems and editorials in this topic are written in original wording and are standard CS concepts (locks, condition variables, deadlocks, MVCC). They are not copied from any proprietary platform statements.

## Index

Each entry links to the corresponding files.

1. `CON-001` Mutex vs Spinlock Selection
   - Problem: `problems/CON-001-mutex-vs-spinlock-selection.md`
   - Editorial: `editorials/CON-001-mutex-vs-spinlock-selection.md`
   - Testcases: `testcases/CON-001-mutex-vs-spinlock-selection.yaml`

2. `CON-002` Producer-Consumer with Priority and Aging
   - Problem: `problems/CON-002-producer-consumer-priority-aging.md`
   - Editorial: `editorials/CON-002-producer-consumer-priority-aging.md`
   - Testcases: `testcases/CON-002-producer-consumer-priority-aging.yaml`

3. `CON-003` Readers-Writers with Lease Expiry
   - Problem: `problems/CON-003-readers-writers-lease.md`
   - Editorial: `editorials/CON-003-readers-writers-lease.md`
   - Testcases: `testcases/CON-003-readers-writers-lease.yaml`

4. `CON-004` Reusable Barrier
   - Problem: `problems/CON-004-reusable-barrier.md`
   - Editorial: `editorials/CON-004-reusable-barrier.md`
   - Testcases: `testcases/CON-004-reusable-barrier.yaml`

5. `CON-005` Semaphore-Based Rate Limiter
   - Problem: `problems/CON-005-semaphore-rate-limiter.md`
   - Editorial: `editorials/CON-005-semaphore-rate-limiter.md`
   - Testcases: `testcases/CON-005-semaphore-rate-limiter.yaml`

6. `CON-006` Deadlock Detection in Wait-For Graph
   - Problem: `problems/CON-006-deadlock-detection-resource-graph.md`
   - Editorial: `editorials/CON-006-deadlock-detection-resource-graph.md`
   - Testcases: `testcases/CON-006-deadlock-detection-resource-graph.yaml`

7. `CON-007` Dining Philosophers with Asymmetric Forks
   - Problem: `problems/CON-007-dining-philosophers-staggered.md`
   - Editorial: `editorials/CON-007-dining-philosophers-staggered.md`
   - Testcases: `testcases/CON-007-dining-philosophers-staggered.yaml`

8. `CON-008` Thread Pool with Work Stealing
   - Problem: `problems/CON-008-threadpool-work-stealing.md`
   - Editorial: `editorials/CON-008-threadpool-work-stealing.md`
   - Testcases: `testcases/CON-008-threadpool-work-stealing.yaml`

9. `CON-009` Atomicity with CAS Loop
   - Problem: `problems/CON-009-atomicity-cas-loop.md`
   - Editorial: `editorials/CON-009-atomicity-cas-loop.md`
   - Testcases: `testcases/CON-009-atomicity-cas-loop.yaml`

10. `CON-010` Lock-Free Queue Sketch
    - Problem: `problems/CON-010-lock-free-queue-sketch.md`
    - Editorial: `editorials/CON-010-lock-free-queue-sketch.md`
    - Testcases: `testcases/CON-010-lock-free-queue-sketch.yaml`

11. `CON-011` Condition Variable Spurious Wakeup Handling
    - Problem: `problems/CON-011-condvar-spurious-wakeup.md`
    - Editorial: `editorials/CON-011-condvar-spurious-wakeup.md`
    - Testcases: `testcases/CON-011-condvar-spurious-wakeup.yaml`

12. `CON-012` Priority Inversion Scenario
    - Problem: `problems/CON-012-priority-inversion-scenario.md`
    - Editorial: `editorials/CON-012-priority-inversion-scenario.md`
    - Testcases: `testcases/CON-012-priority-inversion-scenario.yaml`

13. `CON-013` Fair Ticket Lock
    - Problem: `problems/CON-013-fair-ticket-lock.md`
    - Editorial: `editorials/CON-013-fair-ticket-lock.md`
    - Testcases: `testcases/CON-013-fair-ticket-lock.yaml`

14. `CON-014` Bounded Retry with Exponential Backoff
    - Problem: `problems/CON-014-bounded-retry-backoff.md`
    - Editorial: `editorials/CON-014-bounded-retry-backoff.md`
    - Testcases: `testcases/CON-014-bounded-retry-backoff.yaml`

15. `CON-015` Hazards of Signal Handlers
    - Problem: `problems/CON-015-hazards-signal-handlers.md`
    - Editorial: `editorials/CON-015-hazards-signal-handlers.md`
    - Testcases: `testcases/CON-015-hazards-signal-handlers.yaml`

16. `CON-016` Multiversion Concurrency Control (MVCC) Basics
    - Problem: `problems/CON-016-mvcc-basics.md`
    - Editorial: `editorials/CON-016-mvcc-basics.md`
    - Testcases: `testcases/CON-016-mvcc-basics.yaml`
- Slug: bounded-retry-backoff
- Difficulty: Medium
- Problem: Implement retry logic with exponential backoff capped at max delay for transient failures.
- Constraints: N/A.
- Example:
  - Input: operation fails 2 times then succeeds
  - Output: retries at 1ms,2ms, then success

## 15) Hazards of Signal Handlers
- Slug: hazards-signal-handlers
- Difficulty: Medium
- Problem: Identify async-signal-unsafe functions; design minimal-safe handler that sets an atomic flag and returns.
- Constraints: POSIX signals.
- Example:
  - Input: signal arrives during malloc
  - Output: handler just sets flag

## 16) Multiversion Concurrency Control Basics
- Slug: mvcc-basics
- Difficulty: Medium
- Problem: Describe MVCC read/write rules to avoid blocking readers; handle write-write conflicts.
- Constraints: N/A.
- Example:
  - Input: two concurrent transactions T1 (read X) T2 (write X)
  - Output: readers see snapshot; writers serialize
