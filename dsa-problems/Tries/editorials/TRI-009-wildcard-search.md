---
problem_id: TRI_WILDCARD_SEARCH__5672
display_id: TRI-009
slug: wildcard-search
title: "Wildcard Search"
difficulty: Medium
difficulty_score: 52
topics:
  - Trie
  - String
  - Recursion
  - Backtracking
tags:
  - trie
  - pattern-matching
  - wildcards
  - dfs
premium: true
subscription_tier: basic
---

# TRI-009: Wildcard Search

## 📋 Problem Summary

Implement a search function on a trie that supports wildcard patterns with `?` (matches any single character) and `*` (matches any sequence of characters, including empty).

## 🌍 Real-World Scenario

**Unix/Linux File System Search**

Imagine you're implementing the `find` command for a Unix-like operating system. Users need to search for files using wildcard patterns like:

- `*.txt` - all text files
- `file?.log` - file1.log, file2.log, etc.
- `test*data` - testdata, test_user_data, test123data, etc.

Your file system stores millions of file paths in a trie for fast lookups. When users enter a wildcard pattern, you need to efficiently find all matching files without scanning the entire filesystem.

**Example Use Case:**

A developer searches their project with pattern `co*e`:

- Matches: "code", "coder", "codec", "coffee", "complete"
- Doesn't match: "car", "cat", "core" (no 'e' at end)

**Why This Problem Matters:**

- **Developer Tools**: IDEs use wildcard search for "Find in Files" features
- **Database Queries**: SQL LIKE operator (`%` similar to `*`)
- **Log Analysis**: Search log files with patterns like `error-*-2024`
- **Email Filters**: Gmail uses wildcards in filter rules
- **Security**: Firewall rules use wildcard patterns for URL/domain matching

**Industry Applications:**

1. **Git**: `.gitignore` files use wildcards to exclude files
2. **Docker**: `.dockerignore` patterns for build context
3. **Cloud Storage**: S3, Google Cloud use wildcards for bulk operations
4. **DNS**: Wildcard DNS records (`*.example.com`)
5. **RegEx Engines**: Simplified pattern matching

**Performance Impact:**

- Without trie: O(n × m) to check all n files against pattern of length m
- With trie + DFS: O(total nodes visited) - prunes non-matching branches early
- For 1M files with pattern `te*`: Visits only ~1000 nodes instead of 1M comparisons!

![Real-World Application](../images/TRI-009/real-world-scenario.png)

## Detailed Explanation

This problem extends basic trie search with two wildcards:

1. **`?` (Question Mark)**: Matches exactly one character, any character
2. **`*` (Asterisk)**: Matches zero or more characters, any characters

**Key Challenges:**

- `?` is straightforward: at that position, try all children nodes
- `*` is complex: can match 0, 1, 2, ... many characters
  - Need to recursively try all possibilities: match 0 chars, 1 char, 2 chars, etc.
  - This creates branching in search space → use DFS/backtracking

**Example Walkthrough:**

Trie contains: `["code", "coder", "codec"]`
Pattern: `"co*e"`

**Wildcard Matching:**

```
Trie structure:
Root
  |
  c
  |
  o
  |
  d
  |
  e (end: "code") ✓
  |
  +-- r (end: "coder")
  |
  +-- c (end: "codec")

Pattern: "co*e"
         ||^^
         |└─ * matches 0+ characters
         └── Fixed prefix "co"

Matching process:
Step 1: c ✓ → node 'c'
Step 2: o ✓ → node 'o'
Step 3: * → Try matching 0+ characters before 'e'

  Branch 1: * = "" (0 chars)
    └─ Look for 'e' from 'o' → No direct child ✗

  Branch 2: * = "d" (1 char)
    └─ 'o' → 'd' ✓ → Look for 'e' → Found! ✓
       └─ "code" matches! ✓

  Branch 3: * = "de" (2 chars)
    └─ 'o' → 'd' → 'e' ✓ → Look for 'e' → No child ✗

  Branch 4: * = "dec" (3 chars)
    └─ 'o' → 'd' → 'e' → 'c' ✓ → Look for 'e' → No child ✗

Result: TRUE (found "code")
```

Search process:

1. Match 'c': Move to 'c' node ✓
2. Match 'o': Move to 'o' node ✓
3. Match '\*': This can match 0+ characters before 'e'
   - Try matching 0 chars: Look for 'e' immediately → no child 'e' ✗
   - Try matching 1 char ('d'): Move to 'd', then look for 'e' → found! ✓
     - "code" matches!
   - Try matching 2 chars ('de'): Move to 'd'→'e', then look for 'e' → no child 'e' ✗
   - Try matching 3 chars ('dec'): Move to 'd'→'e'→'c', then look for 'e' → no child 'e' ✗
   - Try matching 3 chars ('der'): Move to 'd'→'e'→'r', then look for 'e' → no child 'e' ✗

