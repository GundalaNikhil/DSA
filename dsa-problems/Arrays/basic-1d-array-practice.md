# Original 1D Array Practice Set (16 Questions)

## 1) Snack Restock Snapshot
- Slug: snack-restock-snapshot
- Difficulty: Easy
- Problem: Given daily deliveries `arr[i]`, output prefix averages rounded down for each day.
- Constraints: `1 <= n <= 10^5`, `0 <= arr[i] <= 10^6`.
- Hint: Maintain running sum; avg = sum//(i+1).
- Example:
  - Input: `[4, 6, 6, 0]`
  - Output: `[4, 5, 5, 4]`

## 2) Bench Flip With Locked Ends
- Slug: bench-flip-locked-ends
- Difficulty: Easy
- Problem: Reverse the array in place but keep the first and last elements fixed; only the middle segment reverses.
- Constraints: `2 <= n <= 2 * 10^5`.
- Hint: Two-pointer from positions 1 and n-2.
- Example:
  - Input: `[9, 3, 8, 1, 5]`
  - Output: `[9, 5, 1, 8, 3]`

## 3) Shuttle Shift With Blackout
- Slug: shuttle-shift-blackout
- Difficulty: Easy-Medium
- Problem: Rotate the array left by `k` but positions listed in `blackout` stay in place; only other positions rotate cyclically among themselves.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= k <= 10^9`, `|blackout| <= n`.
- Hint: Extract movable elements, rotate them, then reinsert.
- Example:
  - Input: `arr=[1,2,3,4,5], k=2, blackout={1,3}`
  - Output: `[3,2,5,4,1]`

## 4) Lab Temperature Offline Ranges
- Slug: lab-temperature-offline-ranges
- Difficulty: Medium
- Problem: Given temps array and queries `[l,r]`, some queries are type “add x to range” (offline, applied cumulatively), others ask for range sum after all adds. Return answers to sum queries.
- Constraints: `1 <= n,q <= 10^5`, `-10^9 <= temp[i], x <= 10^9`.
- Hint: Use difference array to accumulate adds, then prefix for final temps before answering sums with prefix sums.
- Example:
  - Input: `temps=[1,2,3], queries=[("add",0,1,5),("sum",0,2),("add",2,2,-1),("sum",1,2)]`
  - Output: `[16,9]`

## 5) Weighted Balance Point
- Slug: weighted-balance-point
- Difficulty: Medium
- Problem: Find smallest index `i` where `sum(left)*L == sum(right)*R` for given weights `L` and `R`; left excludes `i`, right excludes `i`. If none, return -1.
- Constraints: `1 <= n <= 2 * 10^5`, `-10^9 <= a[i] <= 10^9`, `1 <= L,R <= 10^6`.
- Hint: Precompute total; iterate maintaining left sum.
- Example:
  - Input: `a=[2,3,-1,3,2], L=2, R=1`
  - Output: `1` (left*2=4*2=8, right*1=8)

## 6) Zero Slide With Limit
- Slug: zero-slide-limit
- Difficulty: Easy-Medium
- Problem: Move all zeros to the end but allow at most `m` swaps total; stop once swaps exceed `m`. Return resulting array.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= m <= 10^9`.
- Hint: Use write pointer; count swaps when writing non-zero over zero.
- Example:
  - Input: `[0,4,0,5,7], m=1`
  - Output: `[4,0,5,7,0]`

## 7) Hostel Roster Merge With Gap
- Slug: hostel-roster-merge-gap
- Difficulty: Medium
- Problem: Merge two sorted arrays `A` and `B` into sorted order, but if two equal elements come from different arrays, place the one from `A` before the one from `B`. Return merged array.
- Constraints: `0 <= n,m <= 10^5`.
- Hint: Standard merge with tie-break on source.
- Example:
  - Input: `A=[1,3,3], B=[3,4]`
  - Output: `[1,3,3,3,4]`

## 8) Partner Pair Sum With Forbidden
- Slug: partner-pair-sum-forbidden
- Difficulty: Easy-Medium
- Problem: Given sorted array and target, find if a pair sums to target such that neither element index is in `forbidden` set.
- Constraints: `1 <= n <= 2 * 10^5`, `|forbidden| <= n`.
- Hint: Two-pointer skipping forbidden indices.
- Example:
  - Input: `arr=[1,4,6,7], target=11, forbidden={0}`
  - Output: `true` (4 + 7)

