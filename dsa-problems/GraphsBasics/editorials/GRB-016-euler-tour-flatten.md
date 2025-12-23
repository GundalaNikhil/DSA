---
problem_id: GRB_EULER_TOUR_FLATTEN__5068
display_id: GRB-016
slug: euler-tour-flatten
title: "Euler Tour of Tree (Array Flatten)"
difficulty: Medium
difficulty_score: 44
topics:
  - Graphs
  - Trees
  - DFS
  - Euler Tour
tags:
  - graphs-basics
  - euler-tour
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# GRB-016: Euler Tour of Tree (Array Flatten)

## 📋 Problem Summary

Given a rooted tree, perform a DFS traversal (Euler Tour) to compute two values for each node `u`:
1.  `tin[u]`: Entry time (when DFS first visits `u`).
2.  `tout[u]`: Exit time (when DFS finishes `u`'s subtree).

This "flattens" the tree into an array such that the subtree of `u` corresponds exactly to the range `[tin[u], tout[u]]`.

## 🌍 Real-World Scenario

**Scenario Title:** Organizational Hierarchy Management

Imagine a large corporation with a CEO (root) and a hierarchy of employees.
-   **Query:** "List all subordinates of Manager X."
-   **Naive:** Traverse the tree starting from X. Slow if done repeatedly.
-   **Euler Tour:** Assign each employee an ID range based on when they joined the meeting (DFS order).
    -   Manager X has range `[100, 150]`.
    -   Any employee with an ID between 100 and 150 is a subordinate of X.
    -   Checking "Is Y a subordinate of X?" becomes `tin[X] <= tin[Y] && tout[Y] <= tout[X]`. O(1) check!

![Real-World Application](../images/GRB-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      0
     / \
    1   2
       / \
      3   4
```
**DFS Traversal:**
1.  **Enter 0:** `tin[0] = 0`. Timer = 1.
2.  **Enter 1:** `tin[1] = 1`. Timer = 2.
3.  **Exit 1:** `tout[1] = 1`.
4.  **Enter 2:** `tin[2] = 2`. Timer = 3.
5.  **Enter 3:** `tin[3] = 3`. Timer = 4.
6.  **Exit 3:** `tout[3] = 3`.
7.  **Enter 4:** `tin[4] = 4`. Timer = 5.
8.  **Exit 4:** `tout[4] = 4`.
9.  **Exit 2:** `tout[2] = 4`.
10. **Exit 0:** `tout[0] = 4`.

**Result:**
-   `tin`: `[0, 1, 2, 3, 4]`
-   `tout`: `[4, 1, 4, 3, 4]`

**Subtree of 2:** Range `[2, 4]`. Nodes with `tin` in this range are `{2, 3, 4}`. Correct.

### Algorithm Steps

1.  **Initialize:** Global `timer = 0`. `tin` and `tout` arrays.
2.  **DFS(u, p):**
    -   `tin[u] = timer++`.
    -   For each child `v` of `u`:
        -   If `v != p`, call `DFS(v, u)`.
    -   `tout[u] = timer - 1` (or `timer` depending on convention; problem implies inclusive range of *entry times*).
    -   `tout[u]` is the value of `timer` *after* processing all children, minus 1. Or simply, `tout[u]` is the `tin` of the last node visited in `u`'s subtree.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Timer:** Starts at 0.
-   **Tout Definition:** `tout[u]` should be the maximum `tin` value in the subtree of `u`.
-   **Root:** Given in input.

## Naive Approach

### Intuition

Just standard DFS. There isn't really a "naive" way other than BFS, which doesn't give the subtree property.

## Optimal Approach (DFS)

Standard DFS traversal.

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(N)**: Recursion stack and arrays.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int timer;
    private int[] tin;
    private int[] tout;

    public int[][] eulerTour(int n, List<List<Integer>> adj, int root) {
        tin = new int[n];
        tout = new int[n];
        timer = 0;
        
        dfs(root, -1, adj);
        
        return new int[][]{tin, tout};
    }

    private void dfs(int u, int p, List<List<Integer>> adj) {
        tin[u] = timer++;
        
        for (int v : adj.get(u)) {
            if (v != p) {
                dfs(v, u, adj);
            }
        }
        
        // tout[u] is the max tin in the subtree.
        // Since timer increments monotonically, the current (timer-1) is the max tin seen so far.
        tout[u] = timer - 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        int root = sc.nextInt();

        Solution solution = new Solution();
        int[][] res = solution.eulerTour(n, adj, root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(res[0][i]);
        }
        sb.append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(res[1][i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def euler_tour(n: int, adj: list[list[int]], root: int):
    tin = [0] * n
    tout = [0] * n
    timer = 0
    
    def dfs(u, p):
        nonlocal timer
        tin[u] = timer
        timer += 1
        
        for v in adj[u]:
            if v != p:
                dfs(v, u)
                
        tout[u] = timer - 1
        
    dfs(root, -1)
    return tin, tout

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        root = int(next(iterator))
        
        tin, tout = euler_tour(n, adj, root)
        print(" ".join(map(str, tin)))
        print(" ".join(map(str, tout)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, tout;

    void dfs(int u, int p, const vector<vector<int>>& adj) {
        tin[u] = timer++;
        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u, adj);
            }
        }
        tout[u] = timer - 1;
    }

public:
    pair<vector<int>, vector<int>> eulerTour(int n, const vector<vector<int>>& adj, int root) {
        tin.assign(n, 0);
        tout.assign(n, 0);
        timer = 0;
        dfs(root, -1, adj);
        return {tin, tout};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int root;
    cin >> root;

    Solution solution;
    auto res = solution.eulerTour(n, adj, root);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << res.first[i];
    }
    cout << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << res.second[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  eulerTour(n, adj, root) {
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);
    let timer = 0;

    // Iterative DFS to avoid stack overflow
    // We need to simulate the post-order processing to set tout
    const stack = [root];
    const parent = new Int32Array(n).fill(-1);
    
    // Iterative DFS to avoid stack overflow for large N
    
    const stackIter = [root];
    const parentMap = new Int32Array(n).fill(-1);
    const childIndex = new Int32Array(n).fill(0); // Index of next child to visit
    
    tin[root] = timer++;
    
    while (stackIter.length > 0) {
        const u = stackIter[stackIter.length - 1];
        const p = parentMap[u];
        const children = adj[u];
        
        let pushedChild = false;
        
        // Find next valid child
        while (childIndex[u] < children.length) {
            const v = children[childIndex[u]];
            childIndex[u]++;
            if (v !== p) {
                parentMap[v] = u;
                tin[v] = timer++;
                stackIter.push(v);
                pushedChild = true;
                break; // Process this child
            }
        }
        
        if (!pushedChild) {
            // All children done, post-order for u
            tout[u] = timer - 1;
            stackIter.pop();
        }
    }

    return [tin, tout];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
    adj[v].push(u);
  }
  const root = parseInt(data[idx++], 10);

  const solution = new Solution();
  const res = solution.eulerTour(n, adj, root);
  console.log(res[0].join(" "));
  console.log(res[1].join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
0 1
0 2
0
```
**Tree:** `1-0-2`. Root 0.

**Iterative DFS:**
1.  Push 0. `tin[0]=0`. Timer=1.
2.  **Node 0:** Child 1. Push 1. `tin[1]=1`. Timer=2.
3.  **Node 1:** No children (except parent 0). Pop 1. `tout[1]=1`.
4.  **Node 0:** Child 2. Push 2. `tin[2]=2`. Timer=3.
5.  **Node 2:** No children. Pop 2. `tout[2]=2`.
6.  **Node 0:** No more children. Pop 0. `tout[0]=2`.

**Result:**
`tin`: `0 1 2`
`tout`: `2 1 2`
Matches example.

## ✅ Proof of Correctness

The DFS traversal visits every node in the subtree of `u` exactly between the time it enters `u` and the time it leaves `u`. Thus, the set of nodes in `u`'s subtree is exactly `{v | tin[u] <= tin[v] <= tout[u]}`.

## 💡 Interview Extensions (High-Value Add-ons)

-   **LCA:** `u` is an ancestor of `v` iff `tin[u] <= tin[v]` and `tout[u] >= tout[v]`. This allows O(1) ancestor checks.
-   **Subtree Queries:** Flattening the tree allows using Segment Trees or Fenwick Trees on the array to answer subtree queries (e.g., sum of values in subtree).
-   **Heavy-Light Decomposition:** Uses a similar flattening idea but prioritizes "heavy" edges to optimize path queries.

### Common Mistakes to Avoid

1.  **Timer Increment:** Ensure timer increments *only* on entry (pre-order).
2.  **Tout Value:** `tout[u]` is the *last* `tin` value in the subtree, not the time when we *leave* `u` (which would be `2*N` in a full Euler tour). This problem specifically asks for the "Array Flattening" variant where range size = subtree size.
3.  **Stack Overflow:** In Python/JS, deep trees cause recursion errors. Use `sys.setrecursionlimit` or iterative DFS.
