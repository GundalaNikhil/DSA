---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: "Pairwise XOR in Band With Index Parity"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Array
tags:
  - bitwise
  - xor
  - trie
  - counting
  - medium
premium: true
subscription_tier: basic
---

# BIT-004: Pairwise XOR in Band With Index Parity

## 📋 Problem Summary

Given an array and range `[L, U]`, count the number of index pairs `(i, j)` such that `i < j`, `i + j` is even, and the XOR sum `a[i] ^ a[j]` falls within `[L, U]`.

## 🌍 Real-World Scenario

**Scenario Title:** The Parity-Synchronized Network Mesh

You are building a mesh network where nodes are assigned IDs.

- **Link Condition**: Two nodes can form a secure link if their IDs, when XORed, produce a value within a specific "Signal Strength" range `[L, U]`.
- **Timing Constraint**: Links are time-slotted. Odd-numbered nodes operate in Phase 1, Even-numbered nodes in Phase 2. A link is valid only if both nodes operate in the same phase (i.e., both Odd or both Even indices). Note: `i+j` is even if and only if `i` and `j` have the same parity.
- **Goal**: Count the total valid potential links in the network.

**Why This Problem Matters:**

- **Trie Data Structure**: Standard tool for efficient prefix-based queries (XOR, strings).
- **Decomposition**: Breaking a complex condition (`i+j` even) into simpler structural properties (Same Parity).
- **Range counting**: Reducing `[L, U]` queries to `Count(<= U) - Count(<= L-1)`.

![Real-World Application](../images/BIT-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Trie Query

```
Query: Count y < x such that (x ^ y) <= K
x = 1011 (11)
K = 0101 (5)
Trie Root
|
|-- Bit 3 (K=0): Must match x(1). Go Right (1).
    |
    |-- Bit 2 (K=1):
        |-- Match x(0) -> XOR is 0 (< 1). All sub-nodes valid. Add Count.
        |-- Diff x(1) -> XOR is 1 (= 1). Continue to check lower bits.
            |
            ...
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Array `a`, integers `L` and `U`.
- **Condition `i+j` Even**: Means `i` and `j` are both Even or both Odd.
- **Pairs**: `(i, j)` with `i < j`. Order doesn't matter for value, but counting pairs once.

Common interpretation mistake:

- ❌ Trying to handle `i + j` even inside the Trie logic directly.
- ✅ Splitting the input array into two arrays (`even_indices` and `odd_indices`) and solving the problem for each independently.

### Core Concept: XOR Range Counting with Trie

To count pairs with `XOR <= K`, we use a Trie.
Iterate through numbers. For each number `x`:

1.  **Query**: How many numbers already in Trie satisfy `num ^ x <= K`?
2.  **Insert**: Add `x` to Trie.

`Count([L, U]) = Count(<= U) - Count(<= L-1)`.

### Why Naive Approach is too slow

Checking every pair is O(N²). N=100,000 means 10^10 operations, which is TLE.
Trie approach is O(N \* 30). 3 million ops. Fast.

## Naive Approach (Brute Force)

### Intuition

Double loop. Check conditions.

### Algorithm

1. `count = 0`
2. Loop `i` from 0 to `n-1`:
   - Loop `j` from `i+1` to `n-1`:
     - If `(i + j) % 2 == 0`:
       - `xor_val = a[i] ^ a[j]`
       - If `L <= xor_val <= U`: `count++`

### Time Complexity

- **O(N²)**.

### Space Complexity

- **O(1)**.

## Optimal Approach (Trie + Splitting)

### Key Insight

1. `(i + j) % 2 == 0` is equivalent to `i % 2 == j % 2`.
2. We can separate `a` into `evens` (elements at 0, 2, 4...) and `odds` (1, 3, 5...).
3. Solve the standard "Count Pairs with XOR <= K" problem for each list.
4. Total = `Solve(evens, L, U) + Solve(odds, L, U)`.
5. `Solve(arr, L, U) = Count(arr, U) - Count(arr, L - 1)`.

### Trie Logic for Count <= K

For a number `x` and limit `K`:

- Traverse bits 29 down to 0.
- `bitX`: bit of x. `bitK`: bit of K.
- We want `bitX ^ bitNode <= bitK`.
- **Case 1 (bitK == 0)**:
  - We MUST have `bitX ^ bitNode == 0` to not exceed K.
  - So `bitNode` must be `bitX`.
  - Go to child `bitX`. (If null, return current accumulated count? No, return 0 for this path).
- **Case 2 (bitK == 1)**:
  - Option A: `bitX ^ bitNode == 0`. This bit is strictly less than K (0 < 1). So ALL numbers in this subtree are valid regardless of lower bits. Add `count[child[bitX]]`.
  - Option B: `bitX ^ bitNode == 1`. This bit matches K (1 = 1). We need to check lower bits. Continue to child `!bitX` (1^bitX).

### Time Complexity

- **O(N \* 30)**.

### Space Complexity

- **O(N \* 30)** for Trie nodes.

![Algorithm Visualization](../images/BIT-004/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-004/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `2, 3, 1, 7` (Indices 0, 1, 2, 3). `L=1, U=4`.
**Split**:

- Evens: `[2, 1]` (Idx 0, 2)
- Odds: `[3, 7]` (Idx 1, 3)

**Processing Evens**: `[2, 1]`

1. Insert 2.
   - Query 1 for valid pairs (None).
   - Trie: `{2}`.
2. Process 1.
   - Query `1 ^ y <= 4`. `y=2`. `1^2=3`. `3 <= 4`. Valid.
   - Count += 1.
   - Query `1 ^ y <= 0` (L-1). `3 <= 0` False.
   - Net pairs: 1. `(2, 1)`.

**Processing Odds**: `[3, 7]`

1. Insert 3.
2. Process 7.
   - Query `7 ^ y <= 4`. `y=3`. `7^3=4`. `4 <= 4`. Valid.
   - Count += 1.
   - Query `7 ^ y <= 0`. False.
   - Net pairs: 1. `(3, 7)`.

**Total**: 1 + 1 = 2.
Matches Example.

## ✅ Proof of Correctness

### Invariant

The condition `i+j` is even strictly partitions the search space into independent problems. The Trie logic correctly counts elements strictly less than `k` whenever a bit differs from `k` in the "smaller" direction, and follows the "equal" path otherwise. Summing these counts covers all valid leaves.

## 💡 Interview Extensions (High-Value Add-ons)

- **Max XOR**: Related classic problem.
- **Dynamic Updates**: If elements are added/removed (Trie supports deletion easily).
- **Modulo parity**: `i+j % 3 == 0`? Split into 3 buckets `0, 1, 2`. Pairs `(0,0), (1,2)`.

## Common Mistakes to Avoid

1. **Memory**:
   - ❌ Creating a new Trie for every number.
   - ✅ One Trie per sub-problem.
2. **Bit Depth**:
   - ❌ Using 32 bits when input is small? Safe but slightly slower. 30 (up to 10^9) is standard.