## 9) Best Streak With One Smoothing
- Slug: best-streak-one-smoothing
- Difficulty: Medium
- Problem: You may choose exactly one index `i` and replace `a[i]` with `floor((a[i-1]+a[i]+a[i+1])/3)` (use existing neighbors; for endpoints, smoothing not allowed). Then compute the maximum subarray sum. Find the maximum achievable sum.
- Constraints: `3 <= n <= 2 * 10^5`, `-10^9 <= a[i] <= 10^9`.
- Hint: Precompute best prefix/suffix Kadane values; test smoothing effect as replacing `a[i]` with new value and combining left/right bests.
- Example:
  - Input: `[-2, 3, -4, 5]`
  - Output: `9` (smooth -4 with neighbors -> floor((3-4+5)/3)=1; subarray 3+1+5)

## 10) Early Discount With Stay Window and Ceiling
- Slug: early-discount-stay-window
- Difficulty: Medium
- Problem: You may buy once and sell once. You must hold the item for at least `dMin` days and at most `dMax` days, and the sell price must not exceed a ceiling `C` (if price > C, you are forced to sell at C). Return maximum achievable profit (or 0 if not profitable).
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= price[i] <= 10^9`, `1 <= dMin <= dMax <= n`.
- Hint: Track best effective buy value up to day i-dMin; when selling on day i, profit = min(price[i], C) - best buy in window [i-dMax, i-dMin].
- Example:
  - Input: prices `[7,2,5,1,9], dMin=1, dMax=3, C=6`
  - Output: `5` (buy at 1 on day3, sell at min(9,6)=6 on day4)

## 11) Leaky Roof Reinforcement
- Slug: leaky-roof-reinforcement
- Difficulty: Medium
- Problem: Given roof heights, you can add planks on top of any positions (increase height) so that water will not spill off either end when raining (heights become non-decreasing from left to peak and non-increasing to right). Find the minimum total plank height to add to achieve a single-peak non-leaking profile; peak can be any index.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= height[i] <= 10^9`.
- Hint: Precompute non-decreasing prefix maxima and suffix maxima; for each peak, cost = sum(maxLeft[i],maxRight[i]) - current heights; take minimum.
- Example:
  - Input: `[4,1,3,1,5]`
  - Output: `7`

## 12) Longest Zero-Sum Even Length
- Slug: longest-zero-sum-even
- Difficulty: Medium
- Problem: Find the maximum even length of a subarray with sum zero.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Prefix sums with hashmap of first index for each parity bucket.
- Example:
  - Input: `[1, -1, 3, -3, 2]`
  - Output: `4` (subarray indices 0..3)

## 13) Tool Frequency Top K with Recency Decay
- Slug: tool-frequency-top-k-decay
- Difficulty: Medium
- Problem: Each element appears with a timestamp. Score of value v is `sum(exp(-(now - t_i)/D))` over its occurrences (D given). Return the k values with highest decayed score; ties broken by smaller value.
- Constraints: `1 <= n <= 2 * 10^5`, timestamps non-decreasing up to 1e9, `1 <= k <= n`, `1 <= D <= 10^6`.
- Hint: Aggregate scores per value using decay formula; maintain top-k via min-heap.
- Example:
  - Input: values `[3@0,1@0,3@5,2@6,1@9]`, now=10, D=5, k=2
  - Output: `[3,1]`

## 14) Boarding Order With Fixed Ones
- Slug: boarding-order-fixed-ones
- Difficulty: Medium
- Problem: Array contains only 0s,1s,2s. All 1s are already in correct relative order and must not move. Sort the array (0s before 1s before 2s) while keeping 1s in place.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Two-pass to fill 0s from left skipping 1s, then fill 2s from right skipping 1s.
- Example:
  - Input: `[2,1,0,2,0,1]`
  - Output: `[0,1,0,1,2,2]`

## 15) Seat Gap After Removals
- Slug: seat-gap-after-removals
- Difficulty: Easy-Medium
- Problem: Seats are sorted; remove seats at given indices (by position in array, not seat number). After removals, return max gap between remaining consecutive seats.
- Constraints: `2 <= n <= 2 * 10^5`, removals list size `<= n-2`.
- Hint: Use set of indices; iterate remaining to compute gaps.
- Example:
  - Input: seats `[2,5,9,10]`, remove indices `[1]` (remove seat 5)
  - Output: `7` (gap 2->9)

## 16) Power Window With Drop
- Slug: power-window-with-drop
- Difficulty: Medium
- Problem: Given positive integers and window size `k`, find the maximum sum of any window after optionally removing one element from that window (you may also remove none). Return that maximal adjusted sum.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= k <= n`.
- Hint: Maintain window sum and track minimum element in window to consider dropping.
- Example:
  - Input: `arr=[2,1,5,3,2], k=3`
  - Output: `10` (window 5,3,2 with no drop)
