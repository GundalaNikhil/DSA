---
problem_id: LNK_ROBOTICS_PALINDROME_ONE_SKIP__6741
display_id: LNK-014
slug: robotics-palindrome-one-skip
title: "Robotics Palindrome with One Skip"
difficulty: Medium
difficulty_score: 54
topics:
  - Linked List
  - Two Pointers
  - Palindrome
tags:
  - linked-list
  - palindrome
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-014: Robotics Palindrome with One Skip

## Problem Statement

Determine whether a singly linked list can become a palindrome after deleting at most one node. Deleting zero nodes is allowed.

![Problem Illustration](../images/LNK-014/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)

## Output Format

- Print `true` if the list can be a palindrome after at most one deletion, otherwise `false`

## Constraints

- `1 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
5
1 2 3 2 1
```

**Output:**

```
true
```

**Explanation:**

The list is already a palindrome, so zero deletions are needed.

![Example Visualization](../images/LNK-014/example-1.png)

## Notes

- You may use array conversion or reverse the second half
- Allow one mismatch and try skipping either side
- Time complexity: O(n)
- Space complexity: O(1) or O(n) depending on approach

## Related Topics

Linked Lists, Palindromes, Two Pointers

---

## Solution Template

### Java


### Python


### C++


### JavaScript

