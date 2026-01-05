---
problem_id: GRB_ARTICULATION_POINTS_COLORED__1685
display_id: GRB-010
slug: articulation-points-colored
title: "Articulation Points Under Edge Colors"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - DFS
  - Articulation Points
tags:
  - graphs-basics
  - articulation-points
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-010: Articulation Points Under Edge Colors

## Problem Statement

You are given an undirected graph where each edge is colored `R` (red) or `B` (blue). A node is **critical** if removing it disconnects the graph into components such that at least one component contains a red edge and at least one (different) component contains a blue edge.

Return all critical nodes in increasing order.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graph_basics/GRB-010.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v c` describing an undirected edge with color `c` (`R` or `B`)

## Output Format

- Line 1: integer `k`, number of critical nodes
- Line 2: `k` integers, the critical node indices in increasing order (or empty line if `k=0`)

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
- `c` is `R` or `B`

## Example

**Input:**

```
5 4
0 2 R
3 4 B
1 0 R
1 3 B
```

**Output:**

```
1
1
```

**Explanation:**

Removing node `1` splits the graph into a red-edge component `{0,2}` and a blue-edge component `{3,4}`.

![Example Visualization](../images/GRB-010/example-1.png)

## Notes

- Use DFS low-link to identify articulation points.
- Track whether each subtree contains red/blue edges to detect color separation.
- A node can be an articulation point without being critical under color rules.

## Related Topics

Articulation Points, DFS, Graph Coloring

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> findCriticalNodes(int n, int m, List<List<Edge>> adj) {
        // Implement here
        return new ArrayList<>();
    }

    static class Edge {
        int to;
        char color;
        Edge(int to, char color) {
            this.to = to;
            this.color = color;
        }
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

        List<List<Solution.Edge>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(line[0]);
            int v = Integer.parseInt(line[1]);
            char c = line[2].charAt(0);
            adj.get(u).add(new Solution.Edge(v, c));
            adj.get(v).add(new Solution.Edge(u, c));
        }

        Solution sol = new Solution();
        List<Integer> critical = sol.findCriticalNodes(n, m, adj);

        PrintWriter out = new PrintWriter(System.out);
        out.println(critical.size());
        for (int i = 0; i < critical.size(); i++) {
            out.print(critical.get(i) + (i == critical.size() - 1 ? "" : " "));
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
    def find_critical_nodes(self, n, m, adj):
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
        c = input_data[idx+2]
        adj[u].append((v, c))
        adj[v].append((u, c))
        idx += 3

    sol = Solution()
    critical = sol.find_critical_nodes(n, m, adj)

    print(len(critical))
    print(*(critical))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    char color;
};

class Solution {
public:
    vector<int> findCriticalNodes(int n, int m, vector<vector<Edge>>& adj) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        char c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    Solution sol;
    vector<int> critical = sol.findCriticalNodes(n, m, adj);

    cout << critical.size() << endl;
    for (int i = 0; i < critical.size(); i++) {
        cout << critical[i] << (i == critical.size() - 1 ? "" : " ");
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
  findCriticalNodes(n, m, adj) {
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
    const c = input[idx++];
    adj[u].push([v, c]);
    adj[v].push([u, c]);
  }

  const sol = new Solution();
  const critical = sol.findCriticalNodes(n, m, adj);

  console.log(critical.length);
  console.log(critical.join(" "));
}

solve();
```
