---
problem_id: HEP_PRIORITY_QUEUE_DECREASE_KEY__8091
display_id: HEP-016
slug: priority-queue-decrease-key
title: "Priority Queue with Decrease-Key"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Priority Queue
  - Data Structures
tags:
  - heaps
  - priority-queue
  - decrease-key
  - medium
premium: true
subscription_tier: basic
---

# HEP-016: Priority Queue with Decrease-Key

## 📋 Problem Summary

Implement a Min-Priority Queue supporting:
1. `INSERT id value`: Add element.
2. `DECREASE id delta`: Reduce value of existing element by `delta`.
3. `EXTRACT`: Remove and return element with minimum value.
   - Tie-breaker: Lexicographically smallest `id`.
   - If empty, return `EMPTY`.

## 🌍 Real-World Scenario

**Scenario Title:** Dijkstra's Algorithm Optimization

In network routing (OSPF) or map navigation (GPS), Dijkstra's algorithm finds the shortest path.
- It maintains a set of "tentative distances" to nodes.
- When a shorter path to a node is found, we must update its priority in the queue.
- This "Decrease Key" operation is critical for performance (`O(E log V)` vs `O(E log V)` with lazy deletion vs `O(E + V log V)` with Fibonacci Heap).
- You are implementing the core data structure that enables efficient pathfinding updates.

![Real-World Application](../images/HEP-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Decrease Key Operation

Heap (Min):
      (10, A)
     /       \
 (20, B)   (30, C)

Operation: `DECREASE C 25`.
New Value for C: `30 - 25 = 5`.

Step 1: Update value.
      (10, A)
     /       \
 (20, B)   (5, C)

Step 2: Bubble Up (Percolate Up).
5 < 10. Swap C and A.

      (5, C)
     /      \
 (20, B)  (10, A)

Result: Heap property restored.

### Key Concept: Index Map

Standard Binary Heaps support `push` and `pop` in `O(log N)`.
To support `decrease-key` in `O(log N)`, we need to find the element in the heap array instantly.
- **Solution:** Maintain a Hash Map `id -> index`.
- `map[id]` stores the current position of `id` in the heap array.
- When swapping elements during bubble-up/down, update the map.

### Lazy Deletion vs. Explicit Decrease Key

- **Lazy Deletion:** When updating, just push a new pair `(new_val, id)`. When popping, ignore stale entries.
  - Pros: Easy to implement with standard library PQ.
  - Cons: Heap size grows to `O(Operations)`. Space overhead.
- **Explicit Decrease Key:** Modify the element in place and re-heapify.
  - Pros: Heap size stays `O(N)`. Optimal space.
  - Cons: Requires custom Heap implementation with index tracking.
  - **This problem requires Explicit Decrease Key** (implied by "Implement a priority queue" and efficiency context, though lazy deletion can pass on looser constraints). Given "Medium" and specific operations, a custom heap is the intended educational goal.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `INSERT`, `DECREASE`, `EXTRACT`.
- **Output:** `value id` or `EMPTY`.
- **Tie-Breaking:** If values equal, smaller `id` string comes first.
- **Constraints:** IDs are alphanumeric. Values fit in integer.

## Naive Approach

### Intuition

Use a list. Scan for min (`O(N)`). Scan for ID to update (`O(N)`).

### Time Complexity

- **O(Q * N)**: Too slow.

## Optimal Approach

### Key Insight

Custom Binary Heap with a `Map<String, Integer>` to track indices.

### Algorithm

1. **Data Structures:**
   - `heap`: Array of `Node { id, value }`.
   - `pos`: Map `id -> index in heap`.
2. **INSERT(id, val):**
   - Add to end of `heap`.
   - Update `pos`.
   - `bubbleUp(size - 1)`.
3. **DECREASE(id, delta):**
   - Find index `i = pos[id]`.
   - `heap[i].value -= delta`.
   - `bubbleUp(i)`.
4. **EXTRACT:**
   - If empty, return `EMPTY`.
   - Result = `heap[0]`.
   - Remove `id` from `pos`.
   - Move last element to `heap[0]`. Update its `pos`.
   - `bubbleDown(0)`.
   - Return Result.
5. **Bubble Up/Down:**
   - Standard heap logic.
   - **Crucial:** When swapping `i` and `j`, update `pos[heap[i].id]` and `pos[heap[j].id]`.
   - **Comparator:** `val1 < val2` OR `val1 == val2 && id1 < id2`.

### Time Complexity

- **O(Q log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-016/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
INSERT id1 5
INSERT id2 3
DECREASE id1 4
EXTRACT
EXTRACT
```

1. `INSERT id1 5`: Heap `[(5, id1)]`. Map `{id1: 0}`.
2. `INSERT id2 3`: Heap `[(5, id1), (3, id2)]`. Bubble up `(3, id2)`.
   - Swap. Heap `[(3, id2), (5, id1)]`. Map `{id2: 0, id1: 1}`.
3. `DECREASE id1 4`:
   - `pos[id1] = 1`.
   - `heap[1].value = 5 - 4 = 1`.
   - Bubble up index 1.
   - `(1, id1)` vs `(3, id2)`. 1 < 3. Swap.
   - Heap `[(1, id1), (3, id2)]`. Map `{id1: 0, id2: 1}`.
4. `EXTRACT`:
   - Min `(1, id1)`. Output `1 id1`.
   - Move last `(3, id2)` to 0. Remove last.
   - Heap `[(3, id2)]`. Map `{id2: 0}`.
   - Bubble down 0. No children.
5. `EXTRACT`:
   - Min `(3, id2)`. Output `3 id2`.
   - Empty.

Output matches example.

## ✅ Proof of Correctness

### Invariant
- The binary heap property (parent <= child) is maintained after every operation.
- The `pos` map always correctly points to the index of each ID in the heap array, allowing `O(1)` access for updates.

## 💡 Interview Extensions

- **Extension 1:** Increase Key?
  - *Answer:* Similar, but bubble down.
- **Extension 2:** Delete arbitrary ID?
  - *Answer:* Decrease key to `-infinity`, then extract min.

### Common Mistakes to Avoid

1. **Map Sync**
   - ❌ Wrong: Forgetting to update map during swap.
   - ✅ Correct: Update map for BOTH swapped elements.
2. **Tie-Breaking**
   - ❌ Wrong: Ignoring IDs when values equal.
   - ✅ Correct: Use ID string comparison as secondary key.

## Related Concepts

- **Dijkstra/Prim:** Uses this exact structure.
- **Fibonacci Heap:** Theoretical optimization.
