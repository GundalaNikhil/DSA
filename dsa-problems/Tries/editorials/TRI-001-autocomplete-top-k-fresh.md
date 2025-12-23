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
---

# TRI-001: Autocomplete Top-K with Freshness Decay

## 📋 Problem Summary

Build a trie-based autocomplete system that ranks search suggestions using a freshness decay formula, combining base frequency with recency to provide the most relevant top-k results for a given prefix.

## 🌍 Real-World Scenario

**Smart Search Engine at E-Commerce Platform**

Imagine you're a software engineer at a major e-commerce platform like Amazon or eBay. Users type search queries millions of times per day, and your job is to build an intelligent autocomplete system that suggests the most relevant products.

Here's the challenge: A product searched frequently 6 months ago ("iPhone 12") might be less relevant today than a newer product ("iPhone 15") searched less often but more recently. Your system needs to balance:

- **Historical popularity**: Products searched frequently should rank higher
- **Recency**: Recently searched items are more relevant
- **User experience**: Results must appear instantly (< 50ms)

The freshness decay formula `score = frequency × exp(-(currentTime - lastUsed)/D)` achieves this perfectly. The decay constant `D` controls how quickly old searches lose relevance:

- Small `D` (e.g., 1 day): Heavy recency bias, great for trending news
- Large `D` (e.g., 30 days): Balances history and recency, ideal for e-commerce

**Why This Problem Matters:**

- **Revenue Impact**: Better autocomplete increases search success rate by 15-25%, directly boosting sales
- **User Retention**: Fast, relevant suggestions keep users engaged and reduce bounce rate
- **Scalability**: Must handle millions of words and thousands of queries per second efficiently

![Real-World Application](../images/TRI-001/real-world-scenario.png)

## Detailed Explanation

This problem combines multiple data structures:

1. **Trie**: Efficiently stores words and enables prefix-based retrieval
2. **Hash Map**: Stores metadata (frequency, timestamp) for each word
3. **Heap/Sorting**: Ranks words by decayed score

The key challenge is computing the decay score efficiently. The exponential decay formula ensures older searches gradually lose relevance while maintaining long-term popularity signals.

**Example Walkthrough:**

Given words: `[(hello, freq=5, t=0), (helium, freq=3, t=5), (he, freq=4, t=9)]`
Current time = 10, Decay constant D = 10, Prefix = "he", k = 2

Calculate decayed scores:

- "hello": 5 × exp(-(10-0)/10) = 5 × exp(-1) ≈ 5 × 0.368 = 1.84
- "helium": 3 × exp(-(10-5)/10) = 3 × exp(-0.5) ≈ 3 × 0.606 = 1.82
- "he": 4 × exp(-(10-9)/10) = 4 × exp(-0.1) ≈ 4 × 0.905 = 3.62

Sorted by score (descending): "he" (3.62), "hello" (1.84), "helium" (1.82)

Top 2: ["he", "hello"]

**Trie with Frequency & Timestamp:**

```
Root
  |
  h
  |
  e (freq=4, lastUsed=9, score=3.62)
  |
  +-- l
      |
      +-- i
      |   |
      |   u
      |   |
      |   m (freq=3, lastUsed=5, score=1.82)
      |
      +-- l
          |
          o (freq=5, lastUsed=0, score=1.84)

Query: prefix="he", currentTime=10, D=10, k=2

Decay Formula: score = freq × e^(-(currentTime - lastUsed)/D)

Matching words traversed from "he" node:
  - "he":     score = 4 × e^(-0.1) = 3.62  ← Rank 1
  - "hello":  score = 5 × e^(-1.0) = 1.84  ← Rank 2 ✓
  - "helium": score = 3 × e^(-0.5) = 1.82  ← Rank 3

Result: ["he", "hello"]
```

## Naive Approach

**Intuition:**

Store all words in a list. For each autocomplete query:

1. Filter words matching the prefix
2. Compute decay score for each
3. Sort by score
4. Return top k

**Algorithm:**

1. Store words with metadata in a list
2. For autocomplete query:
   - Linear scan to find all words with matching prefix
   - Compute decay score for each: `freq × exp(-(currentTime - lastUsed)/D)`
   - Sort results by score (descending), then lexicographically
   - Return top k results

**Time Complexity:** O(N × L + N log N) per query, where N = total words, L = average word length
**Space Complexity:** O(N × L)

**Why This Works:**

