---
title: K Smallest Prefix Updates
slug: k-smallest-prefix-updates
difficulty: Medium
difficulty_score: 50
tags:
- Segment Tree
- Range Assignment
- Prefix Updates
problem_id: SEG_K_SMALLEST_PREFIX_UPDATES__9461
display_id: SEG-014
topics:
- Segment Tree
- Range Assignment
- Prefix Updates
---
# K Smallest Prefix Updates - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SETPREFIX k x**: Set `a[0..k-1] = x`.
2.  **SUM l r**: Calculate the sum of `a[l..r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= n`
## Real-World Scenario

Imagine a **Budget Allocation System**.
-   You have a list of departments or projects.
-   **SETPREFIX**: The CEO decides to reset the budget for the top `k` priority projects to a fixed amount `x`.
-   **SUM**: You need to calculate the total budget for a range of projects (e.g., a specific division).

## Problem Exploration

### 1. Range Assignment
This is a standard **Range Assignment** problem, but restricted to prefixes.
-   Prefix assignment is just `update(0, k-1, x)`.
-   Range Sum is standard.

### 2. Segment Tree with Lazy Propagation
-   We need a Segment Tree that supports range set updates and range sum queries.
-   **Lazy Tag**: `lazy_set`.
    -   If `lazy_set != -1` (or some sentinel), it means all elements in this range are set to `lazy_set`.
    -   When pushing down, update children's values and lazy tags.
    -   Sum of a range `[L, R]` with set value `v` is `(R - L + 1) * v`.

### 3. Sentinel Value
-   Since values can be anything (including negative), we need a robust sentinel.
-   Or use a boolean flag `has_lazy`.

## Approaches

### Approach 1: Segment Tree with Lazy Propagation
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: `O(log N)`.
-   Space: `O(N)`.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class Node {
        long sum;
        long lazySet;
        boolean hasLazy;
        
        Node() {
            lazySet = 0;
            hasLazy = false;
        }
    }
    
    private Node[] tree;
    private int n;

    public List<Long> process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Node[4 * n];
        for(int i=0; i<4*n; i++) tree[i] = new Node();
        
        build(arr, 0, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SETPREFIX")) {
                int k = Integer.parseInt(op[1]);
                long x = Long.parseLong(op[2]);
                if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void push(int node, int start, int end) {
        if (tree[node].hasLazy) {
            int mid = (start + end) / 2;
            long val = tree[node].lazySet;
            
            tree[2 * node + 1].lazySet = val;
            tree[2 * node + 1].hasLazy = true;
            tree[2 * node + 1].sum = val * (mid - start + 1);
            
            tree[2 * node + 2].lazySet = val;
            tree[2 * node + 2].hasLazy = true;
            tree[2 * node + 2].sum = val * (end - mid);
            
            tree[node].hasLazy = false;
        }
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node].sum = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
        }
    }

    private void update(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].lazySet = val;
            tree[node].hasLazy = true;
            tree[node].sum = val * (end - start + 1);
            return;
        }
        
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
    }
}

class Main {
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
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
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
        # Tree stores (sum, lazy_val, has_lazy)
        tree_sum = [0] * (4 * n)
        tree_lazy = [0] * (4 * n)
        tree_has_lazy = [False] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree_sum[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree_sum[node] = tree_sum[2 * node + 1] + tree_sum[2 * node + 2]

        def push(node, start, end):
            if tree_has_lazy[node]:
                mid = (start + end) // 2
                val = tree_lazy[node]
                
                # Left child
                tree_lazy[2 * node + 1] = val
                tree_has_lazy[2 * node + 1] = True
                tree_sum[2 * node + 1] = val * (mid - start + 1)
                
                # Right child
                tree_lazy[2 * node + 2] = val
                tree_has_lazy[2 * node + 2] = True
                tree_sum[2 * node + 2] = val * (end - mid)
                
                tree_has_lazy[node] = False

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                tree_lazy[node] = val
                tree_has_lazy[node] = True
                tree_sum[node] = val * (end - start + 1)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node + 1, start, mid, l, r, val)
            update(2 * node + 2, mid + 1, end, l, r, val)
            tree_sum[node] = tree_sum[2 * node + 1] + tree_sum[2 * node + 2]

        def query(node, start, end, l, r):
            if l > end or r < start:
                return 0
            if l <= start and end <= r:
                return tree_sum[node]
            
            push(node, start, end)
            mid = (start + end) // 2
            return query(2 * node + 1, start, mid, l, r) + \
                   query(2 * node + 2, mid + 1, end, l, r)

