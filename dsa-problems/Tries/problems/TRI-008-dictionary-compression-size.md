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

class Solution {
    public int countTrieNodes(String[] words) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }

        Solution solution = new Solution();
        int result = solution.countTrieNodes(words);
        System.out.println(result);
    }
}
```

### Python

```python
from typing import List

class Solution:
    def count_trie_nodes(self, words: List[str]) -> int:
        # Implement here
        return 0

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    words = input_data[1:n+1]

    solution = Solution()
    result = solution.count_trie_nodes(words)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int countTrieNodes(vector<string>& words) {
        // Implement here
        return 0;
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
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

class Solution {
  countTrieNodes(words) {
    // Implement here
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
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  const n = parseInt(tokens[0]);
  const words = tokens.slice(1, n + 1);

  const solution = new Solution();
  const result = solution.countTrieNodes(words);
  console.log(result);
});
```
