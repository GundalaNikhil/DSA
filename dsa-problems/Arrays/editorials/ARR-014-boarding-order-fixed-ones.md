---
problem_id: ARR_FIXED_ONES_SORT__5412
display_id: ARR-014
slug: boarding-order-fixed-ones
title: "Boarding Order With Fixed Ones"
difficulty: Medium
difficulty_score: 48
topics:
  - Arrays
  - Sorting
  - Two Pointers
tags:
  - arrays
  - sorting
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# ARR-014: Boarding Order With Fixed Ones

## 📋 Problem Summary

Sort an array containing `0`s, `1`s, and `2`s such that all `0`s appear before `2`s in the available slots, while **keeping all `1`s exactly where they are**.

## 🌍 Real-World Scenario

**Scenario Title:** The Reserved Seating Protocol

You are boarding passengers onto a plane.

- **Group 0**: Economy (Must board first).
- **Group 1**: VIPs/Disabled (Already seated/fixed).
- **Group 2**: Late arrivals (Must board last).

The plane has a single aisle. The VIPs (`1`) are already in their specific assigned seats and cannot move.
You have a mixed line of Economy (`0`) and Late (`2`) passengers standing in the aisle. You need to swap them around so that all Economy passengers sit in the front-most available seats, and Late passengers take the back-most available seats, skipping over the occupied VIP seats.

**Why This Problem Matters:**

- **In-Place Partitioning**: Handling fixed obstacles while sorting/partitioning is a practical constraint in memory management (pinned pages).
- **Two Pointers**: Navigating disjoint subsets of indices efficiently.
- **Dutch National Flag Variant**: A twist on the classic Dijkstra problem.

![Real-World Application](../images/ARR-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Skipping Fixed Elements

```
Idx:    0   1   2   3   4   5
Arr:   [2] [1] [0] [2] [0] [1]

Left Pointer searches for a '2' (misplaced). Finds Idx 0.
Right Pointer searches for a '0' (misplaced). Finds Idx 4 (skips Idx 5 '1').
Swap(0, 4).

Arr:   [0] [1] [0] [2] [2] [1]
        ^       ^
       Fixed   Moved
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sorting Order**: `0`s ... `1`s (fixed) ... `2`s? No, `0`s take _available_ slots from left, `2`s take _available_ slots from right. `1`s interrupt the flow but don't move.
- **Stability**: Not required generally, just value partitioning.
- **In-Place**: Preferred solution uses O(1) space.

Common interpretation mistake:

- ❌ Collecting all 0s, 1s, 2s and overwriting.
- ✅ Collecting only 0s and 2s, but putting 1s back in? NO. You must **never** touch the 1s.

### Core Concept: Two Pointers (Filter)

We effectively ignore the `1`s.

- `left` pointer scans from start, skipping `1`s, looking for `2`s (which belong on the right).
- `right` pointer scans from end, skipping `1`s, looking for `0`s (which belong on the left).
- When both pause, swap them.

### Why Naive Approach is too slow

Standard `sort` O(N log N) works if you extract 0s/2s into a temp array, sort them, and put them back. But that uses O(N) space and is overkill for 3 values.
We want O(N) time and O(1) space.

## Naive Approach (Extract and Fill)

### Intuition

Pull all `0`s and `2`s into a list. Sort/Partition that list. Put them back into non-`1` slots.

### Algorithm

1. `temp = []`.
2. Loop `i` 0 to N-1: if `arr[i] != 1`, add to `temp`.
3. Count 0s in `temp`. Reconstruct sorted version (all 0s then all 2s).
4. `k = 0`. Loop `i` 0 to N-1:
   - if `arr[i] != 1`: `arr[i] = temp[k++]`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** (Temp array).

## Optimal Approach (Two Pointers In-Place)

### Key Insight

We only need to fix inversions where a `2` is to the left of a `0`. The `1`s are just "walls" we jump over.
This is similar to partitioning an array into `[Evens | Odds]`, but here slots are non-contiguous.

### Algorithm

1. Initialize `L = 0`, `R = n - 1`.
2. Loop while `L < R`:
   - While `L < R` and (`arr[L] == 0` or `arr[L] == 1`):
     - If `arr[L] == 1`: skip.
     - If `arr[L] == 0`: correct place, skip.
     - Increment `L`.
   - While `L < R` and (`arr[R] == 2` or `arr[R] == 1`):
     - If `arr[R] == 1`: skip.
     - If `arr[R] == 2`: correct place, skip.
     - Decrement `R`.
   - If `L < R`:
     - Now `arr[L]` must be `2` and `arr[R]` must be `0`.
     - Swap `arr[L]` and `arr[R]`.
     - `L++`, `R--`.

### Time Complexity

- **O(N)**: Each element visited constant times.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

Single pass, minimal writes.

![Algorithm Visualization](../images/ARR-014/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-014/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[2, 1, 0, 2, 0, 1]`

**Step-by-step execution**:

1. **Initial state**: `left=0`, `right=5`

   - `arr[0]=2` (needs to move right)
   - `arr[5]=1` (skip, it's fixed)
   - Move `right` left: `arr[4]=0` (good for left side)

2. **First swap**: Swap `arr[0]` and `arr[4]`

   - Array becomes: `[0, 1, 0, 2, 2, 1]`
   - `left` moves to 1

3. **Continue scanning**:
   - `arr[1]=1` → Skip (fixed)
   - `arr[2]=0` → Skip (already on left side)
   - `arr[3]=2` → Stop at index 3
   - `right=4`, `arr[4]=2` → Already on right side
   - Pointers meet: `left=3`, `right=3`

**Final Output**: `[0, 1, 0, 2, 2, 1]`

**Verification**:

- **1s remain fixed**: Indices 1 and 5 still contain value `1` ✓
- **0s on left**: Indices 0 and 2 contain `0` ✓
- **2s on right**: Indices 3 and 4 contain `2` ✓
- **Relative order maintained**: Non-1 elements are properly partitioned ✓

## ✅ Proof of Correctness

### Invariant

`arr[0...left-1]` (ignoring 1s) contains `0`s. `arr[right+1...n-1]` (ignoring 1s) contains `2`s. The pointers converge, swapping misplaced elements, ensuring final partition.

## 💡 Interview Extensions (High-Value Add-ons)

- **Counting Sort**: Simpler mental model.
- **Pivot variation**: What if pivot isn't fixed but just 'middle value'? (Standard QSort partition).

## Common Mistakes to Avoid

1. **Overwriting 1s**:

   - ❌ Moving a 1.
   - ✅ Always skipping index if `arr[i] == 1`.

2. **Pointer Convergence**:
   - ❌ `while (arr[left] == 0)` might go out of bounds.
   - ✅ Always check `left < right` AND value condition.

## Related Concepts

- **Dutch National Flag**: The base problem.
- **Partitioning**: Core quicksort logic.