        build(0, 0, n - 1)
        results = []
        
        for op in ops:
            if op[0] == "SETPREFIX":
                k = int(op[1])
                x = int(op[2])
                if k > 0:
                    update(0, 0, n - 1, 0, k - 1, x)
            else:
                l = int(op[1])
                r = int(op[2])
                results.append(query(0, 0, n - 1, l, r))
                
        return results

def main():
    import sys
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
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
#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Node {
    long long sum;
    long long lazySet;
    bool hasLazy;
};

class Solution {
    vector<Node> tree;
    int n;

    void push(int node, int start, int end) {
        if (tree[node].hasLazy) {
            int mid = (start + end) / 2;
            long long val = tree[node].lazySet;
            
            tree[2 * node + 1].lazySet = val;
            tree[2 * node + 1].hasLazy = true;
            tree[2 * node + 1].sum = val * (mid - start + 1);
            
            tree[2 * node + 2].lazySet = val;
            tree[2 * node + 2].hasLazy = true;
            tree[2 * node + 2].sum = val * (end - mid);
            
            tree[node].hasLazy = false;
        }
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = {arr[start], 0, false};
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = {tree[2 * node + 1].sum + tree[2 * node + 2].sum, 0, false};
        }
    }

    void update(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].lazySet = val;
            tree[node].hasLazy = true;
            tree[node].sum = val * (end - start + 1);
            return;
        }
        
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, {0, 0, false});
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "SETPREFIX") {
                int k = stoi(op[1]);
                long long x = stoll(op[2]);
                if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                results.push_back(query(0, 0, n - 1, l, r));
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
        string type, a, b;
        cin >> type >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
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
    
    // Parallel arrays for performance
    const treeSum = new Float64Array(4 * n);
    const treeLazy = new Float64Array(4 * n);
    const treeHasLazy = new Int8Array(4 * n); // 0 or 1

    const build = (node, start, end) => {
      if (start === end) {
        treeSum[node] = arr[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        treeSum[node] = treeSum[2 * node + 1] + treeSum[2 * node + 2];
      }
    };

    const push = (node, start, end) => {
      if (treeHasLazy[node]) {
        const mid = Math.floor((start + end) / 2);
        const val = treeLazy[node];
        
        // Left
        treeLazy[2 * node + 1] = val;
        treeHasLazy[2 * node + 1] = 1;
        treeSum[2 * node + 1] = val * (mid - start + 1);
        
        // Right
        treeLazy[2 * node + 2] = val;
        treeHasLazy[2 * node + 2] = 1;
        treeSum[2 * node + 2] = val * (end - mid);
        
        treeHasLazy[node] = 0;
      }
    };

    const update = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        treeLazy[node] = val;
        treeHasLazy[node] = 1;
        treeSum[node] = val * (end - start + 1);
        return;
      }
      
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      update(2 * node + 1, start, mid, l, r, val);
      update(2 * node + 2, mid + 1, end, l, r, val);
      treeSum[node] = treeSum[2 * node + 1] + treeSum[2 * node + 2];
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return 0;
      if (l <= start && end <= r) return treeSum[node];
      
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      return query(2 * node + 1, start, mid, l, r) + 
             query(2 * node + 2, mid + 1, end, l, r);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "SETPREFIX") {
        const k = parseInt(op[1], 10);
        const x = parseInt(op[2], 10);
        if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        results.push(query(0, 0, n - 1, l, r));
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
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
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
`3 2`
`1 2 3`
`SETPREFIX 2 5`
`SUM 0 2`

1.  **Initial**: `[1, 2, 3]`. Sum = 6.
2.  **SETPREFIX 2 5**: Set `a[0..1]` to 5.
    -   Array becomes `[5, 5, 3]`.
    -   Segment tree updates range `[0, 1]`.
3.  **SUM 0 2**:
    -   Sum `5 + 5 + 3 = 13`.

## Proof of Correctness

-   **Lazy Propagation**: Ensures updates are efficient (`O(log N)`) and correctly applied to sub-ranges when queried.
-   **Prefix as Range**: Treating prefix update as `[0, k-1]` update maps problem to standard Range Assignment.

## Interview Extensions

1.  **Range Add + Range Set?**
    -   Need two lazy tags. Order matters (Set overrides Add).
2.  **History Sum?**
    -   Persistent Segment Tree or specialized tags.

### Common Mistakes

-   **Lazy Flag**: Forgetting `hasLazy` and assuming `lazy=0` means no update (0 is a valid value to set).
-   **Push Order**: Push before recursing children in both update and query.
