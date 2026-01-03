---
title: "Path Queries with Euler Tour and RMQ"
problem_id: TDP_PATH_QUERIES_RMQ__6729
display_id: TDP-009
difficulty: Medium
tags: [tree-dp, euler-tour, rmq, lca, sparse-table]
slug: path-queries-rmq
time_limit: 2000
memory_limit: 256
---

## Problem Description

You are given a weighted tree with N nodes. The tree has N-1 edges, where each edge has a weight w. You need to preprocess the tree to efficiently answer Q distance queries. Each query asks for the shortest distance between two nodes u and v along the tree path.

---

## Input Format

- First line: Integer N (1 ≤ N ≤ 200,000) — number of nodes
- Next N-1 lines: Three integers u, v, w (1 ≤ u, v ≤ N, 1 ≤ w ≤ 10^6) — edge between u and v with weight w
- Next line: Integer Q (1 ≤ Q ≤ 200,000) — number of queries
- Next Q lines: Two integers u, v — query for distance between u and v

---

## Output Format

For each query, print the distance between nodes u and v.

---

## Examples

### Example 1

**Input:**

```
3
1 2 5
1 3 10
2
2 3
1 2
```

**Output:**

```
15
5
```

**Explanation:**

- Query 1: Distance from node 2 to node 3 = 5 (edge 2-1) + 10 (edge 1-3) = 15
- Query 2: Distance from node 1 to node 2 = 5

### Example 2

**Input:**

```
5
1 2 3
1 3 7
2 4 2
2 5 4
3
4 5
3 5
1 4
```

**Output:**

```
6
14
5
```

**Explanation:**

- Query 1: Distance from node 4 to node 5
  - Path: 4→2→5
  - Distance: 2 (edge 4-2) + 4 (edge 2-5) = 6
- Query 2: Distance from node 3 to node 5
  - Path: 3→1→2→5
  - Distance: 7 (edge 3-1) + 3 (edge 1-2) + 4 (edge 2-5) = 14
- Query 3: Distance from node 1 to node 4
  - Path: 1→2→4
  - Distance: 3 (edge 1-2) + 2 (edge 2-4) = 5

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ w ≤ 10^6
- The graph is guaranteed to be a tree
- 1 ≤ u, v ≤ N

---

## Solution Template

### Java

```java
import java.util.*;

class Main {
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

        //Implement here

    }

static void buildSparseTable() {

        //Implement here

    }

static int queryLCA(int u, int v) {

        //Implement here

        return 0;

    }

static int queryDistance(int u, int v) {

        //Implement here

        return 0;

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
        # //Implement here
        return 0
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
        # //Implement here
        return 0
    def query_distance(u, v):
        # //Implement here
        return 0
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
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int n, timer_val;
vector<vector<pair<int, int>>> adj;
vector<int> first_occ, depth_val, euler_tour;
vector<vector<int>> st;
int log_size;


void dfs(int u, int p, int d) {

    //Implement here

}

void build_sparse_table() {

    //Implement here

}

int query_lca(int u, int v) {

    //Implement here

    return 0;

}

int query_distance(int u, int v) {

    //Implement here

    return 0;

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
    //Implement here
    return 0;
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
    //Implement here
    return 0;
  }

  function queryDistance(u, v) {
    //Implement here
    return 0;
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(queryDistance(u, v));
  }
});
```
