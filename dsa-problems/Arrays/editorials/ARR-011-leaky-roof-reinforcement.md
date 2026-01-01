---
problem_id: ARR_LEAKY_ROOF_REINFORCE__3586
display_id: ARR-011
slug: leaky-roof-reinforcement
title: "Leaky Roof Reinforcement"
difficulty: Medium
difficulty_score: 55
topics:
  - Arrays
  - Prefix Suffix
  - Greedy
tags:
  - arrays
  - prefix-suffix
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# ARR-011: Leaky Roof Reinforcement

## 📋 Problem Summary

Modify the array heights by increasing them such that the array becomes "pyramid-shaped" (non-decreasing up to a peak, then non-increasing). Minimize the total height added.

## 🌍 Real-World Scenario

**Scenario Title:** The Warehouse Roof Repair

You are reinforcing the flat, leaky roof of a large warehouse. To ensure proper drainage, the roof must slope downwards from a single ridge (the peak) to both sides.

- Current state: An irregular chaotic profile.
- Requirement: You can add insulation layers (increase height) but cannot cut the roof (decrease height).
- Goal: Create a perfect pyramid shape `... <= h[i] <= h[i+1] ... Peak ... h[j] >= h[j+1] >= ...` using the minimum amount of material.

**Why This Problem Matters:**

- **Unimodal Sequences**: Optimizing data to fit a specific geometric profile.
- **Prefix/Suffix Arrays**: Using precomputed auxiliary arrays to solve "best split point" problems in linear time.
- **Constraints**: "Only increase" is a key greedy constraint often found in resource allocation.

