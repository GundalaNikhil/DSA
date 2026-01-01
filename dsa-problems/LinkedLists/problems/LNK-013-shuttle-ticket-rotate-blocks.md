---
problem_id: LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__8156
display_id: LNK-013
slug: shuttle-ticket-rotate-blocks
title: "Shuttle Ticket Rotate by Blocks"
difficulty: Medium
difficulty_score: 46
topics:
  - Linked List
  - Rotation
  - Block Processing
tags:
  - linked-list
  - rotation
  - blocks
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-013: Shuttle Ticket Rotate by Blocks

## Problem Statement

Rotate the list to the right by `k` places, but only within each block of size `b`. The list is partitioned into consecutive blocks of length `b` (the final block may be shorter). Rotate each block independently by `k % blockSize`, then concatenate the blocks in order.

![Problem Illustration](../images/LNK-013/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: two integers `b` and `k`

## Output Format

- Single line: list values after block rotations

## Constraints

- `0 <= n <= 100000`
- `1 <= b <= max(1, n)`
- `0 <= k <= 10^9`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
6
1 2 3 4 5 6
3 1
```

**Output:**

```
3 1 2 6 4 5
```

**Explanation:**

Blocks of size 3:

- [1, 2, 3] rotated right by 1 -> [3, 1, 2]
- [4, 5, 6] rotated right by 1 -> [6, 4, 5]

![Example Visualization](../images/LNK-013/example-1.png)

## Notes

- For each block, use `k % blockSize`
- The last block may be shorter but is still rotated
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Rotation, Block Processing

---

## Solution Template

### Java


### Python


### C++


### JavaScript

