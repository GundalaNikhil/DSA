---
problem_id: TRI_LONGEST_WORD_K_PREFIXES__8329
display_id: TRI-014
slug: longest-word-by-k-prefixes
title: "Longest Word Buildable by At Least K Prefixes"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - String
  - DFS
tags:
  - trie
  - prefix-matching
  - word-building
premium: true
subscription_tier: basic
---

# TRI-014: Longest Word Buildable by At Least K Prefixes

## 📋 Problem Summary

Find the longest word in a dictionary that has at least `k` of its prefixes also present in the dictionary. If multiple words qualify, return the lexicographically smallest. If no word meets the requirement, return empty string.

## 🌍 Real-World Scenario

**Language Learning & Word Formation**

Consider a language learning app like Duolingo that teaches vocabulary progressively. The app wants to identify which complex words students can learn based on simpler words they already know.

For example, if students know:

- "a", "ap", "app" → they can learn "apple" (has 3 known prefixes)
- "a", "ap" → they shouldn't learn "apex" yet (only 2 known prefixes)

This progressive learning approach:

- **Builds Understanding**: Complex words feel less intimidating when built from known parts
- **Reinforces Memory**: Each prefix reinforces previous learning
- **Optimizes Curriculum**: Determines optimal word introduction order

**Industry Applications:**

1. **Auto-Completion Systems**: Prioritize suggesting words with many common prefixes
2. **Spell Checkers**: Suggest corrections based on prefix similarity
3. **Code Completion**: IDEs suggest identifiers based on partial matches
4. **Domain-Specific Vocabularies**: Medical/legal terminology with prefix-based construction

In morphologically rich languages (like Turkish or Finnish), words are formed by adding prefixes and suffixes. This problem models identifying which compound words are "buildable" from simpler morphemes.

![Real-World Application](../images/TRI-014/real-world-scenario.png)

## Detailed Explanation

**Problem Breakdown:**

Given:

- A dictionary of words
- An integer `k`

Find:

- The longest word `w` such that at least `k` different prefixes of `w` exist in the dictionary
- Among ties (same length), choose lexicographically smallest

**Key Insights:**

1. A prefix of word `w` is `w[0:i]` for `i` from 1 to `len(w)-1` (excluding the word itself and empty string)
2. We need to count how many such prefixes exist in the dictionary
3. Use a trie to efficiently check prefix existence

**Example Walkthrough:**

Dictionary: `["a", "ap", "app", "apple", "apex"]`, k=3

**Prefix Counting:**

```
Trie of dictionary:
Root
  |
  a (end) ✓ ← Word 1
  |
  p (end) ✓ ← Word 2 ("ap")
  |
  +-- p (end) ✓ ← Word 3 ("app")
  |   |
  |   l
  |   |
  |   e (end) ✓ ← Word 4 ("apple")
  |
  +-- e
      |
      x (end) ✓ ← Word 5 ("apex")

Checking each word:
────────────────────────────────────
"a" (length 1):
  Prefixes to check: none (length < 2)
  Count: 0 ✗

"ap" (length 2):
  Prefixes: ["a"]
    "a": exists ✓
  Count: 1 ✗

"app" (length 3):
  Prefixes: ["a", "ap"]
    "a": exists ✓
    "ap": exists ✓
  Count: 2 ✗

"apple" (length 5):
  Prefixes: ["a", "ap", "app", "appl"]
    "a": exists ✓
    "ap": exists ✓
    "app": exists ✓
    "appl": does NOT exist ✗
  Count: 3 ✓ ← Meets k=3!

"apex" (length 4):
  Prefixes: ["a", "ap", "ape"]
    "a": exists ✓
    "ap": exists ✓
    "ape": does NOT exist ✗
  Count: 2 ✗

Result: "apple" (length 5, has exactly k=3 prefixes)
```

Analysis:

