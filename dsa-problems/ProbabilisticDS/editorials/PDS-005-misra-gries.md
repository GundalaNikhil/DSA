---
problem_id: PDS_MISRA_GRIES__9624
display_id: PDS-005
slug: misra-gries
title: "Frequent Items with Misra-Gries"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - Streaming
  - Frequency Estimation
tags:
  - probabilistic-ds
  - misra-gries
  - streaming
  - medium
premium: true
subscription_tier: basic
---

# PDS-005: Frequent Items with Misra-Gries

## 📋 Problem Summary

We need to identify all elements in a stream of `n` items that appear more than `n/k` times.
- We must use the **Misra-Gries** algorithm.
- We are allowed to maintain at most `k-1` counters.
- The output should be the set of candidate items remaining in the counters after processing the stream.

## 🌍 Real-World Scenario

**Scenario Title:** Real-Time Traffic Analysis

Imagine you are monitoring a high-speed network link (100 Gbps).
- You want to identify IP addresses that are consuming a significant portion of the bandwidth (e.g., > 1%).
- There are billions of possible IP addresses, so you can't store a counter for each one.
- However, you know that there can be at most 99 IPs that consume > 1% of the bandwidth.
- **Misra-Gries** allows you to track these "heavy hitters" using a very small amount of memory (just 99 counters) with a guarantee that you won't miss any true heavy hitter.

**Why This Problem Matters:**

- **DDoS Detection:** Identifying IPs sending a flood of packets.
- **Search Trends:** Finding the most popular queries in a stream.
- **Financial Trading:** Identifying stocks with unusually high trade volume.

![Real-World Application](../images/PDS-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Misra-Gries Logic

Stream: `A B A C A D` (`k=3`, so we keep `k-1=2` counters).

1. **Read A:** Counters: `{A:1}`
2. **Read B:** Counters: `{A:1, B:1}` (Full)
3. **Read A:** Increment A. Counters: `{A:2, B:1}`
4. **Read C:** C is not in counters, and counters are full.
   - Decrement ALL counters.
   - `{A:1, B:0}` -> Remove B.
   - Counters: `{A:1}`
5. **Read A:** Increment A. Counters: `{A:2}`
6. **Read D:** Counters: `{A:2, D:1}`

Result Candidates: `{A, D}`.
Note: A appeared 3 times (50% of 6). D appeared 1 time.
Threshold `n/k = 6/3 = 2`. A is a true heavy hitter. D is a false positive candidate (which is allowed).

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - `n`: Stream length.
  - `k`: Parameter (threshold `n/k`).
  - Stream: List of integers.
- **Output:**
  - Sorted list of keys remaining in the map.
- **Algorithm:**
  - Maintain a map of size at most `k-1`.
  - If item `x` in map: increment count.
  - Else if map size < `k-1`: add `x` with count 1.
  - Else (map full): decrement ALL counts in map. Remove keys that drop to 0.

## Naive Approach

### Intuition

Store counts for ALL items in a hash map.

### Algorithm

1. Count everything.
2. Filter keys with count `> n/k`.

### Limitations

- **Space Complexity:** `O(N)` unique items. If stream has 1 billion unique items, this crashes memory.
- Misra-Gries uses `O(k)` space, which is tiny.

## Optimal Approach

### Key Insight

The Misra-Gries algorithm generalizes the Boyer-Moore Voting Algorithm (which finds a majority element `> n/2`).
- By decrementing `k` distinct elements at once (the new one + the `k-1` in the map), we "cancel out" groups of `k` distinct items.
- If an item appears `> n/k` times, it cannot be fully cancelled out.

### Algorithm

1. Initialize empty map `counts`.
2. For each item `x` in stream:
   - If `x` in `counts`: `counts[x]++`
   - Else if `counts.size() < k-1`: `counts[x] = 1`
   - Else:
     - Decrement all keys in `counts`.
     - Remove keys with value 0.
3. Extract keys from `counts`, sort them, and print.

### Time Complexity

- **O(n \cdot k)** if decrementing takes `O(k)`.
- Can be optimized to `O(n)` with advanced data structures, but `O(n * k)` is acceptable since `k` is small.

### Space Complexity

- **O(k)**.

![Algorithm Visualization](../images/PDS-005/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-005/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `7 3`, Stream `1 2 1 3 1 2 4`
`k=3`, capacity=2.

1. `1`: `{1:1}`
2. `2`: `{1:1, 2:1}`
3. `1`: `{1:2, 2:1}`
4. `3`: Full. Decr all. `{1:1, 2:0}` -> `{1:1}`.
5. `1`: `{1:2}`
6. `2`: `{1:2, 2:1}`
7. `4`: Full. Decr all. `{1:1, 2:0}` -> `{1:1}`.

Step 4: `3` arrives. Map `{1:2, 2:1}`. Decrement: `{1:1, 2:0}`. Remove 2. Map `{1:1}`.
Step 5: `1` arrives. Map `{1:2}`.
Step 6: `2` arrives. Map `{1:2, 2:1}`.
Step 7: `4` arrives. Map `{1:2, 2:1}`. Decrement: `{1:1, 2:0}`. Remove 2. Map `{1:1}`.

Result: `1`.

## ✅ Proof of Correctness

### Invariant
At any point, if we have processed `m` items and the counters are `C`, then for any item `j` with true frequency `f_j`, `f_j <= C[j] + D`, where `D` is the total amount of decrements performed.
Also `D <= (m - sum C)/k`.
This guarantees `f_j - C[j] <= m/k`.
If `f_j > m/k`, then `C[j] > 0`.

### Why the approach is correct
Standard Misra-Gries logic.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Space Saving Algorithm?
  - *Hint:* Similar to Misra-Gries but keeps the item with min count and replaces it. Better accuracy in practice.
- **Extension 2:** Distributed Heavy Hitters?
  - *Hint:* Merge summaries from multiple nodes. (Merge counters by adding).
- **Extension 3:** Weighted updates?
  - *Hint:* Generalizes naturally.

### Common Mistakes to Avoid

1. **Off-by-one**
   - ❌ Wrong: Using `k` counters when asked for `k-1`.
   - ✅ Correct: Capacity `k-1`.
2. **Decrement Logic**
   - ❌ Wrong: Decrementing only the new item.
   - ✅ Correct: Decrement ALL items (including the virtual new one, which effectively means ignoring the new one and decrementing existing ones).

## Related Concepts

- **Majority Element:** Special case where `k=2`.
- **Frequent Directions:** Matrix sketching.
