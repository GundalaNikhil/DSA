---
problem_id: GRP_ROBOTICS_WEIGHTED_REACH__9571
display_id: GRP-018
slug: robotics-weighted-reachability
title: "Robotics Weighted Reachability"
difficulty: Medium
difficulty_score: 50
topics:
  - Weighted Graph
  - BFS
  - DFS
  - Union-Find
tags:
  - graph
  - weighted-graph
  - reachability
  - bfs
  - dfs
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-018: Robotics Weighted Reachability

## Problem Statement

Given a weighted undirected graph with `n` nodes (numbered 0 to n-1), edges with positive weights, and a threshold `T`, count how many nodes are reachable from node 0 using only edges with weight `<= T`.

An edge (u, v, w) can be traversed if and only if `w <= T`. Count all nodes that can be reached from node 0 through such valid edges.

![Problem Illustration](../images/GRP-018/problem-illustration.png)

## Input Format

- First line: two integers `n T` (number of nodes and threshold)
- Second line: integer `m` (number of edges)
- Next `m` lines: three integers `u v w` representing an undirected edge between nodes `u` and `v` with weight `w`

## Output Format

- Single integer: number of nodes reachable from node 0 using only edges with weight `<= T` (including node 0 itself)

## Constraints

- `1 <= n <= 10^5`
- `1 <= m <= 2*10^5`
- `0 <= u, v < n`
- `1 <= w <= 10^9`
- `0 <= T <= 10^9`

## Example

**Input:**

```
5 4
4
0 1 3
1 2 7
0 3 2
3 4 5
```

**Output:**

```
3
```

**Explanation:**

Graph edges:

- (0, 1) with weight 3 ≤ 4 ✓ (valid)
- (1, 2) with weight 7 > 4 ✗ (invalid)
- (0, 3) with weight 2 ≤ 4 ✓ (valid)
- (3, 4) with weight 5 > 4 ✗ (invalid)

Reachable nodes from node 0 using edges with weight ≤ 4:

- Node 0 (starting point)
- Node 1 (via edge 0-1 with weight 3)
- Node 3 (via edge 0-3 with weight 2)

Nodes 2 and 4 are not reachable because:

- Node 2 requires edge (1,2) with weight 7 > 4
- Node 4 requires edge (3,4) with weight 5 > 4

Total reachable: 3 nodes

![Example Visualization](../images/GRP-018/example-1.png)

## Notes

- Filter edges to include only those with weight ≤ T
- Run BFS or DFS from node 0 on the filtered graph
- Count all visited nodes
- Alternative approach: Use Union-Find
  - Sort edges by weight
  - Union nodes connected by edges with weight ≤ T
  - Return size of component containing node 0
- Time complexity: O(m log m) for sorting + O(m × α(n)) for Union-Find, or O(n + m) for BFS/DFS

## Related Topics

Weighted Graph, Reachability, BFS, DFS, Union-Find, Edge Filtering

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countReachable(int n, long t, List<Edge> edges) {
        // Implement here
        return 0;
    }

    static class Edge {
        int u, v;
        long w;
        Edge(int u, int v, long w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ntLine = br.readLine();
        if (ntLine == null) return;
        String[] nt = ntLine.trim().split("\\s+");
        int n = Integer.parseInt(nt[0]);
        long t = Long.parseLong(nt[1]);

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        List<Solution.Edge> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            edges.add(new Solution.Edge(Integer.parseInt(line[0]), Integer.parseInt(line[1]), Long.parseLong(line[2])));
        }

        Solution sol = new Solution();
        System.out.println(sol.countReachable(n, t, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_reachable(self, n, t, edges):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    t = int(input_data[1])
    m = int(input_data[2])

    idx = 3
    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((u, v, w))
        idx += 3

    sol = Solution()
    print(sol.count_reachable(n, t, edges))

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
    long long w;
};

class Solution {
public:
    int countReachable(int n, long long t, vector<Edge>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long t;
    if (!(cin >> n >> t)) return 0;

    int m;
    cin >> m;

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    Solution sol;
    cout << sol.countReachable(n, t, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countReachable(n, t, edges) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const t = BigInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    const w = BigInt(input[idx++]);
    edges.push([u, v, w]);
  }

  const sol = new Solution();
  console.log(sol.countReachable(n, t, edges));
}

solve();
```
