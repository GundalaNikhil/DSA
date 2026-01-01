---
problem_id: ARR_MERGE_PRIORITY_TIE__6153
display_id: ARR-007
slug: hostel-roster-merge-gap
title: "Hostel Roster Merge With Gap"
difficulty: Medium
difficulty_score: 42
topics:
  - Arrays
  - Two Pointers
  - Merge
tags:
  - arrays
  - two-pointers
  - merge
  - medium
premium: true
subscription_tier: basic
---

# ARR-007: Hostel Roster Merge With Gap

## 📋 Problem Summary

Merge two pre-sorted lists `A` and `B` into a single sorted list. In case of tie (equal values), elements from `A` must appear before elements from `B`.

## 🌍 Real-World Scenario

**Scenario Title:** The University Merger

Two rival universities, "Alpha Academy" (A) and "Beta Institute" (B), are merging into one mega-campus. The administration needs to create a single master list of students ranked by their Entrance Exam Score (sorted, lowest to highest).

However, Alpha Academy has been around longer. The dean decides:
"If a student from Alpha and a student from Beta have the exact same score, the **Alpha student should be listed first** in the new roster."

You need to write the script to merge the two sorted databases while respecting this seniority rule.

**Why This Problem Matters:**

- **Merge Sort**: This is the core "Conquer" step of the Merge Sort algorithm.
- **Stability**: Understanding how to preserve relative order of equal elements is critical in sorting complex objects (e.g., sorting by Date, then by Name).
- **Stream Processing**: Merging sorted logs from different servers by timestamp.

![Real-World Application](../images/ARR-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Merge Process

```
List A:   [1]   [3]   [3]
Pointer:   ^     ^
List B:   [3]   [4]
Pointer:   ^

Comparison: A[1] (3) vs B[0] (3)
Rule: Tie -> Pick A
Result adds: 3 (from A)
Pointer A moves.

Next: A[2] (3) vs B[0] (3)
Rule: Tie -> Pick A
Result adds: 3 (from A)
Pointer A moves.

Next: A empty? No. B empty? No.
...
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sorted Inputs**: You can assume A and B are already sorted.
- **Priority**: A comes before B. This corresponds to a "Stable Merge".
- **Empty Arrays**: One or both arrays might be empty. Handle this gracefully.

Common interpretation mistake:

- ❌ Treating `A[i] < B[j]` as the only condition to pick A.
- ✅ Correctly using `A[i] <= B[j]` to pick A on ties.

### Core Concept: Two Pointers (Merge Step)

Maintain a pointer `i` for array A and `j` for array B. Compare `A[i]` and `B[j]`. Append the smaller one to the result. If equal, append `A[i]`. Increment the pointer of the chosen element.

### Why Naive Approach is too slow

Concatenating both arrays and calling `sort()` takes `O(K log K)` where `K = N + M`.
Since the inputs are _already sorted_, we are wasting work re-sorting them. We can do it in linear time `O(K)`.

## Naive Approach (Concat + Sort)

### Intuition

Combine vectors and sort.

### Algorithm

1. `C = A + B`
2. `C.sort()` (standard sort is usually stable, but verify language spec or use composite key).
3. Return `C`.

### Time Complexity

- **O((N+M) log (N+M))**: Dominant term is sorting.

### Space Complexity

- **O(N+M)**: To store result.

### Limitations

- **Inefficient**: Ignores the sorted structure of inputs.

## Optimal Approach (Two Pointers)

### Key Insight

Since A and B are sorted, the smallest element of the standard merge will always be either `A[current]` or `B[current]`. We just choose the winner repeatedly.

### Algorithm

1. Initialize `i = 0`, `j = 0`, `k = 0`.
2. Create result array `C` of size `N + M`.
3. Loop while `i < N` AND `j < M`:
   - If `A[i] <= B[j]`:
     - `C[k] = A[i]`, `i++`
   - Else:
     - `C[k] = B[j]`, `j++`
   - `k++`
4. If `i < N` (A has leftovers): copy remaining A to C.
5. If `j < M` (B has leftovers): copy remaining B to C.
6. Return C.

### Time Complexity

- **O(N + M)**: We iterate through each element of A and B exactly once.

### Space Complexity

- **O(N + M)**: To store the merged result.

### Why This Is Optimal

We must output N+M elements, so O(N+M) is required.

![Algorithm Visualization](../images/ARR-007/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `A=[1, 3, 3]`, `B=[3, 4]`

1. **Init**: `i=0`, `j=0`.
2. `1 <= 3`. Pick A[0]=1. Result `[1]`. `i=1`.
3. `3 <= 3`. Tie! Pick A[1]. Result `[1, 3]`. `i=2`.
4. `3 <= 3`. Tie! Pick A[2]. Result `[1, 3, 3]`. `i=3`.
5. `i=3` (End of A). Loop breaks.
6. Flush B: Append 3, 4.
7. Final: `[1, 3, 3, 3, 4]`.

Matches Example.

![Example Visualization](../images/ARR-007/example-1.png)

## ✅ Proof of Correctness

### Invariant

At step `k`, `result` contains the smallest `k` elements from `A union B`. The "next" smallest is `min(A[i], B[j])`. The logic correctly selects the minimum and resolves ties in favor of A, thus maintaining stability.

## 💡 Interview Extensions (High-Value Add-ons)

- **One Array Empty**: Handle correctly? (Yes).
- **In-Place**: Merge sorted B into sorted A? (A: Start from the END of A if A has extra buffer space).
- **K Arrays**: Merge K sorted arrays? (A: Use Min-Heap).

## Common Mistakes to Avoid

1. **Index Out of Bounds**:

   - ❌ Checking `A[i] <= B[j]` without verifying `i < n` and `j < m`.
   - ✅ Always check bounds in `while` loop condition.

2. **Incorrect Tie Breaking**:
   - ❌ Using `A[i] < B[j]` (strict less). If equal, this condition fails, so you'd pick B. Wrong!
   - ✅ Use `A[i] <= B[j]`. If equal, this holds, so you pick A.

## Related Concepts

- **Merge Sort**: Uses this exact subroutine.
- **Two Pointers**: General pattern.
