---
problem_id: LNK_HOSTEL_CLEANUP_DEDUPLICATE_TWO__6294
display_id: LNK-004
slug: hostel-cleanup-deduplicate-two
title: "Hostel Cleanup Deduplicate (At Most Two)"
difficulty: Medium
difficulty_score: 45
topics:
  - Linked List
  - Two Pointers
  - Deduplication
tags:
  - linked-list
  - duplicates
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# LNK-004: Hostel Cleanup Deduplicate (At Most Two)

## 📋 Problem Summary

You are given a **sorted** singly linked list. Your task is to remove duplicate nodes such that each distinct value appears **at most twice**. The relative order of the remaining nodes must be preserved.

## 🌍 Real-World Scenario

**Scenario Title:** The Hostel Room Allocation

You are the warden of a university hostel. Students have signed up for rooms based on their preferred floor plan (represented by the node value). However, due to a glitch in the registration system, some floor plans were overbooked.

Each floor plan type can accommodate at most **two** students. If 5 students signed up for "Type 1" rooms, you can keep the first two, but you must cancel the bookings for the other three. You need to go through the list of bookings and remove the excess ones while keeping the valid ones in order.

**Why This Problem Matters:**

- **Data Cleaning:** Removing excessive redundancy while preserving some history (e.g., keeping the last 2 backups).
- **Rate Limiting:** Allowing a user to perform an action (like login attempts) a limited number of times before blocking subsequent attempts.
- **Inventory Control:** Ensuring that no more than `N` units of a specific SKU are in a particular batch.

