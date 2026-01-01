---
problem_id: PDS_MISRA_GRIES__9624
display_id: PDS-005
slug: misra-gries
title: "Frequent Items with Misra-Gries"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - Streaming
  - Frequency Estimation
tags:
  - probabilistic-ds
  - misra-gries
  - streaming
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-005: Frequent Items with Misra-Gries

## Problem Statement

Given a stream of `n` integers and a parameter `k`, run the Misra-Gries algorithm with `k-1` counters. Output the set of candidate items after processing the stream.

If no candidates remain, print an empty line.

![Problem Illustration](../images/PDS-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers (stream)

## Output Format

- Single line: candidate items in ascending order, space-separated

## Constraints

- `1 <= n <= 10^6`
- `2 <= k <= 1000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
7 3
1 2 1 3 1 2 4
```

**Output:**

```
1 2
```

**Explanation:**

Misra-Gries keeps at most 2 counters and returns {1,2} as candidates.

![Example Visualization](../images/PDS-005/example-1.png)

## Notes

- The algorithm guarantees all items with frequency > n/k appear in the candidates
- A second pass is needed to verify true frequencies (not required here)
- Time complexity: O(n * k) in the naive implementation, O(n) with hash map

## Related Topics

Heavy Hitters, Streaming Algorithms

---

## Solution Template

### Java


### Python


### C++


### JavaScript

