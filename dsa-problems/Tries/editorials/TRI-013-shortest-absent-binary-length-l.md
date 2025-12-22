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
---

# TRI-013: Shortest Absent Binary String of Length L

## 📋 Problem Summary

Given a set of binary strings all of length exactly `L`, find the lexicographically smallest binary string of length `L` that is NOT present in the set. If all possible strings of length `L` exist, return empty string.

## 🌍 Real-World Scenario

**Binary Code Generation & Error Detection**

Imagine you're developing a firmware validation system for IoT devices. Each device has a unique 8-bit binary identifier, and you need to assign identifiers to new devices. Your system must:

- Quickly find the smallest available identifier (in lexicographic order)
- Ensure no duplicates exist in the system
- Handle the case where all 256 possible 8-bit codes are assigned

For example, if your database contains device IDs: `["00000000", "00000001", "00000011"]`, the next available ID should be `"00000010"` (the lexicographically smallest missing code).

**Industry Applications:**

1. **Error-Correcting Codes**: Finding missing codewords in Hamming codes or other error-detection schemes
2. **Test Case Generation**: Systematically generating missing test patterns in digital circuit testing
3. **Hash Table Probing**: Finding empty slots in hash tables using binary representations
4. **Network Packet Sequencing**: Identifying missing packet sequence numbers in binary form

This problem is fundamental in **coding theory**, where prefix-free binary codes must be complete yet identifiable.

![Real-World Application](../images/TRI-013/real-world-scenario.png)

## Detailed Explanation

**Problem Breakdown:**

Given a set of binary strings all with the same length `L`:

- We need to find the first binary string (in lexicographic order) of length `L` that isn't in the set
- Lexicographic order for binary: "00" < "01" < "10" < "11"
- If all 2^L possible strings exist, return empty string

**Key Insights:**

1. There are exactly 2^L possible binary strings of length L
2. If the set has 2^L elements, all possibilities are covered → return ""
3. Otherwise, we need to find the first missing one in lexicographic order
4. A trie is perfect for this: traverse in lexicographic order (left child '0' before right child '1')

**Example Walkthrough:**

Input: `L=2`, set = `{"00", "01"}`

All possible binary strings of length 2: `["00", "01", "10", "11"]`

Set contains: `{"00", "01"}`
Missing: `{"10", "11"}`

Lexicographically smallest missing: `"10"`

**Trie Visualization:**

```
         root
        /    \
      0(✓)   1(✗)
      /  \    /  \
    0(✓) 1(✓) 0   1
    END  END
```

Traversal in lexicographic order:

- Try "00": Exists ✓
- Try "01": Exists ✓
- Try "10": Missing! ✗ → Return "10"

![Problem Illustration](../images/TRI-013/problem-illustration.png)

## Naive Approach

**Intuition:**

Generate all possible binary strings of length L in lexicographic order and check each against the set.

**Algorithm:**

1. Generate all 2^L binary strings of length L
2. Store the given set in a HashSet for O(1) lookup
3. Iterate through all possibilities in order
4. Return the first one not in the set

**Time Complexity:** O(2^L × L)

- Generate all 2^L strings: O(2^L)
- Each string comparison/generation: O(L)

**Space Complexity:** O(n × L) for the HashSet where n = size of input set

**Limitations:**

- **Exponential Time**: For L=20, we check up to 1,048,576 strings!
- **Memory Intensive**: Must store all possibilities or check repeatedly
- **Wasteful**: We know some strings exist, yet we check them anyway

## Optimal Approach

**Key Insight:**

Use a **binary trie** to store existing strings, then perform a **DFS traversal in lexicographic order** to find the first missing path of length L.

**Binary Trie DFS:**

```
Example: inserted = ["00", "01", "11"], L = 2

Binary Trie:
         Root
        /    \
      0       1
     / \       \
    0✓ 1✓      1✓
   (00)(01)   (11)

All possible strings of length 2: {00, 01, 10, 11}
Present: {00, 01, 11}
Missing: {10}

DFS Traversal (lexicographic order):
1. Try path 0→0: Present ✓ (continue searching)
2. Try path 0→1: Present ✓ (continue searching)
3. Try path 1→0: Missing! ✗
   └─ Node '1' exists, but child '0' missing
   └─ Return "10" ✓

Larger example: inserted = ["000", "001", "010", "100"], L = 3

         Root
        /    \
      0       1
     / \       \
    0   1       0
   /\   |       |
  0✓ 1✓ 0✓     0✓
 000 001 010   100

DFS finds first missing:
  0→0→0 ✓, 0→0→1 ✓, 0→1→0 ✓, 0→1→1 ✗ → "011"

Result: "011" (first missing in lexicographic order)
```

**Algorithm:**

1. **Build Binary Trie**:

   - Insert all strings into trie
   - Each node has at most 2 children: '0' (left) and '1' (right)
   - Mark end nodes at depth L

2. **DFS Search for Missing String**:

   - Start from root with empty path
   - At each level (depth < L):
     - Try '0' child first (lexicographically smaller)
     - If '0' child doesn't exist, we found missing path → append '0's to reach length L
     - If '0' child exists, recursively explore it
     - If '0' subtree fully explored without finding missing, try '1' child
   - If we reach depth L and node is not marked as end → missing string found
   - If all paths explored → return ""

