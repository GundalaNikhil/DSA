---
problem_id: HEP_MERGE_K_STREAMS_RATE_LIMIT__9034
display_id: HEP-002
slug: merge-k-streams-rate-limit
title: "Merge K Streams with Rate Limit"
difficulty: Medium
difficulty_score: 52
topics:
  - Heaps
  - K-Way Merge
  - Streaming
tags:
  - heaps
  - k-way-merge
  - rate-limit
  - medium
premium: true
subscription_tier: basic
---

# HEP-002: Merge K Streams with Rate Limit

## 📋 Problem Summary

You have `k` sorted streams of numbers.
You need to merge them into a single sorted sequence, but with a twist:
- In each "round", a stream can contribute at most `r` elements.
- Once a stream hits this limit for the round, it's "blocked" until the next round.
- Within a round, you always pick the smallest available number from unblocked streams.
  - "After a stream has contributed `r` elements in the current round, it is blocked until the next round."
  - "Within a round, always output the smallest available element among the unblocked streams."
  - Implicitly: A round ends when no stream can contribute anymore (all are blocked or empty). Then all non-empty streams unblock, and a new round begins.

## 🌍 Real-World Scenario

**Scenario Title:** Fair Bandwidth Scheduling

Imagine a network router merging packets from `k` different users.
- To prevent one heavy user from hogging the bandwidth, the router enforces a **Quota** (`r`).
- Each user can send up to `r` packets in a cycle.
- The router picks the earliest timestamped packet (smallest value) from users who haven't used up their quota yet.
- Once everyone is capped or done, the quotas reset for the next cycle.

