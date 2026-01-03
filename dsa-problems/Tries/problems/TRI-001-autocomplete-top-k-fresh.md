---
problem_id: TRI_AUTOCOMPLETE_DECAY__7294
display_id: TRI-001
slug: autocomplete-top-k-fresh
title: "Autocomplete Top-K with Freshness Decay"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - Priority Queue
  - Hash Table
  - Sorting
tags:
  - trie
  - heap
  - autocomplete
  - ranking
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-001: Autocomplete Top-K with Freshness Decay

## Problem Statement

Build a trie of lowercase words, each with a base frequency and last-used timestamp. Given the current time and a prefix, return the top `k` words ranked by a freshness decay score calculated as:

**score = frequency × exp(-(currentTime - lastUsed) / D)**

where `D` is a decay constant. If scores are equal, rank lexicographically.

![Problem Illustration](../images/TRI-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains `word frequency timestamp`
  - `word`: lowercase string
  - `frequency`: integer representing base popularity
  - `timestamp`: integer representing last access time
- Next line: `prefix currentTime D k`
  - `prefix`: query prefix (lowercase)
  - `currentTime`: current timestamp
  - `D`: decay constant
  - `k`: number of results to return

## Output Format

Return a list of the top `k` words matching the prefix, sorted by:

1. Decayed score (descending)
2. Lexicographic order (ascending) for ties

Format: `["word1", "word2", ...]`

## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= frequency <= 10^6`
- `0 <= timestamp, currentTime <= 10^9`
- `1 <= D <= 10^9` (decay constant)
- `1 <= k <= 10`
- All words are lowercase English letters

## Example

**Input:**

```
3
hello 5 0
helium 3 5
he 4 9
he 10 10 2
```

**Output:**

```
["he", "hello"]
```

**Explanation:**

Words with prefix "he": hello, helium, he

Calculate decayed scores at currentTime=10 with D=10:

- "hello": 5 × exp(-(10-0)/10) = 5 × exp(-1) ≈ 5 × 0.368 = 1.84
- "helium": 3 × exp(-(10-5)/10) = 3 × exp(-0.5) ≈ 3 × 0.606 = 1.82
- "he": 4 × exp(-(10-9)/10) = 4 × exp(-0.1) ≈ 4 × 0.905 = 3.62

Sorted by score (descending): "he" (3.62), "hello" (1.84), "helium" (1.82)

Top k=2 results: ["he", "hello"]

![Example Visualization](../images/TRI-001/example-1.png)

## Notes

- The exponential decay formula ensures recently used words rank higher
- Smaller `D` values create stronger recency bias
- If no words match the prefix, return an empty list
- Exact floating-point precision is not required; standard library `exp()` is sufficient

## Related Topics

Trie, Priority Queue, Hash Table, Sorting, Autocomplete Systems

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

class WordMetadata {
    int frequency;
    int lastUsed;

    WordMetadata(int freq, int time) {
        this.frequency = freq;
        this.lastUsed = time;
    }
}

class Solution {
    private TrieNode root = new TrieNode();
    private Map<String, WordMetadata> metadata = new HashMap<>();

    public void insertWord(String word, int frequency, int timestamp) {
        //Implement here
    }

    public List<String> autocomplete(String prefix, int currentTime, int D, int k) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // Number of words
        Solution solution = new Solution();

        for (int i = 0; i < n; i++) {
            String word = sc.next();
            int freq = sc.nextInt();
            int time = sc.nextInt();
            solution.insertWord(word, freq, time);
        }

        String prefix = sc.next();
        int currentTime = sc.nextInt();
        int D = sc.nextInt();
        int k = sc.nextInt();

        List<String> result = solution.autocomplete(prefix, currentTime, D, k);
        // Output in Python list format with single quotes
        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print("'" + result.get(i) + "'");
            if (i < result.size() - 1) System.out.print(", ");
        }
        System.out.println("]");

        sc.close();
    }
}
```

### Python

```python
import math
from typing import List, Tuple
from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.metadata = {}  # word -> (frequency, lastUsed)

    def insert_word(self, word: str, frequency: int, timestamp: int):
        # //Implement here
        pass

    def autocomplete(self, prefix: str, current_time: int, D: int, k: int) -> List[str]:
        # //Implement here
        return []
def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    idx = 0

    n = int(input_data[idx])
    idx += 1

    solution = Solution()
    for _ in range(n):
        word = input_data[idx]
        freq = int(input_data[idx + 1])
        time = int(input_data[idx + 2])
        idx += 3
        solution.insert_word(word, freq, time)

    prefix = input_data[idx]
    current_time = int(input_data[idx + 1])
    D = int(input_data[idx + 2])
    k = int(input_data[idx + 3])

    result = solution.autocomplete(prefix, current_time, D, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord = false;
};

struct WordMetadata {
    int frequency;
    int lastUsed;
};

struct WordScore {
    string word;
    double score;

    bool operator<(const WordScore& other) const {
        if (abs(score - other.score) > 1e-9) {
            return score < other.score; // Max-heap by score
        }
        return word > other.word; // Min-heap by lexicographic
    }
};

class Solution {
private:
    TrieNode* root;
    unordered_map<string, WordMetadata> metadata;

public:
    Solution() : root(new TrieNode()) {}

    void insertWord(string word, int frequency, int timestamp) {
        //Implement here
    }

    vector<string> autocomplete(string prefix, int currentTime, int D, int k) {
        //Implement here
        return {};
    }
};

int main() {
    int n;
    cin >> n;

    Solution solution;
    for (int i = 0; i < n; i++) {
        string word;
        int freq, time;
        cin >> word >> freq >> time;
        solution.insertWord(word, freq, time);
    }

    string prefix;
    int currentTime, D, k;
    cin >> prefix >> currentTime >> D >> k;

    vector<string> result = solution.autocomplete(prefix, currentTime, D, k);

    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << "'" << result[i] << "'";
        if (i < result.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEndOfWord = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.metadata = new Map();
  }

  insertWord(word, frequency, timestamp) {
    //Implement here
  }

  autocomplete(prefix, currentTime, D, k) {
    //Implement here
    return [];
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
  const tokens = lines.join(" ").split(/\s+/);
  let idx = 0;

  const n = parseInt(tokens[idx++]);
  const solution = new Solution();

  for (let i = 0; i < n; i++) {
    const word = tokens[idx++];
    const freq = parseInt(tokens[idx++]);
    const time = parseInt(tokens[idx++]);
    solution.insertWord(word, freq, time);
  }

  const prefix = tokens[idx++];
  const currentTime = parseInt(tokens[idx++]);
  const D = parseInt(tokens[idx++]);
  const k = parseInt(tokens[idx++]);

  const result = solution.autocomplete(prefix, currentTime, D, k);
  // Output in Python list format with single quotes
  console.log('[' + result.map(s => "'" + s + "'").join(', ') + ']');
});
```
