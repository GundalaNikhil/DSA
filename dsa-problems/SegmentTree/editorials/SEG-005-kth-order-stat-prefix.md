---
title: K-th Order Statistic in Prefix
slug: kth-order-stat-prefix
difficulty: Medium
difficulty_score: 57
tags:
- Segment Tree
- Persistent Data Structures
- Order Statistics
problem_id: SEG_KTH_ORDER_STAT_PREFIX__7093
display_id: SEG-005
topics:
- Segment Tree
- Persistent Data Structures
- Order Statistics
---
# K-th Order Statistic in Prefix - Editorial

## Problem Summary

You are given an array `a`. You need to answer queries `PREFIX r k`: find the `k`-th smallest value in the prefix `a[0..r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`
## Real-World Scenario

Imagine a **Sales Performance Dashboard**.
-   You have a stream of sales data coming in over time.
-   A manager wants to know: "What was the median sale amount among the first 1000 transactions?" or "What was the 90th percentile sale in the first month?"
-   This corresponds to finding the `k`-th smallest value in a prefix of the data.

## Problem Exploration

### 1. Naive Approach
For each query `(r, k)`, take `a[0..r]`, sort it, and pick the `k`-th element.
-   Sorting takes `O(r log r)`.
-   Total time: `O(q * n log n)`. Too slow for `n, q = 200,000`.

### 2. Persistent Segment Tree
We can view the prefix `a[0..r]` as a collection of values.
If we build a Segment Tree over the **values** (coordinate compressed), we can find the `k`-th smallest in `O(log (value range))`.
However, we have different prefixes.
A **Persistent Segment Tree** allows us to store the state of the segment tree after inserting each element `a[i]`.
-   `root[i]` represents the segment tree containing values `a[0..i]`.
-   To find the `k`-th smallest in `a[0..r]`, we query `root[r]`.

### 3. Coordinate Compression
Since values can be large (`-10^9` to `10^9`), but `n` is small (`200,000`), we map the distinct values to ranks `0, 1, dots, m-1`.
The segment tree will cover the range `[0, m-1]`.

### 4. Query Logic
In a standard segment tree storing counts of values:
-   Let `cnt` be the number of elements in the left child.
-   If `k <= cnt`, recurse left.
-   Else, recurse right with `k - cnt`.

## Approaches

### Approach 1: Persistent Segment Tree
1.  **Coordinate Compress**: Map values to `0 dots m-1`.
2.  **Build Trees**:
    -   `root[-1]` is an empty tree (all zeros).
    -   For `i` from `0` to `n-1`:
        -   `root[i] = update(root[i-1], compressed_val[i], +1)`
        -   This creates a new version of the tree with count of `val` incremented.
3.  **Query**:
    -   For `PREFIX r k`, call `query(root[r], k)`.
    -   Map the result index back to the original value.

