---
problem_id: PRB_SKIP_LIST_EXPECTED_HEIGHT__6591
display_id: PRB-007
slug: skip-list-expected-height
title: "Skip List Expected Height"
difficulty: Medium
difficulty_score: 45
topics:
  - Probability
  - Data Structures
  - Logs
tags:
  - probability
  - skip-list
  - expectation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-007: Skip List Expected Height

## Problem Statement

A skip list promotes each node to the next level independently with probability `p`. Given `n` inserted elements, approximate the expected maximum height of the skip list using:

```
H = log(n) / log(1/p)
```

Output `H`.

![Problem Illustration](../images/PRB-007/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `p`

## Output Format

- Single floating-point number: expected height

## Constraints

- `1 <= n <= 10^6`
- `0 < p < 1`

## Example

**Input:**

```
1024 0.5
```

**Output:**

```
10
```

**Explanation:**

log_{1/p}(n) = log_2(1024) = 10.

![Example Visualization](../images/PRB-007/example-1.png)

## Notes

- Use natural logs in computation
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Skip Lists, Expected Value, Logarithms

---

## Solution Template

### Java


### Python


### C++


### JavaScript

