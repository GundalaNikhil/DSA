---
title: "Path Queries with Euler Tour and RMQ - Editorial"
problem_id: TDP_PATH_QUERIES_RMQ__6729
difficulty: Medium
tags: [tree-dp, euler-tour, rmq, lca, sparse-table]
editorial_categories: [Tree DP, LCA, RMQ]
slug: path-queries-rmq
---

## 📝 Problem Summary

Given a weighted tree with N nodes, preprocess it to answer Q distance queries efficiently. Each query asks for the distance between two nodes u and v. The challenge is to answer queries in O(1) or O(log N) time after O(N log N) preprocessing using Euler Tour, LCA (Lowest Common Ancestor), and RMQ (Range Minimum Query).

---

## 🔍 Approach: Euler Tour + Sparse Table RMQ for LCA

### Key Insight

The distance between two nodes u and v can be computed as: dist(u, v) = dist(root, u) + dist(root, v) - 2 × dist(root, LCA(u, v))

We can:

1. Compute distances from root to all nodes using DFS
2. Build Euler tour to convert tree to array representation
3. Use Sparse Table for O(1) RMQ to find LCA
4. Answer distance queries using the formula above

### Algorithm Overview

1. **Euler Tour:** Do DFS and record [node, depth] each time we enter/exit a node
2. **First/Last occurrence:** Track first occurrence of each node in Euler tour
3. **Sparse Table:** Build RMQ data structure on depth array from Euler tour
4. **LCA Query:** Query RMQ between first occurrences of u and v
5. **Distance Calculation:** Use precomputed distances + LCA

---

## 🧠 Intuition Builder

### 💡 Visual Intuition

Imagine flattening a tree by walking through it and writing down each node as you encounter it (including backtracking). This creates a linear sequence where any two nodes' LCA corresponds to the minimum depth value between their first occurrences in the sequence.

### 🌍 Real-World Analogy

**File System Navigation:**
Consider a file system tree. To find the distance between two files, you navigate up from each file to find their closest common ancestor directory, then sum the path lengths. The Euler tour is like logging every directory entry/exit during a complete traversal.

### 🔗 Pattern Recognition

This problem combines:

- **Euler Tour**: Convert tree to array
- **RMQ**: Range queries on array
- **LCA**: Lowest common ancestor
- **Precomputation**: Trade space for query time

---

## ✅ Solution: Euler Tour + Sparse Table

### Detailed Solution Steps

1. **DFS to compute Euler tour and depths**
2. **Track first occurrence of each node in tour**
3. **Build Sparse Table on depths for O(1) RMQ**
4. **For each query (u, v):**
   - Find positions of first occurrences: pos[u], pos[v]
   - Query RMQ on range [min(pos[u], pos[v]), max(pos[u], pos[v])]
   - The node at minimum depth is LCA(u, v)
   - Calculate: dist(u, v) = depth[u] + depth[v] - 2 × depth[LCA]

### Implementation Notes

- Sparse Table: st[i][j] = index of min depth in range [i, i + 2^j - 1]
- Euler tour size = 2N - 1 (enter each node once, exit N-1 times)
- Use 0-indexed or 1-indexed consistently

---

## 💻 Implementation

### Java

