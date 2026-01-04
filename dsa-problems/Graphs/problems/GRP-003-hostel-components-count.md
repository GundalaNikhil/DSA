---
problem_id: GRP_HOSTEL_COMPONENTS_COUNT__3184
display_id: GRP-003
slug: hostel-components-count
title: "Hostel Components Count"
difficulty: Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - Connected Components
  - Union-Find
tags:
  - graph
  - connected-components
  - bfs
  - dfs
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-003: Hostel Components Count

## Problem Statement

Given an undirected graph with `n` nodes (numbered from 0 to n-1) and an adjacency list, count the number of connected components in the graph.

A connected component is a maximal set of nodes where every pair of nodes is connected by a path. Two nodes are in the same component if and only if there exists a path between them.

![Problem Illustration](../images/GRP-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single integer representing the number of connected components

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
2
0 1
2 3
```

**Output:**

```
3
```

**Explanation:**

The graph has 5 nodes and 2 edges:

- Component 1: {0, 1} - connected by edge (0,1)
- Component 2: {2, 3} - connected by edge (2,3)
- Component 3: {4} - isolated node

Total: 3 connected components

![Example Visualization](../images/GRP-003/example-1.png)

## Notes

- A single isolated node (with no edges) forms its own connected component
- Can be solved using BFS, DFS, or Union-Find (Disjoint Set Union)
- Iterate through all nodes; for each unvisited node, start a BFS/DFS to mark all reachable nodes
- Each time you start a new BFS/DFS, increment the component count
- Time complexity: O(n + m) for BFS/DFS approach

## Related Topics

Connected Components, Graph Traversal, BFS, DFS, Union-Find, Disjoint Set Union

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countComponents(int n, List<List<Integer>> adj) {
        // Implement here
        return 0;
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
        System.out.println(sol.countComponents(n, adj));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

class Solution:
    def count_components(self, n, adj):
        # Implement here
        return 0

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
    print(sol.count_components(n, adj))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& adj) {
        // Implement here
        return 0;
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
    cout << sol.countComponents(n, adj) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countComponents(n, adj) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

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
  console.log(sol.countComponents(n, adj));
}

solve();
```
