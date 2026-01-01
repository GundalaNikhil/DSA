---
problem_id: PDS_XOR_FILTERS__7789
display_id: PDS-013
slug: xor-filters
title: "XOR Filters"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - XOR Filters
  - False Positives
tags:
  - probabilistic-ds
  - xor-filter
  - false-positives
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-013: XOR Filters

## Problem Statement

An XOR filter stores fingerprints of `b` bits. The false positive rate is approximately:

```
FPR = 2^{-b}
```

Assume the filter uses `ceil(1.23 * n)` cells. Given `n` and `b`, compute:

- Total memory bits: `ceil(1.23 * n) * b`
- False positive rate `FPR`

![Problem Illustration](../images/PDS-013/problem-illustration.png)

## Input Format

- Single line: integers `n` and `b`

## Output Format

- Two values: `memory_bits` and `FPR`

## Constraints

- `1 <= n <= 10^6`
- `1 <= b <= 16`

## Example

**Input:**

```
1000 8
```

**Output:**

```
9840 0.003906
```

**Explanation:**

Cells = ceil(1.23 * 1000) = 1230. Memory = 1230 * 8 = 9840 bits. FPR = 1/256.

![Example Visualization](../images/PDS-013/example-1.png)

## Notes

- Use double precision for FPR
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

XOR Filters, Fingerprints, Approximate Membership

---

## Solution Template

### Java


### Python


### C++


### JavaScript

