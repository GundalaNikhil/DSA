---
title: Range Minimum Index
slug: range-min-index
difficulty: Medium
difficulty_score: 45
tags:
- Segment Tree
- Range Minimum Query
- Tie Breaking
problem_id: SEG_RANGE_MIN_INDEX__3926
display_id: SEG-011
topics:
- Segment Tree
- Range Queries
- Tie Breaking
---
# Range Minimum Index - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SET i x**: Update `a[i] = x`.
2.  **MINIDX l r**: Find the index of the minimum value in `a[l..r]`. If there are ties, return the smallest index.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Task Scheduler**.
-   You have a list of servers, each with a current load.
-   You want to assign a new task to the server with the **minimum load**.
-   If multiple servers have the same minimum load, you pick the one with the lowest ID (index) to maintain a consistent tie-breaking rule.
-   Server loads change dynamically as tasks finish or start.

## Problem Exploration

### 1. Standard RMQ
Standard Range Minimum Query (RMQ) returns the minimum *value*.
Here we need the *index*.
We can store pairs `(value, index)` in the Segment Tree nodes.

### 2. Merge Logic
When merging two nodes `left` and `right`:
-   If `left.value < right.value`: result is `left`.
-   If `right.value < left.value`: result is `right`.
-   If `left.value == right.value`: result is `left` (since `left.index < right.index`).

### 3. Segment Tree Structure
-   Leaf `i`: stores `(a[i], i)`.
-   Internal Node: stores `min(left, right)` based on the comparison logic above.
-   Query: Standard range query returning the best pair.

## Approaches

### Approach 1: Segment Tree with Pairs
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: `O(log N)`.
-   Space: `O(N)`.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Pair {
        long val;
        int idx;
        
        Pair(long val, int idx) {
            this.val = val;
            this.idx = idx;
        }
    }
    
    private Pair[] tree;
    private int n;

    public int[] process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Pair[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                long val = Long.parseLong(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                Pair res = query(0, 0, n - 1, l, r);
                results.add(res.idx);
            }
        }
        
        int[] out = new int[results.size()];
        for (int i = 0; i < results.size(); i++) out[i] = results.get(i);
        return out;
    }

    private Pair merge(Pair p1, Pair p2) {
        if (p1.val < p2.val) return p1;
        if (p2.val < p1.val) return p2;
        return p1.idx < p2.idx ? p1 : p2;
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Pair(arr[start], start);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, long val) {
        if (start == end) {
            tree[node] = new Pair(val, idx);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private Pair query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Pair(Long.MAX_VALUE, -1);
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Pair p1 = query(2 * node + 1, start, mid, l, r);
        Pair p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                ops.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, ops);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        n = len(arr)
        # Tree stores tuples (val, index)
        tree = [(0, 0)] * (4 * n)
        
        def merge(p1, p2):
            if p1[0] < p2[0]:
                return p1
            elif p2[0] < p1[0]:
                return p2
            else:
                return p1 if p1[1] < p2[1] else p2

        def build(node, start, end):
            if start == end:
                tree[node] = (arr[start], start)
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = (val, idx)
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    update(2 * node + 1, start, mid, idx, val)
                else:
                    update(2 * node + 2, mid + 1, end, idx, val)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def query(node, start, end, l, r):
            if l > end or r < start:
                return (float('inf'), -1)
            if l <= start and end <= r:
                return tree[node]
            
            mid = (start + end) // 2
            p1 = query(2 * node + 1, start, mid, l, r)
            p2 = query(2 * node + 2, mid + 1, end, l, r)
            return merge(p1, p2)

        build(0, 0, n - 1)
        results = []
        for op in ops:
            if op[0] == "SET":
                idx = int(op[1])
                val = int(op[2])
                update(0, 0, n - 1, idx, val)
            else:
                l, r = int(op[1]), int(op[2])
                res = query(0, 0, n - 1, l, r)
                results.append(res[1])
        return results

def main():
    import sys
    sys.setrecursionlimit(300000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        type = next(it)
        ops.append([type, next(it), next(it)])
    
    sol = Solution()
    results = sol.process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

struct Pair {
    long long val;
    int idx;
    
    bool operator<(const Pair& other) const {
        if (val != other.val) return val < other.val;
        return idx < other.idx;
    }
};

class Solution {
    vector<Pair> tree;
    int n;

    Pair merge(const Pair& p1, const Pair& p2) {
        if (p1.val < p2.val) return p1;
        if (p2.val < p1.val) return p2;
        return p1.idx < p2.idx ? p1 : p2;
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = {arr[start], start};
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = {val, idx};
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    Pair query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return {LLONG_MAX, -1};
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Pair p1 = query(2 * node + 1, start, mid, l, r);
        Pair p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
    }

public:
    vector<int> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
        n = inputArr.size();
        tree.assign(4 * n, {LLONG_MAX, -1});
        
        build(inputArr, 0, 0, n - 1);
        
        vector<int> results;
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                long long val = stoll(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                Pair res = query(0, 0, n - 1, l, r);
                results.push_back(res.idx);
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        string a, b;
        cin >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<int> results = sol.process(arr, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(arr, ops) {
    const n = arr.length;
    
    // We can't easily store objects in a typed array, so we use parallel arrays or objects.
    // Objects are fine for N=200k in JS usually, but parallel arrays are faster.
    // Let's use objects for clarity as per template.
    
    const tree = new Array(4 * n);

    const merge = (p1, p2) => {
      if (p1.val < p2.val) return p1;
      if (p2.val < p1.val) return p2;
      return p1.idx < p2.idx ? p1 : p2;
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = { val: arr[start], idx: start };
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = { val: val, idx: idx };
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return { val: BigInt("999999999999999999999"), idx: -1 };
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node + 1, start, mid, l, r);
      const p2 = query(2 * node + 2, mid + 1, end, l, r);
      return merge(p1, p2);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "SET") {
        const idx = parseInt(op[1], 10);
        const val = BigInt(op[2]);
        update(0, 0, n - 1, idx, val);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const res = query(0, 0, n - 1, l, r);
        results.push(res.idx);
      }
    }
    return results;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(BigInt(data[idx++]));
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    ops.push([type, data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`4 2 2`
`MINIDX 0 2`

1.  **Build**:
    -   Leaves: `(4, 0)`, `(2, 1)`, `(2, 2)`.
    -   Root merges `(2, 1)` and `(2, 2)`.
    -   Values equal (2 == 2). Indices 1 < 2. Pick `(2, 1)`.
2.  **Query**: `MINIDX 0 2`.
    -   Returns `(2, 1)`.
3.  **Result**: 1.

## Proof of Correctness

-   **Merge Logic**: Correctly implements strict inequality for values and tie-breaking with indices.
-   **Segment Tree**: Standard structure guarantees `O(log N)` operations.

## Interview Extensions

1.  **Range Max Index?**
    -   Same logic, just flip comparison.
2.  **K-th Smallest Index?**
    -   Harder. Requires Merge Sort Tree or Persistent Segment Tree.
3.  **First Element < X?**
    -   Segment Tree Walk. Check if `min(left) < X`. If so, go left, else go right.

### Common Mistakes

-   **Tie-Breaking**: Forgetting to check indices when values are equal.
-   **Infinity**: Use a sufficiently large value for out-of-bounds queries.
