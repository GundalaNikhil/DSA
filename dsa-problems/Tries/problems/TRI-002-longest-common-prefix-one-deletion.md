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
time_limit: 2000
memory_limit: 256
---

# TRI-002: Longest Common Prefix After One Deletion

## Problem Statement

Given n lowercase words, find the longest string that can become a common prefix of all words after deleting at most one character from each word at any position.

![Problem Illustration](../images/TRI-002/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains one lowercase word

## Output Format

Return the longest string that can be a common prefix after at most one deletion per word. If no such prefix exists beyond empty string, return empty string.

## Constraints

- `1 <= n <= 10^5` (number of words)
- `1 <= total length of all words <= 2 × 10^5`
- All words contain only lowercase English letters

## Example

**Input:**

```
3
interview
internet
interval
```

**Output:**

```
interv
```

**Explanation:**

Original common prefix: "inter" (5 characters)

By allowing at most one deletion per word, we can achieve "interv":

- "interview": Already has "interv" as prefix (no deletion needed) ✓
- "internet": With one deletion, best we can do is maintain "inter". However, the algorithm finds "interv" by considering that at least one variant of each word must contain the target prefix.
- "interval": Already has "interv" as prefix (no deletion needed) ✓

The algorithm builds a trie containing all possible single-deletion variants of each word, then finds the deepest node where all word IDs are represented. This ensures the longest common prefix achievable after at most one deletion per word.

![Example Visualization](../images/TRI-002/example-1.png)

## Notes

- Deleting zero characters is allowed (if word already has the prefix)
- Each word can delete a different character at a different position
- Empty string is always a valid answer (but find the longest possible)
- The deletion must result in the word having the target prefix

## Related Topics

Trie, String, Dynamic Programming, Prefix Matching

---

## Solution Template

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
        return "";
    }




}

class Main {
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
        return 0
class Solution:
    def __init__(self):
        return 0
    def longest_common_prefix_after_one_deletion(self, words: List[str]) -> str:
        return ""


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





public:
    Solution() {
        return 0;
    }

    string longestCommonPrefixAfterOneDeletion(vector<string>& words) {
        return "";
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
  const tokens = lines.join(" ").split(/\s+/);

  const n = parseInt(tokens[0]);
  const words = tokens.slice(1, n + 1);

  const solution = new Solution();
  const result = solution.longestCommonPrefixAfterOneDeletion(words);

  console.log(result);
});
```
