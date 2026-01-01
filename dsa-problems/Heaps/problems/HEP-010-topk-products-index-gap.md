---
problem_id: HEP_TOPK_PRODUCTS_INDEX_GAP__8206
display_id: HEP-010
slug: topk-products-index-gap
title: "Top K Products with Index Gap"
difficulty: Medium
difficulty_score: 59
topics:
  - Heaps
  - K Largest Pairs
  - Search
tags:
  - heaps
  - k-largest
  - two-arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-010: Top K Products with Index Gap

## Problem Statement

You are given two arrays `A` and `B`, each sorted in non-increasing order. Find the `k` largest products `A[i] * B[j]` subject to the constraint:

```
|i - j| >= d
```

Indices are 0-based. If fewer than `k` valid pairs exist, return all of them. Output products in descending order.

![Problem Illustration](../images/HEP-010/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `k`, and `d`
- Second line: `n` integers for `A`
- Third line: `m` integers for `B`

## Output Format

- Single line of products in descending order

## Constraints

- `1 <= n, m <= 100000`
- `1 <= k <= min(100000, n * m)`
- `0 <= d < max(n, m)`
- `-10^9 <= A[i], B[j] <= 10^9`

## Example

**Input:**

```
3 3 3 1
9 7 5
8 3 1
```

**Output:**

```
56 40 27
```

**Explanation:**

Valid pairs with |i - j| >= 1 include:

- (1,0): 7 * 8 = 56
- (2,0): 5 * 8 = 40
- (0,1): 9 * 3 = 27

Top 3 products are 56, 40, 27.

![Example Visualization](../images/HEP-010/example-1.png)

## Notes

- Use a max-heap of candidate pairs
- Expand neighbors (i+1,j) and (i,j+1) when valid
- Track visited pairs to avoid duplicates
- Time complexity: O(k log k)
- Space complexity: O(k)

## Related Topics

Heaps, K Largest Pairs, Search, Two Arrays

---

## Solution Template

### Java


### Python


### C++


### JavaScript

