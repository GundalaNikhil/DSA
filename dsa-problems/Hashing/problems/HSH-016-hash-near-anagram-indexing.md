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
time_limit: 2000
memory_limit: 256
---

# HSH-016: Hash-Based Near-Anagram Indexing

## Problem Statement

Group words where two words belong to the same group if they become anagrams after deleting exactly one character from each (you can choose any character to delete).

Return the number of distinct groups formed.

![Problem Illustration](../images/HSH-016/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: one word per line

## Output Format

- Single integer: number of distinct groups

## Constraints

- `1 <= n <= 10^5`
- `1 <= word length <= 30`
- Words contain only lowercase English letters

## Example

**Input:**

```
4
abcd
abdc
abc
abd
```

**Output:**

```
2
```

**Explanation:**

Words: ["abcd", "abdc", "abc", "abd"]

Group 1: "abcd", "abdc", "abc"

- "abcd" → delete 'd' → "abc" (sorted)
- "abdc" → delete 'd' → "abc" (sorted)
- "abc" → delete 'c' → "ab" (sorted), matches others

Group 2: "abd"

- "abd" → delete 'd' → "ab" (sorted)

Total: 2 groups

![Example Visualization](../images/HSH-016/example-1.png)

## Notes

- For each word, generate all possible strings after deleting one character
- Sort each deletion result to create signature
- Use Union-Find or map to group words sharing signatures
- Time complexity: O(n × L²) where L is word length
- Space complexity: O(n × L)

## Related Topics

Anagrams, Hashing, Union-Find, String Manipulation, Grouping

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countNearAnagramGroups(int n, String[] words) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = br.readLine().trim();
        }

        Solution sol = new Solution();
        System.out.println(sol.countNearAnagramGroups(n, words));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_near_anagram_groups(self, n, words):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0].strip())
    words = input_data[1:n+1]

    sol = Solution()
    print(sol.count_near_anagram_groups(n, words))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int countNearAnagramGroups(int n, const vector<string>& words) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> words(n);
    for (int i = 0; i < n; i++) cin >> words[i];

    Solution sol;
    cout << sol.countNearAnagramGroups(n, words) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countNearAnagramGroups(n, words) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const n = parseInt(input[0].trim());
  const words = input.slice(1, n + 1).map((w) => w.trim());

  const sol = new Solution();
  console.log(sol.countNearAnagramGroups(n, words));
}

solve();
```