- Correctly computes decay scores for all matching words
- Sorting ensures top-k results are accurate
- Simple to implement and understand

**Limitations:**

- **Inefficient prefix matching**: Scanning all N words for every query is wasteful
- **Repeated sorting**: If queries share prefixes, we recompute scores unnecessarily
- **Poor scalability**: With millions of words, each query takes seconds

## Optimal Approach

**Key Insight:**

Use a **Trie** to group words by prefix, enabling O(L) prefix matching instead of O(N). Store metadata in a hash map for O(1) access, and use a min-heap of size k to efficiently track top results.

**TrieNode Structure:**

```
TrieNode:
┌─────────────────────────────────────┐
│  children: dict[char → TrieNode]   │  ← Branch to child nodes
├─────────────────────────────────────┤
│  is_end_of_word: bool               │  ← Marks complete word
└─────────────────────────────────────┘

Word Metadata (separate hash map):
┌──────────────────────────────────────┐
│  word → {frequency, last_used_time}  │
└──────────────────────────────────────┘
```

**Algorithm:**

1. **Build Trie**:

   - Insert all words into trie
   - Store word metadata (frequency, lastUsed) in a hash map keyed by word

2. **Autocomplete Query**:

   - Traverse trie to find node corresponding to prefix (O(P) where P = prefix length)
   - DFS from that node to collect all words with the prefix (O(M) where M = matching words)
   - For each matching word:
     - Retrieve metadata from hash map: O(1)
     - Compute decay score: `freq × exp(-(currentTime - lastUsed)/D)`
   - Use min-heap of size k to track top k scores (O(M log k))
   - Extract results from heap and sort if needed (O(k log k))

3. **Optimization**: Maintain max-heap if multiple queries, or cache results per prefix

**Time Complexity:**

- Trie build: O(N × L)
- Per query: O(P + M log k), where P = prefix length, M = matching words, k = result size
- Space Complexity: O(N × L) for trie + O(N) for hash map

**Why This Is Optimal:**

- **Trie prefix matching**: O(P) instead of O(N) for prefix filtering
- **Heap for top-k**: O(M log k) instead of O(M log M) for full sort
- **Scalable**: With smart trie pruning, can handle millions of words
- **Extensible**: Easy to add features like typo tolerance, synonym expansion

![Algorithm Visualization](../images/TRI-001/algorithm-visualization.png)

## Implementations

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
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
        metadata.put(word, new WordMetadata(frequency, timestamp));
    }

    public List<String> autocomplete(String prefix, int currentTime, int D, int k) {
        // Navigate to prefix node
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return new ArrayList<>(); // No matches
            }
            node = node.children.get(c);
        }

        // Collect all words with this prefix
        List<String> matches = new ArrayList<>();
        collectWords(node, prefix, matches);

        // Compute decay scores
        PriorityQueue<WordScore> heap = new PriorityQueue<>((a, b) -> {
            if (Math.abs(a.score - b.score) > 1e-9) {
                return Double.compare(b.score, a.score); // Descending by score
            }
            return a.word.compareTo(b.word); // Ascending lexicographically
        });

        for (String word : matches) {
            WordMetadata meta = metadata.get(word);
            double decay = Math.exp(-(currentTime - meta.lastUsed) / (double) D);
            double score = meta.frequency * decay;
            heap.offer(new WordScore(word, score));
        }

        // Extract top k
        List<String> result = new ArrayList<>();
        for (int i = 0; i < k && !heap.isEmpty(); i++) {
            result.add(heap.poll().word);
        }

        return result;
    }

    private void collectWords(TrieNode node, String prefix, List<String> result) {
        if (node.isEndOfWord) {
            result.add(prefix);
        }
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            collectWords(entry.getValue(), prefix + entry.getKey(), result);
        }
    }

    static class WordScore {
        String word;
        double score;

        WordScore(String w, double s) {
            word = w;
            score = s;
        }
    }
}

public class Main {
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
        System.out.println(result);

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
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        self.metadata[word] = (frequency, timestamp)

    def autocomplete(self, prefix: str, current_time: int, D: int, k: int) -> List[str]:
        # Navigate to prefix node
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Collect all words with this prefix
        matches = []
        self._collect_words(node, prefix, matches)

