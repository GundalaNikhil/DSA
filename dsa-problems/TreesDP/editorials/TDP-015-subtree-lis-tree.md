---
title: DP for Subtree LIS on Tree
problem_id: TDP_SUBTREE_LIS__7392
display_id: TDP-015
difficulty: Hard
tags:
- tree-dp
- lis
- coordinate-compression
- fenwick
editorial_categories:
- Tree DP
- LIS
slug: subtree-lis-tree
---
## 📝 Problem Summary

For each node v, compute the length of the Longest Increasing Subsequence (LIS) formed by values on the path from root to v.

---

## 🌍 Real-World Scenario

**Gene Expression Analysis:** In an evolutionary tree, each node (species) has a gene expression level. For each species, find the longest chain of increasing expression levels from the ancestral species - indicating gradual evolutionary adaptation.

---

## 🔍 Approach: DFS with TreeMap for LIS

### Key Insight

Maintain LIS state during DFS traversal. For each node:

1. Find LIS length ending at this node (using floor lookup)
2. Update LIS structure
3. Process children recursively
4. **Backtrack**: restore previous state after returning

### Visual Example

```
Tree with values:
      1 (val=5)
     / \
    2   3
  (val=3) (val=7)
   |
   4
(val=6)

Path to node 1: [5] → LIS = 1
Path to node 2: [5,3] → LIS = 1 (3 can't extend 5)
Path to node 4: [5,3,6] → LIS = 2 ([5,6] or [3,6])
Path to node 3: [5,7] → LIS = 2 ([5,7])

Output: [1, 1, 2, 2]
```

### Algorithm

```
TreeMap<value, lis_length> active;

dfs(u):
    prev = largest value ≤ values[u] in active
    lis[u] = (prev exists ? active[prev] : 0) + 1

    save old active[values[u]] if exists
    active[values[u]] = max(active[values[u]], lis[u])

    for each child v:
        dfs(v)

    restore active[values[u]] to saved state  // BACKTRACK
```

---

## 🧪 Edge Cases

| Case            | Input            | Expected    | Explanation                 |
| --------------- | ---------------- | ----------- | --------------------------- |
| Single node     | n=1, val=[5]     | [1]         | LIS of single element       |
| Decreasing path | vals=[5,4,3,2,1] | [1,1,1,1,1] | No element extends previous |
| Increasing path | vals=[1,2,3,4,5] | [1,2,3,4,5] | Each extends previous       |
| All same values | vals=[3,3,3,3]   | [1,1,1,1]   | Equal ≠ strictly increasing |

---

## 💻 Implementation

### Java

```java
import java.util.*;
public class SubtreeLIS {
    static List<Integer>[] adj;
    static int[] values, lis;
    static TreeMap<Integer, Integer> active;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        values = new int[n + 1];
        lis = new int[n + 1];

        for (int i = 1; i <= n; i++) values[i] = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        active = new TreeMap<>();
        dfs(1, 0);

        for (int i = 1; i <= n; i++) {
            System.out.print(lis[i] + (i < n ? " " : "\n"));
        }
    }

    static void dfs(int u, int p) {
        Integer prev = active.floorKey(values[u]);
        int prevLen = (prev == null) ? 0 : active.get(prev);
        lis[u] = prevLen + 1;

        Integer next = active.ceilingKey(values[u]);
        int savedLen = (next != null && next == values[u]) ? active.get(next) : -1;

        if (savedLen == -1 || lis[u] > savedLen) {
            active.put(values[u], lis[u]);
        }

        for (int v : adj[u]) {
            if (v != p) dfs(v, u);
        }

        if (savedLen == -1) {
            active.remove(values[u]);
        } else {
            active.put(values[u], savedLen);
        }
    }
}
```

### Python

