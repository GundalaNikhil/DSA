---
problem_id: NUM_COUNT_SURJECTIVE_FUNCTIONS__7773
display_id: NUM-016
slug: count-surjective-functions
title: "Count Surjective Functions"
difficulty: Medium
difficulty_score: 55
topics:
  - Number Theory
  - Combinatorics
  - Inclusion-Exclusion
tags:
  - number-theory
  - combinatorics
  - inclusion-exclusion
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-016: Count Surjective Functions

## Problem Statement

Count the number of surjective (onto) functions from an n-element set to a k-element set. Return the result modulo `1000000007`.

![Problem Illustration](../images/NUM-016/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single integer: number of surjective functions modulo `1000000007`

## Constraints

- `1 <= k <= n <= 30`

## Example

**Input:**

```
3 2
```

**Output:**

```
6
```

**Explanation:**

There are 2^3 total functions. Remove the 2 functions that map all elements to a single value.

2^3 - 2 = 6.

![Example Visualization](../images/NUM-016/example-1.png)

## Notes

- Use inclusion-exclusion: sum_{i=0..k} (-1)^i C(k,i) (k-i)^n
- Time complexity: O(k^2)
- Space complexity: O(k)

## Related Topics

Inclusion-Exclusion, Combinatorics, Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

