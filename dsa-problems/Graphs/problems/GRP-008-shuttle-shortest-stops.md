---
problem_id: GRP_SHUTTLE_SHORTEST_STOPS__9247
display_id: GRP-008
slug: shuttle-shortest-stops
title: "Shuttle Shortest Stops"
difficulty: Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - BFS
  - Shortest Path
tags:
  - graph
  - bfs
  - shortest-path
  - unweighted
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-008: Shuttle Shortest Stops

## Problem Statement

Given an unweighted undirected graph with `n` nodes (numbered 0 to n-1) and a source node `s`, find the shortest distance (in number of edges) from the source to all other nodes.

For each node, output its shortest distance from the source. If a node is unreachable from the source, output `-1` for that node.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_008.jpg)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`
- Last line: integer `s` (source node)

## Output Format

- Single line with `n` space-separated integers representing the shortest distance from source `s` to nodes 0, 1, 2, ..., n-1

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `0 <= s < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
4
0 1
1 2
0 3
3 4
0
```

**Output:**

```
0 1 2 1 2
```

**Explanation:**

Starting from node 0 (source):

- Distance to node 0: 0 (source itself)
- Distance to node 1: 1 (direct edge 0→1)
- Distance to node 2: 2 (path 0→1→2)
- Distance to node 3: 1 (direct edge 0→3)
- Distance to node 4: 2 (path 0→3→4)

![Example Visualization](../images/GRP-008/example-1.png)

## Notes

- Use BFS (Breadth-First Search) to find shortest paths in unweighted graphs
- Initialize all distances to -1, then set source distance to 0
- BFS guarantees that nodes are visited in increasing order of distance from source
- Time complexity: O(n + m)
- Space complexity: O(n) for queue and distance array

## Related Topics

BFS, Shortest Path, Unweighted Graph, Level Order Traversal

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] getShortestDistances(int n, List<List<Integer>> adj, int s) {
        // Implement here
        return new int[0];
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

        String sLine = br.readLine();
        if (sLine == null) return;
        int s = Integer.parseInt(sLine.trim());

        Solution sol = new Solution();
        int[] result = sol.getShortestDistances(n, adj, s);

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
from collections import deque

class Solution:
    def get_shortest_distances(self, n, adj, s):
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

    s = int(input_data[idx])

    sol = Solution()
    result = sol.get_shortest_distances(n, adj, s)
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

class Solution {
public:
    vector<int> getShortestDistances(int n, vector<vector<int>>& adj, int s) {
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

    int s;
    cin >> s;

    Solution sol;
    vector<int> result = sol.getShortestDistances(n, adj, s);

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
  getShortestDistances(n, adj, s) {
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

  const s = parseInt(input[idx++]);

  const sol = new Solution();
  const result = sol.getShortestDistances(n, adj, s);
  console.log(result.join(" "));
}

solve();
```
