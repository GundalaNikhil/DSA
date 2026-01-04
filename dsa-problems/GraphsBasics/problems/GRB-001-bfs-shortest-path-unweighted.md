---
problem_id: GRB_BFS_SHORTEST_PATH_UNWEIGHTED__4821
display_id: GRB-001
slug: bfs-shortest-path-unweighted
title: "BFS Shortest Path in Unweighted Graph"
difficulty: Easy
difficulty_score: 25
topics:
  - Graphs
  - BFS
  - Shortest Path
tags:
  - graphs-basics
  - bfs
  - shortest-path
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-001: BFS Shortest Path in Unweighted Graph

## Problem Statement

You are given an undirected, unweighted graph with `n` nodes (numbered from `0` to `n-1`) and `m` edges. You need to find the shortest path distance from a source node `s` to all other nodes in the graph.

In an unweighted graph, each edge has the same weight (you can think of it as weight 1). The shortest path between two nodes is the path with the minimum number of edges.

If a node is not reachable from the source, its distance should be `-1`.

![Problem Illustration](../images/GRB-001/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `m`, and `s` — the number of nodes, number of edges, and source node.
- Next `m` lines: Two integers `u` and `v` representing an undirected edge between nodes `u` and `v`.

## Output Format

Print `n` space-separated integers representing the shortest distance from node `s` to nodes `0, 1, 2, ..., n-1`.

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= s < n`
- `0 <= u, v < n`
- No self-loops or multiple edges between the same pair of nodes

## Example

**Input:**

```
4 3 0
0 1
1 2
0 3
```

**Output:**

```
0 1 2 1
```

**Explanation:**

Starting from node 0:

- Distance to node 0 = 0 (itself)
- Distance to node 1 = 1 (direct edge: 0 → 1)
- Distance to node 2 = 2 (path: 0 → 1 → 2)
- Distance to node 3 = 1 (direct edge: 0 → 3)

![Example Visualization](../images/GRB-001/example-1.png)

## Notes

- The graph is undirected, so edge (u, v) means you can travel from u to v and from v to u.
- BFS (Breadth-First Search) naturally finds shortest paths in unweighted graphs.
- Make sure to handle disconnected components (nodes unreachable from source should have distance -1).

## Related Topics

Graphs, BFS, Queue, Shortest Path

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] bfsShortestPath(int n, int m, int s, List<List<Integer>> adj) {
        // Implement here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmsLine = br.readLine();
        if (nmsLine == null) return;
        String[] nms = nmsLine.trim().split("\\s+");
        int n = Integer.parseInt(nms[0]);
        int m = Integer.parseInt(nms[1]);
        int s = Integer.parseInt(nms[2]);

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
        int[] distances = sol.bfsShortestPath(n, m, s, adj);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < n; i++) {
            out.print(distances[i] + (i == n - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys
from collections import deque

class Solution:
    def bfs_shortest_path(self, n, m, s, adj):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])

    adj = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    sol = Solution()
    distances = sol.bfs_shortest_path(n, m, s, adj)
    print(*(distances))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> bfsShortestPath(int n, int m, int s, vector<vector<int>>& adj) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    Solution sol;
    vector<int> distances = sol.bfsShortestPath(n, m, s, adj);

    for (int i = 0; i < n; i++) {
        cout << distances[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  bfsShortestPath(n, m, s, adj) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const s = parseInt(input[idx++]);

  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const sol = new Solution();
  const distances = sol.bfsShortestPath(n, m, s, adj);
  console.log(distances.join(" "));
}

solve();
```
