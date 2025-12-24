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
    TrieNode[] children = new TrieNode[2];
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    public String findShortestAbsent(String[] binaryStrings, int L) {
        // Your implementation here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int L = sc.nextInt();
        int n = sc.nextInt();
        sc.nextLine();

        String[] binaryStrings = new String[n];
        for (int i = 0; i < n; i++) {
            binaryStrings[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        String result = solution.findShortestAbsent(binaryStrings, L);

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
        self.children = [None, None]
        self.is_end = False

def find_shortest_absent(binary_strings: List[str], L: int) -> str:
    """
    Find lexicographically smallest missing binary string of length L
    """
    # Your implementation here
    pass

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    L, n = map(int, lines[0].split())
    binary_strings = [lines[i+1].strip() for i in range(n)]

    result = find_shortest_absent(binary_strings, L)
    print(result if result else "")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
    bool isEnd = false;
};

class Solution {
public:
    string findShortestAbsent(vector<string>& binaryStrings, int L) {
        // Your implementation here
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
    this.children = [null, null];
    this.isEnd = false;
  }
}

function findShortestAbsent(binaryStrings, L) {
  // Your implementation here
  return "";
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

  const result = findShortestAbsent(binaryStrings, L);
  console.log(result);
});
```
