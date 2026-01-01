---
problem_id: TRI_XOR_MINIMIZATION__9417
display_id: TRI-015
slug: xor-minimization-trie
title: "XOR Minimization With Trie"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - Binary Trie
  - XOR
  - Bit Manipulation
tags:
  - trie
  - xor
  - binary
  - prefix-xor
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-015: XOR Minimization With Trie

## Problem Statement

Given an array `a` of `n` non-negative integers and an integer `X`, find the minimum possible value of `(subarray_XOR) ⊕ X` over all subarrays, where `subarray_XOR` is the XOR of all elements in the subarray.

![Problem Illustration](../images/TRI-015/problem-illustration.png)

## Input Format

- First line: two integers `n` (array size) and `X` (target value)
- Second line: `n` space-separated integers representing array `a`

## Output Format

Return a single integer: the minimum value of `(subarray_XOR) ⊕ X`

## Constraints

- `1 <= n <= 2 × 10^5`
- `0 <= a[i], X <= 10^9`
- All array elements and X fit in 32-bit integers

## Example

**Input:**

```
3 3
4 1 2
```

**Output:**

```
0
```

**Explanation:**

Possible subarrays and their results:

- [4]: XOR=4, result=4⊕3=7
- [1]: XOR=1, result=1⊕3=2
- [2]: XOR=2, result=2⊕3=1
- [4,1]: XOR=4⊕1=5, result=5⊕3=6
- [1,2]: XOR=1⊕2=3, result=3⊕3=0 ← minimum!
- [4,1,2]: XOR=4⊕1⊕2=7, result=7⊕3=4

Minimum value: **0** (from subarray [1,2])

![Example Visualization](../images/TRI-015/example-1.png)

## Notes

- Use prefix XOR technique: `subarray[i,j] = prefix[j+1] ⊕ prefix[i]`
- Binary trie enables efficient XOR minimization queries
- Process prefixes sequentially, querying and inserting

## Related Topics

Binary Trie, XOR, Prefix XOR, Bit Manipulation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

