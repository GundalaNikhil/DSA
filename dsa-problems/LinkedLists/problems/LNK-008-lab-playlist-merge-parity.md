---
problem_id: LNK_LAB_PLAYLIST_MERGE_PARITY__5863
display_id: LNK-008
slug: lab-playlist-merge-parity
title: "Lab Playlist Merge by Parity"
difficulty: Medium
difficulty_score: 42
topics:
  - Linked List
  - Merge
  - Stable Ordering
tags:
  - linked-list
  - merge
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-008: Lab Playlist Merge by Parity

## Problem Statement

Merge two sorted linked lists into one list. In the output, all even-valued nodes must appear before all odd-valued nodes, while preserving the relative order among evens and among odds.

![Problem Illustration](../images/LNK-008/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first list)
- Second line: `n` space-separated integers (first list values)
- Third line: integer `m` (length of second list)
- Fourth line: `m` space-separated integers (second list values)

## Output Format

- Single line: merged list values with evens first, space-separated
- If the result is empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
1 4 7
3
2 3 10
```

**Output:**

```
4 2 10 1 7 3
```

**Explanation:**

Evens in order: 4 (list1), 2 (list2), 10 (list2)

Odds in order: 1 (list1), 7 (list1), 3 (list2)

![Example Visualization](../images/LNK-008/example-1.png)

## Notes

- A stable merge by parity keeps original order within even and odd groups
- You can build two chains (evens and odds) and concatenate
- Time complexity: O(n + m)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Merge, Partitioning

---

## Solution Template

### Java


### Python


### C++


### JavaScript

