---
problem_id: GRD_ROBOTICS_MEDIAN_BATCHES_STALE__4276
display_id: GRD-015
slug: robotics-median-after-batches-stale
title: "Robotics Median After Batches with Stale Filter"
difficulty: Medium
difficulty_score: 60
topics:
  - Heap
  - Two Heaps
  - Median Finding
  - Data Structures
tags:
  - heap
  - two-heaps
  - median
  - data-structures
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-015: Robotics Median After Batches with Stale Filter

## Problem Statement

Numbers arrive in batches from robot sensors. A value becomes **"stale"** once it has appeared more than `t` times in total across all batches seen so far. Stale values must be excluded from median calculations.

After processing each batch, report the median of all **non-stale** values seen so far. If all values are stale (or no values exist), output `"NA"`.

**Median definition**:

- If count is odd: middle element
- If count is even: average of two middle elements (round down)

![Problem Illustration](../images/GRD-015/problem-illustration.png)

## Input Format

- First line: two integers `k t` (number of batches and staleness threshold)
- Next `k` lines: each line starts with integer `m` (batch size), followed by `m` integers

## Output Format

- `k` space-separated outputs: median after each batch (or "NA" if no valid values)

## Constraints

- `1 <= k <= 1000`
- `1 <= t <= 10^5`
- Total numbers across all batches `<= 2*10^5`
- Values are integers in range `[-10^9, 10^9]`

## Example

**Input:**

```
3 2
3 5 5 1
2 5 3
2 8 9
```

**Output:**

```
5 3 6
```

**Explanation:**

Threshold t = 2 (values appearing > 2 times become stale)

**After Batch 1: [5, 5, 1]**

- Frequency: {5:2, 1:1}
- Non-stale values: [5, 5, 1] (none exceed threshold)
- Sorted: [1, 5, 5]
- Median: 5

**After Batch 2: [5, 5, 1] + [5, 3]**

- Frequency: {5:3, 1:1, 3:1}
- Value 5 appears 3 times > t=2, so it's stale
- Non-stale values: [1, 3]
- Sorted: [1, 3]
- For even count, we take the upper median: 3

**After Batch 3: [1, 3] + [8, 9]** (excluding stale 5)

- Frequency: {5:3 (stale), 1:1, 3:1, 8:1, 9:1}
- Non-stale values: [1, 3, 8, 9]
- Sorted: [1, 3, 8, 9]
- For even count (4 values), median is the average of the two middle values (3 and 8): (3+8)/2 = 5.5, rounded down = 5

The median calculation uses the upper median for pairs and rounds down for averages.

![Example Visualization](../images/GRD-015/example-1.png)

## Notes

- Use two heaps (max-heap for lower half, min-heap for upper half) to maintain median
- Track frequency map to identify stale values
- Use lazy deletion: when a value becomes stale, remove it from heaps
- After each batch, rebalance heaps and compute median
- Time complexity: O(N log N) where N is total numbers

## Related Topics

Two Heaps, Median Finding, Lazy Deletion, Frequency Map, Data Structures

---

## Solution Template

### Java


### Python


### C++


### JavaScript

