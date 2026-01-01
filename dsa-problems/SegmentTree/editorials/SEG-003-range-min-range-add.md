---
title: Range Minimum with Range Add
slug: range-min-range-add
difficulty: Medium
difficulty_score: 48
tags:
- Segment Tree
- Range Minimum Query
- Lazy Propagation
problem_id: SEG_RANGE_MIN_RANGE_ADD__3915
display_id: SEG-003
topics:
- Segment Tree
- Lazy Propagation
- Range Updates
---
# Range Minimum with Range Add - Editorial

## Problem Summary

You are given an array and need to support two operations:
1.  **ADD l r x**: Add value `x` to all elements in the range `[l, r]`.
2.  **MIN l r**: Find the minimum value in the range `[l, r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Temperature Monitoring System**.
-   **Range Add**: A heatwave increases the temperature of all sensors in a specific region (indices `l` to `r`) by `x` degrees.
-   **Range Min**: You want to find the coolest spot in a region to direct emergency cooling resources.

## Problem Exploration

### 1. Segment Tree with Lazy Propagation
Similar to the "Range Add, Range Sum" problem, we need a Segment Tree with Lazy Propagation.
The key difference is the aggregation function: instead of maintaining the `sum`, we maintain the `min`.

### 2. Node Structure
-   `min_val`: The minimum value in the node's range.
-   `lazy`: The pending addition value to be propagated to children.

### 3. Update Logic
When adding `x` to a range:
-   Update `min_val`: `min_val += x`. (Adding `x` to every element increases the minimum by exactly `x`).
-   Update `lazy`: `lazy += x`.

### 4. Push Logic
When pushing `lazy` to children:
-   Left child: `min_val += lazy`, `lazy += lazy`.
-   Right child: `min_val += lazy`, `lazy += lazy`.
-   Reset current `lazy` to 0.

## Approaches

### Approach 1: Segment Tree with Lazy Propagation
-   **Build**: `O(N)`. Compute min of children.
-   **Update**: `O(log N)`. Add to min and lazy.
-   **Query**: `O(log N)`. Return min of relevant segments.
-   **Space**: `O(4N)`.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private long[] tree;
    private long[] lazy;
    private int n;

    public List<Long> process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new long[4 * n];
        lazy = new long[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            String type = op[0];
            if (type.equals("ADD")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long x = Long.parseLong(op[3]);
                update(0, 0, n - 1, l, r, x);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void push(int node) {
        if (lazy[node] != 0) {
            // Left child
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            
            // Right child
            tree[2 * node + 2] += lazy[node];
            lazy[2 * node + 2] += lazy[node];
            
            lazy[node] = 0;
        }
    }

    private void update(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;

        if (l <= start && end <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }

        push(node);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Long.MAX_VALUE;

        if (l <= start && end <= r) {
            return tree[node];
        }

        push(node);
        int mid = (start + end) / 2;
        return Math.min(query(2 * node + 1, start, mid, l, r),
                        query(2 * node + 2, mid + 1, end, l, r));
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
                if (type.equals("ADD")) {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
                if (res == Long.MAX_VALUE) {
                    System.out.println("inf");
                } else {
                    System.out.println(res);
                }
            }
        }
        sc.close();
    }
}
```

