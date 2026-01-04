---
problem_id: TRI_KTH_MISSING__4257
display_id: TRI-006
slug: kth-string-not-present
title: "Lexicographic k-th String Not Present"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Combinatorics
  - DFS
tags:
  - trie
  - string
  - combinatorics
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lexicographic k-th String Not Present

## Problem Statement

Given a trie of inserted lowercase strings, find the k-th lexicographically smallest string of length up to `L` that is NOT present in the trie.

![Problem Illustration](../images/TRI-006/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `L`, `k` (number of strings, max length, kth position)
- Next `n` lines: Each contains a lowercase string already inserted in the trie

## Output Format

Print the k-th missing string of length ≤ L in lexicographic order, or an empty string if k exceeds the total missing count.

## Constraints

- 0 ≤ n ≤ 10^5
- 1 ≤ L ≤ 6
- 1 ≤ k ≤ 10^9
- All strings consist of lowercase English letters (a-z)

## Examples

### Example 1

**Input:**

```
2 2 1
a
b
```

**Output:**

```
aa
```

**Explanation:**

Inserted: "a", "b"
Missing strings of length ≤ 2 in order:

1. "aa" ← answer
2. "ab"
3. "ac"
   ...

![Example 1 Visualization](../images/TRI-006/example-1.png)

## Notes

- Strings can end at any depth from 1 to L
- Empty string not counted
- Lexicographic order: a < aa < ab < ... < z < za < ...
- Use DFS to count missing strings efficiently

## Related Topics

Trie, String, Combinatorics, DFS, Missing Elements

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String kthMissingString(String[] insertedList, int L, int k) {
        // Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int L = sc.nextInt();
        int k = sc.nextInt();

        String[] insertedList = new String[n];
        for (int i = 0; i < n; i++) {
            insertedList[i] = sc.next();
        }

        Solution solution = new Solution();
        String result = solution.kthMissingString(insertedList, L, k);
        System.out.println(result);
    }
}
```

### Python

```python
from typing import List

class Solution:
    def kth_missing_string(self, inserted_list: List[str], L: int, k: int) -> str:
        # Implement here
        return ""

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    L = int(input_data[1])
    k = int(input_data[2])
    inserted_list = input_data[3:3+n]

    solution = Solution()
    result = solution.kth_missing_string(inserted_list, L, k)
    print(result)

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
    string kthMissingString(const vector<string>& insertedList, int L, int k) {
        // Implement here
        return "";
    }
};

int main() {
    int n, L, k;
    if (!(cin >> n >> L >> k)) return 0;

    vector<string> insertedList(n);
    for (int i = 0; i < n; i++) {
        cin >> insertedList[i];
    }

    Solution solution;
    string result = solution.kthMissingString(insertedList, L, k);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kthMissingString(insertedList, L, k) {
    // Implement here
    return "";
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

  let idx = 0;
  const n = parseInt(tokens[idx++]);
  const L = parseInt(tokens[idx++]);
  const k = parseInt(tokens[idx++]);
  const insertedList = tokens.slice(idx, idx + n);

  const solution = new Solution();
  const result = solution.kthMissingString(insertedList, L, k);

  console.log(result);
});
```
