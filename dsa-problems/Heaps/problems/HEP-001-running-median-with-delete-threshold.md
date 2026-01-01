---
problem_id: HEP_RUNNING_MEDIAN_DELETE_THRESHOLD__4217
display_id: HEP-001
slug: running-median-with-delete-threshold
title: "Running Median with Delete and Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Median
  - Data Streams
tags:
  - heaps
  - median
  - lazy-deletion
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-001: Running Median with Delete and Threshold

## Problem Statement

Maintain a multiset of integers under three operations:

- `ADD x`: insert `x` into the multiset
- `DEL x`: remove one occurrence of `x` if it exists
- `MEDIAN`: report the median (lower middle if size is even)

If the multiset is empty, output `EMPTY`. If the multiset size is less than a given threshold `T`, output `NA` instead of the median.

![Problem Illustration](../images/HEP-001/problem-illustration.png)

## Input Format

- First line: two integers `q` and `T` (number of operations and threshold)
- Next `q` lines: one operation (`ADD x`, `DEL x`, or `MEDIAN`)

## Output Format

- For each `MEDIAN` operation, output one line:
  - `EMPTY` if the multiset is empty
  - `NA` if size < `T`
  - Otherwise the median value (lower middle)

## Constraints

- `1 <= q <= 100000`
- `-10^9 <= x <= 10^9`
- `0 <= T <= 100000`

## Example

**Input:**

```
4 2
ADD 1
ADD 5
DEL 1
MEDIAN
```

**Output:**

```
NA
```

**Explanation:**

Operations:

- ADD 1 -> multiset {1}
- ADD 5 -> multiset {1, 5}
- DEL 1 -> multiset {5}
- MEDIAN -> size is 1 < T (2), so output NA

![Example Visualization](../images/HEP-001/example-1.png)

## Notes

- Use two heaps to track lower and upper halves
- Apply lazy deletion to handle `DEL` efficiently
- Each operation can be processed in O(log n)
- Space complexity: O(n)

## Related Topics

Heaps, Median Maintenance, Lazy Deletion, Data Streams

---

## Solution Template

### Java


### Python


### C++


### JavaScript

