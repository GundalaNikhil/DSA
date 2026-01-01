---
problem_id: HSH_LONGEST_PAL_PREFIX_AFTER_APPEND__3764
display_id: HSH-014
slug: longest-pal-prefix-after-append
title: "Longest Palindromic Prefix After One Append"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - prefix
  - medium
premium: true
subscription_tier: basic
---

# HSH-014: Longest Palindromic Prefix After One Append

## 📋 Problem Summary

You are given a string `s` and a character `c`.

1. Append `c` to `s` to form a new string `T = s + c`.
2. Find the length of the longest prefix of `T` that is a palindrome.

## 🌍 Real-World Scenario

**Scenario Title:** Auto-Complete Correction

Imagine a user typing a word that is supposed to be a palindrome (like "racecar").

- They type "raceca".
- They press 'r' next.
- The system checks: Is "racecar" a palindrome? Yes.
- If they typed "racecx", the system checks "racecx". Longest palindromic prefix might just be "r".
- This logic helps in validating input for specific patterns or games.

![Real-World Application](../images/HSH-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Palindromic Prefix

String `s`: "abac"
Char `c`: 'a'
New String `T`: "abaca"

Prefixes of `T`:

1. "a" -> Palindrome? Yes. (Len 1)
2. "ab" -> Palindrome? No.
3. "aba" -> Palindrome? Yes. (Len 3)
4. "abac" -> Palindrome? No.
5. "abaca" -> Palindrome? No.

Max Length: 3.

### Key Concept: Rolling Hash for Palindromes

To check if a prefix `T[0..i]` is a palindrome, we need to check if `Hash(T[0..i]) == HashReverse(T[0..i])`.

- `Hash(T[0..i])` is the standard prefix hash.
- `HashReverse(T[0..i])` is the hash of the reversed prefix.
- We can maintain both hashes incrementally as we iterate through the string.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, char `c`.
- **Output:** Integer length.
- **Constraints:** `|s| <= 10^5`.
- **Note:** The new string has length `N+1`.

## Naive Approach

### Intuition

Construct `T`. Iterate all prefixes. Check if palindrome by reversing.

### Time Complexity

- **O(N^2)**: Checking each prefix takes `O(L)`. Sum of lengths is `O(N^2)`.

## Optimal Approach

### Key Insight

Use **Rolling Hash**.

- Iterate `i` from 0 to `N` (length of `T` is `N+1`).
- Maintain `forward_hash` of `T[0..i]`.
- Maintain `reverse_hash` of `T[0..i]`.
  - `reverse_hash` updates differently: `H_rev_new = H_rev_old + char x B^i`.
- If `forward_hash == reverse_hash`, update `max_len = i + 1`.

### Algorithm

1. `T = s + c`.
2. `fwd = 0`, `rev = 0`, `power = 1`.
3. `max_len = 0`.
4. Loop `i` from 0 to `len(T) - 1`:
   - `char val = T[i]`.
   - `fwd = (fwd * B + val) % M`.
   - `rev = (rev + val * power) % M`.
   - `power = (power * B) % M`.
   - If `fwd == rev`, `max_len = i + 1`.
5. Return `max_len`.

### Time Complexity

- **O(N)**: Single pass.

### Space Complexity

- **O(N)**: To store `T` (or `O(1)` if we handle `c` virtually).

![Algorithm Visualization](../images/HSH-014/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `s="abac"`, `c='a'`. `T="abaca"`.

**Iter 0 ('a'):**

- Fwd: 'a'. Rev: 'a'. Match. MaxLen=1.

**Iter 1 ('b'):**

- Fwd: "ab". Rev: "ba". No match.

**Iter 2 ('a'):**

- Fwd: "aba". Rev: "aba". Match. MaxLen=3.

**Iter 3 ('c'):**

- Fwd: "abac". Rev: "caba". No match.

**Iter 4 ('a'):**

- Fwd: "abaca". Rev: "acaba". No match.

**Result:** 3.

## ✅ Proof of Correctness

### Invariant

`fwdHash` stores hash of `T[0..i]`.
`revHash` stores hash of `reverse(T[0..i])`.
If they match, `T[0..i]` is a palindrome.
We check all prefixes, so we find the longest.

## 💡 Interview Extensions

- **Extension 1:** Longest Palindromic Suffix?
  - _Answer:_ Same logic, just process from right to left (or reverse string).
- **Extension 2:** KMP Failure Function?
  - _Answer:_ KMP finds longest proper prefix that is also a suffix. Here we want prefix that is palindrome.

### Common Mistakes to Avoid

1. **Power Update**
   - ❌ Wrong: Updating power before using it for `revHash`.
   - ✅ Correct: `revHash` uses `B^i`. Update power after.
2. **Modulo**
   - ❌ Wrong: Forgetting modulo on addition.

## Related Concepts

- **Manacher's Algorithm:** Finds all palindromes in `O(N)`.
- **KMP:** Prefix-Suffix properties.
