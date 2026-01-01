---
problem_id: PDS_PERFECT_HASHING_RANDOM__6203
display_id: PDS-014
slug: perfect-hashing-random
title: "Perfect Hashing via Randomization"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Perfect Hashing
  - Randomization
tags:
  - probabilistic-ds
  - perfect-hashing
  - randomized
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-014: Perfect Hashing via Randomization

## Problem Statement

In two-level perfect hashing (FKS), if bucket sizes are `s_1, s_2, ..., s_t`, the total second-level table size is:

```
S = sum s_i^2
```

Compute `S` and report whether `S <= 4n`.

![Problem Illustration](../images/PDS-014/problem-illustration.png)

## Input Format

- First line: integer `n` (number of keys) and integer `t` (number of buckets)
- Second line: `t` integers (bucket sizes)

## Output Format

- Two values: `S` and `YES` if `S <= 4n`, otherwise `NO`

## Constraints

- `1 <= n <= 10^6`
- `1 <= t <= n`
- Sum of bucket sizes = n

## Example

**Input:**

```
6 3
2 1 3
```

**Output:**

```
14 YES
```

**Explanation:**

S = 4 + 1 + 9 = 14, and 4n = 24, so YES.

![Example Visualization](../images/PDS-014/example-1.png)

## Notes

- Use 64-bit integers for S
- Time complexity: O(t)

## Related Topics

Perfect Hashing, FKS, Randomization

---

## Solution Template

### Java


### Python


### C++


### JavaScript