3. **Early Termination**:
   - If input size = 2^L, immediately return "" (all slots filled)

**Time Complexity:** O(n × L + L)

- Building trie: O(n × L) where n = number of strings
- DFS search: O(L) in best case, O(2^L) worst case but typically much faster
- **Practical**: O(n × L) since we find missing string quickly

**Space Complexity:** O(n × L) for the trie

**Why This Is Optimal:**

- **Avoids Redundant Checks**: We don't check strings we know exist
- **Lexicographic Order**: DFS naturally explores in correct order (left before right)
- **Early Exit**: Returns immediately upon finding first missing string
- **Efficient Lookup**: Trie provides O(L) path existence checks

**Example Execution:**

Input: `L=3`, set = `{"000", "001", "010", "100"}`

Build Trie:

```
           root
          /    \
        0       1
       / \      |
      0   1     0
     / \  |     |
    0   1 0     0
    E   E E     E
```

(E = End marker)

DFS Search:

1. Start at root, path = ""
2. Try '0' → exists, recurse with path = "0"
3. Try '00' → exists, recurse with path = "00"
4. Try '000' → exists (END), backtrack
5. Try '001' → exists (END), backtrack
6. Back to '0', try '01' → exists, recurse with path = "01"
7. Try '010' → exists (END), backtrack
8. Try '011' → NOT exists! → Return "011"

Result: `"011"`

![Algorithm Visualization](../images/TRI-013/algorithm-visualization.png)

## Implementations

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
        // Early exit if all possible strings exist
        if (binaryStrings.length == Math.pow(2, L)) {
            return "";
        }

        // Build trie
        for (String s : binaryStrings) {
            insert(s);
        }

        // DFS to find first missing
        return dfs(root, "", L);
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
        self.children = [None, None]  # Index 0 for '0', index 1 for '1'
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def find_shortest_absent(self, binary_strings: List[str], L: int) -> str:
        # Early exit if all possible strings exist
        if len(binary_strings) == 2 ** L:
            return ""

        # Build trie
        for s in binary_strings:
            self._insert(s)

        # DFS to find first missing
        return self._dfs(self.root, "", L)

    def _insert(self, s: str):
        node = self.root
        for char in s:
            idx = int(char)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def _dfs(self, node: TrieNode, path: str, L: int) -> str:
        # Reached target length
        if len(path) == L:
            return None if node.is_end else path

        # Try '0' first (lexicographically smaller)
        if node.children[0] is None:
            # Missing '0' path - fill rest with '0's
            return path + '0' * (L - len(path))

        result = self._dfs(node.children[0], path + '0', L)
        if result is not None:
            return result

        # Try '1'
        if node.children[1] is None:
            # Missing '1' path - fill rest with '0's
            return path + '1' + '0' * (L - len(path) - 1)

        return self._dfs(node.children[1], path + '1', L)

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
        TrieNode* node = root;
        for (char c : s) {
            int idx = c - '0';
            if (node->children[idx] == nullptr) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    string dfs(TrieNode* node, string path, int L) {
        if (path.length() == L) {
            return node->isEnd ? "" : path;
        }

        // Try '0' first
        if (node->children[0] == nullptr) {
            return path + string(L - path.length(), '0');
        }

        string result = dfs(node->children[0], path + '0', L);
        if (!result.empty()) return result;

        // Try '1'
        if (node->children[1] == nullptr) {
            return path + '1' + string(L - path.length() - 1, '0');
        }

        return dfs(node->children[1], path + '1', L);
    }

public:
    Solution() { root = new TrieNode(); }

    string findShortestAbsent(vector<string>& binaryStrings, int L) {
        if (binaryStrings.size() == pow(2, L)) {
            return "";
        }

        for (const string& s : binaryStrings) {
            insert(s);
        }

        return dfs(root, "", L);
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
    let node = this.root;
    for (const char of s) {
      const idx = parseInt(char);
      if (node.children[idx] === null) {
        node.children[idx] = new TrieNode();
      }
      node = node.children[idx];
    }
    node.isEnd = true;
  }

  dfs(node, path, L) {
    if (path.length === L) {
      return node.isEnd ? null : path;
    }

    // Try '0' first
    if (node.children[0] === null) {
      return path + "0".repeat(L - path.length);
    }

    let result = this.dfs(node.children[0], path + "0", L);
    if (result !== null) return result;

    // Try '1'
    if (node.children[1] === null) {
      return path + "1" + "0".repeat(L - path.length - 1);
    }

    return this.dfs(node.children[1], path + "1", L);
  }

  findShortestAbsent(binaryStrings, L) {
    if (binaryStrings.length === Math.pow(2, L)) {
      return "";
    }

    for (const s of binaryStrings) {
      this.insert(s);
    }

    return this.dfs(this.root, "", L) || "";
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

### Common Mistakes

1. **Not Handling Full Coverage**: Forgetting to check if all 2^L strings exist
2. **Incorrect Lexicographic Order**: Trying '1' before '0' in DFS
3. **Not Filling to Length L**: Returning partial path instead of completing with '0's
4. **Off-by-One in Depth**: Confusing depth/length calculations

## Related Concepts

- Binary Trie
- Lexicographic Ordering
- Coding Theory
- Missing Number Problems
- DFS Traversal
