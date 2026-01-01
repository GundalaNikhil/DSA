---
problem_id: HEP_DYNAMIC_MEDIAN_OF_MEDIANS__7312
display_id: HEP-009
slug: dynamic-median-of-medians
title: "Dynamic Median of Medians"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Medians
  - Union-Find
tags:
  - heaps
  - median
  - union-find
  - medium
premium: true
subscription_tier: basic
---

# HEP-009: Dynamic Median of Medians

## 📋 Problem Summary

You need to manage multiple groups of numbers and support:
1. `NEW id m ...`: Create a group `id` with initial numbers.
2. `ADD id x`: Add `x` to group `id`.
3. `MERGE id1 id2`: Merge group `id2` into `id1`.
4. `QUERY`: Find the median of the medians of all non-empty groups.

The "median" of a group is the lower median if size is even.
The "median of medians" is the median of the set of group medians.

## 🌍 Real-World Scenario

**Scenario Title:** Consolidated Census Data

Imagine a country with many districts.
- Each district maintains a median income statistic.
- Districts can be merged (administrative redistricting).
- New census data comes in (ADD).
- The central government wants to know the "Median of District Medians" to gauge the typical district's economic health.
- This requires a system that efficiently handles local updates, merges, and global queries.

![Real-World Application](../images/HEP-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Hierarchical Structure

**Level 1: Groups**
Group A: `[1, 5, 10]`. Median = 5.
Group B: `[2, 8]`. Median = 2.
Group C: `[20]`. Median = 20.

**Level 2: Global Medians**
Set of Medians: `{5, 2, 20}`.
Sorted: `[2, 5, 20]`.
Global Median: 5.

**Operation: MERGE A B**
- Group A absorbs B: `[1, 5, 10, 2, 8]`. Sorted: `[1, 2, 5, 8, 10]`.
- New Median of A: 5.
- Group B is gone.
- Global Set: `{5, 20}`.
- Global Median: 5 (lower of 5, 20).

### Key Concept: Two-Layer Heap System

1. **Local Layer (Per Group):**
   - Each group maintains two heaps (`LeftMax`, `RightMin`) to track its own median efficiently.
   - `LeftMax` stores smaller half. `RightMin` stores larger half.
   - Median is `LeftMax.top()`.

2. **Global Layer:**
   - We need the median of the *current medians*.
   - We can maintain a global structure of medians.
   - Since medians change upon ADD/MERGE, we need to update this global structure.
   - A `Multiset` or another pair of Heaps (`GlobalLeft`, `GlobalRight`) works.
   - **Lazy Deletion** is crucial because we can't efficiently find and remove old medians from standard heaps.

### Merging Strategy

When merging `id2` into `id1`:
- We must combine the elements of `id2` into `id1`.
- **Small-to-Large Heuristic:** Always merge the smaller group into the larger one to keep complexity low (`O(N log^2 N)` or `O(N log N)`).
- However, the problem says `MERGE id1 id2` means `id2` into `id1`. We can swap internals (rename) if `id2` is larger, but we must ensure `id1` remains the identifier.
- After merging, the median of `id1` changes.
- Update Global structure: Remove old `median(id1)` and `median(id2)`, insert new `median(id1)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Operations. `id` are strings or ints? Example uses `1`, `2`. Assume strings or convert to int.
- **Output:** Median or `EMPTY`.
- **Constraints:** Total elements `10^5`. `Q <= 10^5`.
- **Median Definition:** Lower median for even size.

## Naive Approach

### Intuition

Store full lists for each group. Sort on every query.

### Time Complexity

- **O(Q * N log N)**: Too slow.

## Optimal Approach

### Key Insight

Use **Two Heaps** for each group. Use **Two Heaps with Lazy Deletion** for the global medians.
Use **Union-Find** (or just a map) to track active groups if IDs are dynamic.
We can just move elements.

**Data Structures:**
- `Map<ID, Group>`: Stores heaps for each group.
- `GlobalHeaps`: Two heaps (`GL`, `GR`) storing medians of all groups.
- `LazyMap`: Tracks invalid entries in `GlobalHeaps`.

**Operations:**
1. **NEW:** Create group. Calculate median. Add to Global.
2. **ADD:** Insert to group heaps. Rebalance. Old median `M_old -> M_new`.
   - Global: Remove `M_old` (lazy), Add `M_new`.
3. **MERGE:**
   - Merge heaps of `id2` into `id1`.
   - Heuristic: If `id2` is larger, swap the underlying data structures of `id1` and `id2` (move `id1` elements to `id2`, then update map so `id1` points to `id2`'s data).
   - Recalculate median.
   - Global: Remove old medians of `id1`, `id2`. Add new median.
4. **QUERY:**
   - Clean Global heaps.
   - Return `GL.top()`.

### Time Complexity

- **O(N log^2 N)** or **O(N log N)** depending on merge strategy.
- With small-to-large merging, amortized cost is good.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-009/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
NEW 1 2 1 3
NEW 2 1 2
MERGE 1 2
QUERY
```

1. `NEW 1`: `[1, 3]`. Median 1. Global: `{1}`.
2. `NEW 2`: `[2]`. Median 2. Global: `{1, 2}`. Median 1.
3. `MERGE 1 2`:
   - Remove 1, 2 from Global.
   - Merge `[2]` into `[1, 3]`. Group 1: `[1, 2, 3]`. Median 2.
   - Add 2 to Global. Global: `{2}`.
4. `QUERY`: Output 2.

## ✅ Proof of Correctness

### Invariant
- Each group maintains its median correctly using two heaps.
- The global heaps maintain the median of group medians correctly.
- Lazy deletion ensures we don't process stale data.
- Small-to-large merging ensures efficiency.

## 💡 Interview Extensions

- **Extension 1:** Delete group?
  - *Answer:* Just remove its median from global.
- **Extension 2:** Median of all elements (not median of medians)?
  - *Answer:* Much harder with merges. Requires Segment Tree or Fenwick Tree if values are bounded.

### Common Mistakes to Avoid

1. **Lazy Deletion Logic**
   - ❌ Wrong: Decrementing size without checking if element was in Left or Right.
   - ✅ Correct: Infer location based on value vs top, but handle stale tops carefully.
2. **Merge Direction**
   - ❌ Wrong: Always merging 2 into 1 without checking size.
   - ✅ Correct: Merge smaller into larger to avoid `O(N^2)`.

## Related Concepts

- **Median of Medians:** Selection algorithm.
- **Union-Find:** Managing sets.