```python
import sys
from bisect import bisect_left
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

    lis = [0] * (n + 1)
    active = []

    def dfs(u, p):
        pos = bisect_left(active, values[u])
        saved = active[pos] if pos < len(active) else None

        if pos < len(active):
            active[pos] = values[u]
        else:
            active.append(values[u])

        lis[u] = len(active)

        for v in adj[u]:
            if v != p: dfs(v, u)

        if saved is not None:
            active[pos] = saved
        else:
            active.pop()

    dfs(1, 0)
    print(' '.join(map(str, lis[1:])))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> values, lis_len;
vector<vector<int>> adj;
vector<int> active;

void dfs(int u, int p) {
    int pos = lower_bound(active.begin(), active.end(), values[u]) - active.begin();
    int saved = (pos < active.size()) ? active[pos] : -1;

    if (pos < active.size()) {
        active[pos] = values[u];
    } else {
        active.push_back(values[u]);
    }

    lis_len[u] = active.size();

    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }

    if (saved != -1) {
        active[pos] = saved;
    } else {
        active.pop_back();
    }
}

int main() {
    cin >> n;
    values.resize(n + 1);
    lis_len.resize(n + 1);
    adj.resize(n + 1);

    for (int i = 1; i <= n; i++) cin >> values[i];

    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    dfs(1, 0);

    for (int i = 1; i <= n; i++) {
        cout << lis_len[i] << (i < n ? " " : "\n");
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

  const lis = Array(n + 1).fill(0);
  const active = [];

  function binarySearch(arr, val) {
    let l = 0,
      r = arr.length;
    while (l < r) {
      const mid = Math.floor((l + r) / 2);
      if (arr[mid] < val) l = mid + 1;
      else r = mid;
    }
    return l;
  }

  function dfs(u, p) {
    const pos = binarySearch(active, values[u]);
    const saved = pos < active.length ? active[pos] : null;

    if (pos < active.length) {
      active[pos] = values[u];
    } else {
      active.push(values[u]);
    }

    lis[u] = active.length;

    for (const v of adj[u]) {
      if (v !== p) dfs(v, u);
    }

    if (saved !== null) {
      active[pos] = saved;
    } else {
      active.pop();
    }
  }

  dfs(1, 0);
  console.log(lis.slice(1).join(" "));
});
```

---

## 🧪 Test Case Walkthrough (Dry Run)

### Input

```
5
5 3 7 6 4
1 2
1 3
2 4
2 5
```

### Visual Representation

```
Tree with values:
       1 (v=5)
      / \
   2(v=3) 3(v=7)
   / \
4(v=6) 5(v=4)

Paths from root:
  To 1: [5]
  To 2: [5,3]
  To 3: [5,7]
  To 4: [5,3,6]
  To 5: [5,3,4]
```

### LIS Calculation per Node

| Node | Path Values | LIS | Best Subsequence |
| ---- | ----------- | --- | ---------------- |
| 1    | [5]         | 1   | [5]              |
| 2    | [5,3]       | 1   | [3] or [5]       |
| 3    | [5,7]       | 2   | [5,7]            |
| 4    | [5,3,6]     | 2   | [3,6] or [5,6]   |
| 5    | [5,3,4]     | 2   | [3,4]            |

**Output:** `1 1 2 2 2`

### DFS with Backtracking

| Step | Node | active[] | Action                     | lis[node] |
| ---- | ---- | -------- | -------------------------- | --------- |
| 1    | 1    | [5]      | Insert 5                   | 1         |
| 2    | 2    | [3]      | Replace 5 with 3 (smaller) | 1         |
| 3    | 4    | [3,6]    | Insert 6                   | 2         |
| 4    | -    | [3]      | Backtrack: remove 6        | -         |
| 5    | 5    | [3,4]    | Insert 4                   | 2         |
| 6    | -    | [3]      | Backtrack: remove 4        | -         |
| 7    | -    | [5]      | Backtrack: restore 5       | -         |
| 8    | 3    | [5,7]    | Insert 7                   | 2         |

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                | ❌ Wrong                    | ✅ Correct                 |
| --- | ---------------------- | --------------------------- | -------------------------- |
| 1   | **No backtracking**    | Modify active[] permanently | Restore after DFS returns  |
| 2   | **Use ceiling**        | Find ceil to extend         | Use floor (largest ≤ v)    |
| 3   | **Non-strict LIS**     | Allow equal values          | Strictly increasing only   |
| 4   | **Wrong save/restore** | Save position only          | Save value at position too |

