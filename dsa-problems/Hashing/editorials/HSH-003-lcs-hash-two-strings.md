---
problem_id: HSH_LCS_HASH_TWO_STRINGS__7482
display_id: HSH-003
slug: lcs-hash-two-strings
title: "Longest Common Substring of Two Strings"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Binary Search
  - String Algorithms
tags:
  - hashing
  - binary-search
  - lcs
  - medium
premium: true
subscription_tier: basic
---

# HSH-003: Longest Common Substring of Two Strings

## 📋 Problem Summary

You are given two strings, `a` and `b`. Your task is to find the length of the longest substring that appears in both `a` and `b`. A substring is a contiguous sequence of characters.

## 🌍 Real-World Scenario

**Scenario Title:** Code Plagiarism Detection

Imagine you are a professor checking student assignments for copied code.

- Student A submits file `a`.
- Student B submits file `b`.
- You want to know if they copied a significant chunk of code from each other.
- Finding the "Longest Common Substring" tells you the maximum length of verbatim copying. If this length is large (e.g., 500 characters), it's strong evidence of plagiarism.

![Real-World Application](../images/HSH-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Finding the Overlap

String A: "abcde"
String B: "cdef"

```text
Length 1 check:
A: {a, b, c, d, e}
B: {c, d, e, f}
Common: {c, d, e} -> Found!

Length 2 check:
A: {ab, bc, cd, de}
B: {cd, de, ef}
Common: {cd, de} -> Found!

Length 3 check:
A: {abc, bcd, cde}
B: {cde, def}
Common: {cde} -> Found!

Length 4 check:
A: {abcd, bcde}
B: {cdef}
Common: None -> Stop.

Max Length: 3 ("cde")
```

### Key Concept: Binary Search on Answer

If two strings share a common substring of length `L`, they definitely share a common substring of length `L-1` (just take the prefix of the length `L` match).
This monotonicity allows us to use **Binary Search** on the length.

- Range: `[0, min(|a|, |b|)]`.
- Check function `possible(len)`: Returns true if there exists a common substring of length `len`.

To implement `possible(len)` efficiently, we use **Rolling Hash**.

1. Compute hashes of all substrings of length `len` in `a` and store them in a Hash Set.
2. Compute hashes of all substrings of length `len` in `b`.
3. If any hash from `b` exists in the set from `a`, return true.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Two strings `a` and `b`.
- **Output:** Integer representing the maximum length.
- **Constraints:** Lengths up to `10^5`. `O(N^2)` DP solution will TLE. We need `O(N log N)`.

## Naive Approach

### Intuition

Use Dynamic Programming (LCS table).
`DP[i][j]` = length of common suffix of `a[0 dots i]` and `b[0 dots j]`.
If `a[i] == b[j]`, `DP[i][j] = DP[i-1][j-1] + 1`.
Max value in DP table is the answer.

### Time Complexity

- **O(N \* M)**: Where `N, M` are lengths. For `10^5`, `10^10` operations is too slow.

## Optimal Approach

### Key Insight

Combine **Binary Search** with **Rolling Hash**.

- Binary search gives `O(log N)` steps.
- Rolling hash check takes `O(N)` time.
- Total time: `O(N log N)`.

### Algorithm

1. Initialize `low = 0`, `high = min(|a|, |b|)`.
2. While `low <= high`:
   - `mid = (low + high) / 2`.
   - If `check(mid)` is true:
     - `ans = mid`
     - `low = mid + 1` (Try longer)
   - Else:
     - `high = mid - 1` (Try shorter)
3. Return `ans`.

**Check Function `check(len)`:**

1. Calculate rolling hashes for all substrings of length `len` in `a`. Store in a Set.
2. Calculate rolling hashes for all substrings of length `len` in `b`.
3. If a hash from `b` is in the Set, return true.
   - _Note:_ To avoid collisions, use Double Hashing or check the actual substring (though checking is slow, double hashing is preferred).

### Time Complexity

- **O((N + M) log (min(N, M)))**.

### Space Complexity

- **O(N)**: To store hashes in the set.

![Algorithm Visualization](../images/HSH-003/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
abcde
cdef
```

**Binary Search:**

1. Range `[0, 4]`. Mid = 2.
   - `check(2)`:
     - A substrings: "ab", "bc", "cd", "de". Hashes stored.
     - B substrings: "cd", "de", "ef".
     - "cd" matches! Return true.
   - Ans = 2. Range `[3, 4]`.
2. Mid = 3.
   - `check(3)`:
     - A substrings: "abc", "bcd", "cde".
     - B substrings: "cde", "def".
     - "cde" matches! Return true.
   - Ans = 3. Range `[4, 4]`.
3. Mid = 4.
   - `check(4)`:
     - A substrings: "abcd", "bcde".
     - B substrings: "cdef".
     - No match. Return false.
   - Range `[4, 3]`. Loop ends.

**Result:** 3.

## ✅ Proof of Correctness

### Invariant

If `check(L)` returns true, there is a common substring of length `L`.
Since substring existence is monotonic (if length `L` exists, `L-1` exists), binary search correctly finds the maximum `L`.
The rolling hash correctly computes polynomial hashes for all substrings in `O(N)` time.

## 💡 Interview Extensions

- **Extension 1:** Find LCS of _k_ strings.
  - _Answer:_ Same binary search. In `check(len)`, keep a map `hash -> count`. If count reaches `k`, return true.
- **Extension 2:** What if we want the actual string, not just length?
  - _Answer:_ Store the starting index along with the hash in the set. If match found, return `a.substring(start, start + len)`.

### Common Mistakes to Avoid

1. **Hash Collisions**
   - ❌ Wrong: Assuming single hash is perfect.
   - ✅ Correct: For competitive programming, use Double Hashing or a very large modulus/random base to minimize probability.
2. **Power Calculation**
   - ❌ Wrong: Recomputing `B^L-1` inside the loop.
   - ✅ Correct: Precompute it once per `check` call.

## Related Concepts

- **Suffix Automaton / Suffix Tree:** Solves this in `O(N)` (linear time), but much harder to implement.
- **Dynamic Programming:** `O(N^2)` solution (LCS table).
