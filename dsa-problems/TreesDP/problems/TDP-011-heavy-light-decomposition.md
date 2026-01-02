---
title: "Heavy-Light Decomposition Basics"
problem_id: TDP_HEAVY_LIGHT_DECOMP__8154
display_id: TDP-011
difficulty: Medium
tags: [tree-dp, heavy-light-decomposition, path-queries, segment-tree]
slug: heavy-light-decomposition
time_limit: 2000
memory_limit: 256
---

## Problem Description

Given a weighted tree, preprocess it to answer path sum queries efficiently. Use Heavy-Light Decomposition to partition the tree into chains.

---

## Input Format

- Line 1: N (number of nodes)
- Line 2: N integers (node values)
- Next N-1 lines: u, v (edges)
- Next line: Q (number of queries)
- Next Q lines: u, v (query sum on path from u to v)

---

## Output Format

For each query, print the sum of values on the path from u to v.

---

## Examples

### Example 1

**Input:**

```
5
1 2 3 4 5
1 2
1 3
2 4
2 5
3
1 4
3 5
4 5
```

**Output:**

```
7
11
11
```

### Example 2

**Input:**

```
3
10 20 30
1 2
2 3
2
1 3
1 2
```

**Output:**

```
60
30
```

---

## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

---

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static int n, timer;
    static List<int[]>[] adj;
    static int[] parent, depth, heavy, head, pos, values;
    static long[] segTree;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        values = new int[n + 1];
        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(new int[]{v});
            adj[v].add(new int[]{u});
        }

        parent = new int[n + 1];
        depth = new int[n + 1];
        heavy = new int[n + 1];
        head = new int[n + 1];
        pos = new int[n + 1];

        Arrays.fill(heavy, -1);

        dfs1(1, 0);
        timer = 0;
        dfs2(1, 1);

        segTree = new long[4 * n];
        build(1, 0, n - 1);

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            System.out.println(queryPath(u, v));
        }
    }

    static int dfs1(int u, int p) {
        int size = 1, maxSize = 0;
        parent[u] = p;
        depth[u] = (p == 0) ? 0 : depth[p] + 1;

        for (int[] edge : adj[u]) {
            int v = edge[0];
            if (v == p) continue;
            int subtreeSize = dfs1(v, u);
            size += subtreeSize;
            if (subtreeSize > maxSize) {
                maxSize = subtreeSize;
                heavy[u] = v;
            }
        }
        return size;
    }

    static void dfs2(int u, int h) {
        head[u] = h;
        pos[u] = timer++;

        if (heavy[u] != -1) {
            dfs2(heavy[u], h);
        }

        for (int[] edge : adj[u]) {
            int v = edge[0];
            if (v != parent[u] && v != heavy[u]) {
                dfs2(v, v);
            }
        }
    }

    static void build(int node, int l, int r) {
        if (l == r) {
            for (int i = 1; i <= n; i++) {
                if (pos[i] == l) {
                    segTree[node] = values[i];
                    break;
                }
            }
            return;
        }
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
        segTree[node] = segTree[2 * node] + segTree[2 * node + 1];
    }

    static long query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return segTree[node];
        int mid = (l + r) / 2;
        return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr);
    }

    static long queryPath(int u, int v) {
        long result = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) {
                int temp = u; u = v; v = temp;
            }
            result += query(1, 0, n - 1, pos[head[u]], pos[u]);
            u = parent[head[u]];
        }
        if (depth[u] > depth[v]) {
            int temp = u; u = v; v = temp;
        }
        result += query(1, 0, n - 1, pos[u], pos[v]);
        return result;
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    values = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    heavy = [-1] * (n + 1)
    head = [0] * (n + 1)
    pos = [0] * (n + 1)
    timer = [0]

    def dfs1(u, p):
        return 0
    def dfs2(u, h):
        return 0
    dfs1(1, 0)
    dfs2(1, 1)

    # Build segment tree
    seg = [0] * (4 * n)
    pos_to_val = [0] * n
    for i in range(1, n + 1):
        pos_to_val[pos[i]] = values[i]

    def build(node, l, r):
        return 0
    def query(node, l, r, ql, qr):
        return 0
    build(1, 0, n - 1)

    def query_path(u, v):
        return 0
    q = int(data[idx]); idx += 1
    for _ in range(q):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        print(query_path(u, v))

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
vector<vector<int>> adj;
vector<int> parent, depth, heavy, head, pos, values;
vector<long long> segTree;

