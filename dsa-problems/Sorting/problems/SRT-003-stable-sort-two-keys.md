---
problem_id: SRT_STABLE_SORT_TWO_KEYS__5920
display_id: SRT-003
slug: stable-sort-two-keys
title: "Stable Sort By Two Keys"
difficulty: Easy
difficulty_score: 30
topics:
  - Sorting
  - Stability
  - Records
tags:
  - sorting
  - stable-sort
  - records
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-003: Stable Sort By Two Keys

## Problem Statement

You are given `n` records, each with keys `(key1, key2)`. Sort the records by:

1. `key1` ascending
2. `key2` ascending

If two records have identical `(key1, key2)` values, their original order must be preserved.

![Problem Illustration](../images/SRT-003/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `key1` and `key2`

## Output Format

- `n` lines of sorted `(key1, key2)` pairs

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= key1, key2 <= 10^9`

## Example

**Input:**

```
3
1 2
1 1
0 9
```

**Output:**

```
0 9
1 2
1 1
```

**Explanation:**

Records are ordered by `key1` ascending, and for same `key1` values by `key2` ascending.

![Example Visualization](../images/SRT-003/example-1.png)

## Notes

- Use a stable sorting method
- You can sort by `(key1, key2)` and the sort will maintain stability
- Time complexity: O(n log n)
- Space complexity depends on sorting method

## Related Topics

Stable Sort, Sorting Keys, Records

---

## Solution Template
### Java


### Python


### C++


### JavaScript

