---
problem_id: PDS_BLOOMIER_FILTER__6841
display_id: PDS-012
slug: bloomier-filter
title: "Bloomier Filter Key-Value"
difficulty: Hard
difficulty_score: 65
topics:
  - Probabilistic Data Structures
  - Bloomier Filter
  - False Positives
tags:
  - probabilistic-ds
  - bloomier
  - key-value
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-012: Bloomier Filter Key-Value

## Problem Statement

A Bloomier filter stores key-value mappings with an `r`-bit value cell. The false positive probability for a random non-key is approximately:

```
FPR = 2^{-r}
```

Given the table size `m` and bits per cell `r`, compute:

- Total memory in bits: `m * r`
- False positive probability `FPR`

![Problem Illustration](../images/PDS-012/problem-illustration.png)

## Input Format

- Single line: integers `m` and `r`

## Output Format

- Two values: `memory_bits` and `FPR`

## Constraints

- `1 <= m <= 10^6`
- `1 <= r <= 32`

## Example

**Input:**

```
6 4
```

**Output:**

```
24 0.062500
```

**Explanation:**

Memory = 6 * 4 = 24 bits, FPR = 1/16 = 0.0625.

![Example Visualization](../images/PDS-012/example-1.png)

## Notes

- Use double precision for FPR
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Bloomier Filter, Key-Value Sketches

---

## Solution Template

### Java


### Python


### C++


### JavaScript

