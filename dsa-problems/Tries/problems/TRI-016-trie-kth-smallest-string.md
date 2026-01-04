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
        // Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }

        Solution solution = new Solution();
        String result = solution.kthSmallest(words, k);
        System.out.println(result);
    }
}
```

### Python

```python
from typing import List

class Solution:
    def kth_smallest(self, words: List[str], k: int) -> str:
        # Implement here
        return ""

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    words = input_data[2:n+2]

    solution = Solution()
    result = solution.kth_smallest(words, k)
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
    string kthSmallest(const vector<string>& words, int k) {
        // Implement here
        return "";
    }
};

int main() {
    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
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
  kthSmallest(words, k) {
    // Implement here
    return "";
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
  const k = parseInt(tokens[1]);
  const words = tokens.slice(2, n + 2);

  const solution = new Solution();
  const result = solution.kthSmallest(words, k);
  process.stdout.write(result + "\n");
});
```
