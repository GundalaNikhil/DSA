---
title: Range GCD with Skip Zones
slug: range-gcd-skip-zones
difficulty: Medium
difficulty_score: 54
tags:
- Segment Tree
- GCD
- Dynamic Sets
problem_id: SEG_RANGE_GCD_SKIP_ZONES__6230
display_id: SEG-010
topics:
- Segment Tree
- GCD
- Dynamic Sets
---
# Range GCD with Skip Zones - Editorial

## Problem Summary

You are given an array `a` and a set of **forbidden indices**.
You need to support:
1.  **TOGGLE i**: Flip whether index `i` is forbidden.
2.  **SET i x**: Update `a[i] = x`.
3.  **GCD l r**: Calculate the GCD of all elements in `a[l..r]` that are **not** forbidden. If no allowed elements exist, return 0.

## Real-World Scenario

Imagine a **Cluster Health Monitoring System**.
-   You have a cluster of servers, each reporting a "heartbeat" interval or a version number.
-   You want to find the greatest common divisor of these values to synchronize them or find a common compatible protocol version.
-   However, some servers might be **down** (forbidden) or in maintenance mode. You need to ignore them dynamically.
-   Servers can come back online (TOGGLE) or change their config (SET).

## Problem Exploration

### 1. GCD Properties
-   $\gcd(0, x) = x$.
-   $\gcd(a, b, c) = \gcd(a, \gcd(b, c))$.
-   This associativity allows Segment Trees.

### 2. Handling Forbidden Indices
-   If an index `i` is forbidden, we can treat its value as `0` for GCD purposes.
-   Since $\gcd(0, x) = x$, a `0` effectively contributes nothing to the GCD calculation, which is exactly what we want (ignoring the element).
-   If all elements in a range are forbidden (all 0), the result is 0.

### 3. Segment Tree Approach
-   Maintain a Segment Tree where each leaf `i` stores:
    -   `a[i]` if `i` is allowed.
    -   `0` if `i` is forbidden.
-   **TOGGLE i**: Update leaf `i`. If it was `a[i]`, make it `0`. If `0`, make it `a[i]`.
-   **SET i x**: Update `a[i]`. If `i` is allowed, update leaf to `x`. If forbidden, just update the stored `a[i]` but keep leaf as `0`.
-   **GCD l r**: Standard range GCD query.

## Approaches

