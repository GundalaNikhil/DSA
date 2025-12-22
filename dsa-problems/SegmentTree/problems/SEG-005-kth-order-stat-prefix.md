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
    public int[] kthPrefix(int[] arr, int[][] queries) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            sc.next();
            queries[i][0] = sc.nextInt();
            queries[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] out = solution.kthPrefix(arr, queries);
        for (int v : out) System.out.println(v);
        sc.close();
    }
}
```

### Python

```python
def kth_prefix(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        _ = next(it)
        r = int(next(it))
        k = int(next(it))
        queries.append((r, k))

    out = kth_prefix(arr, queries)
    sys.stdout.write("\n".join(str(x) for x in out))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> kthPrefix(const vector<int>& arr, const vector<pair<int,int>>& queries) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<pair<int,int>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        int r, k;
        cin >> r >> k;
        queries.push_back({r, k});
    }

    Solution solution;
    vector<int> out = solution.kthPrefix(arr, queries);
    for (int v : out) cout << v << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kthPrefix(arr, queries) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const queries = [];
  for (let i = 0; i < q; i++) {
    idx++;
    const r = parseInt(data[idx++], 10);
    const k = parseInt(data[idx++], 10);
    queries.push([r, k]);
  }

  const solution = new Solution();
  const out = solution.kthPrefix(arr, queries);
  console.log(out.join("\n"));
});
```
