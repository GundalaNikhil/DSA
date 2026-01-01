---
problem_id: NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821
display_id: NUM-001
slug: classroom-gcd-prefix-queries
title: "Classroom GCD Prefix Queries"
difficulty: Easy
difficulty_score: 25
topics:
  - Number Theory
  - GCD
  - Prefix Computation
tags:
  - number-theory
  - gcd
  - prefix
  - easy
premium: true
subscription_tier: basic
---

# NUM-001: Classroom GCD Prefix Queries

## 📋 Problem Summary

Given an array of numbers, efficiently answer multiple queries asking for the Greatest Common Divisor (GCD) of the prefix ending at index `r`.
- Input: Array `A`, multiple queries `r`.
- Output: `GCD(A[0], A[1], dots, A[r])` for each query.

## 🌍 Real-World Scenario

**Scenario Title:** The Supply Distributor

Imagine you are a logistics manager for a school district. You have a sequence of classrooms, and each classroom needs a certain number of identical supply kits (e.g., 12 notebooks, 18 pencils, 6 erasers).
- You want to package these supplies into standard boxes such that every classroom receives an integer number of boxes.
- The number of items in a box must divide the requirement of every classroom in the group you are serving.
- To maximize efficiency, you want the largest possible box size (GCD).
- As you add more classrooms to your delivery route (extending the prefix), the box size might need to shrink to accommodate the new requirements. You need to quickly know the optimal box size for the first `r` classrooms.

**Why This Problem Matters:**

- **Cryptography:** GCD is fundamental to RSA and other encryption algorithms.
- **Data Compression:** Finding common patterns or periods in data streams.
- **Resource Allocation:** Distributing resources fairly in discrete chunks.

![Real-World Application](../images/NUM-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Prefix GCD

Consider array: `[12, 18, 6, 8]`

```
Index: 0   1   2   3
Value: 12  18  6   8

Prefix GCDs:
P[0] = gcd(12) = 12
P[1] = gcd(12, 18) = 6
P[2] = gcd(6, 6) = 6
P[3] = gcd(6, 8) = 2
```

Notice that the prefix GCD is **non-increasing**. It can only stay the same or decrease as we include more numbers.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `N, Q <= 200,000`. This means an `O(N * Q)` solution will time out. We need `O(N)` precomputation and `O(1)` per query.
- **Values:** Integers can be negative. GCD is always positive. `gcd(a, b) = gcd(|a|, |b|)`.
- **Zero:** `gcd(x, 0) = |x|`. `gcd(0, 0) = 0`.

### Core Concept: Prefix Array

Just like a prefix sum array allows `O(1)` range sum queries, a prefix GCD array allows `O(1)` prefix GCD queries.
`P[i] = gcd(P[i-1], A[i])`.

## Naive Approach

### Intuition

For each query `r`, iterate from `0` to `r` and compute the GCD.

### Algorithm


### Time Complexity

- **O(Q \cdot N \cdot \log(\text{max\_val}))**.
- With `N, Q = 2 * 10^5`, this is roughly `4 * 10^10` operations, which is way too slow (limit is usually `10^8`).

### Space Complexity

- **O(1)** (excluding input).

## Optimal Approach

### Key Insight

Since the queries are always about prefixes `A[0 dots r]`, we can precompute the answers.
Define `prefix_gcd[i]` as the GCD of all elements from index 0 to `i`.
`prefix_gcd[i] = gcd(prefix_gcd[i-1], A[i])`.

### Algorithm

1. Create an array `pref` of size `N`.
2. Set `pref[0] = abs(A[0])`.
3. Iterate `i` from 1 to `N-1`:
   - `pref[i] = gcd(pref[i-1], abs(A[i]))`.
4. For each query `r`, return `pref[r]`.

### Time Complexity

- **Precomputation:** `O(N * log(max_val))`.
- **Query:** `O(1)`.
- **Total:** `O((N + Q) * log(max_val))`. This fits easily within 2 seconds.

### Space Complexity

- **O(N)** to store the prefix array.

![Algorithm Visualization](../images/NUM-001/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-001/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [12, 18, 6]`, Queries: `0, 1, 2`.

1. **Initialization:**
   - `pref` array of size 3.
   - `pref[0] = abs(12) = 12`.

2. **Iteration 1 (i=1):**
   - `pref[1] = gcd(pref[0], abs(18)) = gcd(12, 18)`.
   - Divisors of 12: 1, 2, 3, 4, 6, 12.
   - Divisors of 18: 1, 2, 3, 6, 9, 18.
   - Largest common is 6.
   - `pref[1] = 6`.

3. **Iteration 2 (i=2):**
   - `pref[2] = gcd(pref[1], abs(6)) = gcd(6, 6)`.
   - `pref[2] = 6`.

4. **Queries:**
   - `r=0`: Return `pref[0]` -> **12**.
   - `r=1`: Return `pref[1]` -> **6**.
   - `r=2`: Return `pref[2]` -> **6**.

Matches example output.

## ✅ Proof of Correctness

### Invariant
At index `i`, `pref[i]` stores the GCD of all elements from `A[0]` to `A[i]`.
Base case: `pref[0] = A[0]` holds.
Inductive step: If `pref[i-1] = gcd(A[0]...A[i-1])`, then `pref[i] = gcd(pref[i-1], A[i]) = gcd(gcd(A[0]...A[i-1]), A[i]) = gcd(A[0]...A[i])` by the associative property of GCD.

### Why the approach is correct
The problem asks for prefix GCDs. Since GCD is associative, we can compute them incrementally in a single pass.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Range GCD Queries (Sparse Table / Segment Tree).
  - *Question:* What if queries are for arbitrary ranges `[L, R]`?
  - *Answer:* Use a Sparse Table for `O(1)` queries (since GCD is idempotent) or a Segment Tree for `O(log N)` queries with updates.
- **Extension 2:** Dynamic Updates.
  - *Question:* What if we update `A[i]`?
  - *Answer:* Segment Tree allows point updates and range queries in `O(log N)`.
- **Extension 3:** Number of distinct prefix GCDs.
  - *Question:* How many unique values can the prefix GCD array contain?
  - *Answer:* At most `O(log(max A))`, because each time the GCD changes, it must decrease by a factor of at least 2.

### Common Mistakes to Avoid

1. **Negative Numbers**
   - ❌ Wrong: `gcd(-12, 18)` might return -6 in some languages or be undefined.
   - ✅ Correct: Always use `abs()` before computing GCD.
2. **Zero Handling**
   - ❌ Wrong: `gcd(0, 0)` might crash.
   - ✅ Correct: Ensure your GCD function handles 0 correctly (usually returns 0).
3. **Time Complexity**
   - ❌ Wrong: Recomputing GCD for each query (`O(N * Q)`).
   - ✅ Correct: Precompute in `O(N)`.

## Related Concepts

- **Euclidean Algorithm:** The standard way to compute GCD.
- **Prefix Sums:** Similar concept for summation.
- **Associative Property:** Allows incremental computation.
