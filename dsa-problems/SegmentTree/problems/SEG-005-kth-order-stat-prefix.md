---
problem_id: SEG_KTH_ORDER_STAT_PREFIX__7093
display_id: SEG-005
slug: kth-order-stat-prefix
title: "K-th Order Statistic in Prefix"
difficulty: Medium
difficulty_score: 57
topics:
  - Segment Tree
  - Persistent Data Structures
  - Order Statistics
tags:
  - segment-tree
  - persistent
  - kth-statistic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-005: K-th Order Statistic in Prefix

## Problem Statement

Given an array `a`, answer queries of the form `PREFIX r k`: find the k-th smallest value in the prefix `a[0..r]`.

All indices are 0-based. It is guaranteed that `1 <= k <= r+1`.

![Problem Illustration](../images/SEG-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `PREFIX r k`

## Output Format

- For each query, output the k-th smallest value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4 1
5 1 3 2
PREFIX 3 2
```

**Output:**

```
2
```

**Explanation:**

The prefix is `[5,1,3,2]`, sorted as `[1,2,3,5]`, so the 2nd smallest is 2.

![Example Visualization](../images/SEG-005/example-1.png)

## Notes

- Coordinate-compress values for the segment tree domain
- Build a persistent segment tree for each prefix
- Query the tree to find the k-th smallest
- Time per query: O(log n)

## Related Topics

Persistent Segment Tree, Order Statistics, Prefix Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processQueries(int n, int q, long[] a, int[] r, int[] k) {
        // Implement here
        // For each query, output the k-th smallest value
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextLong();
            int[] rs = new int[q];
            int[] ks = new int[q];
            for (int i = 0; i < q; i++) {
                String cmd = sc.next();
                rs[i] = sc.nextInt();
                ks[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            sol.processQueries(n, q, a, rs, ks);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_queries(self, n, q, a, queries):
        # Implement here
        # For each query, print the k-th smallest value
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    a = [int(x) for x in input_data[2:2+n]]
    queries = []
    ptr = 2 + n
    for _ in range(q):
        cmd = input_data[ptr]
        r = int(input_data[ptr+1])
        k = int(input_data[ptr+2])
        queries.append((r, k))
        ptr += 3

    sol = Solution()
    sol.process_queries(n, q, a, queries)

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
    void processQueries(int n, int q, const vector<long long>& a, const vector<pair<int, int>>& queries) {
        // Implement here
        // For each query, cout << kth_val << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (cin >> n >> q) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        vector<pair<int, int>> queries(q);
        for (int i = 0; i < q; i++) {
            string cmd;
            cin >> cmd >> queries[i].first >> queries[i].second;
        }

        Solution sol;
        sol.processQueries(n, q, a, queries);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processQueries(n, q, a, queries) {
    // Implement here
    // For each query, console.log(kth_val.toString());
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const q = parseInt(input[1]);
  const a = input.slice(2, 2 + n).map(BigInt);
  const queries = [];
  let ptr = 2 + n;
  for (let i = 0; i < q; i++) {
    const r = parseInt(input[ptr + 1]);
    const k = parseInt(input[ptr + 2]);
    queries.push({ r, k });
    ptr += 3;
  }

  const sol = new Solution();
  sol.processQueries(n, q, a, queries);
});
```
