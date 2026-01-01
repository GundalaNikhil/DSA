---
problem_id: TRI_SUFFIX_LONGEST_REPEAT__3945
display_id: TRI-011
slug: suffix-trie-longest-repeat
title: "Suffix Trie Longest Repeat"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - String
  - Suffix Structures
tags:
  - trie
  - suffix-trie
  - longest-repeat
  - string-algorithms
premium: true
subscription_tier: basic
---

# TRI-011: Suffix Trie Longest Repeat

## 📋 Problem Summary

Build a suffix trie (or use suffix array alternative) to find the length of the longest repeated substring in a given string.

## 🌍 Real-World Scenario

**Plagiarism Detection and Code Clone Detection**

Imagine you're building a plagiarism detection system for a university or a code clone detector for GitHub. You need to find the longest repeated sequences in documents or code files to identify copied content.

**Example Use Cases:**

1. **Academic Integrity**: Detecting when students copy paragraphs from each other
2. **Code Review**: Finding duplicated code blocks that should be refactored
3. **Data Compression**: Identifying repeated patterns for efficient compression
4. **Bioinformatics**: Finding repeated DNA sequences in genetic data

For string "banana":

- "ana" appears twice (at positions 1 and 3)
- Length = 3

**Why This Matters:**

- **Code Quality**: Detecting code duplication (DRY principle)
- **Security**: Finding repeated patterns in malware signatures
- **Compression**: Better compression ratios by identifying repeats
- **Biology**: Understanding gene replication and mutations

![Real-World Application](../images/TRI-011/real-world-scenario.png)

## Detailed Explanation

A suffix trie stores all suffixes of a string. For "banana":

- Suffixes: "banana", "anana", "nana", "ana", "na", "a"

When built into a trie, common prefixes of suffixes become shared paths. The longest path with at least 2 branches (meaning at least 2 suffixes share that prefix) represents the longest repeated substring.

**Key Insight**: If a substring repeats, it will be a prefix of multiple suffixes.

**Example**: "banana"

```
Suffixes and their common prefixes:
- "banana" and "anana" share "" (empty)
- "anana" and "ana" share "ana" (length 3) ✓
- "nana" and "na" share "na" (length 2)
```

Longest repeat: "ana" with length 3.

## Naive Approach

**Algorithm:**

1. Generate all substrings of length L (from longest to shortest)
2. For each substring, check if it appears at least twice in the original string
3. Return the length of the first substring found

**Time Complexity:** O(n³) - O(n²) substrings, O(n) to check each
**Space Complexity:** O(n²) for storing substrings

## Optimal Approach

**Suffix Trie for "banana":**

```
Suffixes: "banana", "anana", "nana", "ana", "na", "a"

Suffix Trie (with suffix counts):
Root
  |
  +-- b
  |   |
  |   a (count=1)
  |   |
  |   n
  |   |
  |   a
  |   |
  |   n
  |   |
  |   a (count=1, end)
  |
  +-- a (count=3)  ← 3 suffixes: "anana", "ana", "a"
  |   |
  |   +-- n (count=2)  ← 2 suffixes: "anana", "ana"
  |       |
  |       a (count=2)  ← 2 suffixes: depth=3, "ana" repeats!
  |       |
  |       n (count=1)
  |       |
  |       a (count=1, end)
  |
  +-- n (count=2)  ← 2 suffixes: "nana", "na"
      |
      a (count=2)  ← depth=2, "na" repeats
      |
      n (count=1)
      |
      a (count=1, end)

DFS finds max depth where count ≥ 2:
  - "a" at depth 1: count=3 ✓
  - "an" at depth 2: count=2 ✓
  - "ana" at depth 3: count=2 ✓ ← Maximum!
  - "n" at depth 1: count=2 ✓
  - "na" at depth 2: count=2 ✓

Result: 3 (longest repeating substring "ana")
```

**Algorithm:**

1. Build suffix trie for all suffixes
2. DFS through trie, tracking depth
3. At each node with 2+ children (branch point), update max depth
4. Return the maximum depth found

**Time Complexity:** O(n²) for building suffix trie
**Space Complexity:** O(n²) for storing trie

**Alternative**: Use suffix array + LCP for O(n log n) time

![Algorithm Visualization](../images/TRI-011/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


### Common Mistakes to Avoid

1. **Not Checking for Branching**
   - Must check if node has 2+ children or paths
2. **Incorrect Depth Tracking**

   - Depth represents length of repeated substring

3. **Missing Edge Cases**
   - Empty string, single character, no repeats

## Related Concepts

- Suffix Trees/Arrays
- Longest Common Substring
- String Matching Algorithms


## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters