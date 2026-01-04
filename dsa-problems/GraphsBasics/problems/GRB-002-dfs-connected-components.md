---
problem_id: GRB_DFS_CONNECTED_COMPONENTS__5190
display_id: GRB-002
slug: dfs-connected-components
title: "DFS Connected Components"
difficulty: Easy
difficulty_score: 28
topics:
  - Graphs
  - DFS
  - Components
tags:
  - graphs-basics
  - dfs
  - components
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-002: DFS Connected Components

## Problem Statement

You are given an undirected graph with `n` nodes (0 to `n-1`) and `m` edges. Count the number of connected components and label each node with its component id.

Use depth-first search (DFS) to explore the graph.

![Problem Illustration](../images/GRB-002/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m`
- Next `m` lines: two integers `u` and `v` describing an undirected edge

## Output Format

- Line 1: integer `c`, the number of connected components
- Line 2: `n` integers, `comp[i]` is the component id (1-based) for node `i`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 2
0 1
2 3
```

**Output:**

```
2
1 1 2 2
```

**Explanation:**

Nodes `{0,1}` form component 1 and nodes `{2,3}` form component 2.

![Example Visualization](../images/GRB-002/example-1.png)

## Notes

- Components are numbered in the order they are discovered by DFS.
- If `m=0`, each node is its own component.
- An isolated node forms a component of size 1.

## Related Topics

Graph Traversal, DFS, Connected Components

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countComponents(int n, int m, List<List<Integer>> adj, int[] componentIds) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmLine = br.readLine();
        if (nmLine == null) return;
        String[] nm = nmLine.trim().split("\\s+");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edge = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edge[0]);
            int v = Integer.parseInt(edge[1]);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] componentIds = new int[n];
        Solution sol = new Solution();
        int count = sol.countComponents(n, m, adj, componentIds);

        PrintWriter out = new PrintWriter(System.out);
        out.println(count);
        for (int i = 0; i < n; i++) {
            out.print(componentIds[i] + (i == n - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DFS trees
sys.setrecursionlimit(200000)

class Solution:
    def count_components(self, n, m, adj, component_ids):
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

    component_ids = [0] * n
    sol = Solution()
    count = sol.count_components(n, m, adj, component_ids)

    print(count)
    print(*(component_ids))

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
    int countComponents(int n, int m, vector<vector<int>>& adj, vector<int>& componentIds) {
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

    vector<int> componentIds(n);
    Solution sol;
    int count = sol.countComponents(n, m, adj, componentIds);

    cout << count << endl;
    for (int i = 0; i < n; i++) {
        cout << componentIds[i] << (i == n - 1 ? "" : " ");
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
  countComponents(n, m, adj, componentIds) {
    // Implement here
    return 0;
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
    if (idx >= input.length) break;
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  const componentIds = new Array(n).fill(0);
  const sol = new Solution();
  const count = sol.countComponents(n, m, adj, componentIds);

  console.log(count);
  console.log(componentIds.join(" "));
}

solve();
```
