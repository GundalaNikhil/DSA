---
problem_id: GRP_LAB_DIRECTED_CYCLE__2647
display_id: GRP-006
slug: lab-directed-cycle-check
title: "Lab Directed Cycle Check"
difficulty: Medium
difficulty_score: 50
topics:
  - Directed Graph
  - Cycle Detection
  - DFS
  - Topological Sort
tags:
  - graph
  - directed-graph
  - cycle-detection
  - dfs
  - topological-sort
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-006: Lab Directed Cycle Check

## Problem Statement

Given a directed graph with `n` nodes (numbered from 0 to n-1) and an adjacency list, detect if the graph contains any cycle.

A cycle in a directed graph is a path that starts and ends at the same vertex, following the direction of edges. Return `true` if the graph contains at least one cycle, `false` otherwise.

![Problem Illustration](../images/GRP-006/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of directed edges)
- Next `m` lines: two integers `u v` representing a directed edge from node `u` to node `v`

## Output Format

- Single word: `true` if cycle exists, `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops

## Example

**Input:**

```
4
4
0 1
1 2
2 1
2 3
```

**Output:**

```
true
```

**Explanation:**

The directed graph has a cycle:

- Node 1 → Node 2 → Node 1 (cycle of length 2)

The path 1 → 2 → 1 forms a cycle, so the output is `true`.

![Example Visualization](../images/GRP-006/example-1.png)

## Notes

- Use DFS with a recursion stack to detect cycles in directed graphs
- Maintain three states for each node: unvisited, visiting (in current recursion stack), and visited (completely processed)
- If you encounter a node that is in the visiting state, a cycle exists (back edge)
- Alternatively, use Kahn's topological sort algorithm: if unable to process all nodes (some nodes have leftover in-degree), a cycle exists
- Time complexity: O(n + m)

## Related Topics

Directed Graph, Cycle Detection, DFS, Recursion Stack, Topological Sort, Kahn's Algorithm

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        // Implement here
        return false;
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
        }

        Solution sol = new Solution();
        System.out.println(sol.hasCycle(n, adj));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

class Solution:
    def has_cycle(self, n, adj):
        # Implement here
        return False

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
    print("true" if sol.has_cycle(n, adj) else "false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool hasCycle(int n, vector<vector<int>>& adj) {
        // Implement here
        return false;
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
    if (sol.hasCycle(n, adj)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  hasCycle(n, adj) {
    // Implement here
    return false;
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
  console.log(sol.hasCycle(n, adj).toString());
}

solve();
```
