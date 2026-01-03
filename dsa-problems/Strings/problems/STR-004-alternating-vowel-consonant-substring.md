---
problem_id: STR_ALTERNATING_VOWEL_CONSONANT_SUBSTRING__1004
display_id: STR-004
slug: alternating-vowel-consonant-substring
title: "Alternating Vowel-Consonant Substring"
difficulty: Medium
difficulty_score: 32
topics:
  - String Manipulation
  - Sliding Window
tags:
  - pattern-matching
  - vowel-consonant
  - substring
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-004: Alternating Vowel-Consonant Substring

## Problem Statement

Given a string `s` of lowercase English letters, find the longest substring where vowels and consonants strictly alternate. Treat 'y' as a consonant.

Return both the length and one such longest substring.

## Input Format

- A single string `s` (1 ≤ |s| ≤ 2 × 10^5)

## Output Format

- First line: Integer representing the length
- Second line: One longest alternating substring

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `s` contains only lowercase English letters
- Vowels: a, e, i, o, u (y is consonant)

## Example 1

**Input:**

```
abracadabra
```

**Output:**

```
3
ada
```

**Explanation:**

- "ada" has alternating pattern: a(vowel), d(consonant), a(vowel)
- Length 3 is the maximum alternating substring

## Example 2

**Input:**

```
aaa
```

**Output:**

```
1
a
```

**Explanation:**

- No alternating pattern possible with all vowels
- Single character has length 1

## Notes

- Use sliding window with reset on pattern break
- O(n) time complexity with single pass
- Track current alternation status with boolean flag
