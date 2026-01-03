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
    public int longestRepeatedSubstring(String s) {
        //Implement here
        return 0;
    }
    private void insertSuffix(String suffix) {
        //Implement here
    }
    private void dfs(TrieNode node, int depth) {
        //Implement here
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
        self.children = {}
        self.suffix_count = 0  # Number of suffixes passing through this node

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.max_length = 0

    def longest_repeated_substring(self, s: str) -> int:
        # //Implement here
        return 0
    def _insert_suffix(self, suffix: str):
        # //Implement here
        return 0
    def _dfs(self, node: TrieNode, depth: int):
        # //Implement here
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
public:
    void insertSuffix(const string& suffix) {
        //Implement here
    }
    void dfs(TrieNode* node, int depth) {
        //Implement here
    }
    int longestRepeatedSubstring(const string& s) {
        //Implement here
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
  insertSuffix(suffix) {
    //Implement here
    return 0;
  }
  dfs(node, depth) {
    //Implement here
    return 0;
  }
  longestRepeatedSubstring(s) {
    //Implement here
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
