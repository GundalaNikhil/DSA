---
problem_id: TRI_MINIMUM_UNIQUE_PREFIX__1847
display_id: TRI-007
slug: minimum-unique-prefix-lengths
title: "Minimum Unique Prefix Lengths"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Hash Table
tags:
  - trie
  - prefix
  - string-matching
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-007: Minimum Unique Prefix Lengths

## Problem Statement

Given an array of lowercase words, for each word, find the minimum prefix length that makes it unique among all words in the array.

![Problem Illustration](../images/TRI-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return an array of integers where the i-th integer represents the minimum prefix length for the i-th word.

Format: `[length1,length2,...]`

## Constraints

- `1 <= n <= 10^5` (number of words)
- Total character length across all words <= `2 × 10^5`
- All words consist of lowercase English letters (a-z)
- No two words are identical

## Example 1

**Input:**

```
4
zebra
dog
duck
dove
```

**Output:**

```
[1,3,2,3]
```

**Explanation:**

- "zebra": First character 'z' is unique (count=1) → prefix length = 1
- "dog": 'd' shared (count=3), 'o' shared with dove (count=2), 'g' unique (count=1) → prefix length = 3
- "duck": 'd' shared (count=3), 'u' unique (count=1) → prefix length = 2
- "dove": 'd' shared (count=3), 'o' shared with dog (count=2), 'v' unique (count=1) → prefix length = 3

![Example Visualization](../images/TRI-007/example-1.png)

## Example 2

**Input:**

```
3
apple
application
app
```

**Output:**

```
[5,5,3]
```

**Explanation:**

- "apple": Shares "app" with others, shares "appl" with "application" → needs "apple" (5 chars)
- "application": Shares "app" with others, shares "appl" with "apple" → needs "appli" (5 chars)
- "app": Shortest word, but shares with others → needs full length (3 chars)

![Example Visualization](../images/TRI-007/example-2.png)

## Notes

- The minimum prefix length is determined by the trie structure
- If a word is a prefix of another word, it needs its full length
- Use a trie with node counts to efficiently compute minimum prefixes

## Related Topics

Trie, String, Prefix Matching, Hash Table

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] findMinimumPrefixLengths(String[] words) {
        // Implement here
        return new int[words.length];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }

        Solution solution = new Solution();
        int[] result = solution.findMinimumPrefixLengths(words);

        System.out.print("[");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(",");
        }
        System.out.println("]");
    }
}
```

### Python

```python
from typing import List

class Solution:
    def find_minimum_prefix_lengths(self, words: List[str]) -> List[int]:
        # Implement here
        return []

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    words = input_data[1:n+1]

    solution = Solution()
    result = solution.find_minimum_prefix_lengths(words)

    print("[" + ",".join(map(str, result)) + "]")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> findMinimumPrefixLengths(vector<string>& words) {
        // Implement here
        return {};
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }

    Solution solution;
    vector<int> result = solution.findMinimumPrefixLengths(words);

    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]" << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findMinimumPrefixLengths(words) {
    // Implement here
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
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  const n = parseInt(tokens[0]);
  const words = tokens.slice(1, n + 1);

  const solution = new Solution();
  const result = solution.findMinimumPrefixLengths(words);

  console.log("[" + result.join(",") + "]");
});
```
