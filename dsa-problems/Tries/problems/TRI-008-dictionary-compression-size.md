---
problem_id: TRI_DICTIONARY_COMPRESSION__2931
display_id: TRI-008
slug: dictionary-compression-size
title: "Dictionary Compression Size"
difficulty: Medium
difficulty_score: 45
topics:
  - Trie
  - String
  - Data Structures
tags:
  - trie
  - compression
  - memory-optimization
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-008: Dictionary Compression Size

## Problem Statement

Given `n` lowercase words, compute the total number of nodes in the trie needed to store them, including the root node.

![Problem Illustration](../images/TRI-008/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return a single integer representing the total number of trie nodes (including root).

## Constraints

- `1 <= n <= 10^5` (number of words)
- Total character length across all words <= `2 × 10^5`
- All words consist of lowercase English letters (a-z)
- Words may have duplicates

## Example 1

**Input:**

```
3
a
ab
abc
```

**Output:**

```
4
```

**Explanation:**

Trie structure:

```
  root (node 1)
    |
    a (node 2, word end)
    |
    b (node 3, word end)
    |
    c (node 4, word end)
```

Total nodes: 4 (root + a + b + c)

![Example Visualization](../images/TRI-008/example-1.png)

## Example 2

**Input:**

```
4
cat
car
card
dog
```

**Output:**

```
7
```

**Explanation:**

Trie structure:

```
      root (node 1)
      /    \
    c(2)   d(6)
    |       |
    a(3)    o(7)
   / \      |
  t(4) r(5) g
       |
     d
```

Total nodes: 7

## Notes

- The root node always counts as 1
- Duplicate words don't create additional nodes
- Shared prefixes result in node reuse

## Related Topics

Trie, String, Data Structures, Memory Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
}

class Solution {
    public int countTrieNodes(String[] words) {
        // Your implementation here
        return 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        int result = solution.countTrieNodes(words);

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

def count_trie_nodes(words: List[str]) -> int:
    """
    Returns total number of trie nodes including root
    """
    # Your implementation here
    pass

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])
    words = [lines[i+1].strip() for i in range(n)]

    result = count_trie_nodes(words)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
};

class Solution {
public:
    int countTrieNodes(vector<string>& words) {
        // Your implementation here
        return 1;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        getline(cin, words[i]);
    }

    Solution solution;
    int result = solution.countTrieNodes(words);

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
  }
}

function countTrieNodes(words) {
  // Your implementation here
  return 1;
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
  const words = [];
  for (let i = 1; i <= n; i++) {
    words.push(lines[i].trim());
  }

  const result = countTrieNodes(words);
  console.log(result);
});
```
