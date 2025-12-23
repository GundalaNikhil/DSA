---
problem_id: STC_AHO_CORASICK_COOLDOWN__1658
display_id: STC-015
slug: aho-corasick-cooldown-scoring
title: "Aho-Corasick With Cooldown Scoring"
difficulty: Medium
difficulty_score: 60
topics:
  - Strings
  - Aho-Corasick
  - Dynamic Programming
tags:
  - strings
  - aho-corasick
  - dp
  - medium
premium: true
subscription_tier: basic
---

# STC-015: Aho-Corasick With Cooldown Scoring

## 📋 Problem Summary

You are given a text `t` and a set of patterns, each with a score. You want to select a subset of pattern occurrences in `t` to maximize the total score. The constraint is that if you pick an occurrence ending at index `r`, the next occurrence you pick must start at or after `r + G + 1`. This effectively imposes a "cooldown" of `G` characters.

## 🌍 Real-World Scenario

**Scenario Title:** Ad Insertion in Streaming

Imagine you are inserting advertisements into a live video stream. You have a set of potential ad spots (patterns) detected in the content stream, each with a certain revenue (score). However, to maintain a good user experience, you cannot show ads too frequently. After an ad finishes, you must wait for a minimum duration (cooldown `G`) before showing another. Your goal is to select the optimal set of ads to maximize revenue while respecting the spacing constraint.

**Why This Problem Matters:**

- **Resource Scheduling:** Scheduling tasks on a machine where each task requires a setup/cooldown time.
- **Rate Limiting:** maximizing throughput under rate limits.

