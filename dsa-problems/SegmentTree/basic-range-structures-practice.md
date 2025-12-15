# Original Segment Tree / Fenwick / Range Structure Practice Set (16 Questions)

## 1) Range Sum with Point Updates
- Slug: range-sum-point-updates
- Difficulty: Easy-Medium
- Problem: Support an array with operations: `update(i, val)` replace a[i], and `query(l, r)` sum over [l, r]. Return answers to queries.
- Constraints: `1 <= n, q <= 2 * 10^5`, values fit 64-bit.
- Example:
  - Input: n=5, arr=[1,2,3,4,5]; ops: query(1,3), update(2,10), query(0,4)
  - Output: [9, 22]

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

## 9) Range Majority Check
- Slug: range-majority-check
- Difficulty: Medium
- Problem: Queries [l,r] ask if there exists a majority element (> half) and return it or -1.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Hint: Segment tree with Boyer-Moore candidate + count; verify with freq query (Fenwick).
- Example:
  - Input: arr=[1,1,2,3,1], query(0,4)
  - Output: 1

## 10) Range GCD with Updates
- Slug: range-gcd-updates
- Difficulty: Medium
- Problem: Point updates; queries ask gcd of [l,r].
- Constraints: `1 <= n,q <= 2 * 10^5`, `|a[i]| <= 10^9`.
- Hint: Segment tree on gcd.
- Example:
  - Input: arr=[6,9,3], query(0,2)
  - Output: 3

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

## 13) Range Sum of Powers
- Slug: range-sum-of-powers
- Difficulty: Medium
- Problem: Queries ask sum of a[i]^2 over [l,r]; support point updates.
- Constraints: `1 <= n,q <= 2 * 10^5`, values within 32-bit.
- Hint: Segment tree storing both sum and sumsq for updates.
- Example:
  - Input: arr=[1,2], query(0,1)
  - Output: 5

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
