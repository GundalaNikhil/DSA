---
problem_id: QUE_EVENT_REGISTRATION_MERGE__6205
display_id: QUE-011
slug: event-registration-merge
title: "Event Registration Merge"
difficulty: Easy
difficulty_score: 22
topics:
  - Queue
  - Merge
  - Two Pointers
tags:
  - queue
  - merge
  - two-pointers
  - easy
premium: true
subscription_tier: basic
---

# QUE-011: Event Registration Merge

## 📋 Problem Summary

We are given two sorted queues of registration IDs. We need to merge them into a single sorted queue.
- Input: Two arrays `A` and `B`, both sorted in ascending order.
- Output: One array `C` containing all elements from `A` and `B`, sorted.

## 🌍 Real-World Scenario

**Scenario Title:** Merging Traffic Lanes

Imagine two lanes of highway traffic merging into one.
- Lane A has cars with speeds `[60, 65, 70]`.
- Lane B has cars with speeds `[55, 62, 80]`.
- To maintain a safe flow where slower cars are ahead of faster cars, we pick the "smallest" value from the front of either lane.
- The merge order: 55, 60, 62, 65, 70, 80.
- This is the fundamental "Merge" step in **Merge Sort**.

**Why This Problem Matters:**

- **Database Join:** Merging sorted files (External Merge Sort).
- **Log Aggregation:** Combining timestamped logs from multiple servers.

![Real-World Application](../images/QUE-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Merge Process

Queue A: `[3, 5, 9]`
Queue B: `[1, 4, 10]`

1. Compare heads: `3` vs `1`.
   - `1` is smaller. Output `1`.
   - A: `[3, 5, 9]`, B: `[4, 10]`.

2. Compare heads: `3` vs `4`.
   - `3` is smaller. Output `3`.
   - A: `[5, 9]`, B: `[4, 10]`.

3. Compare heads: `5` vs `4`.
   - `4` is smaller. Output `4`.
   - A: `[5, 9]`, B: `[10]`.

4. Compare heads: `5` vs `10`.
   - `5` is smaller. Output `5`.
   - A: `[9]`, B: `[10]`.

5. Compare heads: `9` vs `10`.
   - `9` is smaller. Output `9`.
   - A: `[]`, B: `[10]`.

6. A is empty. Output remaining B: `10`.

Result: `1, 3, 4, 5, 9, 10`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Two sorted arrays.
- **Output:** One sorted array.
- **Equality:** If values are equal, order doesn't strictly matter for correctness of sorting, but usually we pick from the first queue for stability.

## Naive Approach

### Intuition

Concatenate both arrays and sort the result.

### Algorithm

1. `C = A + B`.
2. `C.sort()`.

### Limitations

- **Time Complexity:** `O((N+M) log (N+M))`.
- **Space Complexity:** `O(N+M)`.
- While acceptable for small inputs, it ignores the fact that inputs are *already sorted*.

## Optimal Approach

### Key Insight

Use the **Two Pointers** technique (or simply compare the front of two queues). Since both inputs are sorted, the next smallest element is always at the head of one of the queues.

### Algorithm

1. Initialize pointers `i = 0` (for A) and `j = 0` (for B).
2. Create result array `res`.
3. While `i < N` and `j < M`:
   - If `A[i] <= B[j]`: Add `A[i]` to `res`, increment `i`.
   - Else: Add `B[j]` to `res`, increment `j`.
4. While `i < N`: Add `A[i]` to `res`, increment `i`.
5. While `j < M`: Add `B[j]` to `res`, increment `j`.

### Time Complexity

- **O(N + M)**. We visit each element exactly once.

### Space Complexity

- **O(N + M)** for the result.

![Algorithm Visualization](../images/QUE-011/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-011/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `3 5 9` and `1 4 10`.
1. `3` vs `1`. Pick `1`. Res: `[1]`.
2. `3` vs `4`. Pick `3`. Res: `[1, 3]`.
3. `5` vs `4`. Pick `4`. Res: `[1, 3, 4]`.
4. `5` vs `10`. Pick `5`. Res: `[1, 3, 4, 5]`.
5. `9` vs `10`. Pick `9`. Res: `[1, 3, 4, 5, 9]`.
6. A empty. Append `10`. Res: `[1, 3, 4, 5, 9, 10]`.

## ✅ Proof of Correctness

### Invariant
At any step, the smallest remaining element in the union of A and B must be at the head of A or the head of B (because both are sorted). By picking the smaller of the two heads, we guarantee we pick the global minimum of the remaining elements.

### Why the approach is correct
This is the standard proof for the merge step in Merge Sort.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Merge K sorted queues?
  - *Hint:* Use a Min-Heap of size K. Insert heads of all K queues. Pop min, insert next from that queue. `O(N log K)`.
- **Extension 2:** Merge in-place (if A has extra space)?
  - *Hint:* Start from the back (largest elements) to avoid overwriting.

### Common Mistakes to Avoid

1. **Index Out of Bounds**
   - ❌ Wrong: Accessing `a[i]` when `i == n`.
   - ✅ Correct: Check `i < n` in loop condition.
2. **Forgetting Remainders**
   - ❌ Wrong: Loop ends when one queue is empty, forgetting the other.
   - ✅ Correct: Add `while` loops to flush remaining elements.

## Related Concepts

- **Merge Sort:** Uses this exact logic.
- **External Sort:** Merging sorted chunks from disk.
