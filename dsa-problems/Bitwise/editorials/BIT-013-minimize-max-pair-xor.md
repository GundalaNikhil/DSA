---
problem_id: BIT_MINIMIZE_MAX_PAIR_XOR__8413
display_id: BIT-013
slug: minimize-max-pair-xor
title: "Minimize Max Pair XOR"
difficulty: Medium
difficulty_score: 58
topics:
  - Bitwise Operations
  - XOR
  - Dynamic Programming
  - Pairing
tags:
  - bitwise
  - xor
  - dp
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# BIT-013: Minimize Max Pair XOR

## 📋 Problem Summary

Given `n` integers (where `n` is even), partition them into `n/2` pairs such that the maximum XOR value among all pairs is minimized.

## 🌍 Real-World Scenario

**Scenario Title:** The Frequency Pairing

You are configuring a set of `n` transceivers.
- **Interference:** When two transceivers operate as a locked pair, they generate interference proportional to the XOR of their frequency IDs.
- **Goal:** You must pair up all devices.
- **Constraint:** The system's stability is determined by the *worst-case* interference in the network (the maximum interference among all pairs).
- **Optimization:** Find a pairing strategy that minimizes this peak interference.

**Why This Problem Matters:**

- **Min-Max Optimization:** A classic objective function.
- **Matching:** General matching on a complete graph with edge weights.
- **Bitmask DP:** Standard technique for small `N` constraints ($N \le 20$).

![Real-World Application](../images/BIT-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Pairing Choices
```
Array: [1, 2, 3, 4]

Option 1: (1, 2), (3, 4)
  1^2 = 3
  3^4 = 7
  Max = 7

Option 2: (1, 3), (2, 4)
  1^3 = 2
  2^4 = 6
  Max = 6

Option 3: (1, 4), (2, 3)
  1^4 = 5
  2^3 = 1
  Max = 5

Minimum of Maxs = 5. Best Pairing: (1, 4) and (2, 3).
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer `n` (even, up to 16) and array `a`.
- **Output**: The minimized maximum XOR value.
- **Pairing**: Proper partition (every element used exactly once).

Common interpretation mistake:

- ❌ Trying a greedy approach (e.g., sorting). Sorting works for minimizing sum of XORs sometimes, or simple diffs, but Min-Max XOR is non-monotonic.
- ✅ Recognizing `N=16` implies $O(2^N \cdot N)$ or similar exponential complexity.

### Core Concept: Component Processing

We construct the solution set incrementally.
State: `mask` representing the set of elements already paired.
Transition:
1. Pick the smallest index `i` not yet in `mask` (to avoid redundant permutations).
2. Try pairing `i` with every other available index `j`.
3. `Cost = max(a[i] ^ a[j], solve(mask + i + j))`.
4. Minimize this `Cost` over all choices of `j`.

### Why Naive Approach is too slow

Naive permutation testing is $O(N!)$. For $N=16$, $16! \approx 2 \times 10^{13}$. Too slow.
However, we only care about *pairings*, which is $(N-1)!! = 15 \times 13 \times \dots 1 \approx 2 \times 10^6$. This is actually acceptable!
Memoization just makes it safer ($2^{16} = 65536$ states).

## Naive Approach (Backtracking)

### Intuition

Recursively try all pairings for the first available number.

### Algorithm

1. Find first unused `i`.
2. Loop `j` > `i` that is unused.
3. Recurse.
4. Return min.

### Time Complexity

- **O((N-1)!!)**.

### Space Complexity

- **O(N)** recursion stack.

## Optimal Approach (Bitmask DP)

### Key Insight

Use a bitmask to memoize states. Since order of pairs doesn't matter, we always pick the lowest available index `i` to pair next. This fixes the order and avoids counting `(A,B), (C,D)` and `(C,D), (A,B)` separately.

### Algorithm

1. `memo` array of size $2^N$, init with -1.
2. `solve(mask)`:
   - If `mask == (1<<n) - 1`: return 0.
   - If `memo[mask]` exists: return it.
   - Find first unset bit `i`.
   - `res = Infinity`.
   - Loop `j` from `i+1` to `n-1`:
     - If `j` is unset:
       - `current_pair_xor = a[i] ^ a[j]`.
       - `sub_res = solve(mask | (1<<i) | (1<<j))`.
       - `res = min(res, max(current_pair_xor, sub_res))`.
   - `memo[mask] = res`.
   - Return `res`.

### Time Complexity

- **O(N * 2^N)**.
- $16 \times 65536 \approx 10^6$ operations.

### Space Complexity

- **O(2^N)** for memoization.

![Algorithm Visualization](../images/BIT-013/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-013/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `1, 2, 3, 4`.
Top (`mask=0`): Pick `i=0` (Val 1).
- Try `j=1` (Val 2). Pair XOR 3. Recurse mask `0011`.
  - Remaining `3, 4`. `i=2`. Only `j=3`. Pair XOR 7. Recurse `1111` -> 0.
  - Returns `max(7, 0) = 7`.
  - Total path cost: `max(3, 7) = 7`.
- Try `j=2` (Val 3). Pair XOR 2. Recurse mask `0101`.
  - Remaining `2, 4`. `i=1`. Only `j=3`. Pair XOR 6.
  - Returns 6.
  - Total path cost: `max(2, 6) = 6`.
- Try `j=3` (Val 4). Pair XOR 5. Recurse mask `1001`.
  - Remaining `2, 3`. Pair XOR 1.
  - Returns 1.
  - Total path cost: `max(5, 1) = 5`.

Min of (7, 6, 5) -> 5.

## ✅ Proof of Correctness

### Invariant

The recurrence explores all valid edge-disjoint pairings by forcing an order on the first element of each pair. Since we take the minimum of the maximums, the logic holds for the min-max objective. Bitmask guarantees we cover every subset exactly once.

## 💡 Interview Extensions (High-Value Add-ons)

- **Min Sum of XORs**: Same complexity, just change `max` to `+`.
- **General Matching**: For weighted general matching where N is small, this pattern holds.

## Common Mistakes to Avoid

1. **Greedy Strategy**:
   - ❌ Pairing usually doesn't work with sorting.
   - ✅ Always verify small constraints ($N \le 20$) suggest exponential solution.
2. **Double Counting**:
   - ❌ Calculating `(i, j)` and `(j, i)`.
   - ✅ Fixing `i` to `first_unset` avoids permutations.

## Related Concepts

- **Bitmask DP**: Essential for small N problems.
- **Maximum Weight Perfect Matching (General)**: Blossom algorithm (but overkill here).
