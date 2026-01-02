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

class Solution {
    public String kthSmallest(String[] words, int k) {
        // Implementation here
        return "";
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

class Solution:
    def kth_smallest(self, words: List[str], k: int) -> str:
        # Implementation here
        return ""

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

class Solution {
public:
    string kthSmallest(vector<string>& words, int k) {
        // Implementation here
        return {};
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

class Solution {
  constructor() {
    // Implementation here
    return null;
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
