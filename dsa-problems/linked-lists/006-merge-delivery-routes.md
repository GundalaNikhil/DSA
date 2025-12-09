# Merge Delivery Routes

**Problem ID:** LL-006
**Display ID:** 17
**Question Name:** Merge Delivery Routes
**Slug:** merge-delivery-routes
**Title:** Merge Two Sorted Linked Lists
**Difficulty:** Easy
**Premium:** No
**Tags:** Linked List, Recursion, Merge

## Problem Description

Given the heads of two sorted linked lists representing delivery routes, merge them into one sorted linked list. The merged list should be made by splicing together the nodes of the two input lists.

## A Simple Scenario (Daily Life Usage)

You're coordinating two delivery drivers. Driver A has packages to deliver at addresses: 1st Ave → 5th Ave → 9th Ave. Driver B has packages at: 2nd Ave → 4th Ave → 8th Ave. To optimize the route, you merge both lists into a single sorted route: 1st → 2nd → 4th → 5th → 8th → 9th Ave. This ensures the most efficient delivery path.

## Your Task

Write a function that takes two sorted linked lists and merges them into one sorted linked list. You can solve this iteratively or recursively.

## Why is it Important?

This problem teaches you:

- Merging sorted data structures efficiently
- Recursive vs iterative approaches
- Maintaining sorted order while combining lists
- Fundamental merge operation (used in merge sort)

## Examples

### Example 1:

**Input:** `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`
**Output:** `[1, 1, 2, 3, 4, 4]`
**Explanation:** Merge both lists maintaining sorted order.

### Example 2:

**Input:** `list1 = []`, `list2 = []`
**Output:** `[]`
**Explanation:** Both lists are empty.

### Example 3:

**Input:** `list1 = []`, `list2 = [0]`
**Output:** `[0]`
**Explanation:** One list is empty, return the other.

## Constraints

- The number of nodes in both lists is in the range [0, 50]
- -100 ≤ Node.val ≤ 100
- Both list1 and list2 are sorted in non-decreasing order

## Asked by Companies

- FedEx
- UPS
- DoorDash
- Postmates
