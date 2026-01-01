---
problem_id: ARR_ZERO_SLIDE_LIMIT__4908
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Easy-Medium
difficulty_score: 34
topics:
  - Arrays
  - Two Pointers
  - Simulation
tags:
  - arrays
  - two-pointers
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
---

# ARR-006: Zero Slide With Limit

## 📋 Problem Summary

Move all zeros to the end of the array (or equivalently, move all non-zeros to the front) while maintaining the relative order of non-zero elements. You must stop if you reach the limit of `m` swaps.

## 🌍 Real-World Scenario

**Scenario Title:** The Library Shelf Organizer

You are a librarian organizing a shelf. "Zeros" represent empty gaps between books. "Non-zeros" are the books.
You want to push all books to the left to close the gaps and make space at the end.
However, moving a book takes effort. You only have enough energy for `m` "moves" (swaps).

- You scan from left to right.
- Whenever you see a book that has gaps to its left, you move it to the leftmost available gap.
- If you run out of energy (`m` moves), you stop working immediately, leaving the rest of the shelf as is.

**Why This Problem Matters:**

- **Garbage Collection**: Compacting memory involves moving "live" objects to one end and leaving "free" space at the other. Budgeting operations is akin to real-time GC limits.
- **Data Stream Processing**: Filtering nulls/invalid packets with limited CPU cycles per frame.
- **Partitions**: A variation of the partition step in QuickSort.

![Real-World Application](../images/ARR-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Books

```
Shelf:   [0]   [4]   [0]   [5]   [7]
          ^     ^
        Gap    Book

Action: Move [4] to Gap [0]. Cost 1 swap.
Result:  [4]   [0]   [0]   [5]   [7]

Energy Limit m=1. STOP.
Final:   [4]   [0]   [0]   [5]   [7]
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Swap Definition**: Swapping `arr[i]` (non-zero) with `arr[j]` (zero) counts as **1** swap, regardless of the distance between `i` and `j`. (It is a direct memory swap, not bubbling).
- **Self-Swaps**: If a non-zero element is already in the correct position (no zeros to its left), it stays there. This costs 0 swaps.
- **Order**: Relative order of non-zeros must be preserved.

Common interpretation mistake:

- ❌ "Bubbling" the non-zeros (swapping adjacent elements). This is O(N²) and counts differently.
- ✅ Direct swap to the `write` pointer. This is O(N).

### Core Concept: Two Pointers (Read/Write)

We maintain two pointers:

1. `write_idx`: The position where the next non-zero element SHOULD go.
2. `read_idx`: The current element we are inspecting.

### Why Naive Approach is too slow

A "Bubble push" strategy where we swap zeros repeatedly with right-neighbors is O(N²). For N=200,000, this times out. We need a linear pass.

## Naive Approach

### Intuition

Iterate through array. If `arr[i] == 0` and `arr[i+1] != 0`, swap them. Repeat until no zeros are left of non-zeros or limit reached.

### Algorithm

1. Repeat loop:
   - Scan whole array.
   - Swap adjacent `0, non-zero` pair.
   - Decrement `m`.
2. Stop if sorted or `m=0`.

### Time Complexity

- **O(N²)**: Worst case (all zeros at start, all numbers at end).

### Space Complexity

- **O(1)**.

## Optimal Approach (Writer Pointer)

### Key Insight

We don't need to bubble. We know exactly where the next non-zero goes: the first available '0' (or the current position if no zeros passed yet).
`write_idx` tracks the boundary of the "compacted" prefix.

### Algorithm

1. Initialize `write_idx = 0`.
2. Iterate `read_idx` from 0 to `n-1`.
3. If `arr[read_idx]` is non-zero:
   - Check if we need to move it (`read_idx > write_idx`).
   - If yes:
     - Check if `m > 0`.
     - If `m == 0`, break (cannot perform needed swap).
     - Swap `arr[read_idx]` and `arr[write_idx]`.
     - Decrement `m`.
   - Increment `write_idx` (slot filled).
4. Return modified `arr`.

### Time Complexity

- **O(N)**: Single pass.

### Space Complexity

- **O(1)**: In-place.

### Why This Is Optimal

We traverse the array once. Each element is written at most once.

![Algorithm Visualization](../images/ARR-006/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-006/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `arr=[0, 4, 0, 5, 7]`, `m=1`

1. **Init**: `write=0`, `read=0`.

   - `arr[0]` is 0. Skip.

2. **Read=1**: `arr[1]` is 4.

   - `read(1) != write(0)`.
   - `m(1) > 0`. Swap `arr[0], arr[1]`.
   - Arr: `[4, 0, 0, 5, 7]`.
   - `m` becomes 0.
   - `write` becomes 1.

3. **Read=2**: `arr[2]` is 0. Skip.

4. **Read=3**: `arr[3]` is 5.
   - `read(3) != write(1)`.
   - `m(0) <= 0`. **BREAK**.

**Output**: `[4, 0, 0, 5, 7]`. Matches Example.

![Example Visualization](../images/ARR-006/example-1.png)

## ✅ Proof of Correctness

### Invariant

`arr[0...writeIdx-1]` contains the compacted non-zero elements encountered so far in relative order. `m` is decremented exactly when a non-zero is moved into a gap (where `gap` is defined by `writeIdx` effectively pointing to a zero or a position that _was_ a zero before a swap).

### Why the approach is correct

The algorithm greedily moves the leftmost available non-zeros to the leftmost available zero-slots. This compaction order is unique and maintains stability. The limit `m` strictly bounds the number of write operations that cross a gap.

## 💡 Interview Extensions (High-Value Add-ons)

- **Snowball Method**: (The one explained here).
- **Minimum Swaps**: What if we want to minimize writes? (A: This greedy approach already minimizes moves for a stable sort with 0).
- **Large M**: If `m >= n`, this becomes the standard Move Zeroes problem.

## Common Mistakes to Avoid

1. **Swapping 0 with 0**:

   - ❌ Swapping when `arr[read] == 0`.
   - ✅ Only act when `arr[read] != 0`.

2. **Counting Self-Swaps**:

   - ❌ Decrementing `m` when `read == write`.
   - ✅ If `read == write`, the element is already in place. No "move" occurred. `m` stays same.

3. **Continuing after M=0**:
   - ❌ Forgetting to break.
   - ✅ Stop immediately.

## Related Concepts

- **Stable Partition**: Separating array into two groups while keeping order.
- **Two Pointers**: Standard Read/Write pattern.
