# Original Strings & Hashing Practice Set (16 Questions)

## 1) Campus Badge Normalize

- Slug: campus-badge-normalize
- Difficulty: Easy
- Problem: Given a string, lower-case it and collapse any sequence of non-alphanumeric characters into a single hyphen; trim leading/trailing hyphens.
- Constraints: `1 <= |s| <= 10^5`.
- Hint: Single pass building output.
- Example:
  - Input: `"Hello__World!!"`
  - Output: `"hello-world"`

## 2) Lab Code Palindrome After One Rotate

- Slug: lab-code-palindrome-rotate
- Difficulty: Easy-Medium
- Problem: Determine if some rotation of the string can form a palindrome. Characters are lowercase letters.
- Constraints: `1 <= |s| <= 10^5`.
- Hint: A rotation does not change character counts; check palindromic feasibility (at most one odd count).
- Example:
  - Input: `"aab"`
  - Output: `true`

## 3) Smallest Missing Substring

- Slug: smallest-missing-substring
- Difficulty: Medium
- Problem: Find the lexicographically smallest lowercase string of length `k` that does not appear as a substring of `s`. If all length-k strings exist, return empty.
- Constraints: `1 <= |s| <= 10^5`, `1 <= k <= 5`.
- Hint: Use rolling hash or set of substrings; iterate candidates in lexicographic order via DFS until missing found.
- Example:
  - Input: `s="ababa", k=2`
  - Output: `"aa"`

## 4) Alternating Vowel-Consonant Substring

- Slug: alternating-vowel-consonant-substring
- Difficulty: Medium
- Problem: Find the longest substring where vowels and consonants strictly alternate (treat y as consonant). Return length and one such substring.
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Hint: Sliding window resetting on violation.
- Example:
  - Input: `"codeforces"`
  - Output: `5, "odefo"`

## 5) Equal Distinct Split

- Slug: equal-distinct-split
- Difficulty: Medium
- Problem: Count split points where left and right substrings have the same number of distinct characters.
- Constraints: `1 <= |s| <= 2 * 10^5`.
- Hint: Precompute suffix distinct counts; scan left.
- Example:
  - Input: `"ababa"`
  - Output: `2` (splits after indices 1 and 3)

## 6) Minimal Unique Rotation

- Slug: minimal-unique-rotation
- Difficulty: Medium
- Problem: Given a string, find its lexicographically smallest rotation that is NOT equal to the original string; if all rotations equal (all chars same), return original.
- Constraints: `1 <= |s| <= 10^5`.
- Hint: Booth’s algorithm to find minimal rotation; then if it equals original, no smaller distinct rotation exists.
- Example:
  - Input: `"bba"`
  - Output: `"abb"`

## 7) Log Compression With Window

- Slug: log-compression-window
- Difficulty: Medium
- Problem: Compress string by replacing any run of a character of length >= `w` with `char` + count; runs shorter than `w` stay as-is. Return compressed string.
- Constraints: `1 <= |s| <= 2 * 10^5`, `1 <= w <= 10^5`.
- Example:
  - Input: `s="aaabbbbcc", w=3`
  - Output: `"a3b4cc"`

## 8) K-Mismatch Anagram Substrings

- Slug: k-mismatch-anagram-substrings
- Difficulty: Medium
- Problem: Count substrings of length `m` in `s` that become an anagram of pattern `p` after at most `k` character substitutions.
- Constraints: `1 <= |s| <= 10^5`, `1 <= m <= |s| <= 10^5`, `m=|p|`, `0 <= k <= m`.
- Hint: Sliding window with frequency diff; mismatch cost is sum of positive diffs divided by 2.
- Example:
  - Input: `s="abxcab", p="aabc", k=1`
  - Output: `3`

## 9) Minimal Removal for Unique Prefixes

