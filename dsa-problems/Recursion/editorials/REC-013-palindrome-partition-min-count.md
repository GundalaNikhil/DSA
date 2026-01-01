---
title: Palindrome Partition with Minimum Count
slug: palindrome-partition-min-count
difficulty: Medium
difficulty_score: 53
tags:
- Recursion
- Backtracking
- Strings
problem_id: REC_PALINDROME_PARTITION_MIN_COUNT__3491
display_id: REC-013
topics:
- Recursion
- Backtracking
- Strings
---
# Palindrome Partition with Minimum Count - Editorial

## Problem Summary

You need to partition a string `s` into substrings such that:
1.  Every substring is a **palindrome**.
2.  The length of every substring is at most `L`.
3.  The **number of substrings** in the partition is minimized.

Return the **lexicographically smallest** partition achieving this minimum. The lexicographical order is determined by exploring palindromes in order of increasing length at each step.


## Constraints

- `1 <= |s| <= 12`
- `1 <= L <= |s|`
- `s` contains lowercase English letters
## Real-World Scenario

Think of **Data Compression**. You want to split a long message into the fewest possible chunks, but each chunk must satisfy a specific property (like being a palindrome, which might represent a reversible signal) and fit within a buffer size `L`. Minimizing the number of chunks reduces header overhead.

## Problem Exploration

### 1. Palindrome Check
A substring `s[i...j]` is a palindrome if it reads the same forwards and backwards. We can precompute this for all pairs `(i, j)` in `O(N^2)` using Dynamic Programming.
`isPal[i][j] = (s[i] == s[j]) && (j - i < 2 || isPal[i+1][j-1])`.

### 2. Minimum Cuts (DP vs BFS)
To find the *minimum number* of partitions, we can use BFS or DP.
-   **BFS**: Treat indices `0` to `N` as nodes. Edge from `i` to `j` exists if `s[i...j-1]` is a valid palindrome of length `<= L`. Find shortest path from `0` to `N`.
-   **DP**: `dp[i]` = min partitions for suffix `s[i...]`.
    `dp[i] = 1 + min(dp[j+1])` for all valid `j` where `s[i...j]` is palindrome and length `<= L`.

### 3. All Solutions
Since we need *all* partitions achieving the minimum count, we can:
1.  Compute `min_cuts` using BFS/DP.
2.  Use Backtracking (DFS) to reconstruct paths that match this `min_cuts`.

Given `N <= 12`, we can just use pure backtracking with a global minimum tracker, or iterative deepening. But BFS is cleanest for "shortest path" structure.

## Approaches

### Approach 1: BFS for Min Count + DFS for Reconstruction
1.  **BFS**: Compute `dist[i]`: minimum number of palindromes needed to cover prefix `s[0...i-1]`. Or better, `dist[i]` = min partitions for suffix `s[i...]`. Let's do suffix.
    -   `dist[N] = 0`.
    -   Work backwards or use BFS from `N` to `0` in the reversed graph?
2.  **DFS**: Reconstruct paths.
    -   `dfs(index, current_path)`
    -   If `index == N`: Add to results if `current_path.size() == min_k`.
    -   Iterate `j` from `index` to `N-1`.
    -   If `s[index...j]` is valid (palindrome & length `<= L`) AND `dist[j+1] == dist[index] - 1` (optimal substructure):
        -   Add substring to path.
        -   Recurse.
        -   Backtrack.

Then in DFS from `0`: move to `j+1` only if `dist[j+1] == dist[index] + 1`.

### Approach 2: Pure Backtracking (Small N)
With `N=12`, pure recursion is fine.
`solve(index, current_path)`
-   Track `global_min`.
-   If `current_path.size() > global_min`, prune.
-   If `index == N`:
    -   If `size < global_min`: Clear results, update `global_min`, add path.
    -   If `size == global_min`: Add path.

This is simpler to implement and sufficient for `N=12`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `aab`, `L=2`

1.  **Precompute Palindromes**:
    -   `a` (0,0), `a` (1,1), `b` (2,2) -> True.
    -   `aa` (0,1) -> True.
    -   `ab` (1,2) -> False.
    -   `aab` (0,2) -> False.
2.  `backtrack(0)`:
    -   Try `a` (0,0): Path `["a"]`.
        -   `backtrack(1)`:
            -   Try `a` (1,1): Path `["a", "a"]`.
                -   `backtrack(2)`:
                    -   Try `b` (2,2): Path `["a", "a", "b"]`.
                        -   Found len 3. `minCount = 3`. Results `[["a", "a", "b"]]`.
            -   Try `ab` (1,2): Invalid.
    -   Try `aa` (0,1): Path `["aa"]`.
        -   `backtrack(2)`:
            -   Try `b` (2,2): Path `["aa", "b"]`.
                -   Found len 2. `2 < 3`. `minCount = 2`. Results `[["aa", "b"]]`.
    -   Try `aab` (0,2): Length 3 > L=2. Break.

**Result:** `aa b`.

## Proof of Correctness

-   **Validity**: We only pick substrings that are palindromes and satisfy length constraint `L`.
-   **Optimality**: We track `minCount` and only keep solutions that match this minimum.
-   **Completeness**: Backtracking explores all valid partitions.

## Interview Extensions

1.  **Just the count?**
    -   Use DP: `dp[i] = 1 + min(dp[j+1])`. `O(N^2)`.
2.  **Large N?**
    -   Manacher's Algorithm for palindrome finding (`O(N)`), then DP.

### Common Mistakes

-   **Length Constraint**: Forgetting to check `end - start + 1 <= L`.
-   **Pruning**: Not pruning when `current.size() >= minCount` can lead to TLE on slightly larger inputs (though `N=12` is very forgiving).
