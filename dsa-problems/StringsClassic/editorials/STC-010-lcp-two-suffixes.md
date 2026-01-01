---
problem_id: STC_LCP_TWO_SUFFIXES__5381
display_id: STC-010
slug: lcp-two-suffixes
title: "Longest Common Prefix of Two Suffixes"
difficulty: Medium
difficulty_score: 52
topics:
  - Strings
  - Suffix Array
  - RMQ
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
---

# STC-010: Longest Common Prefix of Two Suffixes

## 📋 Problem Summary

Given a string `s`, you need to answer multiple queries. Each query consists of two indices `i` and `j`. You must return the length of the **Longest Common Prefix (LCP)** between the suffix starting at `i` and the suffix starting at `j`. The solution must be efficient enough to handle up to 100,000 queries.

## 🌍 Real-World Scenario

**Scenario Title:** Version Control Diffing

In version control systems like Git, we often need to compare different versions of a file. Finding common blocks of code between two versions is essential for generating "diffs". If we concatenate the two file versions into a single string, finding the longest common prefix between suffixes starting at different positions helps identify identical code blocks that have been moved or copied. This is a fundamental operation in efficient delta compression and diff algorithms.

**Why This Problem Matters:**

- **Efficiency:** Naive comparison is O(N) per query, leading to O(NQ) total. We need O(1) per query.
- **LCA in Trees:** This problem is equivalent to finding the Lowest Common Ancestor (LCA) in a Suffix Tree, which is a classic application of RMQ (Range Minimum Query).

![Real-World Application](../images/STC-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "banana"`.
Suffix Array `sa`: `[5, 3, 1, 0, 4, 2]` ("a", "ana", "anana", "banana", "na", "nana")
LCP Array: `[1, 3, 0, 0, 2]` (between adjacent suffixes in sorted order)

Query: `i=1` ("anana"), `j=3` ("ana").
Ranks:
`rank[1]` (for "anana") is index 2 in SA.
`rank[3]` (for "ana") is index 1 in SA.

We need the minimum LCP value in the range between rank 1 and rank 2 in the sorted order.
Range `[1, 1]` (since we query `min(lcp[min_rank...max_rank-1])`).
`lcp[1] = 3`.
Answer: 3.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Indices:** `i` and `j` are 0-based indices in the original string.
- **Same Index:** If `i == j`, the LCP is the length of the suffix itself (`n - i`).
- **Constraints:** `N, Q <= 100,000`. Preprocessing O(N log N) is fine. Query O(1) is required.

## Naive Approach

### Intuition

For each query `(i, j)`, simply compare characters `s[i+k]` and `s[j+k]` until a mismatch.

### Algorithm

1. For each query `(i, j)`:
2. Loop `k` from 0.
3. While `s[i+k] == s[j+k]`, increment `k`.
4. Return `k`.

### Time Complexity

- **O(N * Q)**: In worst case (e.g., `s="aaaa..."`), each query takes O(N).
- Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach (SA + LCP + RMQ)

### Key Insight

The LCP of any two suffixes `u` and `v` is the minimum value in the LCP array between their positions in the Suffix Array.
Specifically, if `rank[u] < rank[v]`, then `LCP(u, v) = min(lcp[rank[u]], lcp[rank[u]+1], ..., lcp[rank[v]-1])`.
This is a classic **Range Minimum Query (RMQ)** problem.
We can use a **Sparse Table** to preprocess the LCP array in O(N log N) time and answer RMQ queries in O(1) time.

### Algorithm

1. **Build Suffix Array (SA)** and **Rank Array**.
2. **Build LCP Array** using Kasai's algorithm.
3. **Build Sparse Table** on the LCP array.
   - `st[k][i]` stores the minimum value in `lcp[i...i + 2^k - 1]`.
4. **Answer Queries**:
   - Get ranks `r1 = rank[i]`, `r2 = rank[j]`.
   - If `r1 == r2`, return `n - i`.
   - Ensure `r1 < r2`. If not, swap.
   - Query RMQ on range `[r1, r2 - 1]`. Note the `-1` because `lcp[k]` describes the overlap between `sa[k]` and `sa[k+1]`. The interval between `r1` and `r2` involves `lcp[r1], lcp[r1+1]...lcp[r2-1]`.

### Time Complexity

- **Preprocessing:** O(N log N) for SA and Sparse Table.
- **Query:** O(1).
- **Total:** O((N + Q) log N) or O(N log N + Q).

### Space Complexity

- **O(N log N)**: For the Sparse Table.

![Algorithm Visualization](../images/STC-010/algorithm-visualization.png)
![Algorithm Steps](../images/STC-010/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

`s = "banana"`
SA: `[5, 3, 1, 0, 4, 2]`
LCP: `[1, 3, 0, 0, 2]`
Ranks: `rank[0]=3`, `rank[1]=2`, `rank[2]=5`, `rank[3]=1`, `rank[4]=4`, `rank[5]=0`.

Query `(1, 3)`:
`r1 = rank[1] = 2`
`r2 = rank[3] = 1`
Swap: `r1=1, r2=2`.
Query RMQ on `lcp[1...1]`.
`lcp[1] = 3`.
Answer: 3. Correct ("ana").

Query `(0, 2)`:
`r1 = rank[0] = 3`
`r2 = rank[2] = 5`
Query RMQ on `lcp[3...4]`.
`lcp[3]=0`, `lcp[4]=2`. Min is 0.
Answer: 0. Correct.

![Example Visualization](../images/STC-010/example-1.png)

## ✅ Proof of Correctness

### Invariant

The LCP of any two suffixes `u` and `v` is the minimum LCP value in the interval between their ranks in the sorted Suffix Array.
This is a fundamental property of Suffix Arrays.
Since we query the range `[min_rank, max_rank - 1]`, we cover all adjacent LCP values between the two suffixes. The minimum of these adjacent LCPs is the LCP of the endpoints.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Longest Common Substring of K Strings**
  - Concatenate all strings with unique separators. Build SA/LCP. Use sliding window + RMQ.

- **Extension 2: Dynamic Updates**
  - If string changes, SA/LCP is hard to update. Suffix Tree or dynamic string structures are needed.

### Common Mistakes to Avoid

1. **Query Range Error**
   - ❌ Querying `[r1, r2]`.
   - ✅ Querying `[r1, r2 - 1]`. The LCP array has size `N-1`. `lcp[k]` is between `sa[k]` and `sa[k+1]`.

2. **Rank vs Index**
   - ❌ Using `i` and `j` directly in RMQ.
   - ✅ Must map to `rank[i]` and `rank[j]`.

3. **Sparse Table Size**
   - ❌ Not allocating enough rows for `log N`.
   - ✅ `K = floor(log2(N))`.

## Related Concepts

- **LCA**: Lowest Common Ancestor in trees.
- **Cartesian Tree**: Can convert RMQ to LCA.
- **Segment Tree**: Alternative to Sparse Table (O(N) build, O(log N) query, but supports updates).
