---
problem_id: HEP_MERGE_K_STREAMS_RATE_LIMIT__9034
display_id: HEP-002
slug: merge-k-streams-rate-limit
title: "Merge K Streams with Rate Limit"
difficulty: Medium
difficulty_score: 52
topics:
  - Heaps
  - K-Way Merge
  - Streaming
tags:
  - heaps
  - k-way-merge
  - rate-limit
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-002: Merge K Streams with Rate Limit

## Problem Statement

You are given `k` sorted streams. In each round, every stream can contribute at most `r` elements. After a stream has contributed `r` elements in the current round, it is blocked until the next round. Within a round, always output the smallest available element among the unblocked streams.

Return the merged sequence produced by this round-based rate limit.

![Problem Illustration](../images/HEP-002/problem-illustration.png)

## Input Format

- First line: two integers `k` and `r`
- For each stream `i` from 1 to `k`:
  - Line 1: integer `m_i` (length of stream)
  - Line 2: `m_i` integers in non-decreasing order

## Output Format

- Single line of integers: the merged sequence in order

## Constraints

- `1 <= k <= 100000`
- `0 <= total elements <= 200000`
- `1 <= r <= 100000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
2 1
2
1 4
3
2 3 5
```

**Output:**

```
1 2 3 4 5
```

**Explanation:**

Round 1 (limit 1 per stream): available heads {1, 2} -> output 1, 2

Round 2: available heads {4, 3} -> output 3, 4

Round 3: available heads {5} -> output 5

![Example Visualization](../images/HEP-002/example-1.png)

## Notes

- Use a min-heap of (value, stream index)
- Track how many elements each stream has emitted in the current round
- When the heap is empty but elements remain, reset round counters
- Time complexity: O(N log k)
- Space complexity: O(k)

## Related Topics

Heaps, K-Way Merge, Streaming, Rate Limiting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

