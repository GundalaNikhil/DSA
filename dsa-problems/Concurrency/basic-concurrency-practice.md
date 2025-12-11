# Original Concurrency Primitives & Patterns Practice Set (16 Questions)

## 1) Mutex vs Spinlock Selection
- Slug: mutex-vs-spinlock-selection
- Difficulty: Easy
- Problem: Given contention time estimates (critical section duration, expected wait), decide whether to use a mutex or spinlock and justify.
- Constraints: Provide reasoning, not code.
- Example:
  - Input: critical section 1µs, expected wait 50µs
  - Output: prefer mutex (spinning wasteful)

## 2) Producer-Consumer with Bounded Buffer
- Slug: producer-consumer-bounded
- Difficulty: Easy-Medium
- Problem: Design thread-safe bounded queue for multiple producers/consumers using condition variables; avoid lost wakeups.
- Constraints: buffer size up to 10^6.
- Example:
  - Input: buffer size 2, ops: prod A, prod B, prod C, cons X, cons Y, cons Z
  - Output: operations block/unblock correctly

## 3) Readers-Writers with Preference
- Slug: readers-writers-preference
- Difficulty: Medium
- Problem: Implement readers-writers lock with writer preference; avoid writer starvation.
- Constraints: many threads.
- Example:
  - Input: sequence R,R,W,R
  - Output: writers get priority after existing readers

## 4) Barrier with Reuse
- Slug: reusable-barrier
- Difficulty: Medium
- Problem: Implement a reusable barrier for N threads using condition variables or semaphores.
- Constraints: N <= 10^4.
- Example:
  - Input: N=3 threads arriving
  - Output: all released together each phase

## 5) Semaphore-Based Rate Limiter
- Slug: semaphore-rate-limiter
- Difficulty: Medium
- Problem: Allow at most `k` events per second. Implement using semaphores/tokens and a refill thread/timer.
- Constraints: `1 <= k <= 10^6`.
- Example:
  - Input: k=2, events at t=0,0,0.5,1.2
  - Output: first two proceed, third blocked until refill at t=1

## 6) Deadlock Detection in Resource Graph
- Slug: deadlock-detection-resource-graph
- Difficulty: Medium
- Problem: Given wait-for graph snapshots, detect cycles to identify deadlocks.
- Constraints: nodes <= 10^5.
- Example:
  - Input: edges A->B, B->A
  - Output: deadlock detected

## 7) Dining Philosophers with Waiter
- Slug: dining-philosophers-waiter
- Difficulty: Medium
- Problem: Solve dining philosophers using a waiter/arbiter to avoid deadlock; ensure fairness.
- Constraints: philosophers <= 10^4.
- Example:
  - Input: 5 philosophers
  - Output: no deadlock, bounded waiting

## 8) Thread Pool with Work Stealing
- Slug: threadpool-work-stealing
- Difficulty: Medium
- Problem: Design a work-stealing thread pool; each worker has deque; thieves steal from tail.
- Constraints: tasks up to 10^6.
- Example:
  - Input: tasks distributed unevenly
  - Output: balanced completion times

## 9) Atomicity With CAS Loop
- Slug: atomicity-cas-loop
- Difficulty: Medium
- Problem: Implement atomic increment with compare-and-swap loop; discuss ABA problem and mitigation.
- Constraints: N/A.
- Example:
  - Input: initial 0, 3 concurrent inc
  - Output: final 3

## 10) Lock-Free Queue Sketch
- Slug: lock-free-queue-sketch
- Difficulty: Medium
- Problem: Outline Michael-Scott lock-free queue with head/tail pointers, hazard pointers or epoch reclamation.
- Constraints: many threads.
- Example:
  - Input: enq A,B,C, deq X,Y
  - Output: dequeues in order

## 11) Condition Variable Spurious Wakeup Handling
- Slug: condvar-spurious-wakeup
- Difficulty: Easy
- Problem: Show wait loop pattern to handle spurious wakeups and missed signals.
- Constraints: N/A.
- Example:
  - Input: shared flag false, waiters block; signal sets true
  - Output: waiters recheck predicate

## 12) Priority Inversion Scenario
- Slug: priority-inversion-scenario
- Difficulty: Medium
- Problem: Describe a scenario of priority inversion and propose mitigation (priority inheritance/ceiling).
- Constraints: N/A.
- Example:
  - Input: threads H,M,L with shared lock
  - Output: mitigation via inheritance

## 13) Fair Ticket Lock
- Slug: fair-ticket-lock
- Difficulty: Medium
- Problem: Implement fair lock using ticket dispenser and serving number; discuss cache contention.
- Constraints: many threads.
- Example:
  - Input: threads acquire/release
  - Output: FIFO order

## 14) Bounded Retry with Exponential Backoff
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