```java
import java.util.*;

public class PathQueriesRMQ {
    static int n, timer;
    static List<int[]>[] adj;
    static int[] first, depth, dist, euler, parent;
    static int[][] st;
    static int logSize;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        first = new int[n + 1];
        depth = new int[n + 1];
        dist = new int[n + 1];
        euler = new int[2 * n];
        timer = 0;

        dfs(1, 0, 0, 0);

        buildSparseTable();

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            System.out.println(queryDistance(u, v));
        }
    }

    static void dfs(int u, int p, int d, int distance) {
        depth[u] = d;
        dist[u] = distance;
        first[u] = timer;
        euler[timer++] = u;

        for (int[] edge : adj[u]) {
            int v = edge[0], w = edge[1];
            if (v != p) {
                dfs(v, u, d + 1, distance + w);
                euler[timer++] = u;
            }
        }
    }

    static void buildSparseTable() {
        int size = timer;
        logSize = (int)(Math.log(size) / Math.log(2)) + 1;
        st = new int[size][logSize];

        for (int i = 0; i < size; i++) {
            st[i][0] = i;
        }

        for (int j = 1; j < logSize; j++) {
            for (int i = 0; i + (1 << j) <= size; i++) {
                int left = st[i][j - 1];
                int right = st[i + (1 << (j - 1))][j - 1];
                st[i][j] = (depth[euler[left]] <= depth[euler[right]]) ? left : right;
            }
        }
    }

    static int queryLCA(int u, int v) {
        int l = first[u], r = first[v];
        if (l > r) {
            int temp = l; l = r; r = temp;
        }

        int len = r - l + 1;
        int k = (int)(Math.log(len) / Math.log(2));

        int left = st[l][k];
        int right = st[r - (1 << k) + 1][k];

        int lcaIdx = (depth[euler[left]] <= depth[euler[right]]) ? left : right;
        return euler[lcaIdx];
    }

    static int queryDistance(int u, int v) {
        int lca = queryLCA(u, v);
        return dist[u] + dist[v] - 2 * dist[lca];
    }
}
```

### Python

```python
import sys
import math
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1

    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    first = [0] * (n + 1)
    depth = [0] * (n + 1)  # Tree depth (number of edges from root)
    dist = [0] * (n + 1)   # Weighted distance from root
    euler = []

    def dfs(u, p, d, distance):
        depth[u] = d
        dist[u] = distance
        first[u] = len(euler)
        euler.append(u)

        for v, w in adj[u]:
            if v != p:
                dfs(v, u, d + 1, distance + w)
                euler.append(u)

    dfs(1, 0, 0, 0)

    # Build sparse table for RMQ on Euler tour (minimum depth)
    size = len(euler)
    log_size = int(math.log2(size)) + 1
    st = [[0] * log_size for _ in range(size)]

    for i in range(size):
        st[i][0] = i

    for j in range(1, log_size):
        i = 0
        while i + (1 << j) <= size:
            left = st[i][j - 1]
            right = st[i + (1 << (j - 1))][j - 1]
            st[i][j] = left if depth[euler[left]] <= depth[euler[right]] else right
            i += 1

    def query_lca(u, v):
        l, r = first[u], first[v]
        if l > r:
            l, r = r, l

        length = r - l + 1
        k = int(math.log2(length))

        left = st[l][k]
        right = st[r - (1 << k) + 1][k]

        lca_idx = left if depth[euler[left]] <= depth[euler[right]] else right
        return euler[lca_idx]

    def query_distance(u, v):
        lca = query_lca(u, v)
        return dist[u] + dist[v] - 2 * dist[lca]

    q = int(input_data[idx]); idx += 1
    for _ in range(q):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        print(query_distance(u, v))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, timer_val;
vector<vector<pair<int, int>>> adj;
vector<int> first_occ, depth_val, euler_tour;
vector<vector<int>> st;
int log_size;

void dfs(int u, int p, int d) {
    depth_val[u] = d;
    first_occ[u] = timer_val;
    euler_tour[timer_val++] = u;

    for (auto [v, w] : adj[u]) {
        if (v != p) {
            dfs(v, u, d + w);
            euler_tour[timer_val++] = u;
        }
    }
}

void build_sparse_table() {
    int size = timer_val;
    log_size = __lg(size) + 1;
    st.assign(size, vector<int>(log_size));

    for (int i = 0; i < size; i++) {
        st[i][0] = i;
    }

    for (int j = 1; j < log_size; j++) {
        for (int i = 0; i + (1 << j) <= size; i++) {
            int left = st[i][j - 1];
            int right = st[i + (1 << (j - 1))][j - 1];
            st[i][j] = (depth_val[euler_tour[left]] <= depth_val[euler_tour[right]]) ? left : right;
        }
    }
}

int query_lca(int u, int v) {
    int l = first_occ[u], r = first_occ[v];
    if (l > r) swap(l, r);

    int len = r - l + 1;
    int k = __lg(len);

    int left = st[l][k];
    int right = st[r - (1 << k) + 1][k];

    int lca_idx = (depth_val[euler_tour[left]] <= depth_val[euler_tour[right]]) ? left : right;
    return euler_tour[lca_idx];
}

int query_distance(int u, int v) {
    int lca = query_lca(u, v);
    return depth_val[u] + depth_val[v] - 2 * depth_val[lca];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    adj.resize(n + 1);
    first_occ.resize(n + 1);
    depth_val.resize(n + 1);
    euler_tour.resize(2 * n);

    for (int i = 0; i < n - 1; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    timer_val = 0;
    dfs(1, 0, 0);
    build_sparse_table();

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << query_distance(u, v) << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v, w] = lines[idx++].split(" ").map(Number);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const first = Array(n + 1).fill(0);
  const depth = Array(n + 1).fill(0);
  const euler = [];

  function dfs(u, p, d) {
    depth[u] = d;
    first[u] = euler.length;
    euler.push(u);

    for (const [v, w] of adj[u]) {
      if (v !== p) {
        dfs(v, u, d + w);
        euler.push(u);
      }
    }
  }

  dfs(1, 0, 0);

  // Build sparse table
  const size = euler.length;
  const logSize = Math.floor(Math.log2(size)) + 1;
  const st = Array.from({ length: size }, () => Array(logSize).fill(0));

  for (let i = 0; i < size; i++) {
    st[i][0] = i;
  }

  for (let j = 1; j < logSize; j++) {
    for (let i = 0; i + (1 << j) <= size; i++) {
      const left = st[i][j - 1];
      const right = st[i + (1 << (j - 1))][j - 1];
      st[i][j] = depth[euler[left]] <= depth[euler[right]] ? left : right;
    }
  }

  function queryLCA(u, v) {
    let l = first[u],
      r = first[v];
    if (l > r) [l, r] = [r, l];

    const len = r - l + 1;
    const k = Math.floor(Math.log2(len));

    const left = st[l][k];
    const right = st[r - (1 << k) + 1][k];

    const lcaIdx = depth[euler[left]] <= depth[euler[right]] ? left : right;
    return euler[lcaIdx];
  }

  function queryDistance(u, v) {
    const lca = queryLCA(u, v);
    return depth[u] + depth[v] - 2 * depth[lca];
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(queryDistance(u, v));
  }
});
```

