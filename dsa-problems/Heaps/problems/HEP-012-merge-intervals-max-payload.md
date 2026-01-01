---
problem_id: HEP_MERGE_INTERVALS_MAX_PAYLOAD__6043
display_id: HEP-012
slug: merge-intervals-max-payload
title: "Merge Intervals With Max Payload"
difficulty: Medium
difficulty_score: 48
topics:
  - Heaps
  - Intervals
  - Sorting
tags:
  - heaps
  - intervals
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-012: Merge Intervals With Max Payload

## Problem Statement

You are given `n` intervals, each with a payload value. When two intervals overlap, they should be merged into a single interval `[minStart, maxEnd]`. The merged payload is the maximum payload among all intervals in that merged group.

Return the merged intervals sorted by start time.

![Problem Illustration](../images/HEP-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n` lines: three integers `start`, `end`, `payload`

## Output Format

- First line: integer `m` (number of merged intervals)
- Next `m` lines: `start end payload` for each merged interval

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= start <= end <= 10^9`
- `0 <= payload <= 10^9`

## Example

**Input:**

```
2
1 3 5
2 4 7
```

**Output:**

```
1
1 4 7
```

**Explanation:**

The intervals overlap, so they merge into [1,4] with payload max(5,7)=7.

![Example Visualization](../images/HEP-012/example-1.png)

## Notes

- Sort intervals by start time
- Extend the current interval while overlaps exist
- Track the maximum payload in the merged segment
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Intervals, Sorting, Sweeping, Heaps

---

## Solution Template

### Java


### Python


### C++


### JavaScript

