# Task Priority Scheduler

**Problem ID:** HEAP-005
**Display ID:** 88
**Question Name:** Task Priority Scheduler
**Slug:** task-priority-scheduler
**Title:** Process Tasks by Priority and Deadline
**Difficulty:** Medium
**Premium:** No
**Tags:** Heap, Greedy, Sorting, Scheduling

## Problem Description

You are designing a task scheduler for an operating system. Each task has a priority level (1-10, where 10 is highest priority) and a deadline (timestamp by which it must complete). The CPU can process one task at a time, and each task takes a fixed amount of processing time.

Given an array of tasks with their priorities, deadlines, and processing times, determine the optimal order to execute tasks to maximize the number of tasks completed before their deadlines, prioritizing higher-priority tasks when deadlines allow.

## A Simple Scenario (Daily Life Usage)

Imagine your computer's task manager juggling multiple processes: a critical system update (priority 10, deadline in 5 seconds), a video render (priority 6, deadline in 30 seconds), and a file download (priority 4, deadline in 60 seconds). The scheduler must decide which tasks to run first. The system update must run immediately due to high priority and tight deadline. If two tasks have the same deadline, higher priority wins. This ensures your computer runs smoothly without missing critical deadlines.

## Your Task

You are given an array of tasks where each task is represented as:
- `taskId`: unique identifier (string)
- `priority`: importance level 1-10 (integer, 10 is highest)
- `deadline`: time by which task must complete (integer)
- `duration`: time needed to process task (integer)

You start at time = 0. Schedule tasks to maximize completed tasks before their deadlines. When multiple tasks can be scheduled, choose the one with:
1. Higher priority first
2. If priorities are equal, choose earlier deadline

Return an array of taskIds in the order they should be executed. Only include tasks that will complete before their deadline.

## Why is it Important?

This problem teaches you:

- Using heaps for priority-based scheduling algorithms
- Greedy algorithms for optimization problems
- Handling multiple constraints (priority + deadline)
- Real-world operating system concepts
- Time management in resource-constrained systems

## Examples

### Example 1:

**Input:**
```
tasks = [
  {taskId: "T1", priority: 5, deadline: 10, duration: 5},
  {taskId: "T2", priority: 8, deadline: 8, duration: 3},
  {taskId: "T3", priority: 3, deadline: 15, duration: 4}
]
```

**Output:** `["T2", "T1", "T3"]`

**Explanation:**
- Time 0: Start T2 (highest priority 8, finishes at time 3, before deadline 8) ✓
- Time 3: Start T1 (priority 5, finishes at time 8, before deadline 10) ✓
- Time 8: Start T3 (priority 3, finishes at time 12, before deadline 15) ✓
All tasks complete before their deadlines.

### Example 2:

**Input:**
```
tasks = [
  {taskId: "T1", priority: 10, deadline: 5, duration: 6},
  {taskId: "T2", priority: 7, deadline: 10, duration: 4},
  {taskId: "T3", priority: 9, deadline: 12, duration: 5}
]
```

**Output:** `["T2", "T3"]`

**Explanation:**
- T1 has highest priority but duration 6 > deadline 5, so it will miss deadline regardless
- Time 0: Start T2 (priority 7, finishes at time 4, before deadline 10) ✓
- Time 4: Start T3 (priority 9, finishes at time 9, before deadline 12) ✓
- T1 cannot be scheduled without missing its deadline

### Example 3:

**Input:**
```
tasks = [
  {taskId: "T1", priority: 6, deadline: 20, duration: 5},
  {taskId: "T2", priority: 6, deadline: 15, duration: 4},
  {taskId: "T3", priority: 8, deadline: 25, duration: 3}
]
```

**Output:** `["T3", "T2", "T1"]`

**Explanation:**
- T3 has highest priority (8), starts at time 0, finishes at time 3 ✓
- T2 and T1 both have priority 6, but T2 has earlier deadline (15 vs 20)
- Time 3: Start T2, finishes at time 7 ✓
- Time 7: Start T1, finishes at time 12 ✓

## Constraints

- 1 ≤ tasks.length ≤ 1000
- 1 ≤ priority ≤ 10
- 1 ≤ deadline ≤ 10^5
- 1 ≤ duration ≤ 10^4
- All taskIds are unique
- It's possible that no tasks can be completed before their deadlines

## Asked by Companies

- Apple
- Microsoft
- Google
- Amazon