- "a": No prefixes (length 1) → 0 prefixes → doesn't meet k=3
- "ap": Prefix "a" exists → 1 prefix → doesn't meet k=3
- "app": Prefixes "a", "ap" exist → 2 prefixes → doesn't meet k=3
- "apple": Prefixes "a", "ap", "app", "appl" → check which exist:
  - "a": YES ✓
  - "ap": YES ✓
  - "app": YES ✓
  - "appl": NO ✗
  - Total: 3 prefixes ✓ → meets k=3, length 5
- "apex": Prefixes "a", "ap", "ape" → check:
  - "a": YES ✓
  - "ap": YES ✓
  - "ape": NO ✗
  - Total: 2 prefixes ✗ → doesn't meet k=3

Result: "apple" (length 5, meets k=3)

![Problem Illustration](../images/TRI-014/problem-illustration.png)

## Naive Approach

**Intuition:**

For each word, extract all its prefixes and check how many exist in the dictionary using a HashSet.

**Algorithm:**

1. Store all words in a HashSet for O(1) lookup
2. For each word:
   - Generate all prefixes (length 1 to length-1)
   - Count how many exist in the HashSet
   - If count >= k, it's a candidate
3. Among all candidates, find the longest (tie-break by lexicographic order)

**Time Complexity:** O(n × L²)

- For each of n words: O(n)
- Generate and check up to L prefixes: O(L)
- Each prefix check involves string creation: O(L)
- Total: O(n × L²)

**Space Complexity:** O(n × L) for the HashSet

**Limitations:**

- Quadratic in word length due to substring creation
- Doesn't leverage shared prefix structure
- Each word processed independently

## Optimal Approach

**Key Insight:**

Use a **trie** where each node tracks whether it's an end-of-word. When checking a word, traverse the trie and count how many intermediate nodes are marked as word endings.

**Algorithm:**

1. **Build Trie**:

   - Insert all words into trie
   - Mark end-of-word nodes

2. **Find Valid Words**:

   - For each word in dictionary:
     - Traverse its path in the trie
     - Count how many nodes along the path (excluding root and final node) are marked as word-ends
     - If count >= k, it's valid

3. **Select Best**:
   - Among valid words, choose longest
   - Tie-break by lexicographically smallest

**Optimization**: Instead of checking all words at the end, we can integrate validation during a DFS traversal of the trie itself, accumulating prefix count as we go deeper.

**Time Complexity:** O(n × L)

- Build trie: O(n × L)
- Validate each word: O(L) per word, O(n × L) total
- Finding max: O(n)

**Space Complexity:** O(n × L) for the trie

**Why This Is Optimal:**

- **Linear in Total Characters**: Each character processed constant times
- **No Redundant String Creation**: Work with trie nodes directly
- **Shared Prefix Exploitation**: Common prefixes stored once
- **Early Counting**: Accumulate prefix counts during traversal

**Example Execution:**

Dictionary: `["a", "ap", "app", "apple", "apex"]`, k=3

Build Trie:

```
        root
         |
         a (END: "a")
         |
         p (END: "ap")
         /  \
       p     e
      (END)  |
       |     x
       l    (END)
       |
       e
      (END)
```

Validate "apple":

- Traverse: root → a (END! count=1) → p (END! count=2) → p (END! count=3) → l → e
- Total prefix count = 3 >= k=3 ✓

Validate "apex":

- Traverse: root → a (END! count=1) → p (END! count=2) → e → x
- Total prefix count = 2 < k=3 ✗

Result: "apple" (length 5, 3 valid prefixes)

![Algorithm Visualization](../images/TRI-014/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


### Common Mistakes

1. **Including the Word Itself**: Counting the full word as its own prefix (should only count strict prefixes)
2. **Not Handling Ties**: Forgetting lexicographic tie-breaking for same-length words
3. **Off-by-One in Counting**: Including/excluding wrong nodes when counting prefixes
4. **Empty Result Handling**: Not returning empty string when no valid word exists

## Related Concepts

- Trie Data Structure
- Prefix Matching
- Lexicographic Ordering
- Word Formation
- Language Morphology


## Constraints

- `1 <= n <= 10^5` (number of words)
- `1 <= k <= 30`
- `1 <= word length <= 30`
- All words consist of lowercase English letters (a-z)
- No duplicate words in dictionary