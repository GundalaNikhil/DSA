---
problem_id: HSH_COUNT_DISTINCT_SUBSTRINGS__8741
display_id: HSH-005
slug: count-distinct-substrings-hash
title: "Count Distinct Substrings"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Set Operations
tags:
  - hashing
  - substring
  - distinct
  - medium
premium: true
subscription_tier: basic
---

# HSH-005: Count Distinct Substrings

## 📋 Problem Summary

You are given a string `s`. Your task is to count the total number of **distinct** substrings, including the empty string.
For example, in "aaa", the substrings are "", "a", "a", "a", "aa", "aa", "aaa".
Distinct ones: "", "a", "aa", "aaa". Count = 4.

## 🌍 Real-World Scenario

**Scenario Title:** Data Deduplication

Imagine you are building a search engine index. You have a massive text, and you want to index all possible phrases (substrings) so users can search for any part of the text.
- Storing every occurrence of every phrase is wasteful.
- You only need to store each *unique* phrase once.
- Counting distinct substrings helps estimate the size of this index.

![Real-World Application](../images/HSH-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Substring Enumeration

String: "ababa"

```text
Length 1:
"a", "b", "a", "b", "a" -> Distinct: {"a", "b"} (2)

Length 2:
"ab", "ba", "ab", "ba" -> Distinct: {"ab", "ba"} (2)

Length 3:
"aba", "bab", "aba" -> Distinct: {"aba", "bab"} (2)

Length 4:
"abab", "baba" -> Distinct: {"abab", "baba"} (2)

Length 5:
"ababa" -> Distinct: {"ababa"} (1)

Empty String: "" -> Distinct: {""} (1)

Total: 1 + 2 + 2 + 2 + 2 + 1 = 10.
```

### Key Concept: Hashing for Uniqueness

Instead of storing full strings in a Set (which consumes huge memory and time for comparisons), we store their **Hashes**.
- A hash is a single number representing the string.
- Comparing two numbers is `O(1)`.
- Storing numbers is space-efficient.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`.
- **Output:** Integer count.
- **Constraints:** `|s| <= 10^5`.
- **Time Complexity Considerations:**
  - The problem specifies `O(N^2)` time complexity in the notes section.
  - For the constraint `N=10^5`, an `O(N^2)` solution performs `10^10` operations, which may exceed time limits.
  - For production systems with `N=10^5`, **Suffix Automaton** or **Suffix Array** solutions (`O(N)` or `O(N log N)`) are more appropriate.
  - However, the problem title explicitly mentions "Hash" and the notes specify `O(N^2)`.
  - **Implementation approach:** This editorial provides the hashing solution as specified. Test cases may have smaller actual values of N, or the time limit may be generous enough to accommodate `O(N^2)` with optimized hashing.

## Naive Approach

### Intuition

Generate all substrings, put them in a `HashSet<String>`.

### Algorithm

1. `Set<String> distinct = new HashSet<>();`
2. Loop `i` from 0 to `n`:
   - Loop `j` from `i+1` to `n`:
     - `distinct.add(s.substring(i, j))`
3. Return `distinct.size() + 1` (for empty).

### Time Complexity

- **O(N^3)**: `O(N^2)` substrings, each takes `O(N)` to hash/store. Definitely TLE.

## Optimal Approach (for Hashing context)

### Key Insight

Use **Rolling Hash**.
- Iterate through all starting positions `i`.
- For each `i`, iterate `j` from `i` to `n-1`.
- Update the hash incrementally in `O(1)`.
- Insert hash into a `HashSet<Long>`.

### Algorithm

1. Initialize `Set<Long> hashes`.
2. Loop `i` from 0 to `n-1`:
   - `currentHash = 0`
   - Loop `j` from `i` to `n-1`:
     - `currentHash = (currentHash * B + s[j]) % M`
     - `hashes.add(currentHash)`
3. Return `hashes.size() + 1`.

### Time Complexity

- **O(N^2)**: We visit each substring once, `O(1)` work per visit.
- For `N=10^5`, this is still too slow. But it's the optimal *hashing* approach.
- (True optimal is Suffix Automaton `O(N)`).

### Space Complexity

- **O(N^2)**: In worst case (all distinct), we store `O(N^2)` hashes.

![Algorithm Visualization](../images/HSH-005/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
aaa
```

**Iteration i=0:**
- j=0 ("a"): Hash(a). Add to Set.
- j=1 ("aa"): Hash(aa). Add.
- j=2 ("aaa"): Hash(aaa). Add.

**Iteration i=1:**
- j=1 ("a"): Hash(a). Already in Set.
- j=2 ("aa"): Hash(aa). Already in Set.

**Iteration i=2:**
- j=2 ("a"): Hash(a). Already in Set.

**Result:**
Set contains {Hash(a), Hash(aa), Hash(aaa)}. Size = 3.
Return 3 + 1 (empty) = 4.

## ✅ Proof of Correctness

### Invariant
The set contains the hash of every substring exactly once.
Since we iterate all `s[i..j]`, we cover all substrings.
The Set data structure ensures uniqueness.
Collision probability is low with large MOD.

## 💡 Interview Extensions

- **Extension 1:** How to solve for `N=10^5`?
  - *Answer:* Use **Suffix Array** + **LCP Array**. Count = `fracN(N+1)2 - sum LCP[i]`. Time `O(N log N)` or `O(N)`.
- **Extension 2:** Count distinct substrings of length `K`.
  - *Answer:* Sliding window rolling hash. `O(N)`.

### Common Mistakes to Avoid

1. **Memory Limit Exceeded**
   - ❌ Wrong: Storing strings in Set.
   - ✅ Correct: Store `long` hashes.
2. **Time Limit Exceeded**
   - ❌ Wrong: Recomputing hash from scratch for each substring (`O(N^3)`).
   - ✅ Correct: Rolling hash (`O(N^2)`).

## Related Concepts

- **Suffix Automaton:** The ultimate tool for substring problems.
- **Trie:** Insert all suffixes into a Trie. Count nodes. `O(N^2)`.
