---
problem_id: GRP_CITY_TOLL_DIJKSTRA__7561
display_id: GRP-009
slug: city-toll-dijkstra
title: "City Toll Dijkstra"
difficulty: Medium
difficulty_score: 55
topics:
  - Shortest Path
  - Dijkstra
  - Priority Queue
tags:
  - graph
  - dijkstra
  - shortest-path
  - weighted-graph
  - priority-queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-009: City Toll Dijkstra

## Problem Statement

Given a weighted directed graph with `n` nodes (numbered 0 to n-1), find the shortest path from a source node `s` to all other nodes using Dijkstra's algorithm.

Each edge has a non-negative weight representing the toll/cost. Output the minimum cost to reach each node from the source. If a node is unreachable, output `-1`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_009.jpg)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of directed edges)
- Next `m` lines: three integers `u v w` representing a directed edge from node `u` to node `v` with weight `w`
- Last line: integer `s` (source node)

## Output Format

- Single line with `n` space-separated integers representing the shortest distance from source `s` to nodes 0, 1, 2, ..., n-1

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `0 <= w <= 10^6`
- `0 <= s < n`
- There are no self-loops or negative weights

## Example

**Input:**

```
4
5
0 1 4
0 2 1
2 1 2
1 3 1
2 3 5
0
```

**Output:**

```
0 3 1 4
```

**Explanation:**

From source node 0:

- To node 0: 0 (source itself)
- To node 1: 3 (path 0→2→1 with cost 1+2=3, better than direct 0→1 with cost 4)
- To node 2: 1 (direct path 0→2)
- To node 3: 4 (path 0→2→1→3 with cost 1+2+1=4)

![Example Visualization](../images/GRP-009/example-1.png)

## Notes

- Use Dijkstra's algorithm with a priority queue (min-heap)
- Initialize all distances to infinity (or a large value), except source which is 0
- Always extract the node with minimum distance from the priority queue
- Relax edges: if distance[u] + weight(u,v) < distance[v], update distance[v]
- Works only with non-negative edge weights
- Time complexity: O((n + m) log n) with binary heap
- Space complexity: O(n + m)

## Related Topics

Dijkstra's Algorithm, Shortest Path, Weighted Graph, Priority Queue, Greedy Algorithm

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] getShortestCosts(int n, List<List<Edge>> adj, int s) {
        // Implement here
        return new long[0];
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
        }

        String sLine = br.readLine();
        if (sLine == null) return;
        int s = Integer.parseInt(sLine.trim());

        Solution sol = new Solution();
        long[] result = sol.getShortestCosts(n, adj, s);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < n; i++) {
            out.print(result[i] + (i == n - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def get_shortest_costs(self, n, adj, s):
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
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        idx += 3

    s = int(input_data[idx])

    sol = Solution()
    result = sol.get_shortest_costs(n, adj, s)
    print(*(result))

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
    vector<long long> getShortestCosts(int n, vector<vector<Edge>>& adj, int s) {
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
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    int s;
    cin >> s;

    Solution sol;
    vector<long long> result = sol.getShortestCosts(n, adj, s);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
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
  getShortestCosts(n, adj, s) {
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
    const w = BigInt(input[idx++]);
    adj[u].push([v, w]);
  }

  const s = parseInt(input[idx++]);

  const sol = new Solution();
  const result = sol.getShortestCosts(n, adj, s);
  console.log(result.join(" "));
}

solve();
```
