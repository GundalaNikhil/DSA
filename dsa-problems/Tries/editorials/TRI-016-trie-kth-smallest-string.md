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
---

# TRI-016: Trie-Based Kth Smallest String

## 📋 Problem Summary

Given a collection of lowercase strings, return the k-th string in lexicographic order (1-indexed). If k exceeds the total number of strings, return an empty string.

## 🌍 Real-World Scenario

**Database Query Optimization & Pagination**

Consider a large-scale database system like MongoDB or Elasticsearch handling millions of indexed documents. When users request sorted results with pagination (e.g., "show me items 1001-1050"), the system must efficiently:

1. **Skip to the k-th element** without loading all previous elements
2. **Maintain lexicographic order** for string-based indices
3. **Handle large datasets** where k could be in millions

**Real-World Example:**

A dictionary app with 500,000 English words needs to:

- Display the 100,000th word alphabetically (for a quiz game)
- Support "jump to page N" functionality
- Efficiently handle queries like "show words ranked 50,000 to 50,100"

Traditional approaches:

- **Sort entire dataset**: O(n log n) time, impractical for frequent queries
- **Linear scan**: O(k) time, slow for large k

**Trie-based approach**:

- Build trie once: O(total characters)
- Query k-th element: O(length of k-th string)
- Enables efficient skip-counting through lexicographic ordering

**Industry Applications:**

1. **Autocomplete Systems**: "Show me the 10th most common search query starting with 'comp'"
2. **E-commerce**: "Display products ranked 500-600 alphabetically"
3. **File Systems**: Efficiently navigate sorted directory listings
4. **DNA Sequencing**: Find the k-th lexicographically smallest DNA sequence in a genome database
5. **Log Analysis**: Retrieve specific log entries from sorted indices

![Real-World Application](../images/TRI-016/real-world-scenario.png)

## Detailed Explanation

**Problem Breakdown:**

Given:

- A set of n distinct lowercase strings
- An integer k (1-indexed)

Find:

- The k-th string in lexicographic (dictionary) order
- Return empty string if k > n

**Key Insights:**

1. **Lexicographic Order**: "a" < "aa" < "ab" < "b" < "ba"
2. **Trie Structure**: Natural lexicographic ordering through DFS traversal
3. **Counting Strategy**: Each node can track count of strings in its subtree
4. **Skip Counting**: Navigate to k-th element without examining all previous strings

**Example Walkthrough:**

Strings: `["b", "a", "aa"]`, k=2

Lexicographic order: `["a", "aa", "b"]`

k=2 → return "aa"

**DFS with Counting:**

```
Trie Structure:
      Root
      /  \
    a(2) b(1)
    |     ↓
    a(1)  END
    ↓
   END

Each node shows: letter(subtree_count)

DFS Traversal (lexicographic order):
────────────────────────────────────
Step 1: Traverse 'a' subtree first (count=2)
  |
  +-- Visit 'a' node (is_end=False, continue)
  |   Count so far: 0
  |
  +-- Check if current node is END? No
  |
  +-- Visit child 'a' (depth 2)
  |   |
  |   +-- This node is END → "aa"
  |       Count: 1
  |       k=2, count=1 < k, continue...
  |
  +-- Back to depth 1, continue children? No more
  |
  +-- Current node 'a' at depth 1 is END? No
```

**Corrected Trie Structure:**

```
Trie:
      Root
      /  \
    a     b(END)
    |
    a(END)

Corrected DFS:
────────────────────────────────────
Path 1: Root → 'a' (NOT end)
  Count: 0

Path 2: Root → 'a' → 'a' (END) ← "aa"
  Count: 1
  k=2, count=1 < k, continue

Path 3: Root → 'a' (backtrack, IS END!) ← "a"
  Count: 2
  k=2, count=2 == k ✓
  Return "a"

**Revised Analysis:**

DFS traverses depth-first:
────────────────────────────────────
Visit 'a' branch:
  - Go deep first: 'a' → 'a' (END) = "aa" → count=1
  - Backtrack: Check 'a' itself (NOT END)
  - No more children
Back to root, check 'a' (NOT END at depth 1)

**Corrected Trie Structure:**

```

      Root
      /  \
    a(E)  b(E)
    |
    a(E)

