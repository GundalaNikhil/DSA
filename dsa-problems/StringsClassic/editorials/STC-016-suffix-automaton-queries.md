---
problem_id: STC_SUFFIX_AUTOMATON_QUERIES__9036
display_id: STC-016
slug: suffix-automaton-queries
title: "Suffix Automaton Substring Queries"
difficulty: Medium
difficulty_score: 62
topics:
  - Strings
  - Suffix Automaton
  - Counting
tags:
  - strings
  - suffix-automaton
  - counting
  - medium
premium: true
subscription_tier: basic
---

# STC-016: Suffix Automaton Substring Queries

## 📋 Problem Summary

Given a string `s`, you need to answer multiple queries. Each query provides a string `p`, and you must return the number of times `p` appears as a substring in `s`. You are expected to use a **Suffix Automaton** to solve this efficiently.

## 🌍 Real-World Scenario

**Scenario Title:** High-Frequency Trading Pattern Analysis

In financial markets, analysts look for recurring patterns in price movements (represented as a string of symbols). To estimate the significance of a specific pattern (e.g., "Up-Down-Up"), they need to know how often it has occurred in the historical data. A Suffix Automaton allows for extremely fast querying of pattern frequencies over massive datasets, enabling real-time analysis.

**Why This Problem Matters:**

- **Search Engines:** Counting phrase frequencies for indexing and ranking.
- **Bioinformatics:** Counting motif occurrences in a genome.
- **Efficiency:** Suffix Automaton answers queries in O(|p|) time, independent of |s| (after O(|s|) preprocessing).

