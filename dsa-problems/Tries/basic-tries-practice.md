# Original Trie & Advanced String DS Practice Set (16 Questions)

## 1) Autocomplete Top-K
- Slug: autocomplete-top-k
- Difficulty: Easy-Medium
- Problem: Build a trie of lowercase words with frequencies. Given a prefix, return the top `k` words with highest frequency (tie by lexicographic order).
- Constraints: `1 <= total words <= 10^5`, `1 <= |word| <= 30`, `1 <= k <= 10`.
- Example:
  - Input: words `[(hello,5),(helium,3),(he,4)]`, query prefix `"he"`, k=2
  - Output: `["hello","he"]`

## 2) Longest Common Prefix of Set
- Slug: longest-common-prefix-set
- Difficulty: Easy
- Problem: Insert `n` lowercase words; return their longest common prefix (empty if none).
- Constraints: `1 <= n <= 10^5`, total length <= `2 * 10^5`.
- Example:
  - Input: `["interview","internet","internal"]`
  - Output: `"inte"`

## 3) Distinct Substrings Count via Trie
- Slug: distinct-substrings-count-trie
- Difficulty: Medium
- Problem: Count distinct substrings of a string using a suffix trie (or suffix automaton). Return the count.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"aaa"`
  - Output: `3` (a, aa, aaa)

## 4) Replace Words with Shortest Rare Prefix
- Slug: replace-words-shortest-rare-prefix
- Difficulty: Medium
- Problem: Given a dictionary of root words with rarity scores `r[root]` (lower is rarer) and a sentence, replace each word by the prefix among dictionary roots that is both a prefix of the word and has the smallest rarity; if multiple, pick the shortest; if none, leave word unchanged.
- Constraints: `1 <= dict size <= 10^5`, word length <= 30`.
- Example:
  - Input: dict roots `["cat","car"]` with rarity `{cat:1, car:2}`, sentence `"the cattle carried"`.
  - Output: `"the cat car"`

## 5) Binary Trie Min XOR Pair Under Limit
- Slug: binary-trie-min-xor-pair-limit
- Difficulty: Medium
- Problem: Given array of ints and a limit `L`, find the minimum XOR of any pair whose XOR is <= L; if no pair satisfies, return -1.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= a[i] <= 10^9`, `0 <= L <= 10^9`.
- Example:
  - Input: `[3,10,5,25], L=8`
  - Output: `6` (3 xor 5)

## 6) Lexicographic k-th String Not Present
- Slug: kth-string-not-present
- Difficulty: Medium
- Problem: Given a trie of inserted lowercase strings, find the k-th lexicographically smallest string of length up to `L` that is NOT present.
- Constraints: `1 <= inserted <= 10^5`, `1 <= L <= 6`, `1 <= k <= 10^9`.
- Hint: DFS counting missing nodes; strings can end at any depth.
- Example:
  - Input: inserted `["a","b"]`, L=2, k=1
  - Output: `"aa"` (first missing of length<=2)

## 7) Minimum Unique Prefix Lengths
- Slug: minimum-unique-prefix-lengths
- Difficulty: Medium
- Problem: For each word, find the minimum prefix length that makes it unique among all words.
- Constraints: `1 <= n <= 10^5`, total length <= `2 * 10^5`.
- Example:
  - Input: `["zebra","dog","duck","dove"]`
  - Output: `[1,2,2,2]` (z, do, du, do(v))

## 8) Dictionary Compression Size
- Slug: dictionary-compression-size
- Difficulty: Medium
- Problem: Given `n` words, compute total number of nodes in the trie (including root) needed to store them.
- Constraints: `1 <= n <= 10^5`.
- Example:
  - Input: `["a","ab","abc"]`
  - Output: `4` (root + a + b + c)

## 9) Wildcard Search
- Slug: wildcard-search
- Difficulty: Medium
- Problem: Implement search on a trie with pattern containing `?` (matches any single char) and `*` (matches any sequence of chars, including empty). Return true if any word matches.
- Constraints: `1 <= total words <= 10^5`, pattern length <= 30.
- Example:
  - Input: words `["code","coder","codec"]`, pattern `"co*e"`
  - Output: `true`

## 10) Trie-Based Spell Checker
- Slug: trie-spell-checker
- Difficulty: Medium
- Problem: Given dictionary words, for each query word, return true if dictionary contains a word at edit distance 1 (insert/delete/replace one char) from query.
- Constraints: `1 <= dict size, queries <= 10^5`, word length <= 25.
- Example:
  - Input: dict `["cat","bat"]`, query `"cats"`
  - Output: `true`

## 11) Suffix Trie Longest Repeat
- Slug: suffix-trie-longest-repeat
- Difficulty: Medium
- Problem: Build suffix trie (or suffix array alternative) to find the length of the longest repeated substring in `s`.
- Constraints: `1 <= |s| <= 10^5`.
- Example:
  - Input: `"banana"`
  - Output: `3` ("ana")

## 12) Prefix-Free Check After Inserts
- Slug: prefix-free-after-inserts
- Difficulty: Medium
- Problem: Insert phone numbers (digit strings). After each insertion, report whether the set remains prefix-free (no number is prefix of another).
- Constraints: `1 <= inserts <= 10^5`, length <= 15.
- Example:
  - Input: inserts `["91","911","912"]`
  - Output: `[true,false,false]`

## 13) Shortest Absent Binary String of Length L
- Slug: shortest-absent-binary-length-l
- Difficulty: Medium
- Problem: Given set of binary strings length exactly `L`, find lexicographically smallest binary string of length `L` not in the set; return empty if full.
- Constraints: `1 <= L <= 20`, set size <= 2^L.
- Example:
  - Input: L=2, set `{"00","01"}`
  - Output: `"10"`

## 14) Longest Word Buildable by At Least K Prefixes
- Slug: longest-word-by-k-prefixes
- Difficulty: Medium
- Problem: Find the longest word in the dictionary that has at least `k` of its prefixes (not necessarily all) present in the dictionary. Tie by lexicographically smallest. If none meets `k`, return empty.
- Constraints: `1 <= n <= 10^5`, word length <= 30, `1 <= k <= 30`.
- Example:
  - Input: `["a","ap","app","apple","apex"], k=3`
  - Output: `"apple"` (prefixes a, ap, app exist)

## 15) XOR Minimization With Trie
- Slug: xor-minimization-trie
- Difficulty: Medium
- Problem: Given array `a` and integer `X`, find subarray whose XOR with `X` is minimized; return that minimal value.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= a[i], X <= 10^9`.
- Hint: Use prefix XORs in a binary trie to query min XOR with X.
- Example:
  - Input: `a=[4,1,2], X=3`
  - Output: `0` (subarray [1,2] XOR = 3; 3 XOR 3 = 0)

## 16) Trie-Based Kth Smallest String
- Slug: trie-kth-smallest-string
- Difficulty: Medium
- Problem: Insert lowercase strings. Given `k`, return the k-th string in lexicographic order (1-indexed). If k exceeds total, return empty.
- Constraints: `1 <= n <= 10^5`, total length <= 2 * 10^5`, `1 <= k <= 10^9`.
- Example:
  - Input: words `["b","a","aa"]`, k=2
  - Output: `"aa"`
