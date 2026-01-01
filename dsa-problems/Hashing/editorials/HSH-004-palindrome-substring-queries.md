---
problem_id: HSH_PALINDROME_SUBSTRING_QUERIES__2639
display_id: HSH-004
slug: palindrome-substring-queries
title: "Palindrome Substring Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - queries
  - medium
premium: true
subscription_tier: basic
---

# HSH-004: Palindrome Substring Queries

## 📋 Problem Summary

You are given a string `s` and multiple queries. Each query consists of a range `[l, r]`. You need to determine if the substring `s[l..r]` is a palindrome (reads the same forwards and backwards).

## 🌍 Real-World Scenario

**Scenario Title:** DNA Palindrome Detection

In genetics, palindromic sequences in DNA (like `GAATTC` which pairs with `CTTAAG` on the opposite strand, reading the same 5' to 3') are crucial. They often serve as binding sites for restriction enzymes.
- A researcher might want to scan millions of specific regions to check if they are palindromic.
- Doing this naively for every region is slow.
- Hashing allows us to check any region in constant time.

![Real-World Application](../images/HSH-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Forward vs Reverse Hash

String: "banana"
Reverse: "ananab"

Query: `s[1..3]` ("ana")

```text
Original (s):
Index: 0 1 2 3 4 5
Char:  b a n a n a

Reverse (rev_s):
Index: 0 1 2 3 4 5
Char:  a n a n a b
(Note: rev_s[0] corresponds to s[5])

To check if s[l..r] is a palindrome:
1. Compute Hash(s[l..r]) using prefix hashes of s.
2. Compute Hash(Reverse of s[l..r]).
   - The reverse of s[l..r] corresponds to a substring in rev_s.
   - Specifically, index i in s maps to index (N-1-i) in rev_s.
   - So s[l..r] reversed is rev_s[N-1-r ... N-1-l].
3. If Hash(Forward) == Hash(Backward), it's a palindrome.
```

### Key Concept: Reverse String Hashing

A string is a palindrome if it equals its reverse.
Instead of reversing the substring explicitly (which takes `O(Len)`), we can precompute hashes for the **entire reversed string**.
Then, the hash of the "reversed substring" can be retrieved in `O(1)` from the reversed string's hash array.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, queries `(l, r)`.
- **Output:** Boolean for each query.
- **Constraints:** `N, Q <= 2 * 10^5`. `O(1)` per query is required.
- **Double Hashing:** Highly recommended to avoid collisions.

## Naive Approach

### Intuition

For each query `(l, r)`, extract the substring, reverse it, and compare.

### Algorithm

1. For each query:
   - Extract `sub = s.substring(l, r+1)`.
   - Check if `sub == reverse(sub)`.

### Time Complexity

- **O(Q * N)**: Extracting and reversing takes linear time relative to substring length. Too slow.

## Optimal Approach

### Key Insight

Use **Rolling Hash** on both `s` and `reverse(s)`.
- Let `h1` be the prefix hash array for `s`.
- Let `h2` be the prefix hash array for `reverse(s)`.
- For query `(l, r)`:
  - Forward Hash = Hash of `s[l..r]` using `h1`.
  - Backward Hash = Hash of `reverse(s)[(n-1-r)..(n-1-l)]` using `h2`.
  - If they match, it's a palindrome.

### Algorithm

1. Construct `rev_s` by reversing `s`.
2. Compute prefix hashes and powers for `s` (Forward Hash).
3. Compute prefix hashes for `rev_s` (Reverse Hash).
4. For each query `(l, r)`:
   - Get forward hash of `s[l..r]`.
   - Get reverse hash of `rev_s` corresponding to range `[n-1-r, n-1-l]`.
   - Compare.

### Time Complexity

- **O(N + Q)**: Preprocessing takes `O(N)`, queries take `O(1)`.

### Space Complexity

- **O(N)**: Storing hash arrays.

![Algorithm Visualization](../images/HSH-004/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abccba
1
1 4
```
Query: `s[1..4]` ("bccb").

**Preprocessing:**
- `s` = "abccba"
- `hFwd` and `hRev` will be identical arrays.

**Query Processing:**
- `l=1, r=4`. Substring "bccb".
- `fwdHash` = Hash of `s[1..4]` ("bccb").
- `revL` = `6 - 1 - 4 = 1`.
- `revR` = `6 - 1 - 1 = 4`.
- `revHash` = Hash of `rev_s[1..4]` ("bccb").
- `fwdHash == revHash`? Yes.
- `s[1..4]` is "bccb".
- "bccb" IS a palindrome.
- Example Input: `abccba`.
- Query 2: `1 4`.
- `s[1]`='b', `s[2]`='c', `s[3]`='c', `s[4]`='b'.
- "bccb" is a palindrome (reads the same forwards and backwards).
- The implementation correctly checks if a substring is a palindrome.



## ✅ Proof of Correctness

### Invariant
A string `S` is a palindrome iff `S == reverse(S)`.
Hash(`S`) == Hash(`reverse(S)`) is a necessary condition. With double hashing, it is sufficient with high probability.
The mapping `s[l..r]` `<=ftrightarrow` `rev_s[n-1-r .. n-1-l]` correctly identifies the reversed substring.

## 💡 Interview Extensions

- **Extension 1:** Count all palindromic substrings.
  - *Answer:* Manacher's Algorithm (`O(N)`). Hashing is `O(N log N)` or `O(N^2)`.
- **Extension 2:** Longest Palindromic Substring.
  - *Answer:* Binary search on length + Hashing check (`O(N log N)`). Or Manacher's (`O(N)`).

### Common Mistakes to Avoid

1. **Index Mapping**
   - ❌ Wrong: `rev_s[l..r]`.
   - ✅ Correct: `rev_s[n-1-r .. n-1-l]`. The indices flip.
2. **Off-by-one**
   - ❌ Wrong: `len = r - l`.
   - ✅ Correct: `len = r - l + 1`.

## Related Concepts

- **Manacher's Algorithm:** Specialized for palindromes.
- **Rolling Hash:** General purpose string tool.
