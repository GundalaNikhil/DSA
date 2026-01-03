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
time_limit: 2000
memory_limit: 256
---
# STC-015: Aho-Corasick With Cooldown Scoring

## Problem Statement

You are given `k` patterns, each with an integer score, and a text `t`. While scanning `t`, you may choose a subset of pattern occurrences to collect their scores.

If you choose an occurrence that ends at position `r`, then the next chosen occurrence must start at position `>= r + G + 1` (a cooldown of `G` characters after the end).

Return the maximum total score you can collect.

![Problem Illustration](../images/STC-015/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` lines: a pattern string `p_i` and an integer score `w_i`
- Next line: integer `G`
- Last line: text string `t`

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= k <= 100000`
- `1 <= |t| <= 200000`
- Sum of pattern lengths `<= 200000`
- `0 <= w_i <= 1000000`
- `0 <= G <= 1000`
- All strings contain lowercase English letters

## Example

**Input:**

```
2
ab 5
b 2
1
abb
```

**Output:**

```
5
```

**Explanation:**

Matches are "ab" at [1,2] with score 5 and "b" at [2,2] and [3,3] with score 2. Taking "ab" ends at 2, and cooldown `G=1` blocks any chosen match starting at 3, so the best total is 5.

![Example Visualization](../images/STC-015/example-1.png)

## Notes

- Use Aho-Corasick to list all occurrences (end index, start index, score).
- Sort or bucket occurrences by end index for DP transitions.
- This is weighted interval scheduling with a cooldown gap.
- Use 64-bit integers for the DP values.

## Related Topics

Aho-Corasick, Pattern Matching, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxCooldownScore(String text, String[] patterns, long[] weights, int g) {
        //Implement here
        return 0L;
    }

    public long countMatches(String text, String[] patterns) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;

        String firstToken = sc.next();

        // Try to parse as k (MD format)
        int k = -1;
        try {
            k = Integer.parseInt(firstToken);
            if (k <= 0 || k >= 100000) k = -1;
        } catch (NumberFormatException e) {
            k = -1;
        }

        Solution solution = new Solution();

        if (k > 0) {
            // MD Format: k pattern1 weight1 pattern2 weight2 ... G text
            String[] patterns = new String[k];
            long[] weights = new long[k];
            for (int i = 0; i < k; i++) {
                patterns[i] = sc.next();
                weights[i] = sc.nextLong();
            }
            int g = sc.nextInt();
            String text = sc.next();
            System.out.println(solution.maxCooldownScore(text, patterns, weights, g));
        } else {
            // YAML Format: text k pattern1 pattern2 ...
            String text = firstToken;
            if (sc.hasNextInt()) {
                k = sc.nextInt();
                String[] patterns = new String[k];
                for (int i = 0; i < k; i++) {
                    patterns[i] = sc.next();
                }
                System.out.println(solution.countMatches(text, patterns));
            }
        }

        sc.close();
    }
}
```

### Python

```python
import sys
import collections

# Increase recursion depth
sys.setrecursionlimit(200000)

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = None
        self.patterns = [] # List of (len, weight) for Cooldown / List of indices/counts for Counting

def build_aho_corasick(patterns, weights=None):
    root = Node()
    for i, p in enumerate(patterns):
        curr = root
        for char in p:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        w = weights[i] if weights else 1
        curr.patterns.append((len(p), w))
    
    queue = collections.deque()
    for char, node in root.children.items():
        node.fail = root
        queue.append(node)
        
    while queue:
        curr = queue.popleft()
        if curr.fail.patterns:
            curr.output = curr.fail
        else:
            curr.output = curr.fail.output
            
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char in curr.children:
                child = curr.children[char]
                child.fail = curr.fail.children.get(char, root)
                queue.append(child)
            else:
                curr.children[char] = curr.fail.children.get(char, root)
                
    return root

def solve_cooldown(text, patterns, weights, g):
    # //Implement here
    return 0

def solve_counting(text, patterns):
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Check format
    # MD: k (int) ...
    # YAML: text (string) ...
    
    first_token = input_data[0]
    
    is_md_format = False
    try:
        k = int(first_token)
        is_md_format = True
    except ValueError:
        is_md_format = False
        
    iter_data = iter(input_data)
    
    if is_md_format:
        try:
            k = int(next(iter_data))
            patterns = []
            weights = []
            for _ in range(k):
                patterns.append(next(iter_data))
                weights.append(int(next(iter_data)))
            g = int(next(iter_data))
            text = next(iter_data)
            print(solve_cooldown(text, patterns, weights, g))
        except StopIteration:
            pass
    else:
        # YAML Format: Text, k, patterns...
        try:
            text = next(iter_data)
            k = int(next(iter_data))
            patterns = []
            for _ in range(k):
                patterns.append(next(iter_data))
            
            print(solve_counting(text, patterns))
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
        //Implement here
        return 0;
    }

    long long countMatches(const string& text, const vector<string>& patterns) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string firstToken;
    if (!(cin >> firstToken)) return 0;

    // Try to parse as k (MD format)
    int k = -1;
    try {
        k = stoi(firstToken);
        if (k <= 0 || k >= 100000) k = -1;
    } catch (...) {
        k = -1;
    }

    Solution solution;

    if (k > 0) {
        // MD Format: k pattern1 weight1 pattern2 weight2 ... G text
        vector<string> patterns(k);
        vector<long long> weights(k);
        for (int i = 0; i < k; i++) {
            cin >> patterns[i] >> weights[i];
        }
        int g;
        cin >> g;
        string text;
        cin >> text;
        cout << solution.maxCooldownScore(text, patterns, weights, g) << "\n";
    } else {
        // YAML Format: text k pattern1 pattern2 ...
        string text = firstToken;
        int k;
        if (cin >> k) {
            vector<string> patterns(k);
            for (int i = 0; i < k; i++) {
                cin >> patterns[i];
            }
            cout << solution.countMatches(text, patterns) << "\n";
        }
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
    this.patterns = []; // [len, weight] for cooldown, or just indices for counting
  }
}

class Solution {
  maxCooldownScore(text, patterns, weights, g) {
    //Implement here
    return 0;
  }

  countMatches(text, patterns) {
    //Implement here
    return 0;
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

  // Detect format: MD has first token as number (k), YAML has first token as string (text)
  const firstToken = data[0];
  let isMDFormat = false;
  try {
    const k = parseInt(firstToken, 10);
    // If parsing succeeds and result is reasonable, it's MD format
    isMDFormat = !isNaN(k) && k > 0 && k < 100000;
  } catch (e) {
    isMDFormat = false;
  }

  const solution = new Solution();
  let idx = 0;

  if (isMDFormat) {
    try {
      const k = parseInt(data[idx++], 10);
      const patterns = [];
      const weights = [];
      for (let i = 0; i < k; i++) {
        patterns.push(data[idx++]);
        weights.push(parseInt(data[idx++], 10));
      }
      const g = parseInt(data[idx++], 10);
      const text = data[idx] || "";
      console.log(solution.maxCooldownScore(text, patterns, weights, g).toString());
    } catch (e) {
      // Fallback
    }
  } else {
    try {
      const text = data[idx++];
      const k = parseInt(data[idx++], 10);
      const patterns = [];
      for (let i = 0; i < k; i++) {
        patterns.push(data[idx++]);
      }
      console.log(solution.countMatches(text, patterns).toString());
    } catch (e) {
      // Fallback
    }
  }
});
```

