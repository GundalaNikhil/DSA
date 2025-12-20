---
title: "DP on Tree for Maximum Matching - Editorial"
problem_id: TDP_TREE_MAX_MATCHING__6183
difficulty: Medium
tags: [tree-dp, matching, graph-theory]
editorial_categories: [Tree DP, Matching]
slug: tree-max-matching
---

## 📝 Problem Summary

Find the maximum matching in a tree. A matching is a set of edges where no two edges share a vertex. Return the maximum number of edges in such a matching.

---

## 🌍 Real-World Scenario

**Pairing Employees:** In an organization hierarchy (tree), pair managers with direct reports for mentorship. Each person can be in at most one pair. Maximize the number of mentor-mentee pairs.

---

## 🔍 Approach: Tree DP with Matched/Unmatched States

### Key Insight

For each node u, track two states:

- `dp[u][0]` = max matching in subtree(u) when u is **unmatched** (not paired with any child)
- `dp[u][1]` = max matching in subtree(u) when u is **matched** (paired with exactly one child)

### Visual Example

```
Tree:
    1
   /|\
  2 3 4
  |
  5

Matching edges: (1,2), (3), (4), (5) - but only edges count
Best matching: {(1,2)} or {(1,3)} or {(1,4)} or {(2,5)}

**DP Trace from Leaves:**
- dp[5] = [0,0], dp[3] = [0,0], dp[4] = [0,0]  (leaves)
- dp[2][0] = max(dp[5][0], dp[5][1]) = 0
- dp[2][1] = 1 + dp[5][0] = 1  (match 2-5)
- dp[1][0] = sum of max(dp[c][0], dp[c][1]) for c in {2,3,4}
           = max(0,1) + max(0,0) + max(0,0) = 1
- dp[1][1] = try matching with each child:
           = max(1 + dp[2][0] + 0 + 0,   // match 1-2
                 1 + dp[3][0] + 1 + 0,   // match 1-3
                 1 + dp[4][0] + 1 + 0)   // match 1-4
           = max(1, 2, 2) = 2

Answer: max(dp[1][0], dp[1][1]) = max(1, 2) = 2
Matching: {(1,3), (2,5)} or {(1,4), (2,5)}
```

### Recurrence

```
dp[u][0] = sum of max(dp[v][0], dp[v][1]) for all children v

dp[u][1] = max over all children v of:
           1 + dp[v][0] + (sum - max(dp[v][0], dp[v][1]))
           ^   ^^^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           |   must be    other children can be matched
           |   unmatched  or not (take best)
           edge (u,v)
```

---

## 🧪 Edge Cases

| Case           | Input                  | Expected | Explanation            |
| -------------- | ---------------------- | -------- | ---------------------- |
| Single node    | n=1                    | 0        | No edges to match      |
| Two nodes      | 1-2                    | 1        | Match edge (1,2)       |
| Star graph     | 1 connected to 2,3,4,5 | 1        | Only one edge possible |
| Linear chain n | 1-2-3-...-n            | ⌊n/2⌋    | Alternate edges        |

---

## 💻 Implementation

### Java

```java
import java.util.*;
public class TreeMaxMatching {
    static List<Integer>[] adj;
    static int[][] dp;
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v); adj[v].add(u);
        }

        dp = new int[n + 1][2];
        dfs(1, 0);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }

    static void dfs(int u, int p) {
        dp[u][0] = 0;
        dp[u][1] = 0;
        int sum = 0;

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs(v, u);
            sum += Math.max(dp[v][0], dp[v][1]);
        }

        dp[u][0] = sum;

        for (int v : adj[u]) {
            if (v == p) continue;
            dp[u][1] = Math.max(dp[u][1], 1 + dp[v][0] + sum - Math.max(dp[v][0], dp[v][1]));
        }
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

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        adj[u].append(v); adj[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]

    def dfs(u, p):
        dp[u][0] = 0
        dp[u][1] = 0
        total = 0

        for v in adj[u]:
            if v == p: continue
            dfs(v, u)
            total += max(dp[v][0], dp[v][1])

        dp[u][0] = total

        for v in adj[u]:
            if v == p: continue
            dp[u][1] = max(dp[u][1], 1 + dp[v][0] + total - max(dp[v][0], dp[v][1]))

    dfs(1, 0)
    print(max(dp[1][0], dp[1][1]))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;
vector<array<int, 2>> dp;

void dfs(int u, int p) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    int sum = 0;

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        sum += max(dp[v][0], dp[v][1]);
    }

    dp[u][0] = sum;

    for (int v : adj[u]) {
        if (v == p) continue;
        dp[u][1] = max(dp[u][1], 1 + dp[v][0] + sum - max(dp[v][0], dp[v][1]));
    }
}

int main() {
    cin >> n;
    adj.resize(n + 1);
    dp.resize(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    dfs(1, 0);
    cout << max(dp[1][0], dp[1][1]) << "\n";
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

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const dp = Array.from({ length: n + 1 }, () => [0, 0]);

  function dfs(u, p) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    let sum = 0;

    for (const v of adj[u]) {
      if (v === p) continue;
      dfs(v, u);
      sum += Math.max(dp[v][0], dp[v][1]);
    }

    dp[u][0] = sum;

    for (const v of adj[u]) {
      if (v === p) continue;
      dp[u][1] = Math.max(
        dp[u][1],
        1 + dp[v][0] + sum - Math.max(dp[v][0], dp[v][1])
      );
    }
  }

  dfs(1, 0);
  console.log(Math.max(dp[1][0], dp[1][1]));
});
```

