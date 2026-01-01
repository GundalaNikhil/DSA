---
problem_id: LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__8156
display_id: LNK-013
slug: shuttle-ticket-rotate-blocks
title: "Shuttle Ticket Rotate by Blocks"
difficulty: Medium
difficulty_score: 46
topics:
  - Linked List
  - Rotation
  - Block Processing
tags:
  - linked-list
  - rotation
  - blocks
  - medium
premium: true
subscription_tier: basic
---

# LNK-013: Shuttle Ticket Rotate by Blocks

## 📋 Problem Summary

You are given a linked list. You need to divide it into consecutive blocks of size `b`. For each block, rotate its nodes to the right by `k` positions.
- If the last block has fewer than `b` nodes, rotate it by `k` relative to its actual size.
- Concatenate the rotated blocks to form the final list.

## 🌍 Real-World Scenario

**Scenario Title:** The Shift Scheduler

A factory has `N` workers standing in a line. They are divided into teams of size `b`. Every week, the manager rotates the roles within each team by `k` positions to ensure everyone learns every job.
- Team 1: Workers 1-3. Rotate by 1 -> Worker 3 moves to front.
- Team 2: Workers 4-6. Rotate by 1 -> Worker 6 moves to front.
- Team 3: Workers 7-8 (incomplete team). Rotate by 1 -> Worker 8 moves to front.

You need to generate the new lineup order.

**Why This Problem Matters:**

- **Cryptography:** Block ciphers often involve permuting or rotating bits within fixed-size blocks.
- **UI Carousels:** Multiple independent carousels on a page rotating their content.
- **Data Batching:** Processing batches of data where the processing order within each batch is cyclic.

![Real-World Application](../images/LNK-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Block Rotation

List: `1 -> 2 -> 3 -> 4 -> 5 -> 6`
`b = 3`, `k = 1`

**Block 1:** `1 -> 2 -> 3`
- Size = 3.
- Rotate Right by `1 % 3 = 1`.
- Result: `3 -> 1 -> 2`.

**Block 2:** `4 -> 5 -> 6`
- Size = 3.
- Rotate Right by `1 % 3 = 1`.
- Result: `6 -> 4 -> 5`.

**Concatenate:**
`3 -> 1 -> 2` -> `6 -> 4 -> 5`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Independent Rotations:** Rotating block 1 does not affect block 2.
- **Last Block:** If `N=5, b=3`, the second block has size 2. Rotate it by `k % 2`.
- **Large K:** `k` can be very large, so always use modulo arithmetic.

Common interpretation mistake:

- ❌ **Wrong:** Rotating the entire list first, then splitting.
- ✅ **Correct:** Split first, then rotate each piece.

### Core Concept: Isolate and Rotate

To solve this cleanly, write a helper function `rotate(head, length, k)` that rotates a standalone list. Then, iterate through the main list, cutting out chunks of size `b`, rotating them, and stitching them back together.

## Naive Approach

### Intuition

Convert list to array. Process chunks in array. Convert back.

### Algorithm

1. List -> ArrayList.
2. For `i = 0` to `n` step `b`:
   - Extract sublist `[i, min(i+b, n))`.
   - Rotate sublist.
   - Append to result.
3. Array -> List.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

In-place manipulation. Maintain a `tail` pointer for the *previous* block to link to the *current* rotated block.

### Algorithm

1. `dummy` points to head. `prevTail = dummy`.
2. Loop while `head` exists:
   - **Identify Block:** Traverse `b` nodes to find the end of the current block. Count actual length `len`.
   - **Detach:** Save `nextBlockHead`. Break the link after the current block.
   - **Rotate:** Perform standard linked list rotation on the current block (size `len`, shift `k`).
   - **Attach:**
     - `prevTail.next = newBlockHead`
     - `prevTail = newBlockTail`
   - **Advance:** `head = nextBlockHead`.

### Time Complexity

- **O(N)**. We visit each node a constant number of times.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-013/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-013/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 2 3 4 5 6`, `b=3`, `k=1`

**Block 1:**
- `curr` at 1. `blockTail` moves 2 steps to 3. `len`=3.
- `nextBlockHead` = 4. Detach 3->null.
- Rotate `1->2->3` right by 1.
  - `moves` = 3 - 1 = 2.
  - `newTail` moves 1 step to 2.
  - `newHead` = 3.
  - Link 3->1. Break 2->null.
  - Result: `3->1->2`.
- Attach to dummy: `dummy->3->1->2`. `prevTail` = 2.

**Block 2:**
- `curr` at 4. `blockTail` moves 2 steps to 6. `len`=3.
- `nextBlockHead` = null. Detach 6->null.
- Rotate `4->5->6` right by 1.
  - Result: `6->4->5`.
- Attach to `prevTail`: `2->6->4->5`. `prevTail` = 5.

**Result:** `3 1 2 6 4 5`.

![Example Visualization](../images/LNK-013/example-1.png)

## ✅ Proof of Correctness

### Invariant
The list processed so far consists of fully rotated blocks in their correct relative order. `prevTail` always points to the last node of the processed portion.

### Why the approach is correct
- **Isolation:** Detaching blocks prevents rotation logic from messing up the rest of the list.
- **Modularity:** Using a standard `rotateList` function ensures correctness for edge cases (k=0, k>len).
- **Connectivity:** We explicitly track `prevTail` to stitch the result back together.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Rotate Left instead of Right.
  - *Hint:* `Rotate Left(k)` is same as `Rotate Right(len - k)`.
- **Extension 2:** Reverse blocks instead of rotate.
  - *Hint:* This is "Reverse Nodes in k-Group".
- **Extension 3:** Variable block sizes (given as an array).
  - *Hint:* Pass `sizes[i]` to the loop instead of constant `b`.

### Common Mistakes to Avoid

1. **Tail Linking**
   - ❌ Wrong: Forgetting to link the new tail of a rotated block to the *next* block (though our loop handles this by linking `prevTail` to `newHead` in the next iteration).
   - ✅ Correct: Our approach links `prevTail.next = newHead`.

2. **Modulo Arithmetic**
   - ❌ Wrong: `k % b` (using block size constant).
   - ✅ Correct: `k % len` (using actual length, which might be smaller for the last block).

## Related Concepts

- **List Rotation:** Standard problem.
- **Block Processing:** Breaking problems into chunks.
- **In-place Manipulation:** Avoiding extra arrays.
