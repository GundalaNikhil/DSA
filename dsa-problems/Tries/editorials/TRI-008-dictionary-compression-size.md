---
problem_id: TRI_DICTIONARY_COMPRESSION__2931
display_id: TRI-008
slug: dictionary-compression-size
title: "Dictionary Compression Size"
difficulty: Medium
difficulty_score: 45
topics:
  - Trie
  - String
  - Data Structures
tags:
  - trie
  - compression
  - memory-optimization
premium: true
subscription_tier: basic
---

# TRI-008: Dictionary Compression Size

## 📋 Problem Summary

Given n words, compute the total number of nodes required in a trie to store them efficiently, including the root node.

## 🌍 Real-World Scenario

**Mobile Keyboard Dictionary Optimization**

Imagine you're an engineer at a mobile keyboard company like SwiftKey or Gboard. Your autocorrect dictionary contains hundreds of thousands of words, but mobile devices have limited memory. You need to determine how much memory your trie-based dictionary will consume before deploying it.

Consider storing these words: `["a", "ab", "abc"]`

**Naive Storage**: Store each word separately

- "a" → 1 char
- "ab" → 2 chars
- "abc" → 3 chars
- **Total: 6 characters** in memory

**Trie Storage**: Share common prefixes

```
  root (1 node)
    ↓
   'a' (1 node, stores "a")
    ↓
   'b' (1 node, stores "ab")
    ↓
   'c' (1 node, stores "abc")
```

- **Total: 4 nodes** (root + a + b + c)
- Memory saved: 33% reduction!

**Why This Problem Matters:**

- **Memory Efficiency**: Mobile keyboards with 100K words can save 40-60% memory using tries
- **Performance Metrics**: Node count directly correlates with memory footprint and load time
- **Deployment Decisions**: Helps decide if trie-based storage fits within memory budgets
- **Cost Optimization**: Cloud services charge for memory usage; accurate estimation saves costs

**Industry Applications:**

1. **Mobile Keyboards**: Gboard, SwiftKey optimize dictionary storage for offline use
2. **Spell Checkers**: Microsoft Word, Google Docs compress dictionaries for fast loading
3. **URL Shorteners**: Bitly, TinyURL use tries to store and retrieve shortened URLs efficiently
4. **DNS Servers**: Cache domain names in memory-efficient trie structures
5. **Search Engines**: Index compression for billions of web pages

**Real Impact Example:**

A mobile keyboard with 150,000 English words:

- Raw storage: ~1.5 million characters (10 avg chars/word)
- Trie storage: ~400,000 nodes (with shared prefixes)
- **Memory saved: 73%** → Fits in 2MB instead of 7.5MB!

![Real-World Application](../images/TRI-008/real-world-scenario.png)

## Detailed Explanation

The problem asks for a simple yet important metric: how many nodes does the trie contain?

**Key Insights:**

1. **Root node**: Every trie starts with one root node (counts as 1)
2. **Character nodes**: Each unique character in each position of any word requires a node
3. **Shared prefixes**: Words sharing prefixes share nodes, saving space
4. **Branching**: When words diverge, new branches are created

**Example Walkthrough:**

Words: `["a", "ab", "abc"]`

**Trie Node Creation:**

```
Build the trie step-by-step:

Step 1: Insert "a"
  Root
   |
   a (end) ← Node 2

  Nodes created: 2 (Root + a)

Step 2: Insert "ab"
  Root
   |
   a (end)  ← Reused!
   |
   b (end)  ← Node 3

  Nodes created: 3 (Root + a + b)
  Note: 'a' node reused, only 'b' is new

Step 3: Insert "abc"
  Root
   |
   a (end)  ← Reused!
   |
   b (end)  ← Reused!
   |
   c (end)  ← Node 4

  Nodes created: 4 (Root + a + b + c)
  Note: Both 'a' and 'b' reused, only 'c' is new

Comparison:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Without Trie (separate storage):
  "a"   → 1 char
  "ab"  → 2 chars
  "abc" → 3 chars
  Total: 6 character positions

With Trie (shared prefixes):
  Total: 4 nodes (33% space saving!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total nodes: 4
```

Build the trie:

```
Step 1: Insert "a"
  root
   |
   a (isEnd=true)
Nodes: 2 (root + a)

Step 2: Insert "ab"
  root
   |
   a (isEnd=true)
   |
   b (isEnd=true)
Nodes: 3 (root + a + b) - reused 'a'!

Step 3: Insert "abc"
  root
   |
   a (isEnd=true)
   |
   b (isEnd=true)
   |
   c (isEnd=true)
Nodes: 4 (root + a + b + c) - reused 'a' and 'b'!
```

**Total nodes: 4**

Without trie (separate storage): 1 + 2 + 3 = 6 character positions
With trie: 4 nodes (33% savings)

## Naive Approach

