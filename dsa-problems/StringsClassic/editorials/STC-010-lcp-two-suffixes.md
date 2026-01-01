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
---

# STC-010: Longest Common Prefix of Two Suffixes

## 📋 Problem Summary

Given a string `s`, you need to answer multiple queries. Each query consists of two indices `i` and `j`. You must return the length of the **Longest Common Prefix (LCP)** between the suffix starting at `i` and the suffix starting at `j`. The solution must be efficient enough to handle up to 100,000 queries.

## 🌍 Real-World Scenario

**Scenario Title:** Version Control Diffing

In version control systems like Git, we often need to compare different versions of a file. Finding common blocks of code between two versions is essential for generating "diffs". If we concatenate the two file versions into a single string, finding the longest common prefix between suffixes starting at different positions helps identify identical code blocks that have been moved or copied. This is a fundamental operation in efficient delta compression and diff algorithms.

**Why This Problem Matters:**

- **Efficiency:** Naive comparison is O(N) per query, leading to O(NQ) total. We need O(1) per query.
- **LCA in Trees:** This problem is equivalent to finding the Lowest Common Ancestor (LCA) in a Suffix Tree, which is a classic application of RMQ (Range Minimum Query).

![Real-World Application](../images/STC-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "banana"`.
Suffix Array `sa`: `[5, 3, 1, 0, 4, 2]` ("a", "ana", "anana", "banana", "na", "nana")
LCP Array: `[1, 3, 0, 0, 2]` (between adjacent suffixes in sorted order)

Query: `i=1` ("anana"), `j=3` ("ana").
Ranks:
`rank[1]` (for "anana") is index 2 in SA.
`rank[3]` (for "ana") is index 1 in SA.

We need the minimum LCP value in the range between rank 1 and rank 2 in the sorted order.
Range `[1, 1]` (since we query `min(lcp[min_rank...max_rank-1])`).
`lcp[1] = 3`.
Answer: 3.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Indices:** `i` and `j` are 0-based indices in the original string.
- **Same Index:** If `i == j`, the LCP is the length of the suffix itself (`n - i`).
- **Constraints:** `N, Q <= 100,000`. Preprocessing O(N log N) is fine. Query O(1) is required.

## Naive Approach

### Intuition

For each query `(i, j)`, simply compare characters `s[i+k]` and `s[j+k]` until a mismatch.

### Algorithm

1. For each query `(i, j)`:
2. Loop `k` from 0.
3. While `s[i+k] == s[j+k]`, increment `k`.
4. Return `k`.

### Time Complexity

- **O(N * Q)**: In worst case (e.g., `s="aaaa..."`), each query takes O(N).
- Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach (SA + LCP + RMQ)

### Key Insight

The LCP of any two suffixes `u` and `v` is the minimum value in the LCP array between their positions in the Suffix Array.
Specifically, if `rank[u] < rank[v]`, then `LCP(u, v) = min(lcp[rank[u]], lcp[rank[u]+1], ..., lcp[rank[v]-1])`.
This is a classic **Range Minimum Query (RMQ)** problem.
We can use a **Sparse Table** to preprocess the LCP array in O(N log N) time and answer RMQ queries in O(1) time.

### Algorithm

1. **Build Suffix Array (SA)** and **Rank Array**.
2. **Build LCP Array** using Kasai's algorithm.
3. **Build Sparse Table** on the LCP array.
   - `st[k][i]` stores the minimum value in `lcp[i...i + 2^k - 1]`.
4. **Answer Queries**:
   - Get ranks `r1 = rank[i]`, `r2 = rank[j]`.
   - If `r1 == r2`, return `n - i`.
   - Ensure `r1 < r2`. If not, swap.
   - Query RMQ on range `[r1, r2 - 1]`. Note the `-1` because `lcp[k]` describes the overlap between `sa[k]` and `sa[k+1]`. The interval between `r1` and `r2` involves `lcp[r1], lcp[r1+1]...lcp[r2-1]`.

### Time Complexity

- **Preprocessing:** O(N log N) for SA and Sparse Table.
- **Query:** O(1).
- **Total:** O((N + Q) log N) or O(N log N + Q).

### Space Complexity

- **O(N log N)**: For the Sparse Table.

![Algorithm Visualization](../images/STC-010/algorithm-visualization.png)
![Algorithm Steps](../images/STC-010/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    int[][] st;
    int[] logs;
    int[] rank;
    int n;

    public int[] lcpQueries(String s, int[][] queries) {
        n = s.length();
        buildSA(s);
        int[] lcp = buildLCP(s);
        buildSparseTable(lcp);
        
        int[] ans = new int[queries.length];
        for (int k = 0; k < queries.length; k++) {
            int i = queries[k][0];
            int j = queries[k][1];
            if (i == j) {
                ans[k] = n - i;
            } else {
                int r1 = rank[i];
                int r2 = rank[j];
                if (r1 > r2) {
                    int temp = r1; r1 = r2; r2 = temp;
                }
                ans[k] = query(r1, r2 - 1);
            }
        }
        return ans;
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
        n = len(s)
        if n == 0:
            return [0] * len(queries)
            
        # 1. Build SA
        sa = list(range(n))
        rank = [ord(c) for c in s]
        new_rank = [0] * n
        
        k = 1
        while k < n:
            key_func = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
            sa.sort(key=key_func)
            
            new_rank[sa[0]] = 0
            for i in range(1, n):
                prev = sa[i-1]
                curr = sa[i]
                if key_func(prev) == key_func(curr):
                    new_rank[curr] = new_rank[prev]
                else:
                    new_rank[curr] = new_rank[prev] + 1
            
            rank = list(new_rank)
            if rank[sa[n-1]] == n - 1:
                break
            k *= 2
            
        # 2. Build LCP
        lcp = [0] * (n - 1)
        k_val = 0
        for i in range(n):
            if rank[i] == n - 1:
                k_val = 0
                continue
            j = sa[rank[i] + 1]
            while i + k_val < n and j + k_val < n and s[i + k_val] == s[j + k_val]:
                k_val += 1
            lcp[rank[i]] = k_val
            if k_val > 0:
                k_val -= 1
                
        # 3. Build Sparse Table
        m = len(lcp)
        if m == 0:
            return [n - q[0] if q[0] == q[1] else 0 for q in queries]
            
        logs = [0] * (m + 1)
        for i in range(2, m + 1):
            logs[i] = logs[i // 2] + 1
            
        K = logs[m]
        st = [[0] * m for _ in range(K + 1)]
        for i in range(m):
            st[0][i] = lcp[i]
            
        for k in range(1, K + 1):
            for i in range(m - (1 << k) + 1):
                st[k][i] = min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))])
                
        def query(L, R):
            if L > R: return 0
            j = logs[R - L + 1]
            return min(st[j][L], st[j][R - (1 << j) + 1])
            
        ans = []
        for i, j in queries:
            if i == j:
                ans.append(n - i)
            else:
                r1 = rank[i]
                r2 = rank[j]
                if r1 > r2:
                    r1, r2 = r2, r1
                ans.append(query(r1, r2 - 1))
        return ans

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
        int n = s.length();
        if (n == 0) return vector<int>(queries.size(), 0);
        
        // Build SA
        vector<int> sa(n), newRank(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s[i];
        }
        
        for (int k = 1; k < n; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < n) ? rank[i + k] : -1;
                int rj = (j + k < n) ? rank[j + k] : -1;
                return ri < rj;
            };
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                if (cmp(sa[i - 1], sa[i])) newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                else newRank[sa[i]] = newRank[sa[i - 1]];
            }
            rank = newRank;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        // Build LCP
        vector<int> lcp(n - 1);
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // Build Sparse Table
        int m = lcp.size();
        if (m > 0) {
            logs.resize(m + 1);
            logs[1] = 0;
            for (int i = 2; i <= m; i++) logs[i] = logs[i / 2] + 1;
            
            int K = logs[m];
            st.assign(K + 1, vector<int>(m));
            for (int i = 0; i < m; i++) st[0][i] = lcp[i];
            
            for (int j = 1; j <= K; j++) {
                for (int i = 0; i + (1 << j) <= m; i++) {
                    st[j][i] = min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
                }
            }
        }
        
        vector<int> ans;
        for (auto& q : queries) {
            int i = q.first;
            int j = q.second;
            if (i == j) {
                ans.push_back(n - i);
            } else {
                int r1 = rank[i];
                int r2 = rank[j];
                if (r1 > r2) swap(r1, r2);
                
                if (m == 0) ans.push_back(0);
                else {
                    int L = r1;
                    int R = r2 - 1;
                    int lg = logs[R - L + 1];
                    ans.push_back(min(st[lg][L], st[lg][R - (1 << lg) + 1]));
                }
            }
        }
        return ans;
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
    const n = s.length;
    if (n === 0) return new Array(queries.length).fill(0);
    
    // Build SA
    let sa = new Array(n).fill(0).map((_, i) => i);
    let rank = new Array(n).fill(0).map((_, i) => s.charCodeAt(i));
    let newRank = new Array(n).fill(0);
    
    for (let k = 1; k < n; k *= 2) {
      sa.sort((i, j) => {
        if (rank[i] !== rank[j]) return rank[i] - rank[j];
        const ri = (i + k < n) ? rank[i + k] : -1;
        const rj = (j + k < n) ? rank[j + k] : -1;
        return ri - rj;
      });
      
      newRank[sa[0]] = 0;
      for (let i = 1; i < n; i++) {
        const prev = sa[i - 1];
        const curr = sa[i];
        const r1 = rank[prev];
        const r2 = (prev + k < n) ? rank[prev + k] : -1;
        const r3 = rank[curr];
        const r4 = (curr + k < n) ? rank[curr + k] : -1;
        
        if (r1 === r3 && r2 === r4) newRank[curr] = newRank[prev];
        else newRank[curr] = newRank[prev] + 1;
      }
      for (let i = 0; i < n; i++) rank[i] = newRank[i];
      if (rank[sa[n - 1]] === n - 1) break;
    }
    
    // Build LCP
    const lcp = new Array(n - 1).fill(0);
    let kVal = 0;
    for (let i = 0; i < n; i++) {
      if (rank[i] === n - 1) {
        kVal = 0;
        continue;
      }
      const j = sa[rank[i] + 1];
      while (i + kVal < n && j + kVal < n && s[i + kVal] === s[j + kVal]) {
        kVal++;
      }
      lcp[rank[i]] = kVal;
      if (kVal > 0) kVal--;
    }
    
    // Build Sparse Table
    const m = lcp.length;
    if (m === 0) {
        return queries.map(([i, j]) => i === j ? n - i : 0);
    }
    
    const logs = new Array(m + 1).fill(0);
    for (let i = 2; i <= m; i++) logs[i] = logs[Math.floor(i / 2)] + 1;
    
    const K = logs[m];
    const st = new Array(K + 1).fill(0).map(() => new Array(m).fill(0));
    for (let i = 0; i < m; i++) st[0][i] = lcp[i];
    
    for (let k = 1; k <= K; k++) {
      for (let i = 0; i + (1 << k) <= m; i++) {
        st[k][i] = Math.min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
      }
    }
    
    const query = (L, R) => {
      if (L > R) return 0;
      const j = logs[R - L + 1];
      return Math.min(st[j][L], st[j][R - (1 << j) + 1]);
    };
    
    const ans = [];
    for (const [i, j] of queries) {
      if (i === j) {
        ans.push(n - i);
      } else {
        let r1 = rank[i];
        let r2 = rank[j];
        if (r1 > r2) {
          const temp = r1; r1 = r2; r2 = temp;
        }
        ans.push(query(r1, r2 - 1));
      }
    }
    return ans;
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

## 🧪 Test Case Walkthrough (Dry Run)

`s = "banana"`
SA: `[5, 3, 1, 0, 4, 2]`
LCP: `[1, 3, 0, 0, 2]`
Ranks: `rank[0]=3`, `rank[1]=2`, `rank[2]=5`, `rank[3]=1`, `rank[4]=4`, `rank[5]=0`.

Query `(1, 3)`:
`r1 = rank[1] = 2`
`r2 = rank[3] = 1`
Swap: `r1=1, r2=2`.
Query RMQ on `lcp[1...1]`.
`lcp[1] = 3`.
Answer: 3. Correct ("ana").

Query `(0, 2)`:
`r1 = rank[0] = 3`
`r2 = rank[2] = 5`
Query RMQ on `lcp[3...4]`.
`lcp[3]=0`, `lcp[4]=2`. Min is 0.
Answer: 0. Correct.

![Example Visualization](../images/STC-010/example-1.png)

## ✅ Proof of Correctness

### Invariant

The LCP of any two suffixes `u` and `v` is the minimum LCP value in the interval between their ranks in the sorted Suffix Array.
This is a fundamental property of Suffix Arrays.
Since we query the range `[min_rank, max_rank - 1]`, we cover all adjacent LCP values between the two suffixes. The minimum of these adjacent LCPs is the LCP of the endpoints.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Longest Common Substring of K Strings**
  - Concatenate all strings with unique separators. Build SA/LCP. Use sliding window + RMQ.

- **Extension 2: Dynamic Updates**
  - If string changes, SA/LCP is hard to update. Suffix Tree or dynamic string structures are needed.

### Common Mistakes to Avoid

1. **Query Range Error**
   - ❌ Querying `[r1, r2]`.
   - ✅ Querying `[r1, r2 - 1]`. The LCP array has size `N-1`. `lcp[k]` is between `sa[k]` and `sa[k+1]`.

2. **Rank vs Index**
   - ❌ Using `i` and `j` directly in RMQ.
   - ✅ Must map to `rank[i]` and `rank[j]`.

3. **Sparse Table Size**
   - ❌ Not allocating enough rows for `log N`.
   - ✅ `K = floor(log2(N))`.

## Related Concepts

- **LCA**: Lowest Common Ancestor in trees.
- **Cartesian Tree**: Can convert RMQ to LCA.
- **Segment Tree**: Alternative to Sparse Table (O(N) build, O(log N) query, but supports updates).