![Real-World Application](../images/LNK-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Deduplication Logic

We traverse the list. Since it's sorted, all duplicates are grouped together. We just need to count how many times we've seen the current value.

```
Initial List: 1 -> 1 -> 1 -> 2 -> 2 -> 3

Step 1: Node(1). Count = 1. Keep.
Step 2: Node(1). Value == Prev. Count = 2. Keep.
Step 3: Node(1). Value == Prev. Count = 3. DELETE.
   List becomes: 1 -> 1 -> 2 -> 2 -> 3
Step 4: Node(2). Value != Prev (last kept). Reset Count = 1. Keep.
Step 5: Node(2). Value == Prev. Count = 2. Keep.
Step 6: Node(3). Value != Prev. Reset Count = 1. Keep.

Final List: 1 -> 1 -> 2 -> 2 -> 3
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sorted Input:** The list is guaranteed to be sorted non-decreasingly. This is crucial because it means duplicates are adjacent.
- **At Most Two:** If a value appears once, keep it. If twice, keep both. If 3+ times, keep first two.
- **In-Place:** Ideally, you should modify the existing list pointers rather than creating a new list.

Common interpretation mistake:

- ❌ **Wrong:** Removing *all* nodes that have duplicates (leaving only unique numbers).
- ✅ **Correct:** Keeping up to two instances of each number.

### Core Concept: Predecessor Pointer

To delete a node `current`, we need access to the node *before* it (`prev`). We set `prev.next = current.next` to bypass `current`.

## Naive Approach

### Intuition

Create a new list. Iterate through the original list. If the value is different from the last added value in the new list, add it and reset counter. If it's the same, increment counter. If counter <= 2, add it.

### Algorithm

1. Create `newListHead` and `newListTail`.
2. Iterate `current` through original list.
3. Maintain `lastVal` and `count`.
4. If `current.val != lastVal`:
   - Append `current` to new list.
   - `lastVal = current.val`, `count = 1`.
5. Else (`current.val == lastVal`):
   - `count++`.
   - If `count <= 2`, append `current` to new list.
6. Return `newListHead`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** if we create new nodes, or **O(1)** if we just relink existing nodes (which is the goal).

## Optimal Approach

### Key Insight

We can do this in one pass using pointers `prev` (last valid node) and `current` (node being inspected).

### Algorithm

1. Handle edge case: if list has fewer than 3 nodes, return it as is.
2. Initialize `prev` to `head` and `current` to `head.next`.
3. Initialize `count = 1` (since we started with one node).
4. Loop while `current` is not `null`:
   - If `current.val == prev.val`:
     - Increment `count`.
     - If `count > 2`:
       - **Delete:** `prev.next = current.next`.
       - `current` becomes `prev.next` (the next node to check).
       - (Do not move `prev` because we haven't validated the new `current` yet).
     - Else (count <= 2):
       - **Keep:** `prev = current`.
       - `current = current.next`.
   - Else (`current.val != prev.val`):
     - Reset `count = 1`.
     - **Keep:** `prev = current`.
     - `current = current.next`.
5. Return `head`.

### Time Complexity

- **O(N)**. We visit each node once.

### Space Complexity

- **O(1)**. We modify the list in place.

![Algorithm Visualization](../images/LNK-004/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-004/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 1 1 2 2 3`

**Initialization:**
- `prev` = Node(1) [1st]
- `current` = Node(1) [2nd]
- `count` = 1

**Iteration 1:**
- `current.val` (1) == `prev.val` (1).
- `count` becomes 2.
- `count <= 2`. Keep.
- `prev` moves to Node(1) [2nd].
- `current` moves to Node(1) [3rd].

**Iteration 2:**
- `current.val` (1) == `prev.val` (1).
- `count` becomes 3.
- `count > 2`. **Remove.**
- `prev.next` set to `current.next` (Node(2)).
- `current` moves to Node(2).
- List state: `1 -> 1 -> 2 -> 2 -> 3`

**Iteration 3:**
- `current.val` (2) != `prev.val` (1).
- `count` reset to 1.
- `prev` moves to Node(2) [1st].
- `current` moves to Node(2) [2nd].

**Iteration 4:**
- `current.val` (2) == `prev.val` (2).
- `count` becomes 2.
- `count <= 2`. Keep.
- `prev` moves to Node(2) [2nd].
- `current` moves to Node(3).

**Iteration 5:**
- `current.val` (3) != `prev.val` (2).
- `count` reset to 1.
- `prev` moves to Node(3).
- `current` moves to `null`.

**End:** Return head.

![Example Visualization](../images/LNK-004/example-1.png)

## ✅ Proof of Correctness

### Invariant
At any step, the sublist from `head` to `prev` contains a valid sequence where no element appears more than twice. `current` is the next candidate to be appended to this valid sequence.

### Why the approach is correct
- We only advance `prev` when we accept a node.
- If we reject a node (count > 2), we skip it by linking `prev` to `current.next`, effectively removing it from the chain.
- Since the list is sorted, checking `current.val == prev.val` is sufficient to detect duplicates.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Generalize to "At most K duplicates".
  - *Hint:* Just change `if (count > 2)` to `if (count > K)`.
- **Extension 2:** Remove *all* nodes that have duplicates (leave only unique numbers).
  - *Hint:* This requires a `dummy` head because the real head might be removed. You need to look ahead to see if duplicates exist.
- **Extension 3:** Unsorted list.
  - *Hint:* You need a Hash Set to track counts. O(N) time, O(N) space.

### Common Mistakes to Avoid

1. **Advancing Prev too early**
   - ❌ Wrong: Always moving `prev = prev.next` inside the loop.
   - ✅ Correct: Only move `prev` when you *keep* a node. If you delete, `prev` stays put to link to the next potential node.

2. **Memory Leaks (C++)**
   - ❌ Wrong: Just changing pointers.
   - ✅ Correct: In C++, you should `delete` the skipped node to free memory.

3. **Empty List**
   - ❌ Wrong: Accessing `head.next` without checking `head`.
   - ✅ Correct: Handle `head == null` at the start.

## Related Concepts

- **Two Pointers:** One for the end of the valid list (`prev`), one for scanning (`current`).
- **In-place Modification:** Modifying the structure without extra space.