- Slug: minimal-removal-unique-prefixes
- Difficulty: Medium
- Problem: Given `n` lowercase strings, remove the fewest total characters (you may delete chars from ends of any strings) so that all resulting strings have distinct prefixes of length `L` (given). Return the minimal total deletions.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= L <= 20`, total length <= `2 * 10^5`.
- Hint: Build a trie; when conflicts at depth L, delete from shorter tails to adjust prefixes.
- Example:
  - Input: `L=2`, strings `["ab","ac","ad"]`
  - Output: `0` (already distinct prefixes)

## 10) Balanced Brackets With Limited Skips

- Slug: balanced-brackets-limited-skips
- Difficulty: Medium
- Problem: String consists of '(' and ')' and a limited number `k` of skip tokens you may insert anywhere (each skip can remove one parenthesis). Decide if you can make the string balanced using at most `k` skips.
- Constraints: `1 <= |s| <= 2 * 10^5`, `0 <= k <= |s|`.
- Hint: Greedy balance scan; when balance drops below 0, consume a skip; at end, remaining balance must be <= skips left.
- Example:
  - Input: `"())("`, `k=2`
  - Output: `true`

## 11) Longest Chunked Decomposition (Bounded)

- Slug: longest-chunked-bounded
- Difficulty: Medium
- Problem: Split string into the maximum number of chunks where the i-th chunk from start equals i-th chunk from end. Chunks must have length <= `L`.
- Constraints: `1 <= |s| <= 10^5`, `1 <= L <= |s|`.
- Hint: Two-pointer building chunks; reset when match found and length within bound.
- Example:
  - Input: `s="abcabc"`, L=3
  - Output: `4` (chunks ["a","b","c","abc"])

## 12) Distinct Subsequence Count with Character Limit

- Slug: distinct-subsequence-char-limit
- Difficulty: Medium
- Problem: Count distinct subsequences of `s` where each character appears at most `maxFreq` times in the subsequence. Return count modulo `MOD`. Empty subsequence counts.
- Constraints: `1 <= |s| <= 10^5`, `1 <= maxFreq <= 10`, prime `MOD <= 10^9+7`.
- Hint: DP tracking last occurrence and current character frequencies in subsequence; prune branches exceeding maxFreq.
- Example:
  - Input: `s="aaa"`, maxFreq=2, MOD=1000000007
  - Output: `5` (empty, "a", "a" (2nd), "a" (3rd), "aa", "aa" (indices differ) - but "aaa" excluded due to maxFreq=2)

## 13) Run-Length Decode with Cap

- Slug: run-length-decode-cap
- Difficulty: Easy-Medium
- Problem: Decode run-length string like "a3b12" but cap any run exceeding `cap` to exactly `cap`. Return decoded string.
- Constraints: `1 <= |s| <= 10^5`, `1 <= cap <= 10^4`.
- Example:
  - Input: `s="a10b2", cap=3`
  - Output: `"aaabb"`

## 14) Shortest Covering Window for Set

- Slug: shortest-covering-window-set
- Difficulty: Medium
- Problem: Given array of strings `arr` and a set `T`, find the shortest contiguous subarray of `arr` whose set of elements covers all of `T`. Return length and one such window.
- Constraints: `1 <= |arr| <= 10^5`, `|T| <= 10^3`.
- Hint: Sliding window with frequency map for required tokens.
- Example:
  - Input: `arr=["db","aa","cc","db","aa","cc"], T={"aa","cc"}`
  - Output: `2, [aa,cc]`

## 15) Cyclic Shift Equality Classes

- Slug: cyclic-shift-equality-classes
- Difficulty: Medium
- Problem: Given `n` strings, group them into equivalence classes where two strings are equivalent if one is a cyclic shift of the other. Return the number of classes.
- Constraints: `1 <= n <= 2 * 10^5`, each string length <= 20.
- Hint: Use minimal rotation as canonical form; hash counts.
- Example:
  - Input: `["ab","ba","abc","bca","cab"]`
  - Output: `3`

## 16) Minimal Delete to Make K-Periodic

- Slug: minimal-delete-k-periodic
- Difficulty: Medium
- Problem: Delete the fewest characters so that the string becomes periodic with period exactly `k` (length of repeating block is k). Return the minimal deletions.
- Constraints: `1 <= |s| <= 10^5`, `1 <= k <= |s|`.
- Hint: For each position mod k, keep the most frequent character; deletions are total minus sum of maxima.
- Example:
  - Input: `s="abac", k=2`
  - Output: `1`
