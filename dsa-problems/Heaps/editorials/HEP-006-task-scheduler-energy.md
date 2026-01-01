---
problem_id: HEP_TASK_SCHEDULER_ENERGY__9471
display_id: HEP-006
slug: task-scheduler-energy
title: "Task Scheduler with Energy"
difficulty: Medium
difficulty_score: 56
topics:
  - Heaps
  - Greedy
  - Scheduling
tags:
  - heaps
  - greedy
  - energy
  - medium
premium: true
subscription_tier: basic
---

# HEP-006: Task Scheduler with Energy

## 📋 Problem Summary

You have `n` tasks, each with a `duration` (cost) and a `gain` (reward).
You start with energy `E`.
To start a task, you need `E >= duration`.
After finishing, `E = E - duration + gain`.
Find the maximum number of tasks you can complete.

## 🌍 Real-World Scenario

**Scenario Title:** RPG Quest Progression

In a Role-Playing Game, you have a Stamina bar.
- Quests require a minimum Stamina to start (e.g., "Climb the Mountain" needs 50 Stamina).
- Completing the quest consumes Stamina but also rewards you with a Stamina Potion or boost.
- Some quests are net positive (gain > cost), increasing your capacity for harder quests.
- Some are net negative (gain < cost), draining you.
- You want to complete as many quests as possible.

![Real-World Application](../images/HEP-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Energy Flow

Start E = 10.
Tasks:
A: Cost 5, Gain 10 (Net +5).
B: Cost 15, Gain 20 (Net +5).
C: Cost 8, Gain 2 (Net -6).

Strategy:
1. Do A first? Need 5. Have 10. OK.
   - E = 10 - 5 + 10 = 15.
2. Now have 15. Can do B (Need 15).
   - E = 15 - 15 + 20 = 20.
3. Now have 20. Can do C (Need 8).
   - E = 20 - 8 + 2 = 14.
Total: 3 tasks.

If we tried B first: Need 15. Have 10. Impossible.

### Key Concept: Positive vs Negative Net Gain

Split tasks into:
- **Positive tasks** (`gain >= duration`): executing them never decreases energy.
- **Negative tasks** (`gain < duration`): executing them decreases energy by
  `loss = duration - gain`.

#### Positive tasks
Sort by duration ascending and execute while possible. If the smallest-duration
positive task is not feasible, no other positive task is feasible and energy
cannot increase further from positives.

#### Negative tasks
Let `E_peak` be the energy after all feasible positive tasks.
For negative tasks, an optimal execution order is by **gain descending**.
In that order, before task `i` the energy is
`E_peak - sum_loss_prev`, so feasibility requires:
```
E_peak >= gain_i + sum_loss_prefix
```
where `sum_loss_prefix` includes the current task's loss.

To maximize the number of negative tasks, keep `sum_loss_prefix` as small as
possible:
- Iterate negative tasks by gain descending.
- Add each loss to a max-heap and to `sum_loss`.
- If `sum_loss + gain_i > E_peak`, remove the task with the **largest loss**.

The heap size after processing all negatives is the maximum number of negative
tasks that can be scheduled.

### Algorithm

1. Split tasks into positive and negative.
2. Sort positive by duration ascending and execute while feasible.
3. Let `E_peak` be the resulting energy.
4. Sort negative by gain descending.
5. Max-heap of losses and running `sum_loss`:
   - Add `loss`.
   - If `sum_loss + gain_i > E_peak`, remove the largest loss.
6. Answer = `positive_count + heap_size`.

### Time Complexity

- **O(N log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-006/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** E=3. Tasks: `(2,3)`, `(3,1)`.

1. **Positive:** `(2,3)`.
   - `3 >= 2`. Do it.
   - `E = 3 - 2 + 3 = 4`. Count = 1.
2. **Negative:** `(3,1)`. Loss = 2.
   - Sort by gain desc: `(3,1)` (gain 1).
   - Check: `4 >= 1 + 0 + 2 = 3`.
   - Yes. Do it.
   - Count = 2.

**Result:** 2.

**Input:** E=10. Negatives: `(10, 5)`, `(15, 10)`.
- Sorted by gain: `(15, 10)` (gain 10), `(10, 5)` (gain 5).
- T1 (15, 10): Loss 5.
  - Sum loss = 5. Check `5 + 10 > 10`. Remove loss 5.
- T2 (10, 5): Loss 5.
  - Sum loss = 5. Check `5 + 5 <= 10`. Keep.
- Result 1. (Correct: 10->5. Can't do 15).

## ✅ Proof of Correctness

### Invariant
- Positive tasks increase capacity, so doing them first (cheapest first) maximizes peak energy.
- Negative tasks decrease capacity. Sorting by gain descending ensures we satisfy the tightest "end constraints" first (in reverse logic).
- The heap ensures we pick the subset with minimal total loss that fits in the budget.

## 💡 Interview Extensions

- **Extension 1:** What if tasks have deadlines?
  - *Answer:* Combine with "Job Sequencing" (sort by deadline).
- **Extension 2:** Maximize total gain instead of count?
  - *Answer:* DP (Knapsack).

### Common Mistakes to Avoid

1. **Mixing Positive/Negative**
   - ❌ Wrong: Sorting all tasks together.
   - ✅ Correct: Positive tasks must be done first to build energy.
2. **Sorting Negative Tasks**
   - ❌ Wrong: Sorting by cost or loss.
   - ✅ Correct: Sort by `gain` descending.

## Related Concepts

- **Greedy:** Standard approach for scheduling.
- **Priority Queue:** For optimizing selections with constraints.