        # Compute decay scores
        scores = []
        for word in matches:
            freq, last_used = self.metadata[word]
            decay = math.exp(-(current_time - last_used) / D)
            score = freq * decay
            # Negative score for max-heap behavior, word for lexicographic tie-breaking
            scores.append((-score, word))

        # Sort and get top k
        scores.sort()
        result = [word for _, word in scores[:k]]

        return result

    def _collect_words(self, node: TrieNode, prefix: str, result: List[str]):
        if node.is_end_of_word:
            result.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, result)

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

    void collectWords(TrieNode* node, string prefix, vector<string>& result) {
        if (node->isEndOfWord) {
            result.push_back(prefix);
        }
        for (auto& [ch, child] : node->children) {
            collectWords(child, prefix + ch, result);
        }
    }

public:
    Solution() {
        root = new TrieNode();
    }

    void insertWord(string word, int frequency, int timestamp) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
        metadata[word] = {frequency, timestamp};
    }

    vector<string> autocomplete(string prefix, int currentTime, int D, int k) {
        // Navigate to prefix node
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }

        // Collect all words with this prefix
        vector<string> matches;
        collectWords(node, prefix, matches);

        // Compute decay scores
        priority_queue<WordScore> heap;
        for (const string& word : matches) {
            WordMetadata meta = metadata[word];
            double decay = exp(-(currentTime - meta.lastUsed) / (double)D);
            double score = meta.frequency * decay;
            heap.push({word, score});
        }

        // Extract top k
        vector<string> result;
        for (int i = 0; i < k && !heap.empty(); i++) {
            result.push_back(heap.top().word);
            heap.pop();
        }

        return result;
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
        cout << "\"" << result[i] << "\"";
        if (i < result.size() - 1) cout << ",";
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
    this.metadata = new Map(); // word -> {frequency, lastUsed}
  }

  insertWord(word, frequency, timestamp) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
    }
    node.isEndOfWord = true;
    this.metadata.set(word, { frequency, lastUsed: timestamp });
  }

  autocomplete(prefix, currentTime, D, k) {
    // Navigate to prefix node
    let node = this.root;
    for (const char of prefix) {
      if (!node.children.has(char)) {
        return [];
      }
      node = node.children.get(char);
    }

    // Collect all words with this prefix
    const matches = [];
    this._collectWords(node, prefix, matches);

    // Compute decay scores
    const scores = matches.map((word) => {
      const meta = this.metadata.get(word);
      const decay = Math.exp(-(currentTime - meta.lastUsed) / D);
      const score = meta.frequency * decay;
      return { word, score };
    });

    // Sort by score (desc), then lexicographically (asc)
    scores.sort((a, b) => {
      if (Math.abs(a.score - b.score) > 1e-9) {
        return b.score - a.score;
      }
      return a.word.localeCompare(b.word);
    });

    // Return top k
    return scores.slice(0, k).map((item) => item.word);
  }

  _collectWords(node, prefix, result) {
    if (node.isEndOfWord) {
      result.push(prefix);
    }
    for (const [char, child] of node.children) {
      this._collectWords(child, prefix + char, result);
    }
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
  console.log(JSON.stringify(result));
});
```

### Common Mistakes to Avoid

1. **Incorrect Decay Calculation**

   - **Issue**: Using integer division or forgetting to cast to double
   - ❌ Wrong: `exp(-(currentTime - lastUsed) / D)` when D is int
   - ✅ Correct: `exp(-(currentTime - lastUsed) / (double)D)`

2. **Not Handling Tie-Breaking**

   - **Issue**: When scores are equal, forgetting to sort lexicographically
   - ❌ Wrong: Only sorting by score
   - ✅ Correct: Sort by score DESC, then by word ASC

3. **Inefficient Full Sort**

   - **Issue**: Sorting all M matches when only k results are needed
   - ❌ Wrong: `sort(matches)` then `return matches[:k]`
   - ✅ Correct: Use min-heap of size k for O(M log k)

## Related Concepts

- **Prefix Trees (Tries)**: Fundamental data structure for string prefix matching
- **Exponential Decay**: Widely used in recommendation systems, caching, and time-series analysis
- **Top-K Selection**: Heap-based optimization for ranking problems
- **Autocomplete Systems**: Real-world applications in search engines, IDEs, mobile keyboards


## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= frequency <= 10^6`
- `0 <= timestamp, currentTime <= 10^9`
- `1 <= D <= 10^9` (decay constant)
- `1 <= k <= 10`
- All words are lowercase English letters