Where (E) = END node

```

**DFS Lexicographic Traversal:**

```

1. Visit 'a' child from root

   - Node 'a' IS END ← String "a", count=1 ✓

2. Visit 'a' child from 'a'

   - Node 'a' IS END ← String "aa", count=2 ✓
   - k=2, found! Return "aa"

3. Would visit 'b' next, but already done

Result: "aa"

Visualization:
Root
/ \
 a(1) b(3)
|
a(2)

Numbers in () show the count when visiting each END node

```

**Trie Structure:**

```

      root
      /  \
    a(1) b(1,END)
    |
    a(1,END)

```

**DFS Traversal** (in-order):

1. Visit 'a' subtree first (comes before 'b')
   - Visit "a" (END) → count=1
   - Visit 'a' child
     - Visit "aa" (END) → count=2 ← k=2, return "aa"
2. Would visit 'b' next, but already found answer

![Problem Illustration](../images/TRI-016/problem-illustration.png)

## Naive Approach

**Intuition:**

Store all strings in an array, sort them, and return the k-th element.

**Algorithm:**

1. Create an array from all strings
2. Sort the array using lexicographic comparison
3. If k <= array length, return array[k-1]
4. Otherwise return empty string

**Time Complexity:** O(n log n × L)

- Sorting n strings: O(n log n) comparisons
- Each comparison: O(L) where L = average string length
- Total: O(n log n × L)

**Space Complexity:** O(n × L) for the array

**Limitations:**

- **Sorting Overhead**: Wasteful if we only need one element
- **Memory Intensive**: Must store all strings in array
- **Not Reusable**: Each new query requires re-sorting
- **Poor for Large k**: No advantage even if k is near n

## Optimal Approach

**Key Insight:**

Use a **trie with subtree counts** and perform **in-order DFS traversal** with skip counting to directly jump to the k-th string.

**Algorithm:**

1. **Build Trie with Counts**:

   - Each node stores count of strings in its subtree
   - Mark end-of-word nodes

2. **DFS with Skip Counting**:

```

function findKth(node, k):
if node is END:
k--
if k == 0:
return current path

       for each child in alphabetical order:
           subtree_count = child.count
           if subtree_count >= k:
               recurse into child
           else:
               skip this subtree (k -= subtree_count)

```

3. **Optimization**:
- Instead of counting during traversal, pre-compute counts during trie construction
- Navigate directly to k-th element by skipping entire subtrees

**Time Complexity:** O(n × L + L_k)

- Build trie: O(n × L) where n = number of strings, L = average length
- Find k-th: O(L_k) where L_k = length of k-th string
- **Amortized**: O(L_k) per query after one-time O(n × L) build

**Space Complexity:** O(n × L) for the trie

**Why This Is Optimal:**

- **No Sorting Required**: Lexicographic order implicit in trie structure
- **Skip Entire Subtrees**: Don't examine strings we won't return
- **Reusable Structure**: Multiple queries answered efficiently
- **Linear Query Time**: O(L_k) to find k-th element

**Example Execution:**

Strings: `["b", "a", "aa", "ab", "ba"]`, k=3

Build Trie with counts:

```

         root
        /    \
      a(3)   b(2)
      / \     |

a(1) b(1) a(1)
END END END
END

````

Counts indicate strings in subtree:

- Node 'a' has count=3 (strings: "a", "aa", "ab")
- Node 'b' has count=2 (strings: "b", "ba")

Find k=3:

1. Start at root, k=3
2. Check 'a' subtree (count=3):
   - 3 >= 3, so answer is in this subtree
3. Enter 'a' node:
   - Is END → k=2 (found "a", but not target yet)
   - Check 'a' child (count=1):
     - 1 < 2, skip (k -= 1, k=1)
   - Check 'b' child (count=1):
     - 1 >= 1, enter
4. At 'ab' node:
   - Is END → k=0 → Return "ab"

Result: "ab" (the 3rd string: ["a", "aa", "ab", "b", "ba"])

![Algorithm Visualization](../images/TRI-016/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new TreeMap<>();  // TreeMap for alphabetical order
    boolean isEnd = false;
    int count = 0;  // Number of strings in this subtree
}

