---
problem_id: ARR_DISTINCT_PEAKS__5533
display_id: ARR-036
slug: longest-subarray-distinct-peaks
title: "Longest Subarray with <= K Distinct Peaks"
difficulty: Medium
difficulty_score: 40
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - peaks
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-036: Longest Subarray with <= K Distinct Peaks

## 📋 Problem Summary

Find the maximum length of a contiguous subarray such that the number of "Peaks" inside it is at most `K`.
A peak is an element strictly greater than its immediate neighbors.

## 🌍 Real-World Scenario

**Scenario Title:** 🚵 The Gentle Trail

### The Problem

A novice cyclist wants to go on a ride.
They don't mind climbing hills, but they hate the "Up and Down" exhaustion of constantly changing gradients.
They are willing to conquer at most `K` summits (Peaks) in one continuous ride.
You have an elevation map. Find the longest trail segment they can ride that fits their stamina constraint.

### Real-World Relevance

- **Financial Volatility:** Identifying long periods of time where a stock price didn't fluctuate wildly (few local maxima).

## 🚀 Detailed Explanation

### 1. Identifying Peaks

First, pre-process the array to identify peak indices.
`IsPeak[i] = true` if `arr[i-1] < arr[i]` and `arr[i] > arr[i+1]`.
Edges (0 and N-1) cannot be peaks.

### 2. Sliding Window (Two Pointers)

We want the longest window `[L, R]` containing `<= K` peaks.
As `R` moves right, the number of peaks in `[L, R]` non-decreases.
This Monotonic property allows a Sliding Window.

### 3. The Boundary Subtlety

The definition of a peak is local to the subarray?
Problem Statement says: "For a subarray `a_l..a_r`, an index `i` (l < i < r) is a peak if..."
This means peaks are determined by neighbors _inside_ the subarray.
Crucially, **endpoints (L and R) are never peaks**.
Wait.
If `arr` is `1 5 1`. Index 1 is a peak globally.
In subarray `[1 5 1]`, index 1 is a peak (neighbors 1, 1 exist).
In subarray `[1 5]`, index 1 is NOT a peak (no right neighbor).
So, if `i` is a peak in the full array, it is ONLY a peak in `[L, R]` if `L < i < R`.
This simplifies things!
We just need to count how many _Global Peaks_ fall strictly inside `(L, R)`.

### 4. Algorithm

1. Create a boolean array `P` where `P[i] = 1` if `arr[i]` is a Global Peak, `0` otherwise.
2. We need `Sum(P[L+1...R-1]) <= K`.
3. Sliding Window:
   - Expand `R`.
   - If `P[R-1]` is a peak (and `R > L+1`), increment `PeakCount`.
   - While `PeakCount > K`:
     - Contract `L`.
     - If `P[L+1]` was a peak (and `L < R-1`), decrement `PeakCount`.
   - `MaxLen = max(MaxLen, R - L + 1)`.

Wait, care with indices.
When we add `R`, the new potential peak is at `R-1`. `R` itself is never a peak (endpoint).
When we remove `L`, the old potential peak was at `L+1`. `L` itself was never a peak (endpoint).
So we track peaks in the range `[L+1, R-1]`.
Window state: `CurrentPeaks`.

- `Add(R)`: If `IsGlobalPeak[R-1]`, count++.
- `Remove(L)`: If `IsGlobalPeak[L+1]`, count--.
- Note: We must ensure window length is at least 1. If Len < 3, peaks is always 0.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Identify Global Peaks P[1..N-2]]
    B --> C[Init L=0, R=0, Count=0, MaxLen=0]
    C --> D[Loop R from 0 to N-1]
    D --> E{R >= 2 and P[R-1]?}
    E -- Yes --> F[Count++]
    E -- No --> G[Continue]
    F --> H{Count > K?}
    H -- Yes --> I{P[L+1]?}
    I -- Yes --> J[Count--]
    I -- No --> K[Continue]
    J --> L[L++]
    K --> L
    L --> H
    H -- No --> M[MaxLen = max(MaxLen, R-L+1)]
    M --> D
    D -- End Loop --> N[Return MaxLen]
```

## 🧪 Edge Cases to Test

1.  **Length < 3:** No peaks possible. MaxLen = N (if K>=0).
2.  **K=0:** Longest subarray with no internal peaks.
3.  **Peaks at Boundaries:** If `arr[1]` is a peak, and we select `[0, 1]`, it's not a peak. Correct.

## 🏃 Naive vs Optimal Approach

### Naive O(N^2)

Check every subarray.

### Sliding Window O(N)

- **Time:** O(N).
- **Space:** O(N) for peak array (or O(1) on the fly).
  Optimal.
