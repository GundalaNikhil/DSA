---
problem_id: PDS_COUNT_MIN_SKETCH__4815
display_id: PDS-004
slug: count-min-sketch
title: "Count-Min Sketch Error Bound"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Sketches
  - Error Bounds
tags:
  - probabilistic-ds
  - sketch
  - error-bound
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-004: Count-Min Sketch Error Bound

## Problem Statement

Given desired error `epsilon` and failure probability `delta`, compute parameters for a Count-Min Sketch:

```
w = ceil(e / epsilon)
d = ceil(ln(1 / delta))
```

Output `w` and `d`.

![Problem Illustration](../images/PDS-004/problem-illustration.png)

## Input Format

- Single line: real `epsilon` and real `delta`

## Output Format

- Two integers: `w` and `d`

## Constraints

- `0 < epsilon < 1`
- `0 < delta < 1`

## Example

**Input:**

```
0.01 0.01
```

**Output:**

```
272 5
```

**Explanation:**

w = ceil(e / 0.01) = 272, d = ceil(ln(100)) = 5.

![Example Visualization](../images/PDS-004/example-1.png)

## Notes

- Use natural log
- Time complexity: O(1)

## Related Topics

Count-Min Sketch, Approximate Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