### Approach 1: Segment Tree with Zero-Masking
-   Store actual values in an auxiliary array `vals`.
-   Store `active` boolean array.
-   Segment Tree stores the effective values.
-   **Update**: $O(\log N + \log (\text{max\_val}))$. GCD takes logarithmic time.
-   **Query**: $O(\log N + \log (\text{max\_val}))$.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int[] tree;
    private int[] vals;
    private boolean[] active;
    private int n;

    private int gcd(int a, int b) {
        if (a == 0) return b;
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public List<Integer> process(int[] arr, boolean[] forbidden, List<String[]> ops) {
        n = arr.length;
        vals = arr.clone();
        active = new boolean[n];
        for (int i = 0; i < n; i++) active[i] = !forbidden[i];
        
        tree = new int[4 * n];
        build(0, 0, n - 1);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            String type = op[0];
            if (type.equals("TOGGLE")) {
                int idx = Integer.parseInt(op[1]);
                active[idx] = !active[idx];
                int effectiveVal = active[idx] ? vals[idx] : 0;
                update(0, 0, n - 1, idx, effectiveVal);
            } else if (type.equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                int val = Integer.parseInt(op[2]);
                vals[idx] = val;
                int effectiveVal = active[idx] ? vals[idx] : 0;
                update(0, 0, n - 1, idx, effectiveVal);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = active[start] ? vals[start] : 0;
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private int query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        int p1 = query(2 * node + 1, start, mid, l, r);
        int p2 = query(2 * node + 2, mid + 1, end, l, r);
        return gcd(p1, p2);
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def process(arr: list[int], forbidden: list[bool], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    vals = list(arr)
    active = [not f for f in forbidden]
    tree = [0] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            tree[node] = vals[start] if active[start] else 0
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2])

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2])

    def query(node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return tree[node]
        
        mid = (start + end) // 2
        p1 = query(2 * node + 1, start, mid, l, r)
        p2 = query(2 * node + 2, mid + 1, end, l, r)
        return gcd(p1, p2)

    build(0, 0, n - 1)
    results = []
    
    for op in ops:
        type = op[0]
        if type == "TOGGLE":
            idx = int(op[1])
            active[idx] = not active[idx]
            eff_val = vals[idx] if active[idx] else 0
            update(0, 0, n - 1, idx, eff_val)
        elif type == "SET":
            idx = int(op[1])
            val = int(op[2])
            vals[idx] = val
            eff_val = vals[idx] if active[idx] else 0
            update(0, 0, n - 1, idx, eff_val)
        else:
            l = int(op[1])
            r = int(op[2])
            results.append(query(0, 0, n - 1, l, r))
            
    return results
```

### C++

```cpp
#include <vector>
#include <numeric>
#include <string>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

class Solution {
    vector<int> tree;
    vector<int> vals;
    vector<bool> active;
    int n;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = active[start] ? vals[start] : 0;
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    int query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        int p1 = query(2 * node + 1, start, mid, l, r);
        int p2 = query(2 * node + 2, mid + 1, end, l, r);
        return gcd(p1, p2);
    }

public:
    vector<int> process(const vector<int>& arr, const vector<bool>& forbidden, const vector<vector<string>>& ops) {
        n = arr.size();
        vals = arr;
        active.resize(n);
        for (int i = 0; i < n; i++) active[i] = !forbidden[i];
        
        tree.resize(4 * n);
        build(0, 0, n - 1);
        
        vector<int> results;
        for (const auto& op : ops) {
            if (op[0] == "TOGGLE") {
                int idx = stoi(op[1]);
                active[idx] = !active[idx];
                int effVal = active[idx] ? vals[idx] : 0;
                update(0, 0, n - 1, idx, effVal);
            } else if (op[0] == "SET") {
                int idx = stoi(op[1]);
                int val = stoi(op[2]);
                vals[idx] = val;
                int effVal = active[idx] ? vals[idx] : 0;
                update(0, 0, n - 1, idx, effVal);
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
  process(arr, forbidden, ops) {
    const n = arr.length;
    const vals = [...arr];
    const active = forbidden.map(f => !f);
    const tree = new Int32Array(4 * n);

    const gcd = (a, b) => {
      while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
      }
      return a;
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = active[start] ? vals[start] : 0;
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = val;
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return 0;
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node + 1, start, mid, l, r);
      const p2 = query(2 * node + 2, mid + 1, end, l, r);
      return gcd(p1, p2);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      const type = op[0];
      if (type === "TOGGLE") {
        const idx = parseInt(op[1], 10);
        active[idx] = !active[idx];
        const effVal = active[idx] ? vals[idx] : 0;
        update(0, 0, n - 1, idx, effVal);
      } else if (type === "SET") {
        const idx = parseInt(op[1], 10);
        const val = parseInt(op[2], 10);
        vals[idx] = val;
        const effVal = active[idx] ? vals[idx] : 0;
        update(0, 0, n - 1, idx, effVal);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        results.push(query(0, 0, n - 1, l, r));
      }
    }
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`3 3`
`6 9 3`
`1` (forbidden count)
`1` (index 1 is forbidden)
`GCD 0 2`
`TOGGLE 1`
`GCD 0 2`

1.  **Initial State**:
    -   `vals = [6, 9, 3]`.
    -   `active = [T, F, T]`.
    -   Leaves: `6`, `0`, `3`.
    -   Root: `gcd(6, 0, 3) = gcd(6, 3) = 3`.
2.  **Query 1**: `GCD 0 2`. Returns 3.
3.  **Toggle 1**:
    -   `active[1]` becomes `T`.
    -   Leaf 1 becomes `9`.
    -   Root: `gcd(6, 9, 3) = 3`.
4.  **Query 2**: `GCD 0 2`. Returns 3.

## Proof of Correctness

-   **Zero Identity**: $\gcd(0, x) = x$ ensures that setting forbidden elements to 0 effectively removes them from the calculation without affecting the result of other elements.
-   **Segment Tree**: Correctly maintains range GCDs under point updates.

## Interview Extensions

1.  **Range Toggle?**
    -   Lazy propagation with boolean flip?
    -   If we flip a range, we need to swap "active GCD" and "inactive GCD"?
    -   We can maintain `gcd_active` and `gcd_inactive` in each node.
    -   Flip swaps them.
2.  **Number of Active Elements?**
    -   Maintain count sum in segment tree.

### Common Mistakes

-   **GCD(0, 0)**: Should be 0.
-   **Negative Numbers**: GCD is usually defined on non-negative integers. If input has negatives, take `abs()`.
