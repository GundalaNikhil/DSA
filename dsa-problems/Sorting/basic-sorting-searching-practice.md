# Original Sorting & Searching Practice Set (16 Questions)

## 1) Partial Selection Sort Stats

- Slug: partial-selection-sort-stats
- Difficulty: Easy
- Problem: Given an array, simulate only the first `k` iterations of selection sort (finding min and swapping with position i). Return the array after `k` iterations.
- Constraints: `1 <= n <= 10^5`, `0 <= k <= n-1`.
- Example:
  - Input: `[4,3,1,2], k=2`
  - Output: `[1,2,3,4]`

## 2) Kth Missing Positive with Blocks

- Slug: kth-missing-positive-blocks
- Difficulty: Easy-Medium
- Problem: Sorted array of unique positives `arr`, and queries of form `(k, blockSize)` where missing numbers are counted in blocks of size blockSize (i.e., skip ahead by blockSize when counting missing). For each query, find the k-th missing number under that counting scheme.
- Constraints: `1 <= n <= 10^5`, `1 <= q <= 10^5`, `1 <= blockSize <= 10^9`.
- Hint: Precompute standard missing counts; adjust by block factor.
- Example:
  - Input: `arr=[2,3,7], query (k=3, block=2)`
  - Output: `9` (missing numbers counted as 1,4,5,6,8,9,... in blocks of 2)

## 3) Stable Sort By Two Keys

- Slug: stable-sort-two-keys
- Difficulty: Easy-Medium
- Problem: Sort records by key1 ascending, then key2 descending, but stability requirement: original order of equal pairs must be kept. Implement with a stable algorithm conceptually.
- Constraints: `1 <= n <= 10^5`.
- Example:
  - Input: `[(1,2),(1,1),(0,9)]`
  - Output: `[(0,9),(1,2),(1,1)]`

## 4) Minimum Inversions After One Swap

- Slug: min-inversions-one-swap
- Difficulty: Medium
- Problem: Find the minimum possible inversion count after performing at most one swap of two elements.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Use BIT/Fenwick to compute inversions; test swapping candidates found via out-of-order pairs.
- Example:
  - Input: `[3,1,2]`
  - Output: `0` (swap 3 and 1)

## 5) Two-Pointer Sum Closest to Target

- Slug: two-pointer-closest-target
- Difficulty: Easy-Medium
- Problem: Given sorted array and target, find pair sum closest to target; return the pair.
- Constraints: `2 <= n <= 2 * 10^5`.
- Example:
  - Input: `[1,4,6,8], target=10`
  - Output: `(4,6)`

## 6) K-Sorted Array Minimum Swaps

