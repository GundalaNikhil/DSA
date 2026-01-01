---
problem_id: STK_BIKE_REPAIR_PLATES__5937
display_id: STK-015
slug: bike-repair-plates
title: "Bike Repair Plates"
difficulty: Medium
difficulty_score: 47
topics:
  - Stack
  - Monotonic Stack
  - Simulation
tags:
  - stack
  - monotonic
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-015: Bike Repair Plates

## Problem Statement

You have a stack of metal plates with diameters, listed from top to bottom. Plates are removed one by one from the top. If a plate is smaller than a plate beneath it at the moment that plate is revealed, the lower plate is marked unsafe.

Count how many plates become unsafe during the entire removal process.

![Problem Illustration](../images/STK-015/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (diameters, top to bottom)

## Output Format

- Single integer: number of unsafe plates

## Constraints

- `1 <= n <= 200000`
- `1 <= d[i] <= 10^9`

## Example

**Input:**

```
3
5 2 4
```

**Output:**

```
1
```

**Explanation:**

When the top plate 5 is removed, 2 is revealed (safe). When 2 is removed, 4 is revealed and marked unsafe because 2 < 4.

![Example Visualization](../images/STK-015/example-1.png)

## Notes

- Scan from top to bottom
- Track the last removed plate diameter
- A plate is unsafe if it is larger than the plate removed just above it
- Time complexity: O(n)

## Related Topics

Stack Simulation, Monotonic Patterns, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

