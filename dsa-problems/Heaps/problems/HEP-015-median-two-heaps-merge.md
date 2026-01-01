---
problem_id: HEP_MEDIAN_TWO_HEAPS_MERGE__4476
display_id: HEP-015
slug: median-two-heaps-merge
title: "Median of Two Heaps After Merge"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
  - Median
  - Data Structures
tags:
  - heaps
  - median
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-015: Median of Two Heaps After Merge

## Problem Statement

You are given the contents of a max-heap and a min-heap (as arrays). Treat them as two multisets. Compute the median of all elements after merging both sets.

If the total number of elements is odd, the median is the middle element. If it is even, the median is the average of the two middle elements.

![Problem Illustration](../images/HEP-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers (max-heap contents)
- Third line: `m` integers (min-heap contents)

## Output Format

- Single number: the median (use `.5` if needed)

## Constraints

- `0 <= n, m <= 200000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
2 2
1 3
2 4
```

**Output:**

```
2.5
```

**Explanation:**

Merged values are [1,2,3,4]. Median is (2 + 3) / 2 = 2.5.

![Example Visualization](../images/HEP-015/example-1.png)

## Notes

- Use two heaps to balance all elements
- Keep size difference at most 1
- Time complexity: O((n+m) log(n+m))
- Space complexity: O(n+m)

## Related Topics

Heaps, Median Maintenance, Data Structures

---

## Solution Template

### Java


### Python


### C++


### JavaScript

