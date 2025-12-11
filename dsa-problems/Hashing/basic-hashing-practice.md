# Original Hashing & String Algorithms Practice Set (16 Questions)

## 1) Polynomial Hash of Prefixes
- Slug: polynomial-hash-prefixes
- Difficulty: Easy
- Problem: Compute polynomial rolling hash for all prefixes of a lowercase string with base `B` and mod `M`. Output the hash array.
- Constraints: `1 <= |s| <= 2 * 10^5`, `1 <= B <= 1e9+6`, `1 <= M <= 1e9+7`.
- Example:
  - Input: `s="abc", B=911382323, M=1_000_000_007`
  - Output: `[97, 97*B+98 mod M, (prev*B+99) mod M]`

## 2) Substring Equality Queries
- Slug: substring-equality-queries
- Difficulty: Medium
- Problem: Given string `s` and many queries `(l1,r1,l2,r2)`, check if substrings are equal using hashing.
- Constraints: `1 <= |s| <= 2 * 10^5`, `1 <= q <= 2 * 10^5`.
- Hint: Precompute forward and reverse hashes; double hash to reduce collision.
- Example:
  - Input: `s="ababa"`, query (0,1) vs (2,3)
  - Output: `true`

## 3) Longest Common Substring of Two Strings
- Slug: lcs-hash-two-strings
- Difficulty: Medium
- Problem: Given strings `a` and `b`, find the length of their longest common substring via binary search + hashing.
- Constraints: `1 <= |a|,|b| <= 10^5`.
- Example:
  - Input: `a="abcde", b="cdef"`
  - Output: `3`

## 4) Palindrome Substring Queries
- Slug: palindrome-substring-queries
- Difficulty: Medium
- Problem: Answer queries whether `s[l..r]` is a palindrome using hash comparisons.
- Constraints: `1 <= |s| <= 2 * 10^5`, `q <= 2 * 10^5`.
- Example:
  - Input: `s="abccba"`, query (1,4)
  - Output: `false`

## 5) Count Distinct Substrings
- Slug: count-distinct-substrings-hash
- Difficulty: Medium
- Problem: Count distinct substrings using hash multiset or suffix automaton; return the count.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"aaa"`
  - Output: `3`

## 6) Minimal Rotation via Hash Compare
- Slug: minimal-rotation-hash
- Difficulty: Medium
- Problem: Find lexicographically smallest rotation of `s` using hashing and binary lifting comparisons.
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Example:
  - Input: `"bba"`
  - Output: `"abb"`

## 7) Detect Period of String
- Slug: detect-period-string
- Difficulty: Medium
- Problem: Determine the smallest period `p` of string `s` (smallest p such that s is p repeated). Use hashes for O(n log n).
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Example:
  - Input: `"ababab"`
  - Output: `2`

## 8) Maximum Repeated Block Length
- Slug: max-repeated-block-length
- Difficulty: Medium
- Problem: Find the longest length `L` such that there exist two non-overlapping substrings of length `L` that are equal.
- Constraints: `1 <= |s| <= 10^5`.
- Hint: Binary search length, check equality via hashes with gap constraint.
- Example:
  - Input: `"banana"`
  - Output: `3` ("ana" repeats non-overlapping as positions 1-3 and 3-5 overlap; longest non-overlap is "ban"/"ana" length 3? better example "abcabc" -> 3)

## 9) Substring Hash Under Edits
- Slug: substring-hash-under-edits
- Difficulty: Medium
- Problem: Support point updates to `s` (change one character) and queries for hash of substring [l,r].
- Constraints: `1 <= |s|, q <= 2 * 10^5`.
- Hint: Fenwick/segment tree storing hashed values with powers.
- Example:
  - Input: `s="abc"`, update pos1 to 'x', query hash(0,2)
  - Output: hash of "axc"

## 10) Two-String Concatenation Equal Check
- Slug: two-string-concat-equal
- Difficulty: Medium
- Problem: Given strings `a,b,c,d`, determine if `a+b == c+d` without explicit concatenation, using hashes.
- Constraints: lengths <= 10^5.
- Example:
  - Input: `a="ab", b="cd", c="a", d="bcd"`
  - Output: `true`

## 11) Rolling Hash Collision Finder
- Slug: rolling-hash-collision
- Difficulty: Medium
- Problem: Given base B, modulus M, and length L, find two different strings of length L that collide under the polynomial hash. Return any pair.
- Constraints: `1 <= L <= 8`, `1 <= M <= 1e9+7`.
- Hint: Birthday search/backtracking.
- Example:
  - Input: `B=3, M=7, L=3`
  - Output: e.g., "aaa" and "aba" (if collide; compute to ensure collision)

## 12) Subarray Hash Equality (Integers)
- Slug: subarray-hash-equality
- Difficulty: Medium
- Problem: Treat integer array as string; build rolling hash to support equality checks between subarrays.
- Constraints: `1 <= n <= 2 * 10^5`, `|a[i]| <= 10^9`.
- Example:
  - Input: `a=[1,2,1,2]`, query (0,1) vs (2,3)
  - Output: `true`

## 13) 2D Rolling Hash for Matrix Match
- Slug: 2d-rolling-hash
- Difficulty: Medium
- Problem: Given matrix `A` and smaller matrix `B`, determine if `B` appears in `A` as a submatrix using 2D rolling hash.
- Constraints: `1 <= n,m <= 1000`.
- Example:
  - Input: A 3x3 with rows [1 2 3; 4 5 6; 7 8 9], B 2x2 [5 6; 8 9]
  - Output: true

## 14) Longest Palindromic Prefix After One Append
- Slug: longest-pal-prefix-after-append
- Difficulty: Medium
- Problem: Given string `s` and char `c`, append `c` to end; find length of longest prefix of new string that is also a suffix and is a palindrome.
- Constraints: `1 <= |s| <= 10^5`.
- Hint: Use rolling hash forward/backward to test borders.
- Example:
  - Input: `s="abac", c='a'`
  - Output: `3` ("aba")

## 15) Count Pairs with Equal Hash Mod Two Mods
- Slug: count-pairs-equal-double-hash
- Difficulty: Medium
- Problem: Count pairs of substrings of fixed length L that have equal hash under two different moduli (assume negligible collision). Return the count.
- Constraints: `1 <= |s| <= 10^5`, `1 <= L <= |s|`.
- Example:
  - Input: `s="aaaa", L=2`
  - Output: `3` (substrings at (0,1),(1,2),(2,3))

## 16) Hash-Based Anagram Indexing
- Slug: hash-anagram-indexing
- Difficulty: Medium
- Problem: Group words that are anagrams using signature hashing (frequency vector hash). Return number of groups.
- Constraints: `1 <= n <= 10^5`, word length <= 30.
- Example:
  - Input: ["eat","tea","tan","ate","nat","bat"]
  - Output: 3
