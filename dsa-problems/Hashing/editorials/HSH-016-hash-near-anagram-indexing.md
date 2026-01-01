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
---

# HSH-016: Hash-Based Near-Anagram Indexing

## 📋 Problem Summary

You are given a list of words. Two words are considered "connected" if they can become anagrams of each other by removing exactly one character from each.
Find the number of connected groups (connected components) of words.

## 🌍 Real-World Scenario

**Scenario Title:** Fuzzy Search for Typos

Imagine a search engine trying to group similar search queries.
- User A types "apple".
- User B types "aple" (missing 'p').
- User C types "applee" (extra 'e').
- Let's re-read: "remove exactly one character from each".
- "apple" (remove 'p') -> "aple". "aple" (remove 'e') -> "apl". Not anagrams.
- "apple" (remove 'e') -> "appl". "apply" (remove 'y') -> "appl". Connected!
- This models finding words that share a common "root" or "stem" despite minor variations.

![Real-World Application](../images/HSH-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Connection Graph

Words: `["abc", "abd", "ab"]`

1. **"abc"**:
   - Remove 'a' -> "bc"
   - Remove 'b' -> "ac"
   - Remove 'c' -> "ab"

2. **"abd"**:
   - Remove 'a' -> "bd"
   - Remove 'b' -> "ad"
   - Remove 'd' -> "ab"

3. **"ab"**:
   - Remove 'a' -> "b"
   - Remove 'b' -> "a"

**Connections:**
- "abc" generates "ab".
- "abd" generates "ab".
- Since they both generate "ab", they are connected via the intermediate key "ab".
- Note: The problem says "remove 1 from each". So "abc" and "abd" are connected because `abc - c = ab` and `abd - d = ab`.
- "abc" and "ab"? `abc - c = ab`. `ab - ?`. `ab` needs to remove 1 char to become something.
- `ab - b = a`. `ab` is not equal to `a`.
- So "abc" and "ab" are NOT connected directly by this definition.
- But "abc" and "abd" ARE connected.

### Key Concept: Intermediate Hash Keys

Instead of comparing every pair of words (`O(N^2)`), we generate all possible "reduced" forms for each word.
- Word `W` generates reduced forms `R_1, R_2, dots, R_L`.
- Map each reduced form to the list of words that generated it.
- If two words generate the same reduced form, union them.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** List of `N` words.
- **Output:** Number of groups.
- **Constraints:** `N=10^5`, Length `L=30`.
- **Anagram:** Two strings are anagrams if sorting them results in the same string.
- **Strategy:** Sort the reduced forms to canonicalize them.

## Naive Approach

### Intuition

For every pair of words, check if they satisfy the condition.

### Time Complexity

- **O(N^2 * L)**: Too slow.

## Optimal Approach

### Key Insight

Use **Union-Find (Disjoint Set Union)**.
1. Create a DSU structure for `N` words.
2. Use a Map: `String (Sorted Reduced Form) -> List<Integer (Word Index)>`.
3. For each word `i`:
   - Generate all `L` reduced strings (remove char at `k`).
   - Sort the reduced string.
   - Add `i` to the map entry for this sorted string.
4. Iterate through the map. For each key, all indices in the list should be unioned together.
5. Count number of disjoint sets.

### Algorithm

1. Initialize DSU with `N` components.
2. `Map<String, List<Integer>> invertedIndex`.
3. Loop `i` from 0 to `N-1`:
   - `w = words[i]`.
   - Sort `w` to `sortedW`.
   - Loop `j` from 0 to `L-1`:
     - Create `sub = sortedW` without char at `j`.
     - `invertedIndex[sub].add(i)`.
4. For each list in `invertedIndex`:
   - Union all indices in the list (e.g., union `list[0]` with `list[k]`).
5. Return `dsu.count`.

### Time Complexity

- **O(N * L^2 log L)**: Sorting takes `L log L`. We do it `L` times (actually just sort once and remove takes `O(L)`).
- Better: Sort word first (`L log L`). Then removing one char takes `O(L)`. Total `O(N * L)`.
- Map operations: String key length `L`.
- Total: `O(N * L^2)`. With `L=30`, this is very fast.

### Space Complexity

- **O(N * L^2)**: Storing all reduced forms.

![Algorithm Visualization](../images/HSH-016/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    class UnionFind {
        int[] parent;
        int count;
        
        public UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
            count = n;
        }
        
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent[rootX] = rootY;
                count--;
            }
        }
    }
    
    public int countNearAnagramGroups(String[] words) {
        int n = words.length;
        UnionFind uf = new UnionFind(n);
        Map<String, List<Integer>> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            char[] chars = words[i].toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);
            
            // Generate all reduced forms
            // Since word is sorted, removing char at j maintains sorted order mostly
            // but duplicates might exist.
            
            for (int j = 0; j < sortedWord.length(); j++) {
                String reduced = sortedWord.substring(0, j) + sortedWord.substring(j + 1);
                map.putIfAbsent(reduced, new ArrayList<>());
                map.get(reduced).add(i);
            }
        }
        
        for (List<Integer> group : map.values()) {
            int first = group.get(0);
            for (int k = 1; k < group.size(); k++) {
                uf.union(first, group.get(k));
            }
        }
        
        return uf.count;
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
        self.parent = list(range(n))
        self.count = n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            self.count -= 1

