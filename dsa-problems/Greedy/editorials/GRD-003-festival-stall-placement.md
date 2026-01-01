---
problem_id: GRD_FESTIVAL_STALL_PLACEMENT__7146
display_id: GRD-003
slug: festival-stall-placement
title: "Festival Stall Placement"
difficulty: Medium
difficulty_score: 45
topics:
  - Greedy Algorithms
  - Intervals
  - Activity Selection
tags:
  - greedy
  - intervals
  - scheduling
  - activity-selection
  - medium
premium: true
subscription_tier: basic
---

# GRD-003: Festival Stall Placement

## 📋 Problem Summary

You have `n` requests to place stalls at a festival. Each request specifies a desired interval `[start, end]`. Due to safety regulations, any two placed stalls must be separated by a minimum distance `d`. Your goal is to select the maximum number of requests that satisfy this safety constraint.

## 🌍 Real-World Scenario

**Scenario Title:** Social Distancing at Public Events

Organizers of a street market need to approve vendor applications. Each vendor wants a specific spot on the street (e.g., from meter 10 to meter 15). To comply with health regulations, there must be at least 2 meters of empty space between any two stalls to prevent overcrowding.

Approving the maximum number of vendors maximizes revenue for the organizers and variety for the attendees, but the physical constraints must be strictly followed.

**Why This Problem Matters:**

- **Resource Optimization:** Maximizing utilization of a limited resource (space, time) under constraints.
- **Scheduling:** Similar to scheduling meetings with mandatory setup/cleanup times between them.

![Real-World Application](../images/GRD-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Gap Constraint

```text
Distance d = 2

Request A: [0, 2]
Request B:    [3, 5]
Request C:       [5, 7]

Timeline:
0   1   2   3   4   5   6   7
|---|---|---|---|---|---|---|
[ A ]---|       [ B ]---|
        ^ Gap=1 (Invalid)

[ A ]---|---|---| [ C ]---|
        ^ Gap=3 (Valid, >= 2)

If we pick A, we cannot pick B (gap 3-2=1 < 2).
We can pick C (gap 5-2=3 >= 2).
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Distance Measurement:** The distance is between the *end* of the earlier stall and the *start* of the later stall. `later.start - earlier.end >= d`.
- **Coordinates:** Intervals are inclusive `[start, end]`.
- **Sorting:** The input is not guaranteed to be sorted.

## Naive Approach

### Intuition

Try every possible combination (subset) of stalls. For each subset, check if all pairs satisfy the distance constraint. Pick the largest valid subset.

### Algorithm

1. Generate all `2^n` subsets.
2. For each subset, sort it and check gaps.
3. Keep the size of the largest valid one.

### Time Complexity

- **O(2^n * n log n)**: Generating subsets and validating.

### Space Complexity

- **O(n)**: To store a subset.

### Limitations

- With `n=10^5`, this is impossible. We need a polynomial time solution.

## Optimal Approach

### Key Insight

This is a variation of the classic **Activity Selection Problem**. The standard problem asks for max non-overlapping intervals. Our problem adds a "buffer" requirement.

The greedy strategy for Activity Selection is: **Always pick the interval that finishes earliest.**
Why? By finishing as early as possible, you leave the maximum amount of "free resource" (time or space) for subsequent intervals. This logic holds true even with the buffer `d`.

### Algorithm

1. **Sort** all requests by their **end time** in ascending order.
2. Initialize `count = 0` and `last_end = -infinity`.
3. Iterate through the sorted requests:
   - Let current request be `[start, end]`.
   - Check if `start - last_end >= d`.
   - If yes:
     - Select this request.
     - `count++`
     - `last_end = end`
   - If no:
     - Skip this request (it conflicts with the last selected one).

### Time Complexity

- **O(N log N)**: Dominated by sorting. The iteration is O(N).

### Space Complexity

- **O(1)**: Or O(N) depending on sort implementation/input storage.

### Why This Is Optimal

Let the greedy solution be `G` and an optimal solution be `O`.
- `G` picks the first interval `g_1` that ends earliest. `O` picks some first interval `o_1`.
- Since `g_1` ends earliest, `g_1.end <= o_1.end`.
- This means `g_1` leaves *at least as much* room for the rest of the timeline as `o_1` does.
- We can replace `o_1` with `g_1` in the optimal solution without breaking validity for the rest.
- By induction, the greedy set is of the same size as the optimal set.

![Algorithm Visualization](../images/GRD-003/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 2
0 2
1 4
5 6
```

**Sorted by End Time:**
1. `[0, 2]` (Ends at 2)
2. `[1, 4]` (Ends at 4)
3. `[5, 6]` (Ends at 6)

**Execution:**
- `lastEnd` initialized to `-inf`.
- **Stall 1 `[0, 2]`**: `0 - (-inf) >= 2` is True.
  - Pick it. `count = 1`. `lastEnd = 2`.
- **Stall 2 `[1, 4]`**: `1 - 2 = -1`. `-1 >= 2` is False.
  - Skip it.
- **Stall 3 `[5, 6]`**: `5 - 2 = 3`. `3 >= 2` is True.
  - Pick it. `count = 2`. `lastEnd = 6`.

**Result:** `2`

![Example Visualization](../images/GRD-003/example-1.png)

## ✅ Proof of Correctness

### Invariant
The greedy strategy maintains the property that after selecting `k` stalls, the end time of the `k`-th stall is the minimum possible end time for any valid set of `k` stalls.

### Why the approach is correct
Suppose the greedy choice selects a stall ending at `e_1`. Suppose an optimal solution selects a different first stall ending at `e'_1`.
By our sorting, `e_1 <= e'_1`.
The remaining problem is to fit stalls after `e_1 + d` (for greedy) vs after `e'_1 + d` (for optimal).
Since `e_1 + d <= e'_1 + d`, the greedy choice leaves *more* (or equal) space for subsequent stalls. Thus, the greedy choice cannot prevent finding an optimal solution.

## 💡 Interview Extensions

- **Extension 1:** What if each stall has a "profit" value?
  - *Answer:* This becomes the **Weighted Interval Scheduling** problem. Greedy fails; you need Dynamic Programming (`O(N log N)`).
- **Extension 2:** What if the road is circular?
  - *Answer:* Pick an arbitrary starting point, unroll the circle (duplicate intervals), or try fixing the first interval and solving linearly.
- **Extension 3:** What if we need to place exactly `k` stalls and maximize the minimum distance?
  - *Answer:* This is the "Aggressive Cows" problem. Use Binary Search on the answer (distance).

### Common Mistakes to Avoid

1. **Sorting by Start Time**
   - ❌ Wrong: Picking the one that starts earliest doesn't account for how long it blocks the road. A stall `[0, 100]` would block everything else.
   - ✅ Correct: Sort by **End Time**.

2. **Incorrect Distance Check**
   - ❌ Wrong: `start > lastEnd + d`.
   - ✅ Correct: `start - lastEnd >= d` (or `start >= lastEnd + d`).

3. **Integer Overflow**
   - ❌ Wrong: `lastEnd + d` might overflow if both are near `INT_MAX`.
   - ✅ Correct: Use subtraction `start - lastEnd >= d` or cast to `long`.

## Related Concepts

- **Activity Selection Problem:** The base version of this problem.
- **Interval Scheduling:** General class of problems.
- **Greedy Choice Property:** Local optimal -> Global optimal.