- Slug: k-sorted-array-min-swaps
- Difficulty: Medium
- Problem: An array is k-sorted if every element is at most k positions away from its sorted position. Given such an array and k, find min swaps to fully sort it.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= k < n`.
- Hint: Use indexed positions after sorting; count cycles within windows.
- Example:
  - Input: `[3,1,2], k=2`
  - Output: `2`

## 7) Binary Search In Rotated With Duplicates Count

- Slug: search-rotated-duplicates-count
- Difficulty: Medium
- Problem: Given a rotated sorted array with duplicates, count how many times value `x` occurs.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Find rotation pivot; binary search ranges; or use modified binary to find first/last occurrence.
- Example:
  - Input: `[4,5,5,1,2,3], x=5`
  - Output: `2`

## 8) Balanced Range Covering K Lists

- Slug: balanced-range-covering-k-lists
- Difficulty: Medium
- Problem: Given k sorted lists, find an interval [L,R] of minimum length that contains at least two numbers from each list (if a list has only one number, it must appear). Return any one such interval; if impossible, return empty.
- Constraints: `1 <= total elements <= 2 * 10^5`, `1 <= k <= 10^5`.
- Hint: Merge k lists with a min-heap; maintain counts per list and a deque to ensure each list contributes two; slide window.
- Example:
  - Input: `[[1,4,10],[0,9],[5,6,18]]`
  - Output: `[4,6]`

## 9) Weighted Median of Two Sorted Arrays

- Slug: weighted-median-two-sorted
- Difficulty: Medium
- Problem: Two sorted arrays A and B come with weights wA and wB (positive integers). Treat each element of A as repeated wA times and each of B as repeated wB times. Return the median of the multiset without expanding it.
- Constraints: `1 <= n,m <= 10^5`, `1 <= wA,wB <= 10^6`.
- Hint: Binary search on value space using prefix counts; similar to kth order statistic on weighted arrays.
- Example:
  - Input: `A=[1,3], B=[2,7], wA=1, wB=2`
  - Expanded multiset (conceptual): `[1, 3, 2, 2, 7, 7]` → sorted: `[1, 2, 2, 3, 7, 7]`
  - Total count = 6 (even), median = average of 3rd and 4th = (2+3)/2 = 2.5
  - Output: `2.5`

## 10) Sort Colors With Frozen Indexes

- Slug: sort-colors-frozen
- Difficulty: Medium
- Problem: Array contains 0,1,2; some indices are frozen and cannot move. Reorder movable elements to get 0s before 1s before 2s while keeping frozen elements in place.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Collect movable elements, sort, reinsert around frozen slots.
- Example:
  - Input: `arr=[2,1,0,2,0,1], frozen={1,4}`
  - Output: `[0,1,0,2,0,1]` (frozen positions stay)

## 11) Longest Consecutive After At Most One Change

- Slug: longest-consecutive-one-change
- Difficulty: Medium
- Problem: Find the length of the longest consecutive increasing subsequence you can obtain by changing at most one element to any value.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Prefix/suffix lengths; try bridging gap with one change.
- Example:
  - Input: `[1,2,5,3,4,5]`
  - Output: `5` (change 5 to 3 to get 1,2,3,4,5)

## 12) Count Within Threshold After Self

- Slug: count-within-threshold-after-self
- Difficulty: Medium
- Problem: For each element `a[i]`, count how many elements to its right satisfy `a[i] - a[j] <= T` (threshold given). Return the counts.
- Constraints: `1 <= n <= 2 * 10^5`, `-10^9 <= a[i] <= 10^9`, `0 <= T <= 10^9`.
- Hint: Use merge-sort based counting on sorted halves comparing differences.
- Example:
  - Input: `a=[5,2,6,1], T=3`
  - Output: `[2,1,1,0]` (for 5: 2 and 1 within 3; for 2: only 1 within 3; for 6: none within 3 except 1; for 1: none)

## 13) Closest Pair in Sorted Circular Array

- Slug: closest-pair-sorted-circular
- Difficulty: Medium
- Problem: Given a sorted circular array, find pair with sum closest to target (wrap-around allowed).
- Constraints: `2 <= n <= 2 * 10^5`.
- Hint: Find pivot; use two-pointer circular.
- Example:
  - Input: `[4,5,1,2,3], target=7`
  - Output: `(4,3)`

## 14) Minimum Operations to Make Array Alternating

- Slug: min-ops-make-alternating
- Difficulty: Medium
- Problem: Array should be strictly alternating between two values `x` and `y`. You may change elements; find minimal changes and resulting pair `(x,y)` (x != y).
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Count frequencies on even/odd positions; choose best pair maximizing correct placements.
- Example:
  - Input: `[1,1,1,2]`
  - Output: `1` change (make pattern 1,2,1,2)

## 15) Kth Smallest Triple Sum

- Slug: kth-smallest-triple-sum
- Difficulty: Medium
- Problem: Find the k-th smallest value of `a[i]+a[j]+a[k]` over all i<j<k.
- Constraints: `3 <= n <= 10^5`, `1 <= k <= n*(n-1)*(n-2)/6`.
- Hint: Sort array; binary search on sum; count triples <= mid with two-pointer.
- Example:
  - Input: `[1,2,4,7], k=3`
  - Output: `7` (triple sums sorted: 7,10,12,13)

## 16) Locate Peak with Limited Queries

- Slug: locate-peak-limited-queries
- Difficulty: Medium
- Problem: You can query array elements by index at most `q` times (black-box API). Array has at least one peak (greater than neighbors). Devise a strategy to find a peak index within `q` queries.
- Constraints: `1 <= n <= 10^5`, `1 <= q <= 20`.
- Hint: Binary search with lazy evaluation; ensure you don't exceed query budget.
- Example:
  - Input: implicit array `[1,3,2,4,1]`, q=5
  - Output: `1` or `3`
