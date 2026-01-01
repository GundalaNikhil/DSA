---
problem_id: HEP_SCHEDULER_COOLING_PRIORITY__5382
display_id: HEP-014
slug: scheduler-cooling-priority
title: "Scheduler With Cooling and Priority"
difficulty: Medium
difficulty_score: 57
topics:
  - Heaps
  - Scheduling
  - Greedy
tags:
  - heaps
  - cooldown
  - scheduling
  - medium
premium: true
subscription_tier: basic
---

# HEP-014: Scheduler With Cooling and Priority

## 📋 Problem Summary

You have `m` task types. Each has a `count` (available units) and a `priority` (score per unit).
You have `T` time slots.
In each slot, you can run one task or idle.
Constraint: If you run task type `X` at time `t`, you cannot run `X` again until `t + k + 1`.
Goal: Maximize total priority score within `T` slots.

## 🌍 Real-World Scenario

**Scenario Title:** High-Performance Computing Job Dispatch

A supercomputer scheduler receives jobs of different types (e.g., Physics Sim, AI Training).
- Each job type has a value (priority) and a limited number of pending requests (count).
- Running a job of type `X` heats up a specific hardware component.
- The component needs `k` cycles to cool down before it can run type `X` again.
- You have a fixed time window `T` to maximize the value of completed jobs.

![Real-World Application](../images/HEP-014/real-world-scenario.png)

## Detailed Explanation

### Feasibility of counts

Let `x_i` be how many times task type `i` is executed, with `0 <= x_i <= count_i`.
A schedule exists in `T` slots with cooldown `k` iff:
```
L = max(sum_x, (max_x - 1) * (k + 1) + n_max) <= T
```
where `sum_x = sum x_i`, `max_x = max x_i`, and `n_max` is the number of task
types that achieve `max_x`. This is the standard Task Scheduler bound and is
always tight.

So the problem reduces to choosing `x_i` to maximize:
```
score = sum(x_i * priority_i)
```
subject to the feasibility constraint above.

### Greedy reduction to maximize score

1. **Per-task cap:** A single task type cannot exceed
   `limit = floor((T + k) / (k + 1))`, so clamp
   `x_i = min(count_i, limit)`.
2. **Schedule constraint:** While
   `(max_x - 1) * (k + 1) + n_max > T`, only tasks at `max_x` can reduce the
   bound. Keep the `Y = T - (max_x - 1) * (k + 1)` highest-priority tasks at
   `max_x` and decrement the rest by 1.
3. **Sum constraint:** If `sum_x > T`, remove units from the lowest-priority
   tasks until `sum_x = T`. This never violates the schedule bound because
   decreasing counts only makes it easier to schedule.

### Algorithm

1. Initialize `x_i = min(count_i, limit)` for all tasks.
2. Fix the schedule bound by repeatedly demoting the lowest-priority tasks among
   those at `max_x`.
3. Fix the sum bound by removing units from lowest-priority tasks until
   `sum_x <= T`.
4. Return `sum(x_i * priority_i)`.

### Time Complexity

- **O(m^2 log m)** (with `m <= 26`, this is tiny).

### Space Complexity

- **O(m)**.

![Algorithm Visualization](../images/HEP-014/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `2 1 3`. A: `2 3`. B: `1 5`.
1. Clamp: `limit = (3+1)/2 = 2`.
   - `x_A = min(2, 2) = 2`.
   - `x_B = min(1, 2) = 1`.
2. Schedule Check:
   - `maxX = 2`. `atMax = [A]`.
   - `req = (2-1)*2 + 1 = 3`.
   - `3 <= 3`. OK.
3. Sum Check:
   - `sum = 2 + 1 = 3`.
   - `3 <= 3`. OK.
4. Score: `2*3 + 1*5 = 11`.

**Input:** `2 0 5`. A: `10 10`. B: `10 5`.
1. Clamp: `limit = 5`. `x_A=5, x_B=5`.
2. Schedule: `maxX=5`. `atMax=[A, B]`.
   - `req = 4*1 + 2 = 6`.
   - `6 > 5`. Fail.
   - `allowed = 5 - 4 = 1`.
   - Keep top 1 (A). Demote B to 4.
   - `x_A=5, x_B=4`.
   - Loop: `maxX=5`. `atMax=[A]`. `req=5`. OK.
3. Sum: `5+4=9`. `9 > 5`.
   - Remove 4.
   - Low prio is B. `x_B` becomes 0.
   - `x_A=5, x_B=0`.
4. Score: `50`.

## ✅ Proof of Correctness

### Invariant
- Feasibility depends only on `L = max(sum_x, (max_x - 1)(k + 1) + n_max)` and
  is achievable whenever `L <= T` (Task Scheduler bound).
- If `L > T`, only tasks at `max_x` can reduce the bound. Demoting the
  lowest-priority tasks among those at `max_x` preserves feasibility while
  losing the least score.
- Once `L <= T`, the only remaining restriction is `sum_x <= T`. Removing units
  from the lowest-priority tasks maximizes the total score.

## 💡 Interview Extensions

- **Extension 1:** Infinite T?
  - *Answer:* Just sum all priorities.
- **Extension 2:** Dynamic priorities?
  - *Answer:* Much harder, needs global optimization.

### Common Mistakes to Avoid

1. **Simple Greedy**
   - ❌ Wrong: Picking max priority at each step (simulation).
   - ✅ Correct: Global optimization of counts.
2. **Ignoring Cooldown**
   - ❌ Wrong: Only checking sum constraint.
   - ✅ Correct: Must check `(max-1)(k+1) + n_max`.

## Related Concepts

- **Task Scheduler (LC 621):** Core logic.
- **Greedy:** Global vs Local.
