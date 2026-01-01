---
problem_id: HSH_SUBSTRING_HASH_UNDER_EDITS__7394
display_id: HSH-009
slug: substring-hash-under-edits
title: "Substring Hash Under Edits"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Data Structures
  - Segment Tree
tags:
  - hashing
  - segment-tree
  - updates
  - queries
  - medium
premium: true
subscription_tier: basic
---

# HSH-009: Substring Hash Under Edits

## 📋 Problem Summary

You are given a string `s`. You need to support two operations:
1. **Update:** Change the character at index `i` to `c`.
2. **Query:** Return the polynomial rolling hash of the substring `s[l..r]`.

## 🌍 Real-World Scenario

**Scenario Title:** Collaborative Document Editing

Imagine a collaborative text editor like Google Docs.
- Users are constantly typing (updating characters).
- The system needs to quickly verify if two sections of the document are identical (e.g., to merge changes or detect duplicates).
- Recomputing the hash of the entire document after every keystroke is too slow.
- We need a way to update the hash locally and query any part instantly.

![Real-World Application](../images/HSH-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Segment Tree for Hashing

String: "abc" (Indices 0, 1, 2)
Base: 10 (for simplicity)

Tree Structure:
```text
        [0-2]
       /     \
    [0-1]    [2-2] ('c')
    /   \
 [0-0] [1-1]
 ('a') ('b')
```

**Leaf Nodes:**
- Node `[0-0]`: Hash("a") = 97
- Node `[1-1]`: Hash("b") = 98
- Node `[2-2]`: Hash("c") = 99

**Merging Nodes:**
- To merge left child (hash `H_L`, length `Len_L`) and right child (hash `H_R`, length `Len_R`):
- Combined Hash = `H_L x B^Len_R + H_R`.
- Node `[0-1]`: Hash("ab") = `97 x 10^1 + 98 = 1068`.
- Node `[0-2]`: Hash("abc") = `1068 x 10^1 + 99 = 10779`.

**Update:**
- Change 'b' to 'x'.
- Update leaf `[1-1]`.
- Recompute parent `[0-1]`.
- Recompute root `[0-2]`.
- Complexity: `O(log N)`.

### Key Concept: Associativity of Hashing

Polynomial hashing is associative if we track lengths.
`Hash(A + B) = Hash(A) x Base^Length(B) + Hash(B)`.
This property allows us to use a **Segment Tree**. Each node stores the hash of the substring it covers.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, list of operations.
- **Output:** Hashes for query operations.
- **Constraints:** `N, Q <= 2 * 10^5`.
- **Indexing:** 0-based.

## Naive Approach

### Intuition

- **Update:** Modify string array (`O(1)`).
- **Query:** Compute hash by iterating from `l` to `r` (`O(N)`).

### Time Complexity

- **O(Q * N)**: Too slow for `2 * 10^5` operations.

## Optimal Approach

### Key Insight

Use a **Segment Tree**.
- Each node stores the hash of its range.
- **Build:** `O(N)`.
- **Update:** `O(log N)`. Traverse path to root, applying the merge formula.
- **Query:** `O(log N)`. Combine hashes of relevant nodes.

### Algorithm

1. Precompute powers of Base: `B^0, B^1, dots, B^N`.
2. Build Segment Tree.
   - Leaf: `H = s[i]`.
   - Internal: `H = (H_left x B^len_right + H_right) +/-od M`.
3. **Update(i, c):**
   - Go to leaf `i`. Update value.
   - Recalculate ancestors.
4. **Query(l, r):**
   - Standard range query.
   - Be careful when combining partial results: ensure correct powers are multiplied.
   - So, query should return `{hash, length}`.

### Time Complexity

- **O(Q log N)**.

### Space Complexity

- **O(N)**: Segment Tree size (`4N`).

![Algorithm Visualization](../images/HSH-009/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abc
Q 0 2
U 1 x
Q 0 2
```

**Build:**
- Leaf `[0]`: 'a'(97).
- Leaf `[1]`: 'b'(98).
- Leaf `[2]`: 'c'(99).
- Root `[0-2]`: Hash("abc") = `97 * 100 + 98 * 10 + 99 = 10779`. (Using base 10 for simplicity).

**Op 1 (Q 0 2):**
- Returns root hash: 10779.

**Op 2 (U 1 x):**
- Update index 1 to 'x'(120).
- Leaf `[1]` becomes 120.
- Parent `[0-1]` recomputed: `97 * 10 + 120 = 1090`.
- Root `[0-2]` recomputed: `1090 * 10 + 99 = 11009`.

**Op 3 (Q 0 2):**
- Returns new root hash: 11009.

## ✅ Proof of Correctness

### Invariant
Each node in the segment tree correctly stores the polynomial hash of the substring it covers.
The merge operation `H = H_L x B^Len_R + H_R` correctly combines two adjacent substrings.
Updates propagate correctly up the tree.

## 💡 Interview Extensions

- **Extension 1:** Range Updates?
  - *Answer:* Lazy propagation. Need to maintain sum of powers to update a range to a specific character.
- **Extension 2:** Find first index where two strings differ (with updates).
  - *Answer:* Binary search on Segment Tree (`O(log N)`).

### Common Mistakes to Avoid

1. **Incorrect Merge Logic**
   - ❌ Wrong: `H_L + H_R`.
   - ✅ Correct: Shift `H_L` by length of `R`.
2. **Query Overlap Calculation**
   - ❌ Wrong: Using full length of right child.
   - ✅ Correct: Use length of the *intersection* of query range and right child range.

## Related Concepts

- **Fenwick Tree:** Can also be used (Hash = `sum s[i] * B^i`). Update is adding `(c_new - c_old) * B^i`. Query is range sum.
- **Treap:** For splitting/merging strings.
