---
title: Range Add, Range Sum
slug: range-add-range-sum
difficulty: Medium
difficulty_score: 46
tags:
- Segment Tree
- Lazy Propagation
- Range Updates
problem_id: SEG_RANGE_ADD_RANGE_SUM__6841
display_id: SEG-002
topics:
- Segment Tree
- Lazy Propagation
- Range Updates
---
# Range Add, Range Sum - Editorial

## Problem Summary

You are given an array and need to support two operations:
1.  **ADD l r x**: Add value `x` to all elements in the range `[l, r]`.
2.  **SUM l r**: Calculate the sum of elements in the range `[l, r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Mass Salary Adjustment System**.
-   **Range Add**: The company decides to give a bonus of $500 to all employees with IDs from 100 to 200.
-   **Range Sum**: The finance department needs to calculate the total salary expenditure for employees in department range 150-250 to budget for the next month.
Updating each employee individually is too slow (`O(N)`). We need a way to update the whole group instantly (`O(log N)`).

## Problem Exploration

### 1. The Challenge of Range Updates
A standard Segment Tree handles point updates in `O(log N)`. However, a range update naively requires updating every leaf node in the range, which takes `O(N)` in the worst case.
To achieve `O(log N)` for range updates, we need **Lazy Propagation**.

### 2. Lazy Propagation Logic
Instead of updating all children immediately, we update the current node and "flag" it to indicate that its children need to be updated later.
-   **Node Structure**: Each node stores `sum` (total value of its range) and `lazy` (pending addition value).
-   **Update**: When updating a range `[L, R]` that fully covers a node's range `[start, end]`:
    -   Update the node's `sum`: `sum += (end - start + 1) * x`.
    -   Update the node's `lazy`: `lazy += x`.
    -   Stop recursing.
-   **Push (Propagate)**: Before visiting children (for a query or partial update), we "push" the `lazy` value down:
    -   Add `lazy` to left child's `sum` and `lazy`.
    -   Add `lazy` to right child's `sum` and `lazy`.
    -   Reset current node's `lazy` to 0.

### 3. Data Structures
-   **Segment Tree with Lazy Propagation**: Ideal for this problem.
-   **Fenwick Tree (BIT)**: Can also handle Range Add + Range Sum using two BITs (one for `d[i]` and one for `i * d[i]`), but Segment Tree is more intuitive for general range operations.

## Approaches

### Approach 1: Segment Tree with Lazy Propagation
We build a tree where each node represents a range `[start, end]`.
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: `O(log N)`.
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
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    private void push(int node, int start, int end) {
        if (lazy[node] != 0) {
            int mid = (start + end) / 2;
            
            // Left child
            tree[2 * node + 1] += lazy[node] * (mid - start + 1);
            lazy[2 * node + 1] += lazy[node];
            
            // Right child
            tree[2 * node + 2] += lazy[node] * (end - mid);
            lazy[2 * node + 2] += lazy[node];
            
            lazy[node] = 0;
        }
    }

    private void update(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;

        if (l <= start && end <= r) {
            tree[node] += val * (end - start + 1);
            lazy[node] += val;
            return;
        }

        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;

        if (l <= start && end <= r) {
            return tree[node];
        }

        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
    }
}
```

### Python

```python
def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def push(node, start, end):
        if lazy[node] != 0:
            mid = (start + end) // 2
            
            # Left child
            tree[2 * node + 1] += lazy[node] * (mid - start + 1)
            lazy[2 * node + 1] += lazy[node]
            
            # Right child
            tree[2 * node + 2] += lazy[node] * (end - mid)
            lazy[2 * node + 2] += lazy[node]
            
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            tree[node] += val * (end - start + 1)
            lazy[node] += val
            return

        push(node, start, end)
        mid = (start + end) // 2
        update(2 * node + 1, start, mid, l, r, val)
        update(2 * node + 2, mid + 1, end, l, r, val)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def query(node, start, end, l, r):
        if l > end or r < start:
            return 0
        
        if l <= start and end <= r:
            return tree[node]
        
        push(node, start, end)
        mid = (start + end) // 2
        return query(2 * node + 1, start, mid, l, r) + \
               query(2 * node + 2, mid + 1, end, l, r)

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
```

### C++

