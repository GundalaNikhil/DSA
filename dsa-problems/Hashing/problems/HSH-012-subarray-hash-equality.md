---
problem_id: HSH_SUBARRAY_HASH_EQUALITY__6271
display_id: HSH-012
slug: subarray-hash-equality
title: "Subarray Hash Equality (Integers)"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Arrays
  - Rolling Hash
tags:
  - hashing
  - array
  - subarray
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-012: Subarray Hash Equality (Integers)

## Problem Statement

Given an integer array and queries, treat the array as a "string" where each element is a character. Build a rolling hash to support equality checks between subarrays.

Each query asks: are subarrays `a[l1..r1]` and `a[l2..r2]` equal?

![Problem Illustration](../images/HSH-012/problem-illustration.png)

## Input Format

- First line: integer `n` (array size)
- Second line: `n` space-separated integers (array elements)
- Third line: integer `q` (number of queries)
- Next `q` lines: four integers `l1 r1 l2 r2`

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= n <= 2*10^5`
- `1 <= q <= 2*10^5`
- `-10^9 <= a[i] <= 10^9`
- `0 <= l1 <= r1 < n`
- `0 <= l2 <= r2 < n`

## Example

**Input:**

```
4
1 2 1 2
2
0 1 2 3
0 0 2 2
```

**Output:**

```
true
true
```

**Explanation:**

Array: [1, 2, 1, 2]

Query 1: a[0..1] = [1, 2], a[2..3] = [1, 2] → equal → true
Query 2: a[0..0] = [1], a[2..2] = [1] → equal → true

![Example Visualization](../images/HSH-012/example-1.png)

## Notes

- Map integers to unique values (handle negative numbers)
- Use polynomial rolling hash
- Precompute prefix hashes
- Answer queries in O(1) after O(n) preprocessing
- Time complexity: O(n + q)
- Space complexity: O(n)

## Related Topics

Rolling Hash, Arrays, Subarray Comparison, Integer Hashing

---

## Solution Template

### Java


### Python


### C++


### JavaScript

