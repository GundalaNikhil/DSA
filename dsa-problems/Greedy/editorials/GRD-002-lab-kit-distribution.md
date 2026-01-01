---
problem_id: GRD_LAB_KIT_DISTRIBUTION__5291
display_id: GRD-002
slug: lab-kit-distribution
title: "Lab Kit Distribution"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - distribution
  - medium
premium: true
subscription_tier: basic
---

# GRD-002: Lab Kit Distribution

## 📋 Problem Summary

You have `k` types of lab kits with varying quantities. You need to distribute these kits to `m` students. Each student needs exactly one kit of any type. Your goals are, in order:
1. Maximize the number of students who receive a kit.
2. Minimize the number of kit types that run out completely (reach zero quantity).

## 🌍 Real-World Scenario

**Scenario Title:** Disaster Relief Supply Management

Imagine you are coordinating disaster relief. You have stockpiles of different food rations (Type A, Type B, Type C). You have a line of people needing food.
- **Goal 1:** Feed as many people as possible.
- **Goal 2:** Maintain variety in your stockpile for as long as possible. If you run out of Type A completely, you lose the ability to accommodate specific dietary restrictions or nutritional balance that Type A might offer later.

By always distributing from the largest stockpile, you keep your options open and delay the moment any single resource type is completely exhausted.

**Why This Problem Matters:**

- **Inventory Health:** Preventing stockouts of specific items is often critical in supply chain management.
- **Load Balancing:** In server clusters, you want to send requests to the server with the most capacity to prevent any single server from crashing (reaching 0 capacity).

![Real-World Application](../images/GRD-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Leveling the Piles

Imagine the quantities as stacks of blocks. We want to take blocks away such that we avoid hitting the ground (0) for any stack.

```text
Initial State:
   [ ]
   [ ]      [ ]
   [ ] [ ]  [ ]
    A   B    C
   (3) (1)  (2)

Student 1 takes from A (Largest):
            [ ]
   [ ] [ ]  [ ]
   [ ] [ ]  [ ]
    A   B    C
   (2) (1)  (2)

Student 2 takes from A or C (Largest is 2):
   Let's pick A.
       [ ]  [ ]
   [ ] [ ]  [ ]
    A   B    C
   (1) (1)  (2)

...and so on.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Fulfilled Count:** This is simply `min(m, sum(quantities))`. You can't give more than you have, and you can't give more than needed.
- **Zeroed Types:** A type counts as "zeroed" if its final quantity is exactly 0.
- **Tie-breaking:** If multiple types have the same maximum quantity, picking any of them is fine for the optimal solution.

## Naive Approach

### Intuition

For each student, scan the entire array of quantities to find the maximum. Decrement it. Repeat `m` times.

### Algorithm

1. Loop `m` times.
2. Inside, loop `k` times to find index of max value.
3. Decrement that value.
4. If all values are 0, stop.

### Time Complexity

- **O(m * k)**: For each student, we scan `k` elements. With `m, k` up to `10^5`, this is `10^10` operations, which will TLE.

### Space Complexity

- **O(1)**: No extra space beyond input.

### Limitations

- Too slow for large inputs.

## Optimal Approach

### Key Insight

We always want the current maximum. A **Max-Heap (Priority Queue)** is the perfect data structure for repeatedly accessing and updating the maximum element efficiently.

### Algorithm

1. Calculate total available kits. `fulfilled = min(m, total)`.
2. Insert all non-zero quantities into a Max-Heap.
3. Iterate `fulfilled` times:
   - Extract max `q` from heap.
   - Decrement `q`.
   - If `q > 0`, push it back into the heap.
   - If `q == 0`, we don't push it back (it's exhausted).
4. The number of zeroed types is `k - heap.size()` (assuming we started with `k` types; if some were initially 0, handle accordingly).
   - Better: Count how many types end up at 0. Or simply `initial_non_zero_types - final_heap_size + initial_zero_types`.
   - Simplest: Just simulate. If `q` becomes 0, it's effectively removed from consideration for future "max" picks, but we need to count it as zeroed at the end.

### Time Complexity

- **O(m log k)**: We perform `m` extractions and insertions. Each heap operation is `log k`.
- **O(k)**: To build the initial heap.
- Total: **O(m log k)**.

### Space Complexity

- **O(k)**: To store the heap.

### Why This Is Optimal

Greedily reducing the largest pile minimizes the variance between pile heights. By keeping piles as equal as possible, we minimize the chance that any single pile hits zero before necessary.

![Algorithm Visualization](../images/GRD-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 4
3 1 2
```

**Initialization:**
- Heap: `[3, 2, 1]` (Max-Heap)
- Total Kits: 6
- Fulfilled: `min(4, 6) = 4`

**Iteration:**

| Step | Heap State (Before) | Action | Heap State (After) | Remaining to Distribute |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `[3, 2, 1]` | Pop 3, push 2 | `[2, 2, 1]` | 3 |
| 2 | `[2, 2, 1]` | Pop 2, push 1 | `[2, 1, 1]` | 2 |
| 3 | `[2, 1, 1]` | Pop 2, push 1 | `[1, 1, 1]` | 1 |
| 4 | `[1, 1, 1]` | Pop 1, push 0 (discard) | `[1, 1]` | 0 |

**Result:**
- Fulfilled: 4
- Remaining types in heap: 2
- Original types: 3
- Zeroed types: `3 - 2 = 1`

**Output:** `4 1`

![Example Visualization](../images/GRD-002/example-1.png)

## ✅ Proof of Correctness

### Invariant
At any step, the heap contains the current quantities of all non-zero kit types.

### Why Greedy Works
Suppose we deviate from the greedy strategy and take from a smaller pile `S` instead of the largest pile `L` (`S < L`).
- The new state is `S-1, L`.
- The greedy state is `S, L-1`.
- Since `S < L`, `S-1` is closer to 0 than `L-1` is. In fact, `S-1` is the most dangerous state.
- By reducing `L`, we keep the minimum value in the set as high as possible (or at least don't lower it unnecessarily).
- This maximizes the time until any pile hits 0.

## 💡 Interview Extensions

- **Extension 1:** What if we want to minimize the variance of the remaining quantities?
  - *Answer:* The same greedy strategy works! It tends to equalize the values.
- **Extension 2:** What if `m` is extremely large (`10^18`)?
  - *Answer:* We can't simulate. We need binary search on the "water level" (the final height of the piles).
- **Extension 3:** What if taking a kit has a cost associated with the type?
  - *Answer:* Then it becomes a Min-Cost Flow problem or a different greedy strategy based on cost.

### Common Mistakes to Avoid

1. **Sorting Only Once**
   - ❌ Wrong: Sort array, take from largest, decrement.
   - ⚠️ Issue: After decrementing, the order might change. You need to re-sort or use a Heap.
   - ✅ Correct: Use a Max-Heap.

2. **Ignoring Initial Zeros**
   - ❌ Wrong: `zeroed = heap.size()`.
   - ✅ Correct: `zeroed = k - heap.size()`. Some types might have been 0 to start with and never entered the heap.

3. **Integer Overflow**
   - ❌ Wrong: Using `int` for total sum if quantities are large.
   - ✅ Correct: Use `long` (Java/C++) for summing quantities, though `m` fits in int here.

## Related Concepts

- **Heap / Priority Queue:** Efficient max extraction.
- **Load Balancing:** Distributing tasks to resources.
- **Water Filling Algorithm:** Related concept for equalizing levels.
