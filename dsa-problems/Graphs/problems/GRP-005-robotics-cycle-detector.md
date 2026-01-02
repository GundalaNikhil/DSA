---
problem_id: GRP_ROBOTICS_CYCLE_DETECTOR__8341
display_id: GRP-005
slug: robotics-cycle-detector
title: "Robotics Cycle Detector"
difficulty: Medium
difficulty_score: 45
topics:
  - Graph Traversal
  - Cycle Detection
  - DFS
tags:
  - graph
  - cycle-detection
  - dfs
  - undirected-graph
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-005: Robotics Cycle Detector

## Problem Statement

Given an undirected graph with `n` nodes (numbered from 0 to n-1) and an adjacency list, detect if the graph contains any cycle.

A cycle is a path of edges and vertices where a vertex is reachable from itself through at least three edges. In other words, starting from a vertex, you can traverse edges and return to the starting vertex without repeating any edge.

Return `true` if the graph contains at least one cycle, `false` otherwise.

![Problem Illustration](../images/GRP-005/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single word: `true` if cycle exists, `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
3
3
0 1
1 2
2 0
```

**Output:**

```
true
```

**Explanation:**

The graph has nodes {0, 1, 2} with edges forming a triangle:

- Edge 0-1
- Edge 1-2
- Edge 2-0

This forms a cycle: 0 → 1 → 2 → 0

Therefore, the output is `true`.

![Example Visualization](../images/GRP-005/example-1.png)

## Notes

- Use DFS with parent tracking to detect cycles in undirected graphs
- When exploring neighbors during DFS, if you encounter a visited node that is not the parent of the current node, a cycle exists
- A back edge indicates a cycle in an undirected graph
- Handle disconnected components by starting DFS from all unvisited nodes
- Time complexity: O(n + m)

## Related Topics

Cycle Detection, DFS, Back Edge, Undirected Graph, Parent Tracking

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        return false;
    }

    private boolean dfs(int node, int parent, List<List<Integer>> adj, boolean[] visited) {
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution solution = new Solution();
        boolean result = solution.hasCycle(n, adj);

        System.out.println(result ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys
sys.setrecursionlimit(200000)
from typing import List

def has_cycle(n: int, adj: List[List[int]]) -> bool:
    return False
def main():
    n = int(input())
    m = int(input())

    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    result = has_cycle(n, adj)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
        return false;
    }
    
public:
    bool hasCycle(int n, vector<vector<int>>& adj) {
        return false;
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Sort neighbors for deterministic traversal
    for (int i = 0; i < n; i++) {
        sort(adj[i].begin(), adj[i].end());
    }

    Solution solution;
    cout << (solution.hasCycle(n, adj) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasCycle(n, adj) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const adj = Array.from({ length: n }, () => []);

  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    adj[u].push(v);
    adj[v].push(u);
  }

  // Sort neighbors for deterministic traversal
  for (let i = 0; i < n; i++) {
    adj[i].sort((a, b) => a - b);
  }

  const solution = new Solution();
  console.log(solution.hasCycle(n, adj) ? "true" : "false");
});
```

