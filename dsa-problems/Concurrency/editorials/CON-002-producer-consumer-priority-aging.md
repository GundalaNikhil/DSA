---
problem_id: CON_PRIO_QUEUE_AGING__C4B7
display_id: CON-002
slug: producer-consumer-priority-aging
title: "Producer-Consumer with Priority and Aging"
difficulty: Medium
difficulty_score: 55
topics:
  - Concurrency
  - Condition Variables
  - Producer Consumer
  - Priority Queue
tags:
  - concurrency
  - producer-consumer
  - condition-variables
  - priority-queue
  - medium
premium: true
subscription_tier: basic
---

# Producer-Consumer with Priority and Aging

## Problem summary

You need a bounded buffer that is:

- thread-safe with multiple producers and consumers
- blocks producers when full and consumers when empty
- dequeues the highest-priority element
- prevents starvation via “aging” (waiting increases priority)
- avoids lost wakeups (correct condition-variable usage)

This is basically the classic bounded-buffer problem, except:

1) the buffer is a priority queue
2) the priority is time-dependent (aging)

## Real-world scenario (how to explain it to BTech / interview audiences)

Imagine a campus “IT helpdesk” queue:

- Students raise tickets with severity (priority).
- During exam week, high-severity tickets dominate.
- But you still must not starve low-severity tickets forever.

Aging is the policy that says: “if a ticket waits long enough, its priority increases so it eventually gets served.”

### C++ore concurrency invariant

All shared state must be protected by one mutex (or monitor lock), and every condition variable wait must:

- check a predicate in a loop
- release the mutex while sleeping
- re-acquire the mutex before proceeding

If you cannot state the predicate precisely, your design will be buggy.

## Data model (what to store per item)

For each item you need:

- `basePriority` (given by producer)
- `enqueueTime` (monotonic time, not wall clock)
- `id` or sequence number (for stable tie-breaking)
- the payload

Define effective priority at time `now`:

`effective = basePriority + floor((now - enqueueTime) / T)`

This definition is deterministic, monotonic, and prevents starvation provided items remain in the queue.

## The “hard” part: aging without O(n) rescans

If you recompute effective priority for all items on every `take()`, you will not scale to `10^6`.

Two realistic design options:

### Option A: Recompute only at pop time (lazy aging) with re-heapify loop

Use a max-heap ordered by a key you can update:

1) At `take()`, peek the heap top.
2) Compute its current effective priority using `now`.
3) If its key is stale (it should be higher now), update it and push it back / sift down/up, then check again.
4) Repeat until the heap top is stable (no other element should outrank it).

This can work, but worst-case behavior can degrade if many items become stale at once.

### Option B: Bucketed aging (practical and scalable)

If priorities are bounded or you can bucket them:

- Keep multiple FIFO queues (buckets) per priority level
- Track time and “promote” items when they cross aging thresholds

This is closer to OS schedulers (multi-level feedback queues). It can be more complex, but avoids heap churn.

In interviews, it is enough to propose Option A with a clear argument about amortization and correctness, as long as you acknowledge performance risks and propose bucketization as an optimization.

## Synchronization protocol (avoid lost wakeups)

Shared state:

- `size` (0..capacity)
- the priority structure (heap/buckets)
- `mutex`
- `notEmpty` condition variable
- `notFull` condition variable

Predicates:

- Producer may proceed when: `size < capacity`
- Consumer may proceed when: `size > 0`

Pseudocode (monitor style):

`put(x)`:

- lock mutex
- while `size == capacity`: wait(notFull, mutex)
- insert item with `enqueueTime = now()`
- size++
- signal(notEmpty) (or broadcast if many consumers)
- unlock mutex

`take()`:

- lock mutex
- while `size == 0`: wait(notEmpty, mutex)
- remove highest effective-priority item (with aging policy)
- size--
- signal(notFull)
- unlock mutex
- return item

Key correctness point: signals happen while holding the lock, after changing the state, so waiters cannot miss the update.

## Starvation prevention argument

With effective priority defined as:

`base + floor((waitTime)/T)`

An item’s effective priority grows without bound as time passes. That means:

- For any fixed set of other items with bounded base priority, there exists a time after which the waiting item’s effective priority exceeds theirs.

So starvation is prevented as long as:

- the system continues to dequeue items
- time moves forward (monotonic clock)

If new higher-priority items arrive forever, aging ensures older items eventually catch up, unless base priorities are unbounded and arrivals are adversarial. In practice, you should state any assumptions (e.g., base priorities in a finite range).

## Edge cases students must mention

- Use monotonic time (avoid wall clock jumps).
- Decide tie-break rules: if effective priorities are equal, pick oldest to maintain fairness.
- Decide what happens when producers block: enqueue time should be when the item is actually inserted, not when `put()` was called.
- Avoid priority explosion: consider capping effective priority or using buckets.

### C++omplexity

- Locking: O(1) per operation for the monitor overhead.
- Data structure:
  - heap: insert O(log n), remove O(log n), plus possible extra adjustments due to lazy aging
  - buckets: near O(1) average if priority range and promotion are handled efficiently

## What a “strong” interview answer looks like

- Precise invariants: size bounds, predicates for waits.
- Correct condvar usage (while loop).
- Clear aging rule and fairness reasoning.
- Performance awareness: why naive rescanning is bad and what to do instead.

