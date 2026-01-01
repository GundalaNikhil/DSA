---
problem_id: LNK_LAB_SWAP_NEIGHBORS_SKIP__5817
display_id: LNK-003
slug: lab-swap-neighbors-skip-threshold
title: "Lab Swap Neighbors with Skip and Threshold"
difficulty: Medium
difficulty_score: 45
topics:
  - Linked List
  - Two Pointers
  - Simulation
tags:
  - linked-list
  - swapping
  - constraints
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-003: Lab Swap Neighbors with Skip and Threshold

## Problem Statement

Swap nodes in pairs in a singly linked list with two constraints:

- If either node in a pair has a negative value, do not swap that pair
- You can perform at most `K` swaps total; after `K` swaps are used, all remaining pairs stay as-is

Return the new head and the number of swaps actually performed.

![Problem Illustration](../images/LNK-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `K` (maximum swaps)

## Output Format

- First line: space-separated list values after swaps
- Second line: integer swaps performed

## Constraints

- `0 <= n <= 100000`
- `0 <= K <= n / 2`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
6
1 -2 3 4 5 6
1
```

**Output:**

```
1 -2 4 3 5 6
1
```

**Explanation:**

Pairs are (1, -2), (3, 4), (5, 6).

- Pair (1, -2): contains negative, no swap
- Pair (3, 4): swap (K becomes 0)
- Pair (5, 6): K exhausted, no swap

![Example Visualization](../images/LNK-003/example-1.png)

## Notes

- A dummy head simplifies pair manipulation
- Track swap count and stop swapping once K is reached
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Pair Swapping, Constraints Handling

---

## Solution Template

### Java


### Python


### C++


### JavaScript

