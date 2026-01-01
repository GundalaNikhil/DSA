---
problem_id: GRD_CAMPUS_EVENT_TICKET_CAPS__5864
display_id: GRD-011
slug: campus-event-ticket-caps
title: "Campus Event Ticket Caps"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Heap
  - Scheduling
tags:
  - greedy
  - heap
  - priority-queue
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-011: Campus Event Ticket Caps

## Problem Statement

You have `n` ticket requests for campus events. Each request `i` has:

- Quantity `q[i]` (number of tickets requested)
- Deadline `d[i]` (last day to process this request)

You can process at most **one request per day** (day 1, day 2, ...). Partial fulfillment counts as processing a request (and uses up one day).

Your goal is to maximize the total number of tickets sold.

![Problem Illustration](../images/GRD-011/problem-illustration.png)

## Input Format

- First line: integer `n` (number of requests)
- Next `n` lines: two integers `q d` representing quantity and deadline for each request

## Output Format

- Single integer: maximum total tickets that can be sold

## Constraints

- `1 <= n <= 10^5`
- `1 <= q[i], d[i] <= 10^5`

## Example

**Input:**

```
3
3 1
5 3
2 2
```

**Output:**

```
7
```

**Explanation:**

Requests:

- Request 0: 3 tickets, deadline day 1
- Request 1: 5 tickets, deadline day 3
- Request 2: 2 tickets, deadline day 2

Greedy strategy (sort by deadline):

- Day 1: Process request 0 (deadline 1) → sell 3 tickets
- Day 2: Process request 2 (deadline 2) → sell 2 tickets
- Day 3: Process request 1 (deadline 3) → sell 5 tickets

Total: 3 + 5 + 2 = 10 tickets

By processing requests in order of deadline, we maximize the number of tickets sold.

![Example Visualization](../images/GRD-011/example-1.png)

## Notes

- Sort requests by deadline
- Use a min-heap to track quantities of selected requests
- For each day, tentatively include all requests with deadline >= current day
- If more requests than available days, drop the smallest quantities
- Greedy strategy: prioritize larger quantities within deadline constraints
- Time complexity: O(n log n)

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Scheduling, Optimization

---

## Solution Template

### Java


### Python


### C++


### JavaScript

