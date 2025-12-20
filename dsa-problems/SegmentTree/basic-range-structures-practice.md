# Original Segment Tree / Fenwick / Range Structure Practice Set (16 Questions)

## 1) Range Sum with Point Updates and Undo

- Slug: range-sum-point-updates-undo
- Difficulty: Medium
- Problem: Support an array with operations: `update(i, val)` replace a[i], `query(l, r)` sum over [l, r] modulo M, and `undo(k)` which reverts the last k updates. Return answers to queries.
- Constraints: `1 <= n, q <= 2 * 10^5`, values fit 64-bit, `1 <= M <= 10^9+7`, `0 <= k <= min(q, 100)`.
- Hint: Fenwick/Segment Tree with operation history stack for rollback.
- Example:
  - Input: n=5, arr=[1,2,3,4,5], M=1000; ops: query(1,3), update(2,10), query(0,4), undo(1), query(0,4)
  - Output: [9, 22, 15]

## 2) Range Add, Range Sum

- Slug: range-add-range-sum
- Difficulty: Medium
- Problem: Support operations: add `x` to all elements in [l, r], and query sum over [l, r].
- Constraints: `1 <= n, q <= 2 * 10^5`.
- Hint: Use segment tree with lazy propagation or Fenwick with difference trick.
- Example:
  - Input: n=3, arr=[0,0,0]; ops: add(0,1,5), add(1,2,2), query(0,2)
  - Output: [9]

## 3) Range Minimum with Range Add

- Slug: range-min-range-add
- Difficulty: Medium
- Problem: Support range add updates and range minimum queries.
- Constraints: `1 <= n, q <= 2 * 10^5`.
- Hint: Segment tree with lazy; store min.
- Example:
  - Input: arr=[3,1,4], ops: add(0,2,2), min(1,2)
  - Output: [3]

## 4) Inversion Count Updates

- Slug: inversion-count-updates
- Difficulty: Medium
- Problem: Array of size n <= 2e5 with point updates. After each update, output current inversion count.
- Constraints: Values within 32-bit; coordinate compress.
- Hint: Fenwick for counts; segment tree over value domain.
- Example:
  - Input: arr=[3,1,2]; update pos1->4
  - Output: initial 2, after update 2

## 5) K-th Order Statistic in Prefix

- Slug: kth-order-stat-prefix
- Difficulty: Medium
- Problem: Support queries: given r and k, find k-th smallest element in a[0..r].
- Constraints: `1 <= n, q <= 2 * 10^5`, 0-indexed.
- Hint: Persistent segment tree on value domain.
- Example:
  - Input: arr=[5,1,3,2], query(r=3,k=2)
  - Output: 2 (sorted prefix [1,2,3,5])

## 6) Count of Values in Range

- Slug: count-values-in-range
- Difficulty: Medium
- Problem: Support point updates and queries counting how many elements in [l,r] fall into value interval [x,y].
- Constraints: `1 <= n,q <= 2 * 10^5`, values fit 32-bit.
- Hint: Segment tree of Fenwicks or offline compress with BIT of BIT.
- Example:
  - Input: arr=[1,5,2], query l=0 r=2 x=2 y=5
  - Output: 2

## 7) Range XOR Basis

- Slug: range-xor-basis
- Difficulty: Medium
- Problem: Support point updates and queries asking for the maximum XOR obtainable from any subset of elements in [l,r].
- Constraints: `1 <= n,q <= 10^5`.
- Hint: Segment tree storing linear basis; merge bases.
- Example:
  - Input: arr=[1,2,3], query(0,2)
  - Output: 3

## 8) Longest Increasing Subarray After Updates

- Slug: longest-increasing-subarray-updates
- Difficulty: Medium
- Problem: Point updates on array; after each, report length of longest strictly increasing contiguous subarray.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Hint: Segment tree storing prefix/suffix inc lengths and full length.
- Example:
  - Input: arr=[1,2,1], update pos2->3
  - Output: initial 2, after update 3

## 9) Range T-Threshold Majority Check

