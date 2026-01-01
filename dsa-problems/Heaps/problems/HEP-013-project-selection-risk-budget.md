---
problem_id: HEP_PROJECT_SELECTION_RISK_BUDGET__2917
display_id: HEP-013
slug: project-selection-risk-budget
title: "Project Selection with Risk Budget"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Greedy
  - Finance
tags:
  - heaps
  - greedy
  - risk-budget
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-013: Project Selection with Risk Budget

## Problem Statement

You have `n` projects. Project `i` has cost `c_i`, profit `p_i`, and risk `r_i`. You start with capital `C` and risk budget `R`. You may select at most `k` projects. A project can be selected only if:

- `c_i <= current capital`
- `current risk + r_i <= R`

When you select a project, your capital increases by `p_i` and your risk increases by `r_i`.

Return the maximum final capital you can achieve.

![Problem Illustration](../images/HEP-013/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, `C`, `R`
- Next `n` lines: `c_i p_i r_i`

## Output Format

- Single integer: maximum final capital

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- `0 <= C, R <= 10^12`
- `1 <= c_i, p_i, r_i <= 10^9`

## Example

**Input:**

```
3 2 1 3
1 2 1
2 2 2
3 5 2
```

**Output:**

```
5
```

**Explanation:**

Pick projects 1 and 2:

- Start: capital=1, risk=0
- Project 1: capital=3, risk=1
- Project 2: capital=5, risk=3

Final capital is 5.

![Example Visualization](../images/HEP-013/example-1.png)

## Notes

- Sort projects by cost to unlock affordable options
- Use a max-heap of profits among projects within risk budget
- Greedily pick the most profitable affordable project each step
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Greedy, Resource Allocation, Scheduling

---

## Solution Template

### Java


### Python


### C++


### JavaScript

