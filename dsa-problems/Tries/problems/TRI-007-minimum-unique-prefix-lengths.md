---
problem_id: TRI_MINIMUM_UNIQUE_PREFIX__1847
display_id: TRI-007
slug: minimum-unique-prefix-lengths
title: "Minimum Unique Prefix Lengths"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Hash Table
tags:
  - trie
  - prefix
  - string-matching
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-007: Minimum Unique Prefix Lengths

## Problem Statement

Given an array of lowercase words, for each word, find the minimum prefix length that makes it unique among all words in the array.

![Problem Illustration](../images/TRI-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return an array of integers where the i-th integer represents the minimum prefix length for the i-th word.

Format: `[length1,length2,...]`

## Constraints

- `1 <= n <= 10^5` (number of words)
- Total character length across all words <= `2 × 10^5`
- All words consist of lowercase English letters (a-z)
- No two words are identical

## Example 1

**Input:**

```
4
zebra
dog
duck
dove
```

**Output:**

```
[1,2,2,2]
```

**Explanation:**

- "zebra": First character 'z' is unique among all first characters → prefix length = 1
- "dog": Shares 'd' with duck/dove, shares "do" with dove → at position 2, differs from "duck" → prefix length = 2
- "duck": Shares 'd' with dog/dove, but "du" is unique → prefix length = 2
- "dove": Shares 'd' with dog/duck, shares "do" with dog, but at position 2 has 'v' vs 'g'/'u' → prefix length = 2

Note: The minimum prefix is the earliest position where the count of words sharing that prefix becomes 1 for this word's path.

![Example Visualization](../images/TRI-007/example-1.png)

## Example 2

**Input:**

```
3
apple
application
app
```

**Output:**

```
[5,5,3]
```

**Explanation:**

- "apple": Shares "app" with others, shares "appl" with "application" → needs "apple" (5 chars)
- "application": Shares "app" with others, shares "appl" with "apple" → needs "appli" (5 chars)
- "app": Shortest word, but shares with others → needs full length (3 chars)

![Example Visualization](../images/TRI-007/example-2.png)

## Notes

- The minimum prefix length is determined by the trie structure
- If a word is a prefix of another word, it needs its full length
- Use a trie with node counts to efficiently compute minimum prefixes

## Related Topics

Trie, String, Prefix Matching, Hash Table

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    int count = 0;
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public int[] findMinimumPrefixLengths(String[] words) {
        return null;
    }




}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        int[] result = solution.findMinimumPrefixLengths(words);

        System.out.print("[");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(",");
        }
        System.out.println("]");

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
    def find_minimum_prefix_lengths(self, words: List[str]) -> List[int]:
        return []


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.find_minimum_prefix_lengths(words)

    print("[" + ",".join(map(str, result)) + "]")

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
    int count = 0;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;





public:
    Solution() {
        return 0;
    }

    vector<int> findMinimumPrefixLengths(vector<string>& words) {
        return {};
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
    vector<int> result = solution.findMinimumPrefixLengths(words);

    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]" << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.count = 0;
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
  }

  findMinimumPrefixLengths(words) {
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
  const words = [];
  for (let i = 1; i <= n; i++) {
    words.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.findMinimumPrefixLengths(words);

  console.log("[" + result.join(",") + "]");
});
```
