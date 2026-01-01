---
problem_id: GRD_LIBRARY_MERGE_QUEUES__8135
display_id: GRD-010
slug: library-merge-queues
title: "Library Merge Queues"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Heap
  - Merge K Sorted Lists
tags:
  - greedy
  - heap
  - priority-queue
  - merge
  - medium
premium: true
subscription_tier: basic
---

# GRD-010: Library Merge Queues

## 📋 Problem Summary

You have `k` sorted queues of book IDs. You need to merge them into a single sorted stream, but you cannot output the same book ID more than twice in a row. If the smallest available ID violates this rule, you must skip it and pick the next smallest valid ID.

## 🌍 Real-World Scenario

**Scenario Title:** Playlist Generation

Imagine you are building a "Party Mix" playlist from several genre-specific playlists (Pop, Rock, Jazz), which are already sorted by popularity (most popular first).
You want to play the most popular songs first to keep the energy high. However, to avoid monotony, you have a rule: **No more than 2 songs from the same artist in a row.** (Assuming Book IDs = Artist IDs).

If the top song in Pop and the top song in Rock are both by "The Beatles", and you just played two Beatles songs, you have to skip them for a moment and play the next best song by a different artist (e.g., "Queen") before returning to the Beatles.

**Why This Problem Matters:**

- **Fairness/Variety:** In recommendation systems, interleaving content sources while preventing domination by one type.
- **Resource Scheduling:** merging task queues where no single user can hog the CPU for more than 2 consecutive time slices.