![Real-World Application](../images/STC-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "ababa"`.
Suffix Automaton States (simplified):
- **Root**: Empty string.
- **State "a"**: Occurs at {0, 2, 4}. Count = 3.
- **State "ab"**: Occurs at {1, 3}. Count = 2.
- **State "aba"**: Occurs at {2, 4}. Count = 2.
- **State "abab"**: Occurs at {3}. Count = 1.
- **State "ababa"**: Occurs at {4}. Count = 1.

Query "aba": Walk `root -> a -> ab -> aba`. Current state has count 2. Answer: 2.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s` and multiple query strings `p`.
- **Output:** Count of occurrences for each `p`.
- **Constraints:** `|s| <= 100,000`. Sum of `|p| <= 200,000`.
- **Clones:** The construction involves "cloning" states. Cloned states initially have count 0, while original states (created when extending the string) have count 1. Counts must be propagated.

## Naive Approach

### Intuition

For each query `p`, scan `s` to count occurrences (e.g., using KMP or naive search).

### Algorithm

1. For each query `p`:
2. Count occurrences in `s` using `s.indexOf(p, start)`.
3. Return count.

### Time Complexity

- **O(Q * (|s| + |p|))**: Too slow if many queries or long `s`.

### Space Complexity

- **O(1)**.

## Optimal Approach (Suffix Automaton)

### Key Insight

A **Suffix Automaton (SAM)** is a DAG where nodes represent equivalence classes of substrings. All substrings in a class `u` appear at the same set of end positions in `s`.
- `len(u)`: Length of the longest substring in class `u`.
- `link(u)`: Points to the state representing the longest proper suffix of `u` that is in a different class.
- `count(u)`: The number of times substrings in class `u` appear in `s`.

**Construction:**
We build the SAM incrementally. When adding character `c`:
- Create a new state `cur`.
- `count[cur] = 1` (it represents the full prefix ending at current position).
- Update transitions and links. If we split a state `q` into `q` and `clone`, `clone` inherits `count = 0` (it represents substrings that appear elsewhere, but doesn't account for the *current* prefix position directly; its count will be accumulated from children in the link tree).

**Count Propagation:**
The suffix links form a tree rooted at the initial state.
If a state `u` appears `k` times, then any suffix of `u` (represented by `link[u]`) also appears at least `k` times (plus occurrences where the suffix appears but `u` doesn't).
Therefore, `count[link[u]] += count[u]`.
We must process states in decreasing order of length (or reverse topological order) to propagate counts correctly.

**Querying:**
Start at root. For each char in `p`, follow transitions.
- If no transition, count is 0.
- If we process all of `p` and end at state `u`, the answer is `count[u]`.

### Algorithm

1. **Build SAM**:
   - Standard construction.
   - Maintain `is_clone` flag or initialize `cnt=1` for non-clones.
2. **Sort States**:
   - Sort states by `len` descending (or use bucket sort since `len <= |s|`).
3. **Propagate Counts**:
   - For each state `u` in sorted order (except root):
     - `cnt[link[u]] += cnt[u]`.
4. **Answer Queries**:
   - Walk the SAM. Return `cnt[final_state]`.

### Time Complexity

- **O(|s|)**: Construction and propagation.
- **O(|p|)**: Per query.
- **Total**: O(|s| + Sum(|p|)).

### Space Complexity

- **O(|s| * Sigma)**: Number of states is at most `2*|s|`.

![Algorithm Visualization](../images/STC-016/algorithm-visualization.png)
![Algorithm Steps](../images/STC-016/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

`s = "ababa"`
SAM Construction:
- `extend(a)`: `st[1] ("a")`, `cnt=1`.
- `extend(b)`: `st[2] ("ab")`, `cnt=1`.
- `extend(a)`: `st[3] ("aba")`, `cnt=1`. Note: `st[1]` ("a") is split? No, `st[0]` has `a` -> 1. `st[2]` has no `a`. `st[2]` links to `st[0]`. `p=2`. `st[2].next[a]=3`. `p=0`. `st[0].next[a]=1`. `q=1`. `len(0)+1 == len(1)`. `link[3]=1`.
- `extend(b)`: `st[4] ("abab")`.
- `extend(a)`: `st[5] ("ababa")`.

Propagation:
- `st[5]` ("ababa", cnt=1) -> link to `st[3]` ("aba"). `cnt[3] += 1` -> 2.
- `st[4]` ("abab", cnt=1) -> link to `st[2]` ("ab"). `cnt[2] += 1` -> 2.
- `st[3]` ("aba", cnt=2) -> link to `st[1]` ("a"). `cnt[1] += 2` -> 3.
- `st[2]` ("ab", cnt=2) -> link to `st[?]` ("b").
- Note: This trace highlights the accumulation logic. In the actual SAM, `cnt[u]` correctly accumulates occurrences from longer strings to their suffixes.
  - "aba" occurs 2 times. `st[3]` represents "aba". `cnt[3]` becomes 2.
  - "ab" occurs 2 times. `st[2]` represents "ab". `cnt[2]` becomes 2.
  - "a" occurs 3 times. `st[1]` represents "a". `cnt[1]` becomes 3.

Query "aba":
- `root -> a (1) -> b (2) -> a (3)`.
- `cnt[3] = 2`. Correct.

Query "baa":
- `root -> b`. `next[b]`? Yes.
- `-> a`. `next[a]`? Yes.
- `-> a`. `next[a]`? No.
- Result 0. Correct.

## ✅ Proof of Correctness

### Invariant

`count[u]` initially counts the number of times the longest string in class `u` appears as a *prefix* of the string processed so far (which is 1 for original states, 0 for clones).
The suffix link tree represents suffix inclusion. If `u` is a child of `v` in the link tree, then substrings in `v` are suffixes of substrings in `u`.
Any occurrence of `u` implies an occurrence of `v` ending at the same position.
Summing counts up the link tree correctly aggregates all end positions for each equivalence class.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: First Occurrence Index**
  - Maintain `first_end_pos[u]`. Update during extension (for original) and cloning (copy from original). Do not sum up links; take min/max if needed, but usually `first_end_pos` is invariant for the class? No, `clone` inherits `first_end_pos`.

- **Extension 2: Longest Common Substring**
  - Build SAM for `S`. Stream `T` through it, tracking current length and state. Max length seen is LCS.

### Common Mistakes to Avoid

1. **Not Propagating Counts**
   - ❌ Returning `cnt` directly after construction (will be 1 or 0).
   - ✅ Must propagate up suffix links.

2. **Sorting Order**
   - ❌ Propagating in arbitrary order.
   - ✅ Must be decreasing length (children before parents in link tree).

## Related Concepts

- **Suffix Tree**: Similar capabilities, often O(N) construction (Ukkonen's).
- **LCP Array**: Can solve counting but slower query time.
