---
title: Range T-Threshold Majority Check
slug: range-t-threshold-majority
difficulty: Medium
difficulty_score: 62
tags:
- Segment Tree
- Frequency Counting
- Range Queries
problem_id: SEG_RANGE_T_THRESHOLD_MAJORITY__7412
display_id: SEG-009
topics:
- Segment Tree
- Frequency Counting
- Range Queries
---
# Range T-Threshold Majority Check - Editorial

## Problem Summary

You are given an array `a`. You need to answer queries `MAJ l r T`: find a value that appears at least `T` times in the subarray `a[l..r]`. If multiple exist, return the one with the highest frequency (tie-break: smallest value). If none, return -1.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `1 <= T <= r - l + 1`
## Real-World Scenario

Imagine a **Voting System Audit**.
-   You have a list of votes cast in a sequence.
-   An auditor wants to check if any candidate received at least `T` votes in a specific precinct (range of votes).
-   If someone did, they are a "majority" candidate for that precinct.

## Problem Exploration

### 1. Randomized Approach
If a value appears `T` times in length `L = r - l + 1`, its probability of being picked at random is `T/L`.
If `T` is large (e.g., `T > L/2`), we can pick random elements and check their frequency.
However, `T` can be small (e.g., `T=1`), making this unreliable.
But the problem asks for *any* value with freq `>= T`. If `T` is small, almost any value works. If `T` is large, random sampling works.

### 2. Segment Tree with Candidates
This is similar to the **Range Majority Query** problem.
Standard approach: **Boyer-Moore Voting Algorithm** on Segment Tree nodes.
-   Each node stores a candidate and a count.
-   Merge: Combine candidates.
-   This finds a candidate that *might* be the majority (> L/2).
-   For arbitrary `T`, this requires a different approach.

For this problem, we need to find *any* value with freq >= T, specifically the one with *highest* frequency.
If `T` is small, many values qualify. We need the one with highest frequency.
This is essentially **Range Mode Query**, which is challenging (`O(N sqrtN)` with Mo's Algorithm).

With constraints `N, Q <= 200,000` and the hint "Store small candidate frequency map", the solution uses a **Misra-Gries** type summary approach:
-   Store `k` candidates and their counts per segment node.
-   When merging, combine counts. If map size exceeds `k`, apply pruning.
-   For `k=1`, this is Boyer-Moore.
-   For `k` small (e.g., 3-5), we capture frequent elements.
-   Then verify these candidates.

**Strategy:**
1.  Identify a set of **candidates** that are likely to be the answer using Misra-Gries.
2.  For each candidate, verify its frequency in `a[l..r]` using binary search on index lists.
3.  Return the best one.

**Implementation Approach:**
-   Node stores `vector<pair<int, int>> candidates`.
-   Merge: Combine two vectors. If same value, add counts. If size > K, prune by decrementing all counts.
-   Query: Merge `O(log N)` nodes to get a set of candidates.
-   Verify candidates using `vector<int> positions[MAX_VAL]`.

## Approaches

### Approach 1: Segment Tree with Misra-Gries Merging
1.  **Preprocess**: Store positions of each number: `pos[val] = {i1, i2, ...}`.
2.  **Segment Tree**: Each node stores top `K` (e.g., 3 or 5) candidates.
    -   Leaf: `[{val, 1}]`.
    -   Merge: Combine lists. If size > K, reduce all counts by min count? Or just keep top K?
    -   Correct Misra-Gries logic:
        -   Add counts for existing keys.
        -   For new keys, if space, add.
        -   If no space, decrement all counters by 1 (conceptually removing `K+1` distinct elements).
3.  **Query**:
    -   Get candidates from range `[l, r]`.
    -   Also add candidates from random sampling (optional but helpful).
    -   For each candidate, calculate exact frequency in `[l, r]` using `pos[val]`.
    -   Filter those with freq >= T.
    -   Pick best.

**Complexity**: `O(Q * (K log N + K log N))`. With `K=3`, feasible.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`5 1`
`1 1 2 3 1`
`MAJ 0 4 3`

1.  **Build**:
    -   Leaves: `{1:1}`, `{1:1}`, `{2:1}`, `{3:1}`, `{1:1}`.
    -   Merges up. Root will likely contain `{1:3, 2:1, 3:1}` (or similar, depending on K).
2.  **Query**: `l=0, r=4`.
    -   Returns summary with candidates, e.g., `1`.
    -   Check `1`: Positions `[0, 1, 4]`.
    -   Range `[0, 4]`: Indices `0, 1, 4` are inside. Count = 3.
    -   `3 >= 3`. Candidate 1 is valid.
3.  **Result**: 1.

## Proof of Correctness

-   **Misra-Gries Property**: If an element has frequency `> (R-L+1)/(K+1)`, it is guaranteed to be in the candidate set.
-   **Verification**: We verify exact counts using binary search on position lists, ensuring correctness.
-   **Tie-Breaking**: We explicitly check for max frequency and smallest value among valid candidates.

## Interview Extensions

1.  **Dynamic Updates?**
    -   If array updates, we need dynamic segment tree. Position lists become `std::set` or similar (slow) or use SQRT decomposition.
2.  **K-th Frequent?**
    -   Harder. Requires Persistent Segment Tree or similar.

### Common Mistakes

-   **K Value**: If `T` is very small, Misra-Gries might miss the true mode if the mode's frequency is not dominant enough relative to `K`. However, for "Majority" problems, usually `T` is large enough or `K` can be increased. With `K=3`, we find elements with freq > 25%.
-   **Tie-Breaking**: Don't forget to return the *smallest* value if frequencies match.
