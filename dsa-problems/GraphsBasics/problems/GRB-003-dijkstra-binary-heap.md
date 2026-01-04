---
problem_id: GRB_DIJKSTRA_BINARY_HEAP__6041
display_id: GRB-003
slug: dijkstra-binary-heap
title: "Dijkstra with Binary Heap"
difficulty: Medium
difficulty_score: 45
topics:
  - Graphs
  - Dijkstra
  - Shortest Path
tags:
  - graphs-basics
  - dijkstra
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-003: Dijkstra with Binary Heap

## Problem Statement

You are given a directed graph with non-negative edge weights. Compute the shortest distance from a source node `s` to every node.

If a node is unreachable, its distance should be `-1`.

![Problem Illustration](../images/GRB-003/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Single line: `n` integers, the distances from `s` to nodes `0..n-1`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= w <= 10^9`
- `0 <= s < n`

## Example

**Input:**

```
3 3 0
0 1 1
1 2 2
0 2 5
```

**Output:**

```
0 1 3
```

**Explanation:**

The shortest path to node 2 is `0 -> 1 -> 2` with total cost 3.

![Example Visualization](../images/GRB-003/example-1.png)

## Notes

- Use Dijkstra with a min-heap (priority queue).
- Skip outdated heap entries using a distance check.
- Distances can exceed 32-bit; use 64-bit integers.

## Related Topics

Dijkstra, Priority Queue, Shortest Path

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] dijkstra(int n, int m, int s, List<List<Edge>> adj) {
        // Implement here
        return new long[0];
    }

    static class Edge {
        int to;
        int weight;
        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmsLine = br.readLine();
        if (nmsLine == null) return;
        String[] nms = nmsLine.trim().split("\\s+");
        int n = Integer.parseInt(nms[0]);
        int m = Integer.parseInt(nms[1]);
        int s = Integer.parseInt(nms[2]);

        List<List<Solution.Edge>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edgeLine = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edgeLine[0]);
            int v = Integer.parseInt(edgeLine[1]);
            int w = Integer.parseInt(edgeLine[2]);
            adj.get(u).add(new Solution.Edge(v, w));
        }

        Solution sol = new Solution();
        long[] distances = sol.dijkstra(n, m, s, adj);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < n; i++) {
            out.print(distances[i] + (i == n - 1 ? "" : " "));
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
    def dijkstra(self, n, m, s, adj):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])

    adj = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        idx += 3

    sol = Solution()
    distances = sol.dijkstra(n, m, s, adj)
    print(*(distances))

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
    int weight;
};

class Solution {
public:
    vector<long long> dijkstra(int n, int m, int s, vector<vector<Edge>>& adj) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<vector<Edge>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution sol;
    vector<long long> distances = sol.dijkstra(n, m, s, adj);

    for (int i = 0; i < n; i++) {
        cout << distances[i] << (i == n - 1 ? "" : " ");
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
  dijkstra(n, m, s, adj) {
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
  const s = parseInt(input[idx++]);

  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    const w = parseInt(input[idx++]);
    adj[u].push([v, w]);
  }

  const sol = new Solution();
  const distances = sol.dijkstra(n, m, s, adj);
  console.log(distances.join(" "));
}

solve();
```
