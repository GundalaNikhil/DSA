---
problem_id: GRP_BATTERY_ARCHIPELAGO__3928
display_id: GRP-010
slug: battery-archipelago-analyzer
title: "Battery Archipelago Analyzer"
difficulty: Hard
difficulty_score: 65
topics:
  - Shortest Path
  - Dijkstra Variant
  - Custom Constraints
tags:
  - graph
  - dijkstra
  - shortest-path
  - constraints
  - hard
premium: true
subscription_tier: premium
time_limit: 2000
memory_limit: 256
---

# GRP-010: Battery Archipelago Analyzer

## Problem Statement

Given a weighted undirected graph with `n` nodes and a battery constraint, find the shortest path from source `s` to destination `d` such that no single edge weight exceeds the battery capacity `B`.

Each edge has a weight representing the energy/distance required. You can only traverse an edge if its weight is <= B. Among all valid paths (paths where every edge weight <= B), find the one with minimum total cost.

Return the minimum total cost, or `-1` if no valid path exists.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_010.jpg)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of undirected edges)
- Next `m` lines: three integers `u v w` representing an undirected edge between `u` and `v` with weight `w`
- Last line: three integers `s d B` (source, destination, battery capacity)

## Output Format

- Single integer: minimum cost from `s` to `d` using only edges with weight <= B, or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `1 <= w <= 10^6`
- `0 <= s, d < n`
- `1 <= B <= 10^6`

## Example

**Input:**

```
4
5
0 1 10
0 2 50
1 2 20
1 3 30
2 3 5
0 3 25
```

**Output:**

```
35
```

**Explanation:**

Battery capacity B = 25

Available paths from 0 to 3:

- Direct 0→3: NOT VALID (edge weight 30 > 25)
- Path 0→1→3: cost = 10+30 = NOT VALID (edge 1→3 has weight 30 > 25)
- Path 0→2→3: NOT VALID (edge 0→2 has weight 50 > 25)
- Path 0→1→2→3: cost = 10+20+5 = 35 (all edges <= 25) ✓
- Path 0→1→3: cost = 10+30 = 40 (edge 1→3 has weight 30 > 25) ❌
- Path 0→2→3: cost = 50+5 = 55 (edge 0→2 has weight 50 > 25) ❌

The minimum valid path with all edges <= 25 has total cost 35.

![Example Visualization](../images/GRP-010/example-1.png)

## Notes

- Modified Dijkstra: only consider edges with weight <= B
- Filter the adjacency list before running Dijkstra to exclude heavy edges
- Alternatively, modify Dijkstra to skip edges with weight > B during relaxation
- Time complexity: O((n + m) log n)
- This is a constrained shortest path problem

## Related Topics

Dijkstra's Algorithm, Constrained Shortest Path, Graph Filtering, Weighted Graph

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long getMinCost(int n, List<List<Edge>> adj, int s, int d, int b) {
        // Implement here
        return -1;
    }

    static class Edge {
        int to;
        long weight;
        Edge(int to, long weight) {
            this.to = to;
            this.weight = weight;
        }
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

        List<List<Solution.Edge>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edge = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edge[0]);
            int v = Integer.parseInt(edge[1]);
            long w = Long.parseLong(edge[2]);
            adj.get(u).add(new Solution.Edge(v, w));
            adj.get(v).add(new Solution.Edge(u, w));
        }

        String[] sdb = br.readLine().trim().split("\\s+");
        int s = Integer.parseInt(sdb[0]);
        int d = Integer.parseInt(sdb[1]);
        int b = Integer.parseInt(sdb[2]);

        Solution sol = new Solution();
        System.out.println(sol.getMinCost(n, adj, s, d, b));
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def get_min_cost(self, n, adj, s, d, b):
        # Implement here
        return -1

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
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3

    s = int(input_data[idx])
    d = int(input_data[idx+1])
    b = int(input_data[idx+2])

    sol = Solution()
    print(sol.get_min_cost(n, adj, s, d, b))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    long long weight;
};

class Solution {
public:
    long long getMinCost(int n, vector<vector<Edge>>& adj, int s, int d, int b) {
        // Implement here
        return -1;
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
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    int s, d, b;
    cin >> s >> d >> b;

    Solution sol;
    cout << sol.getMinCost(n, adj, s, d, b) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getMinCost(n, adj, s, d, b) {
    // Implement here
    return -1;
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
    const w = BigInt(input[idx++]);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const s = parseInt(input[idx++]);
  const d = parseInt(input[idx++]);
  const b = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.getMinCost(n, adj, s, d, b).toString());
}

solve();
```