### Detailed Example:

**Mistake 1: Forgetting to Backtrack**

```python
# ❌ Wrong: active[] state pollutes sibling subtrees
def dfs(u, p):
    pos = bisect_left(active, values[u])
    if pos < len(active):
        active[pos] = values[u]
    else:
        active.append(values[u])
    lis[u] = len(active)
    for v in adj[u]:
        if v != p:
            dfs(v, u)
    # NO BACKTRACKING - sibling sees wrong state!

# ✅ Correct: Restore state after recursive calls
def dfs(u, p):
    pos = bisect_left(active, values[u])
    saved = active[pos] if pos < len(active) else None
    if pos < len(active):
        active[pos] = values[u]
    else:
        active.append(values[u])
    lis[u] = len(active)
    for v in adj[u]:
        if v != p:
            dfs(v, u)
    # BACKTRACK
    if saved is not None:
        active[pos] = saved
    else:
        active.pop()
```

---

## ⏱️ Complexity

### Detailed Breakdown

| Phase                   | Time           | Space    | Explanation                 |
| ----------------------- | -------------- | -------- | --------------------------- |
| DFS traversal           | O(N)           | O(h)     | Visit each node once        |
| Per-node LIS operation  | O(log N)       | O(log N) | TreeMap/binary search       |
| Binary search (Python)  | O(log L)       | O(L)     | L = active array length ≤ N |
| TreeMap floorKey (Java) | O(log M)       | O(M)     | M = entries in map ≤ N      |
| Backtracking            | O(1) per node  | O(1)     | Restore single value        |
| **Total Time**          | **O(N log N)** | **O(N)** | N nodes × log N per node    |

### Why O(N log N)?

**Per-Node Processing:**

1. Find floor(value[u]) in active set: O(log N)
2. Insert or replace in active: O(log N) for TreeMap, O(N) worst for array shift
3. Backtrack after subtree: O(log N) for TreeMap, O(1) for array pop

**TreeMap (Java) Approach:**

```java
Integer floor = active.floorKey(values[u]);  // O(log N)
if (floor != null) {
    saved = active.get(floor);               // O(log N)
    active.remove(floor);                    // O(log N)
}
active.put(values[u], values[u]);            // O(log N)
// ... recurse ...
if (saved != null) {
    active.remove(values[u]);                // O(log N)
    active.put(floor, saved);                // O(log N)
}
```

- Each operation: O(log N) where N = size of TreeMap
- Total per node: O(log N)
- Total: O(N log N)

**Binary Search Array (Python) Approach:**

```python
pos = bisect_left(active, values[u])         # O(log L)
if pos < len(active):
    saved = active[pos]
    active[pos] = values[u]                  # O(1)
else:
    active.append(values[u])                 # O(1) amortized
# ... recurse ...
if saved is not None:
    active[pos] = saved                      # O(1)
else:
    active.pop()                             # O(1)
```

- Binary search: O(log L) where L ≤ N
- Array operations: O(1) amortized
- Total per node: O(log N)
- Total: O(N log N)

### Why TreeMap/Binary Search?

**LIS Problem:**

- Maintain array `active` where `active[i]` = smallest tail value for LIS of length i+1
- To extend LIS with value v: find largest value ≤ v (floor)
- Binary search or TreeMap.floorKey() provides O(log N) lookup

**Backtracking Requirement:**

- When leaving subtree, must restore parent's state
- Siblings see parent's original LIS, not modified by earlier siblings
- This ensures correct independent LIS calculation per root-to-node path

**For N = 200K:**

- O(N log N): ~3.6M operations
- Naive O(N²) (recompute LIS per node): ~40B operations

---

## 💡 Key Takeaways

1. **Backtracking is crucial**: Must restore state when leaving subtree
2. **LIS extension**: Find floor key to extend, not ceiling
3. **Strictly increasing**: Equal values don't extend LIS
4. **Two approaches**: TreeMap (Java) vs sorted array (Python/JS)


## Constraints

- 1 ≤ N ≤ 200,000
- 1 ≤ values[i] ≤ 10^9