![Real-World Application](../images/ARR-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Forming the Pyramid

```
Original: [4] [1] [3] [1] [5]

Candidate 1: Peak at index 4 (Value 5)
Left side must be non-decreasing ending at 5.
[4] -> 4
[1] -> max(4, 1) = 4
[3] -> max(4, 3) = 4
[1] -> max(4, 1) = 4
[5] -> 5 (Peak)
Result: [4, 4, 4, 4, 5]. Total = 21.

Candidate 2: Peak at index 1 (Value 1)
- Natural height forced to 4 due to left neighbor's value of 4
- Left side: [4, 4]
- Right side (non-increasing): starts at 4, must handle remaining values
- Result: [4, 4, 4, 4, 5] (right side value 5 forces the peak to be 5)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Non-decreasing**: `x <= y`. Equal values are allowed (flat spots).
- **Peak choice**: You iterate through all possible indices `i` to be the peak.
- **Height Calculation**: Total height of the modified array minus sum of original array.

Common interpretation mistake:

- ❌ Trying to simulate "water flow" or Trapping Rain Water logic. This is about _shape constraints_, not volume filling.
- ✅ Understanding that if index `i` is the peak, `new_arr[i] = max(L[i], R[i])` where `L` and `R` are "natural" non-decreasing/non-increasing limits.

### Core Concept: Natural Floors

For any index `i`, if it belongs to the "left slope", its height must be at least `max(arr[0...i])`.

**Reasoning**: Because `new[i] >= new[i-1] >= ... >= arr[0]` and `new[i] >= arr[i]`, therefore `new[i] >= max(original prefix)`.

Formally: `L[i] = max(arr[i], L[i-1])`.

Similarly for the right slope: `R[i] = max(arr[i], R[i+1])`.

### Why Naive Approach is too slow

Iterating every possible peak `k`, then scanning left and right to compute sums is O(N) per peak -> Total O(N²).
With N=200,000, we need O(N).

## Naive Approach

### Intuition

Try every index as peak. Build the array. Sum it. Minimize.

### Algorithm

1. `min_total = infinity`.
2. Loop `k` from 0 to `n-1`.
   - `peak_val = arr[k]`.
   - Scan left `j=k-1...0`: `h[j] = max(arr[j], h[j+1])`? No, left is non-dec. `h[j] = min(h[j+1], ...)`? Wait.
   - The greedy construction for a fixed peak is tricky in loop.
   - Correct logic: Peak `k` forces `h[k] >= arr[k]`. Also neighbors force `h[k]` potentially higher.
   - This suggests O(N²) is not even trivial to write correctly without precomputation.

### Time Complexity

- **O(N²)**.

### Space Complexity

- **O(N)**.

## Optimal Approach (Prefix/Suffix Scan)

### Key Insight

Let `L[i]` be the lowest possible height of `i` if `0...i` is non-decreasing.
`L[i] = max(arr[i], L[i-1])`.
Let `SumL[i]` be the sum of heights `0...i` configured as minimal non-decreasing sequence ending at `L[i]`.
`SumL[i] = SumL[i-1] + L[i]`.

Similarly for `R[i]` (suffix non-increasing) and `SumR[i]`.
`R[i] = max(arr[i], R[i+1])`.
`SumR[i] = SumR[i+1] + R[i]`.

For a generic peak at `k`, the sequence is `0...k` (left slope) and `k...n-1` (right slope).
The value at `k` must satisfy both sides. Effectively `FinalPeak = max(L[k], R[k])`.
The total sum = `(SumL[k] adjusted for FinalPeak) + (SumR[k] adjusted for FinalPeak) - FinalPeak`.
Since `L[k]` and `R[k]` are the "floors" for index `k`, raising `k` to `FinalPeak` simply adds `(FinalPeak - L[k])` cost to the left sum, and `(FinalPeak - R[k])` to the right sum.
Why? Because raising the end of a non-decreasing sequence doesn't force previous elements to raise further (they were bounded by `L[k]`, now bounded by `FinalPeak` which is looser).

Final Formula for Peak `k`:
`Cost = SumL[k] + SumR[k] - min(L[k], R[k])`.

### Algorithm

1. Compute `L` and `SumL` arrays (Forward).
2. Compute `R` and `SumR` arrays (Backward).
3. `TotalOriginalSum = sum(arr)`.
4. Iterate `k` from 0 to `n-1`:
   - `TotalH = SumL[k] + SumR[k] - min(L[k], R[k])`
   - `MinH = min(MinH, TotalH)`
5. Return `MinH - TotalOriginalSum`.

### Time Complexity

- **O(N)**: 3 linear passes.

### Space Complexity

- **O(N)**: Auxiliary arrays.

### Why This Is Optimal

Linear processing of the array is required.

![Algorithm Visualization](../images/ARR-011/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-011/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[4, 1, 3, 1, 5]`
**Arrays**:

- `L`: `[4, 4, 4, 4, 5]`
- `SumL`: `[4, 8, 12, 16, 21]`
- `R`: `[5, 5, 5, 5, 5]`
- `SumR`: `[25, 20, 15, 10, 5]`

**Scan**:

- i=0: `4 + 25 - 4 = 25`.
- i=1: `8 + 20 - min(4,5) = 24`.
- i=2: `12 + 15 - 4 = 23`.
- i=3: `16 + 10 - 4 = 22`.
- i=4: `21 + 5 - 5 = 21`.

**Min**: 21.
**Original Sum**: `4+1+3+1+5 = 14`.
**Result**: `21 - 14 = 7`. Matches Example.

![Example Visualization](../images/ARR-011/example-1.png)

## ✅ Proof of Correctness

### Invariant

`SumL[i]` is the minimal cost to make the prefix `0...i` non-decreasing. Any other non-decreasing prefix ending at index `i` must have height `H >= L[i]` and thus would cost `SumL[i] + (H - L[i]) * (something)`. The greedy choice of `L[i]` is optimal for fixed index constraints.

### Why the approach is correct

The global optimum must have _some_ peak index. Our linear scan exhaustively checks every possible peak loction efficiently, ensuring the global minimum is found.

## 💡 Interview Extensions (High-Value Add-ons)

- **Bitonic Subsequence**: Longest Bitonic Subsequence (DP, O(N log N) or O(N^2)). This is related but about _subsequences_, not modification.
- **Two Peaks**: What if "M" shape? (Scan for best valley).

## Common Mistakes to Avoid

1. **Double Counting Peak**:

   - ❌ `SumL[i] + SumR[i]` adds the peak column twice.
   - ✅ Correct formula: `SumL + SumR - min(L, R)`

   **Derivation**:

   - `SumL` uses peak height `L[i]`
   - `SumR` uses peak height `R[i]`
   - Actual peak `P = max(L[i], R[i])`
   - Left contributions: `SumL + (P - L[i])`
   - Right contributions: `SumR + (P - R[i])`
   - Total = `SumL + SumR + P - L[i] - R[i]`
   - Since `P = max(L, R)`, we have `P - L - R = -min(L, R)`
   - Therefore: Total = `SumL + SumR - min(L, R)`
   - So YES, `SumL + SumR - min(L, R)` is correct.

2. **Overflow**:
   - ❌ Using int for sums.
   - ✅ Use long.

## Related Concepts

- **Trapping Rain Water**: But inverted (filling valleys vs building peaks).
- **Product of Array Except Self**: Prefix/Suffix pattern.
