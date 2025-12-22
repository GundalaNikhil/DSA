---
title: Range Sum of Multiple Powers
slug: range-sum-multiple-powers
difficulty: Medium
difficulty_score: 55
tags:
- Segment Tree
- Modular Arithmetic
- Range Sum
problem_id: SEG_RANGE_SUM_MULTIPLE_POWERS__4175
display_id: SEG-013
topics:
- Segment Tree
- Modular Arithmetic
- Range Sum
---
# Range Sum of Multiple Powers - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SET i x**: Update `a[i] = x`.
2.  **SUM l r p**: Calculate $\sum_{i=l}^{r} (a[i]^p) \pmod{10^9+7}$ for $p \in \{1, 2, 3\}$.

## Real-World Scenario

Imagine a **Statistical Analysis Tool**.
-   You have a dataset of measurements.
-   To calculate variance, skewness, or kurtosis, you need sums of powers (moments).
-   Mean requires sum of $x^1$.
-   Variance requires sum of $x^2$.
-   Skewness requires sum of $x^3$.
-   As data updates, you need to recompute these moments efficiently for any subset of the data.

## Problem Exploration

### 1. Segment Tree Node Structure
Each node in the Segment Tree will store three values:
-   `sum1`: $\sum a[i]^1$
-   `sum2`: $\sum a[i]^2$
-   `sum3`: $\sum a[i]^3$

### 2. Merge Logic
When merging two nodes `left` and `right`:
-   `node.sum1 = (left.sum1 + right.sum1) % MOD`
-   `node.sum2 = (left.sum2 + right.sum2) % MOD`
-   `node.sum3 = (left.sum3 + right.sum3) % MOD`

### 3. Update Logic
When updating `a[i] = x`:
-   Leaf `i` updates its sums: `x`, `x^2`, `x^3`.
-   Path to root updates by re-merging.

### 4. Query Logic
-   Standard range sum query.
-   Return the specific sum requested by `p`.

## Approaches

