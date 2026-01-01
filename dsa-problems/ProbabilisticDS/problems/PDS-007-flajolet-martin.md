---
problem_id: PDS_FLAJOLET_MARTIN__2749
display_id: PDS-007
slug: flajolet-martin
title: "Flajolet-Martin Bit Pattern"
difficulty: Medium
difficulty_score: 48
topics:
  - Probabilistic Data Structures
  - Flajolet-Martin
  - Distinct Count
tags:
  - probabilistic-ds
  - flajolet-martin
  - distinct-count
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-007: Flajolet-Martin Bit Pattern

## Problem Statement

Given the maximum number of trailing zeros `R` observed in hashed stream items, estimate the number of distinct elements using:

```
Estimate = 2^R / phi
```

where `phi = 0.77351`.

![Problem Illustration](../images/PDS-007/problem-illustration.png)

## Input Format

- Single line: integer `R`

## Output Format

- Single floating-point number: estimated distinct count

## Constraints

- `0 <= R <= 60`

## Example

**Input:**

```
4
```

**Output:**

```
20.684930
```

**Explanation:**

Estimate = 16 / 0.77351 = 20.68493.

![Example Visualization](../images/PDS-007/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Flajolet-Martin, Distinct Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

