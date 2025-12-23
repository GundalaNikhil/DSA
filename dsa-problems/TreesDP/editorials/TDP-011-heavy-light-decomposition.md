---
title: Heavy-Light Decomposition Basics
problem_id: TDP_HEAVY_LIGHT_DECOMP__8154
display_id: TDP-011
difficulty: Medium
tags:
- tree-dp
- heavy-light-decomposition
- path-queries
- segment-tree
editorial_categories:
- Tree DP
- Advanced Data Structures
slug: heavy-light-decomposition
---
## 📝 Problem Summary

Decompose tree into heavy and light chains to answer path queries (sum/max) efficiently using segment trees. Heavy-Light Decomposition (HLD) enables O(log² N) path queries on trees.

---

## 🌍 Real-World Scenario

**Network Bandwidth Monitoring:** In a network topology (tree structure), monitor bandwidth usage along paths. HLD allows efficiently querying "total/max bandwidth on path from server A to B" and updating link capacities dynamically.

---

## 🔍 Approach: Heavy-Light Decomposition with Segment Tree

### Key Insight

Partition tree into heavy paths (each node's heavy child is the one with largest subtree) and light edges. Any root-to-node path crosses at most O(log N) light edges, allowing efficient queries by combining at most O(log N) segment tree queries.

### Visual Example

```
Tree:
        1 (val=3)
       / \
     2    3
  (val=5) (val=2)
   /|\
  4 5 6
(1)(4)(2)

Heavy children (largest subtree):
- Node 1's heavy child = 2 (subtree size 4)
- Node 2's heavy child = 5 (or any, equal sizes)

Heavy chains: [1→2→5], [3], [4], [6]

Query path(4, 3):
- Path: 4 → 2 → 1 → 3
- Chains traversed: [4], [1→2], [3]
- Sum: 1 + (3+5) + 2 = 11
```

### Algorithm

1. **DFS 1**: Compute subtree sizes, designate heavy children
2. **DFS 2**: Assign positions in chains, build chains
3. **Segment Tree**: Store chain values for range queries
4. **Path Query**: Decompose path into O(log N) chains, query each

---

## 🧪 Edge Cases

| Case            | Input               | Expected            | Explanation           |
| --------------- | ------------------- | ------------------- | --------------------- |
| Single node     | n=1, query(1,1)     | val[1]              | Path is just the node |
| Linear tree     | Chain 1-2-3-...-n   | Sum of path segment | All one chain         |
| Query same node | query(v, v)         | val[v]              | LCA is v itself       |
| Leaf to leaf    | query(leaf1, leaf2) | Sum via LCA         | Crosses root possibly |

---

## 💻 Implementation

### Java

```java
import java.util.*;

public class HeavyLightDecomposition {
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
        size, max_size = 1, 0
        parent[u] = p
        depth[u] = 0 if p == 0 else depth[p] + 1

        for v in adj[u]:
            if v == p: continue
            subtree_size = dfs1(v, u)
            size += subtree_size
            if subtree_size > max_size:
                max_size = subtree_size
                heavy[u] = v
        return size

    def dfs2(u, h):
        head[u] = h
        pos[u] = timer[0]
        timer[0] += 1

        if heavy[u] != -1:
            dfs2(heavy[u], h)

        for v in adj[u]:
            if v != parent[u] and v != heavy[u]:
                dfs2(v, v)

    dfs1(1, 0)
    dfs2(1, 1)

    # Build segment tree
    seg = [0] * (4 * n)
    pos_to_val = [0] * n
    for i in range(1, n + 1):
        pos_to_val[pos[i]] = values[i]

    def build(node, l, r):
        if l == r:
            seg[node] = pos_to_val[l]
            return
        mid = (l + r) // 2
        build(2 * node, l, mid)
        build(2 * node + 1, mid + 1, r)
        seg[node] = seg[2 * node] + seg[2 * node + 1]

    def query(node, l, r, ql, qr):
        if ql > r or qr < l: return 0
        if ql <= l and r <= qr: return seg[node]
        mid = (l + r) // 2
        return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)

    build(1, 0, n - 1)

    def query_path(u, v):
        result = 0
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            result += query(1, 0, n - 1, pos[head[u]], pos[u])
            u = parent[head[u]]
        if depth[u] > depth[v]:
            u, v = v, u
        result += query(1, 0, n - 1, pos[u], pos[v])
        return result

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
#include <bits/stdc++.h>
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
  let idx = 0;
  const n = parseInt(lines[idx++]);
  const values = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const parent = Array(n + 1).fill(0);
  const depth = Array(n + 1).fill(0);
  const heavy = Array(n + 1).fill(-1);
  const head = Array(n + 1).fill(0);
  const pos = Array(n + 1).fill(0);
  let timer = 0;

  function dfs1(u, p) {
    let size = 1,
      maxSize = 0;
    parent[u] = p;
    depth[u] = p === 0 ? 0 : depth[p] + 1;

    for (const v of adj[u]) {
      if (v === p) continue;
      const subtreeSize = dfs1(v, u);
      size += subtreeSize;
      if (subtreeSize > maxSize) {
        maxSize = subtreeSize;
        heavy[u] = v;
      }
    }
    return size;
  }

  function dfs2(u, h) {
    head[u] = h;
    pos[u] = timer++;

    if (heavy[u] !== -1) dfs2(heavy[u], h);

    for (const v of adj[u]) {
      if (v !== parent[u] && v !== heavy[u]) {
        dfs2(v, v);
      }
    }
  }

  dfs1(1, 0);
  dfs2(1, 1);

  const posToVal = Array(n).fill(0);
  for (let i = 1; i <= n; i++) {
    posToVal[pos[i]] = values[i];
  }

  const seg = Array(4 * n).fill(0);

  function build(node, l, r) {
    if (l === r) {
      seg[node] = posToVal[l];
      return;
    }
    const mid = Math.floor((l + r) / 2);
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
    seg[node] = seg[2 * node] + seg[2 * node + 1];
  }

  function query(node, l, r, ql, qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return seg[node];
    const mid = Math.floor((l + r) / 2);
    return (
      query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)
    );
  }

  build(1, 0, n - 1);

  function queryPath(u, v) {
    let result = 0;
    while (head[u] !== head[v]) {
      if (depth[head[u]] < depth[head[v]]) [u, v] = [v, u];
      result += query(1, 0, n - 1, pos[head[u]], pos[u]);
      u = parent[head[u]];
    }
    if (depth[u] > depth[v]) [u, v] = [v, u];
    result += query(1, 0, n - 1, pos[u], pos[v]);
    return result;
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(queryPath(u, v));
  }
});
```

---

## 🧪 Walkthrough: Sample Testcase

### Input

```
5
3 5 2 4 1
1 2
1 3
2 4
2 5
2
4 5
1 3
```

### Visual Representation

```
Tree with values:
       1 (val=3)
      / \
    2(5) 3(2)
   / \
 4(4) 5(1)

Subtree sizes: 1→5, 2→3, 3→1, 4→1, 5→1
Heavy child: 1→2 (size 3), 2→4 or 5 (tie, pick first)
Heavy chains: [1,2,4], [3], [5]
```

### HLD Position Assignment

```
pos[]: 1→0, 2→1, 4→2, 3→3, 5→4
head[]: 1→1, 2→1, 4→1, 3→3, 5→5
Segment tree on: [3, 5, 4, 2, 1]
```

### Query Walkthrough

| Query | u   | v   | Chains Traversed       | Segment Queries           | Sum    |
| ----- | --- | --- | ---------------------- | ------------------------- | ------ |
| 1     | 4   | 5   | 4 in [1,2,4], 5 in [5] | [2,2]→4, [4,4]→1, [1,1]→5 | **10** |
| 2     | 1   | 3   | 1 in [1,2,4], 3 in [3] | [3,3]→2, [0,0]→3          | **5**  |

**Output:**

```
10
5
```

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                       | ❌ Wrong                | ✅ Correct                                  |
| --- | ----------------------------- | ----------------------- | ------------------------------------------- |
| 1   | **Heavy child = first child** | Pick any child as heavy | Pick child with largest subtree             |
| 2   | **Wrong position order**      | Random DFS order        | Heavy child first in DFS2                   |
| 3   | **Head assignment**           | `head[v] = v` always    | `head[v] = head[u]` if v is heavy child     |
| 4   | **Query termination**         | Until u == v            | Until `head[u] == head[v]` then final range |

### Detailed Example:

**Mistake 3: Incorrect Head Assignment**

```python
# ❌ Wrong: Every node is its own head
def dfs2(u, h):
    head[u] = u  # WRONG!
    pos[u] = timer++
    if heavy[u] != -1:
        dfs2(heavy[u], head[u])
    for v in children[u]:
        if v != heavy[u]:
            dfs2(v, v)

# ✅ Correct: Heavy children inherit parent's head
def dfs2(u, h):
    head[u] = h  # Inherit from caller
    pos[u] = timer++
    if heavy[u] != -1:
        dfs2(heavy[u], h)  # Same head for heavy child
    for v in children[u]:
        if v != heavy[u]:
            dfs2(v, v)  # New head for light child
```

---

## ⏱️ Complexity Analysis

### Detailed Breakdown

| Phase                   | Time            | Space    | Explanation               |
| ----------------------- | --------------- | -------- | ------------------------- |
| **Preprocessing**       |                 |          |                           |
| DFS1 (subtree sizes)    | O(N)            | O(N)     | Compute size[] array      |
| DFS2 (decompose chains) | O(N)            | O(N)     | Assign head[], pos[]      |
| Build segment tree      | O(N)            | O(N)     | Initialize with values    |
| **Total Preprocessing** | **O(N)**        | **O(N)** | Linear setup              |
| **Per Query**           |                 |          |                           |
| Find LCA                | O(log N)        | O(1)     | Jump up light edges       |
| Chain traversals        | O(log N) chains | O(1)     | At most log N chains      |
| Segment query per chain | O(log N)        | O(1)     | Standard segment tree     |
| **Per Query Total**     | **O(log² N)**   | **O(1)** | log chains × log seg tree |
| **Q Queries**           | **O(Q log² N)** | **O(1)** | Total query time          |

### Why O(log N) Chains?

**Heavy-Light Lemma:**

- Each light edge move halves the subtree size
- From any node to root: at most log₂ N light edges
- Therefore: at most O(log N) chains on any path

**Proof:**

- When moving from child c to parent p via light edge:
- size[c] ≤ size[p] / 2 (by definition of heavy child)
- Starting from subtree size S, after k light edges: size ≤ S / 2ᵏ
- To reach root (size = N): k ≤ log₂ N

**Per-Query Breakdown:**

1. Path from u to LCA: O(log N) chains
2. Path from v to LCA: O(log N) chains
3. Each chain: one segment tree query = O(log N)
4. Total: O(log N) chains × O(log N) per query = O(log² N)

**For N = 200K, Q = 200K:**

- Preprocessing: ~200K operations
- Per query: ~(log 200K)² ≈ 18² = 324 operations
- Total: ~65M operations vs ~40B for naive

---

## 💡 Key Takeaways

1. **HLD enables efficient tree path queries** - reduces to segment tree operations
2. **Heavy child = largest subtree** - ensures O(log N) chains
3. **Segment tree per linearized tree** - not per chain (one global array)
4. **O(log² N) total**: O(log N) chains × O(log N) per query
5. **Supports both sum and max** - change segment tree merge operation


## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ Q ≤ 200,000
- 1 ≤ values[i] ≤ 10^9

---