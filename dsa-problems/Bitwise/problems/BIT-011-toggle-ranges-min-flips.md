---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Array
  - Greedy
  - Flipping
tags:
  - bitwise
  - array-transformation
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-011: Toggle Ranges Minimum Flips

## Problem Statement

You may flip all bits in any chosen subarray (0 -> 1, 1 -> 0). Find the minimum number of flips required to convert binary array A into binary array B.

![Problem Illustration](../images/BIT-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated bits of A
- Third line: n space-separated bits of B

## Output Format

Print the minimum number of flips.

## Constraints

- `1 <= n <= 200000`

## Example

**Input:**
```
4
0 1 1 0
1 0 1 1
```

**Output:**
```
2
```

**Explanation:**

Mismatch segments are indices 0..1 and 3, so two flips are sufficient.

![Example Visualization](../images/BIT-011/example-1.png)

## Notes

- A flip inverts every bit in the chosen subarray.
- Count contiguous mismatch runs to minimize flips.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java



### Python



### C++



### JavaScript


