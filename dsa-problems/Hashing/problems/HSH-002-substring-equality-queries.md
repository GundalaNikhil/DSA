---
problem_id: HSH_SUBSTRING_EQUALITY_QUERIES__5917
display_id: HSH-002
slug: substring-equality-queries
title: "Substring Equality Queries"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - Rolling Hash
  - String Matching
tags:
  - hashing
  - rolling-hash
  - substring
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-002: Substring Equality Queries

## Problem Statement

Given a string `s` and `q` queries, each query asks whether two substrings of `s` are equal.

Each query is specified as `(l1, r1, l2, r2)` where:

- First substring: `s[l1..r1]` (inclusive, 0-indexed)
- Second substring: `s[l2..r2]` (inclusive, 0-indexed)

For each query, output `true` if the two substrings are equal, `false` otherwise.

Use polynomial hashing with double hashing (two different moduli) to minimize collision probability.

![Problem Illustration](../images/HSH-002/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of queries)
- Next `q` lines: four integers `l1 r1 l2 r2` for each query

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= l1 <= r1 < |s|`
- `0 <= l2 <= r2 < |s|`
- `r1 - l1 == r2 - l2` (substring lengths must match)

## Example

**Input:**

```
ababa
3
0 1 2 3
0 2 2 4
1 1 3 3
```

**Output:**

```
true
true
true
```

**Explanation:**

String: "ababa"

Query 1: s[0..1] = "ab", s[2..3] = "ab" → true
Query 2: s[0..2] = "aba", s[2..4] = "aba" → true
Query 3: s[1..1] = "b", s[3..3] = "b" → true

![Example Visualization](../images/HSH-002/example-1.png)

## Notes

- Precompute prefix hashes during initialization
- Use two different moduli for double hashing to reduce collision probability
- Hash comparison: O(1) per query after O(n) preprocessing
- Time complexity: O(n + q)
- Space complexity: O(n)

## Related Topics

Rolling Hash, String Matching, Substring Comparison, Double Hashing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean[] areSubstringsEqual(String s, int q, int[][] queries) {
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

        int[][] queries = new int[q][4];
        for (int i = 0; i < q; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            for (int j = 0; j < 4; j++) queries[i][j] = Integer.parseInt(parts[j]);
        }

        Solution sol = new Solution();
        boolean[] result = sol.areSubstringsEqual(s, q, queries);

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
    def are_substrings_equal(self, s, q, queries):
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
        queries.append(list(map(int, input_data[idx:idx+4])))
        idx += 4

    sol = Solution()
    result = sol.are_substrings_equal(s, q, queries)
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
    vector<bool> areSubstringsEqual(string s, int q, vector<vector<int>>& queries) {
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

    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        for (int j = 0; j < 4; j++) cin >> queries[i][j];
    }

    Solution sol;
    vector<bool> result = sol.areSubstringsEqual(s, q, queries);

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
  areSubstringsEqual(s, q, queries) {
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
    queries.push([
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  const result = sol.areSubstringsEqual(s, q, queries);
  process.stdout.write(
    result.map((res) => (res ? "true" : "false")).join("\n") + "\n"
  );
}

solve();
```
