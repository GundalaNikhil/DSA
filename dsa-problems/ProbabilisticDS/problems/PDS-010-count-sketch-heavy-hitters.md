---
problem_id: PDS_COUNT_SKETCH_HEAVY_HITTERS__3405
display_id: PDS-010
slug: count-sketch-heavy-hitters
title: "Heavy Hitters with Count Sketch"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Count Sketch
  - Streaming
tags:
  - probabilistic-ds
  - count-sketch
  - heavy-hitters
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-010: Heavy Hitters with Count Sketch

## Problem Statement

Given the Count Sketch signed estimates for a single item across `d` rows, compute its frequency estimate as the median of the signed counts.

Each row provides:

- `count`: the bucket count
- `sign`: either `+1` or `-1`

The signed value is `count * sign`.

![Problem Illustration](../images/PDS-010/problem-illustration.png)

## Input Format

- First line: integer `d` (odd)
- Next `d` lines: `count` and `sign`

## Output Format

- Single integer: the median of signed counts

## Constraints

- `1 <= d <= 101`, `d` is odd
- `count` fits in 32-bit signed integer
- `sign` is either -1 or 1

## Example

**Input:**

```
3
10 1
9 -1
11 1
```

**Output:**

```
10
```

**Explanation:**

Signed counts are [10, -9, 11]. Median is 10.

![Example Visualization](../images/PDS-010/example-1.png)

## Notes

- For odd `d`, the median is the middle after sorting
- Time complexity: O(d log d)
- Space complexity: O(d)

## Related Topics

Count Sketch, Heavy Hitters, Streaming

---

## Solution Template

### Java


### Python


### C++


### JavaScript

