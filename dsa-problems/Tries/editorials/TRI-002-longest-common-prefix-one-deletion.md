---
problem_id: TRI_LCP_ONE_DELETE__3841
display_id: TRI-002
slug: longest-common-prefix-one-deletion
title: "Longest Common Prefix After One Deletion"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Dynamic Programming
tags:
  - trie
  - string-matching
  - prefix
premium: true
subscription_tier: basic
---

# TRI-002: Longest Common Prefix After One Deletion

## 📋 Problem Summary

Given n lowercase words, find the longest string that can become a common prefix of all words after deleting at most one character from each word at any position.

## 🌍 Real-World Scenario

**Version Control System Conflict Resolution**

Imagine you're building a smart merge tool for Git. When multiple developers work on similar feature branches, their branch names often share common patterns:

- `feature/user-authentication`
- `feature/user-authorization`
- `feature/user-interface`

Your merge tool needs to identify the core common prefix to group related branches automatically. However, typos and inconsistent naming conventions mean you might need to "forgive" one character difference per branch name.

**Real-World Applications:**

A developer accidentally typed:

- `feature/xuser-auth` (extra 'x')
- `feature/user-autz` (typo: 'z' instead of 'h')
- `feature/user-aauth` (duplicate 'a')

Your algorithm should detect that removing one character from each makes them share the prefix `"feature/user-a"`, helping automatically categorize these as related branches.

**Why This Problem Matters:**

- **DevOps Automation**: Group related CI/CD pipelines by branch prefix
- **Log Analysis**: Cluster similar error messages ignoring noise characters
- **Data Deduplication**: Find near-identical record prefixes in databases
- **API Versioning**: Detect common API endpoint patterns despite typos

![Real-World Application](../images/TRI-002/real-world-scenario.png)

## Detailed Explanation

This problem extends classic LCP (Longest Common Prefix) by allowing flexibility. For each word, we can delete at most one character at any position, making it possible to align words that are "almost" sharing a prefix.

**Example Walkthrough:**

Words: `["interview", "internet", "interval"]`

Without deletions: Common prefix is "inter" (5 chars)

With one deletion per word, we can achieve "interv":

- "interview": Already has "interv" as prefix (no deletion needed) ✓
- "internet": Delete 'n' at position 5 → "iteret", then forms "inter" but not "interv". Alternative: delete 't' at position 2 → "inernet", still doesn't work. Keep as "internet" and match up to "inter"
- "interval": Already has "interv" as prefix (no deletion needed) ✓

The key insight: Build a trie of all possible variants (original + all single-deletion variants) of each word, then find the longest prefix path where each word has at least one variant passing through. In this case, "interv" works because at least one variant of each word contains it as a prefix.

## Naive Approach

**Intuition:**

Try every possible prefix length from longest to shortest. For each candidate prefix, check if each word can match it after deleting at most one character.

**Algorithm:**

1. Find max possible prefix length = min(all word lengths)
2. For length L from max down to 0:
   - For each candidate prefix of length L:
     - Check if every word can be transformed to have this prefix by deleting ≤ 1 char
     - If yes, return this prefix
3. Return empty string if no match

**Time Complexity:** O(N × L³) where N = number of words, L = max length

- For each length L: O(L)
- For each prefix: O(26^L) possible prefixes
- Checking each word: O(L × N)

**Space Complexity:** O(L)

**Why This Works:**

- Exhaustively checks all possibilities
- Guaranteed to find the longest valid prefix

**Limitations:**

- **Exponential candidate space**: Too many possible prefixes to enumerate
- **Repeated work**: Checks same transformations multiple times
- **Impractical for long words**: Becomes infeasible beyond small inputs

## Optimal Approach

**Key Insight:**

Build a **trie of variants**: For each word, insert both the original and all single-deletion variants (at most L+1 variants per word). Then find the deepest trie node reached by at least one variant from each word.

**Variant Generation:**

