# Original Dynamic Programming Practice Set (16 Questions)

## 1) Staircase With Cracked Steps and Max Jump

- Slug: staircase-cracked-steps-maxjump
- Difficulty: Medium
- Problem: A staircase has `n` steps. You may climb 1..J steps at a time (given J), but some steps are cracked and cannot be landed on (may be jumped over). Count the number of distinct ways to reach step `n`.
- Constraints: `1 <= n <= 10^5`, `1 <= J <= 50`, cracked indices list size `<= 10^5`.
- Hint: Sliding-window sum of dp over last J non-cracked positions.
- Example:
  - Input: `n=4`, J=3, cracked=`{2}`
  - Output: `3` (paths: 0-1-3-4, 0-1-4, 0-3-4)

## 2) Capped Coin Change With Penalty

- Slug: capped-coin-change-penalty
- Difficulty: Medium
- Problem: Each denomination d[i] can be used at most c[i] times.
  Using more than floor(c[i]/2) coins of type i adds penalty p[i] to
  your total. Find minimum (coins + penalties) to form target, or -1.
- Constraints: `1 <= k <= 50`, `1 <= target <= 5000`.
- Hint: 2D DP tracking (amount, penalty state per coin type).
- Example:
  - Input: `d=[1,5], c=[4,2], p=[2,1], target=7`
  - Output: `4` (use 2×5 + 2×1 = 4 coins, no penalties)

## 3) Required Weight Knapsack

- Slug: required-weight-knapsack
- Difficulty: Medium
- Problem: Given items with `weight[i]` and `value[i]`, capacity `W`, and a required minimum total weight `R` (<= W). Maximize value while ensuring total weight >= R and <= W.
- Constraints: `1 <= n <= 200`, `1 <= W <= 5000`, `1 <= R <= W`.
- Hint: Standard 0/1 knap maximizing value; invalidate weights < R after fill.
- Example:
  - Input: `weight=[2,3,4], value=[4,5,6], W=6, R=5`
  - Output: `10` (items 1 and 2)

## 4) Exact Count Subset Sum

- Slug: exact-count-subset-sum
- Difficulty: Medium
- Problem: Determine if there exists a subset of exactly `k` elements that sums to `target`.
- Constraints: `1 <= n <= 200`, `1 <= target <= 5000`, `1 <= k <= n`.
- Hint: 2D boolean DP on (count, sum); iterate items downward.
- Example:
  - Input: `arr=[3, 1, 9, 7], target=10, k=2`
  - Output: `true` (3+7)

## 5) Keyboard Row Edit Distance with Shift Penalty

- Slug: keyboard-row-edit-distance-shift
- Difficulty: Medium
- Problem: Strings `a` and `b` consist of lowercase letters. Replace cost: 1 if letters on same keyboard row, 2 if different row but same hand (left/right), 3 otherwise. Insert/delete cost 1. Compute minimum cost to convert `a` to `b`.
- Constraints: `0 <= |a|,|b| <= 2000`.
- Example:
  - Input: `a="type"`, `b="tap"`
  - Output: `4`

## 6) Strict Jump LIS With Max Gap

- Slug: strict-jump-lis-bounded
- Difficulty: Medium
- Problem: Find the longest subsequence where each next element is at least `d` larger and at most `g` larger than the previous (d<=diff<=g). Return the length.
- Constraints: `1 <= n <= 10^5`, `-10^9 <= a[i] <= 10^9`, `0 <= d <= g <= 10^9`.
- Hint: Segment tree/Fenwick on compressed values storing best length; query range (prev+d, prev+g).
- Example:
  - Input: `a=[1,3,4,9,10], d=2, g=6`
  - Output: `3` (1,3,9 or 1,4,9)

## 7) Auditorium Max Sum With Gap Three

- Slug: auditorium-max-sum-gap-three
- Difficulty: Medium
- Problem: Pick elements to maximize sum such that any two chosen
  indices differ by at least 3 (skip at least two elements between picks).
- Constraints: `1 <= n <= 10^5`.
- Hint: `dp[i] = max(dp[i-1], dp[i-3] + a[i])`.
- Example:
  - Input: `[4, 1, 2, 9, 3]`
  - Output: `13` (indices 0 and 3: 4 + 9)

## 8) Grid Paths With Turn Limit

- Slug: grid-paths-turn-limit
- Difficulty: Medium
- Problem: Count paths from top-left to bottom-right in an `m x n` grid moving only right or down, using at most `T` turns (direction changes).
- Constraints: `1 <= m,n <= 100`, `0 <= T <= 50`.
- Hint: 3D DP on (i,j,dir,turns); start with both directions.
- Example:
  - Input: `m=2, n=3, T=1`
  - Output: `2` (RRD, DRR)

