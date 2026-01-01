---
problem_id: LNK_EXAM_SEATING_INTERSECTION_SUM__5629
display_id: LNK-011
slug: exam-seating-intersection-sum
title: "Exam Seating Intersection Sum"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Intersection
  - Two Pointers
tags:
  - linked-list
  - intersection
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# LNK-011: Exam Seating Intersection Sum

## 📋 Problem Summary

You are given two singly linked lists, List A and List B. They might intersect at some node and share all subsequent nodes (forming a 'Y' shape). Your task is to:
1. Determine if they intersect.
2. If they do, calculate the sum of values of all nodes in the shared suffix (starting from the intersection node to the end).
3. If they don't intersect, return 0.

## 🌍 Real-World Scenario

**Scenario Title:** The Merging Exam Lines

Students from two different exam halls (Hall A and Hall B) are leaving the building.
- Hall A students walk down Corridor A.
- Hall B students walk down Corridor B.
- At some point, Corridor B merges into Corridor A, and from there, everyone walks down the same final path to the exit.

You want to calculate the "total age" (sum of values) of all students who are walking in the shared path after the merge point.

**Why This Problem Matters:**

- **Git Branches:** Two branches of development history merging into a common timeline.
- **River Systems:** Tributaries joining a main river; calculating water volume in the main channel.
- **Memory Sharing:** In immutable data structures (like in functional programming), two lists might share a common tail to save memory.

![Real-World Application](../images/LNK-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Intersection

List A: `1 -> 2 -> 3 -> 4`
List B: `9 -> 3 -> 4` (Connects to 3 in A)

Visualizing the 'Y' shape:
```
A: 1 -> 2
         \
          3 -> 4 -> null
         /
B:      9
```
Intersection Node: `3`.
Shared Suffix: `3 -> 4`.
Sum: `3 + 4 = 7`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Reference Equality:** Intersection is defined by reference (memory address), not value. Two nodes with value `3` are distinct unless they are literally the same object.
- **No Intersection:** If the lists never merge, return 0.
- **Suffix Sum:** Include the intersection node itself in the sum.

Common interpretation mistake:

- ❌ **Wrong:** Summing values from the start of both lists.
- ✅ **Correct:** Only summing the shared tail.

### Core Concept: Length Alignment

If List A has length 5 and List B has length 3, the intersection cannot happen at A's first 2 nodes. We can skip the first `5-3=2` nodes of A to align the starting positions.

## Naive Approach

### Intuition

For every node in List A, traverse List B to see if it matches.

### Algorithm

1. Loop `currA` through List A.
2. Inside, loop `currB` through List B.
3. If `currA == currB`, we found intersection. Calculate sum and return.

### Time Complexity

- **O(N * M)**. Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Align the starts. Calculate length of A (`lenA`) and B (`lenB`). Advance the pointer of the longer list by `abs(lenA - lenB)`. Then move both pointers forward together. They will meet at the intersection.

### Algorithm

1. Calculate `lenA` and `lenB`.
2. Reset pointers `ptrA = headA`, `ptrB = headB`.
3. If `lenA > lenB`, advance `ptrA` by `lenA - lenB`.
4. If `lenB > lenA`, advance `ptrB` by `lenB - lenA`.
5. While `ptrA != ptrB`:
   - `ptrA = ptrA.next`
   - `ptrB = ptrB.next`
   - If either becomes null, return 0 (no intersection).
6. Now `ptrA` is the intersection node (or null).
7. Traverse from `ptrA` to end, summing values.
8. Return sum.

### Time Complexity

- **O(N + M)**. We traverse each list a constant number of times.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-011/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-011/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: A=`1->2->3->4`, B=`9->3->4` (B connects to A's 3).
`lenA` = 4. `lenB` = 3.

**Alignment:**
- `lenA` > `lenB`. Advance `ptrA` by 1.
- `ptrA` points to 2. `ptrB` points to 9.

**Search:**
- `ptrA` (2) != `ptrB` (9). Advance both.
- `ptrA` (3) == `ptrB` (3). **Match!**

**Sum:**
- Start at 3. Sum = 3.
- Next is 4. Sum = 3 + 4 = 7.
- Next is null.

Result: 7.

![Example Visualization](../images/LNK-011/example-1.png)

## ✅ Proof of Correctness

### Invariant
After alignment, `ptrA` and `ptrB` are equidistant from the end of the list.

### Why the approach is correct
- Since they share the suffix, the distance from intersection to end is identical.
- By aligning starts, we ensure that if they meet, they meet at the *first* common node.
- If they reach null without meeting, there is no intersection.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if list has cycles?
  - *Hint:* Much harder. Need to detect cycles first, then check if cycles are same.
- **Extension 2:** Find intersection without length calculation (Two Pointers trick).
  - *Hint:* `ptrA` traverses A then B. `ptrB` traverses B then A. They meet at intersection or null.
- **Extension 3:** Minimize memory access.
  - *Hint:* Length calculation is cache-friendly (sequential access).

### Common Mistakes to Avoid

1. **Value Comparison**
   - ❌ Wrong: `ptrA.val == ptrB.val`.
   - ✅ Correct: `ptrA == ptrB` (reference check).

2. **Off-by-one**
   - ❌ Wrong: Advancing `lenA - lenB - 1`.
   - ✅ Correct: Advance exactly the difference.

3. **Null Pointer**
   - ❌ Wrong: Accessing `ptrA.next` when `ptrA` is null.
   - ✅ Correct: Loop condition `ptrA != null`.

## Related Concepts

- **Two Pointers:** Aligning start positions.
- **Reference vs Value:** Crucial in linked lists.
