# Print Job Scheduler

**Problem ID:** QUE-002
**Display ID:** 25
**Question Name:** Print Job Scheduler
**Slug:** print-job-scheduler
**Title:** Design Circular Queue
**Difficulty:** Medium
**Premium:** No
**Tags:** Queue, Array, Design

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design your implementation of the circular queue. A circular queue is a linear data structure in which operations are performed based on FIFO principle and the last position is connected back to the first position to make a circle. It is also called a "Ring Buffer".

## A Simple Scenario (Daily Life Usage)

You're managing an office printer queue. The printer has a fixed buffer that can hold 5 print jobs. When employees send documents to print, they go into this circular buffer. Once the buffer is full, no more jobs can be accepted until current jobs are printed. The circular design allows efficient memory reuse as old jobs are cleared.

## Your Task

Implement the MyCircularQueue class:

- `MyCircularQueue(k)` - Initializes the object with the size of the queue to be k
- `boolean enQueue(int value)` - Inserts an element into the circular queue. Return true if the operation is successful
- `boolean deQueue()` - Deletes an element from the circular queue. Return true if the operation is successful
- `int Front()` - Gets the front item from the queue. Return -1 if the queue is empty
- `int Rear()` - Gets the last item from the queue. Return -1 if the queue is empty
- `boolean isEmpty()` - Checks whether the circular queue is empty
- `boolean isFull()` - Checks whether the circular queue is full

## Why is it Important?

This problem teaches you:

- Circular buffer implementation
- Efficient memory management
- Fixed-size queue handling
- Modular arithmetic applications

## Examples

### Example 1:

**Input:**
```
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
```

**Output:** `[null, true, true, true, false, 3, true, true, true, 4]`

**Explanation:**
```
MyCircularQueue queue = new MyCircularQueue(3);
queue.enQueue(1); // return true (queue: [1])
queue.enQueue(2); // return true (queue: [1, 2])
queue.enQueue(3); // return true (queue: [1, 2, 3])
queue.enQueue(4); // return false (queue is full)
queue.Rear();     // return 3
queue.isFull();   // return true
queue.deQueue();  // return true (queue: [2, 3])
queue.enQueue(4); // return true (queue: [2, 3, 4])
queue.Rear();     // return 4
```

### Example 2:

**Input:**
```
["MyCircularQueue", "enQueue", "deQueue", "enQueue", "Front"]
[[2], [5], [], [10], []]
```

**Output:** `[null, true, true, true, 10]`

**Explanation:** Single job printed, new job added, check front job.

## Constraints

- 1 ≤ k ≤ 1000
- 0 ≤ value ≤ 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- HP
- Canon
- Xerox
- Brother

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
