---
problem_id: QUE_ASSEMBLY_LINE_BUFFER_SWAP__9053
display_id: QUE-016
slug: assembly-line-buffer-swap
title: "Assembly Line Buffer Swap"
difficulty: Easy
difficulty_score: 29
topics:
  - Queue
  - Simulation
  - In-Place
tags:
  - queue
  - swap
  - simulation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-016: Assembly Line Buffer Swap

## Problem Statement

An assembly line has two buffers, each represented by a queue of equal length. Swap their contents using only queue operations.

Given the two queues, output their contents after the swap.

![Problem Illustration](../images/QUE-016/problem-illustration.png)

## Input Format

- First line: integer `n` (length of each queue)
- Second line: `n` space-separated integers (Queue 1, front to back)
- Third line: `n` space-separated integers (Queue 2, front to back)

## Output Format

- First line: Queue 1 after the swap
- Second line: Queue 2 after the swap

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
2
4 5
7 8
```

**Output:**

```
7 8
4 5
```

**Explanation:**

After swapping, the entire contents of the queues are exchanged.

![Example Visualization](../images/QUE-016/example-1.png)

## Notes

- The queues have equal length
- Use only enqueue and dequeue operations conceptually
- Time complexity: O(n)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Simulation, In-Place Algorithms

---

## Solution Template

### Java


### Python


### C++


### JavaScript