![Real-World Application](../images/GRD-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Constraint

Queues:
Q1: [1, 1, 1]
Q2: [1, 2]
Q3: [2]

Output Stream: `[ ]`

1. Min is 1 (from Q1). Output: `[1]`. Last: 1. Count: 1.
2. Min is 1 (from Q1). Output: `[1, 1]`. Last: 1. Count: 2.
3. Min is 1 (from Q1). **Violation!** (Count would be 3).
   - Look for next best valid option.
   - Next best is 2 (from Q2 or Q3).
   - Pick 2. Output: `[1, 1, 2]`. Last: 2. Count: 1.
4. Now we can pick 1 again. Output: `[1, 1, 2, 1]`.

```text
Heap: {(1, Q1), (1, Q2), (2, Q3)}
Top: 1. Valid? Yes. -> Output 1.
Heap: {(1, Q1), (1, Q2), (2, Q3)}
Top: 1. Valid? Yes. -> Output 1.
Heap: {(1, Q1), (1, Q2), (2, Q3)}
Top: 1. Valid? No (1==1 and count==2).
   -> Pop 1, save it.
   -> Pop next: 2. Valid? Yes. -> Output 2.
   -> Push saved 1 back.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sorted Input:** All individual queues are sorted. This allows us to use the "Merge K Sorted Lists" approach.
- **Constraint:** "Consecutive" means immediately adjacent in the output list.
- **Tie-breaking:** If multiple queues have the same value, any one can be picked.
- **Exhaustion:** If we only have invalid values left (e.g., only 1s remain and we just outputted two 1s), we stop? Or is it guaranteed possible? The problem doesn't state it's guaranteed. But usually, in such merge problems, we output as much as possible. If we are blocked, we stop.

## Naive Approach

### Intuition

At each step, scan the front of all `k` queues. Find the smallest value that is valid (doesn't violate the 2-consecutive rule).

### Algorithm

1. Loop until all queues empty.
2. In each iteration, iterate `i` from 0 to `k-1`.
3. Find min value among heads of queues that is != last_val OR count < 2.
4. If found, remove from queue and append to result.
5. If not found (deadlock), break.

### Time Complexity

- **O(N * k)**: For each of N elements, we scan k queues.
- With `N=2 * 10^5` and `k=100`, `2 * 10^7` operations. This might pass but is slow.

## Optimal Approach

### Key Insight

We can optimize the search for the minimum using a **Min-Heap**.
Standard "Merge K Sorted Lists" uses a heap to store `{value, queue_index}`.
Here, we just need to handle the "blocked" case.
If the top of the heap is "blocked" (same as last 2 outputs), we need the *next* smallest value.
We can pop the top, store it temporarily, pop the next one, use it, and then push the first one back.

### Algorithm

1. Initialize Min-Heap with the head of each queue: `(value, queue_index)`.
2. Track `last_val` and `consecutive_count`.
3. While heap is not empty:
   - Pop `(val, q_idx)`.
   - Check validity:
     - If `val == last_val` AND `consecutive_count == 2`:
       - This value is blocked.
       - If heap is empty (no other options), we are done (deadlock).
       - Else, pop next best `(val2, q_idx2)`.
       - Append `val2` to result. Update `last_val`, `consecutive_count`.
       - Advance `q_idx2` (push next element from that queue).
       - **Push back** the blocked `(val, q_idx)` into heap.
     - Else (Valid):
       - Append `val` to result. Update `last_val`, `consecutive_count`.
       - Advance `q_idx`.

### Time Complexity

- **O(N log k)**: Each element is pushed/popped at most twice (once normally, once if blocked).

### Space Complexity

- **O(k)**: Heap size.

### Why This Is Optimal

We efficiently retrieve the smallest available valid number. The heap structure minimizes the cost of finding the minimum to `O(log k)`.

![Algorithm Visualization](../images/GRD-010/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
3 1 1 1
2 1 2
1 2
```
Queues: `Q0:[1,1,1]`, `Q1:[1,2]`, `Q2:[2]`

**Step 1:** Heap `{(1,0), (1,1), (2,2)}`.
- Pop `(1,0)`. Valid. Result `[1]`. Last=1, Cnt=1. Push `(1,0)` (next from Q0).
- Heap `{(1,0), (1,1), (2,2)}`.

**Step 2:**
- Pop `(1,0)`. Valid. Result `[1, 1]`. Last=1, Cnt=2. Push `(1,0)` (next from Q0).
- Heap `{(1,0), (1,1), (2,2)}`.

**Step 3:**
- Pop `(1,0)`. Blocked (1==1, Cnt=2).
- Pop `(1,1)`. Blocked.
- Pop `(2,2)`. Valid! Result `[1, 1, 2]`. Last=2, Cnt=1.
- Push back `(1,0)`, `(1,1)`. Q2 empty.
- Heap `{(1,0), (1,1)}`.

**Step 4:**
- Pop `(1,0)`. Valid. Result `[1, 1, 2, 1]`. Last=1, Cnt=1.
- Push empty (Q0 done).
- Heap `{(1,1)}`.

**Step 5:**
- Pop `(1,1)`. Valid. Result `[1, 1, 2, 1, 1]`. Last=1, Cnt=2.
- Push `(2,1)` (next from Q1).
- Heap `{(2,1)}`.

**Step 6:**
- Pop `(2,1)`. Valid. Result `[1, 1, 2, 1, 1, 2]`.
- Done.

Example output in problem description: `1 1 1 2 2`.
"If a book ID would appear for the third time in a row, skip it..."
Ah, the example output in the problem file is `1 1 1 2 2`?
Line 66: `1 1 1 2 2`
Line 81: "3. Cannot take another 1... Take 2 from queue 1 -> output: [1, 1, 2]"
Line 82: "4. Take 1 from queue 0 -> output: [1, 1, 2, 1]"
Line 83: "5. Take 2 from queue 2 -> output: [1, 1, 2, 1, 2]"
The explanation says `1 1 2 1 2`.
The Output block says `1 1 1 2 2`.
This is a contradiction in the problem file.
Given the constraint "no book ID can appear more than twice consecutively", `1 1 1` is clearly invalid.
The explanation is correct (`1 1 2 1 2`). The Output block is wrong.
We follow the explanation logic in the editorial.

## ✅ Proof of Correctness

### Invariant
At each step, we append the smallest available number that does not violate the constraint.
This greedy strategy ensures that we output smaller numbers as early as possible (lexicographically smallest valid stream).
By temporarily skipping blocked values, we resolve local conflicts with minimal disruption to the sorted order.

## 💡 Interview Extensions

- **Extension 1:** What if the constraint is "no more than K consecutive"?
  - *Answer:* Generalize `count == 2` to `count == K`.
- **Extension 2:** What if we need to merge `k` unsorted lists?
  - *Answer:* Sort them first (`O(N log N)`), then merge.
- **Extension 3:** What if we can't skip, but must buffer?
  - *Answer:* Same logic, just different perspective.

### Common Mistakes to Avoid

1. **Infinite Loop**
   - ❌ Wrong: Popping a blocked value and pushing it back immediately without checking for deadlock.
   - ✅ Correct: If all values in heap are blocked, break loop.

2. **Heap Order**
   - ❌ Wrong: Assuming the second item in heap is different.
   - ✅ Correct: You might need to pop multiple items until you find a different value.

3. **Updating Count**
   - ❌ Wrong: Resetting count to 0.
   - ✅ Correct: Reset to 1 (since we just added one instance of the new value).

## Related Concepts

- **Merge K Sorted Lists:** The base pattern.
- **Heap:** Efficient selection.
