---
problem_id: HSH_HASH_NEAR_ANAGRAM_INDEXING__7523
display_id: HSH-016
slug: hash-near-anagram-indexing
title: "Hash-Based Near-Anagram Indexing"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Anagrams
  - Union-Find
tags:
  - hashing
  - anagram
  - grouping
  - union-find
  - medium
premium: true
subscription_tier: basic
---

# HSH-016: Hash-Based Near-Anagram Indexing

## 📋 Problem Summary

You are given a list of words. Two words are considered "connected" if they can become anagrams of each other by removing exactly one character from each.
Find the number of connected groups (connected components) of words.

## 🌍 Real-World Scenario

**Scenario Title:** Fuzzy Search for Typos

Imagine a search engine trying to group similar search queries.
- User A types "apple".
- User B types "aple" (missing 'p').
- User C types "applee" (extra 'e').
- Let's re-read: "remove exactly one character from each".
- "apple" (remove 'p') -> "aple". "aple" (remove 'e') -> "apl". Not anagrams.
- "apple" (remove 'e') -> "appl". "apply" (remove 'y') -> "appl". Connected!
- This models finding words that share a common "root" or "stem" despite minor variations.

![Real-World Application](../images/HSH-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Connection Graph

Words: `["abc", "abd", "ab"]`

1. **"abc"**:
   - Remove 'a' -> "bc"
   - Remove 'b' -> "ac"
   - Remove 'c' -> "ab"

2. **"abd"**:
   - Remove 'a' -> "bd"
   - Remove 'b' -> "ad"
   - Remove 'd' -> "ab"

3. **"ab"**:
   - Remove 'a' -> "b"
   - Remove 'b' -> "a"

**Connections:**
- "abc" generates "ab".
- "abd" generates "ab".
- Since they both generate "ab", they are connected via the intermediate key "ab".
- Note: The problem says "remove 1 from each". So "abc" and "abd" are connected because `abc - c = ab` and `abd - d = ab`.
- "abc" and "ab"? `abc - c = ab`. `ab - ?`. `ab` needs to remove 1 char to become something.
- `ab - b = a`. `ab` is not equal to `a`.
- So "abc" and "ab" are NOT connected directly by this definition.
- But "abc" and "abd" ARE connected.

### Key Concept: Intermediate Hash Keys

Instead of comparing every pair of words (`O(N^2)`), we generate all possible "reduced" forms for each word.
- Word `W` generates reduced forms `R_1, R_2, dots, R_L`.
- Map each reduced form to the list of words that generated it.
- If two words generate the same reduced form, union them.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** List of `N` words.
- **Output:** Number of groups.
- **Constraints:** `N=10^5`, Length `L=30`.
- **Anagram:** Two strings are anagrams if sorting them results in the same string.
- **Strategy:** Sort the reduced forms to canonicalize them.

## Naive Approach

### Intuition

For every pair of words, check if they satisfy the condition.

### Time Complexity

- **O(N^2 * L)**: Too slow.

## Optimal Approach

### Key Insight

Use **Union-Find (Disjoint Set Union)**.
1. Create a DSU structure for `N` words.
2. Use a Map: `String (Sorted Reduced Form) -> List<Integer (Word Index)>`.
3. For each word `i`:
   - Generate all `L` reduced strings (remove char at `k`).
   - Sort the reduced string.
   - Add `i` to the map entry for this sorted string.
4. Iterate through the map. For each key, all indices in the list should be unioned together.
5. Count number of disjoint sets.

### Algorithm

1. Initialize DSU with `N` components.
2. `Map<String, List<Integer>> invertedIndex`.
3. Loop `i` from 0 to `N-1`:
   - `w = words[i]`.
   - Sort `w` to `sortedW`.
   - Loop `j` from 0 to `L-1`:
     - Create `sub = sortedW` without char at `j`.
     - `invertedIndex[sub].add(i)`.
4. For each list in `invertedIndex`:
   - Union all indices in the list (e.g., union `list[0]` with `list[k]`).
5. Return `dsu.count`.

### Time Complexity

- **O(N * L^2 log L)**: Sorting takes `L log L`. We do it `L` times (actually just sort once and remove takes `O(L)`).
- Better: Sort word first (`L log L`). Then removing one char takes `O(L)`. Total `O(N * L)`.
- Map operations: String key length `L`.
- Total: `O(N * L^2)`. With `L=30`, this is very fast.

### Space Complexity

- **O(N * L^2)**: Storing all reduced forms.

![Algorithm Visualization](../images/HSH-016/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `["abcd", "abdc", "abc", "abd"]`

**Processing:**
1. "abcd" (sorted "abcd"):
   - "bcd", "acd", "abd", "abc".
   - Map: `{"bcd":[0], "acd":[0], "abd":[0], "abc":[0]}`
2. "abdc" (sorted "abcd"):
   - "bcd", "acd", "abd", "abc".
   - Map updates: `{"bcd":[0,1], "acd":[0,1], "abd":[0,1], "abc":[0,1]}`
3. "abc" (sorted "abc"):
   - "bc", "ac", "ab".
   - Map updates: `{"bc":[2], "ac":[2], "ab":[2]}`
4. "abd" (sorted "abd"):
   - "bd", "ad", "ab".
   - Map updates: `{"bd":[3], "ad":[3], "ab":[2,3]}`

**Union:**
- From "bcd": Union(0, 1). Group {0, 1}.
- From "ab": Union(2, 3). Group {2, 3}.
- "abc" generates "ab". "abd" generates "ab". So 2 and 3 connected.
- "abcd" generates "abc". "abc" generates... wait.
- "abcd" generates "abc". This "abc" is the *reduced form*.
- Does word "abc" (index 2) connect to reduced form "abc"?
- No. Word "abc" generates "ab", "ac", "bc".
- Word "abcd" generates "abc".
- The reduced form "abc" is just a key.
- Index 0 generates key "abc".
- Does Index 2 generate key "abc"? No.
- So Index 0 and Index 2 are NOT connected via key "abc".
- Are they connected via anything else?
- Index 0: keys {abc, abd, acd, bcd}
- Index 2: keys {ab, ac, bc}
- No common keys.
- So {0, 1} are one group. {2, 3} are another group.
- Total 2 groups. Matches example output.

## ✅ Proof of Correctness

### Invariant
Two words are in the same set if and only if they share a common reduced form.
Transitivity of Union-Find ensures that if A connects to B, and B connects to C, then A connects to C.

## 💡 Interview Extensions

- **Extension 1:** What if we can remove *up to* K characters?
  - *Answer:* Generate all subsequences of length `L-K dots L`. Too slow for large K.
- **Extension 2:** Longest chain of such words?
  - *Answer:* Graph problem (Longest Path in DAG if length decreases, or component size).

### Common Mistakes to Avoid

1. **Sorting**
   - ❌ Wrong: Not sorting the word before generating reduced forms. Anagrams must be canonicalized.
2. **Duplicates**
   - ❌ Wrong: Processing same reduced form multiple times for one word (e.g., "aba" -> "ba", "ba").
   - ✅ Correct: Use a Set or check `s[j] == s[j-1]`.

## Related Concepts

- **BK-Tree:** For fuzzy matching with edit distance.
- **SimHash:** For document similarity.
