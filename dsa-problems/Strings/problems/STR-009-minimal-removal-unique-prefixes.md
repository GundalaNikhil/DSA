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

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minDeletions(int L, int n, String[] strings) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int L = sc.nextInt();
            if (sc.hasNextInt()) {
                int n = sc.nextInt();
                String[] strings = new String[n];
                for (int i = 0; i < n; i++) {
                    if (sc.hasNext()) {
                        strings[i] = sc.next();
                    }
                }
                Solution sol = new Solution();
                System.out.println(sol.minDeletions(L, n, strings));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    L = int(input_data[0])
    n = int(input_data[1])
    strings = input_data[2:2+n]
    solution = Solution()
    print(solution.min_deletions(L, n, strings))

class Solution:
    def min_deletions(self, L: int, n: int, strings: list) -> int:
        # Implement here
        return 0

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
    int minDeletions(int L, int n, const vector<string>& strings) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int L, n;
    if (cin >> L >> n) {
        vector<string> strings(n);
        for (int i = 0; i < n; i++) {
            cin >> strings[i];
        }
        Solution sol;
        cout << sol.minDeletions(L, n, strings) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minDeletions(L, n, strings) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length >= 2) {
    const L = parseInt(input[0]);
    const n = parseInt(input[1]);
    const strings = input.slice(2, 2 + n);
    const sol = new Solution();
    console.log(sol.minDeletions(L, n, strings));
  }
});
```