- Slug: range-t-threshold-majority
- Difficulty: Medium-Hard
- Problem: Queries [l,r,T] ask if there exists an element appearing at least T times in the range (where T varies per query). Return the element with highest frequency if it meets threshold, or -1. If multiple meet threshold, return smallest value.
- Constraints: `1 <= n,q <= 2 * 10^5`, `1 <= T <= r-l+1`.
- Hint: Segment tree with frequency maps at each node; merge maps tracking top-k frequent; verify threshold at query time.
- Example:
  - Input: arr=[1,1,2,3,1], query(0,4,T=3)
  - Output: 1 (appears 3 times)

## 10) Range GCD with Skip Zones

- Slug: range-gcd-skip-zones
- Difficulty: Medium
- Problem: Point updates; queries ask gcd of [l,r] but skip elements at positions marked as "forbidden" in a bitmask. The forbidden set can be updated via `toggleForbidden(i)`. GCD of empty set returns 0.
- Constraints: `1 <= n,q <= 2 * 10^5`, `|a[i]| <= 10^9`, support negative values by taking absolute value.
- Hint: Segment tree on gcd with sparse representation; maintain forbidden bitmask separately; rebuild affected ranges on toggle.
- Example:
  - Input: arr=[6,9,3], forbidden={1}, query(0,2)
  - Output: 3 (gcd of 6 and 3, skipping index 1)

## 11) Range Minimum Index

- Slug: range-min-index
- Difficulty: Medium
- Problem: Queries ask for the index of the minimum value in [l,r]; in ties, pick smallest index. Support point updates.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Hint: Segment tree storing (value,index).
- Example:
  - Input: arr=[4,2,2], query(0,2)
  - Output: 1

## 12) Range Add, K-th Order

- Slug: range-add-kth-order
- Difficulty: Hard
- Problem: Support range add updates and queries asking for k-th smallest in [l,r].
- Constraints: `1 <= n,q <= 10^5`.
- Hint: Use sqrt-decomp with lazy and offline queries, or segment tree with value buckets.
- Example:
  - Input: arr=[1,2,3], add(0,2,1), kth(0,2,2)
  - Output: 3

## 13) Range Sum of Multiple Powers

- Slug: range-sum-multiple-powers
- Difficulty: Medium-Hard
- Problem: Queries ask for sum of a[i]^p over [l,r] where p is specified per query (p ∈ {1,2,3}). Support point updates. Return result modulo 10^9+7.
- Constraints: `1 <= n,q <= 2 * 10^5`, values within 32-bit, `1 <= p <= 3`.
- Hint: Segment tree storing sum, sum of squares, and sum of cubes; combine appropriately per query.
- Example:
  - Input: arr=[2,3], query(0,1,p=2), query(0,1,p=3)
  - Output: [13, 35] (2²+3²=13, 2³+3³=35)

## 14) K Smallest Prefix Updates

- Slug: k-smallest-prefix-updates
- Difficulty: Medium
- Problem: Maintain array; operation `setPrefix(k, x)` sets first k elements to x. Queries ask for sum of array.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Hint: Segment tree with range assignment lazy.
- Example:
  - Input: arr=[1,2,3], setPrefix(2,5), sum(0,2)
  - Output: 13

## 15) Range Min After Additive Toggles

- Slug: range-min-after-toggles
- Difficulty: Medium
- Problem: Two update types: add x to [l,r] and multiply by -1 on [l,r]. Queries: min in [l,r].
- Constraints: `1 <= n,q <= 10^5`.
- Hint: Segment tree with lazy storing add and flip flags.
- Example:
  - Input: arr=[1,-2,3], flip(0,2), add(1,2,1), min(0,2)
  - Output: -4

## 16) Dynamic Connectivity Over Time (Offline)

- Slug: dynamic-connectivity-offline
- Difficulty: Hard
- Problem: Given edges added/removed over time and connectivity queries, answer if nodes u,v are connected at query times.
- Constraints: `1 <= n <= 10^5`, `1 <= events <= 2 * 10^5`.
- Hint: Use segment tree over time with union-find rollback.
- Example:
  - Input: n=3; events: add(1-2) at t1..t3, query(1,2,t2), remove(1-2), query(1,2,t4)
  - Output: [true,false]
