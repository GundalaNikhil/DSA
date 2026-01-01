---
problem_id: STC_KMP_PREFIX_FUNCTION__5824
display_id: STC-001
slug: kmp-prefix-function
title: "Prefix Function (KMP) Construction"
difficulty: Easy
difficulty_score: 22
topics:
  - Strings
  - KMP
  - Prefix Function
tags:
  - strings
  - kmp
  - prefix-function
  - easy
premium: true
subscription_tier: basic
---

# STC-001: Prefix Function (KMP) Construction

## 📋 Problem Summary

Given a string `s`, you need to compute the **prefix function** array `pi`. For each index `i`, `pi[i]` represents the length of the longest **proper** prefix of the substring `s[0...i]` that is also a suffix of this substring. A proper prefix is a prefix that is not equal to the substring itself.

## 🌍 Real-World Scenario

**Scenario Title:** DNA Sequence Alignment

Imagine you are a bioinformatician working on aligning DNA sequences. You have a long reference genome and a short read (a fragment of DNA). To efficiently find where the short read fits into the genome, you need to understand the internal structure of the read itself. Specifically, knowing if the beginning of the read matches the end of some part of the read allows you to skip unnecessary comparisons when a mismatch occurs during the search process. This is the core idea behind the Knuth-Morris-Pratt (KMP) algorithm, and the "prefix function" is the precomputed table that enables this efficiency.

**Why This Problem Matters:**

- **Efficient Search:** It's the building block for the KMP algorithm, which allows searching for a pattern in a text in linear time O(N+M).
- **Periodicity Analysis:** The prefix function can be used to determine the smallest period of a string, which is useful in data compression and pattern recognition.
- **Avoids Backtracking:** In text editors or search engines, it allows for "search as you type" functionality without re-scanning the entire text for every new character.

