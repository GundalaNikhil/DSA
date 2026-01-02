---
problem_id: TRI_SHORTEST_ABSENT_BINARY__7241
display_id: TRI-013
slug: shortest-absent-binary-length-l
title: "Shortest Absent Binary String of Length L"
difficulty: Medium
difficulty_score: 52
topics:
  - Trie
  - Binary String
  - Backtracking
tags:
  - trie
  - binary
  - lexicographic
  - missing-element
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-013: Shortest Absent Binary String of Length L

## Problem Statement

Given a set of binary strings all of length exactly `L`, find the lexicographically smallest binary string of length `L` that is NOT present in the set. If all possible strings of length `L` are present, return an empty string.

![Problem Illustration](../images/TRI-013/problem-illustration.png)

## Input Format

- First line: two integers `L` (length) and `n` (number of binary strings)
- Next `n` lines: each contains a binary string of length exactly `L`

## Output Format

Return the lexicographically smallest missing binary string of length `L`, or an empty string if all are present.

## Constraints

- `1 <= L <= 20`
- `0 <= n <= 2^L` (set size cannot exceed total possibilities)
- All input strings have length exactly `L`
- Input strings consist only of '0' and '1'
- No duplicate strings in input

## Example

**Input:**

```
2 2
00
01
```

**Output:**

```
10
```

**Explanation:**

All possible binary strings of length 2: `["00", "01", "10", "11"]`

Given set: `{"00", "01"}`

Missing strings: `{"10", "11"}`

Lexicographically smallest missing: `"10"` (comes before "11")

![Example Visualization](../images/TRI-013/example-1.png)

## Notes

- Lexicographic order for binary strings: "00" < "01" < "10" < "11"
- If `n = 2^L`, all possible strings are present, return empty string
- Use a binary trie for efficient missing string detection
- DFS traversal in lexicographic order (explore '0' child before '1' child)

## Related Topics

Trie, Binary String, Lexicographic Order, DFS, Coding Theory

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    TrieNode[] children = new TrieNode[2];  // 0 and 1
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public String findShortestAbsent(String[] binaryStrings, int L) {
        return "";
    }

    private void insert(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            int idx = c - '0';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    private String dfs(TrieNode node, String path, int L) {
        // Reached target length
        if (path.length() == L) {
            return node.isEnd ? null : path;
        }

        // Try '0' first (lexicographically smaller)
        if (node.children[0] == null) {
            // Missing '0' path - fill rest with '0's
            StringBuilder result = new StringBuilder(path);
            result.append('0');
            while (result.length() < L) {
                result.append('0');
            }
            return result.toString();
        }

        String result = dfs(node.children[0], path + '0', L);
        if (result != null) return result;

        // Try '1'
        if (node.children[1] == null) {
            // Missing '1' path - fill rest with '0's
            StringBuilder sb = new StringBuilder(path);
            sb.append('1');
            while (sb.length() < L) {
                sb.append('0');
            }
            return sb.toString();
        }

        return dfs(node.children[1], path + '1', L);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int L = sc.nextInt();
        int n = sc.nextInt();

        String[] binaryStrings = new String[n];
        for (int i = 0; i < n; i++) {
            if (sc.hasNext()) {
                binaryStrings[i] = sc.next();
            } else {
                binaryStrings[i] = "";
            }
        }

        Solution solution = new Solution();
        String result = solution.findShortestAbsent(binaryStrings, L);

        System.out.println(result.isEmpty() ? "" : result);
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
    def find_shortest_absent(self, binary_strings: List[str], L: int) -> str:
        return ""
    def _insert(self, s: str):
        return 0
    def _dfs(self, node: TrieNode, path: str, L: int) -> str:
        return ""
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    L = int(lines[0].split()[0])
    n = int(lines[0].split()[1])

    binary_strings = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.find_shortest_absent(binary_strings, L)

    print(result if result else "")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;

    void insert(const string& s) {
    }

    string dfs(TrieNode* node, string path, int L) {
        return "";
    }

public:
    Solution() { root = new TrieNode(); }

    string findShortestAbsent(vector<string>& binaryStrings, int L) {
        return "";
    }
};

int main() {
    int L, n;
    cin >> L >> n;
    cin.ignore();

    vector<string> binaryStrings(n);
    for (int i = 0; i < n; i++) {
        getline(cin, binaryStrings[i]);
    }

    Solution solution;
    string result = solution.findShortestAbsent(binaryStrings, L);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null]; // 0 and 1
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
  }

  insert(s) {
    return 0;
  }

  dfs(node, path, L) {
    return 0;
  }

  findShortestAbsent(binaryStrings, L) {
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
  const [L, n] = lines[0].split(" ").map(Number);
  const binaryStrings = [];
  for (let i = 1; i <= n; i++) {
    binaryStrings.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.findShortestAbsent(binaryStrings, L);

  console.log(result);
});
```

