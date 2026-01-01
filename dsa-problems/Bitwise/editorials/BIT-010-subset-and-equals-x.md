---
problem_id: BIT_SUBSET_AND_EQUALS_X__8410
display_id: BIT-010
slug: subset-and-equals-x
title: "Subset AND Equals X"
difficulty: Medium
difficulty_score: 52
topics:
  - Bitwise Operations
  - AND
  - Subset
  - Dynamic Programming
tags:
  - bitwise
  - and-operation
  - subset
  - dp
  - medium
premium: true
subscription_tier: basic
---

# BIT-010: Subset AND Equals X

## 📋 Problem Summary

Given an array of integers and a target `X`, count the number of non-empty subsets such that the bitwise AND of the subset elements is exactly `X`.

## 🌍 Real-World Scenario

**Scenario Title:** The Strict Permission Group

You are analyzing access control lists (ACLs).
- **Users**: Each user has a set of permissions (bits set to 1).
- **Requirement**: You want to form a committee (subset of users).
- **Consensus**: The committee can only perform an action if *everyone* in the committee has the permission for it (Committee Permission = AND of User Permissions).
- **Goal**: You need to find how many ways you can form a committee such that the resulting set of actionable permissions is *exactly* `X`.
  - It must have *all* permissions in `X`.
  - It must *not* have any extra permissions common to everyone (consensus on `X` only).

**Why This Problem Matters:**

- **Parameter Constraints**: Recognizing that `N <= 20` allows exponential solutions ($O(2^N)$).
- **Filtering**: Pruning the search space by pre-checking validity.
- **Inclusion-Exclusion**: A key concept if `N` were larger.

![Real-World Application](../images/BIT-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Subset AND
```
Array: [6 (110), 4 (100), 2 (010)]
Target X = 2 (010)

Subsets:
- {6}: AND=6. No.
- {4}: AND=4. No.
- {2}: AND=2. Yes.
- {6, 4}: AND=4. No.
- {6, 2}: AND=2. Yes.
- {4, 2}: AND=0. No.
- {6, 4, 2}: AND=0. No.

Matches: {2}, {6, 2}. Total 2.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: `n` (up to 20), Array `a`, Target `X`.
- **Output**: Count of subsets.
- **Empty Subset**: Not counted.

Common interpretation mistake:

- ❌ Assuming `N` is large and trying complicated DP.
- ✅ Checking constraints first. `N=20` implies $2^{20} \approx 10^6$ ops, which fits in 2 seconds.

### Core Concept: Small N Iteration

When `N` is small (<= 20), iterating through all $2^N$ subsets is standard practice.
We can use a bitmask from `1` to `(1<<N) - 1` to represent each non-empty subset.

## Naive Approach (Bitmask Iteration)

### Intuition

Generate every subset, compute AND, check partial equality? No, check exact equality.

### Algorithm

1. `count = 0`.
2. Loop `mask` from 1 to `(1 << n) - 1`:
   - `current_and = -1` (All 1s)
   - Loop `i` from 0 to `n-1`:
     - If `(mask >> i) & 1`:
       - `current_and &= a[i]`
   - If `current_and == X`: `count++`
3. Return `count`.

### Time Complexity

- **O(N * 2^N)**.
- $20 \times 10^6 = 2 \times 10^7$ ops. Very safe.

### Space Complexity

- **O(1)**.

## Optimal Approach (Pre-filtering + Iteration)

### Key Insight

We can optimize slightly.
For a subset to have `AND == X`:
1. Every element MUST be a supermask of `X` (i.e. `(elem & X) == X`). If an element has a 0 where X has a 1, the total AND will have 0 there, failing the match.
2. The AND of the chosen elements must not have any *extra* bits set that are not in X.

### Algorithm

1. Filter `a`: keep only elements where `(v & X) == X`. Let this new list be `b`.
2. Iterate all subsets of `b`.
3. Compute AND. Check if `AND == X`.

This reduces the base of the exponent if many elements are incompatible.

**Alternative High-N Approach (Context)**:
If `N` was 100,000 but values were small ($< 2^{20}$), we would use **Sum Over Subsets (SOS) DP**.
`Count(AND=X) = Sum( (-1)^|S^X| * (2^{Freq[S]} - 1) )` for all `S` supermask of `X`.
But here, standard iteration is optimal.

### Time Complexity

- **O(N * 2^K)** where K is number of valid supermasks. Worst case **O(N * 2^N)**.

### Space Complexity

- **O(N)** for filtered list.

![Algorithm Visualization](../images/BIT-010/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-010/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `6, 4, 2`. `X=2`.
1. **Filter**:
   - 6 (110) & 2 (010) = 2 == 2. OK.
   - 4 (100) & 2 (010) = 0 != 2. Reject.
   - 2 (010) & 2 (010) = 2 == 2. OK.
   Candidates: `[6, 2]`.
2. **Subsets**:
   - `[6]` -> AND 6. (6 != 2).
   - `[2]` -> AND 2. (2 == 2). Count 1.
   - `[6, 2]` -> 6 & 2 = 2. (2 == 2). Count 2.
3. **Result**: 2.

## ✅ Proof of Correctness

### Invariant

We iterate all possible subsets of potentially valid candidates. Since we essentially brute force the check, correctness is guaranteed. The filter step is valid because any `v` such that `(v & X) != X` would force the result to have a 0 bit where X has a 1 bit, making equality impossible.

## 💡 Interview Extensions (High-Value Add-ons)

- **Large N (10^5)**: Use SOS DP (Sum Over Subsets).
- **Count Supermasks**: Simpler problem.

## Common Mistakes to Avoid

1. **All Subsets**:
   - ❌ Including empty subset (usually AND is undefined or -1).
   - ✅ Loop `mask` from 1.
2. **Filter Logic**:
   - ❌ Filtering `v & X != 0`.
   - ✅ Filtering `v & X == X`.

## Related Concepts

- **Sum Over Subsets (SOS) DP**: For scaling to large N.
- **Inclusion-Exclusion Principle**: For solving equations.
