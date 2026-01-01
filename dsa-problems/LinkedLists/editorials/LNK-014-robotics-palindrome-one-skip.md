---
problem_id: LNK_ROBOTICS_PALINDROME_ONE_SKIP__6741
display_id: LNK-014
slug: robotics-palindrome-one-skip
title: "Robotics Palindrome with One Skip"
difficulty: Medium
difficulty_score: 54
topics:
  - Linked List
  - Two Pointers
  - Palindrome
tags:
  - linked-list
  - palindrome
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# LNK-014: Robotics Palindrome with One Skip

## 📋 Problem Summary

You are given a linked list. Determine if it can become a palindrome by removing **at most one** node.
- If it's already a palindrome, return `true`.
- If removing one node makes it a palindrome, return `true`.
- Otherwise, return `false`.

## 🌍 Real-World Scenario

**Scenario Title:** The DNA Sequence Validator

A robotic sensor reads a DNA sequence from a biological sample. DNA strands often contain palindromic sequences (like `GAATTC` for EcoRI restriction sites). However, due to minor mutations or reading errors, a single extra base pair might be inserted.
- Sequence: `A -> G -> C -> T -> T -> C -> G -> A` (Perfect Palindrome)
- Mutation: `A -> G -> X -> C -> T -> T -> C -> G -> A` (One 'X' inserted)

The robot needs to validate if the sequence is a "near-palindrome" (valid palindrome with at most one error) to accept the sample.

**Why This Problem Matters:**

- **Spell Checkers:** Detecting words that are one typo away from a valid palindrome.
- **Data Transmission:** Error detection where a single bit flip or insertion can be ignored.
- **Computer Vision:** Recognizing symmetric shapes that have a minor defect or noise.

![Real-World Application](../images/LNK-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Two Pointers with Skip

List: `1 -> 2 -> 3 -> 4 -> 2 -> 1`

1. **Convert to Array:** `[1, 2, 3, 4, 2, 1]`
2. **Pointers:** `L=0` (1), `R=5` (1). Match!
3. **Move:** `L=1` (2), `R=4` (2). Match!
4. **Move:** `L=2` (3), `R=3` (4). **Mismatch!**

**Branch 1 (Skip Left):**
- Remove index 2 (val 3).
- Check subarray `[4]` (indices 3 to 3).
- Palindrome? Yes. **Return True.**

**Branch 2 (Skip Right):**
- Remove index 3 (val 4).
- Check subarray `[3]` (indices 2 to 2).
- Palindrome? Yes.

Since at least one branch works, the answer is `true`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **At Most One:** 0 deletions is fine.
- **Empty List:** Is a palindrome.
- **Single Node:** Is a palindrome.

Common interpretation mistake:

- ❌ **Wrong:** Trying to modify the linked list in-place and restore it.
- ✅ **Correct:** Converting to an ArrayList/Vector is O(N) space but makes the logic trivial (random access). Given the constraints and difficulty, this is the expected approach.

### Core Concept: Greedy Match

We match from outside in. The moment we find a mismatch, we have exactly two choices: delete the left character or delete the right character. We don't need to try deleting characters elsewhere because the outer layers already matched.

## Naive Approach

### Intuition

For every node `i`, remove it, check if remaining list is palindrome.

### Algorithm

1. Loop `i` from 0 to `n`.
2. Create copy of list without node `i`.
3. Check if copy is palindrome.
4. If yes, return true.

### Time Complexity

- **O(N^2)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Use Two Pointers on an array representation.

### Algorithm

1. Traverse list and store values in an array `vals`.
2. Initialize `left = 0`, `right = n - 1`.
3. While `left < right`:
   - If `vals[left] == vals[right]`:
     - `left++`, `right--`
   - Else:
     - Check if `vals[left+1...right]` is a palindrome OR
     - Check if `vals[left...right-1]` is a palindrome.
     - Return result of check.
4. Return `true` (if loop finishes without returning).

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** for the array. (O(1) space is possible by reversing the second half of the linked list, but it's much more complex and destructive).

![Algorithm Visualization](../images/LNK-014/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-014/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 2 3 2 1`
Array: `[1, 2, 3, 2, 1]`
- L=0 (1), R=4 (1). Match.
- L=1 (2), R=3 (2). Match.
- L=2 (3), R=2 (3). Loop ends.
Result: `true`.

Input: `1 5 2`
Array: `[1, 5, 2]`
- L=0 (1), R=2 (2). Mismatch.
- Try Skip Left (L=1, R=2): `[5, 2]`. 5 != 2. Fail.
- Try Skip Right (L=0, R=1): `[1, 5]`. 1 != 5. Fail.
Result: `false`.

![Example Visualization](../images/LNK-014/example-1.png)

## ✅ Proof of Correctness

### Invariant
If a palindrome exists with at most one deletion, the mismatch MUST occur at the first pair of indices `(L, R)` where `vals[L] != vals[R]`.

### Why the approach is correct
- We match greedily from the outside.
- When we hit a mismatch, the "bad" character must be either `vals[L]` or `vals[R]`.
- We try both possibilities. If either results in a valid inner palindrome, we are good.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Solve in O(1) space.
  - *Hint:* Find middle, reverse second half. Compare. If mismatch, skip one node and compare rest. Complex pointer management.
- **Extension 2:** Longest Palindromic Subsequence.
  - *Hint:* Dynamic Programming (O(N^2)).
- **Extension 3:** K deletions allowed.
  - *Hint:* Recursion with memoization or DP.

### Common Mistakes to Avoid

1. **Skipping Both**
   - ❌ Wrong: Skipping both L and R at the same time.
   - ✅ Correct: You can only delete ONE node total.

2. **Edge Cases**
   - ❌ Wrong: Failing on empty list or single node.
   - ✅ Correct: Loop `left < right` handles these naturally.

