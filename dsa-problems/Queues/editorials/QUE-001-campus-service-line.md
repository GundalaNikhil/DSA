---
problem_id: QUE_CAMPUS_SERVICE_LINE__4821
display_id: QUE-001
slug: campus-service-line
title: "Campus Service Line"
difficulty: Easy
difficulty_score: 18
topics:
  - Queue
  - Simulation
  - Data Streams
tags:
  - queue
  - simulation
  - easy
  - data-structures
premium: true
subscription_tier: basic
---

# QUE-001: Campus Service Line

## 📋 Problem Summary

We need to simulate a service line (queue) that processes students in a First-In-First-Out (FIFO) order.
- **ENQUEUE x:** A student with ID `x` joins the back of the line.
- **DEQUEUE:** The student at the front leaves the line. We must report their ID.
- **FRONT:** We report the ID of the student at the front without removing them.
- If the line is empty during a `DEQUEUE` or `FRONT` operation, we output `EMPTY`.

## 🌍 Real-World Scenario

**Scenario Title:** Printer Job Spooler

Imagine a shared printer in a university library.
- Students send documents to be printed from various computers.
- The printer cannot print everything at once; it processes jobs one by one.
- The **Spooler** maintains a queue of print jobs.
- When you click "Print" (`ENQUEUE`), your job goes to the end of the list.
- The printer takes the next job from the front (`DEQUEUE`) to print it.
- You might check the status screen to see which job is currently printing (`FRONT`).
- This ensures fairness: the first person to send a job gets their paper first.

**Why This Problem Matters:**

- **Operating Systems:** Process scheduling, I/O buffering.
- **Web Servers:** Handling incoming HTTP requests.
- **Breadth-First Search (BFS):** The fundamental data structure for graph traversal.

![Real-World Application](../images/QUE-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Queue Operations

Initial State: `[]` (Empty)

1. `ENQUEUE 12`:
   Queue: `[12]`
   Front: 12, Back: 12

2. `ENQUEUE -5`:
   Queue: `[12, -5]`
   Front: 12, Back: -5

3. `FRONT`:
   Output: `12`
   Queue remains: `[12, -5]`

4. `DEQUEUE`:
   Output: `12`
   Queue becomes: `[-5]`
   Front: -5, Back: -5

5. `DEQUEUE`:
   Output: `-5`
   Queue becomes: `[]` (Empty)

6. `DEQUEUE`:
   Output: `EMPTY`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** A list of commands.
- **Output:** A list of strings (results of `DEQUEUE` and `FRONT`).
- **Edge Case:** Calling `DEQUEUE` or `FRONT` on an empty queue.
- **Data Types:** IDs are integers (can be negative).

## Naive Approach

### Intuition

Use a dynamic array (like `ArrayList` in Java or `list` in Python).
- `ENQUEUE`: Add to the end.
- `DEQUEUE`: Remove from index 0.

### Algorithm

1. Maintain a list `L`.
2. `ENQUEUE x`: `L.append(x)`.
3. `DEQUEUE`: If empty return "EMPTY", else return `L.remove(0)`.
4. `FRONT`: If empty return "EMPTY", else return `L[0]`.

### Limitations

- **Time Complexity:** `DEQUEUE` takes `O(N)` because removing from the start of an array requires shifting all other elements.
- With `M` operations, total time could be `O(M^2)`, which is too slow for `M=100,000`.

## Optimal Approach

### Key Insight

Use a data structure designed for FIFO operations.
- **Linked List:** Adding to tail and removing from head are both `O(1)`.
- **Deque (Double-Ended Queue):** Optimized dynamic array (circular buffer) supporting `O(1)` add/remove at both ends.

### Algorithm

1. Use a standard Queue library (e.g., `LinkedList` in Java, `collections.deque` in Python, `std::queue` in C++).
2. `ENQUEUE`: Call `push` / `add`.
3. `DEQUEUE`: Check empty. If not, call `pop` / `poll` and record value.
4. `FRONT`: Check empty. If not, call `peek` / `front` and record value.

### Time Complexity

- **O(1)** per operation.
- Total: **O(M)**.

### Space Complexity

- **O(M)** to store elements.

![Algorithm Visualization](../images/QUE-001/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-001/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input:
```
6
ENQUEUE 12
ENQUEUE -5
FRONT
DEQUEUE
FRONT
DEQUEUE
```

1. `ENQUEUE 12`: Queue `[12]`.
2. `ENQUEUE -5`: Queue `[12, -5]`.
3. `FRONT`: Head is `12`. Output `12`.
4. `DEQUEUE`: Remove `12`. Queue `[-5]`. Output `12`.
5. `FRONT`: Head is `-5`. Output `-5`.
6. `DEQUEUE`: Remove `-5`. Queue `[]`. Output `-5`.

Output matches example.

![Example Visualization](../images/QUE-001/example-1.png)

## ✅ Proof of Correctness

### Invariant
The queue maintains the order of insertion. The element removed is always the one that has been in the collection the longest.

### Why the approach is correct
By definition, a Queue data structure satisfies the FIFO property required by the problem.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Implement Queue using Stacks?
  - *Hint:* Use two stacks (`input` and `output`). Push to `input`. Pop from `output`. If `output` is empty, move all from `input` to `output`. Amortized `O(1)`.
- **Extension 2:** Circular Queue?
  - *Hint:* Use a fixed-size array with `head` and `tail` pointers wrapping around modulo `N`. Efficient for fixed capacity.

### Common Mistakes to Avoid

1. **Using List as Queue**
   - ❌ Wrong: Using Python `list.pop(0)` or JS `array.shift()` inside a loop.
   - ✅ Correct: These are `O(N)` operations. Use `collections.deque` or a pointer-based approach.
2. **Empty Check**
   - ❌ Wrong: Forgetting to check if queue is empty before accessing front.
   - ✅ Correct: Always handle the empty case to avoid exceptions.

## Related Concepts

- **Stack:** LIFO (Last-In-First-Out).
- **Priority Queue:** Elements ordered by priority, not arrival time.