class Solution:
    def count_near_anagram_groups(self, words: list) -> int:
        n = len(words)
        uf = UnionFind(n)
        groups = {}
        
        for i, word in enumerate(words):
            sorted_word = "".join(sorted(word))
            length = len(sorted_word)
            
            # Generate reduced forms
            # Using a set to avoid processing duplicate reduced forms for the same word
            # e.g. "aba" -> remove 'a' -> "ba", remove 'a' -> "ba"
            seen_reduced = set()
            
            for j in range(length):
                reduced = sorted_word[:j] + sorted_word[j+1:]
                if reduced in seen_reduced:
                    continue
                seen_reduced.add(reduced)
                
                if reduced not in groups:
                    groups[reduced] = []
                groups[reduced].append(i)
                
        for indices in groups.values():
            first = indices[0]
            for k in range(1, len(indices)):
                uf.union(first, indices[k])
                
        return uf.count

def count_near_anagram_groups(words: list) -> int:
    solver = Solution()
    return solver.count_near_anagram_groups(words)

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
        int n = words.size();
        UnionFind uf(n);
        unordered_map<string, vector<int>> groups;
        
        for (int i = 0; i < n; i++) {
            string sortedWord = words[i];
            sort(sortedWord.begin(), sortedWord.end());
            
            int len = sortedWord.length();
            for (int j = 0; j < len; j++) {
                // Optimization: Skip if same char as previous to avoid duplicate work
                if (j > 0 && sortedWord[j] == sortedWord[j-1]) continue;
                
                string reduced = sortedWord.substr(0, j) + sortedWord.substr(j + 1);
                groups[reduced].push_back(i);
            }
        }
        
        for (auto& entry : groups) {
            vector<int>& indices = entry.second;
            if (indices.empty()) continue;
            int first = indices[0];
            for (size_t k = 1; k < indices.size(); k++) {
                uf.unite(first, indices[k]);
            }
        }
        
        return uf.count;
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
    const n = words.length;
    const uf = new UnionFind(n);
    const groups = new Map();
    
    for (let i = 0; i < n; i++) {
      const chars = words[i].split('').sort();
      const sortedWord = chars.join('');
      const len = sortedWord.length;
      
      for (let j = 0; j < len; j++) {
        // Optimization: skip duplicates
        if (j > 0 && sortedWord[j] === sortedWord[j - 1]) continue;
        
        const reduced = sortedWord.substring(0, j) + sortedWord.substring(j + 1);
        if (!groups.has(reduced)) {
          groups.set(reduced, []);
        }
        groups.get(reduced).push(i);
      }
    }
    
    for (const indices of groups.values()) {
      const first = indices[0];
      for (let k = 1; k < indices.length; k++) {
        uf.union(first, indices[k]);
      }
    }
    
    return uf.count;
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `["abcd", "abdc", "abc", "abd"]`

**Processing:**
1. "abcd" (sorted "abcd"):
   - "bcd", "acd", "abd", "abc".
   - Map: `{"bcd":[0], "acd":[0], "abd":[0], "abc":[0]}`
2. "abdc" (sorted "abcd"):
   - "bcd", "acd", "abd", "abc".
   - Map updates: `{"bcd":[0,1], "acd":[0,1], "abd":[0,1], "abc":[0,1]}`
3. "abc" (sorted "abc"):
   - "bc", "ac", "ab".
   - Map updates: `{"bc":[2], "ac":[2], "ab":[2]}`
4. "abd" (sorted "abd"):
   - "bd", "ad", "ab".
   - Map updates: `{"bd":[3], "ad":[3], "ab":[2,3]}`

**Union:**
- From "bcd": Union(0, 1). Group {0, 1}.
- From "ab": Union(2, 3). Group {2, 3}.
- "abc" generates "ab". "abd" generates "ab". So 2 and 3 connected.
- "abcd" generates "abc". "abc" generates... wait.
- "abcd" generates "abc". This "abc" is the *reduced form*.
- Does word "abc" (index 2) connect to reduced form "abc"?
- No. Word "abc" generates "ab", "ac", "bc".
- Word "abcd" generates "abc".
- The reduced form "abc" is just a key.
- Index 0 generates key "abc".
- Does Index 2 generate key "abc"? No.
- So Index 0 and Index 2 are NOT connected via key "abc".
- Are they connected via anything else?
- Index 0: keys {abc, abd, acd, bcd}
- Index 2: keys {ab, ac, bc}
- No common keys.
- So {0, 1} are one group. {2, 3} are another group.
- Total 2 groups. Matches example output.

## ✅ Proof of Correctness

### Invariant
Two words are in the same set if and only if they share a common reduced form.
Transitivity of Union-Find ensures that if A connects to B, and B connects to C, then A connects to C.

## 💡 Interview Extensions

- **Extension 1:** What if we can remove *up to* K characters?
  - *Answer:* Generate all subsequences of length `L-K dots L`. Too slow for large K.
- **Extension 2:** Longest chain of such words?
  - *Answer:* Graph problem (Longest Path in DAG if length decreases, or component size).

### Common Mistakes to Avoid

1. **Sorting**
   - ❌ Wrong: Not sorting the word before generating reduced forms. Anagrams must be canonicalized.
2. **Duplicates**
   - ❌ Wrong: Processing same reduced form multiple times for one word (e.g., "aba" -> "ba", "ba").
   - ✅ Correct: Use a Set or check `s[j] == s[j-1]`.

## Related Concepts

- **BK-Tree:** For fuzzy matching with edit distance.
- **SimHash:** For document similarity.
