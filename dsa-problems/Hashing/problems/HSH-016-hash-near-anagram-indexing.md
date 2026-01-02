---
problem_id: HSH_HASH_NEAR_ANAGRAM_INDEXING__7523
display_id: HSH-016
slug: hash-near-anagram-indexing
title: "Hash-Based Near-Anagram Indexing"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Anagrams
  - Union-Find
tags:
  - hashing
  - anagram
  - grouping
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-016: Hash-Based Near-Anagram Indexing

## Problem Statement

Group words where two words belong to the same group if they become anagrams after deleting exactly one character from each (you can choose any character to delete).

Return the number of distinct groups formed.

![Problem Illustration](../images/HSH-016/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: one word per line

## Output Format

- Single integer: number of distinct groups

## Constraints

- `1 <= n <= 10^5`
- `1 <= word length <= 30`
- Words contain only lowercase English letters

## Example

**Input:**

```
4
abcd
abdc
abc
abd
```

**Output:**

```
2
```

**Explanation:**

Words: ["abcd", "abdc", "abc", "abd"]

Group 1: "abcd", "abdc", "abc"

- "abcd" → delete 'd' → "abc" (sorted)
- "abdc" → delete 'd' → "abc" (sorted)
- "abc" → delete 'c' → "ab" (sorted), matches others

Group 2: "abd"

- "abd" → delete 'd' → "ab" (sorted)

Total: 2 groups

![Example Visualization](../images/HSH-016/example-1.png)

## Notes

- For each word, generate all possible strings after deleting one character
- Sort each deletion result to create signature
- Use Union-Find or map to group words sharing signatures
- Time complexity: O(n × L²) where L is word length
- Space complexity: O(n × L)

## Related Topics

Anagrams, Hashing, Union-Find, String Manipulation, Grouping

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    class UnionFind {
        int[] parent;
        int count;
        
        public UnionFind(int n) {
        return 0;
    }
        
        public int find(int x) {
        return 0;
    }
        
        public void union(int x, int y) {
    }
    }
    
    public int countNearAnagramGroups(String[] words) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            sc.nextLine();
            String[] words = new String[n];
            for (int i = 0; i < n; i++) {
                words[i] = sc.nextLine();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.countNearAnagramGroups(words));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class UnionFind:
    def __init__(self, n):
        return 0
    def find(self, x):
        return 0
    def union(self, x, y):
        return 0
class Solution:
    def count_near_anagram_groups(self, words: list) -> int:
        return 0
def count_near_anagram_groups(words: list) -> int:
    return 0
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        words = []
        for _ in range(n):
            words.append(next(iterator))
            
        print(count_near_anagram_groups(words))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <numeric>

using namespace std;

class UnionFind {
public:
    vector<int> parent;
    int count;
    
    UnionFind(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        count = n;
    }
    
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
            count--;
        }
    }
};

class Solution {
public:
    int countNearAnagramGroups(vector<string>& words) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<string> words(n);
        for (int i = 0; i < n; i++) {
            cin >> words[i];
        }
        
        Solution solution;
        cout << solution.countNearAnagramGroups(words) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.count = n;
  }
  
  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }
  
  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);
    if (rootX !== rootY) {
      this.parent[rootX] = rootY;
      this.count--;
    }
  }
}

class Solution {
  countNearAnagramGroups(words) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  
  const words = [];
  for (let i = 0; i < n; i++) {
    words.push(data[ptr++]);
  }
  
  const solution = new Solution();
  console.log(solution.countNearAnagramGroups(words));
});
```

