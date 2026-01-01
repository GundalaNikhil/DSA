---
problem_id: HSH_SUBSTRING_HASH_UNDER_EDITS__7394
display_id: HSH-009
slug: substring-hash-under-edits
title: "Substring Hash Under Edits"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Data Structures
  - Segment Tree
tags:
  - hashing
  - segment-tree
  - updates
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-009: Substring Hash Under Edits

## Problem Statement

Support two types of operations on a string `s`:

1. **Update**: Change character at position `i` to character `c`
2. **Query**: Return the polynomial hash of substring `s[l..r]`

Use a data structure (Segment Tree or Fenwick Tree) to handle updates and queries efficiently.

![Problem Illustration](../images/HSH-009/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of operations)
- Next `q` lines: either
  - `U i c` (update position i to character c)
  - `Q l r` (query hash of substring [l, r])

## Output Format

- For each query operation, output the hash value on a new line

## Constraints

- `1 <= |s|, q <= 2*10^5`
- `0 <= i, l, r < |s|`
- Character `c` is a lowercase English letter

## Example

**Input:**

```
abc
3
Q 0 2
U 1 x
Q 0 2
```

**Output:**

```
549818522
650293847
```

**Explanation:**

Initial string: "abc"

Operation 1: Query hash of "abc" (positions 0-2)
Operation 2: Update position 1 to 'x' → string becomes "axc"
Operation 3: Query hash of "axc" (positions 0-2)

![Example Visualization](../images/HSH-009/example-1.png)

## Notes

- Use Segment Tree with each node storing hash value
- Precompute powers of base for combination
- Update: O(log n), Query: O(log n)
- Total time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Segment Tree, Fenwick Tree, Hashing, Dynamic Updates

---

## Solution Template

### Java


### Python


### C++


### JavaScript

