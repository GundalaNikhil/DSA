# Browser History Manager

**Problem ID:** LL-003
**Display ID:** 14
**Question Name:** Browser History Manager
**Slug:** browser-history-manager
**Title:** Find Middle Node of Linked List
**Difficulty:** Easy
**Premium:** No
**Tags:** Linked List, Two Pointers, Fast and Slow Pointer

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given the head of a singly linked list representing browser history, return the middle node of the list. If there are two middle nodes (even number of pages), return the second middle node.

## A Simple Scenario (Daily Life Usage)

You're implementing a "Jump to Middle" feature in a browser's history navigation. A user has visited 9 pages: Home → Search → Profile → Settings → Cart → Checkout → Confirmation → Receipt → Exit. Instead of clicking "Back" multiple times, they can jump directly to the middle page (Checkout) to review their purchase flow. This makes navigation more efficient.

## Your Task

Write a function that takes the head of a singly linked list and returns the middle node. Use the fast and slow pointer technique to solve this in one pass with O(1) space.

## Why is it Important?

This problem teaches you:

- Fast and slow pointer technique (two-pointer approach)
- Finding middle element without knowing list length
- Single-pass algorithm optimization
- Efficient traversal strategies

## Examples

### Example 1:

**Input:** `head = [1, 2, 3, 4, 5]`
**Output:** `[3, 4, 5]`
**Explanation:** The middle node is 3, and we return from that node onwards.

### Example 2:

**Input:** `head = [1, 2, 3, 4, 5, 6]`
**Output:** `[4, 5, 6]`
**Explanation:** Two middle nodes (3 and 4), we return the second one.

### Example 3:

**Input:** `head = [1]`
**Output:** `[1]`
**Explanation:** Single node is itself the middle.

## Constraints

- The number of nodes in the list is in the range [1, 100]
- 1 ≤ Node.val ≤ 100

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Chrome (Google)
- Firefox (Mozilla)
- Safari (Apple)
- Edge (Microsoft)

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