![Real-World Application](../images/STC-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Text: `a b b a c`
Patterns: `ab` (5), `b` (2). `G=1`.

Occurrences:
1. `ab` at `[0, 1]`. Score 5. Ends at 1. Next start >= 1+1+1 = 3.
2. `b` at `[1, 1]`. Score 2. Ends at 1. Next start >= 3.
3. `b` at `[2, 2]`. Score 2. Ends at 2. Next start >= 4.

DP Decisions:
- At index 1 (`b`): Can pick `ab` (score 5) or `b` (score 2).
  - If `ab`: `prev = dp[0 - 2 - 1] = 0`. Total 5.
  - If `b`: `prev = dp[1 - 1 - 1] = 0`. Total 2.
  - `dp[1] = 5`.
- At index 2 (`b`): Can pick `b` (score 2).
  - `prev = dp[2 - 1 - 1] = dp[0] = 0`. Total 2.
  - Or inherit `dp[1] = 5`.
  - `dp[2] = 5`.

Result: 5.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Indices:** 0-based indexing for text.
- **Cooldown:** If match ends at `i`, next match starts at `i + G + 1`.
- **Overlaps:** Patterns can overlap in the text, but selected occurrences cannot overlap (and must satisfy cooldown).
- **Constraints:** `G` is small (1000), but `N` is 200,000. O(N * G) is too slow. We need something close to O(N).

## Naive Approach

### Intuition

Find all occurrences. Sort them. Use standard Weighted Interval Scheduling DP.

### Algorithm

1. Find all `M` occurrences. Store as `(start, end, score)`.
2. Sort by `end`.
3. `dp[i]` = max score using subset of first `i` occurrences.
4. `dp[i] = max(dp[i-1], score_i + dp[prev_compatible])`.
5. Find `prev_compatible` using binary search.

### Time Complexity

- **O(M log M)**: where `M` is number of matches.
- `M` can be large (O(N * sqrt(N)) or worse).
- Might be acceptable, but finding all matches first uses extra memory.

## Optimal Approach (AC + DP)

### Key Insight

Instead of listing all matches, we can compute the DP state as we scan the text.
`dp[i]` = Max score considering text prefix `t[0...i]`.
Transitions:
1. Don't pick any pattern ending at `i`: `dp[i] = dp[i-1]`.
2. Pick a pattern `p` ending at `i`: `dp[i] = max(dp[i], dp[i - len(p) - G] + weight(p))`.

To efficiently find which patterns end at `i`, we use the **Aho-Corasick Automaton**.
As we traverse the text, we maintain the current state in the AC trie.
The patterns ending at the current position correspond to the current node and all nodes reachable via **suffix links** (failure links).
Since traversing all suffix links can be slow, we can optimize by precomputing the "best" transition or simply relying on the fact that the number of distinct pattern lengths ending at a position is bounded by `sqrt(2 * sum_lengths)`. Given the constraints (`sum_lengths <= 200,000`), this is small enough (~630).

### Algorithm

1. **Build AC Automaton**:
   - Insert all patterns. Store `(len, weight)` at terminal nodes.
   - Build failure links.
   - Optimization: Create `output_link[u]` which points to the nearest terminal node reachable via failure links. This allows skipping non-terminal nodes.
2. **DP Initialization**:
   - `dp` array of size `N + 1`. `dp[i]` corresponds to text length `i` (index `i-1`).
   - `dp[0] = 0`.
3. **Scan Text**:
   - `curr = root`.
   - For `i` from 0 to `N-1`:
     - Transition `curr` using `t[i]`.
     - `dp[i+1] = dp[i]`.
     - Traverse `temp = curr` using `output_link`:
       - For each pattern `(len, w)` at `temp`:
         - `prev_idx = i + 1 - len - G`.
         - `score = (prev_idx < 0) ? 0 : dp[prev_idx]`.
         - `dp[i+1] = max(dp[i+1], score + w)`.
4. **Result**: `dp[N]`.

### Time Complexity

- **O(N * sqrt(SumLen))**: In the worst case, we traverse `sqrt(SumLen)` output links per character. With `SumLen = 200,000`, this is fast enough.

### Space Complexity

- **O(SumLen + N)**.

![Algorithm Visualization](../images/STC-015/algorithm-visualization.png)
![Algorithm Steps](../images/STC-015/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        Node[] children = new Node[26];
        Node fail;
        Node output; // Nearest terminal node via fail links
        List<Integer> lens = new ArrayList<>();
        List<Long> weights = new ArrayList<>();
    }

    public long maxCooldownScore(String text, String[] patterns, long[] weights, int g) {
        Node root = new Node();
        
        // 1. Build Trie
        for (int i = 0; i < patterns.length; i++) {
            Node curr = root;
            for (char c : patterns[i].toCharArray()) {
                int idx = c - 'a';
                if (curr.children[idx] == null) curr.children[idx] = new Node();
                curr = curr.children[idx];
            }
            curr.lens.add(patterns[i].length());
            curr.weights.add(weights[i]);
        }
        
        // 2. Build Failure Links
        Queue<Node> q = new LinkedList<>();
        for (int i = 0; i < 26; i++) {
            if (root.children[i] != null) {
                root.children[i].fail = root;
                q.add(root.children[i]);
            } else {
                root.children[i] = root;
            }
        }
        
        while (!q.isEmpty()) {
            Node curr = q.poll();
            // Compute output link
            if (!curr.fail.lens.isEmpty()) curr.output = curr.fail;
            else curr.output = curr.fail.output;
            
            for (int i = 0; i < 26; i++) {
                if (curr.children[i] != null) {
                    curr.children[i].fail = curr.fail.children[i];
                    q.add(curr.children[i]);
                } else {
                    curr.children[i] = curr.fail.children[i];
                }
            }
        }
        
        // 3. DP
        int n = text.length();
        long[] dp = new long[n + 1];
        Node curr = root;
        
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i];
            curr = curr.children[text.charAt(i) - 'a'];
            
            Node temp = curr;
            while (temp != root) {
                if (!temp.lens.isEmpty()) {
                    for (int k = 0; k < temp.lens.size(); k++) {
                        int len = temp.lens.get(k);
                        long w = temp.weights.get(k);
                        int prevIdx = i + 1 - len - g;
                        long prevScore = (prevIdx < 0) ? 0 : dp[prevIdx];
                        dp[i + 1] = Math.max(dp[i + 1], prevScore + w);
                    }
                }
                if (temp.output == null) break;
                temp = temp.output;
            }
        }
        
        return dp[n];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int k = sc.nextInt();
        String[] patterns = new String[k];
        long[] weights = new long[k];
        for (int i = 0; i < k; i++) {
            patterns[i] = sc.next();
            weights[i] = sc.nextLong();
        }
        int g = sc.nextInt();
        String text = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.maxCooldownScore(text, patterns, weights, g));
        sc.close();
    }
}
```

### Python

```python
import collections

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = None
        self.patterns = [] # List of (len, weight)

