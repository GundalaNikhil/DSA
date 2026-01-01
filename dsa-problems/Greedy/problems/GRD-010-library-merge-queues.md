---
problem_id: GRD_LIBRARY_MERGE_QUEUES__8135
display_id: GRD-010
slug: library-merge-queues
title: "Library Merge Queues"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Heap
  - Merge K Sorted Lists
tags:
  - greedy
  - heap
  - priority-queue
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-010: Library Merge Queues

## Problem Statement

You have `k` sorted queues of book IDs (integers). You need to merge them into a single sorted stream with a constraint: **no book ID can appear more than twice consecutively** in the output.

If a book ID would appear for the third time in a row, skip it and move to the next available different ID. Continue this process until all queues are processed.

Return the merged stream as a list.

![Problem Illustration](../images/GRD-010/problem-illustration.png)

## Input Format

- First line: integer `k` (number of queues)
- Next `k` lines: each line starts with an integer `len` (queue length), followed by `len` sorted integers

## Output Format

- Single line with space-separated integers representing the merged stream

## Constraints

- `1 <= k <= 100`
- Total elements across all queues `<= 2*10^5`
- All queues are sorted in non-decreasing order
- Book IDs are integers in range `[1, 10^9]`

## Example

**Input:**

```
3
3 1 1 1
2 1 2
1 2
```

**Output:**

```
1 1 1 2 2
```

**Explanation:**

Queues:

- Queue 0: [1, 1, 1]
- Queue 1: [1, 2]
- Queue 2: [2]

Merge process:

1. Take 1 from queue 0 → output: [1], last two: [1]
2. Take 1 from queue 0 → output: [1, 1], last two: [1, 1]
3. Cannot take another 1 (would be third consecutive). Take 2 from queue 1 → output: [1, 1, 2]
4. Take 1 from queue 0 → output: [1, 1, 2, 1]
5. Take 2 from queue 2 → output: [1, 1, 2, 1, 2]

The constraint ensures no more than 2 consecutive identical values.

![Example Visualization](../images/GRD-010/example-1.png)

## Notes

- Use a min-heap to track the minimum value across all queue fronts
- Track the last two values added to the output
- If the next minimum would create three consecutive identical values, temporarily skip it
- Pull from a different queue/value, then resume
- Time complexity: O(N log k) where N is total elements

## Related Topics

Merge K Sorted Lists, Heap, Priority Queue, Greedy Algorithms, Constraint Handling

---

## Solution Template

### Java


### Python


### C++


### JavaScript

