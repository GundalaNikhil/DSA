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
  - Input: `"banana"`
  - Output: `[5,3,1,0,4,2]`

## 6) LCP Array (Kasai)
- Slug: lcp-array-kasai
- Difficulty: Medium
- Problem: Given string and suffix array, compute LCP array.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"banana"`, suffix array `[5,3,1,0,4,2]`
  - Output: `[1,3,0,0,2]`

## 7) Longest Repeated Substring via SA/LCP
- Slug: longest-repeated-substring-sa
- Difficulty: Medium
- Problem: Using SA and LCP, find longest substring appearing at least twice.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"banana"`
  - Output: `"ana"`

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

## 14) Manacher’s Longest Palindromic Substring
- Slug: manacher-longest-palindrome
- Difficulty: Medium
- Problem: Find longest palindromic substring in O(n).
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Example:
  - Input: "babad"
  - Output: "bab" or "aba"

## 15) Aho-Corasick Multi-Pattern Match
- Slug: aho-corasick-multi-pattern
- Difficulty: Medium
- Problem: Build automaton for patterns; report all pattern occurrences in text.
- Constraints: total pattern length <= 2 * 10^5.
- Example:
  - Input: patterns ["he","she","his","hers"], text "ahishers"
  - Output: matches at appropriate indices

## 16) Suffix Automaton Substring Queries
- Slug: suffix-automaton-queries
- Difficulty: Medium
- Problem: Build SAM for string; answer if a query string is a substring in O(m), and count occurrences by endpos size.
- Constraints: `1 <= |s| <= 10^5`, queries <= 10^5.
- Example:
  - Input: s="ababa", queries ["aba","baa"]
  - Output: [true,false]
