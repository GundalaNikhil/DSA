---
problem_id: GRP_CAMPUS_CARPOOL_PAIRING__2914
display_id: GRP-016
slug: campus-carpool-pairing
title: "Campus Carpool Pairing"
difficulty: Medium
difficulty_score: 45
topics:
  - Graph Theory
  - Cycle Detection
  - Union-Find
  - Forest
tags:
  - graph
  - cycle-detection
  - union-find
  - forest
  - tree
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-016: Campus Carpool Pairing

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1) and `m` edges, determine if the graph is a **forest**.

A **forest** is a graph with no cycles. Equivalently, it's a collection of trees where each tree is a connected acyclic graph. An isolated node (with no edges) is considered a tree of size 1.

Return `true` if the graph is a forest (has no cycles), `false` otherwise.

![Problem Illustration](../images/GRP-016/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single word: `true` if the graph is a forest (no cycles), `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
3
2
0 1
1 2
```

**Output:**

```
true
```

**Explanation:**

Graph structure:

```
0 --- 1 --- 2
```

This is a simple path (a tree) with no cycles, so it's a forest.

Output: `true`

![Example Visualization](../images/GRP-016/example-1.png)

## Notes

- A forest has no cycles
- For a graph to be a forest, it must satisfy: `m < n` (number of edges < number of nodes)
- If `m >= n`, at least one cycle must exist (pigeonhole principle)
- Use Union-Find (DSU) to detect cycles:
  - Process each edge (u, v)
  - If u and v are already in the same component, adding this edge creates a cycle
  - If they're in different components, union them
- Alternatively, use DFS with parent tracking (same as undirected cycle detection)
- Time complexity: O(m × α(n)) for Union-Find, O(n + m) for DFS

## Related Topics

Forest, Trees, Cycle Detection, Union-Find, DFS, Acyclic Graph

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean isForest(int n, List<List<Integer>> adj) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edge = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edge[0]);
            int v = Integer.parseInt(edge[1]);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution sol = new Solution();
        System.out.println(sol.isForest(n, adj));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

class Solution:
    def is_forest(self, n, adj):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    sol = Solution()
    print("true" if sol.is_forest(n, adj) else "false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool isForest(int n, vector<vector<int>>& adj) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    Solution sol;
    if (sol.isForest(n, adj)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  isForest(n, adj) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const sol = new Solution();
  console.log(sol.isForest(n, adj).toString());
}

solve();
```
