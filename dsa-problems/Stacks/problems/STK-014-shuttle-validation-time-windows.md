---
problem_id: STK_SHUTTLE_VALIDATION_TIME_WINDOWS__2743
display_id: STK-014
slug: shuttle-validation-time-windows
title: "Shuttle Validation with Time Windows"
difficulty: Medium
difficulty_score: 61
topics:
  - Stack
  - Simulation
  - Constraints
tags:
  - stack
  - simulation
  - validation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-014: Shuttle Validation with Time Windows
## Problem Statement
You are given a push sequence and a pop sequence for a stack, along with timestamps for each push and pop. Some elements have time window constraints `W[x]` that require the element to be popped within `W[x]` time units after it was pushed. Some elements are marked as `priority` and must be popped before any larger non-priority element.
Determine whether all three conditions hold:
1. The pop sequence is valid for the given push sequence
2. Every constrained element is popped within its time window
3. Each priority element is popped before any larger non-priority element
Output `true` if all conditions hold, otherwise `false`.
![Problem Illustration](../images/STK-014/problem-illustration.png)
## Input Format
- First line: integer `n`
- Second line: `n` integers (push sequence)
- Third line: `n` integers (push times)
- Fourth line: `n` integers (pop sequence)
- Fifth line: `n` integers (pop times)
- Sixth line: integer `w` (number of window constraints)
- Next `w` lines: `value window`
- Next line: integer `p` (number of priority values)
- Next line: `p` integers (priority values)
## Output Format
- Single line: `true` or `false`
## Constraints
- `1 <= n <= 100000`
- `0 <= times <= 10^9`
- All values are integers and unique in the push sequence
## Example
**Input:**
```
3
4 5 6
0 2 4
6 5 4
5 6 10
1
5 2
1
4
```
**Output:**
```
false
```
**Explanation:**
Value 5 must be popped within 2 time units of push at time 2, but it is popped at time 6, so the window constraint fails.
![Example Visualization](../images/STK-014/example-1.png)
## Notes
- Simulate stack pushes and pops in order
- Check time window when an element is popped
- Track the smallest pending priority value
- Time complexity: O(n)
## Related Topics
Stack Simulation, Constraints Checking, Validation
---
## Solution Template
### Java
### Python
### C++
### JavaScript