```
Example: words = ["interview", "internet", "internal"]
Word 0: "interview" → variants: "interview", "nterview", "iterview", "inerview", ...
Word 1: "internet"  → variants: "internet", "nternet", "iternet", "inernet", ...
Word 2: "internal"  → variants: "internal", "nternal", "iternal", "inernal", ...

Trie with word IDs tracked:
Root
  |
  i {0,1,2}
  |
  n {0,1,2}
  |
  t {0,1,2}
  |
  e {0,1,2}
  |
  r {0,1,2}  ← All 3 words reach here (LCP = "inter")
  |
  +-- v {0}      (from "interview")
  |
  +-- n {1,2}
      |
      +-- e {1}  (from "internet")
      |
      +-- a {2}  (from "internal")

Result: "inter" (depth 5, all word IDs present)
```

**Algorithm:**

1. **Generate Variants**:

   - For each word `w`:
     - Insert `w` into trie (no deletion)
     - For each position `i` in `w`:
       - Create variant by deleting character at position `i`
       - Insert variant into trie
     - Mark each trie path with the word ID it represents

2. **DFS to Find Longest Common Prefix**:

   - Traverse trie depth-first
   - At each node, check if all N word IDs are represented
   - Track the deepest node where all words have coverage
   - Return the path (prefix) to that node

3. **Optimization**: Use bit-masking or hash sets to track which words are represented at each node

**Time Complexity:** O(N × L²)

- Generating variants: O(N × L²) (N words, L deletions each, L chars per variant)
- DFS: O(total trie nodes) = O(N × L²)

**Space Complexity:** O(N × L²) for trie storage

**Why This Is Optimal:**

- **Avoids enumeration**: Builds only relevant prefixes (those from actual word variants)
- **Single pass**: DFS checks all words simultaneously
- **Practical**: Handles realistic word lengths (L ≤ 100) efficiently

![Algorithm Visualization](../images/TRI-002/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    Set<Integer> wordIds = new HashSet<>();
}

class Solution {
    private TrieNode root = new TrieNode();
    private String longestPrefix = "";

    public String longestCommonPrefixAfterOneDeletion(String[] words) {
        int n = words.length;

        // Insert all variants into trie
        for (int wordId = 0; wordId < n; wordId++) {
            String word = words[wordId];

            // Insert original word
            insertWord(word, wordId);

            // Insert all single-deletion variants
            for (int i = 0; i < word.length(); i++) {
                String variant = word.substring(0, i) + word.substring(i + 1);
                insertWord(variant, wordId);
            }
        }

        // DFS to find longest prefix with all word IDs
        dfs(root, "", n);

        return longestPrefix;
    }

    private void insertWord(String word, int wordId) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.wordIds.add(wordId);
        }
    }

    private void dfs(TrieNode node, String prefix, int totalWords) {
        // If all words are represented at this node, update longest prefix
        if (node.wordIds.size() == totalWords) {
            if (prefix.length() > longestPrefix.length()) {
                longestPrefix = prefix;
            }
        }

        // Continue DFS
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            dfs(entry.getValue(), prefix + entry.getKey(), totalWords);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }

        Solution solution = new Solution();
        String result = solution.longestCommonPrefixAfterOneDeletion(words);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_ids = set()

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.longest_prefix = ""

    def longest_common_prefix_after_one_deletion(self, words: List[str]) -> str:
        n = len(words)

        # Insert all variants into trie
        for word_id, word in enumerate(words):
            # Insert original word
            self._insert_word(word, word_id)

            # Insert all single-deletion variants
            for i in range(len(word)):
                variant = word[:i] + word[i+1:]
                self._insert_word(variant, word_id)

        # DFS to find longest prefix with all word IDs
        self._dfs(self.root, "", n)

        return self.longest_prefix

    def _insert_word(self, word: str, word_id: int):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_ids.add(word_id)

    def _dfs(self, node: TrieNode, prefix: str, total_words: int):
        # If all words are represented at this node, update longest prefix
        if len(node.word_ids) == total_words:
            if len(prefix) > len(self.longest_prefix):
                self.longest_prefix = prefix

        # Continue DFS
        for char, child in node.children.items():
            self._dfs(child, prefix + char, total_words)

