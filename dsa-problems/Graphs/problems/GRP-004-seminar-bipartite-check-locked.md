---
problem_id: GRP_SEMINAR_BIPARTITE_LOCKED__6927
display_id: GRP-004
slug: seminar-bipartite-check-locked
title: "Seminar Bipartite Check with Locked Nodes"
difficulty: Medium
difficulty_score: 50
topics:
  - Graph Coloring
  - Bipartite Graphs
  - BFS
  - DFS
tags:
  - graph
  - bipartite
  - coloring
  - bfs
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-004: Seminar Bipartite Check with Locked Nodes

## Problem Statement

Given an undirected graph with `n` nodes, determine if the graph can be colored to satisfy bipartite constraints while respecting pre-colored (locked) nodes.

Some nodes are pre-colored either group A (locked value 1) or group B (locked value 2) and cannot change their color. Unlocked nodes (value 0) can be colored either A or B. The graph must satisfy the bipartite property: no two adjacent nodes can have the same color.

Return `true` if a valid coloring exists, `false` otherwise.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/graphs/grp_004.jpg)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`
- Last line: `n` space-separated integers representing the locked array (0 = unlocked, 1 = force group A, 2 = force group B)

## Output Format

- Single word: `true` if valid bipartite coloring exists, `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- locked[i] ∈ {0, 1, 2}
- There are no self-loops or multiple edges

## Example

**Input:**

```
4
4
0 1
1 2
2 3
3 0
0 1 0 2
```

**Output:**

```
true
```

**Explanation:**

The graph forms a cycle: 0 - 1 - 2 - 3 - 0

- Node 0: locked to group A (1)
- Node 1: unlocked (0)
- Node 2: unlocked (0)
- Node 3: locked to group B (2)

Valid coloring:

- Node 0: A (locked)
- Node 1: B (to satisfy edge 0-1)
- Node 2: A (to satisfy edge 1-2)
- Node 3: B (locked, and satisfies edges 2-3 and 3-0)

This is a valid bipartite coloring.

![Example Visualization](../images/GRP-004/example-1.png)

## Notes

- Use BFS or DFS for graph coloring
- When visiting a locked node, check if its forced color conflicts with the color it should have based on its parent
- If a locked node's color conflicts with its required color, return false immediately
- For unlocked nodes, assign them the opposite color of their parent
- Handle disconnected components by checking all nodes
- A cycle of odd length cannot be bipartite

## Related Topics

Bipartite Graphs, Graph Coloring, BFS, DFS, Two-Coloring

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean isBipartite(int n, List<List<Integer>> adj, int[] locked) {
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
            adj.get(v).add(u);
        }

        String[] lockedStr = br.readLine().trim().split("\\s+");
        int[] locked = new int[n];
        for (int i = 0; i < n; i++) {
            locked[i] = Integer.parseInt(lockedStr[i]);
        }

        Solution sol = new Solution();
        System.out.println(sol.isBipartite(n, adj, locked));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

class Solution:
    def is_bipartite(self, n, adj, locked):
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
        adj[v].append(u)
        idx += 2

    locked = []
    for _ in range(n):
        locked.append(int(input_data[idx]))
        idx += 1

    sol = Solution()
    print("true" if sol.is_bipartite(n, adj, locked) else "false")

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
    bool isBipartite(int n, vector<vector<int>>& adj, vector<int>& locked) {
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
        adj[v].push_back(u);
    }

    vector<int> locked(n);
    for (int i = 0; i < n; i++) {
        cin >> locked[i];
    }

    Solution sol;
    if (sol.isBipartite(n, adj, locked)) {
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
  isBipartite(n, adj, locked) {
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
    adj[v].push(u);
  }

  const locked = [];
  for (let i = 0; i < n; i++) {
    locked.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.isBipartite(n, adj, locked).toString());
}

solve();
```
