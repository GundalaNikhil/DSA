---
problem_id: GRP_LAB_NETWORK_DFS__5729
display_id: GRP-002
slug: lab-network-dfs
title: "Lab Network DFS"
difficulty: Easy
difficulty_score: 25
topics:
  - Graph Traversal
  - Depth-First Search
  - Recursion
tags:
  - graph
  - dfs
  - traversal
  - recursion
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-002: Lab Network DFS

## Problem Statement

Given an undirected graph represented by `n` nodes (numbered from 0 to n-1) and an adjacency list, perform a Depth-First Search (DFS) in preorder starting from node 0 and return the visited nodes in the order they were first encountered.

DFS explores as far as possible along each branch before backtracking. The preorder means we record a node when we first visit it, not when we backtrack from it.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_002.jpg)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single line with space-separated integers representing the preorder DFS traversal starting from node 0

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- The graph may be disconnected
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
3
0 1
0 2
1 4
```

**Output:**

```
0 1 4 2
```

**Explanation:**

Starting from node 0:

- Visit node 0 (record it)
- Go to neighbor 1 (first neighbor in adjacency list)
- Visit node 1 (record it)
- Go to neighbor 4 (only unvisited neighbor of 1)
- Visit node 4 (record it)
- Backtrack to 1, then to 0
- Go to neighbor 2 (next unvisited neighbor of 0)
- Visit node 2 (record it)

The DFS preorder traversal is: 0 → 1 → 4 → 2

![Example Visualization](../images/GRP-002/example-1.png)

## Notes

- Can be implemented recursively (using call stack) or iteratively (using explicit stack)
- Use a visited array/set to track which nodes have been explored
- If the graph is disconnected, only nodes reachable from node 0 will be visited
- The order of neighbors in the adjacency list determines which branch to explore first
- Preorder means recording the node when first visited, not during backtracking

## Related Topics

Graph Traversal, DFS, Recursion, Stack, Backtracking

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> dfsPreorder(int n, List<List<Integer>> adj) {
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
        List<Integer> result = sol.dfsPreorder(n, adj);

        PrintWriter out = new PrintWriter(System.out);
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
    def dfs_preorder(self, n, adj):
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
    result = sol.dfs_preorder(n, adj)
    print(*(result))

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
    vector<int> dfsPreorder(int n, vector<vector<int>>& adj) {
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
    vector<int> result = sol.dfsPreorder(n, adj);

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
  dfsPreorder(n, adj) {
    // Implement here
    return [];
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
  const result = sol.dfsPreorder(n, adj);
  console.log(result.join(" "));
}

solve();
```
