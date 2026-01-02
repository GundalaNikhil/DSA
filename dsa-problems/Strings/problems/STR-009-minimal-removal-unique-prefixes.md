---
problem_id: STR_MINIMAL_REMOVAL_UNIQUE_PREFIXES__1009
display_id: STR-009
slug: minimal-removal-unique-prefixes
title: "Minimal Removal for Unique Prefixes"
difficulty: Medium
difficulty_score: 45
topics:
  - String Manipulation
  - Trie
  - Greedy
tags:
  - prefix-conflict
  - deletion
  - trie-structure
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-009: Minimal Removal for Unique Prefixes

## Problem Statement

Given an integer `L` and `n` strings, delete the minimum total number of characters (only from the ends of strings) so that all resulting strings have distinct prefixes of length `L`.

## Input Format

- First line: Integer `L` (1 ≤ L ≤ 20)
- Second line: Integer `n` (1 ≤ n ≤ 2 × 10^5)
- Next n lines: One string per line (total length ≤ 2 × 10^5)

## Output Format

- A single integer representing minimum deletions

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `1 ≤ L ≤ 20`
- Total string length ≤ `2 × 10^5`

## Example 1

**Input:**

```
2
3
ab
ac
ad
```

**Output:**

```
0
```

**Explanation:**

- All prefixes already distinct: "ab", "ac", "ad"

## Example 2

**Input:**

```
2
3
abc
abd
acc
```

**Output:**

```
2
```

**Explanation:**

- Prefixes: "ab", "ab", "ac" → conflict on first two
- Delete 2 chars from "abd" → "a" (prefix length < L)
- Result prefixes: "ab", "a", "ac" (all distinct)

## Notes

- Use trie to identify prefix conflicts
- Greedy: keep longest string in each conflict group
- Deletion formula: len(s) - (L-1) for conflicts

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    List<String> strings = new ArrayList<>();
}

class Solution {
    private int totalDeletions = 0;

    public int minimalRemovalUniquePrefixes(int L, List<String> strings) {
        return 0;
    }

    private void findConflicts(TrieNode node, int depth, int L) {
        if (depth == L) {
            if (node.strings.size() > 1) {
                // Sort by length descending
                node.strings.sort((a, b) -> Integer.compare(b.length(), a.length()));

                // Delete all except longest
                for (int i = 1; i < node.strings.size(); i++) {
                    String s = node.strings.get(i);
                    if (s.length() >= L) {
                        totalDeletions += s.length() - (L - 1);
                    }
                }
            }
            return;
        }

        for (TrieNode child : node.children.values()) {
            findConflicts(child, depth + 1, L);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        int strings_n = sc.nextInt();
        List<String> strings = new ArrayList<>();
        for(int i=0; i<strings_n; i++) strings.add(sc.next());
        Solution sol = new Solution();
        System.out.println(sol.minimalRemovalUniquePrefixes(L, strings));
        sc.close();
    }
}
```

### Python

```python
class TrieNode:
    def __init__(self):
        return 0
def minimal_removal_unique_prefixes(L: int, strings: list[str]) -> int:
    return 0
def main():
    import sys

    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if not parts:
        return
        
    iterator = iter(parts)
    try:
        L = int(next(iterator))
        N = int(next(iterator))
        strings = []
        for _ in range(N):
            strings.append(next(iterator))
            
        print(minimal_removal_unique_prefixes(L, strings))
    except StopIteration:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    vector<string> strings;
};

class Solution {
public:
    int minimalRemovalUniquePrefixes(int L, vector<string>& strings) {
        return 0;
    }

private:
    void findConflicts(TrieNode* node, int depth, int L, int& totalDeletions) {
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int L; cin >> L;
    int strings_n; cin >> strings_n; vector<string> strings(strings_n); for(int i=0; i<strings_n; i++) cin >> strings[i];
    Solution sol;
    cout << sol.minimalRemovalUniquePrefixes(L, strings) << endl;
    return 0;
}
```

### JavaScript

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.strings = [];
  }
}

function minimalRemovalUniquePrefixes(L, strings) {
    return 0;
  }
  function findConflicts(node, depth) {
    return 0;
  }

  findConflicts(root, 0);
  return totalDeletions;
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const L = parseInt(tokens[ptr++]);
    const strings_n = parseInt(tokens[ptr++]);
    const strings = [];
    for(let i=0; i<strings_n; i++) strings.push(tokens[ptr++]);
    console.log(minimalRemovalUniquePrefixes(L, strings));
});
```

