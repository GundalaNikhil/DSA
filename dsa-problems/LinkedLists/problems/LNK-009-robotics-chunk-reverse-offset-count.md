---
problem_id: LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6837
display_id: LNK-009
slug: robotics-chunk-reverse-offset-count
title: "Robotics Chunk Reverse with Offset and Reversal Count"
difficulty: Medium
difficulty_score: 55
topics:
  - Linked List
  - Reversal
  - Simulation
tags:
  - linked-list
  - reversal
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-009: Robotics Chunk Reverse with Offset and Reversal Count

## Problem Statement

Reverse nodes in groups of size `k`, but start grouping at position `s` (1-indexed). Nodes before position `s` remain unchanged. From `s` onward, reverse each full group of size `k`; any leftover tail with fewer than `k` nodes stays as-is.

Return three outputs:

- The new head of the list
- `reversal_count`: number of full groups reversed
- `sum_of_reversed_values`: sum of all node values that were part of reversed groups

![Problem Illustration](../images/LNK-009/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: two integers `k` and `s`

## Output Format

- First line: list values after reversal, space-separated
- Second line: `reversal_count`
- Third line: `sum_of_reversed_values`

## Constraints

- `0 <= n <= 100000`
- `1 <= k <= max(1, n)`
- `1 <= s <= max(1, n)`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
5
1 2 3 4 5
2 3
```

**Output:**

```
1 2 4 3 5
1
7
```

**Explanation:**

Start at position 3. The group [3, 4] is reversed, yielding 4 -> 3.

- reversal_count = 1
- sum_of_reversed_values = 3 + 4 = 7

![Example Visualization](../images/LNK-009/example-1.png)

## Notes

- Only complete groups of size `k` are reversed
- Keep running sum of values inside reversed groups
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Block Reversal, Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