---

## ⏱️ Complexity Analysis

### Detailed Breakdown

| Phase                   | Time           | Space          | Explanation                        |
| ----------------------- | -------------- | -------------- | ---------------------------------- |
| **Preprocessing**       |                |                |                                    |
| DFS for Euler tour      | O(N)           | O(N)           | Visit each node, record 2N times   |
| Depth recording         | O(N)           | O(N)           | Store depth at each tour position  |
| Build sparse table      | O(N log N)     | O(N log N)     | RMQ preprocessing                  |
| **Total Preprocessing** | **O(N log N)** | **O(N log N)** | Dominated by sparse table          |
| **Per Query**           |                |                |                                    |
| Find positions          | O(1)           | O(1)           | Direct lookup in first[]           |
| RMQ query               | O(1)           | O(1)           | Sparse table lookup                |
| LCA to distance         | O(1)           | O(1)           | depth[u] + depth[v] - 2×depth[lca] |
| **Per Query Total**     | **O(1)**       | **O(1)**       | Constant time                      |
| **Q Queries**           | **O(Q)**       | **O(1)**       | Total query time                   |

### Why This Complexity:

**Euler Tour:**

- Visit each edge twice (down and up): 2(N-1) steps
- Record depth at each position: O(2N) = O(N)

**Sparse Table for RMQ:**

- Build table st[i][j] = min in range [i, i+2^j)
- Levels: log₂(2N) ≈ log N levels
- Entries per level: 2N
- Total: O(2N × log N) = O(N log N)

**Query:**

- Euler tour positions: first[u] and first[v] precomputed
- RMQ(l, r): O(1) with sparse table (overlapping ranges trick)
- No tree traversal needed per query

**For N = 200K, Q = 200K:**

- Preprocessing: ~3.6M operations (one-time)
- Queries: ~200K operations (vs ~40B for naive BFS per query)

---

## 🧪 Walkthrough: Sample Testcase

