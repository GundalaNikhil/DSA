---
problem_id: ARR_LEAKY_ROOF_REINFORCE__3586
display_id: ARR-011
slug: leaky-roof-reinforcement
title: "Leaky Roof Reinforcement"
difficulty: Medium
difficulty_score: 55
topics:
  - Arrays
  - Prefix Suffix
  - Greedy
tags:
  - arrays
  - prefix-suffix
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-011: Leaky Roof Reinforcement

## Problem Statement

You can add planks to increase heights so the profile becomes non-decreasing up to a single peak and non-increasing after that peak. Find the minimum total height added.

![Problem Illustration](../images/ARR-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers height[i]

## Output Format

Print the minimum total added height.

## Constraints

- `1 <= n <= 200000`
- `0 <= height[i] <= 1000000000`

## Example

**Input:**
```
5
4 1 3 1 5
```

**Output:**
```
7
```

**Explanation:**

Choose peak at index 4 with height 5. The reinforced profile is [4, 4, 4, 4, 5],
adding 3 + 1 + 3 = 7 in total.

![Example Visualization](../images/ARR-011/example-1.png)

## Notes

- You may only increase heights, never decrease.
- The peak can be any index.

## Related Topics

Prefix Suffix, Greedy, Arrays

---

## Solution Template

### Java



### Python



### C++



### JavaScript


