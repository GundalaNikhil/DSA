---
problem_id: ARR_TEMP_OFFLINE_RANGES__5631
display_id: ARR-004
slug: lab-temperature-offline-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 46
topics:
  - Arrays
  - Difference Array
  - Prefix Sum
tags:
  - arrays
  - difference-array
  - prefix-sum
  - medium
premium: true
subscription_tier: basic
---

# ARR-004: Lab Temperature Offline Ranges

## 📋 Problem Summary

Given an initial array and a sequence of operations where **all range updates come before all range sum queries**, efficiently apply the updates and then answer the sum queries.

## 🌍 Real-World Scenario

**Scenario Title:** The overnight Lab Calibration

A research laboratory runs a long array of incubators.
During the night, an automated system applies a series of calibration steps.
- "Increase temperature by 5°C for incubators 10 to 50."
- "Decrease temperature by 2°C for incubators 30 to 80."

In the morning, the scientists arrive and need to check the total heat energy in various sectors to ensure safety.
- "What is the total temperature sum for incubators 0 to 100?"

By processing the "offline" updates efficiently (using a difference array) instead of updating the array one by one, the system saves massive computation time.

**Why This Problem Matters:**

- **Batch Processing**: Many systems buffer updates to apply them in bulk (e.g., database writes, screen rendering).
- **Difference Arrays**: A powerful technique for applying O(1) range updates.
- **Prefix Sums**: The standard tool for O(1) range queries.

