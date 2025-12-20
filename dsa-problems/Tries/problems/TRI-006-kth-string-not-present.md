---
problem_id: TRI_KTH_MISSING__4257
display_id: TRI-006
slug: kth-string-not-present
title: "Lexicographic k-th String Not Present"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Combinatorics
  - DFS
tags:
  - trie
  - string
  - combinatorics
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lexicographic k-th String Not Present

## Problem Statement

Given a trie of inserted lowercase strings, find the k-th lexicographically smallest string of length up to `L` that is NOT present in the trie.

![Problem Illustration](../images/TRI-006/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `L`, `k` (number of strings, max length, kth position)
- Next `n` lines: Each contains a lowercase string already inserted in the trie

## Output Format

Print the k-th missing string of length ≤ L in lexicographic order.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ L ≤ 6
- 1 ≤ k ≤ 10^9
- All strings consist of lowercase English letters (a-z)

## Examples

### Example 1

**Input:**

```
2 2 1
a
b
```

**Output:**

```
aa
```

**Explanation:**

Inserted: "a", "b"
Missing strings of length ≤ 2 in order:

1. "aa" ← answer
2. "ab"
3. "ac"
   ...

![Example 1 Visualization](../images/TRI-006/example-1.png)

## Notes

- Strings can end at any depth from 1 to L
- Empty string not counted
- Lexicographic order: a < aa < ab < ... < z < za < ...
- Use DFS to count missing strings efficiently

## Related Topics

Trie, String, Combinatorics, DFS, Missing Elements

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEnd;

    TrieNode() {
        children = new HashMap<>();
        isEnd = false;
    }
}

class Solution {
    public String kthMissingString(List<String> inserted, int L, int k) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int L = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        List<String> inserted = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            inserted.add(sc.nextLine());
        }

        Solution solution = new Solution();
        String result = solution.kthMissingString(inserted, L, k);

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
        self.is_end = False

def kth_missing_string(inserted: list, L: int, k: int) -> str:
    # Your implementation here
    pass

def main():
    n, L, k = map(int, input().split())
    inserted = [input().strip() for _ in range(n)]
    result = kth_missing_string(inserted, L, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd;

    TrieNode() : isEnd(false) {}
};

class Solution {
public:
    string kthMissingString(vector<string>& inserted, int L, int k) {
        // Your implementation here
    }
};

int main() {
    int n, L, k;
    cin >> n >> L >> k;
    cin.ignore();

    vector<string> inserted(n);
    for (int i = 0; i < n; i++) {
        getline(cin, inserted[i]);
    }

    Solution solution;
    string result = solution.kthMissingString(inserted, L, k);

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
  }
}

class Solution {
  kthMissingString(inserted, L, k) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, L, k] = lines[0].split(" ").map(Number);
  const inserted = lines.slice(1, n + 1);

  const solution = new Solution();
  const result = solution.kthMissingString(inserted, L, k);

  console.log(result);
});
```
