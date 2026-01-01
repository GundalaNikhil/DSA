---
problem_id: TRI_AUTOCOMPLETE_DECAY__7294
display_id: TRI-001
slug: autocomplete-top-k-fresh
title: "Autocomplete Top-K with Freshness Decay"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - Priority Queue
  - Hash Table
  - Sorting
tags:
  - trie
  - heap
  - autocomplete
  - ranking
premium: true
subscription_tier: basic
---

# TRI-001: Autocomplete Top-K with Freshness Decay

## 📋 Problem Summary

Build a trie-based autocomplete system that ranks search suggestions using a freshness decay formula, combining base frequency with recency to provide the most relevant top-k results for a given prefix.

## 🌍 Real-World Scenario

**Smart Search Engine at E-Commerce Platform**

Imagine you're a software engineer at a major e-commerce platform like Amazon or eBay. Users type search queries millions of times per day, and your job is to build an intelligent autocomplete system that suggests the most relevant products.

Here's the challenge: A product searched frequently 6 months ago ("iPhone 12") might be less relevant today than a newer product ("iPhone 15") searched less often but more recently. Your system needs to balance:

- **Historical popularity**: Products searched frequently should rank higher
- **Recency**: Recently searched items are more relevant
- **User experience**: Results must appear instantly (< 50ms)

The freshness decay formula `score = frequency × exp(-(currentTime - lastUsed)/D)` achieves this perfectly. The decay constant `D` controls how quickly old searches lose relevance:

- Small `D` (e.g., 1 day): Heavy recency bias, great for trending news
- Large `D` (e.g., 30 days): Balances history and recency, ideal for e-commerce

**Why This Problem Matters:**

- **Revenue Impact**: Better autocomplete increases search success rate by 15-25%, directly boosting sales
- **User Retention**: Fast, relevant suggestions keep users engaged and reduce bounce rate
- **Scalability**: Must handle millions of words and thousands of queries per second efficiently

![Real-World Application](../images/TRI-001/real-world-scenario.png)

## Detailed Explanation

This problem combines multiple data structures:

1. **Trie**: Efficiently stores words and enables prefix-based retrieval
2. **Hash Map**: Stores metadata (frequency, timestamp) for each word
3. **Heap/Sorting**: Ranks words by decayed score

The key challenge is computing the decay score efficiently. The exponential decay formula ensures older searches gradually lose relevance while maintaining long-term popularity signals.

**Example Walkthrough:**

Given words: `[(hello, freq=5, t=0), (helium, freq=3, t=5), (he, freq=4, t=9)]`
Current time = 10, Decay constant D = 10, Prefix = "he", k = 2

Calculate decayed scores:

- "hello": 5 × exp(-(10-0)/10) = 5 × exp(-1) ≈ 5 × 0.368 = 1.84
- "helium": 3 × exp(-(10-5)/10) = 3 × exp(-0.5) ≈ 3 × 0.606 = 1.82
- "he": 4 × exp(-(10-9)/10) = 4 × exp(-0.1) ≈ 4 × 0.905 = 3.62

Sorted by score (descending): "he" (3.62), "hello" (1.84), "helium" (1.82)

Top 2: ["he", "hello"]

**Trie with Frequency & Timestamp:**

```
Root
  |
  h
  |
  e (freq=4, lastUsed=9, score=3.62)
  |
  +-- l
      |
      +-- i
      |   |
      |   u
      |   |
      |   m (freq=3, lastUsed=5, score=1.82)
      |
      +-- l
          |
          o (freq=5, lastUsed=0, score=1.84)

Query: prefix="he", currentTime=10, D=10, k=2

Decay Formula: score = freq × e^(-(currentTime - lastUsed)/D)

Matching words traversed from "he" node:
  - "he":     score = 4 × e^(-0.1) = 3.62  ← Rank 1
  - "hello":  score = 5 × e^(-1.0) = 1.84  ← Rank 2 ✓
  - "helium": score = 3 × e^(-0.5) = 1.82  ← Rank 3

Result: ["he", "hello"]
```

## Naive Approach

**Intuition:**

Store all words in a list. For each autocomplete query:

1. Filter words matching the prefix
2. Compute decay score for each
3. Sort by score
4. Return top k

**Algorithm:**

1. Store words with metadata in a list
2. For autocomplete query:
   - Linear scan to find all words with matching prefix
   - Compute decay score for each: `freq × exp(-(currentTime - lastUsed)/D)`
   - Sort results by score (descending), then lexicographically
   - Return top k results

**Time Complexity:** O(N × L + N log N) per query, where N = total words, L = average word length
**Space Complexity:** O(N × L)

**Why This Works:**

- Correctly computes decay scores for all matching words
- Sorting ensures top-k results are accurate
- Simple to implement and understand

