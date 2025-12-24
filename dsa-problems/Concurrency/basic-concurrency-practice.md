# Original Concurrency Primitives & Patterns Practice Set (16 Questions)

## 1) Mutex vs Spinlock Selection

- Slug: mutex-vs-spinlock-selection
- Difficulty: Easy
- Problem: Given contention time estimates (critical section duration, expected wait), decide whether to use a mutex or spinlock and justify.
- Constraints: Provide reasoning, not code.
- Example:
  - Input: critical section 1µs, expected wait 50µs
  - Output: prefer mutex (spinning wasteful)

## 2) Producer-Consumer with Priority and Aging

- Slug: producer-consumer-priority-aging
- Difficulty: Medium
- Problem: Design a bounded, thread-safe priority queue (higher number = higher priority) with multiple producers/consumers. Producers may block when full. Older items should age: after `T` ms in the queue, their priority increases by 1 (logical aging) to prevent starvation. Avoid lost wakeups.
- Constraints: buffer size up to 10^6, T given.
- Example:
  - Input: buffer size 2, T=100ms, items: prod (p=1), prod (p=5), prod (p=2) waits; after 100ms, first item ages to p=2
  - Output: consumers get priorities in order [5,2,2]

## 3) Readers-Writers with Lease Expiry

- Slug: readers-writers-lease
- Difficulty: Medium
- Problem: Implement readers-writers lock where each reader holds a lease time `L` after which it must renew or release. Writers must wait for leases to expire or readers to release, but should not starve. Design the algorithm.
- Constraints: many threads, lease times up to seconds.
- Example:
  - Input: readers acquire with L=50ms, writer arrives at 20ms, readers renew?
  - Output: writer proceeds after leases end; no starvation

## 4) Barrier with Reuse

- Slug: reusable-barrier
- Difficulty: Medium
- Problem: Implement a reusable barrier for N threads using condition variables or semaphores.
- Constraints: N <= 10^4.
- Example:
  - Input: N=3 threads arriving
  - Output: all released together each phase

## 5) Semaphore-Based Rate Limiter with Burst and Sliding Window

- Slug: semaphore-rate-limiter-burst-sliding
- Difficulty: Medium
- Problem: Allow at most `k` events per second with burst capacity `b` (can accumulate up to `b` unused tokens). Use a sliding window of duration `w` ms (not fixed 1-second buckets) to track recent events. Implement using semaphores/tokens and a refill thread/timer that respects both burst limits and sliding window constraints.
- Constraints: `1 <= k <= 10^6`, `1 <= b <= 10*k`, `100 <= w <= 10000` ms.
- Example:
  - Input: k=2, b=3, w=1000ms, events at t=0,0,0,500,1200
  - Output: first three proceed (burst), fourth blocked (exceeds k in window), fifth proceeds (oldest event aged out)

## 6) Deadlock Detection in Resource Graph

- Slug: deadlock-detection-resource-graph
- Difficulty: Medium
- Problem: Given wait-for graph snapshots, detect cycles to identify deadlocks.
- Constraints: nodes <= 10^5.
- Example:
  - Input: edges A->B, B->A
  - Output: deadlock detected

## 7) Dining Philosophers with Staggered Seating

- Slug: dining-philosophers-staggered
- Difficulty: Medium
- Problem: Five philosophers sit around a table, but forks are asymmetric: some forks require two hands (cannot hold another fork simultaneously). Design a protocol to avoid deadlock and starvation when some forks are two-handed and some are normal. Assume philosophers know fork types.
- Constraints: philosophers <= 10^4.
- Example:
  - Input: 5 philosophers, forks: [normal, two-hand, normal, two-hand, normal]
  - Output: protocol with ordering/priorities to avoid deadlock

## 8) Thread Pool with Work Stealing and Task Priorities

- Slug: threadpool-work-stealing-priority
- Difficulty: Medium
- Problem: Design a work-stealing thread pool where each worker has a priority deque (high-priority tasks at front, low-priority at back). Thieves can only steal low-priority tasks from tail. Additionally, some tasks have dependencies (task B can only run after task A completes). Workers must check dependency satisfaction before executing stolen tasks; if dependencies aren't met, task goes back to queue.
- Constraints: tasks up to 10^6, priority levels {1,2,3}, dependency edges up to 10^6.
- Example:
  - Input: tasks with mixed priorities and dependencies [A→B, C→D]
  - Output: balanced completion times respecting priorities and dependencies; high-priority tasks never stolen

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

## 14) Bounded Retry with Exponential Backoff and Failure Classification

- Slug: bounded-retry-backoff-classification
- Difficulty: Medium
- Problem: Implement retry logic with exponential backoff capped at max delay for transient failures. Add jitter (randomization ±25% of delay) to prevent thundering herd. Additionally, failures are classified as: TRANSIENT (retry with backoff), RATE_LIMIT (retry with 2x normal backoff), PERMANENT (abort immediately). Track retry count and total elapsed time; abort if either exceeds threshold.
- Constraints: max retries <= 10, max total time <= 60s, base delay 10ms, max delay 5s.
- Example:
  - Input: operation fails [TRANSIENT, RATE_LIMIT, TRANSIENT] then succeeds
  - Output: retries at ~10ms (±jitter), ~40ms (2x for rate limit, ±jitter), ~20ms (normal backoff, ±jitter), then success

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
