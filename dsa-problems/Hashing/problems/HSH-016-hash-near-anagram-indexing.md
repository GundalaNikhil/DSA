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
import java.io.*;
import java.util.*;

class Solution {
    public int countNearAnagramGroups(List<String> words) {
        //Implemention here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        int n = Integer.parseInt(data[idx++]);
        List<String> words = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            words.add(data[idx++]);
        }

        Solution solution = new Solution();
        int result = solution.countNearAnagramGroups(words);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def count_near_anagram_groups(words):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    idx += 1
    words = []
    for _ in range(n):
        words.append(data[idx])
        idx += 1
    result = count_near_anagram_groups(words)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int count_near_anagram_groups(const vector<string>& words) {
    //Implemention here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<string> words;
    words.reserve(n);
    for (int i = 0; i < n; i++) {
        string w;
        cin >> w;
        words.push_back(w);
    }

    int result = count_near_anagram_groups(words);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function countNearAnagramGroups(words) {
  //Implemention here
  return 0;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const words = [];
for (let i = 0; i < n; i++) {
  words.push(data[idx++]);
}
const result = countNearAnagramGroups(words);
process.stdout.write(String(result));
```

