---
problem_id: LNK_HOSTEL_NUMBER_REMOVE_MTH__4285
display_id: LNK-012
slug: hostel-number-remove-mth
title: "Hostel Number Remove Mth from Start"
difficulty: Medium
difficulty_score: 44
topics:
  - Linked List
  - Deletion
  - Single Pass
tags:
  - linked-list
  - deletion
  - single-pass
  - medium
premium: true
subscription_tier: basic
---

# LNK-012: Hostel Number Remove Mth from Start

## 📋 Problem Summary

You are given a linked list representing a sequence of items. You need to remove the **M-th** node from the beginning (1-based index).
- If `M=1`, remove the head.
- If `M` is greater than the list length, do nothing.
- Return the head of the modified list.

## 🌍 Real-World Scenario

**Scenario Title:** The Hostel Room Renovation

A hostel has a long corridor with rooms numbered sequentially. The management decides to convert one specific room into a utility closet.
- "Remove the 3rd room from the list of available rooms."
- The corridor structure (linked list) remains, but the pointer from Room 2 now skips Room 3 and points directly to Room 4.

**Why This Problem Matters:**

- **Task Cancellation:** Removing the M-th task from a processing queue.
- **Playlist Management:** "Remove the 5th song from the queue."
- **Data Cleaning:** Dropping a specific record (e.g., the header or a corrupted row) from a stream.

![Real-World Application](../images/LNK-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Deletion

List: `9 -> 8 -> 7 -> 6`
`M = 2` (Remove 2nd node, value 8)

1. **Start:** Dummy -> 9 -> 8 -> 7 -> 6
2. **Move to M-1:** Move 1 step. Pointer at 9.
3. **Relink:** `9.next = 9.next.next` (Skip 8).
   `9 -> 7`
4. **Result:** `9 -> 7 -> 6`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **1-based Indexing:** `M=1` means the first node.
- **Out of Bounds:** If `M > length`, return original list.
- **Edge Case:** `M=1` requires updating the head.

Common interpretation mistake:

- ❌ **Wrong:** Confusing "M-th from start" with "M-th from end" 
- ✅ **Correct:** This is simpler. Count from the start.

### Core Concept: Dummy Node

Using a `dummy` node pointing to `head` allows us to handle `M=1` (removing head) using the exact same logic as removing any other node. We stop at the `(M-1)`-th node relative to the dummy.

## Naive Approach

### Intuition

Handle `M=1` separately. Then loop `M-2` times to find the predecessor.

### Algorithm

1. If `M=1`, return `head.next`.
2. `prev = head`.
3. Loop `M-2` times: `prev = prev.next`.
4. If `prev` or `prev.next` is null, return head (out of bounds).
5. `prev.next = prev.next.next`.

### Time Complexity

- **O(M)**.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Use a dummy node to unify logic. The predecessor of the M-th node is the (M-1)-th node. If we start at dummy (index 0), we move `M-1` steps to get to the predecessor.

### Algorithm

1. Create `dummy` node, `dummy.next = head`.
2. `curr = dummy`.
3. Loop `M-1` times:
   - `curr = curr.next`
   - If `curr` becomes null, `M` is out of bounds. Return `dummy.next`.
4. Check if `curr.next` exists (the node to remove).
   - If yes, `curr.next = curr.next.next`.
5. Return `dummy.next`.

### Time Complexity

- **O(M)**. We only traverse up to the removal point.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-012/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-012/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `9 8 7 6`, `M=2`

**Initialization:**
- `dummy -> 9 -> 8 -> 7 -> 6`
- `curr = dummy`.

**Loop (M-1 = 1 time):**
- `curr` moves to `dummy.next` (Node 9).

**Removal:**
- `curr` is at 9. `curr.next` is 8.
- `curr.next = curr.next.next` (8's next is 7).
- Link becomes `9 -> 7`.

**Result:** `9 -> 7 -> 6`.

![Example Visualization](../images/LNK-012/example-1.png)

## ✅ Proof of Correctness

### Invariant
The loop correctly positions `curr` at the node immediately preceding the target node to be removed.

### Why the approach is correct
- **Dummy Node:** Handles the case where the head itself needs to be removed (predecessor is dummy).
- **Bounds Check:** If loop completes and `curr` or `curr.next` is null, we safely do nothing.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Remove M-th from End.
  - *Hint:* Two pointers (fast/slow) with gap M.
- **Extension 2:** Remove node given only access to that node (no head).
  - *Hint:* Copy value from next node, delete next node. (Cannot delete tail).
- **Extension 3:** Remove all occurrences of value V.
  - *Hint:* Loop through entire list.

### Common Mistakes to Avoid

1. **Null Pointer Exception**
   - ❌ Wrong: `curr.next.next` without checking `curr.next`.
   - ✅ Correct: Always check existence before dereferencing.

2. **Off-by-one**
   - ❌ Wrong: Looping `M` times lands you ON the node to delete (cannot delete without prev).
   - ✅ Correct: Loop `M-1` times to land on PREV.

## Related Concepts

- **Dummy Head:** Essential for simplifying head operations.
- **Pointer Manipulation:** The core of linked lists.
