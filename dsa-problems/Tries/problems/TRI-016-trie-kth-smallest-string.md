---
problem_id: TRI_KTH_SMALLEST_STRING__5628
display_id: TRI-016
slug: trie-kth-smallest-string
title: "Trie-Based Kth Smallest String"
difficulty: Medium
difficulty_score: 51
topics:
  - Trie
  - String
  - Lexicographic Order
tags:
  - trie
  - kth-element
  - lexicographic
  - inorder-traversal
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-016: Trie-Based Kth Smallest String

## Problem Statement

Given a collection of `n` distinct lowercase strings and an integer `k`, return the k-th string in lexicographic order (1-indexed). If `k` exceeds the total number of strings, return an empty string.

![Problem Illustration](../images/TRI-016/problem-illustration.png)

## Input Format

- First line: two integers `n` (number of strings) and `k` (position)
- Next `n` lines: each contains a single lowercase string

## Output Format

Return the k-th smallest string in lexicographic order, or an empty string if k > n.

## Constraints

- `1 <= n <= 10^5` (number of strings)
- `1 <= k <= 10^9` (may exceed n)
- Total character length across all strings <= `2 × 10^5`
- All strings consist of lowercase English letters (a-z)
- No duplicate strings in input

## Example

**Input:**

```
3 2
b
a
aa
```

**Output:**

```
aa
```

**Explanation:**

Sorting strings lexicographically: `["a", "aa", "b"]`

Position 1: "a"
Position 2: "aa" ← answer
Position 3: "b"

The 2nd string is "aa".

![Example Visualization](../images/TRI-016/example-1.png)

## Notes

- k is 1-indexed (first string is at position 1)
- Lexicographic order: "a" < "aa" < "ab" < "b"
- Use trie with DFS traversal in alphabetical order
- Maintain subtree counts for efficient skip-counting

## Related Topics

Trie, String, Lexicographic Order, Kth Element, DFS

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new TreeMap<>();  // TreeMap for alphabetical order
    boolean isEnd = false;
    int count = 0;  // Number of strings in this subtree
}

class Solution {
    private TrieNode root = new TrieNode();
    private String result = "";
    private int remaining;

    public String kthSmallest(String[] words, int k) {
        return "";
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.count++;
        }
        node.isEnd = true;
    }

    private boolean dfs(TrieNode node, StringBuilder path) {
        if (node.isEnd) {
            remaining--;
            if (remaining == 0) {
                result = path.toString();
                return true;
            }
        }

        // Traverse children in alphabetical order (TreeMap ensures this)
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            char c = entry.getKey();
            TrieNode child = entry.getValue();

            // Check if k-th string is in this subtree
            if (child.count >= remaining) {
                path.append(c);
                if (dfs(child, path)) {
                    return true;
                }
                path.deleteCharAt(path.length() - 1);
            } else {
                // Skip this entire subtree
                remaining -= child.count;
            }
        }

        return false;
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
        String result = solution.kthSmallest(words, k);

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
    def kth_smallest(self, words: List[str], k: int) -> str:
        return ""
    def _insert(self, word: str):
        return 0
    def _dfs(self, node: TrieNode, path: List[str]) -> bool:
        return False
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n, k = map(int, lines[0].split())
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.kth_smallest(words, k)

    print(result if result else "")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    map<char, TrieNode*> children;  // map maintains alphabetical order
    bool isEnd = false;
    int count = 0;
};

class Solution {
private:
    TrieNode* root;
    string result;
    int remaining;

    void insert(const string& word) {
    }

    bool dfs(TrieNode* node, string& path) {
        return false;
    }

public:
    Solution() { root = new TrieNode(); }

    string kthSmallest(vector<string>& words, int k) {
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
    string result = solution.kthSmallest(words, k);

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
    this.count = 0;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.result = "";
    this.remaining = 0;
  }

  insert(word) {
    return 0;
  }

  dfs(node, path) {
    return 0;
  }

  kthSmallest(words, k) {
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
  const result = solution.kthSmallest(words, k);

  console.log(result);
});
```

