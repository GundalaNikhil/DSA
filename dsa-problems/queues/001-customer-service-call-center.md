# Customer Service Call Center

**Problem ID:** QUE-001
**Display ID:** 24
**Question Name:** Customer Service Call Center
**Slug:** customer-service-call-center
**Title:** Implement Queue using Stacks
**Difficulty:** Easy
**Premium:** No
**Tags:** Queue, Stack, Design

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

## A Simple Scenario (Daily Life Usage)

You're building a call center system. Customers call in and are put in a queue. The first customer who called should be the first one helped (FIFO). However, your system only has stack data structures available. You need to simulate a queue using two stacks so that customers are served in the order they called.

## Your Task

Implement the MyQueue class:

- `void push(int x)` - Pushes element x to the back of the queue
- `int pop()` - Removes the element from the front of the queue and returns it
- `int peek()` - Returns the element at the front of the queue
- `boolean empty()` - Returns true if the queue is empty, false otherwise

## Why is it Important?

This problem teaches you:

- Understanding of stack and queue data structures
- Converting between different data structure behaviors
- Amortized time complexity analysis
- Practical design patterns in system architecture

## Examples

### Example 1:

**Input:**
```
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
```

**Output:** `[null, null, null, 1, 1, false]`

**Explanation:**
```
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2]
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
```

### Example 2:

**Input:**
```
["MyQueue", "push", "push", "push", "pop", "pop", "pop", "empty"]
[[], [3], [4], [5], [], [], [], []]
```

**Output:** `[null, null, null, null, 3, 4, 5, true]`

**Explanation:** All three customers (3, 4, 5) are served in order and queue becomes empty.

## Constraints

- 1 ≤ x ≤ 9
- At most 100 calls will be made to push, pop, peek, and empty
- All calls to pop and peek are valid (queue is not empty)

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Zendesk
- Salesforce Service Cloud
- Freshdesk
- Genesys

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
