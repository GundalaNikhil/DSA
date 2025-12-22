---
title: Tree Flatten with Subtree Updates
problem_id: TDP_TREE_FLATTEN_UPDATES__5418
display_id: TDP-016
difficulty: Medium
tags:
- tree-dp
- euler-tour
- fenwick-tree
- range-updates
editorial_categories:
- Tree DP
- Euler Tour
slug: tree-flatten-subtree-updates
---
## 📝 Problem Summary

Support two operations on a tree:

1. **Subtree Add**: Add value `val` to all nodes in subtree of u
2. **Point Query**: Get current value of node u

---

## 🌍 Real-World Scenario

**Department Budget Updates:** In a company hierarchy (tree), when a department head (node u) receives budget allocation, all sub-departments (subtree) get updated. Query individual department budgets efficiently.

---

## 🔍 Approach: Euler Tour + Fenwick Tree

### Key Insight

**Euler Tour** (DFS time stamps) converts each subtree to a contiguous interval:

- `in[u]` = entry time of node u
- `out[u]` = exit time (after all descendants)
- Subtree(u) = all nodes with times in `[in[u], out[u]]`

Then subtree operations become range operations on an array!

### Visual Example

```
Tree:
      1
     / \
    2   3
   /|
  4 5

DFS traversal: 1 → 2 → 4 → 5 → 3

Euler Tour times:
Node:   1  2  3  4  5
in[]:   1  2  5  3  4
out[]:  5  4  5  3  4

Subtree(2) = nodes with time in [2,4] = {2,4,5} ✓
Subtree(1) = nodes with time in [1,5] = {1,2,3,4,5} ✓
```

### Algorithm

1. **Preprocess**: DFS to compute `in[]` and `out[]`
2. **Subtree Add(u, val)**: Range add on `[in[u], out[u]]`
3. **Point Query(u)**: Point query at `in[u]`

For **range add + point query**, use Fenwick Tree with difference array trick.

---

## 🧪 Edge Cases

| Case                | Input                        | Expected                            | Explanation             |
| ------------------- | ---------------------------- | ----------------------------------- | ----------------------- |
| Query root          | query(1)                     | sum of all adds to root's ancestors | Root in all subtrees    |
| Leaf update         | add(leaf, v)                 | Only leaf affected                  | Subtree is just leaf    |
| No updates          | query(u)                     | Initial value[u]                    | Just initial value      |
| Overlapping updates | add(1,5), add(2,3), query(4) | 5+3+initial                         | Both subtrees contain 4 |

---

## 💻 Implementation

### Java

