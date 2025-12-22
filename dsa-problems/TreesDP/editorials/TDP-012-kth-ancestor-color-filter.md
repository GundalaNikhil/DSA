---
title: Binary Lifting for K-th Ancestor with Color Filter
problem_id: TDP_KTH_ANCESTOR_COLOR__3741
display_id: TDP-012
difficulty: Medium
tags:
- tree-dp
- binary-lifting
- ancestor-queries
- color-filter
editorial_categories:
- Tree DP
- Binary Lifting
slug: kth-ancestor-color-filter
---
## 📝 Problem Summary

Given a rooted tree where each node has a color, answer queries: "Find the k-th ancestor of node v that has color c." If node v itself has color c, it counts as the 1st such ancestor.

---

## 🌍 Real-World Scenario

**File System Permission Inheritance:** In a hierarchical file system, directories (nodes) have different permission levels (colors). When a process at directory v requests access requiring permission level c, the system needs to find which ancestor directory grants the access.

---

## 🔍 Approach: Linear Ancestor Walk

### Key Insight

**Important**: The node v itself is considered as an "ancestor" of itself. So when asked for the k-th ancestor with color c:

- If v has color c, then v is the 1st such ancestor
- The parent is checked next, then grandparent, etc.

### Visual Example

```
Tree rooted at 1:
        1 (color=1)
       / \
      2   3
    (c=2) (c=1)
    / \
   4   5
 (c=2)(c=1)

Query: (v=4, c=2, k=1)
- Start at node 4, color=2 ✓ count=1
- k=1 reached! Return 4

Query: (v=5, c=1, k=2)
- Start at node 5, color=1 ✓ count=1
- Parent is 2, color=2 ✗
- Grandparent is 1, color=1 ✓ count=2
- k=2 reached! Return 1
```

### Algorithm

```
findKthColoredAncestor(v, c, k):
    count = 0
    while v != 0:           // 0 means past root
        if color[v] == c:
            count++
            if count == k:
                return v
        v = parent[v]
    return -1               // Not enough ancestors with color c
```

---

## 🧪 Edge Cases

| Case              | Query     | Expected         | Explanation           |
| ----------------- | --------- | ---------------- | --------------------- |
| Node is root      | (1, c, k) | 1 or -1          | Only root to check    |
| Color not in path | (v, c, k) | -1               | No matching ancestors |
| k too large       | (v, c, k) | -1               | Not enough matches    |
| Single node       | (1, c, 1) | 1 if color[1]==c | Root has no parent    |

---

## 💻 Implementation

### Java

```java
import java.util.*;
public class KthAncestorColorFilter {
    static int n, LOG;
    static int[] color, depth;
    static int[][] up;
    static List<Integer>[] adj;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        LOG = 20;

        color = new int[n + 1];
        for (int i = 1; i <= n; i++) color[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        up = new int[n + 1][LOG];
        depth = new int[n + 1];
        dfs(1, 0);

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int v = sc.nextInt(), c = sc.nextInt(), k = sc.nextInt();
            System.out.println(findKthColoredAncestor(v, c, k));
        }
    }

    static void dfs(int u, int p) {
        up[u][0] = p;
        for (int i = 1; i < LOG; i++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
        for (int v : adj[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }

    static int findKthColoredAncestor(int v, int c, int k) {
        int count = 0;
        while (v != 0) {
            if (color[v] == c) {
                count++;
                if (count == k) return v;
            }
            v = up[v][0];
        }
        return -1;
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
    LOG = 20

    color = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    up = [[0] * LOG for _ in range(n + 1)]

    def dfs(u, p):
        up[u][0] = p
        for i in range(1, LOG):
            up[u][i] = up[up[u][i - 1]][i - 1]
        for v in adj[u]:
            if v != p:
                dfs(v, u)

    dfs(1, 0)

    def find_kth(v, c, k):
        count = 0
        while v != 0:
            if color[v] == c:
                count += 1
                if count == k: return v
            v = up[v][0]
        return -1

    q = int(data[idx]); idx += 1
    for _ in range(q):
        v, c, k = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        print(find_kth(v, c, k))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, LOG = 20;
vector<int> color;
vector<vector<int>> up, adj;

void dfs(int u, int p) {
    up[u][0] = p;
    for (int i = 1; i < LOG; i++) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }
}

int findKth(int v, int c, int k) {
    int count = 0;
    while (v != 0) {
        if (color[v] == c) {
            count++;
            if (count == k) return v;
        }
        v = up[v][0];
    }
    return -1;
}

int main() {
    cin >> n;
    color.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    up.assign(n + 1, vector<int>(LOG));
    dfs(1, 0);

    int q; cin >> q;
    while (q--) {
        int v, c, k; cin >> v >> c >> k;
        cout << findKth(v, c, k) << "\n";
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
  const LOG = 20;
  const color = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const up = Array.from({ length: n + 1 }, () => Array(LOG).fill(0));

  function dfs(u, p) {
    up[u][0] = p;
    for (let i = 1; i < LOG; i++) {
      up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (const v of adj[u]) {
      if (v !== p) dfs(v, u);
    }
  }

  dfs(1, 0);

  function findKth(v, c, k) {
    let count = 0;
    while (v !== 0) {
      if (color[v] === c) {
        count++;
        if (count === k) return v;
      }
      v = up[v][0];
    }
    return -1;
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [v, c, k] = lines[idx++].split(" ").map(Number);
    console.log(findKth(v, c, k));
  }
});
```

