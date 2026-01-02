---
problem_id: TRI_LONGEST_WORD_K_PREFIXES__8329
display_id: TRI-014
slug: longest-word-by-k-prefixes
title: "Longest Word Buildable by At Least K Prefixes"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - String
  - DFS
tags:
  - trie
  - prefix-matching
  - word-building
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-014: Longest Word Buildable by At Least K Prefixes

## Problem Statement

Given a dictionary of lowercase words and an integer `k`, find the longest word that has at least `k` of its prefixes present in the dictionary. If multiple words have the same maximum length, return the lexicographically smallest one. If no word meets the requirement, return an empty string.

A prefix of a word `w` is any substring `w[0...i]` where `0 <= i < len(w)-1` (excluding the word itself).

![Problem Illustration](../images/TRI-014/problem-illustration.png)

## Input Format

- First line: two integers `n` (number of words) and `k` (minimum prefix count)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return the longest word with at least `k` prefixes in the dictionary, or an empty string if none exists.

## Constraints

- `1 <= n <= 10^5` (number of words)
- `1 <= k <= 30`
- `1 <= word length <= 30`
- All words consist of lowercase English letters (a-z)
- No duplicate words in dictionary

## Example

**Input:**

```
5 3
a
ap
app
apple
apex
```

**Output:**

```
apple
```

**Explanation:**

Analyzing each word:

- "a": No prefixes → 0 < k=3 ✗
- "ap": Prefix "a" exists → 1 < k=3 ✗
- "app": Prefixes "a", "ap" exist → 2 < k=3 ✗
- "apple": Prefixes "a", "ap", "app", "appl"
  - "a" exists ✓
  - "ap" exists ✓
  - "app" exists ✓
  - "appl" doesn't exist ✗
  - Total: 3 >= k=3 ✓ (length 5)
- "apex": Prefixes "a", "ap", "ape"
  - "a" exists ✓
  - "ap" exists ✓
  - "ape" doesn't exist ✗
  - Total: 2 < k=3 ✗

Result: "apple" (longest with >= 3 prefixes)

![Example Visualization](../images/TRI-014/example-1.png)

## Notes

- A word's prefix does NOT include the word itself or the empty string
- For tie-breaking, use lexicographic order (dictionary order)
- Use a trie to efficiently check prefix existence

## Related Topics

Trie, String, Prefix Matching, Lexicographic Order

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public String longestWordWithKPrefixes(String[] words, int k) {
        return "";
    }

    private void insert(String word) {
    }

    private int countPrefixes(String word) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        String result = solution.longestWordWithKPrefixes(words, k);

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
        return 0
class Solution:
    def __init__(self):
        return 0
    def longest_word_with_k_prefixes(self, words: List[str], k: int) -> str:
        return ""
    def _insert(self, word: str):
        return 0
    def _count_prefixes(self, word: str) -> int:
        return 0
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n, k = map(int, lines[0].split())
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.longest_word_with_k_prefixes(words, k)

    print(result if result else "")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;

    void insert(const string& word) {
    }

    int countPrefixes(const string& word) {
        return 0;
    }

public:
    Solution() { root = new TrieNode(); }
        return 0;
    }
    string longestWordWithKPrefixes(vector<string>& words, int k) {
        return "";
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    cin.ignore();

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        getline(cin, words[i]);
    }

    Solution solution;
    string result = solution.longestWordWithKPrefixes(words, k);

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
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    return 0;
  }

  countPrefixes(word) {
    return 0;
  }

  longestWordWithKPrefixes(words, k) {
    return 0;
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
  const [n, k] = lines[0].split(" ").map(Number);
  const words = [];
  for (let i = 1; i <= n; i++) {
    words.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.longestWordWithKPrefixes(words, k);

  console.log(result);
});
```

