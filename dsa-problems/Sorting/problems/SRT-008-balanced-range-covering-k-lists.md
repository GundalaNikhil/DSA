---
problem_id: SRT_BALANCED_RANGE_COVERING_K_LISTS__5746
display_id: SRT-008
slug: balanced-range-covering-k-lists
title: "Balanced Range Covering K Lists"
difficulty: Medium
difficulty_score: 58
topics:
  - Sorting
  - Sliding Window
  - Heaps
tags:
  - sorting
  - sliding-window
  - heap
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-008: Balanced Range Covering K Lists

## Problem Statement

You are given `k` sorted lists. Find an interval `[L, R]` of minimum length that contains at least two numbers from each list. If a list has only one number, that single number must appear in the interval.

Return any one optimal interval. If no such interval exists, output `NONE`.

![Problem Illustration](../images/SRT-008/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` blocks:
  - First line of block: integer `m` (size of list)
  - Second line of block: `m` space-separated integers (sorted)

## Output Format

Print two space-separated integers `L R` representing the chosen interval of minimum length.
- `L` is the left endpoint (inclusive)
- `R` is the right endpoint (inclusive)

If no valid interval exists, print `NONE`.

**Note about length**: The "length" of an interval [L, R] is defined as `R - L` (the difference). For example:
- Interval [1, 5] has length 4 (not 5 elements)
- Interval [1, 3] has length 2
- You want to minimize this difference while satisfying the coverage requirement

## Constraints

- `1 <= k <= 100000`
- Total elements across all lists <= 200000
- List values fit in 32-bit signed integer

## Example

**Input:**

```
3
3
1 2 10
3
2 3 11
3
1 3 12
```

**Output:**

```
1 3
```

**Explanation:**

We have 3 lists:
- List 0: [1, 2, 10]
- List 1: [2, 3, 11]
- List 2: [1, 3, 12]

The interval [1, 3] contains:
- From List 0: 1, 2 (2 elements) ✓
- From List 1: 2, 3 (2 elements) ✓
- From List 2: 1, 3 (2 elements) ✓

The interval length is 3 - 1 = 2. This is optimal (minimum possible).

Other possible intervals that work:
- [2, 3]: length 1, contains {2}, {2,3}, {3} - List 0 only has 1! ✗
- [1, 10]: length 9, works but much longer
- [2, 11]: length 9, works but much longer

![Example Visualization](../images/SRT-008/example-1.png)

## Notes

- Merge all lists with their list IDs
- Use a sliding window to maintain counts per list
- Ensure each list contributes at least two elements
- Time complexity: O(N log N)

## Related Topics

Sliding Window, Heaps, Range Cover

---

## Solution Template
### Java


### Python


### C++


### JavaScript

