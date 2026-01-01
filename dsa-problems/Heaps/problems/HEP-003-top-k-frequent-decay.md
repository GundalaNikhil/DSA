---
problem_id: HEP_TOP_K_FREQUENT_DECAY__5829
display_id: HEP-003
slug: top-k-frequent-decay
title: "Top K Frequent with Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Lazy Updates
  - Time Decay
tags:
  - heaps
  - decay
  - frequency
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-003: Top K Frequent with Decay

## Problem Statement

You receive events with timestamps. Each event adds 1 to the count of a key. Every `d` seconds, counts decay by half. At query time `t`, the effective count for a key is:

```
count * 0.5^(floor((t - last_update) / d))
```

Return the top `k` keys by effective count at each query. Break ties by lexicographic order. If fewer than `k` keys exist, return all. If no keys exist, output `EMPTY`.

![Problem Illustration](../images/HEP-003/problem-illustration.png)

## Input Format

- First line: three integers `q`, `d`, and `k`
- Next `q` lines:
  - `ADD key t`
  - `QUERY t`

## Output Format

- For each `QUERY`, output one line with up to `k` keys separated by spaces, or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= d <= 10^9`
- `1 <= k <= 100000`
- `0 <= t <= 10^9`
- `1 <= |key| <= 20` (lowercase letters)

## Example

**Input:**

```
4 5 1
ADD a 0
ADD a 5
ADD b 5
QUERY 10
```

**Output:**

```
a
```

**Explanation:**

At t=10:

- a was updated at t=5 with count 1.5, then decays once -> 0.75
- b was updated at t=5 with count 1, then decays once -> 0.5

Top 1 key is a.

![Example Visualization](../images/HEP-003/example-1.png)

## Notes

- Store last update time and current count per key
- Apply decay lazily when a key is accessed
- Use a max-heap for retrieving top k keys per query
- Time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Heaps, Time Decay, Lazy Updates, Streaming

---

## Solution Template

### Java


### Python


### C++


### JavaScript