```cpp
#include <vector>
#include <string>

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
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    void push(int node, int start, int end) {
        if (lazy[node] != 0) {
            int mid = (start + end) / 2;
            
            tree[2 * node + 1] += lazy[node] * (mid - start + 1);
            lazy[2 * node + 1] += lazy[node];
            
            tree[2 * node + 2] += lazy[node] * (end - mid);
            lazy[2 * node + 2] += lazy[node];
            
            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;

        if (l <= start && end <= r) {
            tree[node] += val * (end - start + 1);
            lazy[node] += val;
            return;
        }

        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;

        if (l <= start && end <= r) {
            return tree[node];
        }

        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
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
```

### JavaScript

```javascript
class Solution {
  process(arr, ops) {
    const n = arr.length;
    const tree = new BigInt64Array(4 * n);
    const lazy = new BigInt64Array(4 * n);

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = BigInt(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
      }
    };

    const push = (node, start, end) => {
      if (lazy[node] !== 0n) {
        const mid = Math.floor((start + end) / 2);
        
        tree[2 * node + 1] += lazy[node] * BigInt(mid - start + 1);
        lazy[2 * node + 1] += lazy[node];
        
        tree[2 * node + 2] += lazy[node] * BigInt(end - mid);
        lazy[2 * node + 2] += lazy[node];
        
        lazy[node] = 0n;
      }
    };

    const update = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;

      if (l <= start && end <= r) {
        tree[node] += val * BigInt(end - start + 1);
        lazy[node] += val;
        return;
      }

      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      update(2 * node + 1, start, mid, l, r, val);
      update(2 * node + 2, mid + 1, end, l, r, val);
      tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return 0n;

      if (l <= start && end <= r) {
        return tree[node];
      }

      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      return query(2 * node + 1, start, mid, l, r) + 
             query(2 * node + 2, mid + 1, end, l, r);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "ADD") {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const x = BigInt(op[3]);
        update(0, 0, n - 1, l, r, x);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        results.push(query(0, 0, n - 1, l, r).toString());
      }
    }
    return results;
  }
}
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 3`
`0 0 0`
1.  `ADD 0 1 5`:
    -   Update range `[0, 1]` with +5.
    -   Node `[0, 2]` (root): partial overlap. Push.
    -   Node `[0, 1]`: full overlap. `sum` += 5*2=10. `lazy` += 5.
    -   Node `[2, 2]`: no overlap.
    -   Root sum becomes 10.
2.  `ADD 1 2 2`:
    -   Update range `[1, 2]` with +2.
    -   Node `[0, 2]`: partial. Push.
    -   Node `[0, 1]`: partial. Push `lazy=5`.
        -   Node `[0, 0]`: `sum`=5, `lazy`=5.
        -   Node `[1, 1]`: `sum`=5, `lazy`=5.
    -   Node `[0, 0]`: no overlap with `[1, 2]`.
    -   Node `[1, 1]`: full overlap. `sum` += 2*1 = 7. `lazy` += 2 = 7.
    -   Node `[2, 2]`: full overlap. `sum` += 2*1 = 2. `lazy` += 2.
    -   Root sum becomes 5 + 7 + 2 = 14.
3.  `SUM 0 2`:
    -   Query `[0, 2]`. Full overlap with root. Return 14.

**Output:**
14

## Proof of Correctness

-   **Lazy Propagation**: Ensures that we only visit `O(log N)` nodes per update. By pushing the lazy value down only when necessary, we maintain the invariant that a node's `sum` is correct relative to its subtree's pending updates.
-   **Sum Calculation**: `tree[node] += val * (end - start + 1)` correctly updates the sum of a range by adding `val` to every element.

## Interview Extensions

1.  **Range Set to Value?**
    -   Instead of `+=`, we do `=`. We need a boolean flag `hasLazy` to distinguish "set to 0" from "no update".
2.  **Range Mul?**
    -   Maintain `mulLazy` and `addLazy`. Order of operations matters (usually multiply then add).
3.  **Max instead of Sum?**
    -   `tree[node] += val` works for max too. `push` adds to children.

### Common Mistakes

-   **Array Size**: Segment tree array should be `4 * N`.
-   **Push Logic**: Forgetting to multiply `lazy` by range length when updating `sum` for children.
-   **Index Bounds**: Ensure `l` and `r` are within `[0, n-1]`.
