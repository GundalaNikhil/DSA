# Undo Redo System

**Problem ID:** LL-004
**Display ID:** 15
**Question Name:** Undo Redo System
**Slug:** undo-redo-system
**Title:** Remove Nth Node From End of List
**Difficulty:** Medium
**Premium:** No
**Tags:** Linked List, Two Pointers, One Pass

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given the head of a linked list representing an undo/redo stack, remove the nth node from the end of the list and return its head. You must do this in one pass.

## A Simple Scenario (Daily Life Usage)

You're building a document editor's undo system. Each action is stored in a stack: Type "Hello" → Bold text → Add image → Change font → Save. The user wants to undo the 2nd most recent action (Change font), but keep the most recent one (Save). Your system needs to efficiently remove that specific action from the history without traversing the entire stack multiple times.

## Your Task

Write a function that takes the head of a linked list and an integer n, then removes the nth node from the end of the list. The solution must work in a single pass using the two-pointer technique.

## Why is it Important?

This problem teaches you:

- Two-pointer technique with offset
- Single-pass algorithm for efficiency
- Handling edge cases (removing head node)
- Maintaining proper node connections

## Examples

### Example 1:

**Input:** `head = [1, 2, 3, 4, 5]`, n = 2
**Output:** `[1, 2, 3, 5]`
**Explanation:** Remove the 2nd node from the end (node with value 4).

### Example 2:

**Input:** `head = [1]`, n = 1
**Output:** `[]`
**Explanation:** Removing the only node results in an empty list.

### Example 3:

**Input:** `head = [1, 2]`, n = 1
**Output:** `[1]`
**Explanation:** Remove the last node.

## Constraints

- The number of nodes in the list is sz
- 1 ≤ sz ≤ 30
- 0 ≤ Node.val ≤ 100
- 1 ≤ n ≤ sz

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Microsoft Word
- Google Docs
- Notion
- Figma

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
