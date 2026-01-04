---
problem_id: HSH_PALINDROME_SUBSTRING_QUERIES__2639
display_id: HSH-004
slug: palindrome-substring-queries
title: "Palindrome Substring Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-004: Palindrome Substring Queries

## Problem Statement

Given a string `s` and `q` queries, answer whether substring `s[l..r]` is a palindrome using hash-based comparisons.

For each query `(l, r)`, determine if the substring from index `l` to `r` (inclusive, 0-indexed) reads the same forwards and backwards.

![Problem Illustration](../images/HSH-004/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of queries)
- Next `q` lines: two integers `l r` for each query

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= l <= r < |s|`

## Example

**Input:**

```
abccba
3
0 5
1 4
2 3
```

**Output:**

```
true
false
true
```

**Explanation:**

String: "abccba"

Query 1: s[0..5] = "abccba" → palindrome → true
Query 2: s[1..4] = "bccb" → not a palindrome → false
Query 3: s[2..3] = "cc" → palindrome → true

![Example Visualization](../images/HSH-004/example-1.png)

## Notes

- Precompute forward and reverse polynomial hashes
- Compare hash of s[l..r] with hash of reverse(s[l..r])
- Use double hashing to minimize false positives
- Time complexity: O(n + q) with O(n) preprocessing
- Space complexity: O(n)

## Related Topics

Palindrome Detection, Hashing, Rolling Hash, String Reversal

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean[] arePalindromes(String s, int q, int[][] queries) {
        // Implement here
        return new boolean[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;
        String qLine = br.readLine();
        if (qLine == null) return;
        int q = Integer.parseInt(qLine.trim());

        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            queries[i][0] = Integer.parseInt(parts[0]);
            queries[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        boolean[] result = sol.arePalindromes(s, q, queries);

        PrintWriter out = new PrintWriter(System.out);
        for (boolean res : result) {
            out.println(res);
        }
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def are_palindromes(self, s, q, queries):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    q = int(input_data[1])
    queries = []
    idx = 2
    for _ in range(q):
        queries.append(list(map(int, input_data[idx:idx+2])))
        idx += 2

    sol = Solution()
    result = sol.are_palindromes(s, q, queries)
    for res in result:
        print("true" if res else "false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<bool> arePalindromes(string s, int q, vector<vector<int>>& queries) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    int q;
    if (!(cin >> q)) return 0;

    vector<vector<int>> queries(q, vector<int>(2));
    for (int i = 0; i < q; i++) cin >> queries[i][0] >> queries[i][1];

    Solution sol;
    vector<bool> result = sol.arePalindromes(s, q, queries);

    for (int i = 0; i < q; i++) {
        cout << (result[i] ? "true" : "false") << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  arePalindromes(s, q, queries) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const s = input[0];
  const q = parseInt(input[1]);
  const queries = [];
  let idx = 2;
  for (let i = 0; i < q; i++) {
    queries.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  const result = sol.arePalindromes(s, q, queries);
  console.log(result.map((res) => (res ? "true" : "false")).join("\n"));
}

solve();
```
