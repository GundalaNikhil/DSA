---
problem_id: STR_DISTINCT_SUBSEQUENCE_CHAR_LIMIT__1012
display_id: STR-012
slug: distinct-subsequence-char-limit
title: "Distinct Subsequence Count with Character Limit"
difficulty: Medium
difficulty_score: 48
topics:
  - String Manipulation
  - Dynamic Programming
  - Subsequence
tags:
  - frequency-constraint
  - dp-optimization
  - modular-arithmetic
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-012: Distinct Subsequence Count with Character Limit

## Problem Statement

Given a string `s`, an integer `maxFreq`, and a modulus `MOD`, count the number of distinct subsequences where each character appears at most `maxFreq` times. Return the count modulo `MOD`.

The empty subsequence counts.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `maxFreq` (1 ≤ maxFreq ≤ 10)
- Third line: Integer `MOD` (prime, ≤ 10^9+7)

## Output Format

- A single integer representing the count modulo MOD

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ maxFreq ≤ 10`
- Prime `MOD ≤ 10^9+7`

## Example 1

**Input:**

```
aaa
2
1000000007
```

**Output:**

```
7
```

**Explanation:**

- Valid subsequences by position:
  - Empty: 1
  - Single 'a': positions {0}, {1}, {2} → 3
  - Double 'aa': positions {0,1}, {0,2}, {1,2} → 3
  - Triple 'aaa' excluded (freq=3 > maxFreq=2)
- Total: 7

## Notes

- DP with frequency state tracking
- Use map for sparse state representation
- Apply modulo at every step
