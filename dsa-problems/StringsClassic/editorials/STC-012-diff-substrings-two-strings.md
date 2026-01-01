---
problem_id: STC_DIFF_SUBSTRINGS_TWO_STRINGS__6174
display_id: STC-012
slug: diff-substrings-two-strings
title: "Number of Different Substrings of Two Strings"
difficulty: Medium
difficulty_score: 58
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
---

# STC-012: Number of Different Substrings of Two Strings

## 📋 Problem Summary

Given two strings `a` and `b`, calculate the number of **distinct** substrings of `a` that do **not** appear in `b`.

## 🌍 Real-World Scenario

**Scenario Title:** Proprietary Code Analysis

Suppose you have a proprietary codebase (`a`) and an open-source library (`b`). You want to know how much "unique" code you have written that isn't just a copy of the open-source library. By counting the distinct substrings in `a` that are not present in `b`, you get a measure of the unique information content in your codebase relative to the library.

**Why This Problem Matters:**

- **Copyright Enforcement:** Identifying unique creative content vs. common boilerplate.
- **Bioinformatics:** Finding unique gene sequences in a specific species compared to a reference genome.
- **Cybersecurity:** Identifying unique malware signatures that haven't been seen in a database of known safe files.

![Real-World Application](../images/STC-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `a = "ab"`, `b = "b"`.
Substrings of `a`:
- "a" (Not in `b`) -> Count!
- "ab" (Not in `b`) -> Count!
- "b" (In `b`) -> Skip.

Total unique in `a` but not `b`: 2.

### Algorithm Logic

1. **Distinctness in `a`**: Normally, we count distinct substrings of `a` using `len(suffix) - lcp(suffix, prev_suffix_in_a)`.
2. **Exclusion from `b`**: For each suffix of `a`, let `L` be the length of the longest prefix that appears in `b`. Any substring starting at this suffix with length `<= L` is present in `b`.
3. **Combination**: For a suffix of `a`, the valid lengths are those greater than `L` and also "new" (not counted by previous `a`-suffixes).
   - Valid Range: `(max(LCP_prev_a, Max_Match_b) + 1)` to `len(suffix)`.
   - Contribution: `max(0, len(suffix) - max(LCP_prev_a, Max_Match_b))`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Distinct:** If "xyz" appears twice in `a` and never in `b`, it counts as 1.
- **Empty Strings:** If `a` is empty, answer is 0.
- **Constraints:** `|a| + |b| <= 200,000`. Use O(N log N) or O(N).

## Naive Approach

### Intuition

Generate all substrings of `a`, store them in a Set. Then iterate through the Set and check if each is in `b`.

### Algorithm

1. `Set<String> distinctA`
2. Add all substrings of `a` to `distinctA`.
3. `count = 0`
4. For each `s` in `distinctA`:
   - If `!b.contains(s)`, `count++`.
5. Return `count`.

### Time Complexity

- **O(|a|^3 + |a|*|b|)**: Very slow.

### Space Complexity

- **O(|a|^2)**.

## Optimal Approach (SA + LCP)

### Key Insight

We need two pieces of information for every suffix `i` of `a`:
1. `max_match_b[i]`: The length of the longest prefix of `suffix_a[i]` that appears as a substring in `b`.
2. `lcp_prev_a[i]`: The LCP with the lexicographically preceding suffix that is *also* from `a`.

**Computing `max_match_b`:**
Construct the Generalized Suffix Array for `S = a + '#' + b`.
For any suffix of `a`, its longest common prefix with *any* suffix of `b` is determined by the closest suffixes of `b` in the sorted SA (one above, one below).
We can compute this with two passes over the LCP array:
- **Forward Pass:** Track the minimum LCP since the last seen `b`-suffix.
- **Backward Pass:** Track the minimum LCP since the last seen `b`-suffix (from the right).
`max_match_b[i]` is the maximum of these two values.

**Computing `lcp_prev_a`:**
Iterate through the SA. Keep track of the last seen suffix from `a`. The LCP between the current `a`-suffix and the last `a`-suffix is the `lcp_prev_a`. Note: this is the minimum LCP in the range between them in the full SA.

**Final Count:**
Sum over all suffixes `i` of `a`:
`contribution = max(0, len(suffix_i) - max(lcp_prev_a[i], max_match_b[i]))`

### Algorithm

1. Build SA and LCP for `S = a + '#' + b`.
2. Compute `max_match_b` for each position in SA corresponding to `a`.
   - Use forward/backward passes.
3. Compute `lcp_prev_a` effectively by iterating the SA and maintaining the running minimum LCP since the last `a`-suffix.
   - So if we skip `b`-suffixes, we must take the minimum of all intermediate LCP values.
4. Sum the contributions.

### Time Complexity

- **O(N log N)**: SA construction. Passes are linear.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/STC-012/algorithm-visualization.png)
![Algorithm Steps](../images/STC-012/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

`a = "ab"`, `b = "b"`
`S = "ab#b"`
SA:
0. `#b` (2)
1. `ab#b` (0) - A
2. `b` (3) - B
3. `b#b` (1) - A

LCP (between adjacent):
- `#b` vs `ab#b`: 0
- `ab#b` vs `b`: 0
- `b` vs `b#b`: 1 ("b")

Max Match B:
- `sa[0]` (#b): B-like (sentinel).
- `sa[1]` (ab#b):
  - Forward: prev was #b, LCP 0.
  - Backward: next is b, LCP 0.
  - `maxMatchB` = 0.
- `sa[2]` (b): B.
- `sa[3]` (b#b):
  - Forward: prev was b, LCP 1.
  - Backward: none.
  - `maxMatchB` = 1.

Count:
- `sa[1]` (ab#b): `len=2`. `prevALCP=0`. `deduct=max(0, 0)=0`. Add `2-0=2`. ("ab", "a")
- `sa[3]` (b#b): `len=1`. `prevALCP` (with `sa[1]`): min LCP in range [1..3] -> `min(lcp[2], lcp[3])` -> `min(0, 1) = 0`.
  - `deduct=max(0, 1)=1`. Add `1-1=0`.
  - `lcp[2]` is between `sa[1]` and `sa[2]` -> 0.
  - `lcp[3]` is between `sa[2]` and `sa[3]` -> 1.
  - Min is 0. Correct.
  - "b" is a duplicate of "b" in "ab"? No, "b" in "ab" starts at 1. `sa[3]` starts at 1.
  - "b" is a substring of "ab".
  - My manual trace is slightly off. "b" is present in `b`. So `maxMatchB` correctly identified it.
  - `sa[1]` ("ab") contributes "a", "ab". Both not in `b`. Count 2.
  - `sa[3]` ("b") contributes nothing because `maxMatchB` is 1 (matches "b").
  - Total 2. Correct.

![Example Visualization](../images/STC-012/example-1.png)

## ✅ Proof of Correctness

### Invariant

For each suffix `i` of `a`, the substrings starting at `i` are `s[i...i]`, `s[i...i+1]`, ..., `s[i...n-1]`.
Lengths range from 1 to `len(suffix)`.
Substrings with length `<= max_match_b[i]` are present in `b`.
Substrings with length `<= lcp_prev_a[i]` are present in a lexicographically smaller suffix of `a` (duplicates).
We want substrings that are NEITHER in `b` NOR duplicates in `a`.
Since both conditions define a prefix range, we exclude `max(max_match_b[i], lcp_prev_a[i])`.
The remaining count is `len(suffix) - max(...)`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Count Shared Substrings**
  - Instead of exclusive, count distinct substrings present in BOTH.
  - `min(len, max_match_b) - lcp_prev_a`.

- **Extension 2: Generalized for K Strings**
  - Count substrings unique to string 1 among K strings.
  - `max_match_others` instead of `max_match_b`.

### Common Mistakes to Avoid

1. **LCP Indexing**
   - ❌ `lcp[i]` usually refers to `sa[i-1]` and `sa[i]`. Be careful with 0-based vs 1-based.
   - ✅ In my code, `lcp[i]` is between `sa[i-1]` and `sa[i]`. `lcp[0]` is dummy.

2. **Resetting `prevALCP`**
   - ❌ Forgetting to reset `prevALCP` to `n` (infinity) after processing an `a`-suffix.
   - ✅ Necessary because the "chain" of `a`-suffixes is broken by `b`-suffixes, but we logically want the LCP with the *previous* `a`-suffix in the SA, skipping `b`s. My logic `prevALCP = min(prevALCP, lcp[i])` correctly accumulates the minimum over the gap.

## Related Concepts

- **Suffix Automaton**: Can solve this in O(N) without SA.
- **Aho-Corasick**: For multiple patterns.
