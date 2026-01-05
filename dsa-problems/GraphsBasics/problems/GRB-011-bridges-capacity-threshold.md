---
problem_id: GRB_BRIDGES_CAPACITY_THRESHOLD__4509
display_id: GRB-011
slug: bridges-capacity-threshold
title: "Bridges With Capacity Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Graphs
  - Bridges
  - DFS
tags:
  - graphs-basics
  - bridges
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-011: Bridges With Capacity Threshold

## Problem Statement

You are given an undirected graph where each edge has a capacity `c`. An edge is **critical** if:

1. It is a bridge (removing it increases the number of connected components), and
2. Its capacity is strictly less than a threshold `T`.

Find all such edges.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graph_basics/GRB-011.jpg)

## Input Format

- First line: integers `n`, `m`, and `T`
- Next `m` lines: `u v c` describing an undirected edge with capacity `c`

## Output Format

- Line 1: integer `k`, number of critical edges
- Next `k` lines: `u v` for each critical edge in the order they appear in input

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= c <= 10^9`
- `0 <= T <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4 3
0 1 1
1 2 5
2 0 1
1 3 2
```

**Output:**

```
1
1 3
```

**Explanation:**

Edge (1,3) is a bridge and has capacity 2 < 3.

![Example Visualization](../images/GRB-011/example-1.png)

## Notes

- Use DFS low-link to detect bridges.
- The order of output edges must match their input order.
- If no edges qualify, print `0` and nothing else.

## Related Topics

Bridges, DFS, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<int[]> findCriticalEdges(int n, int m, long threshold, List<Edge> edges, List<List<Integer>> adj) {
        // Implement here
        return new ArrayList<>();
    }

    static class Edge {
        int u, v;
        long c;
        Edge(int u, int v, long c) {
            this.u = u;
            this.v = v;
            this.c = c;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmtLine = br.readLine();
        if (nmtLine == null) return;
        String[] nmt = nmtLine.trim().split("\\s+");
        int n = Integer.parseInt(nmt[0]);
        int m = Integer.parseInt(nmt[1]);
        long t = Long.parseLong(nmt[2]);

        List<Solution.Edge> edges = new ArrayList<>();
        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(line[0]);
            int v = Integer.parseInt(line[1]);
            long c = Long.parseLong(line[2]);
            edges.add(new Solution.Edge(u, v, c));
            adj.get(u).add(i); // Store edge index for multi-edge handling if needed
            adj.get(v).add(i);
        }

        Solution sol = new Solution();
        List<int[]> critical = sol.findCriticalEdges(n, m, t, edges, adj);

        PrintWriter out = new PrintWriter(System.out);
        out.println(critical.size());
        for (int[] edge : critical) {
            out.println(edge[0] + " " + edge[1]);
        }
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
    def find_critical_edges(self, n, m, t, edges, adj):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    edges = []
    adj = [[] for _ in range(n)]
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        edges.append((u, v, c))
        adj[u].append(i)
        adj[v].append(i)
        idx += 3

    sol = Solution()
    critical = sol.find_critical_edges(n, m, t, edges, adj)

    print(len(critical))
    for u, v in critical:
        print(f"{u} {v}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u, v;
    long long c;
};

class Solution {
public:
    vector<pair<int, int>> findCriticalEdges(int n, int m, long long t, vector<Edge>& edges, vector<vector<int>>& adj) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    long long t;
    if (!(cin >> n >> m >> t)) return 0;

    vector<Edge> edges(m);
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].c;
        adj[edges[i].u].push_back(i);
        adj[edges[i].v].push_back(i);
    }

    Solution sol;
    vector<pair<int, int>> critical = sol.findCriticalEdges(n, m, t, edges, adj);

    cout << critical.size() << endl;
    for (auto& edge : critical) {
        cout << edge.first << " " << edge.second << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findCriticalEdges(n, m, t, edges, adj) {
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
  const t = BigInt(input[idx++]);

  const edges = [];
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    const c = BigInt(input[idx++]);
    edges.push({ u, v, c });
    adj[u].push(i);
    adj[v].push(i);
  }

  const sol = new Solution();
  const critical = sol.findCriticalEdges(n, m, t, edges, adj);

  process.stdout.write(critical.length + "\n");
  for (let edge of critical) {
    process.stdout.write(edge[0] + " " + edge[1] + "\n");
  }
}

solve();
```