```java
import java.util.*;
public class TreeFlattenUpdates {
    static int timer;
    static int[] in, out, values;
    static List<Integer>[] adj;
    static long[] fenwick;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        values = new int[n + 1];
        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        in = new int[n + 1];
        out = new int[n + 1];
        timer = 0;
        dfs(1, 0);

        fenwick = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            update(in[i], values[i]);
            update(in[i] + 1, -values[i]);
        }

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int type = sc.nextInt();
            if (type == 1) {
                int u = sc.nextInt(), val = sc.nextInt();
                rangeUpdate(in[u], out[u], val);
            } else {
                int u = sc.nextInt();
                System.out.println(query(in[u]));
            }
        }
    }

    static void dfs(int u, int p) {
        in[u] = ++timer;
        for (int v : adj[u]) {
            if (v != p) dfs(v, u);
        }
        out[u] = timer;
    }

    static void update(int i, long val) {
        while (i < fenwick.length) {
            fenwick[i] += val;
            i += i & (-i);
        }
    }

    static long query(int i) {
        long sum = 0;
        while (i > 0) {
            sum += fenwick[i];
            i -= i & (-i);
        }
        return sum;
    }

    static void rangeUpdate(int l, int r, int val) {
        update(l, val);
        update(r + 1, -val);
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
        adj[u].append(v); adj[v].append(u)

    timer = [0]
    in_time = [0] * (n + 1)
    out_time = [0] * (n + 1)

    def dfs(u, p):
        timer[0] += 1
        in_time[u] = timer[0]
        for v in adj[u]:
            if v != p: dfs(v, u)
        out_time[u] = timer[0]

    dfs(1, 0)

    fenwick = [0] * (n + 2)

    def update(i, val):
        while i <= n:
            fenwick[i] += val
            i += i & (-i)

    def query(i):
        s = 0
        while i > 0:
            s += fenwick[i]
            i -= i & (-i)
        return s

    for i in range(1, n + 1):
        update(in_time[i], values[i])
        update(in_time[i] + 1, -values[i])

    q = int(data[idx]); idx += 1
    for _ in range(q):
        t = int(data[idx]); idx += 1
        if t == 1:
            u, val = int(data[idx]), int(data[idx + 1])
            idx += 2
            update(in_time[u], val)
            update(out_time[u] + 1, -val)
        else:
            u = int(data[idx]); idx += 1
            print(query(in_time[u]))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, timer_val;
vector<int> values, in_time, out_time;
vector<vector<int>> adj;
vector<long long> fenwick;

void dfs(int u, int p) {
    in_time[u] = ++timer_val;
    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }
    out_time[u] = timer_val;
}

void update(int i, long long val) {
    while (i <= n) {
        fenwick[i] += val;
        i += i & (-i);
    }
}

long long query(int i) {
    long long sum = 0;
    while (i > 0) {
        sum += fenwick[i];
        i -= i & (-i);
    }
    return sum;
}

int main() {
    cin >> n;
    values.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> values[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    in_time.resize(n + 1);
    out_time.resize(n + 1);
    fenwick.resize(n + 2);
    timer_val = 0;
    dfs(1, 0);

    for (int i = 1; i <= n; i++) {
        update(in_time[i], values[i]);
        update(in_time[i] + 1, -values[i]);
    }

    int q; cin >> q;
    while (q--) {
        int t; cin >> t;
        if (t == 1) {
            int u; long long val; cin >> u >> val;
            update(in_time[u], val);
            update(out_time[u] + 1, -val);
        } else {
            int u; cin >> u;
            cout << query(in_time[u]) << "\n";
        }
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

  let timer = 0;
  const inTime = Array(n + 1).fill(0);
  const outTime = Array(n + 1).fill(0);

  function dfs(u, p) {
    inTime[u] = ++timer;
    for (const v of adj[u]) {
      if (v !== p) dfs(v, u);
    }
    outTime[u] = timer;
  }

  dfs(1, 0);

  const fenwick = Array(n + 2).fill(0);

  function update(i, val) {
    while (i <= n) {
      fenwick[i] += val;
      i += i & -i;
    }
  }

  function query(i) {
    let sum = 0;
    while (i > 0) {
      sum += fenwick[i];
      i -= i & -i;
    }
    return sum;
  }

  for (let i = 1; i <= n; i++) {
    update(inTime[i], values[i]);
    update(inTime[i] + 1, -values[i]);
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const parts = lines[idx++].split(" ").map(Number);
    if (parts[0] === 1) {
      const [_, u, val] = parts;
      update(inTime[u], val);
      update(outTime[u] + 1, -val);
    } else {
      const [_, u] = parts;
      console.log(query(inTime[u]));
    }
  }
});
```

---

## 🧪 Walkthrough: Sample Testcase

### Input

```
5
10 20 30 40 50
1 2
1 3
2 4
2 5
3
1 2 5
2 4
2 1
```

### Visual Representation

```
Tree Structure:          Euler Tour Assignment:
       1                  Node: 1  2  3  4  5
      / \                 in:   1  2  5  3  4
     2   3                out:  5  4  5  3  4
    / \
   4   5

Euler order: [_, 1, 2, 4, 5, 3]
             idx 1  2  3  4  5
```

### Euler Tour Ranges

| Node | in_time | out_time | Subtree Range     |
| ---- | ------- | -------- | ----------------- |
| 1    | 1       | 5        | [1,5] = all nodes |
| 2    | 2       | 4        | [2,4] = {2,4,5}   |
| 3    | 5       | 5        | [5,5] = {3}       |
| 4    | 3       | 3        | [3,3] = {4}       |
| 5    | 4       | 4        | [4,4] = {5}       |

### Query Walkthrough

| Query   | Operation           | Effect                   | Result |
| ------- | ------------------- | ------------------------ | ------ |
| `1 2 5` | Add 5 to subtree(2) | Nodes {2,4,5} += 5       | -      |
| `2 4`   | Query node 4        | Original 40 + 5 = **45** | 45     |
| `2 1`   | Query node 1        | Node 1 not in subtree(2) | **10** |

### Fenwick Array Updates

```
Initial values at Euler positions:
  pos:     1   2   3   4   5
  node:    1   2   4   5   3
  value:  10  20  40  50  30

After "1 2 5" (add 5 to subtree of node 2):
  update(in[2], +5) = update(2, +5)
  update(out[2]+1, -5) = update(5, -5)

Point query for node 4: query(in[4]) = query(3)
  = prefix_sum(3) = initial(40) + delta(+5) = 45
```

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                   | ❌ Wrong               | ✅ Correct                 |
| --- | ------------------------- | ---------------------- | -------------------------- |
| 1   | **Wrong range end**       | `update(out[u], -val)` | `update(out[u]+1, -val)`   |
| 2   | **Forget initial values** | Only apply updates     | Initialize all nodes first |
| 3   | **Query wrong index**     | `query(node_id)`       | `query(in_time[node_id])`  |
| 4   | **1-indexed confusion**   | Start at 0             | Euler timer starts at 1    |

