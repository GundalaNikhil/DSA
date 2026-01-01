---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Subarray
  - Trie
tags:
  - bitwise
  - xor
  - subarray
  - trie
  - medium
premium: true
subscription_tier: basic
---

# BIT-012: Distinct Subarray XORs

## 📋 Problem Summary

Count the number of **distinct** values obtained by XORing elements of all possible subarrays of `a`.

## 🌍 Real-World Scenario

**Scenario Title:** The Unique Interference Signatures

You are cataloging radio burst patterns.
- **Recording**: A continuous stream of signal samples `a[i]`.
- **Bursts**: A "burst" is any contiguous segment of time (subarray).
- **Signature**: The digital signature of a burst is the XOR sum of its samples.
- **Goal**: You want to build a database of all *unique* signatures seen in the recording. Duplicates don't add new information.
- **Challenge**: The recording is long (10,000 samples), so the number of bursts is huge (50 million). You need an efficient way to catalog them.

**Why This Problem Matters:**

- **Constraints Analysis**: `N=10,000` lies in the tricky zone where $O(N^2)$ is theoretically computation-feasible ($10^8$ ops) but memory-intensive ($10^8$ integers).
- **Memory Management**: Choosing `int[]` vs `HashSet` becomes critical.
- **Sorting vs Hashing**: Understanding tradeoffs for uniqueness checking.

![Real-World Application](../images/BIT-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Brute Force Collection
```
Array: [1, 2, 3]

Subarrays:
[1] -> 1
[2] -> 2
[3] -> 3
[1, 2] -> 1^2 = 3
[2, 3] -> 2^3 = 1
[1, 2, 3] -> 1^2^3 = 0

Results: {1, 2, 3, 3, 1, 0}
Distinct: {0, 1, 2, 3} -> Count 4.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: `a` size `N <= 10,000`.
- **Values**: Up to $10^9$.
- **Output**: Integer count.

Common interpretation mistake:

- ❌ Using Python `set` or Java `HashSet` blindly.
- ✅ realizing that for $N=10,000$, total subarrays $\approx 5 \times 10^7$. Storing this many objects in a Hash Set will cause Memory Limit Exceeded (MLE) or Time Limit Exceeded (TLE) due to overhead.
- ✅ Preferring Primitive Arrays + Sorting.

### Core Concept: Space-Efficient Counting

The total number of subarrays is $N(N+1)/2$.
For $N=10000$, this is $\approx 50,000,000$.
Storing 50 million integers takes $50 \times 10^6 \times 4$ bytes $\approx 200$ MB.
This fits in 256MB memory.
However, a `HashSet` node has overhead (pointers, object headers), easily 3-4x the size.
Thus, **collecting to a primitive array and sorting** is the viable approach.

## Naive Approach (HashSet)

### Intuition

Iterate all subarrays, add XORs to a Set.

### Algorithm

1. `Set<Integer> distinct`.
2. Loop `i` from 0 to `n-1`:
   - `curr = 0`.
   - Loop `j` from `i` to `n-1`:
     - `curr ^= a[j]`.
     - `distinct.add(curr)`.
3. Return `distinct.size()`.

### Time Complexity

- **O(N²)** on average, but overhead is high.

### Space Complexity

- **O(N²)**. High constant factor (MLE risk).

## Optimal Approach (Sorting Primitive Array)

### Key Insight

Use a raw integer array to store all XOR sums, then sort and count unique elements. In C++, `std::unique` is perfect. In Java, `Arrays.sort`. Iterating sorted array takes O(K).

### Algorithm

1. Allocate array `results` of size $N(N+1)/2$.
2. Fill array with XOR sums:
   - `idx = 0`
   - Loop `i` 0..n:
     - `curr = 0`
     - Loop `j` i..n:
       - `curr ^= a[j]`
       - `results[idx++] = curr`
3. Sort `results`.
4. Iterate to count unique elements.
   - `count = 0`
   - If `len > 0`, `count=1`.
   - Loop `k` from 1 to `len-1`:
     - `if results[k] != results[k-1]`: `count++`.
5. Return `count`.

### Time Complexity

- **O(N² log(N²))**. Sorting dominates.
- But sequential access is cache-friendly.

### Space Complexity

- **O(N²)**. Minimized constant factor.

![Algorithm Visualization](../images/BIT-012/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-012/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `1, 2, 3`.
1. i=0:
   - [1] -> 1
   - [1,2] -> 3
   - [1,2,3] -> 0
2. i=1:
   - [2] -> 2
   - [2,3] -> 1
3. i=2:
   - [3] -> 3
Array: `[1, 3, 0, 2, 1, 3]`.
Sorted: `[0, 1, 1, 2, 3, 3]`.
Unique: `0, 1, 2, 3`. Count 4.

## ✅ Proof of Correctness

### Invariant

We explicitly calculate every possible subarray XOR. The only optimization is using sorting to count distinct elements instead of a Hash Set to respect memory constraints. Correctness of logic is absolute.

## 💡 Interview Extensions (High-Value Add-ons)

- **Large N (10^5)**: Only possible if range of values is small, or number of distinct XORs is provably small (not generally true).
- **Trie**: Could insert into Trie to save space (deduplicates implicitly), but node overhead is also high.

## Common Mistakes to Avoid

1. **Memory Blowup**:
   - ❌ Doing `list.append` in a loop in interpreted languages for N=10000.
2. **Slow Sort**:
   - ❌ Bubble sort ($O(M^2)$) on the results array. M is $N^2$. Complexity $N^4$. Total disaster.
   - ✅ Use built-in Quicksort/Mergesort ($O(M \log M)$).

## Related Concepts

- **Radix Sort**: Could sort integers in linear time $O(M)$.
- **Space-Time Tradeoff**: Using sorting (time) to save map overhead (space).
