---
problem_id: ARR_ONE_DROP_INC__6621
display_id: ARR-017
slug: longest-nondecreasing-one-drop
title: "Longest Non-Decreasing with One Drop"
difficulty: Medium
difficulty_score: 35
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - subarray
  - subsequence
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-017: Longest Non-Decreasing with One Drop

## 📋 Problem Summary

Find the longest contiguous subarray where the numbers are going up (or same) `a <= b <= c...`.
Exception: You are allowed **at most one** "drop" (e.g., `5 -> 2`).
But wait! The definition of "drop" needs care.
Usually "One Drop" means you can delete one element? Or just ignore one violation?
Problem says: "A drop is an index `i` such that `a_i > a_{i+1}`."
So `1, 2, 5, 2, 3, 4` has a drop at `5 -> 2`.
Is `2, 3, 4` valid after the drop? Yes.
So we want the longest subarray `L...R` that contains at most one index `k` where `arr[k] > arr[k+1]`.

## 🌍 Real-World Scenario

**Scenario Title:** 📉 The Market Correction

### The Problem

A stock is in a "Bull Run" (going up).
Sometimes there is a single "Correction" (a sharp drop), after which it resumes going up.
Investors are okay with one correction, but if it drops twice, it's a "Crash".
You want to find the longest time period where the market was "Healthy" (Non-decreasing OR Single Correction).

### Real-World Relevance

- **Sensor Data:** A temperature sensor usually rises during the day. A single glitch might read low, or a cloud passes. One anomaly is ignored.
- **Game Streaks:** Winning streak where one loss is forgiven.

## 🚀 Detailed Explanation

### 1. Decomposing segments

The array naturally breaks into "Non-Decreasing Segments".
`[1, 2, 5]`, `[2, 3, 4]`, `[6]`.
If we join two adjacent segments, we have **exactly one** drop at the junction.
So the answer is simply: `Length(Segment_i) + Length(Segment_{i+1})`.
Wait.
Example: `1 2 5 2 3 4`.
Seg 1: `1 2 5`.
Seg 2: `2 3 4`.
Joined: `1 2 5 2 3 4`. Cost: One drop (`5->2`). Valid!
Length: 3 + 3 = 6.

Is it possible to have a drop _inside_ a chosen subarray but NOT at the join?
No, because "Non-decreasing" implies `a[i] <= a[i+1]` everywhere else.
So any valid subarray is formed by taking:

1. Part of a non-decreasing run.
2. The drop.
3. Part of the _next_ non-decreasing run.

Actually, we can take the **entire** first run and the **entire** second run?
Yes, because `Run1 End` > `Run2 Start` is the ONE drop.
All internal checks in Run1 are valid.
All internal checks in Run2 are valid.
Only one violation at the border.

So we just need to find `Max(Length[i] + Length[i+1])` where `i` and `i+1` are consecutive increasing runs.

### 2. Is there a catch?

"At most one".
Zero drops is also allowed. (Just one long run).
Our logic holds: `Length[i] + 0` is covered if we considered single runs.

Wait, what if `1 2 5 | 10 11 12`?
Here `5 < 10`. No drop at boundary.
This is arguably strictly better! This is ONE big run `1 ... 12`.
So my "segment" logic only breaks when `a[i] > a[i+1]`.
If `a[i] <= a[i+1]`, the runs are merged.

**Correct Algorithm:**

1. Identify all indices `k` where `arr[k] > arr[k+1]`. These are "Drop Points".
2. These points split the array into Strictly Non-Decreasing chunks.
3. A valid subarray can cover at most **two** adjacent chunks (the specific drop between them is the "one drop").
4. So calculate lengths of all chunks.
5. Answer is `max(Chunk[i].len + Chunk[i+1].len)`.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Identify Drop Indices]
    B --> C[Split Array into Chunks C1, C2... based on drops]
    C --> D[MaxLen = 0]
    D --> E[Loop i from 0 to NumChunks-2]
    E --> F[Combined = C[i].len + C[i+1].len]
    F --> G[MaxLen = max(MaxLen, Combined)]
    G --> E
    E -- End Loop --> H[Return MaxLen]
```

## 🧪 Edge Cases to Test

1.  **No Drops:** `1 2 3`. 1 chunk. Sum with "next" (0) -> 3. Correct.
2.  **All Drops:** `5 4 3 2 1`.
    - Chunks: `[5]`, `[4]`, `[3]`...
    - Max(1+1) = 2. Correct. `5 4` is valid (one drop). `5 4 3` (two drops).
3.  **Single Element:** `[1]`. Len 1.

## 🏃 Naive vs Optimal Approach

### Linear Scan O(N)

One pass to find drops and measure chunk lengths.
One pass to sum adjacent chunks.

- **Time:** O(N).
- **Space:** O(N) to store chunk lengths (or O(1) if on the fly).
