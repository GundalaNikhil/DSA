---
problem_id: ARR_TOPK_DECAY_SCORE__1198
display_id: ARR-013
slug: tool-frequency-top-k-decay
title: "Tool Frequency Top K with Recency Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Arrays
  - Heap
  - Hashing
tags:
  - arrays
  - heap
  - hashing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-013: Tool Frequency Top K with Recency Decay

## Problem Statement

Each value appears with a timestamp. The score of a value v at time now is the sum of exp(-(now - t) / D) over all timestamps t where v appears.
Return the k values with the highest decayed scores. Break ties by smaller value.

![Problem Illustration](../images/ARR-013/problem-illustration.png)

## Input Format

- First line: integer n
- Next n lines: value and timestamp
- Last line: integers now, D, and k

## Output Format

Print k values in descending score order, space-separated.

## Constraints

- `1 <= n <= 200000`
- `Timestamps are non-decreasing`
- `1 <= k <= n`
- `1 <= D <= 1000000`

## Example

**Input:**
```
3
5 0
5 1
3 2
5 2 1
```

**Output:**
```
3
```

**Explanation:**

Score(5) = exp(-(5-0)/2) + exp(-(5-1)/2) = exp(-2.5) + exp(-2).
Score(3) = exp(-(5-2)/2) = exp(-1.5), which is larger, so 3 is returned.

![Example Visualization](../images/ARR-013/example-1.png)

## Notes

- Use double precision for scores.
- Ties are broken by smaller value.

## Related Topics

Heap, Hashing, Arrays

---

## Solution Template

### Java



### Python



### C++



### JavaScript


