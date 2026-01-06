---
problem_id: ARR_SUB_XOR_RANK__5991
display_id: ARR-033
slug: subarray-xor-rank
title: "Subarray XOR Rank Queries"
difficulty: Hard
difficulty_score: 60
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - k-th-element
  - searching
  - technical-interview-prep
  - two-pointers
  - xor
premium: false
subscription_tier: basic
---

# ARR-033: Subarray XOR Rank Queries

## 📋 Problem Summary

Consider all `N*(N+1)/2` subarrays.
Calculate their XOR sums.
Find the `K`-th smallest XOR sum.

## 🌍 Real-World Scenario

**Scenario Title:** 🔐 The Key Enumeration

### The Problem

A cryptographic system generates `N^2` possible session keys by XORing contiguous blocks of a master key stream.
You want to attack the system by trying the "weakest" (smallest value) keys first.
You need to find the `K`-th smallest key to prioritize your brute-force queue.

### Real-World Relevance

- **Signal Processing:** Analyzing noise characteristics distribution.

## 🚀 Detailed Explanation

### 1. XOR Prefix Property

`XOR(i..j) = PrefixXOR[j] ^ PrefixXOR[i-1]`.
So the problem transforms:
Given an array `P` (prefix XORs including 0), find `K`-th smallest value of `P[j] ^ P[i]` where `0 <= i < j <= N`.
(Basically pairwise XORs).

### 2. Binary Search on Answer

We can binary search for the answer `X`.
Predicate `CountPairsLessOrEqual(X)`:

- Count how many pairs `(i, j)` exist such that `P[i] ^ P[j] <= X`.
- If `Count >= K`, then the answer is `<= X`.
- Else, answer `> X`.

### 3. Counting Pairs with Trie

How to count pairs with XOR <= X?

- Insert all `P` values into a **Binary Trie**.
- For each `P[j]`, query the Trie: "How many values currently in Trie, when XORed with P[j], are <= X?"
- Then Insert `P[j]` into Trie.
- Sum these counts.

Query Trie Logic:

- Traverse bits from MSB (30 down to 0).
- Let `target bit` be `T`, `current P bit` be `B`.
- We want `B ^ NodeBit <= T`.
- If `T == 1`:
  - `B ^ NodeBit = 0` is definitely smaller! So we add ALL counts from the child that gives 0 (child `B`), and we recurse into the child that gives 1 (child `!B`) to see how many match the '1' bit constraint.
- If `T == 0`:
  - `B ^ NodeBit` MUST be 0. We cannot allow 1. So we strictly recurse into the child that gives 0 (child `B`). The other child is invalid (too big).

Wait. `i < j`.
Standard Trie approach sums pairs. We can process sequentially:

- Init Trie with `0` (PrefixXOR[-1]).
- For j=0 to N-1:
  - `val = PrefixXOR[j]`.
  - `cnt = Query(val, X)`.
  - Add `cnt` to total.
  - Insert `val` into Trie.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Calculate Prefix XORs]
    B --> C[BinSearch Range [0, MaxPossibleXOR]]
    C --> D[Mid = (Low + High) / 2]
    D --> E{CountPairs(<= Mid) >= K?}
    E -- Yes --> F[Ans = Mid, High = Mid - 1]
    E -- No --> G[Low = Mid + 1]
    F --> C
    G --> C
    C -- End Loop --> H[Return Ans]
```

## 🧪 Edge Cases to Test

1.  **K outside range:** Substring count is `N(N+1)/2`.
2.  **Duplicate P values:** Trie nodes usually store a `count`.
3.  **Large Values:** Up to `10^9` means 30 bits.

## 🏃 Naive vs Optimal Approach

### Naive O(N^2 log N)

Generate all, sort. TLE.

### Trie + Binary Search O(N log(MaxVal) \* log(MaxVal))

- Outer BS: 30 steps.
- Inner Count: N queries on Trie depth 30. `30 * N`.
- **Total:** `O(30 * 30 * N)` ~ `900 N`. Very Fast.
- **Space:** `O(N * 30)` for Trie.
  Optimal.