class Solution {
    private TrieNode root = new TrieNode();
    private String result = "";
    private int remaining;

    public String kthSmallest(String[] words, int k) {
        // Build trie with counts
        for (String word : words) {
            insert(word);
        }

        remaining = k;
        dfs(root, new StringBuilder());

        return result;
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
            node.count++;
        }
        node.isEnd = true;
    }

    private boolean dfs(TrieNode node, StringBuilder path) {
        if (node.isEnd) {
            remaining--;
            if (remaining == 0) {
                result = path.toString();
                return true;
            }
        }

        // Traverse children in alphabetical order (TreeMap ensures this)
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            char c = entry.getKey();
            TrieNode child = entry.getValue();

            // Check if k-th string is in this subtree
            if (child.count >= remaining) {
                path.append(c);
                if (dfs(child, path)) {
                    return true;
                }
                path.deleteCharAt(path.length() - 1);
            } else {
                // Skip this entire subtree
                remaining -= child.count;
            }
        }

        return false;
    }
}

public class Main {
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
````

### Python

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Will maintain alphabetical order through sorted()
        self.is_end = False
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.result = ""
        self.remaining = 0

    def kth_smallest(self, words: List[str], k: int) -> str:
        # Build trie with counts
        for word in words:
            self._insert(word)

        self.remaining = k
        self._dfs(self.root, [])

        return self.result

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def _dfs(self, node: TrieNode, path: List[str]) -> bool:
        if node.is_end:
            self.remaining -= 1
            if self.remaining == 0:
                self.result = ''.join(path)
                return True

        # Traverse children in alphabetical order
        for char in sorted(node.children.keys()):
            child = node.children[char]

            if child.count >= self.remaining:
                path.append(char)
                if self._dfs(child, path):
                    return True
                path.pop()
            else:
                self.remaining -= child.count

        return False

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

struct TrieNode {
    map<char, TrieNode*> children;  // map maintains alphabetical order
    bool isEnd = false;
    int count = 0;
};

class Solution {
private:
    TrieNode* root;
    string result;
    int remaining;

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->count++;
        }
        node->isEnd = true;
    }

    bool dfs(TrieNode* node, string& path) {
        if (node->isEnd) {
            remaining--;
            if (remaining == 0) {
                result = path;
                return true;
            }
        }

        for (auto& [c, child] : node->children) {
            if (child->count >= remaining) {
                path.push_back(c);
                if (dfs(child, path)) {
                    return true;
                }
                path.pop_back();
            } else {
                remaining -= child->count;
            }
        }

        return false;
    }

public:
    Solution() { root = new TrieNode(); }

    string kthSmallest(vector<string>& words, int k) {
        for (const string& word : words) {
            insert(word);
        }

        remaining = k;
        string path = "";
        dfs(root, path);

        return result;
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

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
    this.count = 0;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.result = "";
    this.remaining = 0;
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
      node.count++;
    }
    node.isEnd = true;
  }

  dfs(node, path) {
    if (node.isEnd) {
      this.remaining--;
      if (this.remaining === 0) {
        this.result = path.join("");
        return true;
      }
    }

    // Sort children for alphabetical order
    const sortedKeys = Array.from(node.children.keys()).sort();

    for (const char of sortedKeys) {
      const child = node.children.get(char);

      if (child.count >= this.remaining) {
        path.push(char);
        if (this.dfs(child, path)) {
          return true;
        }
        path.pop();
      } else {
        this.remaining -= child.count;
      }
    }

    return false;
  }

  kthSmallest(words, k) {
    for (const word of words) {
      this.insert(word);
    }

    this.remaining = k;
    this.dfs(this.root, []);

    return this.result;
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

## Common Mistakes

1. **Not Maintaining Alphabetical Order**: Using HashMap instead of TreeMap/sorted iteration
2. **Off-by-One in k**: Forgetting k is 1-indexed
3. **Incorrect Count Updates**: Not properly counting strings in subtrees
4. **Skipping Logic Error**: Incorrectly subtracting counts when skipping subtrees

## Related Concepts

- Trie Data Structure
- Lexicographic Order
- DFS Traversal
- Kth Element Problems
- Order Statistics
