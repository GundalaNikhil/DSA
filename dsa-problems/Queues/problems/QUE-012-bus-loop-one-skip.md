---
problem_id: QUE_BUS_LOOP_ONE_SKIP__2986
display_id: QUE-012
slug: bus-loop-one-skip
title: "Bus Loop With One Free Skip"
difficulty: Medium
difficulty_score: 58
topics:
  - Greedy
  - Queue
  - Circular Route
tags:
  - greedy
  - circular
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-012: Bus Loop With One Free Skip

## Problem Statement

A circular bus route has `n` stops. At stop `i`, the bus can gain `gain[i]` fuel and must spend `cost[i]` fuel to reach the next stop.

You must skip refueling at exactly one stop (the fuel there is lost). Find a starting index that allows the bus to complete one full loop with that single skip. If no such start exists, output `-1`.

![Problem Illustration](../images/QUE-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `gain[i]`
- Third line: `n` space-separated integers `cost[i]`

## Output Format

- Single integer: a valid starting index (0-based), or `-1` if impossible

## Constraints

- `1 <= n <= 100000`
- `0 <= gain[i], cost[i] <= 10^9`

## Example

**Input:**

```
3
4 5 1
3 3 2
```

**Output:**

```
0
```

**Explanation:**

Start at index 0 and skip refuel at stop 2:

- Stop 0: gain 4, cost 3 -> fuel 1
- Stop 1: gain 5, cost 3 -> fuel 3
- Stop 2: skip gain 1, cost 2 -> fuel 1

The bus completes the loop with fuel remaining, so index 0 is valid.

![Example Visualization](../images/QUE-012/example-1.png)

## Notes

- Track two running balances: without skip and with skip used
- If both balances drop below 0, reset the start
- The total gain minus the skipped refuel must still cover total cost
- Time complexity: O(n)

## Related Topics

Greedy, Circular Array, Simulation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