### Approach 1: Segment Tree
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
        long sum1, sum2, sum3;
        
        Node(long val) {
            long v = val % 1000000007;
            if (v < 0) v += 1000000007;
            sum1 = v;
            sum2 = (v * v) % 1000000007;
            sum3 = (sum2 * v) % 1000000007;
        }
        
        Node() {}
    }
    
    private Node[] tree;
    private int n;
    private static final long MOD = 1000000007;

    public List<Long> process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Node[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                long val = Long.parseLong(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                int p = Integer.parseInt(op[3]);
                Node res = query(0, 0, n - 1, l, r);
                if (p == 1) results.add(res.sum1);
                else if (p == 2) results.add(res.sum2);
                else results.add(res.sum3);
            }
        }
        return results;
    }

    private Node merge(Node left, Node right) {
        Node res = new Node();
        res.sum1 = (left.sum1 + right.sum1) % MOD;
        res.sum2 = (left.sum2 + right.sum2) % MOD;
        res.sum3 = (left.sum3 + right.sum3) % MOD;
        return res;
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, long val) {
        if (start == end) {
            tree[node] = new Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private Node query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Node();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Node p1 = query(2 * node + 1, start, mid, l, r);
        Node p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
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
        MOD = 1000000007
        
        # Tree stores tuples (sum1, sum2, sum3)
        tree = [(0, 0, 0)] * (4 * n)
        
        def make_node(val):
            v = val % MOD
            v2 = (v * v) % MOD
            v3 = (v2 * v) % MOD
            return (v, v2, v3)

        def merge(n1, n2):
            return (
                (n1[0] + n2[0]) % MOD,
                (n1[1] + n2[1]) % MOD,
                (n1[2] + n2[2]) % MOD
            )

        def build(node, start, end):
            if start == end:
                tree[node] = make_node(arr[start])
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = make_node(val)
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    update(2 * node + 1, start, mid, idx, val)
                else:
                    update(2 * node + 2, mid + 1, end, idx, val)
                tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def query(node, start, end, l, r):
            if l > end or r < start:
                return (0, 0, 0)
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
                l = int(op[1])
                r = int(op[2])
                p = int(op[3])
                res = query(0, 0, n - 1, l, r)
                results.append(res[p-1])
                
        return results

def process(arr, ops):
    return Solution().process(arr, ops)
```

### C++

```cpp
#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Node {
    long long sum1, sum2, sum3;
    
    Node() : sum1(0), sum2(0), sum3(0) {}
    Node(long long val) {
        long long MOD = 1000000007;
        long long v = val % MOD;
        if (v < 0) v += MOD;
        sum1 = v;
        sum2 = (v * v) % MOD;
        sum3 = (sum2 * v) % MOD;
    }
};

class Solution {
    vector<Node> tree;
    int n;
    const long long MOD = 1000000007;

    Node merge(const Node& left, const Node& right) {
        Node res;
        res.sum1 = (left.sum1 + right.sum1) % MOD;
        res.sum2 = (left.sum2 + right.sum2) % MOD;
        res.sum3 = (left.sum3 + right.sum3) % MOD;
        return res;
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    Node query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Node();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Node p1 = query(2 * node + 1, start, mid, l, r);
        Node p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.resize(4 * n);
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                long long val = stoll(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                int p = stoi(op[3]);
                Node res = query(0, 0, n - 1, l, r);
                if (p == 1) results.push_back(res.sum1);
                else if (p == 2) results.push_back(res.sum2);
                else results.push_back(res.sum3);
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
    const MOD = 1000000007n;
    
    // Using BigInt for safety with powers and modulo
    const tree = new Array(4 * n);

    const makeNode = (val) => {
      let v = BigInt(val) % MOD;
      if (v < 0n) v += MOD;
      const v2 = (v * v) % MOD;
      const v3 = (v2 * v) % MOD;
      return { sum1: v, sum2: v2, sum3: v3 };
    };

    const merge = (n1, n2) => {
      return {
        sum1: (n1.sum1 + n2.sum1) % MOD,
        sum2: (n1.sum2 + n2.sum2) % MOD,
        sum3: (n1.sum3 + n2.sum3) % MOD
      };
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = makeNode(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = makeNode(val);
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return { sum1: 0n, sum2: 0n, sum3: 0n };
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
        const val = parseInt(op[2], 10);
        update(0, 0, n - 1, idx, val);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const p = parseInt(op[3], 10);
        const res = query(0, 0, n - 1, l, r);
        if (p === 1) results.push(Number(res.sum1));
        else if (p === 2) results.push(Number(res.sum2));
        else results.push(Number(res.sum3));
      }
    }
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`2 2`
`2 3`
`SUM 0 1 2`
`SUM 0 1 3`

1.  **Build**:
    -   Leaf 0: `(2, 4, 8)`.
    -   Leaf 1: `(3, 9, 27)`.
    -   Root: `(5, 13, 35)`.
2.  **Query 1**: `SUM 0 1 2`.
    -   Returns `sum2` from root: 13.
3.  **Query 2**: `SUM 0 1 3`.
    -   Returns `sum3` from root: 35.

## Proof of Correctness

-   **Linearity of Sum**: $\sum (a_i^p) = (\sum_{left} a_i^p) + (\sum_{right} a_i^p)$.
-   **Modular Arithmetic**: $(A + B) \pmod M = (A \pmod M + B \pmod M) \pmod M$.
-   **Segment Tree**: Correctly aggregates these independent sums.

## Interview Extensions

1.  **Range Add Updates?**
    -   If we add `x` to range:
    -   New sum1: $\sum (a_i+x) = \sum a_i + N \cdot x$.
    -   New sum2: $\sum (a_i+x)^2 = \sum (a_i^2 + 2a_ix + x^2) = \sum a_i^2 + 2x\sum a_i + N \cdot x^2$.
    -   New sum3: $\sum (a_i+x)^3 = \sum (a_i^3 + 3a_i^2x + 3a_ix^2 + x^3)$.
    -   We can maintain this with lazy propagation!
2.  **Higher Powers?**
    -   Binomial expansion works for any $p$, but complexity grows with $p$.

### C++ommon Mistakes

-   **Modulo Negative Numbers**: Ensure `val % MOD` handles negatives correctly (add MOD if negative).
-   **Overflow**: Intermediate calculations like `v * v` can exceed 64-bit if not careful, though with MOD $10^9+7$, `v^2` fits in `long long`. `v^3` requires step-by-step modulo.