### Input

```
5 3
1 2 3
1 3 2
2 4 5
2 5 1
4 5
1 3
3 5
```

### Visual Representation

```
Weighted Tree:
       1
     /   \
  (3)     (2)
   2       3
  / \
(5) (1)
 4   5

Distances from root 1:
d[1]=0, d[2]=3, d[3]=2, d[4]=8, d[5]=4
```

### Euler Tour

```
DFS: 1 → 2 → 4 → (back 2) → 5 → (back 2) → (back 1) → 3 → (back 1)

Euler:  [1, 2, 4, 2, 5, 2, 1, 3, 1]
Depths: [0, 1, 2, 1, 2, 1, 0, 1, 0]
first[]: 1→0, 2→1, 3→7, 4→2, 5→4
```

### Query Walkthrough

| Query | u   | v   | Range | Min Depth Node            | LCA | dist(u)+dist(v)-2×dist(LCA) | Answer |
| ----- | --- | --- | ----- | ------------------------- | --- | --------------------------- | ------ |
| 1     | 4   | 5   | [2,4] | depth 1 at pos 3 → node 2 | 2   | 8+4-2×3=6                   | **6**  |
| 2     | 1   | 3   | [0,7] | depth 0 at pos 0 → node 1 | 1   | 0+2-2×0=2                   | **2**  |
| 3     | 3   | 5   | [4,7] | depth 0 at pos 6 → node 1 | 1   | 2+4-2×0=6                   | **6**  |

**Output:**

```
6
2
6
```

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake               | ❌ Wrong                     | ✅ Correct                                    |
| --- | --------------------- | ---------------------------- | --------------------------------------------- |
| 1   | **Wrong Euler size**  | `euler[n]`                   | `euler[2*n - 1]` (visits each node twice - 1) |
| 2   | **first[] range**     | Query `[first[u], first[v]]` | Query `[min(first[u], first[v]), max(...)]`   |
| 3   | **Sparse table init** | `sparse[i][0] = euler[i]`    | `sparse[i][0] = depth[euler[i]]`              |
| 4   | **Distance formula**  | `dist[u] + dist[v]`          | `dist[u] + dist[v] - 2*dist[LCA]`             |

### Detailed Example:

**Mistake 2: Wrong Range Direction**

```python
# ❌ Wrong: Assumes first[u] < first[v]
def lca_query(u, v):
    return rmq_query(first[u], first[v])

# ✅ Correct: Handle either order
def lca_query(u, v):
    l = min(first[u], first[v])
    r = max(first[u], first[v])
    return rmq_query(l, r)
```

---

## ✅ Correctness Proof

### Invariant

The Euler tour depth array allows us to find LCA by identifying the node with minimum depth between any two positions.

### Proof

1. When traversing from node u to node v in the tree, we pass through LCA(u, v)
2. In the Euler tour, all nodes between first[u] and first[v] include all nodes on paths from root to u and root to v
3. The minimum depth in this range corresponds to their LCA
4. Distance formula: dist(u, v) = dist(root, u) + dist(root, v) - 2 × dist(root, LCA) is geometrically correct

---

## 🧪 Edge Cases

| Case           | Input           | Expected Output             |
| -------------- | --------------- | --------------------------- |
| Same node      | u = v           | 0                           |
| Adjacent nodes | u-v edge exists | weight(u, v)                |
| Root queries   | u = root        | depth[v]                    |
| Two leaves     | Deep leaves     | Sum of depths - 2×LCA depth |

---

## 🔗 Related Problems

1. **Binary Lifting for LCA** - Alternative O(log N) LCA query
2. **Heavy-Light Decomposition** - Path queries with updates
3. **Link-Cut Trees** - Dynamic tree queries
4. **Tarjan's Offline LCA** - Union-find based LCA

---

## 💡 Key Takeaways

1. **Euler tour flattens tree** into array for RMQ
2. **Sparse table provides O(1) RMQ** after O(N log N) preprocessing
3. **LCA reduces to RMQ** on depth array
4. **Distance calculation** uses LCA and precomputed depths
5. **Trade-off:** More preprocessing for faster queries
