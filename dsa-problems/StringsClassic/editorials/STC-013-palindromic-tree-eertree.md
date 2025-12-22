---
problem_id: STC_PALINDROMIC_TREE_EERTREE__2893
display_id: STC-013
slug: palindromic-tree-eertree
title: "Palindromic Tree (Eertree) Construction"
difficulty: Hard
difficulty_score: 68
topics:
  - Strings
  - Palindromes
  - Eertree
tags:
  - strings
  - palindromes
  - eertree
  - hard
premium: true
subscription_tier: basic
---

# STC-013: Palindromic Tree (Eertree) Construction

## 📋 Problem Summary

Given a string `s`, you need to count the number of **distinct** palindromic substrings. You are expected to solve this using a **Palindromic Tree** (also known as an **Eertree**).

## 🌍 Real-World Scenario

**Scenario Title:** RNA Structure Prediction

In bioinformatics, RNA molecules often fold back on themselves to form structures like "hairpins" or "stem-loops". These structures are essentially palindromic sequences (in the biological sense of complementarity). Identifying all distinct palindromic substructures is a key step in predicting the secondary structure of RNA, which determines its function. The Eertree provides a compact representation of all such potential folding sites.

**Why This Problem Matters:**

- **Efficiency:** While Manacher's algorithm finds the longest palindrome centered at each position, the Eertree explicitly stores every *unique* palindrome, making it easier to query properties like "how many times does palindrome X appear?".
- **Compression:** Palindromic factorization is a technique used in text compression.