---

## 🧪 Walkthrough: Sample Testcase

### Input

```
6
1 2
1 3
2 4
2 5
3 6
```

### Visual Representation

```
Tree:
      1
     / \
    2   3
   / \   \
  4   5   6

Edges: (1,2), (1,3), (2,4), (2,5), (3,6)
```

### DP Walkthrough (post-order)

| Node | Children | sum=Σmax(dp[c])     | dp[0] | dp[1]                       | Best child match     |
| ---- | -------- | ------------------- | ----- | --------------------------- | -------------------- |
| 4    | none     | 0                   | 0     | 0                           | -                    |
| 5    | none     | 0                   | 0     | 0                           | -                    |
| 6    | none     | 0                   | 0     | 0                           | -                    |
| 2    | 4,5      | max(0,0)+max(0,0)=0 | 0     | 1+0+0-0=**1**               | match (2,4) or (2,5) |
| 3    | 6        | max(0,0)=0          | 0     | 1+0+0-0=**1**               | match (3,6)          |
| 1    | 2,3      | max(0,1)+max(0,1)=2 | 2     | max(1+0+2-1, 1+0+2-1)=**2** | match (1,2) or (1,3) |

**Answer: max(dp[1][0], dp[1][1]) = max(2, 2) = 2**

Optimal matching: {(2,4), (3,6)} or {(2,5), (3,6)} or {(1,2), (3,6)} etc.

**Output:** `2`

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake               | ❌ Wrong                       | ✅ Correct                                        |
| --- | --------------------- | ------------------------------ | ------------------------------------------------- |
| 1   | **Forget edge count** | `dp[u][1] = dp[v][0] + ...`    | `dp[u][1] = 1 + dp[v][0] + ...` (count the edge!) |
| 2   | **Use wrong sum**     | Recalculate sum for each child | Precompute sum, subtract current child            |
| 3   | **Greedy matching**   | Match greedily from leaves     | DP ensures global optimum                         |
| 4   | **Leaf init**         | `dp[leaf][1] = 1`              | `dp[leaf][1] = 0` (no children to match with)     |

---

## ⏱️ Complexity Analysis

### Detailed Breakdown

| Phase              | Time        | Space    | Explanation           |
| ------------------ | ----------- | -------- | --------------------- |
| DFS traversal      | O(N)        | O(h)     | Visit each node once  |
| Per-node DP        | O(d)        | O(1)     | d = degree of node    |
| Sum over all nodes | O(Σ degree) | O(N)     | Total degree = 2(N-1) |
| **Total Time**     | **O(N)**    | **O(N)** | Linear in tree size   |

### Why O(N)?

**Work Per Node:**

- Each node visited exactly once via DFS
- Work per node: iterate over children
- For node u with degree d: O(d) work

**Total Work:**

- Sum of all degrees = 2 × (N-1) edges = O(N)
- Each edge contributes 2 to total degree sum
- Therefore: O(N) total work

**DP Recurrence Cost:**

```
dp[u][0] = sum(max(dp[v][0], dp[v][1])) for all children v
dp[u][1] = max over all children v of:
           1 + dp[v][0] + sum(max(dp[w][0], dp[w][1])) for w != v
```

- Computing dp[u][0]: O(d) where d = number of children
- Computing dp[u][1]: O(d²) naive, but can optimize to O(d)
- Using prefix/suffix sums: O(d) for dp[u][1]

**Optimization:**

- Precompute sum_best = Σ max(dp[child][0], dp[child][1])
- For each child v: contribution = 1 + dp[v][0] + (sum_best - max(dp[v][0], dp[v][1]))
- This is O(d) instead of O(d²)

**Comparison to Other Approaches:**

- Greedy matching: O(N) but incorrect
- All subsets: O(2^N) exponential
- DP on trees: O(N) and correct

**For N = 200K:**

- DP approach: ~400K operations
- Exponential: ~10^60K operations (impossible)

---

## 💡 Key Takeaways

1. **Two states per node**: matched vs unmatched captures all cases
2. **Greedy fails**: Can't just match greedily from leaves up
3. **Subtract and add back**: The formula `1 + dp[v][0] + sum - max(...)` efficiently computes contribution
4. **Similar to vertex cover**: Both use include/exclude DP on trees
