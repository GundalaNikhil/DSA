# Original Classic String Algorithms Practice Set (16 Questions)

## 1) Prefix Function (KMP) Construction

- Slug: kmp-prefix-function
- Difficulty: Easy
- Problem: Compute prefix function (pi array) for a string; return the array.
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Example:
  - Input: `"ababa"`
  - Output: `[0,0,1,2,3]`

## 2) Pattern Search With KMP

- Slug: pattern-search-kmp
- Difficulty: Easy-Medium
- Problem: Find all occurrences of pattern `p` in text `t` using KMP.
- Constraints: `1 <= |p|,|t| <= 2 * 10^5`.
- Example:
  - Input: `p="aba", t="ababa"`
  - Output: `[0,2]`

## 3) Z-Function Construction

- Slug: z-function
- Difficulty: Easy
- Problem: Compute Z-array for a string.
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Example:
  - Input: `"aabxaabx"`
  - Output: `[8,1,0,0,4,1,0,0]`

## 4) Pattern Search With Z-Function

- Slug: pattern-search-z
- Difficulty: Easy-Medium
- Problem: Using Z on `p + # + t`, find all occurrences of pattern.
- Constraints: `1 <= |p|,|t| <= 2 * 10^5`.
- Example:
  - Input: `p="aa", t="aaa"`
  - Output: `[0,1]`

## 5) Suffix Array (Doubling) Construction

- Slug: suffix-array-doubling
- Difficulty: Medium
- Problem: Build suffix array of string using O(n log n) doubling; return array of starting indices.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"cababa"`
  - Output: `[5,3,1,4,2,0]`

## 6) LCP Array (Kasai)

- Slug: lcp-array-kasai
- Difficulty: Medium
- Problem: Given string and suffix array, compute LCP array.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"cababa"`, suffix array `[5,3,1,4,2,0]`
  - Output: `[1,3,0,2,0]`

## 7) Longest Repeated Substring via SA/LCP

- Slug: longest-repeated-substring-sa
- Difficulty: Medium
- Problem: Using SA and LCP, find longest substring appearing at least twice.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"cababa"`
  - Output: `"aba"`

## 8) Distinct Substrings Count via SA/LCP

- Slug: distinct-substrings-sa
- Difficulty: Medium
- Problem: Count distinct substrings using SA/LCP: n(n+1)/2 - sum(LCP).
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"aaa"`
  - Output: `3`

## 9) Lexicographically Minimal Rotation (SA)

- Slug: minimal-rotation-sa
- Difficulty: Medium
- Problem: Find minimal rotation using suffix array on s+s; return rotation index.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"bba"`
  - Output: `1` (rotation `"bab"`? minimal is `"abb"` starting at 2; output index 2)

## 10) Longest Common Prefix of Two Suffixes

- Slug: lcp-two-suffixes
- Difficulty: Medium
- Problem: Preprocess RMQ on LCP to answer LCP of suffixes at i and j in O(1).
- Constraints: `1 <= |s| <= 10^5`, queries <= 10^5.
- Example:
  - Input: `"banana"`, query i=1, j=3
  - Output: `1`

## 11) Longest Common Substring of Two Strings (SA)

- Slug: lcs-two-strings-sa
- Difficulty: Medium
- Problem: Build SA of s1 + '#' + s2; find max LCP between suffixes from different strings.
- Constraints: `1 <= |s1|,|s2| <= 10^5`.
- Example:
  - Input: `"abcd", "bc"`
  - Output: `2`

## 12) Number of Different Substrings of Two Strings

- Slug: diff-substrings-two-strings
- Difficulty: Medium
- Problem: Count substrings present in s1 but not in s2 using SA/LCP on concat.
- Constraints: lengths <= 1e5.
- Example:
  - Input: s1="ab", s2="b"
  - Output: 2 (substrings "a","ab")

## 13) Palindromic Tree (Eertree) Construction

- Slug: palindromic-tree-eertree
- Difficulty: Hard
- Problem: Build eertree for string and output number of distinct palindromic substrings.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: "aba"
  - Output: 3

## 14) Longest Palindromic Substring With One Wildcard

- Slug: longest-palindrome-one-wildcard
- Difficulty: Medium
- Problem: String may contain a single wildcard `?` that can match any one character. Find the longest substring that can become a palindrome by choosing a replacement for `?` (if present) without moving it.
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Hint: Adapt Manacher by allowing one mismatch consumed by the wildcard; or expand centers tracking wildcard usage.
- Example:
  - Input: "ab?ba"
  - Output: "ab?ba" (replace ? with 'c' to form palindrome)

## 15) Aho-Corasick With Cooldown Scoring

- Slug: aho-corasick-cooldown-scoring
- Difficulty: Medium
- Problem: Each pattern `p_i` has a score `w_i`. When you scan text `T`, you may choose a subset of matched occurrences so that after choosing a match ending at position `r`, you must skip the next `G` characters (no chosen match may start in `(r, r+G]`). Find the maximum total score you can collect.
- Constraints: `1 <= |T| <= 2 * 10^5`; total pattern length <= `2 * 10^5`; `0 <= w_i <= 10^6`; `0 <= G <= 1000`.
- Hint: Use Aho-Corasick to list all occurrences (end index, length, weight). Then sort by end position and run DP with binary search over the next allowed start (`r+G+1`) to pick non-overlapping matches respecting the cooldown.
- Example:
  - Input: patterns `[("ab",5),("b",2)]`, `G=1`, text `"abb"`
  - Occurrences: "ab" at [1,2] score 5; "b" at [2,2] score 2; "b" at [3,3] score 2.
  - Output: `5` (take "ab"; cooldown blocks starting at 3, so best total is 5)

## 16) Suffix Automaton Substring Queries

- Slug: suffix-automaton-queries
- Difficulty: Medium
- Problem: Build SAM for string; answer if a query string is a substring in O(m), and count occurrences by endpos size.
- Constraints: `1 <= |s| <= 10^5`, queries <= 10^5.
- Example:
  - Input: s="ababa", queries ["aba","baa"]
  - Output: [true,false]
