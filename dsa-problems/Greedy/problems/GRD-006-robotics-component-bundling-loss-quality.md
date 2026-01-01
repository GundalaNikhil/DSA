---
problem_id: GRD_ROBOTICS_COMPONENT_BUNDLING__7259
display_id: GRD-006
slug: robotics-component-bundling-loss-quality
title: "Robotics Component Bundling with Loss and Quality Score"
difficulty: Medium
difficulty_score: 60
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
  - Simulation
tags:
  - greedy
  - heap
  - priority-queue
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-006: Robotics Component Bundling with Loss and Quality Score

## Problem Statement

You have `n` robot parts, where each part `i` has:

- Weight `w[i]`
- Quality score `q[i]`

You can bundle two parts together using the following rules:

- **Weight calculation**: When bundling parts with weights `w_big` and `w_small` (where `w_big >= w_small`), the new weight is: `w_big + w_small - floor(0.1 × w_small)`
  - This represents a 10% material loss from the smaller part
- **Quality calculation**: When bundling parts with qualities `q[i]` and `q[j]`, the new quality is: `min(q[i], q[j]) - 1`
  - Quality degrades by 1 due to the bundling process

**Constraint**: All intermediate bundles must maintain quality >= T (threshold), otherwise they become unusable.

Your goal is to bundle all parts into a single component while maximizing the final weight. Return the maximum achievable weight, or `-1` if no valid bundling sequence exists.

![Problem Illustration](../images/GRD-006/problem-illustration.png)

## Input Format

- First line: two integers `n T` (number of parts and quality threshold)
- Second line: `n` space-separated integers representing weights `w[0], w[1], ..., w[n-1]`
- Third line: `n` space-separated integers representing qualities `q[0], q[1], ..., q[n-1]`

## Output Format

- Single integer: maximum final weight achievable, or `-1` if impossible

## Constraints

- `1 <= n <= 2*10^5`
- `1 <= w[i] <= 10^9`
- `1 <= q[i] <= 100`
- `1 <= T <= 100`

## Example

**Input:**

```
3 5
4 3 2
10 8 6
```

**Output:**

```
8
```

**Explanation:**

Parts: weights [4, 3, 2], qualities [10, 8, 6]
Threshold: T = 5

Valid bundling sequence:

1. Bundle parts with weights 3 and 2, qualities 8 and 6:

   - New weight: 3 + 2 - floor(0.1 × 2) = 5 - 0 = 5
   - New quality: min(8, 6) - 1 = 5 (meets threshold!)
   - Now have: [4, 5] with qualities [10, 5]

2. Bundle parts with weights 4 and 3, qualities 10 and 8:

   - Weight: 4 + 3 - floor(0.1 × 3) = 7 - 0 = 7
   - Quality: min(10, 8) - 1 = 7

3. Bundle the result (weight 7, quality 7) with the part (weight 2, quality 6):
   - Weight: 7 + 2 - floor(0.1 × 2) = 9 - 0 = 9
   - Quality: min(7, 6) - 1 = 5

Final weight = 9, quality maintained at 5.

![Example Visualization](../images/GRD-006/example-1.png)

## Notes

- Use a max-heap to track (weight, quality) pairs
- Always try to bundle pairs that maintain quality >= T
- The 10% loss applies to the smaller weight
- Greedy strategy: prioritize maintaining quality while maximizing weight
- Time complexity: O(n log n) for heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Simulation, Constraint Satisfaction

---

## Solution Template

### Java


### Python


### C++


### JavaScript

