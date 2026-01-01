---
problem_id: NUM_COUNT_STRINGS_EXACT_VOWELS__6419
display_id: NUM-013
slug: count-strings-exact-vowels
title: "Count Strings With Exact Vowels"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Combinatorics
  - Modular Arithmetic
tags:
  - number-theory
  - combinatorics
  - modular
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-013: Count Strings With Exact Vowels

## Problem Statement

Count the number of strings of length `n` over lowercase English letters that contain exactly `k` vowels. Return the answer modulo `1000000007`.

Vowels are `a, e, i, o, u`.

![Problem Illustration](../images/NUM-013/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single integer: count modulo `1000000007`

## Constraints

- `1 <= n <= 1000000`
- `0 <= k <= n`

## Example

**Input:**

```
2 1
```

**Output:**

```
210
```

**Explanation:**

Choose 1 position for the vowel (C(2,1)=2), pick vowel (5 choices), pick consonant (21 choices):

2 * 5 * 21 = 210.

![Example Visualization](../images/NUM-013/example-1.png)

## Notes

- Count = C(n,k) * 5^k * 21^(n-k) mod M
- Precompute factorials and inverse factorials
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Combinatorics, Binomial Coefficients, Modular Arithmetic

---

## Solution Template

### Java


### Python


### C++


### JavaScript

