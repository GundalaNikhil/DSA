---
problem_id: LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__5392
display_id: LNK-015
slug: workshop-odd-even-grouping-stable
title: "Workshop Odd Even Grouping Stable"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Partitioning
  - Stable Ordering
tags:
  - linked-list
  - partition
  - parity
  - medium
premium: true
subscription_tier: basic
---

# LNK-015: Workshop Odd Even Grouping Stable

## 📋 Problem Summary

You are given a linked list. You need to reorder it such that:
1. All nodes with **odd values** appear first.
2. All nodes with **even values** appear second.
3. The relative order of nodes within the odd group and within the even group must remain unchanged (stable).

## 🌍 Real-World Scenario

**Scenario Title:** The Workshop Team Split

A workshop facilitator wants to split participants into two large teams for a debate: "Team Odd" and "Team Even" based on the number on their badge.
- Participants are currently standing in a single line.
- The facilitator asks all "Odds" to step to the left and all "Evens" to step to the right.
- Then, the "Odd" line is placed in front of the "Even" line to enter the hall.
- Crucially, if Alice (Odd) was standing before Bob (Odd) in the original line, she must still be before him in the new team line.

**Why This Problem Matters:**

- **Data Partitioning:** Separating data into two categories (e.g., active vs. inactive users) for batch processing.
- **Radix Sort:** This is a single pass of a binary Radix Sort (sorting by the least significant bit).
- **Network Traffic:** Prioritizing certain packets (Odds) over others (Evens) while maintaining sequence order.

![Real-World Application](../images/LNK-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Partitioning

List: `2 -> 5 -> 4 -> 7`

1. **Initialize:** `OddHead`, `EvenHead`.
2. **Process 2 (Even):** Add to Even. `E: 2`
3. **Process 5 (Odd):** Add to Odd. `O: 5`
4. **Process 4 (Even):** Add to Even. `E: 2 -> 4`
5. **Process 7 (Odd):** Add to Odd. `O: 5 -> 7`

**Concatenate:**
`Odd` -> `Even`
`5 -> 7` -> `2 -> 4`

Result: `5 -> 7 -> 2 -> 4`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Parity of Value:** We are checking `val % 2`, NOT the index (odd/even positions).
- **Stability:** Order must be preserved.
- **Empty Groups:** If there are no odd numbers, the list starts with evens.

Common interpretation mistake:

- ❌ **Wrong:** Odd/Even *indices*. 
- ✅ **Correct:** Odd/Even *values*.

### Core Concept: Two Dummy Heads

Using `oddDummy` and `evenDummy` eliminates the need to handle the "first node" logic separately. We just append to the respective tails.

## Naive Approach

### Intuition

Create two ArrayLists. Iterate list. Add values to lists. Rebuild list.

### Algorithm

1. `odds = []`, `evens = []`
2. Loop through list:
   - If `val % 2 != 0`: `odds.add(val)`
   - Else: `evens.add(val)`
3. Create new nodes from `odds` then `evens`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Re-link existing nodes in a single pass.

### Algorithm

1. `oddDummy`, `evenDummy`.
2. `oddTail = oddDummy`, `evenTail = evenDummy`.
3. Iterate `curr` through list:
   - If `curr.val % 2 != 0`:
     - `oddTail.next = curr`
     - `oddTail = curr`
   - Else:
     - `evenTail.next = curr`
     - `evenTail = curr`
4. **Terminate:** `evenTail.next = null` (Important! Prevents cycles).
5. **Connect:** `oddTail.next = evenDummy.next`.
6. Return `oddDummy.next`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-015/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-015/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 5 4 7`

**Initialization:**
- `oddDummy`, `evenDummy` empty.

**Iteration:**
1. `2` (Even): `evenTail` -> 2.
2. `5` (Odd): `oddTail` -> 5.
3. `4` (Even): `evenTail` -> 4.
4. `7` (Odd): `oddTail` -> 7.

**Connection:**
- `evenTail.next = null` (4 -> null).
- `oddTail.next = evenDummy.next` (7 -> 2).

**Result:** `5 -> 7 -> 2 -> 4`.

![Example Visualization](../images/LNK-015/example-1.png)

## ✅ Proof of Correctness

### Invariant
`oddTail` points to the last processed odd node, `evenTail` points to the last processed even node. Order is preserved because we append to tail.

### Why the approach is correct
- We process sequentially.
- We separate into two disjoint sets.
- We concatenate them in the correct order (Odd then Even).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Group by index parity (Odd positions then Even positions).
- **Extension 2:** Sort 0s, 1s, 2s.
  - *Hint:* 3 dummy heads.
- **Extension 3:** Partition around pivot X.
  - *Hint:* Same logic, condition `val < X`.

### Common Mistakes to Avoid

1. **Cycle Creation**
   - ❌ Wrong: Forgetting `evenTail.next = null`. The last even node might point to an odd node from the original list, creating a cycle.
   - ✅ Correct: Always terminate the second list.

2. **Connecting Lists**
   - ❌ Wrong: `oddTail.next = evenTail`.
   - ✅ Correct: `oddTail.next = evenDummy.next`.

## Related Concepts

- **Stable Partition:** The general form of this problem.
- **Dummy Node:** Simplifies list construction.
