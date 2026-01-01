---
problem_id: LNK_SHUTTLE_ROUTE_ALTERNATING_REVERSE__5831
display_id: LNK-005
slug: shuttle-route-alternating-reverse
title: "Shuttle Route Alternating Reverse"
difficulty: Medium
difficulty_score: 55
topics:
  - Linked List
  - Reversal
  - Simulation
tags:
  - linked-list
  - reversal
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-005: Shuttle Route Alternating Reverse

## Problem Statement

Starting at position `l` (1-indexed), reverse every other contiguous block of length `k` in the list. The pattern is:

- Reverse `k` nodes
- Skip `k` nodes
- Reverse `k` nodes
- ...

If the final block has fewer than `k` nodes and it is a reverse turn, reverse that smaller block. Nodes before position `l` remain unchanged.

![Problem Illustration](../images/LNK-005/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: two integers `l` and `k`

## Output Format

- Single line: list values after alternating reversals

## Constraints

- `1 <= l <= n <= 100000`
- `1 <= k <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
7
1 2 3 4 5 6 7
2 2
```

**Output:**

```
1 3 2 4 5 7 6
```

**Explanation:**

Start at position 2:

- Reverse nodes [2,3] -> 3,2
- Skip nodes [4,5]
- Reverse nodes [6,7] -> 7,6

Final list: 1 -> 3 -> 2 -> 4 -> 5 -> 7 -> 6

![Example Visualization](../images/LNK-005/example-1.png)

## Notes

- Move a pointer to position `l` before processing blocks
- Toggle between reverse and skip blocks of size `k`
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Block Reversal, Simulation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

