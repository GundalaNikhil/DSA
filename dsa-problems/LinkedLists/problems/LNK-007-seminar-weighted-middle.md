---
problem_id: LNK_SEMINAR_WEIGHTED_MIDDLE__4729
display_id: LNK-007
slug: seminar-weighted-middle
title: "Seminar Weighted Middle Seat"
difficulty: Easy
difficulty_score: 28
topics:
  - Linked List
  - Prefix Sum
  - Weighted Median
tags:
  - linked-list
  - prefix-sum
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-007: Seminar Weighted Middle Seat

## Problem Statement

Each node contains a positive weight. Return the node value where the cumulative weight from the head first reaches at least half of the total weight (weighted median node).

If the total weight is odd, use the ceiling of half (i.e., `(total + 1) / 2`).

![Problem Illustration](../images/LNK-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` positive integers (node weights)

## Output Format

- Single integer: value of the weighted median node

## Constraints

- `1 <= n <= 100000`
- `1 <= weight <= 10^9`

## Example

**Input:**

```
4
2 1 3 4
```

**Output:**

```
3
```

**Explanation:**

Total weight = 10, half = 5. The prefix sums are 2, 3, 6, 10.

The first node reaching at least 5 has value 3.

![Example Visualization](../images/LNK-007/example-1.png)

## Notes

- Compute total weight in one pass
- Find the first node with prefix sum >= (total + 1) / 2
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Prefix Sums, Weighted Median

---

## Solution Template

### Java


### Python


### C++


### JavaScript