int dfs1(int u, int p) {
    int size = 1, maxSize = 0;
    parent[u] = p;
    depth[u] = (p == 0) ? 0 : depth[p] + 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        int subtreeSize = dfs1(v, u);
        size += subtreeSize;
        if (subtreeSize > maxSize) {
            maxSize = subtreeSize;
            heavy[u] = v;
        }
    }
    return size;
}

void dfs2(int u, int h) {
    head[u] = h;
    pos[u] = timer_val++;

    if (heavy[u] != -1) dfs2(heavy[u], h);

    for (int v : adj[u]) {
        if (v != parent[u] && v != heavy[u]) {
            dfs2(v, v);
        }
    }
}

void build(int node, int l, int r, vector<int>& posToVal) {
    if (l == r) {
        segTree[node] = posToVal[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * node, l, mid, posToVal);
    build(2 * node + 1, mid + 1, r, posToVal);
    segTree[node] = segTree[2 * node] + segTree[2 * node + 1];
}

long long query(int node, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return segTree[node];
    int mid = (l + r) / 2;
    return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr);
}

long long queryPath(int u, int v) {
    long long result = 0;
    while (head[u] != head[v]) {
        if (depth[head[u]] < depth[head[v]]) swap(u, v);
        result += query(1, 0, n - 1, pos[head[u]], pos[u]);
        u = parent[head[u]];
    }
    if (depth[u] > depth[v]) swap(u, v);
    result += query(1, 0, n - 1, pos[u], pos[v]);
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    values.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> values[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    parent.resize(n + 1);
    depth.resize(n + 1);
    heavy.assign(n + 1, -1);
    head.resize(n + 1);
    pos.resize(n + 1);
    segTree.resize(4 * n);

    dfs1(1, 0);
    timer_val = 0;
    dfs2(1, 1);

    vector<int> posToVal(n);
    for (int i = 1; i <= n; i++) {
        posToVal[pos[i]] = values[i];
    }
    build(1, 0, n - 1, posToVal);

    int q; cin >> q;
    for (int i = 0; i < q; i++) {
        int u, v; cin >> u >> v;
        cout << queryPath(u, v) << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const data = [];
  lines.forEach(line => data.push(...line.split(" ")));
  
  let idx = 0;
  const n = parseInt(data[idx++]);
  const values = [0];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++]));
  }

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++]);
    const v = parseInt(data[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const parent = Array(n + 1).fill(0);
  const depth = Array(n + 1).fill(0);
  const heavy = Array(n + 1).fill(-1);
  const head = Array(n + 1).fill(0);
  const pos = Array(n + 1).fill(0);
  const timer = [0];

  function dfs1(u, p) {
    return 0;
  }

  function dfs2(u, h) {
    return 0;
  }

  dfs1(1, 0);
  dfs2(1, 1);

  const posToVal = Array(n).fill(0);
  for (let i = 1; i <= n; i++) {
    posToVal[pos[i]] = values[i];
  }

  const seg = Array(4 * n).fill(0);

  function build(node, l, r) {
    return 0;
  }

  function query(node, l, r, ql, qr) {
    return 0;
  }

  build(1, 0, n - 1);

  function queryPath(u, v) {
    return 0;
  }

  const q = parseInt(data[idx++]);
  for (let i = 0; i < q; i++) {
    const u = parseInt(data[idx++]);
    const v = parseInt(data[idx++]);
    console.log(queryPath(u, v));
  }
});
```