def main():
    import sys
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])
    words = input_data[1:n+1]

    solution = Solution()
    result = solution.longest_common_prefix_after_one_deletion(words)

    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    unordered_set<int> wordIds;
};

class Solution {
private:
    TrieNode* root;
    string longestPrefix;

    void insertWord(const string& word, int wordId) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->wordIds.insert(wordId);
        }
    }

    void dfs(TrieNode* node, string prefix, int totalWords) {
        // If all words are represented at this node, update longest prefix
        if (node->wordIds.size() == totalWords) {
            if (prefix.length() > longestPrefix.length()) {
                longestPrefix = prefix;
            }
        }

        // Continue DFS
        for (auto& [ch, child] : node->children) {
            dfs(child, prefix + ch, totalWords);
        }
    }

public:
    Solution() {
        root = new TrieNode();
        longestPrefix = "";
    }

    string longestCommonPrefixAfterOneDeletion(vector<string>& words) {
        int n = words.size();

        // Insert all variants into trie
        for (int wordId = 0; wordId < n; wordId++) {
            const string& word = words[wordId];

            // Insert original word
            insertWord(word, wordId);

            // Insert all single-deletion variants
            for (int i = 0; i < word.length(); i++) {
                string variant = word.substr(0, i) + word.substr(i + 1);
                insertWord(variant, wordId);
            }
        }

        // DFS to find longest prefix with all word IDs
        dfs(root, "", n);

        return longestPrefix;
    }
};

int main() {
    int n;
    cin >> n;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }

    Solution solution;
    string result = solution.longestCommonPrefixAfterOneDeletion(words);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.wordIds = new Set();
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.longestPrefix = "";
  }

  longestCommonPrefixAfterOneDeletion(words) {
    const n = words.length;

    // Insert all variants into trie
    for (let wordId = 0; wordId < n; wordId++) {
      const word = words[wordId];

      // Insert original word
      this._insertWord(word, wordId);

      // Insert all single-deletion variants
      for (let i = 0; i < word.length; i++) {
        const variant = word.slice(0, i) + word.slice(i + 1);
        this._insertWord(variant, wordId);
      }
    }

    // DFS to find longest prefix with all word IDs
    this._dfs(this.root, "", n);

    return this.longestPrefix;
  }

  _insertWord(word, wordId) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
      node.wordIds.add(wordId);
    }
  }

  _dfs(node, prefix, totalWords) {
    // If all words are represented at this node, update longest prefix
    if (node.wordIds.size === totalWords) {
      if (prefix.length > this.longestPrefix.length) {
        this.longestPrefix = prefix;
      }
    }

    // Continue DFS
    for (const [char, child] of node.children) {
      this._dfs(child, prefix + char, totalWords);
    }
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines.join(" ").split(/\s+/);

  const n = parseInt(tokens[0]);
  const words = tokens.slice(1, n + 1);

  const solution = new Solution();
  const result = solution.longestCommonPrefixAfterOneDeletion(words);

  console.log(result);
});
```

### C++ommon Mistakes to Avoid

1. **Forgetting Edge Cases**

   - **Issue**: Not handling empty words or single-character words
   - ❌ Wrong: Assuming all words have length ≥ 2
   - ✅ Correct: Check for empty strings and handle deletion creating empty variants

2. **Incorrect Variant Generation**

   - **Issue**: Generating duplicates or missing the original word
   - ❌ Wrong: Only inserting deletion variants, not the original
   - ✅ Correct: Insert original word PLUS all single-deletion variants

3. **Not Tracking Word IDs**

   - **Issue**: Only checking if trie node exists, not which words reach it
   - ❌ Wrong: Assuming node existence means all words share that prefix
   - ✅ Correct: Maintain a set of word IDs at each node to verify coverage

## Related Concepts

- **Longest Common Prefix (LCP)**: Classic problem without deletions
- **Edit Distance**: Generalized version allowing insertions, deletions, substitutions
- **Trie Data Structure**: Efficient prefix storage and retrieval
- **String Matching with Errors**: Approximate string matching algorithms