**Limitations:**

- **Inefficient prefix matching**: Scanning all N words for every query is wasteful
- **Repeated sorting**: If queries share prefixes, we recompute scores unnecessarily
- **Poor scalability**: With millions of words, each query takes seconds

## Optimal Approach

**Key Insight:**

Use a **Trie** to group words by prefix, enabling O(L) prefix matching instead of O(N). Store metadata in a hash map for O(1) access, and use a min-heap of size k to efficiently track top results.

**TrieNode Structure:**

```
TrieNode:
┌─────────────────────────────────────┐
│  children: dict[char → TrieNode]   │  ← Branch to child nodes
├─────────────────────────────────────┤
│  is_end_of_word: bool               │  ← Marks complete word
└─────────────────────────────────────┘

Word Metadata (separate hash map):
┌──────────────────────────────────────┐
│  word → {frequency, last_used_time}  │
└──────────────────────────────────────┘
```

**Algorithm:**

1. **Build Trie**:

   - Insert all words into trie
   - Store word metadata (frequency, lastUsed) in a hash map keyed by word

2. **Autocomplete Query**:

   - Traverse trie to find node corresponding to prefix (O(P) where P = prefix length)
   - DFS from that node to collect all words with the prefix (O(M) where M = matching words)
   - For each matching word:
     - Retrieve metadata from hash map: O(1)
     - Compute decay score: `freq × exp(-(currentTime - lastUsed)/D)`
   - Use min-heap of size k to track top k scores (O(M log k))
   - Extract results from heap and sort if needed (O(k log k))

3. **Optimization**: Maintain max-heap if multiple queries, or cache results per prefix

**Time Complexity:**

- Trie build: O(N × L)
- Per query: O(P + M log k), where P = prefix length, M = matching words, k = result size
- Space Complexity: O(N × L) for trie + O(N) for hash map

**Why This Is Optimal:**

- **Trie prefix matching**: O(P) instead of O(N) for prefix filtering
- **Heap for top-k**: O(M log k) instead of O(M log M) for full sort
- **Scalable**: With smart trie pruning, can handle millions of words
- **Extensible**: Easy to add features like typo tolerance, synonym expansion

![Algorithm Visualization](../images/TRI-001/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
hello 5 0
helium 3 5
he 4 9
he 10 10 2
```

1.  **Insert Words**:
    -   `hello`: freq=5, time=0.
    -   `helium`: freq=3, time=5.
    -   `he`: freq=4, time=9.

2.  **Query**:
    -   Prefix: "he"
    -   Current Time: 10
    -   D: 10
    -   k: 2

3.  **Trie Traversal**:
    -   Search "he". Node found.
    -   Collect matches: `["he", "hello", "helium"]`.

4.  **Score Calculation**:
    -   **"he"**: `4 * exp(-(10-9)/10) = 4 * exp(-0.1) ≈ 3.619`
    -   **"hello"**: `5 * exp(-(10-0)/10) = 5 * exp(-1.0) ≈ 1.839`
    -   **"helium"**: `3 * exp(-(10-5)/10) = 3 * exp(-0.5) ≈ 1.820`

5.  **Ranking (Top 2)**:
    -   Sort: `he (3.62)`, `hello (1.84)`, `helium (1.82)`
    -   Top 2: `["he", "hello"]`

**Output**: `["he", "hello"]`

### Common Mistakes to Avoid

1. **Incorrect Decay Calculation**

   - **Issue**: Using integer division or forgetting to cast to double
   - ❌ Wrong: `exp(-(currentTime - lastUsed) / D)` when D is int
   - ✅ Correct: `exp(-(currentTime - lastUsed) / (double)D)`

2. **Not Handling Tie-Breaking**

   - **Issue**: When scores are equal, forgetting to sort lexicographically
   - ❌ Wrong: Only sorting by score
   - ✅ Correct: Sort by score DESC, then by word ASC

3. **Inefficient Full Sort**

   - **Issue**: Sorting all M matches when only k results are needed
   - ❌ Wrong: `sort(matches)` then `return matches[:k]`
   - ✅ Correct: Use min-heap of size k for O(M log k)

## Related Concepts

- **Prefix Trees (Tries)**: Fundamental data structure for string prefix matching
- **Exponential Decay**: Widely used in recommendation systems, caching, and time-series analysis
- **Top-K Selection**: Heap-based optimization for ranking problems
- **Autocomplete Systems**: Real-world applications in search engines, IDEs, mobile keyboards


## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= frequency <= 10^6`
- `0 <= timestamp, currentTime <= 10^9`
- `1 <= D <= 10^9` (decay constant)
- `1 <= k <= 10`
- All words are lowercase English letters