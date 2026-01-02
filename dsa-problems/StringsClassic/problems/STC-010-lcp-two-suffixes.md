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
    int[][] st;
    int[] logs;
    int[] rank;
    int n;

    public int[] lcpQueries(String s, int[][] queries) {
        return null;
    }

    int[] sa;
    
    void buildSA(String s) {
        Integer[] saObj = new Integer[n];
        rank = new int[n];
        int[] newRank = new int[n];
        
        for (int i = 0; i < n; i++) {
            saObj[i] = i;
            rank[i] = s.charAt(i);
        }
        
        for (int k = 1; k < n; k *= 2) {
            int len = k;
            Arrays.sort(saObj, (i, j) -> {
                if (rank[i] != rank[j]) return rank[i] - rank[j];
                int ri = (i + len < n) ? rank[i + len] : -1;
                int rj = (j + len < n) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[saObj[0]] = 0;
            for (int i = 1; i < n; i++) {
                int prev = saObj[i - 1];
                int curr = saObj[i];
                int r1 = rank[prev];
                int r2 = (prev + len < n) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < n) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) newRank[curr] = newRank[prev];
                else newRank[curr] = newRank[prev] + 1;
            }
            System.arraycopy(newRank, 0, rank, 0, n);
            if (rank[saObj[n - 1]] == n - 1) break;
        }
        sa = new int[n];
        for(int i=0; i<n; i++) sa[i] = saObj[i];
    }

    int[] buildLCP(String s) {
        int[] lcp = new int[n - 1];
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s.charAt(i + k) == s.charAt(j + k)) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        return lcp;
    }

    void buildSparseTable(int[] arr) {
        int m = arr.length;
        if (m == 0) return;
        logs = new int[m + 1];
        for (int i = 2; i <= m; i++) logs[i] = logs[i / 2] + 1;
        
        int K = logs[m];
        st = new int[K + 1][m];
        for (int i = 0; i < m; i++) st[0][i] = arr[i];
        
        for (int k = 1; k <= K; k++) {
            for (int i = 0; i + (1 << k) <= m; i++) {
                st[k][i] = Math.min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
    }

    int query(int L, int R) {
        if (L > R) return 0;
        int j = logs[R - L + 1];
        return Math.min(st[j][L], st[j][R - (1 << j) + 1]);
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

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(200000)

class Solution:
    def lcp_queries(self, s: str, queries: list[tuple[int, int]]) -> list[int]:
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
    vector<int> rank;
    vector<vector<int>> st;
    vector<int> logs;

public:
    vector<int> lcpQueries(const string& s, const vector<pair<int, int>>& queries) {
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

