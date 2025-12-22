---
title: Range Min After Additive Toggles
slug: range-min-after-toggles
difficulty: Medium
difficulty_score: 60
tags:
- Segment Tree
- Lazy Propagation
- Range Minimum
problem_id: SEG_RANGE_MIN_AFTER_TOGGLES__5728
display_id: SEG-015
topics:
- Segment Tree
- Lazy Propagation
- Range Queries
---
# Range Min After Additive Toggles - Editorial

## Problem Summary

You need to maintain an array `a` under two operations:
1.  **ADD l r x**: Add `x` to all elements in `a[l..r]`.
2.  **FLIP l r**: Multiply all elements in `a[l..r]` by `-1`.
3.  **MIN l r**: Find the minimum value in `a[l..r]`.

## Real-World Scenario

Imagine a **Financial Portfolio Tracker**.
-   **ADD**: Deposit or withdraw a fixed amount from a group of accounts.
-   **FLIP**: Convert debts to credits or vice versa (e.g., reversing a transaction type view).
-   **MIN**: Find the account with the lowest balance (or highest debt).

## Problem Exploration

### 1. Handling Flip
-   When we multiply a range by `-1`, the minimum value becomes `-1 * maximum`.
-   The maximum value becomes `-1 * minimum`.
-   So, we need to track both `min` and `max` in each Segment Tree node.

### 2. Lazy Propagation
-   We have two types of lazy tags: `lazy_add` and `lazy_flip`.
-   **Order matters**:
    -   Usually, we can apply `flip` then `add` or `add` then `flip`.
    -   Let's say a node has pending `lazy_add` and then receives a `flip`.
    -   Current state: `val + lazy_add`.
    -   New state: `-(val + lazy_add) = -val - lazy_add`.
    -   This means `flip` negates both the current values AND the pending `lazy_add`.
    -   So, when pushing `flip`, we negate `lazy_add` of children and toggle their `lazy_flip`.

### 3. Node Structure
-   `minVal`: Minimum in range.
-   `maxVal`: Maximum in range.
-   `lazyAdd`: Pending addition.
-   `lazyFlip`: Pending negation (boolean).

## Approaches