### Python
```python
import sys

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)
    INF = float('inf')

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = min(tree[2 * node + 1], tree[2 * node + 2])

    def push(node):
        if lazy[node] != 0:
            tree[2 * node + 1] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
            
            tree[2 * node + 2] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
            
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            tree[node] += val
            lazy[node] += val
            return

        push(node)
        mid = (start + end) // 2
        update(2 * node + 1, start, mid, l, r, val)
        update(2 * node + 2, mid + 1, end, l, r, val)
        tree[node] = min(tree[2 * node + 1], tree[2 * node + 2])

    def query(node, start, end, l, r):
        if l > end or r < start:
            return INF
        
        if l <= start and end <= r:
            return tree[node]
        
        push(node)
        mid = (start + end) // 2
        return min(query(2 * node + 1, start, mid, l, r),
                   query(2 * node + 2, mid + 1, end, l, r))

    build(0, 0, n - 1)
    results = []
    
    for op in ops:
        if op[0] == "ADD":
            l, r, x = int(op[1]), int(op[2]), int(op[3])
            update(0, 0, n - 1, l, r, x)
        else:
            l, r = int(op[1]), int(op[2])
            results.append(query(0, 0, n - 1, l, r))
            
    return results

def main():
    import sys
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
        if type == "ADD":
            ops.append([type, next(it), next(it), next(it)])
        else:
            ops.append([type, next(it), next(it)])
    
    results = process(arr, ops)
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

class Solution {
    vector<long long> tree;
    vector<long long> lazy;
    int n;

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = min(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void push(int node) {
        if (lazy[node] != 0) {
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            
            tree[2 * node + 2] += lazy[node];
            lazy[2 * node + 2] += lazy[node];
            
            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;

        if (l <= start && end <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }

        push(node);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node] = min(tree[2 * node + 1], tree[2 * node + 2]);
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return LLONG_MAX;

        if (l <= start && end <= r) {
            return tree[node];
        }

        push(node);
        int mid = (start + end) / 2;
        return min(query(2 * node + 1, start, mid, l, r),
                   query(2 * node + 2, mid + 1, end, l, r));
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "ADD") {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                long long x = stoll(op[3]);
                update(0, 0, n - 1, l, r, x);
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
        string type;
        cin >> type;
        if (type == "ADD") {
            string l, r, x;
            cin >> l >> r >> x;
            ops[i] = {type, l, r, x};
        } else {
            string l, r;
            cin >> l >> r;
            ops[i] = {type, l, r};
        }
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        if (res == LLONG_MAX) {
            cout << "inf\n";
        } else {
            cout << res << "\n";
        }
    }
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  process(arr, ops) {
    const n = arr.length;
    // Using BigInt because values can exceed 2^53
    // But Math.min doesn't work with BigInt directly in older envs.
    // Assuming modern env or manual comparison.
    // However, problem constraints say -10^9 to 10^9, adding up to 200000 times.
    // Max value approx 2*10^14, which fits in standard JS Number (2^53 is 9*10^15).
    // So Number is safe.
    
    const tree = new Float64Array(4 * n);
    const lazy = new Float64Array(4 * n);
    const INF = Number.MAX_SAFE_INTEGER;

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = arr[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const push = (node) => {
      if (lazy[node] !== 0) {
        tree[2 * node + 1] += lazy[node];
        lazy[2 * node + 1] += lazy[node];
        
        tree[2 * node + 2] += lazy[node];
        lazy[2 * node + 2] += lazy[node];
        
        lazy[node] = 0;
      }
    };

    const update = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;

      if (l <= start && end <= r) {
        tree[node] += val;
        lazy[node] += val;
        return;
      }

      push(node);
      const mid = Math.floor((start + end) / 2);
      update(2 * node + 1, start, mid, l, r, val);
      update(2 * node + 2, mid + 1, end, l, r, val);
      tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return INF;

      if (l <= start && end <= r) {
        return tree[node];
      }

      push(node);
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node + 1, start, mid, l, r),
                      query(2 * node + 2, mid + 1, end, l, r));
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "ADD") {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const x = parseInt(op[3], 10);
        update(0, 0, n - 1, l, r, x);
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
    const op = data[idx++];
    if (op === "ADD") {
      ops.push([op, data[idx++], data[idx++], data[idx++]]);
    } else {
      ops.push([op, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops).map(val => (val === Number.MAX_SAFE_INTEGER ? "inf" : val));
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 2`
`3 1 4`
1.  `ADD 0 2 2`:
    -   Add 2 to `[0, 2]`.
    -   Root `[0, 2]` covers fully. `min` becomes `min(3,1,4)+2 = 1+2 = 3`. `lazy` += 2.
    -   Array effectively `[5, 3, 6]`.
2.  `MIN 1 2`:
    -   Query `[1, 2]`.
    -   Push root lazy (2) to children.
        -   Left `[0, 1]`: `min` was `min(3,1)=1`. Becomes `1+2=3`. `lazy`=2.
        -   Right `[2, 2]`: `min` was 4. Becomes `4+2=6`. `lazy`=2.
    -   Query `[1, 2]` splits:
        -   Left child `[0, 1]` intersects `[1, 1]`. Recurse.
            -   Push lazy (2) to `[0, 0]` and `[1, 1]`.
            -   `[1, 1]` min becomes `1+2=3`.
            -   Return 3.
        -   Right child `[2, 2]` intersects `[2, 2]`.
            -   Return 6.
    -   Result `min(3, 6) = 3`.

**Output:**
3

## Proof of Correctness

-   **Lazy Propagation**: Ensures updates are efficient (`O(log N)`).
-   **Min Property**: `min(A + x) = min(A) + x`. This property allows us to update the node's `min_val` directly by adding `x` without needing to know the distribution of values in the subtree. This is crucial. If the operation were `Set` or `Multiply` (with negative numbers), it would be more complex.

## Interview Extensions

1.  **Range Set to Value?**
    -   `min_val = x`. `lazy_set = x`. Need to handle precedence if mixing Add and Set.
2.  **Range Max?**
    -   Symmetric to Range Min.
3.  **Range Add, Range Min Count?**
    -   Store `{min_val, count}` in each node. When combining, if left.min < right.min, take left; if equal, sum counts.

### Common Mistakes

-   **Initial Query Value**: Use `INFINITY` (or `LLONG_MAX`) for out-of-bounds queries, not 0.
-   **Push Order**: Always push before recursing to children.
