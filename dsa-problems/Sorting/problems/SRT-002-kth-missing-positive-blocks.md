---
problem_id: SRT_KTH_MISSING_POSITIVE_BLOCKS__4179
display_id: SRT-002
slug: kth-missing-positive-blocks
title: "Kth Missing Positive with Blocks"
difficulty: Easy
difficulty_score: 33
topics:
  - Sorting
  - Binary Search
  - Prefix Counts
tags:
  - sorting
  - binary-search
  - missing-number
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-002: Kth Missing Positive with Blocks

## Problem Statement

You are given a sorted array of unique positive integers. Define the list of missing positive integers in increasing order. A query provides `(k, blockSize)` and asks for the last number in the k-th block of size `blockSize` in that missing list.

Equivalently, the answer is the `(k * blockSize)`-th missing positive integer.

![Problem Illustration](../images/SRT-002/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated sorted positive integers
- Next `q` lines: two integers `k` and `blockSize`

## Output Format

- For each query, print the requested missing number

## Constraints

- `1 <= n, q <= 100000`
- `1 <= a[i] <= 10^9`
- `1 <= k, blockSize <= 10^9`

## Example

**Input:**

```
3 1
2 3 7
3 2
```

**Output:**

```
9
```

**Explanation:**

Missing positives are `1,4,5,6,8,9,...`. The 3rd block of size 2 ends at the 6th missing number, which is 9.

![Example Visualization](../images/SRT-002/example-1.png)

## Notes

- Precompute how many positives are missing up to each array value
- Use binary search to find the position of the m-th missing number
- m can be large (`k * blockSize`)
- Time per query: O(log n)

## Related Topics

Binary Search, Missing Number, Prefix Counts

---

## Solution Template
### Java


### Python


### C++


### JavaScript