![Real-World Application](../images/HEP-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Round-Robin Merging

Streams:
S1: `[1, 5, 10]`
S2: `[2, 3, 6]`
Limit `r = 1`.

**Round 1:**
- Candidates: S1(1), S2(2). Both unblocked.
- Smallest: 1 (from S1). Output `1`.
- S1 usage: 1/1. **S1 Blocked**.
- Candidates: S2(2).
- Smallest: 2 (from S2). Output `2`.
- S2 usage: 1/1. **S2 Blocked**.
- No candidates left. End Round 1.

**Round 2:** (Reset usage)
- Candidates: S1(5), S2(3).
- Smallest: 3 (from S2). Output `3`.
- S2 usage: 1/1. **S2 Blocked**.
- Candidates: S1(5).
- Smallest: 5 (from S1). Output `5`.
- S1 usage: 1/1. **S1 Blocked**.
- No candidates left. End Round 2.

**Round 3:**
- Candidates: S1(10), S2(6).
- Smallest: 6 (from S2). Output `6`.
- S2 usage: 1/1. **S2 Blocked**.
- Candidates: S1(10).
- Smallest: 10 (from S1). Output `10`.
- S1 usage: 1/1. **S1 Blocked**.

Result: `1, 2, 3, 5, 6, 10`.

### Key Concept: Min-Heap with State Tracking

We use a **Min-Heap** to store the current head of each stream.
- Heap Element: `(value, stream_index)`.
- We also maintain an array `usage[k]` to track how many elements stream `i` has output in the current round.
- **Critical Logic:**
  - When we pop `(val, i)` from heap:
    - Output `val`.
    - Increment `usage[i]`.
    - If `usage[i] < r` and stream `i` has more elements, push next element from stream `i` into heap immediately.
    - If `usage[i] == r`, **do not push** next element yet. Stream `i` is blocked for this round.
  - When heap becomes empty but streams are not exhausted:
    - **End of Round.**
    - Reset `usage` for all streams.
    - Push the next available element from every non-empty stream that was blocked (or just iterate all streams and push their current head if not already in heap).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `k` streams, limit `r`.
- **Output:** Merged list.
- **Constraints:** Total elements `N <= 200,000`. `k <= 10^5`.
- **Edge Case:** Some streams can be empty initially.

## Naive Approach

### Intuition

Simulate rounds. In each round, collect available heads, sort them, pick smallest, update.

### Time Complexity

- **O(N * k)**: If we scan all streams every step.

## Optimal Approach

### Key Insight

Use a **Min-Heap** for active streams and a **List** for blocked streams.
1. Initialize heap with first element of all streams.
2. While heap is not empty:
   - Pop min `(val, idx)`.
   - Add to result.
   - Increment `usage[idx]`.
   - If `usage[idx] < r`:
     - If stream `idx` has more, push next to heap.
   - Else (`usage[idx] == r`):
     - Add `idx` to `blocked_queue`.
   - If heap is empty and `blocked_queue` is not empty:
     - **New Round**:
     - Reset `usage` (conceptually).
     - For every `idx` in `blocked_queue`:
       - If stream `idx` has more, push next to heap.
     - Clear `blocked_queue`.

### Algorithm

1. `minHeap` stores `(value, stream_index)`.
2. `blocked` list stores indices of streams that hit limit `r`.
   - When a stream comes back from `blocked`, its usage is 0.
   - When a stream stays in heap, its usage increments.
   - So, we can store `(value, stream_index, current_round_usage)` in heap? No, usage is per stream.
   - Just `usage[stream_index]` is fine. Reset it when moving from blocked to heap?
   - Yes: When moving `idx` from `blocked` to `heap`, set `usage[idx] = 0`.
   - What about streams that didn't hit limit but round ended?
     - "Round ends when heap is empty". This implies *all* active streams hit limit or ran out.
     - So *every* stream in the next round starts fresh.
     - Correct.

### Time Complexity

- **O(N log k)**.

### Space Complexity

- **O(k)**.

![Algorithm Visualization](../images/HEP-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `k=2, r=1`. S1: `[1, 4]`, S2: `[2, 3, 5]`.

**Init:** Heap: `{(1, S1), (2, S2)}`. Blocked: `[]`.

**Step 1:** Pop `(1, S1)`. Res: `[1]`.
- Usage S1: 1. Limit reached.
- Blocked: `[S1]`. Heap: `{(2, S2)}`.

**Step 2:** Pop `(2, S2)`. Res: `[1, 2]`.
- Usage S2: 1. Limit reached.
- Blocked: `[S1, S2]`. Heap: `{}`.

**Round End:** Heap empty. Blocked `[S1, S2]`.
- Reset usage.
- S1 next: `4`. Push `(4, S1)`.
- S2 next: `3`. Push `(3, S2)`.
- Heap: `{(3, S2), (4, S1)}`. Blocked: `[]`.

**Step 3:** Pop `(3, S2)`. Res: `[1, 2, 3]`.
- Usage S2: 1. Blocked: `[S2]`. Heap: `{(4, S1)}`.

**Step 4:** Pop `(4, S1)`. Res: `[1, 2, 3, 4]`.
- Usage S1: 1. Blocked: `[S2, S1]`. Heap: `{}`.

**Round End:** Heap empty. Blocked `[S2, S1]`.
- S2 next: `5`. Push `(5, S2)`.
- S1 next: None.
- Heap: `{(5, S2)}`.

**Step 5:** Pop `(5, S2)`. Res: `[1, 2, 3, 4, 5]`.
- Usage S2: 1. Blocked: `[S2]`. Heap: `{}`.

**Round End:** Heap empty. Blocked `[S2]`.
- S2 next: None.
- Heap: `{}`. Blocked: `[]`.

**Finish.**

## ✅ Proof of Correctness

### Invariant
- The heap always contains the smallest available element from every *unblocked* stream.
- By picking the min from the heap, we satisfy the "smallest available" condition.
- The blocking mechanism strictly enforces the rate limit `r`.
- The round reset mechanism ensures fairness cycles.

## 💡 Interview Extensions

- **Extension 1:** Weighted Round Robin?
  - *Answer:* Give each stream a different `r_i`.
- **Extension 2:** Infinite Streams?
  - *Answer:* Generator-based approach, yield one by one.

### Common Mistakes to Avoid

1. **Premature Round Reset**
   - ❌ Wrong: Resetting when *any* stream gets blocked.
   - ✅ Correct: Reset only when *all* active streams are blocked (heap empty).
2. **Usage Counter**
   - ❌ Wrong: Forgetting to reset usage counters.
   - ✅ Correct: Reset to 0 at the start of each new round.

## Related Concepts

- **K-Way Merge:** Standard algorithm (Merge Sort).
- **Leaky Bucket:** Rate limiting algorithm.
