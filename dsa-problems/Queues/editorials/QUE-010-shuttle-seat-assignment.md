---
problem_id: QUE_SHUTTLE_SEAT_ASSIGNMENT__4407
display_id: QUE-010
slug: shuttle-seat-assignment
title: "Shuttle Seat Assignment"
difficulty: Medium
difficulty_score: 46
topics:
  - Scheduling
  - Priority Queue
  - Queue
tags:
  - scheduling
  - min-heap
  - queue
  - medium
premium: true
subscription_tier: basic
---

# QUE-010: Shuttle Seat Assignment

## 📋 Problem Summary

We are given `N` intervals `[arrival, departure)`. Each interval represents a passenger needing a seat. We need to find the minimum number of seats required to accommodate all passengers simultaneously.
- A seat is occupied from `arrival` to `departure`.
- At `departure` time, the seat becomes free.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Room Booking

Imagine a co-working space with multiple meeting rooms.
- You have a list of meeting requests: `[9:00-10:00]`, `[9:30-10:30]`, `[10:00-11:00]`.
- You want to know the **minimum number of physical rooms** needed to host all meetings.
- If Meeting A ends at 10:00 and Meeting C starts at 10:00, they can share the same room.
- If Meeting A and B overlap, they need separate rooms.
- This is identical to the "Shuttle Seat" problem.

**Why This Problem Matters:**

- **Resource Allocation:** Determining hardware requirements (servers, ports, threads).
- **Logistics:** Fleet sizing for delivery trucks.

![Real-World Application](../images/QUE-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Interval Overlap

Intervals:
1. `[0, 5)`
2. `[4, 5)`
3. `[4, 9)`

Timeline:
```
Time: 0   1   2   3   4   5   6   7   8   9
P1:   [===================)
P2:                   [===)
P3:                   [===================)
```

- At time 0: P1 arrives. Seats: 1 (P1).
- At time 4: P2 arrives. P1 is still there. Seats: 2 (P1, P2).
- At time 4: P3 arrives. P1, P2 are there. Seats: 3?
  - P1 occupies `[0, 5)`.
  - P2 occupies `[4, 5)`.
  - P3 occupies `[4, 9)`.
  - At `t=4`, P1 is active. P2 starts. P3 starts.
  - Input: `0 4 4` arrivals and `5 5 9` departures.
  - P1: `0-5`. P2: `4-5`. P3: `4-9`.
  - Standard "Meeting Rooms II" logic applies:
  - Events:
    - `(0, +1)`
    - `(4, +1)`
    - `(4, +1)`
    - `(5, -1)`
    - `(5, -1)`
    - `(9, -1)`
  - Sort events:
    - `0: +1` (cnt=1)
    - `4: +1` (cnt=2)
    - `4: +1` (cnt=3)
    - `5: -1` (cnt=2)
    - `5: -1` (cnt=1)
    - `9: -1` (cnt=0)
  - Max overlap is 3.
  - The standard "Meeting Rooms II" solution (Min Heap or Line Sweep) is the canonical approach for this problem type.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Two arrays, `arrivals` and `departures`.
- **Output:** Integer (max concurrent intervals).
- **Intervals:** `[start, end)`. Start is inclusive, End is exclusive.
- **Tie-breaking:** If one arrives at X and another departs at X, process departure first (seat frees up before new one takes it).

## Naive Approach

### Intuition

For each time point where someone arrives, count how many people are currently active.

### Algorithm

1. Collect all time points.
2. For each point, check all intervals.
3. Max count is answer.

### Limitations

- **Time Complexity:** `O(N^2)`.
- With `N=100,000`, too slow.

## Optimal Approach

### Key Insight

We can process events in chronological order.
- **Arrival:** +1 seat needed.
- **Departure:** -1 seat needed.
- Sort all events. Iterate and track max `count`.

Alternatively, use a **Min-Heap** to track end times of currently occupied seats.
1. Sort intervals by start time.
2. Min-Heap stores end times of active meetings.
3. For each new meeting `[start, end)`:
   - Free up seats: Remove all elements from heap where `heap.min() <= start`.
   - Occupy seat: Add `end` to heap.
   - `max_seats = max(max_seats, heap.size())`.

### Algorithm (Min-Heap)

1. Pair `(arrival[i], departure[i])` and sort by arrival.
2. Initialize `PriorityQueue` (Min-Heap).
3. Loop through sorted intervals:
   - While `!pq.isEmpty() && pq.peek() <= current.start`: `pq.poll()`.
   - `pq.offer(current.end)`.
   - `max = Math.max(max, pq.size())`.

### Time Complexity

- **O(N log N)** due to sorting. Heap operations are also bounded by `N log N`.

### Space Complexity

- **O(N)** for heap and storage.

![Algorithm Visualization](../images/QUE-010/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-010/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `0 4 4` (Arr), `5 5 9` (Dep).
Intervals: `(0,5), (4,5), (4,9)`. Sorted.

1. `(0,5)`:
   - PQ empty.
   - Push 5. PQ `[5]`. Max=1.
2. `(4,5)`:
   - Peek 5. `5 <= 4`? No.
   - Push 5. PQ `[5, 5]`. Max=2.
3. `(4,9)`:
   - Peek 5. `5 <= 4`? No.
   - Push 9. PQ `[5, 5, 9]`. Max=3.

Result: 3.

Using the "Line Sweep" method (sort start/end independently):
Starts: `0, 4, 4`. Ends: `5, 5, 9`.
- `0`: +1 (1)
- `4`: +1 (2)
- `4`: +1 (3)
- `5`: -1 (2)
- ...
Result: 3.

## ✅ Proof of Correctness

### Invariant
The Min-Heap contains the departure times of all currently active passengers. The size of the heap represents the number of seats currently occupied.

### Why the approach is correct
By processing intervals in order of arrival and removing those that have finished, we accurately simulate the timeline and track peak occupancy.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Weighted Intervals?
  - *Hint:* If each passenger needs `W` seats? Just add `W` to current load.
- **Extension 2:** Max `K` seats available?
  - *Hint:* Check if `heap.size() < K`. If not, can we delay? (Different problem: Scheduling).

### Common Mistakes to Avoid

1. **Sorting only by Start**
   - ❌ Wrong: Sorting intervals but not using a heap/sweep line to track ends.
   - ✅ Correct: Must track when intervals *end* to free resources.
2. **Edge Cases**
   - ❌ Wrong: `start == end` (0 duration).
   - ✅ Correct: Logic should handle it (push then pop immediately or never push).