def max_cooldown_score(text: str, patterns: list[str], weights: list[int], g: int) -> int:
    root = Node()
    
    # 1. Build Trie
    for p, w in zip(patterns, weights):
        curr = root
        for char in p:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.patterns.append((len(p), w))
        
    # 2. Build Failure Links
    queue = collections.deque()
    for char, node in root.children.items():
        node.fail = root
        queue.append(node)
        
    while queue:
        curr = queue.popleft()
        
        # Output link
        if curr.fail.patterns:
            curr.output = curr.fail
        else:
            curr.output = curr.fail.output
            
        for char, child in curr.children.items():
            child.fail = curr.fail.children.get(char, root)
            # If fail link doesn't have char, it should go to root's child or root
            # Standard AC optimization: direct edges
            queue.append(child)
            
    # Optimization: Fill missing transitions
    # But we need to handle "default to fail" logic during traversal
    
    # 3. DP
    n = len(text)
    dp = [0] * (n + 1)
    curr = root
    
    for i in range(n):
        char = text[i]
        
        # Transition
        while curr != root and char not in curr.children:
            curr = curr.fail
        if char in curr.children:
            curr = curr.children[char]
        else:
            curr = root
            
        dp[i + 1] = dp[i]
        
        # Traverse output links
        temp = curr
        while temp != root and temp is not None:
            for length, weight in temp.patterns:
                prev_idx = i + 1 - length - g
                prev_score = dp[prev_idx] if prev_idx >= 0 else 0
                if prev_score + weight > dp[i + 1]:
                    dp[i + 1] = prev_score + weight
            
            
            if temp.output:
                temp = temp.output
            elif not temp.patterns: 
                 break
            else:
                 
                 break
                 
    return dp[n]

def main():
    import sys
    # Increase recursion depth just in case
    sys.setrecursionlimit(200000)
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    k = int(input_data[idx]); idx += 1
    patterns = []
    weights = []
    for _ in range(k):
        patterns.append(input_data[idx]); idx += 1
        weights.append(int(input_data[idx])); idx += 1
    g = int(input_data[idx]); idx += 1
    text = input_data[idx] if idx < len(input_data) else ""
    
    print(max_cooldown_score(text, patterns, weights, g))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    Node* children[26];
    Node* fail;
    Node* output;
    vector<pair<int, long long>> patterns; // len, weight

    Node() {
        for (int i = 0; i < 26; i++) children[i] = nullptr;
        fail = nullptr;
        output = nullptr;
    }
};

class Solution {
public:
    long long maxCooldownScore(const string& text, const vector<string>& patterns,
                               const vector<long long>& weights, int g) {
        Node* root = new Node();
        
        // 1. Build Trie
        for (size_t i = 0; i < patterns.size(); i++) {
            Node* curr = root;
            for (char c : patterns[i]) {
                int idx = c - 'a';
                if (!curr->children[idx]) curr->children[idx] = new Node();
                curr = curr->children[idx];
            }
            curr->patterns.push_back({(int)patterns[i].length(), weights[i]});
        }
        
        // 2. Build Failure Links
        queue<Node*> q;
        for (int i = 0; i < 26; i++) {
            if (root->children[i]) {
                root->children[i]->fail = root;
                q.push(root->children[i]);
            } else {
                root->children[i] = root;
            }
        }
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            
            if (!curr->fail->patterns.empty()) curr->output = curr->fail;
            else curr->output = curr->fail->output;
            
            for (int i = 0; i < 26; i++) {
                if (curr->children[i]) {
                    curr->children[i]->fail = curr->fail->children[i];
                    q.push(curr->children[i]);
                } else {
                    curr->children[i] = curr->fail->children[i];
                }
            }
        }
        
        // 3. DP
        int n = text.length();
        vector<long long> dp(n + 1, 0);
        Node* curr = root;
        
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i];
            curr = curr->children[text[i] - 'a'];
            
            Node* temp = curr;
            while (temp != root) {
                for (auto& p : temp->patterns) {
                    int len = p.first;
                    long long w = p.second;
                    int prevIdx = i + 1 - len - g;
                    long long prevScore = (prevIdx < 0) ? 0 : dp[prevIdx];
                    dp[i + 1] = max(dp[i + 1], prevScore + w);
                }
                if (temp->output == nullptr) break;
                temp = temp->output;
            }
        }
        
        // Cleanup memory (optional for CP, good for practice)
        // ... recursive delete ...
        
        return dp[n];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<string> patterns(k);
        vector<long long> weights(k);
        for (int i = 0; i < k; i++) {
            cin >> patterns[i] >> weights[i];
        }
        int g;
        cin >> g;
        string text;
        cin >> text;

        Solution solution;
        cout << solution.maxCooldownScore(text, patterns, weights, g) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Node {
  constructor() {
    this.children = new Array(26).fill(null);
    this.fail = null;
    this.output = null;
    this.patterns = []; // [len, weight]
  }
}

