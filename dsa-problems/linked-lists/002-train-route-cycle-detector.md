# Train Route Cycle Detector

**Problem ID:** LL-002
**Display ID:** 13
**Question Name:** Train Route Cycle Detector
**Slug:** train-route-cycle-detector
**Title:** Detect Cycle in Linked List
**Difficulty:** Easy
**Premium:** No
**Tags:** Linked List, Two Pointers, Floyd's Algorithm

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given the head of a linked list representing a train route, determine if the route has a cycle in it. A cycle occurs when a station's next connection points back to a previous station in the route, creating an infinite loop.

## A Simple Scenario (Daily Life Usage)

You're managing a train route system where Station A → Station B → Station C → Station D. However, due to a configuration error, Station D points back to Station B, creating an infinite loop: A → B → C → D → B → C → D... Passengers would never reach their final destination! You need to detect such cycles before deploying the route.

## Your Task

Write a function that takes the head of a linked list and returns true if there is a cycle, false otherwise. Use Floyd's Tortoise and Hare algorithm (fast and slow pointers) for optimal O(1) space complexity.

## Why is it Important?

This problem teaches you:

- Floyd's Cycle Detection Algorithm (Tortoise and Hare)
- Two-pointer technique
- Detecting infinite loops in data structures
- Space-efficient algorithm design

## Examples

### Example 1:

**Input:** `head = [3, 2, 0, -4]`, pos = 1 (tail connects to node at index 1)
**Output:** `true`
**Explanation:** There is a cycle where the tail connects back to the second node.

### Example 2:

**Input:** `head = [1, 2]`, pos = 0 (tail connects to node at index 0)
**Output:** `true`
**Explanation:** There is a cycle where the tail connects back to the first node.

### Example 3:

**Input:** `head = [1]`, pos = -1 (no cycle)
**Output:** `false`
**Explanation:** There is no cycle in the linked list.

## Constraints

- The number of nodes in the list is in the range [0, 10000]
- -100000 ≤ Node.val ≤ 100000
- pos is -1 or a valid index in the linked list

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google Maps
- Uber
- Lyft
- Tesla

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
