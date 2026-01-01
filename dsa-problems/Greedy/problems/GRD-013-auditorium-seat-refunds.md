---
problem_id: GRD_AUDITORIUM_SEAT_REFUNDS__2841
display_id: GRD-013
slug: auditorium-seat-refunds
title: "Auditorium Seat Refunds"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-013: Auditorium Seat Refunds

## Problem Statement

An auditorium has seats organized in rows numbered 1 to `r`. Initially, all rows are fully occupied with `capacity[i]` seats in row `i`.

You receive `n` refund requests, where each request specifies a seat ID that includes the row number. When processing refunds, you want to minimize the highest occupied row index remaining after all refunds.

Return the highest occupied row number after processing all refund requests.

![Problem Illustration](../images/GRD-013/problem-illustration.png)

## Input Format

- First line: two integers `r n` (number of rows and number of refund requests)
- Second line: `r` space-separated integers representing initial capacity of each row
- Next `n` lines: two integers `row seat_id` representing each refund request

## Output Format

- Single integer: highest occupied row number (1-indexed) after all refunds

## Constraints

- `1 <= r <= 10^5`
- `1 <= capacity[i] <= 10^5`
- `0 <= n <= sum(capacity[i])`
- `1 <= row <= r`

## Example

**Input:**

```
3 3
5 4 3
3 1
3 2
2 1
```

**Output:**

```
2
```

**Explanation:**

Initial state:

- Row 1: 5 seats occupied
- Row 2: 4 seats occupied
- Row 3: 3 seats occupied

Refund requests:

1. Refund seat 1 from row 3 → Row 3 now has 2 seats
2. Refund seat 2 from row 3 → Row 3 now has 1 seat
3. Refund seat 1 from row 2 → Row 2 now has 3 seats

After processing:

- Row 1: 5 seats (still occupied)
- Row 2: 3 seats (still occupied)
- Row 3: 0 seats (completely empty after processing all refunds)

Since row 3 is completely empty, the highest occupied row is row 2.

The greedy strategy processes refunds from the highest rows first to minimize the highest occupied row number after all refunds are processed.

![Example Visualization](../images/GRD-013/example-1.png)

## Notes

- Track the occupancy count for each row
- Use a max-heap to efficiently track the highest occupied row
- After each refund, decrement the row's count
- If a row becomes empty (count = 0), it's no longer occupied
- Time complexity: O(n log r) for heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, State Management, Optimization

---

## Solution Template

### Java


### Python


### C++


### JavaScript

