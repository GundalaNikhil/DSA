# Bitwise & Math Practice Set (16 Questions)

## 1) Odd After Bit Salt

- Slug: odd-after-bit-salt
- Difficulty: Easy
- Problem: Each array element `x` is first transformed to `x' = x XOR salt`, where `salt` is unknown but equal for all elements. In the transformed multiset, exactly one value appears an odd number of times, others appear an even number of times. Given the original array and `salt`, find that odd-occurring transformed value without explicitly building the transformed array.
- Constraints: `1 <= n <= 2 * 10^5`, `-10^9 <= a[i] <= 10^9`, `-10^9 <= salt <= 10^9`.
- Example:
  - Input: `arr=[4,1,2,1,2,4,7], salt=3`
  - Output: `4` (because transformed array XORs to 4)

## 2) Two Unique With Triple Others Under Mask

- Slug: two-unique-with-triples-mask
- Difficulty: Medium
- Problem: Every number appears exactly three times except two distinct numbers that appear once each. Also given a mask `M`; the two uniques are guaranteed to differ in at least one bit set in `M`. Find the two uniques.
- Constraints: `2 <= n <= 2 * 10^5`, `0 <= M <= 10^9`.
- Hint: Count bits mod 3 to get XOR of uniques; choose a differing bit that is also set in M to split.
- Example:
  - Input: `[5,5,5,9,9,9,3,6], M=2`
  - Output: `3 6`

## 3) Bitwise AND Skipping Multiples

- Slug: bitwise-and-skip-multiples
- Difficulty: Medium
- Problem: Given `L, R, m`, compute the bitwise AND of all numbers in `[L,R]` that are NOT divisible by `m`. If no numbers remain, return `-1`.
- Constraints: `0 <= L <= R <= 10^12`, `1 <= m <= 10^6`.
- Hint: Identify contiguous spans of allowed numbers; AND short-circuits to 0 if spans cross powers of two boundaries.
- Example:
  - Input: `L=10, R=15, m=3`
  - Output: `8` (numbers 10,11,13,14,15 AND to 8)

## 4) Pairwise XOR in Band With Index Parity

- Slug: pairwise-xor-band-index-parity
- Difficulty: Medium
- Problem: Given array `a` and integers `L, U`, count pairs `(i,j)` with `i<j` and `(i+j)` even such that `L <= (a[i] XOR a[j]) <= U`.
- Constraints: `1 <= n <= 10^5`, `0 <= a[i] <= 10^9`, `0 <= L <= U <= 10^9`.
- Hint: Maintain two separate bitwise tries (even-sum parity vs odd-sum parity index pairs) as you sweep; query counts in range [L,U] using two bound queries.
- Example:
  - Input: `a=[2,3,1,7], L=1, U=4`
  - Output: `3` (pairs (0,1):1, (0,2):3, (1,3):4)

## 5) Max Subarray XOR With Start

- Slug: max-subarray-xor-with-start
- Difficulty: Medium
- Problem: Given array and index `s`, find maximum XOR of any subarray that starts at index `s`.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= a[i] <= 10^9`.
- Hint: Prefix XORs with trie for suffixes from s.
- Example:
  - Input: `a=[3,8,2,6], s=1`
  - Output: `14` (subarray [8,2,6])

## 6) Minimal Bits to Flip Range

- Slug: minimal-bits-flip-range
- Difficulty: Medium
- Problem: Find smallest `m` such that flipping the lowest `m` bits of `x` turns it into `y` (i.e., `x xor y` has all 1s only in lower m bits). If impossible, return -1.
- Constraints: `0 <= x,y <= 10^12`.
- Example:
  - Input: `x=10 (1010)`, `y=5 (0101)`
  - Output: `4`

## 7) Count Set Bits Of Indexed XOR

- Slug: count-set-bits-indexed-xor
- Difficulty: Medium
- Problem: Compute the total set bits of the sequence `b[i] = i XOR a[i]` for `i` from `0` to `n-1`.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= a[i] <= 10^9`.
- Hint: Process bits independently using counts of set bits in indices; total set bits at bit `k` equals `ones_idx(k) * zeros_a(k) + zeros_idx(k) * ones_a(k)`.
- Example:
  - Input: `a=[0,2]`
  - Output: `2` (b = [0 XOR0=0, 1 XOR2=3], popcounts 0 + 2 = 2)