![Real-World Application](../images/STC-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "aba"`.
Eertree Structure:
- **Root 1 (Odd Root):** Length -1. Suffix Link: 1.
- **Root 2 (Even Root):** Length 0. Suffix Link: 1.

Processing `s`:
1. Add 'a':
   - Longest palindrome ending at index 0 is "a".
   - Create node "a" (len 1). Parent: Root 1. Link: Root 2.
2. Add 'b':
   - Longest palindrome ending at index 1 is "b".
   - Create node "b" (len 1). Parent: Root 1. Link: Root 2.
3. Add 'a':
   - Longest palindrome ending at index 2 is "aba".
   - Create node "aba" (len 3). Parent: Node "b". Link: Node "a".

Nodes created: "a", "b", "aba". Count = 3.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Distinct:** "aba" contains "a" twice, but "a" is counted only once.
- **Roots:** The tree has two imaginary roots (len -1 and len 0). Do not count them in the final answer.
- **Complexity:** O(N) time and space is required.

## Naive Approach

### Intuition

Generate all substrings, check if each is a palindrome, and store in a Set.

### Algorithm

1. `Set<String> distinctPalindromes`
2. Iterate all substrings.
3. If `isPalindrome(substring)`, add to Set.
4. Return Set size.

### Time Complexity

- **O(N^3)**: Generating substrings O(N^2), checking palindrome O(N).
- Too slow.

## Optimal Approach (Eertree)

### Key Insight

A string of length `N` has at most `N` distinct palindromic substrings.
The **Eertree** is a data structure where each node represents a unique palindrome.
- **Edges:** Transition `(u, c)` means adding character `c` to both sides of palindrome `u`. `new_palindrome = c + u + c`.
- **Suffix Link:** `link[u]` points to the longest proper palindromic suffix of `u`.
- **Roots:**
  - **Odd Root:** Represents an imaginary palindrome of length -1. Used to generate odd-length palindromes (e.g., "a" is `a + "" + a` where center is len -1? No, "a" is `a + (len -1) + a`? Actually, edge from -1 with 'a' creates "a" of len 1).
  - **Even Root:** Represents empty string of length 0. Used to generate even-length palindromes (e.g., "aa" is `a + "" + a`).

### Algorithm

1. Initialize `tree` with two roots: node 0 (len -1) and node 1 (len 0).
2. `link[0] = 0`, `link[1] = 0`.
3. `last = 1` (index of the longest palindromic suffix of the currently processed prefix).
4. For each character `c` in `s` at index `i`:
   - Traverse suffix links from `last` to find a node `curr` such that `s[i - len[curr] - 1] == s[i]`.
   - If node `curr` already has a child with char `c`, update `last` to that child.
   - Else, create a new node `newNode`:
     - `len[newNode] = len[curr] + 2`.
     - Find its suffix link: traverse links from `link[curr]` to find `temp` such that `s[i - len[temp] - 1] == s[i]`.
     - `link[newNode] = tree[temp].children[c]`.
     - Add `newNode` as child of `curr`.
     - `last = newNode`.
     - Increment distinct count.

### Time Complexity

- **O(N)**: Amortized analysis shows we traverse suffix links a total of O(N) times.

### Space Complexity

- **O(N * Sigma)**: Where Sigma is alphabet size (26).

![Algorithm Visualization](../images/STC-013/algorithm-visualization.png)
![Algorithm Steps](../images/STC-013/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        int len;
        int link;
        Map<Character, Integer> next = new HashMap<>();

        Node(int len, int link) {
            this.len = len;
            this.link = link;
        }
    }

    public int countDistinctPalindromes(String s) {
        List<Node> tree = new ArrayList<>();
        // Node 0: root with len -1 (odd root)
        tree.add(new Node(-1, 0));
        // Node 1: root with len 0 (even root)
        tree.add(new Node(0, 0));
        
        int last = 1; // Start at even root (empty string)
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            int curr = last;
            
            // Find the longest palindromic suffix of s[0...i-1] that can be extended with c
            while (true) {
                int len = tree.get(curr).len;
                if (i - 1 - len >= 0 && s.charAt(i - 1 - len) == c) {
                    break;
                }
                curr = tree.get(curr).link;
            }
            
            if (tree.get(curr).next.containsKey(c)) {
                last = tree.get(curr).next.get(c);
                continue;
            }
            
            // Create new node
            int newNodeIdx = tree.size();
            tree.add(new Node(tree.get(curr).len + 2, 0));
            tree.get(curr).next.put(c, newNodeIdx);
            
            // Find suffix link for new node
            if (tree.get(newNodeIdx).len == 1) {
                tree.get(newNodeIdx).link = 1; // Link to even root
            } else {
                int temp = tree.get(curr).link;
                while (true) {
                    int len = tree.get(temp).len;
                    if (i - 1 - len >= 0 && s.charAt(i - 1 - len) == c) {
                        break;
                    }
                    temp = tree.get(temp).link;
                }
                tree.get(newNodeIdx).link = tree.get(temp).next.get(c);
            }
            
            last = newNodeIdx;
        }
        
        return tree.size() - 2; // Exclude the two roots
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.countDistinctPalindromes(s));
        }
        sc.close();
    }
}
```

### Python

```python
class Node:
    def __init__(self, length, link):
        self.len = length
        self.link = link
        self.next = {}

def count_distinct_palindromes(s: str) -> int:
    # Node 0: len -1 (odd root), link 0
    # Node 1: len 0 (even root), link 0
    tree = [Node(-1, 0), Node(0, 0)]
    last = 1
    n = len(s)
    
    for i in range(n):
        char_code = s[i]
        curr = last
        
        # Find node to extend
        while True:
            length = tree[curr].len
            if i - 1 - length >= 0 and s[i - 1 - length] == char_code:
                break
            curr = tree[curr].link
            
        if char_code in tree[curr].next:
            last = tree[curr].next[char_code]
            continue
            
        # Create new node
        new_node_idx = len(tree)
        tree.append(Node(tree[curr].len + 2, 0))
        tree[curr].next[char_code] = new_node_idx
        
        # Find suffix link
        if tree[new_node_idx].len == 1:
            tree[new_node_idx].link = 1
        else:
            temp = tree[curr].link
            while True:
                length = tree[temp].len
                if i - 1 - length >= 0 and s[i - 1 - length] == char_code:
                    break
                temp = tree[temp].link
            tree[new_node_idx].link = tree[temp].next[char_code]
            
        last = new_node_idx
        
    return len(tree) - 2

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(count_distinct_palindromes(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

struct Node {
    int len;
    int link;
    map<char, int> next;
    
    Node(int l = 0, int lnk = 0) : len(l), link(lnk) {}
};

class Solution {
public:
    int countDistinctPalindromes(const string& s) {
        vector<Node> tree;
        tree.emplace_back(-1, 0); // Node 0: odd root
        tree.emplace_back(0, 0);  // Node 1: even root
        
        int last = 1;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            char c = s[i];
            int curr = last;
            
            while (true) {
                int len = tree[curr].len;
                if (i - 1 - len >= 0 && s[i - 1 - len] == c) {
                    break;
                }
                curr = tree[curr].link;
            }
            
            if (tree[curr].next.count(c)) {
                last = tree[curr].next[c];
                continue;
            }
            
            int newNodeIdx = tree.size();
            tree.emplace_back(tree[curr].len + 2, 0);
            tree[curr].next[c] = newNodeIdx;
            
            if (tree[newNodeIdx].len == 1) {
                tree[newNodeIdx].link = 1;
            } else {
                int temp = tree[curr].link;
                while (true) {
                    int len = tree[temp].len;
                    if (i - 1 - len >= 0 && s[i - 1 - len] == c) {
                        break;
                    }
                    temp = tree[temp].link;
                }
                tree[newNodeIdx].link = tree[temp].next[c];
            }
            
            last = newNodeIdx;
        }
        
        return tree.size() - 2;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.countDistinctPalindromes(s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Node {
  constructor(len, link) {
    this.len = len;
    this.link = link;
    this.next = new Map();
  }
}

class Solution {
  countDistinctPalindromes(s) {
    const tree = [];
    tree.push(new Node(-1, 0)); // Node 0: odd root
    tree.push(new Node(0, 0));  // Node 1: even root
    
    let last = 1;
    const n = s.length;
    
    for (let i = 0; i < n; i++) {
      const c = s[i];
      let curr = last;
      
      while (true) {
        const len = tree[curr].len;
        if (i - 1 - len >= 0 && s[i - 1 - len] === c) {
          break;
        }
        curr = tree[curr].link;
      }
      
      if (tree[curr].next.has(c)) {
        last = tree[curr].next.get(c);
        continue;
      }
      
      const newNodeIdx = tree.length;
      tree.push(new Node(tree[curr].len + 2, 0));
      tree[curr].next.set(c, newNodeIdx);
      
      if (tree[newNodeIdx].len === 1) {
        tree[newNodeIdx].link = 1;
      } else {
        let temp = tree[curr].link;
        while (true) {
          const len = tree[temp].len;
          if (i - 1 - len >= 0 && s[i - 1 - len] === c) {
            break;
          }
          temp = tree[temp].link;
        }
        tree[newNodeIdx].link = tree[temp].next.get(c);
      }
      
      last = newNodeIdx;
    }
    
    return tree.length - 2;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.countDistinctPalindromes(s).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`s = "aba"`
Roots: `0 (len -1)`, `1 (len 0)`. `last = 1`.

1. `i=0`, `c='a'`:
   - `curr=1`. `s[-1]` invalid. `link[1]=0`.
   - `curr=0`. `s[0 - (-1) - 1] = s[0] = 'a'`. Match!
   - `tree[0]` has no 'a'. Create Node 2 (len 1).
   - `tree[0].next['a'] = 2`.
   - `link[2] = 1` (len 1 links to even root).
   - `last = 2`.
   - Tree: `{-1, 0, "a"}`. Count: 1.

2. `i=1`, `c='b'`:
   - `curr=2` ("a"). `s[1 - 1 - 1] = s[-1]` invalid. `link[2]=1`.
   - `curr=1` (0). `s[1 - 0 - 1] = s[0] = 'a' != 'b'`. `link[1]=0`.
   - `curr=0` (-1). `s[1 - (-1) - 1] = s[1] = 'b'`. Match!
   - Create Node 3 (len 1). `tree[0].next['b'] = 3`.
   - `link[3] = 1`.
   - `last = 3`.
   - Tree: `{-1, 0, "a", "b"}`. Count: 2.

3. `i=2`, `c='a'`:
   - `curr=3` ("b"). `s[2 - 1 - 1] = s[0] = 'a'`. Match!
   - Create Node 4 (len 3). `tree[3].next['a'] = 4`.
   - Link for 4: Start from `link[3]=1`.
     - `curr=1`. `s[2 - 0 - 1] = s[1] = 'b' != 'a'`. `link[1]=0`.
     - `curr=0`. `s[2 - (-1) - 1] = s[2] = 'a'`. Match!
     - `link[4] = tree[0].next['a'] = 2` ("a").
   - `last = 4`.
   - Tree: `{-1, 0, "a", "b", "aba"}`. Count: 3.

Result: 3. Correct.

![Example Visualization](../images/STC-013/example-1.png)

## ✅ Proof of Correctness

### Invariant

Each node in the Eertree corresponds to a unique palindromic substring.
When processing character `s[i]`, we find the longest palindrome ending at `i`.
If this palindrome has been seen before, we just move `last` to the existing node.
If not, we create a new node.
Since we process the string character by character, we encounter every palindrome at its first occurrence (as the longest palindrome ending at that position).
Thus, the number of nodes created (minus roots) is exactly the number of distinct palindromes.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Palindrome Frequency**
  - Maintain a `count` array. When at node `u`, `count[u]++`. After building, propagate counts up suffix links: `count[link[u]] += count[u]` (in reverse topological order).

- **Extension 2: Minimum Factorization**
  - Find min cuts to split string into palindromes. Eertree + DP on suffix links.

## Common Mistakes to Avoid

1. **Roots Initialization**
   - ❌ Forgetting `link[0] = 0` or `link[1] = 0`. Actually `link[0]` should point to itself or be handled such that loop terminates.
   - ✅ `link[0]` is conceptually problematic because `len` is -1. Usually, we ensure the loop condition `s[i - len - 1] == c` always eventually succeeds at root 0 because `s[i - (-1) - 1] = s[i] == s[i]`. So `link[0]` is never followed.

2. **Suffix Link for Len 1**
   - ❌ Trying to find suffix link for len 1 nodes using the loop.
   - ✅ Len 1 nodes always link to the Even Root (0 length).

## Related Concepts

- **Manacher's Algorithm**: Finds longest palindrome centered at each position (O(N)).
- **Suffix Automaton**: Can also count palindromes but much harder.