![Real-World Application](../images/ARR-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Difference Array Mechanics
```
Array:   [0, 0, 0, 0, 0]
Update: Add 5 to [1, 3]

Diff:    [0, +5, 0, 0, -5, 0]
Indices:  0   1  2  3   4  5

Reconstruct:
idx 0: 0
idx 1: 0 + 5 = 5
idx 2: 5 + 0 = 5
idx 3: 5 + 0 = 5
idx 4: 5 - 5 = 0

Result:  [0, 5, 5, 5, 0]
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Offline Constraint**: All `add`s happen first. This is crucial! It allows us to defer the array reconstruction until all updates are logged.
- **Range Definitions**: `l` and `r` are inclusive.
- **Large Values**: Temperatures and sums can exceed 32-bit integer limits. Use `long` (64-bit).

Common interpretation mistake:

- ❌ Updating the array immediately for every `add` query (O(N) per query).
- ✅ Recording updates in a difference array and applying them once (O(1) per query + O(N) reconstruction).

### Core Concept: Difference Array + Prefix Sum

1. **Difference Array**: Allows applying range updates `[l, r]` in O(1) time by modifying only `diff[l]` and `diff[r+1]`.
2. **Prefix Sum**: After reconstruction, allows answering range sum queries `[l, r]` in O(1) time.

### Why Naive Approach is too slow

If we have `Q` queries and `N` elements:
- Updating range `[l, r]` naively takes O(N).
- `Q` updates take O(Q * N).
- With N, Q = 100,000, `N*Q` = 10^10 operations. This is way too slow (limit is ~10^8).

## Naive Approach

### Intuition

Just simulate exactly what the problem says. Loop through the array for every update.

### Algorithm

1. For each `add l r x`:
   - Loop `i` from `l` to `r`.
   - `temps[i] += x`
2. For each `sum l r`:
   - Loop `i` from `l` to `r`.
   - `total += temps[i]`

### Time Complexity

- **O(Q * N)**: Worst case (all full range).

### Space Complexity

- **O(1)**: In-place updates.

### Limitations

- **TLE**: Time Limit Exceeded for large inputs.

## Optimal Approach (Difference Array)

### Key Insight

Since we don't need intermediate answers, we can record the *start* and *end* of each temperature change.
`diff[i]` stores the change in value between `arr[i]` and `arr[i-1]`.
Update `[l, r]` by `x`:
- `diff[l] += x` (Value increases by x starting at l)
- `diff[r+1] -= x` (Value stops increasing by x after r)

### Algorithm

1. Create `diff` array of size `N + 1`, initialized to 0.
2. For each `add l r x` query:
   - `diff[l] += x`
   - `diff[r+1] -= x`
3. **Reconstruct Array**:
   - `current_val = temps[i]`
   - `running_add = 0`
   - For `i` from 0 to `N-1`:
     - `running_add += diff[i]`
     - `final_temps[i] = temps[i] + running_add`
4. **Build Prefix Sums** of `final_temps`:
   - `P[0] = 0`
   - `P[i+1] = P[i] + final_temps[i]`
5. For each `sum l r` query:
   - result = `P[r+1] - P[l]`

### Time Complexity

- **O(N + Q)**:
  - Processing updates: O(Q_add)
  - Reconstruction: O(N)
  - Prefix Sum build: O(N)
  - Processing sums: O(Q_sum)
  - Total: Linear with respect to input size.

### Space Complexity

- **O(N)**: For `diff` array and `prefix_sum` array.

### Why This Is Optimal

O(N + Q) is the lower bound as we must read the input.

![Algorithm Visualization](../images/ARR-004/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-004/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `temps=[1, 2, 3]`, `add 0 1 5`, `add 2 2 -1`, `sum 0 2`, `sum 1 2`

1. **Difference Array (init 0, size 4)**:
   - `add 0 1 5`: `diff[0]+=5`, `diff[2]-=5`. `[5, 0, -5, 0]`
   - `add 2 2 -1`: `diff[2]+= -1`, `diff[3]-= -1 (ignored)`. `[5, 0, -6, 0]`

2. **Reconstruction**:
   - `i=0`: `cur+=5` -> 5. `final = 1 + 5 = 6`. `P[1]=6`
   - `i=1`: `cur+=0` -> 5. `final = 2 + 5 = 7`. `P[2]=6+7=13`
   - `i=2`: `cur+=-6` -> -1. `final = 3 + (-1) = 2`. `P[3]=13+2=15`
   - Final Array: `[6, 7, 2]`
   - Prefix Sums: `[0, 6, 13, 15]`

3. **Queries**:
   - `sum 0 2`: `P[3] - P[0] = 15 - 0 = 15`.
   - `sum 1 2`: `P[3] - P[1] = 15 - 6 = 9`.

**Output**: `15 9` matches example.

![Example Visualization](../images/ARR-004/example-1.png)

## ✅ Proof of Correctness

### Invariant

`diff[i]` correctly stores the change of accumulation relative to `i-1`. Prefix summing `diff` gives total accumulated additions at step `i`. Prefix summing that result gives range sums.

### Why the approach is correct

Linearly combining operations is associative. Pre-calculating total changes then applying them is mathematically equivalent to applying them one by one, but much faster.

## 💡 Interview Extensions (High-Value Add-ons)

- **Online Updates**: What if `add` and `sum` are intermixed? (A: Segment Tree or Fenwick Tree/Binary Indexed Tree).
- **2D Arrays**: Range updates on a grid? (A: 2D Difference Array, `diff[r1][c1]++, diff[r2+1][c1]--, ...`).

## Common Mistakes to Avoid

1. **Order of Operations**:
   - ❌ Answering sums before all adds are processed.
   - ✅ Check boolean flags or split loops.

2. **IndexOutOfBounds**:
   - ❌ Accessing `diff[n]` without allocating size `n+1`.
   - ✅ Always alloc `n+1` for difference arrays to handle `r+1` seamlessly (or add `if` check).

3. **Integer Overflow**:
   - ❌ Using `int` for prefix sums.
   - ✅ `10^5 * 10^9` fits in `long` / `int64`.

## Related Concepts

- **Fenwick Tree**: Online version of this problem.
- **Segment Tree**: Handling more complex range queries.
- **Scanline Algorithm**: Similar "events at points" logic.
