---
problem_id: GRB_TOPO_SORT_KAHN__7394
display_id: GRB-005
slug: topo-sort-kahn
title: "Topological Sort (Kahn)"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - Topological Sort
  - BFS
tags:
  - graphs-basics
  - topo-sort
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-005: Topological Sort (Kahn)

## Problem Statement

Given a directed acyclic graph (DAG), output any valid topological ordering of its nodes.

![Problem Illustration](../images/GRB-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` representing a directed edge `u -> v`

## Output Format

- Single line: `n` integers representing a topological ordering

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
- The input graph is guaranteed to be a DAG

## Example

**Input:**

```
3 2
0 1
1 2
```

**Output:**

```
0 1 2
```

**Explanation:**

The ordering `0 -> 1 -> 2` respects all edges.

![Example Visualization](../images/GRB-005/example-1.png)

## Notes

- Use Kahn's algorithm with an indegree queue.
- Multiple valid orders may exist; any is accepted.
- Since the graph is a DAG, a full ordering always exists.

## Related Topics

Topological Sort, DAGs, BFS

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] topoSort(int n, int m, List<List<Integer>> adj) {
        // Implement here
        return new int[0];
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
        }

        Solution sol = new Solution();
        int[] result = sol.topoSort(n, m, adj);

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
    def topo_sort(self, n, m, adj):
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
        idx += 2

    sol = Solution()
    result = sol.topo_sort(n, m, adj)
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
    vector<int> topoSort(int n, int m, vector<vector<int>>& adj) {
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
    }

    Solution sol;
    vector<int> result = sol.topoSort(n, m, adj);

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
  topoSort(n, m, adj) {
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
  }

  const sol = new Solution();
  const result = sol.topoSort(n, m, adj);
  console.log(result.join(" "));
}

solve();
```
