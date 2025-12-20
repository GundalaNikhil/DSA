---
problem_id: TRI_PREFIX_FREE_CHECK__6183
display_id: TRI-012
slug: prefix-free-after-inserts
title: "Prefix-Free Check After Inserts"
difficulty: Medium
difficulty_score: 48
topics:
  - Trie
  - String
tags:
  - trie
  - prefix-free
  - phone-numbers
premium: true
subscription_tier: basic
---

# TRI-012: Prefix-Free Check After Inserts

## 📋 Problem Summary

Insert phone numbers (digit strings) into a trie. After each insertion, report whether the set remains prefix-free (no number is a prefix of another).

## 🌍 Real-World Scenario

**Telephone Routing Systems**

In telecom systems, phone number routing must be prefix-free to avoid ambiguity. If "911" and "9112345" both exist, when someone dials "911234...", the system won't know if they're calling "911" or continuing to dial "9112345".

## Detailed Explanation

A set is prefix-free if no string is a prefix of another. After each insertion, check:
1. Is the new number a prefix of any existing number?
2. Is any existing number a prefix of the new number?

## Naive Approach

After each insert, compare new number against all existing numbers: O(n²×L)

## Optimal Approach

Use trie. During insertion:
- If we reach end of new number but node has children → NOT prefix-free
- If we pass through an end-of-word node before finishing → NOT prefix-free
- Otherwise → prefix-free

**Prefix-Free Checking:**

```
Example: Insert ["911", "9112345", "123"]

Insert "911":
Root
  |
  9
  |
  1
  |
  1 (end) ← Prefix-free so far ✓

Insert "9112345":
Root
  |
  9
  |
  1
  |
  1 (end) ← We pass through existing end! ✗
  |
  2 → 3 → 4 → 5 (would be end)

Result: FALSE (9112345 extends 911)

Reset and try different order:

Insert "123":
Root
  |
  1
  |
  2
  |
  3 (end) ← Prefix-free ✓

Insert "911":
Root
  |
  +-- 1
  |   |
  |   2 → 3 (end)
  |
  +-- 9
      |
      1 → 1 (end) ← No conflicts, prefix-free ✓

Insert "9112345":
Root
  |
  +-- 1 → 2 → 3 (end)
  |
  +-- 9
      |
      1
      |
      1 (end) ← We pass through existing end! ✗
      |
      2 → 3 → 4 → 5

Result: [true, true, false]
```

**Time**: O(L) per insert
**Space**: O(N×L)

## Implementations

### Java
```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private TrieNode root = new TrieNode();
    
    public boolean insert(String number) {
        TrieNode node = root;
        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            
            // If current node is end of another number, new number extends it
            if (node.isEnd) return false;
            
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        
        // If node has children, this number is prefix of existing numbers
        if (!node.children.isEmpty()) return false;
        
        node.isEnd = true;
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        
        Solution solution = new Solution();
        List<Boolean> results = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            String number = sc.nextLine().trim();
            results.add(solution.insert(number));
        }
        
        System.out.print("[");
        for (int i = 0; i < results.size(); i++) {
            System.out.print(results.get(i));
            if (i < results.size() - 1) System.out.print(",");
        }
        System.out.println("]");
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

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number: str) -> bool:
        node = self.root
        for char in number:
            if node.is_end:
                return False
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if len(node.children) > 0:
            return False
        
        node.is_end = True
        return True

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    
    solution = Solution()
    results = []
    for i in range(1, n + 1):
        results.append(solution.insert(lines[i].strip()))
    
    print("[" + ",".join(str(r).lower() for r in results) + "]")

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;
    
public:
    Solution() { root = new TrieNode(); }
    
    bool insert(const string& number) {
        TrieNode* node = root;
        for (char c : number) {
            if (node->isEnd) return false;
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        
        if (!node->children.empty()) return false;
        node->isEnd = true;
        return true;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    Solution solution;
    vector<bool> results;
    
    for (int i = 0; i < n; i++) {
        string number;
        getline(cin, number);
        results.push_back(solution.insert(number));
    }
    
    cout << "[";
    for (int i = 0; i < results.size(); i++) {
        cout << (results[i] ? "true" : "false");
        if (i < results.size() - 1) cout << ",";
    }
    cout << "]" << endl;
    
    return 0;
}
```

### JavaScript
```javascript
const readline = require('readline');

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

  insert(number) {
    let node = this.root;
    for (const char of number) {
      if (node.isEnd) return false;
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
    }
    
    if (node.children.size > 0) return false;
    node.isEnd = true;
    return true;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const lines = [];
rl.on('line', (line) => {
  lines.push(line);
}).on('close', () => {
  const n = parseInt(lines[0]);
  const solution = new Solution();
  const results = [];
  
  for (let i = 1; i <= n; i++) {
    results.push(solution.insert(lines[i].trim()));
  }
  
  console.log('[' + results.join(',') + ']');
});
```

## Common Mistakes

1. Not checking both directions (prefix and extension)
2. Forgetting to mark isEnd after successful insert
3. Not returning false when node has children at end

## Related Concepts
- Prefix-Free Codes (Huffman Coding)
- Telephone Routing
- Trie Data Structure
