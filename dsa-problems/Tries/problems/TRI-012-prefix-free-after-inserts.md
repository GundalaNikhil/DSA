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
time_limit: 2000
memory_limit: 256
---

# TRI-012: Prefix-Free Check After Inserts

## Problem Statement

You are building a phone number routing system. Insert phone numbers (digit strings) one by one into your system. After each insertion, determine whether the set of phone numbers remains **prefix-free**.

A set of strings is **prefix-free** if no string in the set is a prefix of another string in the set.

![Problem Illustration](../images/TRI-012/problem-illustration.png)

## Input Format

- First line: integer `n` (number of phone numbers to insert)
- Next `n` lines: each contains a single phone number (string of digits)

## Output Format

Return an array of booleans where the i-th value indicates whether the set remains prefix-free after inserting the i-th phone number.

Format: `[true,false,true,...]`

## Constraints

- `1 <= n <= 10^5` (number of insertions)
- `1 <= length of each phone number <= 15`
- Phone numbers consist only of digits (0-9)
- Phone numbers may have leading zeros

## Example

**Input:**

```
3
91
911
912
```

**Output:**

```
[true,false,false]
```

**Explanation:**

1. Insert "91": Set = {"91"}. No other numbers exist, so prefix-free → **true**
2. Insert "911": Set = {"91", "911"}. "91" is a prefix of "911" → **false**
3. Insert "912": Set = {"91", "911", "912"}. "91" is still a prefix of both "911" and "912" → **false**

![Example Visualization](../images/TRI-012/example-1.png)

## Notes

- A phone number is considered a prefix of itself, but this doesn't violate prefix-free (we only care about **distinct** strings)
- Once the set becomes non-prefix-free, all subsequent insertions will also be non-prefix-free (unless stated otherwise in advanced variants)
- Use a trie to efficiently check prefix relationships during insertion

## Related Topics

Trie, String, Prefix Matching, Telecommunications

---

## Solution Template

### Java


### Python


### C++


### JavaScript