**Complexity**:
-   Build: `O(N log N)`.
-   Query: `O(log N)`.
-   Space: `O(N log N)` nodes.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class Node {
        int count;
        Node left, right;
        
        Node(int count, Node left, Node right) {
            this.count = count;
            this.left = left;
            this.right = right;
        }
    }
    
    private Node[] roots;
    private int[] unique;
    
    public int[] kthPrefix(int[] arr, int[][] queries) {
        int n = arr.length;
        
        // Coordinate Compression
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        // Remove duplicates
        int m = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sorted[i] != sorted[i-1]) {
                m++;
            }
        }
        unique = new int[m];
        m = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sorted[i] != sorted[i-1]) {
                unique[m++] = sorted[i];
            }
        }
        
        // Build Persistent Segment Tree
        roots = new Node[n];
        Node nullNode = build(0, m - 1);
        
        for (int i = 0; i < n; i++) {
            int idx = Arrays.binarySearch(unique, arr[i]);
            Node prev = (i == 0) ? nullNode : roots[i - 1];
            roots[i] = update(prev, 0, m - 1, idx);
        }
        
        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int r = queries[i][0];
            int k = queries[i][1];
            int idx = query(roots[r], 0, m - 1, k);
            results[i] = unique[idx];
        }
        return results;
    }
    
    private Node build(int l, int r) {
        if (l == r) return new Node(0, null, null);
        int mid = (l + r) / 2;
        return new Node(0, build(l, mid), build(mid + 1, r));
    }
    
    private Node update(Node node, int l, int r, int idx) {
        if (l == r) {
            return new Node(node.count + 1, null, null);
        }
        int mid = (l + r) / 2;
        Node left = node.left;
        Node right = node.right;
        if (idx <= mid) {
            left = update(left, l, mid, idx);
        } else {
            right = update(right, mid + 1, r, idx);
        }
        return new Node(left.count + right.count, left, right);
    }
    
    private int query(Node node, int l, int r, int k) {
        if (l == r) return l;
        int mid = (l + r) / 2;
        int leftCount = node.left.count;
        if (k <= leftCount) {
            return query(node.left, l, mid, k);
        } else {
            return query(node.right, mid + 1, r, k - leftCount);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[][] queries = new int[q][2];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // PREFIX
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.kthPrefix(arr, queries);
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

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, count=0, left=None, right=None):
        self.count = count
        self.left = left
        self.right = right

def kth_prefix(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    # Coordinate Compression
    unique = sorted(list(set(arr)))
    val_map = {val: i for i, val in enumerate(unique)}
    m = len(unique)
    
    # Build Null Tree
    def build(l, r):
        node = Node()
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = build(l, mid)
        node.right = build(mid + 1, r)
        return node

    null_root = build(0, m - 1)
    roots = []
    
    def update(prev_node, l, r, idx):
        node = Node(prev_node.count + 1, prev_node.left, prev_node.right)
        if l == r:
            return node
        mid = (l + r) // 2
        if idx <= mid:
            node.left = update(prev_node.left, l, mid, idx)
        else:
            node.right = update(prev_node.right, mid + 1, r, idx)
        return node

    prev = null_root
    for x in arr:
        idx = val_map[x]
        new_root = update(prev, 0, m - 1, idx)
        roots.append(new_root)
        prev = new_root
        
    def query(node, l, r, k):
        if l == r:
            return l
        mid = (l + r) // 2
        left_count = node.left.count
        if k <= left_count:
            return query(node.left, l, mid, k)
        else:
            return query(node.right, mid + 1, r, k - left_count)
            
    results = []
    for r, k in queries:
        idx = query(roots[r], 0, m - 1, k)
        results.append(unique[idx])
        
    return results

def main():
    import sys
    # Increase recursion depth for deep trees
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        type = next(it) # PREFIX
        queries.append((int(next(it)), int(next(it))))
    
    results = kth_prefix(arr, queries)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct Node {
    int count;
    Node *left, *right;
    
    Node(int count, Node* left, Node* right) : count(count), left(left), right(right) {}
};

class Solution {
    vector<Node*> roots;
    vector<int> unique;
    
    Node* build(int l, int r) {
        if (l == r) return new Node(0, nullptr, nullptr);
        int mid = (l + r) / 2;
        return new Node(0, build(l, mid), build(mid + 1, r));
    }
    
    Node* update(Node* node, int l, int r, int idx) {
        if (l == r) {
            return new Node(node->count + 1, nullptr, nullptr);
        }
        int mid = (l + r) / 2;
        Node* left = node->left;
        Node* right = node->right;
        if (idx <= mid) {
            left = update(left, l, mid, idx);
        } else {
            right = update(right, mid + 1, r, idx);
        }
        return new Node(left->count + right->count, left, right);
    }
    
    int query(Node* node, int l, int r, int k) {
        if (l == r) return l;
        int mid = (l + r) / 2;
        int leftCount = node->left->count;
        if (k <= leftCount) {
            return query(node->left, l, mid, k);
        } else {
            return query(node->right, mid + 1, r, k - leftCount);
        }
    }

public:
    vector<int> kthPrefix(const vector<int>& arr, const vector<pair<int,int>>& queries) {
        int n = arr.size();
        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        this->unique = sorted;
        int m = unique.size();
        
        Node* nullRoot = build(0, m - 1);
        roots.clear();
        
        Node* prev = nullRoot;
        for (int x : arr) {
            int idx = lower_bound(unique.begin(), unique.end(), x) - unique.begin();
            Node* curr = update(prev, 0, m - 1, idx);
            roots.push_back(curr);
            prev = curr;
        }
        
        vector<int> results;
        for (const auto& q : queries) {
            int r = q.first;
            int k = q.second;
            int idx = query(roots[r], 0, m - 1, k);
            results.push_back(unique[idx]);
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<pair<int, int>> queries(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // PREFIX
        cin >> queries[i].first >> queries[i].second;
    }
    Solution sol;
    vector<int> results = sol.kthPrefix(arr, queries);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  kthPrefix(arr, queries) {
    // Coordinate Compression
    const unique = Array.from(new Set(arr)).sort((a, b) => a - b);
    const valMap = new Map();
    unique.forEach((val, idx) => valMap.set(val, idx));
    const m = unique.length;

    // Node class
    class Node {
      constructor(count, left, right) {
        this.count = count;
        this.left = left;
        this.right = right;
      }
    }

    const build = (l, r) => {
      if (l === r) return new Node(0, null, null);
      const mid = Math.floor((l + r) / 2);
      return new Node(0, build(l, mid), build(mid + 1, r));
    };

    const update = (node, l, r, idx) => {
      if (l === r) {
        return new Node(node.count + 1, null, null);
      }
      const mid = Math.floor((l + r) / 2);
      let left = node.left;
      let right = node.right;
      if (idx <= mid) {
        left = update(left, l, mid, idx);
      } else {
        right = update(right, mid + 1, r, idx);
      }
      return new Node(left.count + right.count, left, right);
    };

    const query = (node, l, r, k) => {
      if (l === r) return l;
      const mid = Math.floor((l + r) / 2);
      const leftCount = node.left.count;
      if (k <= leftCount) {
        return query(node.left, l, mid, k);
      } else {
        return query(node.right, mid + 1, r, k - leftCount);
      }
    };

    const nullRoot = build(0, m - 1);
    const roots = [];
    let prev = nullRoot;

    for (const x of arr) {
      const idx = valMap.get(x);
      const curr = update(prev, 0, m - 1, idx);
      roots.push(curr);
      prev = curr;
    }

    const results = [];
    for (const [r, k] of queries) {
      const idx = query(roots[r], 0, m - 1, k);
      results.push(unique[idx]);
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
  const queries = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // PREFIX
    queries.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.kthPrefix(arr, queries);
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`4 1`
`5 1 3 2`
`PREFIX 3 2`

1.  **Compression**: Unique sorted: `[1, 2, 3, 5]`. Map: `{1:0, 2:1, 3:2, 5:3}`.
2.  **Build**:
    -   `root[-1]`: Empty.
    -   `root[0]` (add 5 -> idx 3): `{3:1}`.
    -   `root[1]` (add 1 -> idx 0): `{0:1, 3:1}`.
    -   `root[2]` (add 3 -> idx 2): `{0:1, 2:1, 3:1}`.
    -   `root[3]` (add 2 -> idx 1): `{0:1, 1:1, 2:1, 3:1}`.
3.  **Query**: `PREFIX 3 2` (k=2 in `root[3]`).
    -   `root[3]` has counts `[1, 1, 1, 1]` for indices `0, 1, 2, 3`.
    -   Left child (indices 0-1) has count 2.
    -   `k=2 <= 2`. Go left.
    -   Left child (indices 0-1) split to `0` and `1`.
    -   Left child (index 0) has count 1.
    -   `k=2 > 1`. Go right with `k = 2-1 = 1`.
    -   Right child (index 1). Leaf. Return index 1.
4.  **Result**: `unique[1] = 2`.

## Proof of Correctness

-   **Persistence**: `root[r]` correctly represents the frequency array of `a[0..r]`.
-   **Structure**: The segment tree over value ranges allows binary searching for the `k`-th element by counting how many elements fall in the left half.
-   **Space**: Each update adds `log M` nodes, keeping space linear-logarithmic.

## Interview Extensions

1.  **Range [L, R] K-th Smallest?**
    -   Use `root[R]` and `root[L-1]`.
    -   Count in range `[L, R]` is `count(root[R]) - count(root[L-1])`.
    -   This is the standard usage of Persistent Segment Trees (MKTHNUM).
2.  **Dynamic Updates?**
    -   If array changes, Persistent Segment Tree is hard to update. Use **Fenwick Tree of Segment Trees** (or Segment Tree over Fenwick Tree), `O(log^2 N)` per op.

### Common Mistakes

-   **Memory Limit**: Persistent Segment Trees use a lot of memory. In C++, use pointers carefully or static array allocation. In Java/Python, GC handles it but can be slow or OOM.
-   **Coordinate Compression**: Essential when values are large.
-   **Base Cases**: Handle `k=1` or `k=r+1` correctly.
