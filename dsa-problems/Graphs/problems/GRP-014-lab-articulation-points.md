---
problem_id: GRP_LAB_ARTICULATION_POINTS__5694
display_id: GRP-014
slug: lab-articulation-points
title: "Lab Articulation Points"
difficulty: Medium
difficulty_score: 60
topics:
  - Graph Theory
  - Articulation Points
  - Tarjan's Algorithm
  - DFS
tags:
  - graph
  - articulation-points
  - tarjan
  - dfs
  - cut-vertices
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-014: Lab Articulation Points

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1), find all articulation points (also called cut vertices) in the graph.

An **articulation point** is a node whose removal increases the number of connected components. In other words, removing an articulation point disconnects the graph (or a component).

Return a list of all articulation points in sorted order.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_014.jpg)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- First line: integer `k` (number of articulation points)
- Second line: `k` space-separated integers representing articulation points in sorted order

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
```

**Explanation:**

Graph structure:

- Nodes {0, 1, 2} form a cycle (triangle)
- Node 3 is connected to node 1
- Node 4 is connected to node 3

Articulation points:

- Node 1: Removing it disconnects the triangle {0,2} from nodes {3,4}
- Node 3: Removing it disconnects node 4 from the rest of the graph

Nodes 0, 2, and 4 are NOT articulation points:

- Removing 0: Nodes still connected via 1-2 path
- Removing 2: Nodes still connected via 0-1 path
- Removing 4: Only isolates itself, doesn't increase components

![Example Visualization](../images/GRP-014/example-1.png)

## Notes

- Use Tarjan's algorithm for finding articulation points
- Maintain discovery time and low-link values for each node during DFS
- A node `u` is an articulation point if:
  - **Root case**: u is the DFS root and has 2+ children in DFS tree
  - **Non-root case**: u has a child `v` where `low[v] >= discovery[u]`
- Low-link value: minimum discovery time reachable from the subtree rooted at that node
- Time complexity: O(n + m)
- Space complexity: O(n)

## Related Topics

Articulation Points, Cut Vertices, Tarjan's Algorithm, DFS, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> findArticulationPoints(int n, List<List<Integer>> adj) {
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
        List<Integer> result = sol.findArticulationPoints(n, adj);
        Collections.sort(result);

        PrintWriter out = new PrintWriter(System.out);
        out.println(result.size());
        for (int i = 0; i < result.size(); i++) {
            out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        out.println();
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
    def find_articulation_points(self, n, adj):
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
    result = sol.find_articulation_points(n, adj)
    result.sort()

    print(len(result))
    print(*(result))

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
    vector<int> findArticulationPoints(int n, vector<vector<int>>& adj) {
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
    vector<int> result = sol.findArticulationPoints(n, adj);
    sort(result.begin(), result.end());

    cout << result.size() << endl;
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
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
  findArticulationPoints(n, adj) {
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
  const result = sol.findArticulationPoints(n, adj);
  result.sort((a, b) => a - b);

  console.log(result.length);
  console.log(result.join(" "));
}

solve();
```