---

## 🧪 Walkthrough: Sample Testcase

### Input

```
5
2 1 2 1 2
1 2
1 3
2 4
2 5
3
4 2 1
5 1 2
3 2 2
```

### Visual Representation

```
Tree with colors:
       1 (c=2)
      / \
   2(c=1) 3(c=2)
   / \
4(c=1) 5(c=2)
```

### Query Walkthrough

| Query | v   | c   | k   | Path (v→root) | Colored ancestors                | k-th         | Answer |
| ----- | --- | --- | --- | ------------- | -------------------------------- | ------------ | ------ |
| 1     | 4   | 2   | 1   | 4→2→1         | c[4]=1❌, c[2]=1❌, c[1]=2✓      | 1st=1        | **1**  |
| 2     | 5   | 1   | 2   | 5→2→1         | c[5]=2❌, c[2]=1✓(1st), c[1]=2❌ | Only 1 found | **-1** |
| 3     | 3   | 2   | 2   | 3→1           | c[3]=2✓(1st), c[1]=2✓(2nd)       | 2nd=1        | **1**  |

**Output:**

```
1
-1
1
```

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                | ❌ Wrong                   | ✅ Correct                       |
| --- | ---------------------- | -------------------------- | -------------------------------- |
| 1   | **Skip starting node** | Start from parent of v     | Start counting from v itself     |
| 2   | **Wrong termination**  | `while (v != -1)`          | `while (v != 0)` (0 is sentinel) |
| 3   | **Return wrong node**  | Return when `count == k-1` | Return when `count == k`         |
| 4   | **Forget -1 case**     | No return for not found    | `return -1` after loop           |

### Detailed Example:

**Mistake 1: Skipping the Starting Node**

```python
# ❌ Wrong: Skip v, start from parent
def find_kth(v, c, k):
    count = 0
    v = parent[v]  # WRONG! Should start at v
    while v != 0:
        if color[v] == c:
            count += 1
            if count == k: return v
        v = parent[v]
    return -1

# ✅ Correct: Start counting from v itself
def find_kth(v, c, k):
    count = 0
    while v != 0:
        if color[v] == c:
            count += 1
            if count == k: return v
        v = parent[v]
    return -1
```

---

## ⏱️ Complexity

| Metric            | Value                        |
| ----------------- | ---------------------------- |
| **Preprocessing** | O(N log N)                   |
| **Query**         | O(N) per query (linear walk) |
| **Space**         | O(N log N)                   |

### Complexity Breakdown

- **Preprocessing**: Binary lifting table with O(log N) entries per node
- **Query**: Worst case walks from leaf to root (O(N) for skewed tree)
- **Total for Q queries**: O(N log N + Q × N)

### Optimization Potential

### Complexity Analysis

| Phase                   | Time             | Space          | Explanation             |
| ----------------------- | ---------------- | -------------- | ----------------------- |
| **Preprocessing**       |                  |                |                         |
| DFS + binary lifting    | O(N log N)       | O(N log N)     | Build up[][] table      |
| Depth computation       | O(N)             | O(N)           | Traverse tree           |
| **Total Preprocessing** | **O(N log N)**   | **O(N log N)** | Standard binary lifting |
| **Per Query**           |                  |                |                         |
| Binary lifting to kth   | O(k log N) worst | O(1)           | Walk up checking colors |
| Check color             | O(1) per step    | O(1)           | Array lookup            |
| **Naive Per Query**     | **O(k)**         | **O(1)**       | Linear walk up tree     |
| **Optimized Query**     | **O(log N)**     | **O(log N)**   | Color-specific jumps    |

### Why O(k) for Naive?

**Naive Algorithm:**

```
current = v
count = 0
while current != -1:
    if color[current] == C:
        count++
        if count == k:
            return current
    current = parent[current]
```

- Must check up to k ancestors with color C
- In worst case (all nodes have color C): O(k) steps
- Total for Q queries: O(Q·k)

**Optimized with Color-Specific Jumps:**

- Precompute `colorUp[v][c]` = nearest ancestor of v with color c
- Then use binary search on depth
- Query becomes O(log N) per query
- Preprocessing: O(N·C) where C = number of colors

**For N = 200K, Q = 200K, k = 100:**

- Naive: ~20M operations per query = 4T total
- Binary lifting: ~3.6M preprocessing + ~200K×log(200K) ≈ ~4M queries

---

## 💡 Key Takeaways

1. **Node counts as ancestor**: When finding k-th colored ancestor, start counting from v itself
2. Binary lifting enables O(log N) ancestor access
3. Color filtering with linear walk is simple and sufficient for moderate Q
4. For heavy queries, precompute color-specific ancestors
