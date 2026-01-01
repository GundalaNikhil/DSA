---
problem_id: TRI_PREFIX_FREE_CHECK__6183
display_id: TRI-012
slug: prefix-free-after-inserts
title: "Prefix-Free Check After Inserts"
difficulty: Medium
difficulty_score: 48
topics:
  - Trie
  - String
tags:
  - trie
  - prefix-free
  - phone-numbers
premium: true
subscription_tier: basic
---

# TRI-012: Prefix-Free Check After Inserts

## 📋 Problem Summary

Insert phone numbers (digit strings) into a trie. After each insertion, report whether the set remains prefix-free (no number is a prefix of another).

## 🌍 Real-World Scenario

**Telephone Routing Systems**

In telecom systems, phone number routing must be prefix-free to avoid ambiguity. If "911" and "9112345" both exist, when someone dials "911234...", the system won't know if they're calling "911" or continuing to dial "9112345".

## Detailed Explanation

A set is prefix-free if no string is a prefix of another. After each insertion, check:
1. Is the new number a prefix of any existing number?
2. Is any existing number a prefix of the new number?

## Naive Approach

After each insert, compare new number against all existing numbers: O(n²×L)

## Optimal Approach

Use trie. During insertion:
- If we reach end of new number but node has children → NOT prefix-free
- If we pass through an end-of-word node before finishing → NOT prefix-free
- Otherwise → prefix-free

**Prefix-Free Checking:**

```
Example: Insert ["911", "9112345", "123"]

Insert "911":
Root
  |
  9
  |
  1
  |
  1 (end) ← Prefix-free so far ✓

Insert "9112345":
Root
  |
  9
  |
  1
  |
  1 (end) ← We pass through existing end! ✗
  |
  2 → 3 → 4 → 5 (would be end)

Result: FALSE (9112345 extends 911)

Reset and try different order:

Insert "123":
Root
  |
  1
  |
  2
  |
  3 (end) ← Prefix-free ✓

Insert "911":
Root
  |
  +-- 1
  |   |
  |   2 → 3 (end)
  |
  +-- 9
      |
      1 → 1 (end) ← No conflicts, prefix-free ✓

Insert "9112345":
Root
  |
  +-- 1 → 2 → 3 (end)
  |
  +-- 9
      |
      1
      |
      1 (end) ← We pass through existing end! ✗
      |
      2 → 3 → 4 → 5

Result: [true, true, false]
```

**Time**: O(L) per insert
**Space**: O(N×L)

## Implementations

### Java

### Python

### C++

### JavaScript

### Common Mistakes

1. Not checking both directions (prefix and extension)
2. Forgetting to mark isEnd after successful insert
3. Not returning false when node has children at end

## Related Concepts
- Prefix-Free Codes (Huffman Coding)
- Telephone Routing
- Trie Data Structure


## Constraints

- `1 <= n <= 10^5` (number of insertions)
- `1 <= length of each phone number <= 15`
- Phone numbers consist only of digits (0-9)
- Phone numbers may have leading zeros