![Real-World Application](../images/STC-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let's look at the string `s = "ababa"`. We want to find `pi[4]`, which corresponds to the substring `s[0...4] = "ababa"`.

```
Index: 0 1 2 3 4
Char:  a b a b a

Substring s[0...4]: "ababa"

Proper Prefixes:
- "a"      (len 1)
- "ab"     (len 2)
- "aba"    (len 3)
- "abab"   (len 4)

Suffixes:
- "a"      (len 1)
- "ba"     (len 2)
- "aba"    (len 3)
- "baba"   (len 4)
- "ababa"  (len 5) - Not a proper prefix!

Matches:
- "a" (Prefix) == "a" (Suffix) -> Length 1
- "aba" (Prefix) == "aba" (Suffix) -> Length 3

Longest Match Length: 3
So, pi[4] = 3.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Proper Prefix:** The prefix cannot be the entire string itself. For a string of length `L`, the maximum possible value in the `pi` array is `L-1`.
- **Base Case:** `pi[0]` is always `0` because a single character string has no proper prefix that is also a non-empty suffix.
- **Indexing:** The problem uses 0-based indexing.

Common interpretation mistake:
- ❌ Thinking `pi[i]` is the count of matching characters at index `i`.
- ✅ `pi[i]` is the *length* of the matching prefix-suffix structure ending at `i`.

## Naive Approach

### Intuition

For every position `i` in the string, we can simply check all possible lengths `k` (from `i` down to `1`) to see if the prefix of length `k` matches the suffix of length `k` ending at `i`.

### Algorithm

1. Initialize an array `pi` of size `n` with zeros.
2. Iterate `i` from `1` to `n-1`.
3. For each `i`, iterate `k` from `i` down to `1`.
4. Check if `s[0...k-1]` is equal to `s[i-k+1...i]`.
5. If they match, set `pi[i] = k` and break (since we want the longest).

### Time Complexity

- **O(N^3)**: The outer loop runs `N` times. The inner loop runs `O(N)` times. The string comparison takes `O(N)`. Total `O(N^3)`.
- Can be optimized to **O(N^2)** with careful comparison, but still too slow for `N=200,000`.

### Space Complexity

- **O(N)**: To store the result array.

### Limitations

- Too slow for large strings. With `N=200,000`, `N^2` is `4 * 10^10` operations, which will exceed the 2-second time limit.

## Optimal Approach (KMP Construction)

### Key Insight

We can compute `pi[i]` using the values we've already computed for `pi[0]` to `pi[i-1]`.
Specifically, if we know `pi[i-1] = j`, it means `s[0...j-1]` matches `s[i-j...i-1]`.
To compute `pi[i]`, we just need to check if the next character `s[i]` matches the character after the prefix, which is `s[j]`.

- If `s[i] == s[j]`, then we can extend the match: `pi[i] = j + 1`.
- If `s[i] != s[j]`, we can't extend the current prefix of length `j`. We need to find a shorter prefix that is also a suffix ending at `i-1`. The length of the next best candidate is `pi[j-1]`. We update `j = pi[j-1]` and try again.

### Algorithm

1. Initialize `pi` array of size `n` with 0.
2. Maintain a variable `j` representing the length of the current matching prefix (initially 0).
3. Iterate `i` from `1` to `n-1`:
    a. While `j > 0` and `s[i] != s[j]`, backtrack `j` to `pi[j-1]`.
    b. If `s[i] == s[j]`, increment `j`.
    c. Set `pi[i] = j`.
4. Return `pi`.

### Time Complexity

- **O(N)**: Although there is a while loop inside the for loop, the variable `j` increases by at most 1 in each iteration of the for loop (step 3b). The while loop (step 3a) only decreases `j`. Since `j` cannot be negative, the total number of decreases across the entire algorithm cannot exceed the total number of increases. Thus, the amortized complexity is linear.

### Space Complexity

- **O(N)**: To store the `pi` array.

### Why This Is Optimal

- We process each character effectively constant times on average. This is the theoretical lower bound since we must output `N` integers.

![Algorithm Visualization](../images/STC-001/algorithm-visualization.png)
![Algorithm Steps](../images/STC-001/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Use the sample: `s = "ababa"`

We maintain:
- `pi`: array to store results
- `j`: length of current matching prefix
- `i`: current index being processed

Initialize:
- `pi = [0, 0, 0, 0, 0]`
- `j = 0`
- `i` starts from 1

| Step | i | s[i] | j (start) | s[j] | Action | j (end) | pi[i] |
| ---: | :-: | :-: | :-: | :-: | :--- | :-: | :-: |
| 1 | 1 | 'b' | 0 | 'a' | Mismatch, j=0. No backtrack possible. | 0 | 0 |
| 2 | 2 | 'a' | 0 | 'a' | Match! j++ | 1 | 1 |
| 3 | 3 | 'b' | 1 | 'b' | Match! j++ | 2 | 2 |
| 4 | 4 | 'a' | 2 | 'a' | Match! j++ | 3 | 3 |

Final `pi` array: `[0, 0, 1, 2, 3]`

Let's try a trickier one: `s = "aabaa"`

| Step | i | s[i] | j (start) | s[j] | Action | j (end) | pi[i] |
| ---: | :-: | :-: | :-: | :-: | :--- | :-: | :-: |
| 1 | 1 | 'a' | 0 | 'a' | Match! j++ | 1 | 1 |
| 2 | 2 | 'b' | 1 | 'a' | Mismatch. j=pi[0]=0. s[2]!=s[0]. | 0 | 0 |
| 3 | 3 | 'a' | 0 | 'a' | Match! j++ | 1 | 1 |
| 4 | 4 | 'a' | 1 | 'a' | Match! j++ | 2 | 2 |

Final `pi`: `[0, 1, 0, 1, 2]`

![Example Visualization](../images/STC-001/example-1.png)

## ✅ Proof of Correctness

### Invariant

At the start of iteration `i`, `j` holds the value of `pi[i-1]`. This means `s[0...j-1]` is the longest proper prefix of `s[0...i-1]` that is also a suffix of `s[0...i-1]`.

### Why the approach is correct

1. **Extension**: If `s[i] == s[j]`, then the prefix of length `j` can be extended by one character. The new longest prefix-suffix for `s[0...i]` will have length `j+1`.
2. **Backtracking**: If `s[i] != s[j]`, we cannot extend the prefix of length `j`. We need to find the next longest prefix of `s[0...i-1]` that is also a suffix. By definition, this length is `pi[j-1]`. We update `j = pi[j-1]` and repeat the check. This is valid because any proper prefix of a proper prefix is also a proper prefix of the original string.
3. **Termination**: The backtracking reduces `j`. Since `j` is bounded below by 0, this process must terminate.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: String Matching (KMP)**
  - How would you use this `pi` array to find all occurrences of `s` in a text `t`?
  - *Answer:* Construct a new string `P = s + '#' + t`. Compute `pi` for `P`. Any position where `pi[k] == |s|` indicates a match.

- **Extension 2: Smallest Period**
  - Can you find the length of the smallest period of string `s`?
  - *Answer:* Let `len = |s|` and `k = pi[len-1]`. If `len % (len - k) == 0` and `k > 0`, the period length is `len - k`.

- **Extension 3: Counting Occurrences of Each Prefix**
  - How many times does each prefix `s[0...i]` occur in `s`?
  - *Answer:* This can be computed using the `pi` array in O(N) by propagating counts backwards.

### Common Mistakes to Avoid

1. **Off-by-one errors in Initialization**
   - ❌ Starting loop from `i=0`.
   - ✅ `pi[0]` is always 0. Start loop from `i=1`.

2. **Incorrect Backtracking Condition**
   - ❌ Using `if` instead of `while` for backtracking.
   - ✅ Must use `while` because we might need to backtrack multiple steps (e.g., `j -> pi[j-1] -> pi[pi[j-1]-1] ...`).

3. **Mixing 0-based and 1-based indexing**
   - ❌ Confusing length `j` with index `j`.
   - ✅ In 0-based indexing, a prefix of length `j` ends at index `j-1`. The character *after* this prefix is at index `j`. This is why we compare `s[i]` with `s[j]`.

4. **Forgetting to reset `j`**
   - ❌ Not updating `j` correctly inside the loop.
   - ✅ `j` maintains state across iterations of `i`.

## Related Concepts

- **KMP Algorithm**: The direct application of the prefix function.
- **Z-Algorithm**: Another way to preprocess strings for matching, computing the Z-array.
- **Finite Automata**: The KMP algorithm can be viewed as building a DFA.
- **Rolling Hash (Rabin-Karp)**: An alternative probabilistic approach to string matching.
