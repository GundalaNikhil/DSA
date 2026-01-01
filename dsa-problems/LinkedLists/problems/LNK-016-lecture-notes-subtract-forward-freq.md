---
problem_id: LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__9284
display_id: LNK-016
slug: lecture-notes-subtract-forward-freq
title: "Lecture Notes Subtract Two Numbers with Digit Frequency Analysis"
difficulty: Medium
difficulty_score: 60
topics:
  - Linked List
  - Arithmetic
  - Stacks
tags:
  - linked-list
  - subtraction
  - digits
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-016: Lecture Notes Subtract Two Numbers with Digit Frequency Analysis

## Problem Statement

Two linked lists represent non-negative integers in forward order (most significant digit first). Subtract the smaller number from the larger number, and return:

- `sign`: 1 if the result is positive, 0 if the result is zero
- The resulting number as a linked list in forward order
- An array of length 10 with the frequency of each digit (0-9) in the result

Do not use big integers for arithmetic.

![Problem Illustration](../images/LNK-016/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first number)
- Second line: `n` digits (0-9) in forward order
- Third line: integer `m` (length of second number)
- Fourth line: `m` digits (0-9) in forward order

## Output Format

- First line: integer `sign` (1 for positive result, 0 for zero)
- Second line: digits of the result in forward order, space-separated
- Third line: 10 integers for digit frequencies from 0 to 9

## Constraints

- `1 <= n, m <= 100000`
- Digits are in [0, 9]
- No leading zeros except the number zero itself

## Example

**Input:**

```
3
7 1 6
3
2 9 5
```

**Output:**

```
1
4 2 1
0 1 1 0 1 0 0 0 0 0
```

**Explanation:**

716 - 295 = 421. Digit frequencies: one 1, one 2, one 4.

![Example Visualization](../images/LNK-016/example-1.png)

## Notes

- Compare lengths and lexicographic order to choose the minuend
- Use stacks to subtract from least significant digit with borrow
- Remove leading zeros from the result; if empty, result is 0
- Time complexity: O(n + m)
- Space complexity: O(n + m)

## Related Topics

Linked Lists, Big Integer Arithmetic, Stacks

---

## Solution Template

### Java


### Python


### C++


### JavaScript

