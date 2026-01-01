---
problem_id: HEP_MEETING_ROOMS_MIN_IDLE_SETUP__3108
display_id: HEP-005
slug: meeting-rooms-min-idle-setup
title: "Meeting Rooms Min Idle with Setup Time"
difficulty: Medium
difficulty_score: 54
topics:
  - Heaps
  - Scheduling
  - Intervals
tags:
  - heaps
  - scheduling
  - intervals
  - medium
premium: true
subscription_tier: basic
---

# HEP-005: Meeting Rooms Min Idle with Setup Time

## 📋 Problem Summary

You have `k` rooms and `n` meetings. Each meeting has a start and end time.
After a meeting ends, a room needs `s` setup time.
If a room finishes meeting `i` at `end_i`, it is ready at `end_i + s`.
If it takes meeting `j` starting at `start_j`, the **slack** is `start_j - (end_i + s)`.
Goal: Assign meetings to rooms to minimize total slack.
Input guarantees a valid schedule exists.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Center Optimization

You manage a conference center with `k` halls.
- Between events, cleaning crews need `s` minutes to prep the room.
- If a room sits empty after cleaning, that's wasted potential (slack).
- You want to schedule events such that rooms are "back-to-back" as much as possible to maximize efficiency (or minimize idle time).

![Real-World Application](../images/HEP-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Slack Calculation

Room 1 Timeline:
`[Meeting A: 0-10] --Setup(1)-- [Ready at 11] ....... [Meeting B: 15-20]`

Slack = Start(B) - Ready(A) = 15 - 11 = 4.

If we assigned Meeting C (12-14) instead:
`[Meeting A: 0-10] --Setup(1)-- [Ready at 11] . [Meeting C: 12-14]`
Slack = 12 - 11 = 1. Better!

### Key Concept: Best-Fit Strategy

We process meetings in order of their **start times**.
For the current meeting starting at `T_start`, we need a room that is free by `T_start`.
Among all rooms free `<= T_start`, which one should we pick?
- To minimize slack (`T_start - T_free`), we should pick the room with the **largest** `T_free` that is still `<= T_start`.
- This is a "Best Fit" strategy. We want the "tightest" fit.

Why largest `T_free`?
- Suppose rooms are free at 5, 8, 10. Meeting starts at 12.
- Slacks: `12-5=7`, `12-8=4`, `12-10=2`.
- Picking 10 gives min slack.
- Also, picking 10 leaves 5 and 8 available for potential earlier meetings (though we process by start time, so future meetings start `>= 12`).
- So, picking the latest possible valid room is locally and globally optimal.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Meetings list, `k`, `s`.
- **Output:** Total slack.
- **Constraints:** `N <= 10^5`, `K <= N`.
- **Guarantee:** A valid schedule exists (so we don't need to check if `K` is sufficient, just optimize assignment).

## Naive Approach

### Intuition

For each meeting, iterate all `K` rooms to find the best one.

### Time Complexity

- **O(N * K)**: Slow if `K` is large.

## Optimal Approach

### Key Insight

We need to efficiently query: "Find max `T_free <= T_start`" among rooms that have already hosted a meeting.
We track:
- **Used rooms**: a multiset of their next free times.
- **Unused rooms**: a counter. The first meeting in a room has **0 slack** by definition.

For each meeting in start-time order:
- If a used room is free by `start`, assign the meeting to the used room with the **latest** free time (minimizes this meeting's slack).
- Otherwise, open a new room (if any unused remain) and add **0 slack**.

Then update that room's next free time to `end + s`.

### Algorithm

1. Sort meetings by start time.
2. Initialize a Multiset for **used** rooms (empty) and `unused = k`.
3. `totalSlack = 0`.
4. For each meeting `[start, end]`:
   - Find `roomEnd` = largest value in Multiset `<= start`.
   - If found, `slack = start - roomEnd`, remove `roomEnd`.
   - If not found, use an unused room (`unused--`) and add `slack = 0`.
   - Insert `end + s` into Multiset (room is now used).
5. Return `totalSlack`.

### Time Complexity

- **O(N log K)**: Sorting + Multiset operations.

### Space Complexity

- **O(K)**: Multiset size.

![Algorithm Visualization](../images/HEP-005/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 2 1`. Meetings: `[0,10], [5,8], [13,20]`.
Sorted: `[0,10], [5,8], [13,20]`.

1. **Meeting [0,10]**:
   - Used rooms: empty, unused = 2.
   - No used room is free, so open a fresh room.
   - Slack: 0.
   - Add 10+1=11 to used rooms.

2. **Meeting [5,8]**:
   - Used rooms: `{11}` (not free by 5), unused = 1.
   - No used room is free, so open a fresh room.
   - Slack: 0.
   - Add 8+1=9 to used rooms.

3. **Meeting [13,20]**:
   - Used rooms: `{9, 11}`.
   - Floor(13) -> 11.
   - Slack: 13 - 11 = 2.
   - Replace 11 with 20+1=21.

Total Slack: 2.

This matches the example because slack is counted **only between consecutive meetings** in the same room.  
The first meeting assigned to a room contributes **0** slack.

## ✅ Proof of Correctness

### Invariant
- If a used room is available, choosing the latest available free time minimizes the current slack and keeps earlier free times available for future meetings.
- If no used room is available, the meeting must start a new room; by definition its slack is 0.
- Updating the chosen room’s next free time preserves feasibility for all later meetings (sorted by start).

## 💡 Interview Extensions

- **Extension 1:** Weighted Meetings?
  - *Answer:* DP or Max Flow.
- **Extension 2:** Maximize meetings instead of minimize slack?
  - *Answer:* Standard Activity Selection (sort by end time).

### Common Mistakes to Avoid

1. **Initial Slack**
   - ❌ Wrong: Counting `start - 0` as slack.
   - ✅ Correct: First meeting in a room has 0 slack.
2. **Set vs Multiset**
   - ❌ Wrong: Using a Set (ignoring duplicate free times).
   - ✅ Correct: Use Multiset/Map<Time, Count> because multiple rooms can be free at the same time.

## Related Concepts

- **Interval Partitioning:** Minimizing number of rooms.
- **Bin Packing:** Related but NP-hard (this is simpler).