**Intuition:**

Count nodes by simulating trie construction with explicit tracking.

**Algorithm:**

1. Create a trie data structure with node creation tracking
2. Insert each word, creating new nodes as needed
3. Use a counter or unique node IDs to track total nodes created
4. Return the count

**Time Complexity:** O(N × L) where N = number of words, L = average length
**Space Complexity:** O(N × L) for the trie structure

**Why This Works:**

- Directly builds the trie and counts nodes
- Simple and straightforward
- Guaranteed correct result

**Limitations:**

- Not really "naive" - this IS the standard solution
- Could optimize by avoiding full trie construction if only count is needed
- For this problem, the direct approach is optimal

## Optimal Approach

**Key Insight:**

The "naive" approach is actually optimal for this problem. We must build the trie to count nodes accurately since node count depends on prefix sharing, which can only be determined during construction.

**Algorithm:**

1. **Initialize**: Create root node, set count = 1
2. **Insert Words**:
   ```
   for each word:
       node = root
       for each char in word:
           if char not in node.children:
               node.children[char] = new TrieNode()
               count++  // New node created
           node = node.children[char]
       mark node as end of word
   ```
3. **Return**: Total count

**Implementation Optimization:**

Instead of creating full trie objects, we can use a hash set to track unique paths, but this doesn't improve complexity.

**Time Complexity:** O(N × L)

- Must process every character of every word exactly once
- Cannot be better than O(N × L) since we must read all input

**Space Complexity:** O(N × L) for the trie

- Worst case: no prefix sharing (all different first chars)
- Best case: O(L) if all words are prefixes of one long word

**Why This Is Optimal:**

- **Lower bound**: Must read all input → Ω(N × L)
- **Our solution**: O(N × L) matches lower bound → optimal
- **No redundant work**: Each character processed once
- **Efficient sharing**: Automatically handles prefix overlap

![Algorithm Visualization](../images/TRI-008/algorithm-visualization.png)

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
    private int nodeCount = 1; // Start with root

    public int countTrieNodes(String[] words) {
        for (String word : words) {
            insert(word);
        }
        return nodeCount;
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                node.children.put(c, new TrieNode());
                nodeCount++;
            }
            node = node.children.get(c);
        }
        node.isEnd = true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.nextLine().trim();
        }

        Solution solution = new Solution();
        int result = solution.countTrieNodes(words);

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
        self.node_count = 1  # Start with root

    def count_trie_nodes(self, words: List[str]) -> int:
        for word in words:
            self._insert(word)
        return self.node_count

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_count += 1
            node = node.children[char]
        node.is_end = True

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.count_trie_nodes(words)

    print(result)

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
    bool isEnd = false;
};

class Solution {
private:
    TrieNode* root;
    int nodeCount;

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
                nodeCount++;
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

public:
    Solution() {
        root = new TrieNode();
        nodeCount = 1; // Start with root
    }

    int countTrieNodes(vector<string>& words) {
        for (const string& word : words) {
            insert(word);
        }
        return nodeCount;
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
    int result = solution.countTrieNodes(words);

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
  constructor() {
    this.root = new TrieNode();
    this.nodeCount = 1; // Start with root
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
        this.nodeCount++;
      }
      node = node.children.get(char);
    }
    node.isEnd = true;
  }

  countTrieNodes(words) {
    for (const word of words) {
      this.insert(word);
    }
    return this.nodeCount;
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
  const result = solution.countTrieNodes(words);

  console.log(result);
});
```

### Common Mistakes to Avoid

1. **Forgetting the Root Node**

   - **Issue**: Not counting the root in the total
   - ❌ Wrong: Initialize count = 0
   - ✅ Correct: Initialize count = 1 (root exists)

2. **Double Counting Nodes**

   - **Issue**: Incrementing count even when reusing existing nodes
   - ❌ Wrong: Incrementing count for every character processed
   - ✅ Correct: Only increment when creating NEW nodes

3. **Confusing Node Count with Character Count**

   - **Issue**: Counting total characters instead of unique nodes
   - ❌ Wrong: Returning sum of all word lengths
   - ✅ Correct: Returning number of trie nodes (with sharing)

4. **Not Handling Empty Input**

   - **Issue**: Returning 0 for empty word list
   - ❌ Wrong: Return 0 when no words
   - ✅ Correct: Return 1 (root exists even with no words)

## Related Concepts

- **Trie Data Structure**: Fundamental prefix tree for string storage
- **Memory Optimization**: Efficient data structure usage
- **Prefix Compression**: Exploiting shared prefixes to save space
- **Dictionary Compression**: Real-world application in spell checkers and autocomplete


## Constraints

- `1 <= n <= 10^5` (number of words)
- Total character length across all words <= `2 × 10^5`
- All words consist of lowercase English letters (a-z)
- Words may have duplicates