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
    private TrieNode root = new TrieNode();

    public void insertWord(String word) {
    }

    public boolean hasEditDistance1(String query) {
        return false;
    }

    private boolean dfs(TrieNode node, String query, int index, int edits) {
        // If we've used more than 1 edit, prune
        if (edits > 1) {
            return false;
        }

        // If we've consumed the query
        if (index == query.length()) {
            // Check if this is a word end and we used exactly 1 edit
            // OR we can delete remaining trie characters (each is 1 edit)
            if (node.isEnd && edits == 1) {
                return true;
            }
            // Can we reach a word by deleting one more char?
            if (edits == 0) {
                for (TrieNode child : node.children.values()) {
                    if (child.isEnd) {
                        return true;
                    }
                }
            }
            return false;
        }

        char c = query.charAt(index);

        // 1. Match current character (no edit)
        if (node.children.containsKey(c)) {
            if (dfs(node.children.get(c), query, index + 1, edits)) {
                return true;
            }
        }

        // Only try edit operations if budget allows
        if (edits < 1) {
            // 2. Substitute (replace query char with trie char)
            for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
                if (entry.getKey() != c) {
                    if (dfs(entry.getValue(), query, index + 1, edits + 1)) {
                        return true;
                    }
                }
            }

            // 3. Delete from query (insert into result)
            if (dfs(node, query, index + 1, edits + 1)) {
                return true;
            }

            // 4. Insert into query (delete from trie)
            for (TrieNode child : node.children.values()) {
                if (dfs(child, query, index, edits + 1)) {
                    return true;
                }
            }
        }

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
        return 0
class Solution:
    def __init__(self):
        return 0
    def insert_word(self, word: str):
        return 0
    def has_edit_distance_1(self, query: str) -> bool:
        return False
    def _dfs(self, node: TrieNode, query: str, index: int, edits: int) -> bool:
        return False
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
private:
    TrieNode* root;

    bool dfs(TrieNode* node, const string& query, int index, int edits) {
        return false;
    }

public:
    Solution() {
        root = new TrieNode();
    }

    void insertWord(const string& word) {
    }

    bool hasEditDistance1(const string& query) {
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
  constructor() {
    this.root = new TrieNode();
  }

  insertWord(word) {
    return 0;
  }

  hasEditDistance1(query) {
    return 0;
  }

  dfs(node, query, index, edits) {
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

