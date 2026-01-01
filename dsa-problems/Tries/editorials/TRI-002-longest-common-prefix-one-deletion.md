---
problem_id: TRI_LCP_ONE_DELETE__3841
display_id: TRI-002
slug: longest-common-prefix-one-deletion
title: "Longest Common Prefix After One Deletion"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Dynamic Programming
tags:
  - trie
  - string-matching
  - prefix
premium: true
subscription_tier: basic
---

# TRI-002: Longest Common Prefix After One Deletion

## 📋 Problem Summary

Given n lowercase words, find the longest string that can become a common prefix of all words after deleting at most one character from each word at any position.

## 🌍 Real-World Scenario

**Version Control System Conflict Resolution**

Imagine you're building a smart merge tool for Git. When multiple developers work on similar feature branches, their branch names often share common patterns:

- `feature/user-authentication`
- `feature/user-authorization`
- `feature/user-interface`

Your merge tool needs to identify the core common prefix to group related branches automatically. However, typos and inconsistent naming conventions mean you might need to "forgive" one character difference per branch name.

**Real-World Applications:**

A developer accidentally typed:

- `feature/xuser-auth` (extra 'x')
- `feature/user-autz` (typo: 'z' instead of 'h')
- `feature/user-aauth` (duplicate 'a')

Your algorithm should detect that removing one character from each makes them share the prefix `"feature/user-a"`, helping automatically categorize these as related branches.

**Why This Problem Matters:**

- **DevOps Automation**: Group related CI/CD pipelines by branch prefix
- **Log Analysis**: Cluster similar error messages ignoring noise characters
- **Data Deduplication**: Find near-identical record prefixes in databases
- **API Versioning**: Detect common API endpoint patterns despite typos

![Real-World Application](../images/TRI-002/real-world-scenario.png)

## Detailed Explanation

This problem extends classic LCP (Longest Common Prefix) by allowing flexibility. For each word, we can delete at most one character at any position, making it possible to align words that are "almost" sharing a prefix.

**Example Walkthrough:**

Words: `["interview", "internet", "interval"]`

Without deletions: Common prefix is "inter" (5 chars)

With one deletion per word, we can achieve "interv":

- "interview": Already has "interv" as prefix (no deletion needed) ✓
- "internet": Delete 'n' at position 5 → "iteret", then forms "inter" but not "interv". Alternative: delete 't' at position 2 → "inernet", still doesn't work. Keep as "internet" and match up to "inter"
- "interval": Already has "interv" as prefix (no deletion needed) ✓

The key insight: Build a trie of all possible variants (original + all single-deletion variants) of each word, then find the longest prefix path where each word has at least one variant passing through. In this case, "interv" works because at least one variant of each word contains it as a prefix.

## Naive Approach

**Intuition:**

Try every possible prefix length from longest to shortest. For each candidate prefix, check if each word can match it after deleting at most one character.

**Algorithm:**

1. Find max possible prefix length = min(all word lengths)
2. For length L from max down to 0:
   - For each candidate prefix of length L:
     - Check if every word can be transformed to have this prefix by deleting ≤ 1 char
     - If yes, return this prefix
3. Return empty string if no match

**Time Complexity:** O(N × L³) where N = number of words, L = max length

- For each length L: O(L)
- For each prefix: O(26^L) possible prefixes
- Checking each word: O(L × N)

**Space Complexity:** O(L)

**Why This Works:**

- Exhaustively checks all possibilities
- Guaranteed to find the longest valid prefix

**Limitations:**

- **Exponential candidate space**: Too many possible prefixes to enumerate
- **Repeated work**: Checks same transformations multiple times
- **Impractical for long words**: Becomes infeasible beyond small inputs

## Optimal Approach

**Key Insight:**

Build a **trie of variants**: For each word, insert both the original and all single-deletion variants (at most L+1 variants per word). Then find the deepest trie node reached by at least one variant from each word.

**Variant Generation:**

```
Example: words = ["interview", "internet", "internal"]
Word 0: "interview" → variants: "interview", "nterview", "iterview", "inerview", ...
Word 1: "internet"  → variants: "internet", "nternet", "iternet", "inernet", ...
Word 2: "internal"  → variants: "internal", "nternal", "iternal", "inernal", ...

Trie with word IDs tracked:
Root
  |
  i {0,1,2}
  |
  n {0,1,2}
  |
  t {0,1,2}
  |
  e {0,1,2}
  |
  r {0,1,2}  ← All 3 words reach here (LCP = "inter")
  |
  +-- v {0}      (from "interview")
  |
  +-- n {1,2}
      |
      +-- e {1}  (from "internet")
      |
      +-- a {2}  (from "internal")

Result: "inter" (depth 5, all word IDs present)
```

**Algorithm:**

1. **Generate Variants**:

   - For each word `w`:
     - Insert `w` into trie (no deletion)
     - For each position `i` in `w`:
       - Create variant by deleting character at position `i`
       - Insert variant into trie
     - Mark each trie path with the word ID it represents

2. **DFS to Find Longest Common Prefix**:

   - Traverse trie depth-first
   - At each node, check if all N word IDs are represented
   - Track the deepest node where all words have coverage
   - Return the path (prefix) to that node

3. **Optimization**: Use bit-masking or hash sets to track which words are represented at each node

**Time Complexity:** O(N × L²)

- Generating variants: O(N × L²) (N words, L deletions each, L chars per variant)
- DFS: O(total trie nodes) = O(N × L²)

**Space Complexity:** O(N × L²) for trie storage

**Why This Is Optimal:**

- **Avoids enumeration**: Builds only relevant prefixes (those from actual word variants)
- **Single pass**: DFS checks all words simultaneously
- **Practical**: Handles realistic word lengths (L ≤ 100) efficiently

![Algorithm Visualization](../images/TRI-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


### Common Mistakes to Avoid

1. **Forgetting Edge Cases**

   - **Issue**: Not handling empty words or single-character words
   - ❌ Wrong: Assuming all words have length ≥ 2
   - ✅ Correct: Check for empty strings and handle deletion creating empty variants

2. **Incorrect Variant Generation**

   - **Issue**: Generating duplicates or missing the original word
   - ❌ Wrong: Only inserting deletion variants, not the original
   - ✅ Correct: Insert original word PLUS all single-deletion variants

3. **Not Tracking Word IDs**

   - **Issue**: Only checking if trie node exists, not which words reach it
   - ❌ Wrong: Assuming node existence means all words share that prefix
   - ✅ Correct: Maintain a set of word IDs at each node to verify coverage

## Related Concepts

- **Longest Common Prefix (LCP)**: Classic problem without deletions
- **Edit Distance**: Generalized version allowing insertions, deletions, substitutions
- **Trie Data Structure**: Efficient prefix storage and retrieval
- **String Matching with Errors**: Approximate string matching algorithms


## Constraints

- `1 <= n <= 10^5` (number of words)
- `1 <= total length of all words <= 2 × 10^5`
- All words contain only lowercase English letters