---
problem_id: STC_LCP_TWO_SUFFIXES__5381
display_id: STC-010
slug: lcp-two-suffixes
title: "Longest Common Prefix of Two Suffixes"
difficulty: Medium
difficulty_score: 52
topics:
  - Strings
  - Suffix Array
  - RMQ
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-010: Longest Common Prefix of Two Suffixes

## Problem Statement

You are given a string `s`. For each query `(i, j)`, return the length of the longest common prefix of the two suffixes `s[i..]` and `s[j..]`.

You must preprocess once and answer all queries efficiently.

![Problem Illustration](../images/STC-010/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q`, the number of queries
- Next `q` lines: two integers `i` and `j` (0-based indices)

## Output Format

- Print `q` lines, each the LCP length for the corresponding query

## Constraints

- `1 <= |s| <= 100000`
- `1 <= q <= 100000`
- `0 <= i, j < |s|`
- `s` contains lowercase English letters

## Example

**Input:**

```
banana
2
1 3
0 2
```

**Output:**

```
3
0
```

**Explanation:**

Suffix at 1 is "anana" and suffix at 3 is "ana". Their LCP is "ana" with length 3.
Suffix at 0 is "banana" and suffix at 2 is "nana". Their LCP length is 0.

![Example Visualization](../images/STC-010/example-1.png)

## Notes

- Build a suffix array and the LCP array.
- LCP of suffixes at positions `i` and `j` is the minimum LCP between their ranks.
- Use RMQ (sparse table or segment tree) over the LCP array.
- Each query can be answered in O(1) or O(log n) after preprocessing.

## Related Topics

Suffix Array, LCP, RMQ

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] lcpQueries(String s, int[][] queries) {
        // Implementation here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();

        java.util.List<int[]> queryList = new java.util.ArrayList<>();
        while (sc.hasNextInt()) {
            int i = sc.nextInt();
            if (!sc.hasNextInt()) break;
            int j = sc.nextInt();
            queryList.add(new int[]{i, j});
        }
        int[][] queries = queryList.toArray(new int[0][]);

        Solution solution = new Solution();
        int[] ans = solution.lcpQueries(s, queries);
        StringBuilder sb = new StringBuilder();
        for (int k = 0; k < ans.length; k++) {
            sb.append(ans[k]);
            if (k + 1 < ans.length) sb.append('\n');
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def lcp_queries(self, s: str, queries: list[tuple[int, int]]) -> list[int]:
        # Implementation here
        return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    queries = []
    idx = 1
    while idx + 1 < len(input_data):
        try:
            i = int(input_data[idx])
            j = int(input_data[idx + 1])
            queries.append((i, j))
            idx += 2
        except ValueError:
            break
        
    sol = Solution()
    ans = sol.lcp_queries(s, queries)
    sys.stdout.write("\n".join(str(x) for x in ans) + "\n")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> lcpQueries(const string& s, const vector<pair<int, int>>& queries) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        vector<pair<int, int>> queries;
        int i, j;
        while (cin >> i >> j) {
            queries.push_back({i, j});
        }

        Solution solution;
        vector<int> ans = solution.lcpQueries(s, queries);
        for (int x : ans) cout << x << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  lcpQueries(s, queries) {
    // Implementation here
    return null;
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
  const s = data[0];
  const queries = [];
  let idx = 1;
  while (idx + 1 < data.length) {
    const i = parseInt(data[idx++], 10);
    const j = parseInt(data[idx++], 10);
    queries.push([i, j]);
  }

  const solution = new Solution();
  const ans = solution.lcpQueries(s, queries);
  console.log(ans.join("\n"));
});
```