### Detailed Example:

**Mistake 1: Off-by-one in Range Update**

```python
# ❌ Wrong: Excludes last element of subtree
def add_to_subtree(u, val):
    update(in_time[u], val)
    update(out_time[u], -val)  # Wrong! Should be out_time[u] + 1

# ✅ Correct: Include all nodes in subtree range
def add_to_subtree(u, val):
    update(in_time[u], val)
    update(out_time[u] + 1, -val)  # +1 to include node at out_time
```

**Mistake 2: Forgetting Initial Values**

```python
# ❌ Wrong: Queries return 0 initially
dfs(1, 0)  # Compute Euler tour
# Missing: Initialize node values in Fenwick!

# ✅ Correct: Set initial values
dfs(1, 0)
for i in range(1, n + 1):
    update(in_time[i], values[i])
    update(in_time[i] + 1, -values[i])
```

---

## ⏱️ Complexity

### Detailed Breakdown

| Phase                   | Time                | Space    | Explanation                      |
| ----------------------- | ------------------- | -------- | -------------------------------- |
| **Preprocessing**       |                     |          |                                  |
| DFS Euler tour          | O(N)                | O(h)     | Visit each node once             |
| Assign in/out times     | O(N)                | O(N)     | Store 2 values per node          |
| Build Fenwick tree      | O(N log N)          | O(N)     | Initialize N values              |
| **Total Preprocessing** | **O(N log N)**      | **O(N)** | Dominated by Fenwick init        |
| **Per Update**          |                     |          |                                  |
| Two point updates       | O(log N)            | O(1)     | update(in[u]) + update(out[u]+1) |
| Fenwick propagation     | O(log N) per update | O(1)     | Propagate up tree                |
| **Per Update Total**    | **O(log N)**        | **O(1)** | Constant updates                 |
| **Per Query**           |                     |          |                                  |
| One prefix sum          | O(log N)            | O(1)     | query(in[u])                     |
| Fenwick accumulation    | O(log N)            | O(1)     | Sum up tree                      |
| **Per Query Total**     | **O(log N)**        | **O(1)** | Single query                     |
| **Q Operations**        | **O(Q log N)**      | **O(1)** | Q updates + queries              |

### Why O(N log N) Preprocessing?

**Euler Tour: O(N)**

```python
def dfs(u, parent):
    timer += 1
    in_time[u] = timer
    for v in adj[u]:
        if v != parent:
            dfs(v, u)
    out_time[u] = timer  # Last time in subtree
```

- Visit each node exactly once
- Assign in_time and out_time: O(1) per node
- Total: O(N)

**Initialize Fenwick: O(N log N)**

```python
for i in range(1, n+1):
    update(in_time[i], values[i])      # O(log N)
    update(in_time[i]+1, -values[i])   # O(log N)
```

- N nodes × 2 updates × O(log N) each
- Total: O(N log N)

### Why O(log N) Per Operation?

**Fenwick Tree Structure:**

- Binary indexed tree with N positions
- Update propagates up: O(log N) positions
- Query accumulates down: O(log N) positions

**Range Update via Difference Array:**

```
To add val to range [L, R]:
  update(L, +val)      # Start of range
  update(R+1, -val)    # End of range

To query value at position i:
  return prefix_sum(i)  # Sum of all deltas up to i
```

**Subtree Update:**

```python
# Add val to all nodes in subtree of u
update(in_time[u], val)         # O(log N)
update(out_time[u] + 1, -val)   # O(log N)
# Now query(in_time[v]) gives updated value for any v in subtree(u)
```

**Why Subtree is Contiguous Range:**

- Euler tour assigns consecutive times to subtree nodes
- in_time[u] = first time entering subtree
- out_time[u] = last time in subtree
- Any node v in subtree(u): in_time[u] ≤ in_time[v] ≤ out_time[u]

**For N = 200K, Q = 200K:**

- Preprocessing: ~3.6M operations
- Updates/Queries: ~200K × 18 = ~3.6M operations
- Total: ~7.2M operations
- Naive (BFS per query): ~40B operations

---

## 💡 Key Takeaways

1. **Euler tour linearizes tree**: Subtrees become contiguous ranges
2. **Difference array trick**: Range add in O(log N) with two point updates
3. **Point query = prefix sum**: Value at i is sum of all deltas up to i
4. **Fenwick vs Segment Tree**: Fenwick is simpler for this use case
5. **Initialize carefully**: Initial values need their own updates
