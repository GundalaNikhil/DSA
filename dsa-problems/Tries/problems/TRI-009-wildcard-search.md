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
time_limit: 2000
memory_limit: 256
---

# TRI-009: Wildcard Search

## Problem Statement

Implement search on a trie with wildcard pattern matching. The pattern may contain:

- `?` matches any single character
- `*` matches any sequence of characters (including empty)

Return `true` if any word in the trie matches the pattern.

![Problem Illustration](../images/TRI-009/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: lowercase words to insert into trie
- Last line: pattern string (may contain lowercase letters, `?`, and `*`)

## Output Format

Return `true` if any word matches the pattern, `false` otherwise.

## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= |pattern| <= 30` (pattern length)
- Words contain only lowercase English letters
- Pattern contains lowercase letters, `?`, and `*`

## Example 1

**Input:**

```
3
code
coder
codec
co*e
```

**Output:**

```
true
```

**Explanation:**

Pattern `co*e`:

- `*` can match "d" → `code` matches ✓
- `*` can match "dec" → `codec` matches ✓

![Example Visualization](../images/TRI-009/example-1.png)

## Example 2

**Input:**

```
4
hello
help
helper
helpful
hel?
```

**Output:**

```
true
```

**Explanation:**

Pattern `hel?`:

- `?` matches 'l' → `hell` (not in trie) ✗
- `?` matches 'p' → `help` matches ✓

## Notes

- `?` matches exactly one character
- `*` matches zero or more characters
- Use DFS/backtracking to explore all possibilities
- Early termination when match is found

## Related Topics

Trie, String, Recursion, Backtracking, Pattern Matching

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

    public void insertWord(String word) {
    }

    public boolean search(String pattern) {
        return false;
    }

    private boolean dfs(TrieNode node, String pattern, int index) {
        if (index == pattern.length()) {
            return node.isEnd;
        }

        char c = pattern.charAt(index);

        if (c == '?') {
            // Match any single character
            for (TrieNode child : node.children.values()) {
                if (dfs(child, pattern, index + 1)) {
                    return true;
                }
            }
            return false;
        } else if (c == '*') {
            // Match zero or more characters
            // Try matching 0 characters
            if (dfs(node, pattern, index + 1)) {
                return true;
            }
            // Try matching 1+ characters
            for (TrieNode child : node.children.values()) {
                if (dfs(child, pattern, index)) {
                    return true;
                }
            }
            return false;
        } else {
            // Regular character
            if (!node.children.containsKey(c)) {
                return false;
            }
            return dfs(node.children.get(c), pattern, index + 1);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        Solution solution = new Solution();
        for (int i = 0; i < n; i++) {
            solution.insertWord(sc.nextLine().trim());
        }

        String pattern = sc.nextLine().trim();
        boolean result = solution.search(pattern);

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
    def insert_word(self, word: str):
        return 0
    def search(self, pattern: str) -> bool:
        return False
    def _dfs(self, node: TrieNode, pattern: str, index: int) -> bool:
        return False
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])

    solution = Solution()
    for i in range(1, n + 1):
        solution.insert_word(lines[i].strip())

    pattern = lines[n + 1].strip()
    result = solution.search(pattern)

    print('true' if result else 'false')

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;

    bool dfs(TrieNode* node, const string& pattern, int index) {
        return false;
    }

public:
    Solution() {
        root = new TrieNode();
    }

    void insertWord(const string& word) {
    }

    bool search(const string& pattern) {
        return false;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();

    Solution solution;
    for (int i = 0; i < n; i++) {
        string word;
        getline(cin, word);
        solution.insertWord(word);
    }

    string pattern;
    getline(cin, pattern);

    bool result = solution.search(pattern);
    cout << (result ? "true" : "false") << endl;

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

  insertWord(word) {
    return 0;
  }

  search(pattern) {
    return 0;
  }

  dfs(node, pattern, index) {
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
  const n = parseInt(lines[0]);

  const solution = new Solution();
  for (let i = 1; i <= n; i++) {
    solution.insertWord(lines[i].trim());
  }

  const pattern = lines[n + 1].trim();
  const result = solution.search(pattern);

  console.log(result ? "true" : "false");
});
```

