---
problem_id: GRP_ROBOTICS_BRIDGES__4172
display_id: GRP-013
slug: robotics-bridges
title: "Robotics Bridges"
difficulty: Medium
difficulty_score: 60
topics:
  - Graph Theory
  - Bridges
  - Tarjan's Algorithm
  - DFS
tags:
  - graph
  - bridges
  - tarjan
  - dfs
  - critical-edges
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-013: Robotics Bridges

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1), find all bridges in the graph.

A **bridge** (or cut edge) is an edge whose removal increases the number of connected components. In other words, removing a bridge disconnects the graph (or a component).

Return a list of all bridges as pairs of nodes.

![Problem Illustration](../images/GRP-013/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- First line: integer `k` (number of bridges)
- Next `k` lines: two integers `u v` representing a bridge edge (output each bridge in sorted order: smaller node first)
- Sort bridges lexicographically

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
5
0 1
1 2
2 0
1 3
3 4
```

**Output:**

```
2
1 3
3 4
```

**Explanation:**

Graph structure:

- Nodes {0, 1, 2} form a cycle (triangle)
- Node 3 is connected to node 1
- Node 4 is connected to node 3

Bridges:

- Edge (1, 3): Removing it disconnects the triangle {0,1,2} from nodes {3,4}
- Edge (3, 4): Removing it disconnects node 4 from the rest

Edges (0,1), (1,2), (2,0) are NOT bridges because they're part of a cycle.

![Example Visualization](../images/GRP-013/example-1.png)

## Notes

- Use Tarjan's algorithm for finding bridges
- Maintain discovery time and low-link values for each node during DFS
- An edge (u, v) is a bridge if: `low[v] > discovery[u]` (where v is a child of u in DFS tree)
- Low-link value: minimum discovery time reachable from the subtree rooted at that node
- Time complexity: O(n + m)
- Space complexity: O(n)

## Related Topics

Bridges, Tarjan's Algorithm, DFS, Cut Edges, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<int[]> findBridges(int n, List<List<Integer>> adj) {
        // Implement here
        return new ArrayList<>();
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
        List<int[]> result = sol.findBridges(n, adj);

        // Sort each bridge pair and then the list lexicographically
        for (int[] bridge : result) Arrays.sort(bridge);
        result.sort((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);

        PrintWriter out = new PrintWriter(System.out);
        out.println(result.size());
        for (int[] bridge : result) {
            out.println(bridge[0] + " " + bridge[1]);
        }
        out.flush();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

class Solution:
    def find_bridges(self, n, adj):
        # Implement here
        return []

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
    result = sol.find_bridges(n, adj)

    # Sort each bridge pair and list
    sorted_bridges = []
    for u, v in result:
        sorted_bridges.append(sorted([u, v]))
    sorted_bridges.sort()

    print(len(sorted_bridges))
    for u, v in sorted_bridges:
        print(f"{u} {v}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<pair<int, int>> findBridges(int n, vector<vector<int>>& adj) {
        // Implement here
        return {};
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
    vector<pair<int, int>> result = sol.findBridges(n, adj);

    for (auto& p : result) {
        if (p.first > p.second) swap(p.first, p.second);
    }
    sort(result.begin(), result.end());

    cout << result.size() << endl;
    for (const auto& p : result) {
        cout << p.first << " " << p.second << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findBridges(n, adj) {
    // Implement here
    return [];
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
  const result = sol.findBridges(n, adj);

  const sortedBridges = result.map((b) => b.sort((x, y) => x - y));
  sortedBridges.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

  console.log(sortedBridges.length);
  sortedBridges.forEach((b) => console.log(`${b[0]} ${b[1]}`));
}

solve();
```