class Solution {
  maxCooldownScore(text, patterns, weights, g) {
    const root = new Node();
    
    // 1. Build Trie
    for (let i = 0; i < patterns.length; i++) {
      let curr = root;
      for (let j = 0; j < patterns[i].length; j++) {
        const idx = patterns[i].charCodeAt(j) - 97;
        if (!curr.children[idx]) curr.children[idx] = new Node();
        curr = curr.children[idx];
      }
      curr.patterns.push([patterns[i].length, weights[i]]);
    }
    
    // 2. Build Failure Links
    const q = [];
    for (let i = 0; i < 26; i++) {
      if (root.children[i]) {
        root.children[i].fail = root;
        q.push(root.children[i]);
      } else {
        root.children[i] = root;
      }
    }
    
    let head = 0;
    while (head < q.length) {
      const curr = q[head++];
      
      if (curr.fail.patterns.length > 0) curr.output = curr.fail;
      else curr.output = curr.fail.output;
      
      for (let i = 0; i < 26; i++) {
        if (curr.children[i]) {
          curr.children[i].fail = curr.fail.children[i];
          q.push(curr.children[i]);
        } else {
          curr.children[i] = curr.fail.children[i];
        }
      }
    }
    
    // 3. DP
    const n = text.length;
    const dp = new Array(n + 1).fill(0);
    let curr = root;
    
    for (let i = 0; i < n; i++) {
      dp[i + 1] = dp[i];
      const idx = text.charCodeAt(i) - 97;
      curr = curr.children[idx];
      
      let temp = curr;
      while (temp !== root) {
        for (const [len, w] of temp.patterns) {
          const prevIdx = i + 1 - len - g;
          const prevScore = (prevIdx < 0) ? 0 : dp[prevIdx];
          if (prevScore + w > dp[i + 1]) {
            dp[i + 1] = prevScore + w;
          }
        }
        if (!temp.output) break;
        temp = temp.output;
      }
    }
    
    return dp[n];
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
  let idx = 0;
  const k = parseInt(data[idx++], 10);
  const patterns = [];
  const weights = [];
  for (let i = 0; i < k; i++) {
    patterns.push(data[idx++]);
    weights.push(parseInt(data[idx++], 10));
  }
  const g = parseInt(data[idx++], 10);
  const text = data[idx] || "";

  const solution = new Solution();
  console.log(solution.maxCooldownScore(text, patterns, weights, g).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`text = "abb"`, `patterns = ["ab", "b"]`, `weights = [5, 2]`, `g = 1`.

1. **Trie**:
   - `root -> a -> b` (terminal "ab", 5)
   - `root -> b` (terminal "b", 2)
   - `fail(b) = root`. `fail(ab) = b`.
   - `output(ab) = b`.

2. **DP**:
   - `i=0` ('a'): `curr = node(a)`. No patterns. `dp[1] = dp[0] = 0`.
   - `i=1` ('b'): `curr = node(ab)`.
     - Patterns at `ab`: ("ab", 5).
       - `prev = 1 + 1 - 2 - 1 = -1`. `score = 0 + 5 = 5`. `dp[2] = 5`.
     - Output link to `b`. Patterns at `b`: ("b", 2).
       - `prev = 1 + 1 - 1 - 1 = 0`. `score = 0 + 2 = 2`. `dp[2] = max(5, 2) = 5`.
   - `i=2` ('b'): `curr = node(b)` (via fail link from `abb`? No, `ab` -> `b` transition? `node(ab)` has no `b` child. `fail(ab)=b`. `b` has `b` child? No. `fail(b)=root`. `root` has `b`. So `curr` becomes `node(b)`).
     - Patterns at `b`: ("b", 2).
       - `prev = 2 + 1 - 1 - 1 = 1`. `score = dp[1] + 2 = 0 + 2 = 2`.
     - `dp[3] = max(dp[2], 2) = 5`.

Result: 5.

## ✅ Proof of Correctness

### Invariant

`dp[i]` stores the maximum score obtainable using a subset of pattern occurrences that end at or before index `i-1` in the text.
At step `i`, we consider all patterns ending exactly at `i`. For each such pattern `p`, we can extend a valid solution ending at `i - len(p) - G`.
By taking the maximum over all such patterns and `dp[i-1]` (option to ignore matches ending at `i`), we maintain optimality.
The Aho-Corasick structure ensures we find all patterns ending at `i` efficiently.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Max Score with K Matches**
  - `dp[i][k]` = max score using exactly `k` matches.

- **Extension 2: Circular Text**
  - Unwrap string `S + S`. Constrain length to `N`.

### Common Mistakes to Avoid

1. **DP Indexing**
   - ❌ `dp[i]` using `text[i]`.
   - ✅ `dp[i]` usually means prefix of length `i`. `text[i-1]` is the character.

2. **Output Links**
   - ❌ Only checking current node for patterns.
   - ✅ Must traverse `output` links to find patterns that are suffixes of the current match (e.g., "she" and "he").

## Related Concepts

- **Knuth-Morris-Pratt (KMP)**: Single pattern version.
- **Trie**: Basic structure.
