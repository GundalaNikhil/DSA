---
problem_id: HSH_COUNT_DISTINCT_SUBSTRINGS__8741
display_id: HSH-005
slug: count-distinct-substrings-hash
title: "Count Distinct Substrings"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Set Operations
tags:
  - hashing
  - substring
  - distinct
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-005: Count Distinct Substrings

## Problem Statement

Given a string `s`, count the number of distinct substrings (including the empty string) using polynomial hashing.

A substring is a contiguous sequence of characters within the string. Two substrings are considered the same if they have identical characters in the same order.

![Problem Illustration](../images/HSH-005/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: number of distinct substrings

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
aaa
```

**Output:**

```
4
```

**Explanation:**

String: "aaa"

All substrings:

- "" (empty) - 1 distinct
- "a" (positions 0, 1, 2) - 1 distinct
- "aa" (positions 0-1, 1-2) - 1 distinct
- "aaa" (position 0-2) - 1 distinct

Total distinct: 4

![Example Visualization](../images/HSH-005/example-1.png)

## Notes

- Generate all O(n²) substrings
- Compute hash for each substring
- Use a set to store unique hashes
- Use double hashing to minimize collisions
- Time complexity: O(n²)
- Space complexity: O(n²)

## Related Topics

Hashing, Substring Generation, Set Operations, Suffix Array

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countDistinctSubstrings(String s) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;

        Solution sol = new Solution();
        System.out.println(sol.countDistinctSubstrings(s.trim()));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_distinct_substrings(self, s):
        # Implement here
        return 0

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return

    sol = Solution()
    print(sol.count_distinct_substrings(s))

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
    int countDistinctSubstrings(string s) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    Solution sol;
    cout << sol.countDistinctSubstrings(s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countDistinctSubstrings(s) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;

  const sol = new Solution();
  console.log(sol.countDistinctSubstrings(input));
}

solve();
```
