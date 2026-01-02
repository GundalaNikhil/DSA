---
problem_id: TRI_SUFFIX_LONGEST_REPEAT__3945
display_id: TRI-011
slug: suffix-trie-longest-repeat
title: "Suffix Trie Longest Repeat"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - String
  - Suffix Structures
tags:
  - trie
  - suffix-trie
  - longest-repeat
  - string-algorithms
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-011: Suffix Trie Longest Repeat

## Problem Statement

Build a suffix trie (or use suffix array alternative) to find the length of the longest repeated substring in string `s`.

![Problem Illustration](../images/TRI-011/problem-illustration.png)

## Input Format

- Single line: string `s` (lowercase letters)

## Output Format

Return an integer representing the length of the longest repeated substring.

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
banana
```

**Output:**

```
3
```

**Explanation:**

"ana" appears twice (at positions 1-3 and 3-5), length = 3.

![Example Visualization](../images/TRI-011/example-1.png)

## Notes

- A repeated substring must appear at least twice
- Return 0 if no substring repeats
- Overlapping occurrences count (e.g., "ana" in "banana")

## Related Topics

Trie, Suffix Structures, String Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    int suffixCount = 0;  // Number of suffixes passing through this node
}

class Solution {
    private TrieNode root = new TrieNode();
    private int maxLength = 0;

    public int longestRepeatedSubstring(String s) {
        return 0;
    }

    private void insertSuffix(String suffix) {
        TrieNode node = root;
        for (char c : suffix.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.suffixCount++;  // Increment count for each suffix passing through
        }
    }

    private void dfs(TrieNode node, int depth) {
        // A repeated substring exists if 2+ suffixes pass through this node
        if (node.suffixCount >= 2 && depth > 0) {
            maxLength = Math.max(maxLength, depth);
        }

        for (TrieNode child : node.children.values()) {
            dfs(child, depth + 1);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();

        Solution solution = new Solution();
        int result = solution.longestRepeatedSubstring(s);
        System.out.println(result);

        sc.close();
    }
}
```

### Python

```python
class TrieNode:
    def __init__(self):
        return 0
class Solution:
    def __init__(self):
        return 0
    def longest_repeated_substring(self, s: str) -> int:
        return 0
    def _insert_suffix(self, suffix: str):
        return 0
    def _dfs(self, node: TrieNode, depth: int):
        return 0
def main():
    import sys
    s = sys.stdin.read().strip()

    solution = Solution()
    result = solution.longest_repeated_substring(s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int suffixCount = 0;  // Number of suffixes passing through this node
};

class Solution {
private:
    TrieNode* root;
    int maxLength;

    void insertSuffix(const string& suffix) {
    }

    void dfs(TrieNode* node, int depth) {
    }

public:
    Solution() {
        root = new TrieNode();
        maxLength = 0;
    }

    int longestRepeatedSubstring(const string& s) {
        return 0;
    }
};

int main() {
    string s;
    getline(cin, s);

    Solution solution;
    int result = solution.longestRepeatedSubstring(s);
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
    this.suffixCount = 0; // Number of suffixes passing through this node
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.maxLength = 0;
  }

  insertSuffix(suffix) {
    return 0;
  }

  dfs(node, depth) {
    return 0;
  }

  longestRepeatedSubstring(s) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = "";
rl.on("line", (line) => {
  input = line.trim();
  rl.close();
}).on("close", () => {
  const solution = new Solution();
  const result = solution.longestRepeatedSubstring(input);
  console.log(result);
});
```

