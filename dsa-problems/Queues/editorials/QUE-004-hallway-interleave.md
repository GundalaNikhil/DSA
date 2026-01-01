---
problem_id: QUE_HALLWAY_INTERLEAVE__1582
display_id: QUE-004
slug: hallway-interleave
title: "Hallway Interleave"
difficulty: Easy
difficulty_score: 24
topics:
  - Queue
  - Interleaving
  - Simulation
tags:
  - queue
  - interleaving
  - easy
  - simulation
premium: true
subscription_tier: basic
---

# QUE-004: Hallway Interleave

## 📋 Problem Summary

We are given a queue of even length `N`. We need to interleave the first half with the second half.
- Input: `[a1, a2, ..., an, b1, b2, ..., bn]`
- Output: `[a1, b1, a2, b2, ..., an, bn]`

## 🌍 Real-World Scenario

**Scenario Title:** Zipper Merge in Traffic

Imagine two lanes of traffic merging into one.
- Lane A has cars `[A1, A2, A3]`.
- Lane B has cars `[B1, B2, B3]`.
- To merge efficiently and fairly, drivers use the "Zipper Method".
- One car from A goes, then one from B, then A, then B.
- Result: `[A1, B1, A2, B2, A3, B3]`.
- This maximizes throughput and minimizes road rage!

**Why This Problem Matters:**

- **Audio Processing:** Interleaving left and right audio channels for stereo sound.
- **Data Transmission:** Interleaving bits for error correction (burst error protection).
- **Card Shuffling:** A perfect "riffle shuffle".

![Real-World Application](../images/QUE-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Interleaving Process

Input: `[11, 12, 13, 14]` (`N=4`).
Half size = 2.

1. **Split:**
   Half 1: `[11, 12]`
   Half 2: `[13, 14]`

2. **Merge:**
   - Take from Half 1: `11`
   - Take from Half 2: `13`
   - Take from Half 1: `12`
   - Take from Half 2: `14`

Result: `[11, 13, 12, 14]`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Even integer `N`, array of values.
- **Output:** Interleaved array.
- **Constraint:** `N` is always even.

## Naive Approach

### Intuition

Use two separate queues.

### Algorithm

1. Create `Q1` and `Q2`.
2. Enqueue first `N/2` elements to `Q1`.
3. Enqueue remaining `N/2` elements to `Q2`.
4. While queues are not empty:
   - Dequeue from `Q1`, add to result.
   - Dequeue from `Q2`, add to result.

### Limitations

- **Space Complexity:** `O(N)` for auxiliary queues.
- **Time Complexity:** `O(N)`.
- This is actually a very good approach, just uses extra space.

## Optimal Approach

### Key Insight

Since we are given the input as an array (random access), we can construct the result directly using indices without explicit queues.

### Algorithm

1. `mid = n / 2`.
2. Create `result` array of size `N`.
3. Loop `i` from 0 to `mid - 1`:
   - `result[2*i] = values[i]` (From first half)
   - `result[2*i + 1] = values[mid + i]` (From second half)
4. Return `result`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** for the result.

![Algorithm Visualization](../images/QUE-004/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-004/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `11 12 13 14` (`N=4`)
1. `mid = 2`.
2. `i=0`:
   - `result[0] = values[0] = 11`.
   - `result[1] = values[2] = 13`.
3. `i=1`:
   - `result[2] = values[1] = 12`.
   - `result[3] = values[3] = 14`.
4. Result: `[11, 13, 12, 14]`.

Matches example.

![Example Visualization](../images/QUE-004/example-1.png)

## ✅ Proof of Correctness

### Invariant
The element at index `i` in the first half lands at `2*i`. The element at index `i` in the second half lands at `2*i + 1`.

### Why the approach is correct
This mapping `i -> 2i` and `mid+i -> 2i+1` is the definition of interleaving.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Interleave using only a Stack and Queue?
  - *Hint:* This is a classic problem. Push first half to stack. Interleave stack and queue. Reverse stack. Interleave again. (Requires multiple passes).
- **Extension 2:** In-place Interleave?
  - *Hint:* Extremely hard. Requires cycle leader algorithm (similar to in-place matrix transpose).

### Common Mistakes to Avoid

1. **Index Out of Bounds**
   - ❌ Wrong: Loop `i` from 0 to `n`.
   - ✅ Correct: Loop `i` from 0 to `mid - 1`.
2. **Odd Length**
   - ❌ Wrong: Assuming `n` is odd.
   - ✅ Correct: Problem guarantees `n` is even.

## Related Concepts

- **Perfect Shuffle:** The mathematical name for this operation.
- **Merge Sort:** The merge step is similar (but sorted).
