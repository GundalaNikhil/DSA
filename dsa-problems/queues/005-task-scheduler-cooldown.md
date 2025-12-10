# Task Scheduler Cooldown

**Problem ID:** QUE-005
**Display ID:** 28
**Question Name:** Task Scheduler Cooldown
**Slug:** task-scheduler-cooldown
**Title:** Task Scheduler
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Queue, Greedy, Heap, Scheduling

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a characters array tasks representing different tasks where each letter represents a different task, and a non-negative integer n representing the cooldown period between two same tasks, return the minimum number of intervals required to complete all tasks. During the cooldown period, the CPU can either perform a different task or stay idle.

## A Simple Scenario (Daily Life Usage)

You're operating a laundry service with washing machines. Each type of laundry (towels=T, bedsheets=B, clothes=C) requires a cooldown period of n minutes after washing before the same type can be washed again (to prevent overheating). You want to minimize total time by strategically scheduling different laundry types and accepting idle time when necessary.

## Your Task

Given an array of tasks and cooldown period n, return the minimum number of time intervals needed to complete all tasks.

## Why is it Important?

This problem teaches you:

- Task scheduling algorithms
- Greedy strategy application
- Queue-based cooldown management
- Optimal resource utilization

## Examples

### Example 1:

**Input:** `tasks = ["A","A","A","B","B","B"], n = 2`

**Output:** `8`

**Explanation:**
```
A -> B -> idle -> A -> B -> idle -> A -> B
Total intervals: 8
We need cooldown of 2 between same tasks (like washing machines cooling down).
```

### Example 2:

**Input:** `tasks = ["A","A","A","B","B","B"], n = 0`

**Output:** `6`

**Explanation:**
```
No cooldown needed, so we can do: A -> A -> A -> B -> B -> B
Total intervals: 6
```

### Example 3:

**Input:** `tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2`

**Output:** `16`

**Explanation:**
```
One optimal schedule:
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
The most frequent task determines minimum time needed.
```

## Constraints

- 1 ≤ tasks.length ≤ 10^4
- tasks[i] is an uppercase English letter
- 0 ≤ n ≤ 100

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google
- Facebook
- Amazon
- Microsoft

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
