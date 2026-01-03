---
problem_id: TRI_SPELL_CHECKER__8124
display_id: TRI-010
slug: trie-spell-checker
title: "Trie-Based Spell Checker"
difficulty: Medium
difficulty_score: 56
topics:
  - Trie
  - String
  - Edit Distance
  - Dynamic Programming
tags:
  - trie
  - spell-check
  - edit-distance
  - string-matching
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-010: Trie-Based Spell Checker

## Problem Statement

Given a dictionary of words in a trie, for each query word, return `true` if there exists a dictionary word at edit distance exactly 1 from the query. Edit distance 1 means one character insertion, deletion, or substitution.

![Problem Illustration](../images/TRI-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of dictionary words)
- Next `n` lines: lowercase dictionary words
- Last line: query word (lowercase)

## Output Format

Return `true` if any dictionary word is at edit distance 1 from query, `false` otherwise.

## Constraints

- `1 <= n <= 10^5` (dictionary size)
- `1 <= queries <= 10^5`
- `1 <= |word| <= 25` (word length)
- All words are lowercase English letters

## Example 1

**Input:**

```
2
cat
bat
cats
```

**Output:**

```
true
```

**Explanation:**

Query "cats" is edit distance 1 from "cat" (insert 's').

## Example 2

**Input:**

```
3
hello
world
help
hero
```

**Output:**

```
true
```

**Explanation:**

Query "car" is not in the dictionary {"cat", "bat"}. Check edit distance 1:

**Input:**

```
2
cat
bat
car
```

**Output:**

```
true
```

**Explanation:**

Query "car" is edit distance 1 from "cat" (substitute 't' with 'r').

## Notes

- Edit operations: insert one char, delete one char, or replace one char
- Must be exactly edit distance 1 (not 0, not 2+)
- Use trie structure to efficiently explore edit possibilities

## Related Topics

Trie, String, Edit Distance, Dynamic Programming, Spell Checking

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
    public void insertWord(String word) {
        //Implement here
    }
    public boolean hasEditDistance1(String query) {
        //Implement here
        return false;
    }
    private boolean dfs(TrieNode node, String query, int index, int edits) {
        //Implement here
        return false;
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

        String query = sc.nextLine().trim();
        boolean result = solution.hasEditDistance1(query);

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
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str):
        # //Implement here
        return 0
    def has_edit_distance_1(self, query: str) -> bool:
        # //Implement here
        return 0
    def _dfs(self, node: TrieNode, query: str, index: int, edits: int) -> bool:
        # //Implement here
        return 0
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])

    solution = Solution()
    for i in range(1, n + 1):
        solution.insert_word(lines[i].strip())

    query = lines[n + 1].strip()
    result = solution.has_edit_distance_1(query)

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
public:
    bool dfs(TrieNode* node, const string& query, int index, int edits) {
        //Implement here
        return false;
    }
    void insertWord(const string& word) {
        //Implement here
    }
    bool hasEditDistance1(const string& query) {
        //Implement here
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

    string query;
    getline(cin, query);

    bool result = solution.hasEditDistance1(query);
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
  insertWord(word) {
    //Implement here
    return 0;
  }
  hasEditDistance1(query) {
    //Implement here
    return 0;
  }
  dfs(node, query, index, edits) {
    //Implement here
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

  const query = lines[n + 1].trim();
  const result = solution.hasEditDistance1(query);

  console.log(result ? "true" : "false");
});
```
