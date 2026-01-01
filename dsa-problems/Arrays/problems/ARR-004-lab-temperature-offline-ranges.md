---
problem_id: ARR_TEMP_OFFLINE_RANGES__5631
display_id: ARR-004
slug: lab-temperature-offline-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 46
topics:
  - Arrays
  - Difference Array
  - Prefix Sum
tags:
  - arrays
  - difference-array
  - prefix-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-004: Lab Temperature Offline Ranges

## Problem Statement

You are given an array of temperatures and a list of queries. Each query is either an add-range operation or a sum-range request.
All add queries appear before sum queries and should be applied cumulatively. 
After applying all adds, answer each sum query in order.

![Problem Illustration](../images/ARR-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers temps[i]
- Third line: integer q, the number of queries
- Next q lines: either "add l r x" or "sum l r"

## Output Format

Print the answers to sum queries in order, space-separated.

## Constraints

- `1 <= n, q <= 100000`
- `-1000000000 <= temps[i], x <= 1000000000`
- `0 <= l <= r < n`

## Example

**Input:**
```
3
1 2 3
4
add 0 1 5
add 2 2 -1
sum 0 2
sum 1 2
```

**Output:**
```
15 9
```

**Explanation:**

After both add queries, temps become [6, 7, 2].
Then sum 0..2 is 15 and sum 1..2 is 9.

![Example Visualization](../images/ARR-004/example-1.png)

## Notes

- All add queries appear before sum queries.
- Use 64-bit integers for sums.

## Related Topics

Difference Array, Prefix Sum, Range Queries

---

## Solution Template

### Java



### Python



### C++



### JavaScript


