---
problem_id: GRB_MST_PRIM__9142
display_id: GRB-008
slug: mst-prim
title: "MST Prim"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - Priority Queue
tags:
  - graphs-basics
  - mst
  - prim
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-008: MST Prim

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Prim's algorithm.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graph_basics/GRB-008.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the total weight of the MST

## Constraints

- `1 <= n <= 100000`
- `n-1 <= m <= 200000`
- `0 <= w <= 10^9`
- The graph is connected

## Example

**Input:**

```
3 3
0 1 1
1 2 2
0 2 3
```

**Output:**

```
3
```

**Explanation:**

Prim's algorithm selects edges with weights 1 and 2 for total 3.

![Example Visualization](../images/GRB-008/example-1.png)

## Notes

- Use a min-heap keyed by edge weight.
- Track visited nodes to avoid cycles.
- Total MST weight fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Prim, Priority Queue

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long mstPrim(int n, int m, List<List<Edge>> adj) {
        // Implement here
        return 0;
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
        String nmLine = br.readLine();
        if (nmLine == null) return;
        String[] nm = nmLine.trim().split("\\s+");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        List<List<Solution.Edge>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            String[] edgeLine = br.readLine().trim().split("\\s+");
            int u = Integer.parseInt(edgeLine[0]);
            int v = Integer.parseInt(edgeLine[1]);
            long w = Long.parseLong(edgeLine[2]);
            adj.get(u).add(new Solution.Edge(v, w));
            adj.get(v).add(new Solution.Edge(u, w));
        }

        Solution sol = new Solution();
        System.out.println(sol.mstPrim(n, m, adj));
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def mst_prim(self, n, m, adj):
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
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3

    sol = Solution()
    print(sol.mst_prim(n, m, adj))

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
    long long mstPrim(int n, int m, vector<vector<Edge>>& adj) {
        // Implement here
        return 0;
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

    Solution sol;
    cout << sol.mstPrim(n, m, adj) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  mstPrim(n, m, adj) {
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
    const u = parseInt(input[idx++]);
    const v = parseInt(input[idx++]);
    const w = BigInt(input[idx++]);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const sol = new Solution();
  console.log(sol.mstPrim(n, m, adj).toString());
}

solve();
```