### Approach 1: Segment Tree with Two Lazy Tags
-   **Build**: $O(N)$.
-   **Update**: $O(\log N)$.
-   **Query**: $O(\log N)$.
-   Space: $O(N)$.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        long minVal, maxVal;
        long lazyAdd;
        boolean lazyFlip;
        
        Node(long val) {
            minVal = maxVal = val;
            lazyAdd = 0;
            lazyFlip = false;
        }
        
        Node() {
            minVal = Long.MAX_VALUE;
            maxVal = Long.MIN_VALUE;
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
            if (op[0].equals("ADD")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long x = Long.parseLong(op[3]);
                updateAdd(0, 0, n - 1, l, r, x);
            } else if (op[0].equals("FLIP")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                updateFlip(0, 0, n - 1, l, r);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void push(int node, int start, int end) {
        if (tree[node].lazyFlip) {
            applyFlip(2 * node + 1);
            applyFlip(2 * node + 2);
            tree[node].lazyFlip = false;
        }
        if (tree[node].lazyAdd != 0) {
            applyAdd(2 * node + 1, tree[node].lazyAdd);
            applyAdd(2 * node + 2, tree[node].lazyAdd);
            tree[node].lazyAdd = 0;
        }
    }
    
    private void applyFlip(int node) {
        long temp = tree[node].minVal;
        tree[node].minVal = -tree[node].maxVal;
        tree[node].maxVal = -temp;
        tree[node].lazyAdd = -tree[node].lazyAdd;
        tree[node].lazyFlip = !tree[node].lazyFlip;
    }
    
    private void applyAdd(int node, long val) {
        tree[node].minVal += val;
        tree[node].maxVal += val;
        tree[node].lazyAdd += val;
    }

    private void merge(int node) {
        tree[node].minVal = Math.min(tree[2 * node + 1].minVal, tree[2 * node + 2].minVal);
        tree[node].maxVal = Math.max(tree[2 * node + 1].maxVal, tree[2 * node + 2].maxVal);
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            merge(node);
        }
    }

    private void updateAdd(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyAdd(node, val);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateAdd(2 * node + 1, start, mid, l, r, val);
        updateAdd(2 * node + 2, mid + 1, end, l, r, val);
        merge(node);
    }

    private void updateFlip(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyFlip(node);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateFlip(2 * node + 1, start, mid, l, r);
        updateFlip(2 * node + 2, mid + 1, end, l, r);
        merge(node);
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Long.MAX_VALUE;
        if (l <= start && end <= r) return tree[node].minVal;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return Math.min(query(2 * node + 1, start, mid, l, r),
                        query(2 * node + 2, mid + 1, end, l, r));
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
        # Tree stores (min, max, lazy_add, lazy_flip)
        # Using separate arrays for performance
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        tree_add = [0] * (4 * n)
        tree_flip = [False] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree_min[node] = arr[start]
                tree_max[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
                tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def apply_flip(node):
            tree_min[node], tree_max[node] = -tree_max[node], -tree_min[node]
            tree_add[node] = -tree_add[node]
            tree_flip[node] = not tree_flip[node]

        def apply_add(node, val):
            tree_min[node] += val
            tree_max[node] += val
            tree_add[node] += val

        def push(node, start, end):
            if tree_flip[node]:
                apply_flip(2 * node + 1)
                apply_flip(2 * node + 2)
                tree_flip[node] = False
            if tree_add[node] != 0:
                apply_add(2 * node + 1, tree_add[node])
                apply_add(2 * node + 2, tree_add[node])
                tree_add[node] = 0

        def update_add(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                apply_add(node, val)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update_add(2 * node + 1, start, mid, l, r, val)
            update_add(2 * node + 2, mid + 1, end, l, r, val)
            tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
            tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def update_flip(node, start, end, l, r):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                apply_flip(node)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update_flip(2 * node + 1, start, mid, l, r)
            update_flip(2 * node + 2, mid + 1, end, l, r)
            tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
            tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def query(node, start, end, l, r):
            if l > end or r < start:
                return float('inf')
            if l <= start and end <= r:
                return tree_min[node]
            
            push(node, start, end)
            mid = (start + end) // 2
            return min(query(2 * node + 1, start, mid, l, r),
                       query(2 * node + 2, mid + 1, end, l, r))

        build(0, 0, n - 1)
        results = []
        
        for op in ops:
            if op[0] == "ADD":
                update_add(0, 0, n - 1, int(op[1]), int(op[2]), int(op[3]))
            elif op[0] == "FLIP":
                update_flip(0, 0, n - 1, int(op[1]), int(op[2]))
            else:
                results.append(query(0, 0, n - 1, int(op[1]), int(op[2])))
                
        return results

def process(arr, ops):
    return Solution().process(arr, ops)
```

### C++

```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

struct Node {
    long long minVal, maxVal;
    long long lazyAdd;
    bool lazyFlip;
};

class Solution {
    vector<Node> tree;
    int n;

    void applyFlip(int node) {
        long long temp = tree[node].minVal;
        tree[node].minVal = -tree[node].maxVal;
        tree[node].maxVal = -temp;
        tree[node].lazyAdd = -tree[node].lazyAdd;
        tree[node].lazyFlip = !tree[node].lazyFlip;
    }

    void applyAdd(int node, long long val) {
        tree[node].minVal += val;
        tree[node].maxVal += val;
        tree[node].lazyAdd += val;
    }

    void push(int node, int start, int end) {
        if (tree[node].lazyFlip) {
            applyFlip(2 * node + 1);
            applyFlip(2 * node + 2);
            tree[node].lazyFlip = false;
        }
        if (tree[node].lazyAdd != 0) {
            applyAdd(2 * node + 1, tree[node].lazyAdd);
            applyAdd(2 * node + 2, tree[node].lazyAdd);
            tree[node].lazyAdd = 0;
        }
    }

    void merge(int node) {
        tree[node].minVal = min(tree[2 * node + 1].minVal, tree[2 * node + 2].minVal);
        tree[node].maxVal = max(tree[2 * node + 1].maxVal, tree[2 * node + 2].maxVal);
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = {arr[start], arr[start], 0, false};
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            merge(node);
            tree[node].lazyAdd = 0;
            tree[node].lazyFlip = false;
        }
    }

    void updateAdd(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyAdd(node, val);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateAdd(2 * node + 1, start, mid, l, r, val);
        updateAdd(2 * node + 2, mid + 1, end, l, r, val);
        merge(node);
    }

    void updateFlip(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyFlip(node);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateFlip(2 * node + 1, start, mid, l, r);
        updateFlip(2 * node + 2, mid + 1, end, l, r);
        merge(node);
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return LLONG_MAX;
        if (l <= start && end <= r) return tree[node].minVal;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return min(query(2 * node + 1, start, mid, l, r),
                   query(2 * node + 2, mid + 1, end, l, r));
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.resize(4 * n);
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "ADD") {
                updateAdd(0, 0, n - 1, stoi(op[1]), stoi(op[2]), stoll(op[3]));
            } else if (op[0] == "FLIP") {
                updateFlip(0, 0, n - 1, stoi(op[1]), stoi(op[2]));
            } else {
                results.push_back(query(0, 0, n - 1, stoi(op[1]), stoi(op[2])));
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
    
    // Parallel arrays
    const treeMin = new Float64Array(4 * n);
    const treeMax = new Float64Array(4 * n);
    const treeAdd = new Float64Array(4 * n);
    const treeFlip = new Int8Array(4 * n); // 0 or 1

    const applyFlip = (node) => {
      const temp = treeMin[node];
      treeMin[node] = -treeMax[node];
      treeMax[node] = -temp;
      treeAdd[node] = -treeAdd[node];
      treeFlip[node] = 1 - treeFlip[node];
    };

    const applyAdd = (node, val) => {
      treeMin[node] += val;
      treeMax[node] += val;
      treeAdd[node] += val;
    };

    const push = (node, start, end) => {
      if (treeFlip[node]) {
        applyFlip(2 * node + 1);
        applyFlip(2 * node + 2);
        treeFlip[node] = 0;
      }
      if (treeAdd[node] !== 0) {
        applyAdd(2 * node + 1, treeAdd[node]);
        applyAdd(2 * node + 2, treeAdd[node]);
        treeAdd[node] = 0;
      }
    };

    const merge = (node) => {
      treeMin[node] = Math.min(treeMin[2 * node + 1], treeMin[2 * node + 2]);
      treeMax[node] = Math.max(treeMax[2 * node + 1], treeMax[2 * node + 2]);
    };

    const build = (node, start, end) => {
      if (start === end) {
        treeMin[node] = arr[start];
        treeMax[node] = arr[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        merge(node);
      }
    };

    const updateAdd = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        applyAdd(node, val);
        return;
      }
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      updateAdd(2 * node + 1, start, mid, l, r, val);
      updateAdd(2 * node + 2, mid + 1, end, l, r, val);
      merge(node);
    };

    const updateFlip = (node, start, end, l, r) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        applyFlip(node);
        return;
      }
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      updateFlip(2 * node + 1, start, mid, l, r);
      updateFlip(2 * node + 2, mid + 1, end, l, r);
      merge(node);
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return Infinity;
      if (l <= start && end <= r) return treeMin[node];
      
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node + 1, start, mid, l, r),
                      query(2 * node + 2, mid + 1, end, l, r));
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "ADD") {
        updateAdd(0, 0, n - 1, parseInt(op[1]), parseInt(op[2]), parseInt(op[3]));
      } else if (op[0] === "FLIP") {
        updateFlip(0, 0, n - 1, parseInt(op[1]), parseInt(op[2]));
      } else {
        results.push(query(0, 0, n - 1, parseInt(op[1]), parseInt(op[2])));
      }
    }
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`3 3`
`1 -2 3`
`FLIP 0 2`
`ADD 1 2 1`
`MIN 0 2`

1.  **Initial**: `[1, -2, 3]`. Min -2, Max 3.
2.  **FLIP 0 2**:
    -   Array effectively `[-1, 2, -3]`.
    -   Segment tree root: Min -3, Max -1.
3.  **ADD 1 2 1**:
    -   Array effectively `[-1, 3, -2]`.
    -   Segment tree updates range `[1, 2]`.
4.  **MIN 0 2**:
    -   Returns -2.

## Proof of Correctness

-   **Dual Tracking**: Maintaining both Min and Max allows correct updates under sign flip.
-   **Lazy Composition**: Correctly handling interaction between `add` and `flip` (negating `lazy_add` on flip) ensures consistency.

## Interview Extensions

1.  **Range Multiply by Positive X?**
    -   Just multiply min, max, and lazy_add.
2.  **Range Absolute Value?**
    -   Harder. Segment Tree Beats.

### C++ommon Mistakes

-   **Lazy Order**: Applying `flip` without negating `lazy_add` is a common bug.
-   **Min/Max Swap**: Forgetting to swap min and max when flipping.