Result: "code" matches the pattern

## Naive Approach

**Intuition:**

For each word in the trie, extract it and check if it matches the wildcard pattern using standard string matching.

**Algorithm:**

1. DFS through trie to collect all words
2. For each word, check if it matches the pattern:
   - Use dynamic programming or recursive matching
   - Handle `?` and `*` wildcards
3. Return true if any word matches

**Time Complexity:** O(n × m²) where n = total characters in trie, m = pattern length

- Extracting all words: O(n)
- Checking each word against pattern: O(m²) per word (DP or recursion)

**Space Complexity:** O(n) to store all words

**Limitations:**

- **Inefficient**: Extracts ALL words even if pattern only matches a few
- **No Pruning**: Doesn't leverage trie structure to skip impossible branches
- **Memory Intensive**: Stores all words in memory

## Optimal Approach

**Key Insight:**

Perform DFS directly on the trie while matching the pattern character by character. When encountering wildcards, branch the search recursively. This allows early termination of branches that can't possibly match.

**Algorithm:**

```
function search(node, pattern, patternIndex):
    // Base case: reached end of pattern
    if patternIndex == pattern.length:
        return node.isEndOfWord

    char = pattern[patternIndex]

    if char == '?':
        // Try all children
        for each child in node.children:
            if search(child, pattern, patternIndex + 1):
                return true
        return false

    else if char == '*':
        // Try matching 0 characters (skip *)
        if search(node, pattern, patternIndex + 1):
            return true

        // Try matching 1+ characters (consume children then retry *)
        for each child in node.children:
            if search(child, pattern, patternIndex):  // Keep * active
                return true
        return false

    else:
        // Regular character
        if char not in node.children:
            return false
        return search(node.children[char], pattern, patternIndex + 1)
```

**Time Complexity:** O(N) worst case, where N = total nodes in trie

- In worst case with pattern `*`, we might visit all nodes
- In practice, much better due to pruning

**Space Complexity:** O(h × p) where h = trie height, p = pattern length

- Recursion depth is at most h (trie height)
- Each level stores pattern position

**Why This Is Optimal:**

- **Pruning**: Skips entire subtrees that can't match
- **Lazy Evaluation**: Only explores paths that might match
- **Trie Structure**: Leverages prefix sharing to avoid redundant checks
- **Example**: Pattern `"xyz*"` on trie with no words starting with "xyz" returns false after checking just 2-3 nodes, not all words!

**Handling `*` Correctly:**

The key insight for `*`:

1. First try matching 0 characters (move pattern forward, stay at same node)
2. Then try matching 1+ characters (consume one child, keep `*` active in pattern)
3. Recursive call with same pattern index allows `*` to match multiple characters

![Algorithm Visualization](../images/TRI-009/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


### Common Mistakes to Avoid

1. **Incorrect `*` Handling**

   - **Issue**: Only trying to match 0 characters with `*`
   - ❌ Wrong: `if (*) then dfs(node, pattern, index+1)`
   - ✅ Correct: Try both 0 chars AND 1+ chars with recursion

2. **Not Keeping `*` Active**

   - **Issue**: When matching 1+ chars with `*`, incrementing pattern index
   - ❌ Wrong: `dfs(child, pattern, index+1)` when consuming char for `*`
   - ✅ Correct: `dfs(child, pattern, index)` to keep `*` active

3. **Forgetting Base Case**

   - **Issue**: Not checking if pattern is fully consumed
   - ❌ Wrong: Only checking node.isEnd without index check
   - ✅ Correct: `if (index == pattern.length) return node.isEnd`

4. **Not Checking isEnd at Pattern End**

   - **Issue**: Returning true even if we're not at a word boundary
   - ❌ Wrong: `if (index == pattern.length) return true`
   - ✅ Correct: `if (index == pattern.length) return node.isEnd`

## Related Concepts

- **Trie Data Structure**: Foundation for efficient pattern matching
- **Depth-First Search (DFS)**: Explores all possible matches
- **Backtracking**: Trying multiple paths when encountering wildcards
- **Regular Expressions**: More powerful pattern matching (wildcards are simplified regex)
- **Glob Patterns**: File system wildcard matching


## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= |pattern| <= 30` (pattern length)
- Words contain only lowercase English letters
- Pattern contains lowercase letters, `?`, and `*`