## 9) Flooded Campus Min Cost With Free Cells

- Slug: flooded-campus-min-cost-free
- Difficulty: Medium
- Problem: In a cost grid, you may choose up to `f` cells to traverse for free (cost 0). Find the minimum cost from top-left to bottom-right (right/down moves).
- Constraints: `1 <= m,n <= 200`, `0 <= cost[i][j] <= 10^4`, `0 <= f <= 10`.
- Hint: 3D DP on (i,j,freeUsed); transition with or without consuming a free cell.
- Example:
  - Input: `grid=[[5,3],[4,1]]`, `f=1`
  - Output: `4` (take (0,1) for free)

## 10) Longest Common Subsequence With Skips

- Slug: lcs-with-skips
- Difficulty: Medium
- Problem: Find the longest subsequence common to `a` and `b` if you may skip up to `s` characters from `a` for free (i.e., removing them doesn’t break order). Return the length.
- Constraints: `0 <= |a|,|b| <= 2000`, `0 <= s <= |a|`.
- Hint: DP[i][j] = max of match, skip a (using allowance), skip b.
- Example:
  - Input: `a="abcde"`, `b="ace"`, `s=1`
  - Output: `3`

## 11) Expression Target Modulo

- Slug: expression-target-modulo
- Difficulty: Medium
- Problem: Given digit string s and modulus M, insert + or - between
  digits (or concatenate to form multi-digit numbers, no leading zeros
  except 0 itself). Count expressions whose value mod M equals K.
- Constraints: `1 <= |s| <= 12`, `1 <= M <= 50`.
- Hint: DP over position and current mod; track current number being built.
- Example:
  - Input: `s="123"`, `M=5`, `K=4`
  - Output: `2` (12-3=9≡4, 1+23=24≡4)

## 12) Balanced Partition With Size Limit

- Slug: balanced-partition-size-limit
- Difficulty: Medium
- Problem: Partition array into two groups with sum difference <= `D` while minimizing the size of the larger group. Return the minimal possible larger-group size; if impossible, return -1.
- Constraints: `1 <= n <= 50`, `1 <= D <= 5000`, `|a[i]| <= 500`.
- Hint: DP over possible sum differences and counts.
- Example:
  - Input: `a=[3,1,4,2], D=1`
  - Output: `2`

## 13) Paint Fence With Switch Cost

- Slug: paint-fence-switch-cost
- Difficulty: Medium
- Problem: Paint `n` posts using `k` colors. No more than two adjacent posts may share a color, and switching colors from post `i-1` to `i` adds cost `s[i]` (given). Minimize total cost if painting cost per post is 1 regardless of color.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= 50`, `0 <= s[i] <= 10^4`.
- Hint: DP on states of last two colors; track streak length.
- Example:
  - Input: `n=3, k=2, s=[0,2,1]`
  - Output: `4` (colors A,A,B gives one switch cost 1 plus 3 paints)

## 14) Constrained Decode Ways

- Slug: constrained-decode-ways
- Difficulty: Medium
- Problem: Digit string encodes 1-26 as letters. Additionally, any digit `0` must be immediately preceded by an even digit to be valid (forming 20 only). Count decodings.
- Constraints: `1 <= |s| <= 10^5`.
- Hint: DP with validity checks; zeros restricted to “20”.
- Example:
  - Input: `"2012"`
  - Output: `2` (`20-12` and `20-1-2`)

## 15) Stock Trading With Weekly Rest and Fee

- Slug: stock-trading-weekly-rest-fee
- Difficulty: Medium
- Problem: Unlimited transactions, but after each sale you must rest until the next Monday, and each sale incurs fee `f`. Maximize profit.
- Constraints: `1 <= n <= 10^5`, `0 <= f <= 10^9`.
- Hint: DP with hold/free states keyed by day mod 7; selling transitions subtract fee and jump to next Monday.
- Example:
  - Input: week prices `[1,5,3,6,4,2,7]`, f=1
  - Output: `5`

## 16) Exams With Cooldown Gap

- Slug: exams-with-cooldown-gap
- Difficulty: Medium
- Problem: Each exam slot `i` has start, end, and score. You must leave a gap of at least `g` time units between any two chosen exams. Maximize total score.
- Constraints: `1 <= n <= 10^5`, times up to `10^9`, `0 <= g <= 10^9`.
- Hint: Sort by end; binary search latest exam ending at or before `start - g`; weighted interval DP.
- Example:
  - Input: `[(1,3,5),(4,6,6),(6,10,5)], g=1`
  - Output: `11`
