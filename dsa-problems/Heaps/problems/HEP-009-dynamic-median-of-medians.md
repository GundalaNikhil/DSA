---
problem_id: HEP_DYNAMIC_MEDIAN_OF_MEDIANS__7312
display_id: HEP-009
slug: dynamic-median-of-medians
title: "Dynamic Median of Medians"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Medians
  - Union-Find
tags:
  - heaps
  - median
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-009: Dynamic Median of Medians

## Problem Statement

Maintain multiple groups of numbers. Each group has its own median (lower middle if even). You must support the following operations:

- `NEW id m` followed by `m` integers: create a new group
- `ADD id x`: insert `x` into group `id`
- `MERGE id1 id2`: merge group `id2` into `id1`
- `QUERY`: output the median of the current group medians

If no groups contain elements, output `EMPTY`.

![Problem Illustration](../images/HEP-009/problem-illustration.png)

## Input Format

- First line: integer `q` (number of operations)
- Next operations:
  - `NEW id m` then a line with `m` integers
  - `ADD id x`
  - `MERGE id1 id2`
  - `QUERY`

## Output Format

- For each `QUERY`, output one line with the median of medians or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= id <= 100000`
- Total elements across all groups `<= 100000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
4
NEW 1 2
1 3
NEW 2 1
2
MERGE 1 2
QUERY
```

**Output:**

```
2
```

**Explanation:**

After merging, group 1 contains [1, 2, 3]. Its median is 2, which is also the median of all group medians.

![Example Visualization](../images/HEP-009/example-1.png)

## Notes

- Maintain two heaps for each group to track its median
- Track medians globally using another pair of heaps
- Merge smaller group into larger group for efficiency
- Time complexity: O((n + q) log n)
- Space complexity: O(n)

## Related Topics

Heaps, Median Maintenance, Union-Find, Merging

---

## Solution Template

### Java


### Python


### C++


### JavaScript