## 8) Maximize OR With K Picks

- Slug: maximize-or-k-picks
- Difficulty: Medium
- Problem: Choose exactly `k` elements to maximize bitwise OR of the chosen set.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= k <= n`.
- Hint: Greedy by bits from high to low; check if enough elements share a bit.
- Example:
  - Input: `a=[1,2,4], k=2`
  - Output: `6`

## 9) Smallest Absent XOR

- Slug: smallest-absent-xor
- Difficulty: Medium
- Problem: Given `a`, find the smallest non-negative integer `x` such that no pair `(i,j)` has `a[i] XOR a[j] == x`.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= a[i] <= 10^9`.
- Hint: Build XOR basis; reachable XORs up to 2^basis_size; find mex.
- Example:
  - Input: `a=[1,2,3]`
  - Output: `4`

## 10) Subset AND Equals X

- Slug: subset-and-equals-x
- Difficulty: Medium
- Problem: Count non-empty subsets whose bitwise AND equals exactly `X`.
- Constraints: `1 <= n <= 20`, `0 <= a[i], X <= 10^6`.
- Hint: Backtrack with pruning on bits; or DP over masks for small n.
- Example:
  - Input: `a=[6,3,2], X=2`
  - Output: `2` (subsets [6,2] and [2])

## 11) Toggle Ranges Minimum Flips

- Slug: toggle-ranges-min-flips
- Difficulty: Medium
- Problem: You can flip all bits in any chosen subarray (0→1,1→0). Find minimum number of flips to convert binary array `A` into `B`.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Compare A and B; count runs of mismatch.
- Example:
  - Input: `A=[0,1,1,0], B=[1,0,1,0]`
  - Output: `2`

## 12) Distinct Subarray XORs

- Slug: distinct-subarray-xors
- Difficulty: Medium
- Problem: Compute how many distinct XOR results appear among all subarrays.
- Constraints: `1 <= n <= 10^4`, `0 <= a[i] <= 10^9`.
- Hint: Trie of prefix XORs; count unique XORs via set of results per prefix incremental.
- Example:
  - Input: `a=[1,2,3]`
  - Output: `6`

## 13) Minimize Max Pair XOR

- Slug: minimize-max-pair-xor
- Difficulty: Medium
- Problem: Pair up all elements (n even) to minimize the maximum XOR among all pairs. Return that minimal possible maximum.
- Constraints: `2 <= n <= 16`.
- Hint: DP over masks with bitwise tries or brute force with pruning; n small.
- Example:
  - Input: `[1,2,3,4]`
  - Output: `3`

## 14) Bitwise Palindromes With Balanced Ones

- Slug: bitwise-palindromes-balanced-ones
- Difficulty: Medium
- Problem: Count numbers in `[L,R]` whose binary representation is a palindrome AND whose number of `1` bits is even.
- Constraints: `0 <= L <= R <= 10^12`.
- Hint: Generate palindromes by length and mirror construction; track popcount while generating to keep only even-weight numbers.
- Example:
  - Input: `L=5, R=12`
  - Output: `2` (5 -> 101 has two 1s; 9 -> 1001 has two 1s)

## 15) Swap Adjacent 2-Bit Blocks

- Slug: swap-adjacent-2bit-blocks
- Difficulty: Medium
- Problem: Treat the 32-bit representation of `x` as 2-bit blocks: swap each pair of adjacent blocks (bits 0-1 with 2-3, 4-5 with 6-7, etc.). Return the resulting integer.
- Constraints: `0 <= x <= 10^9`, assume unsigned 32-bit operations.
- Example:
  - Input: `x=13 (0000...1101b)` (bits: 01 11 -> swapped to 11 01 = 13? use clearer)
  - Input: `x=6 (0110b)` -> blocks `01|10` -> swap -> `10|01` = 9

## 16) Max Bitwise OR Subarray <= K

- Slug: max-or-subarray-leq-k
- Difficulty: Medium
- Problem: Find the maximum length of a subarray whose bitwise OR is <= `K`.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= a[i], K <= 10^9`.
- Hint: Sliding window maintaining bit counts; shrink when OR exceeds K.
- Example:
  - Input: `a=[1,2,4,1], K=7`
  - Output: `4`
