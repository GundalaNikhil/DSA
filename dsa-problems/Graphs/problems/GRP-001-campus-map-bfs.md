---
problem_id: GRP_CAMPUS_MAP_BFS__4821
display_id: GRP-001
slug: campus-map-bfs
title: "Campus Map BFS"
difficulty: Easy
difficulty_score: 25
topics:
  - Graph Traversal
  - Breadth-First Search
  - Queue
tags:
  - graph
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-001: Campus Map BFS

## Problem Statement

Given an undirected unweighted graph represented by `n` nodes (numbered from 0 to n-1) and an adjacency list, perform a Breadth-First Search (BFS) starting from node 0 and return the order in which nodes are visited.

The graph is represented as an adjacency list where each node may have zero or more neighbors. You must traverse the graph level by level, visiting all nodes at distance `k` before visiting any nodes at distance `k+1`.

![Problem Illustration](../images/GRP-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single line with space-separated integers representing the order of nodes visited during BFS starting from node 0

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- The graph may be disconnected
- There are no self-loops or multiple edges

## Example

**Input:**
```
4
3
0 1
0 2
1 3
```

**Output:**
```
0 1 2 3
```

**Explanation:**

Starting from node 0:
- Level 0: Visit node 0
- Level 1: Visit nodes 1 and 2 (neighbors of 0, in the order they appear in adjacency list)
- Level 2: Visit node 3 (neighbor of 1)

The BFS traversal visits nodes in order: 0 → 1 → 2 → 3

![Example Visualization](../images/GRP-001/example-1.png)

## Notes

- Use a queue data structure to maintain the FIFO order of traversal
- Use a visited array/set to track which nodes have been explored to avoid revisiting
- If the graph is disconnected, only nodes reachable from node 0 will be visited
- The order of neighbors in the adjacency list determines the order of visitation when multiple nodes are at the same level
- Nodes that are not reachable from node 0 will not appear in the output

## Related Topics

Graph Traversal, BFS, Queue, Visited Set, Level Order Traversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> bfsTraversal(int n, List<List<Integer>> adj) {
        //Implement here
        return new ArrayList<>();
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

        // Sort neighbors for deterministic traversal
        for (int i = 0; i < n; i++) {
            Collections.sort(adj.get(i));
        }

        Solution solution = new Solution();
        List<Integer> result = solution.bfsTraversal(n, adj);
        
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(200000)

def bfs_traversal(n: int, adj: List[List[int]]) -> List[int]:
    # //Implement here
    return 0

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    result = bfs_traversal(n, adj)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    public: vector<int> bfsTraversal(int n, vector<vector<int>>& adj) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
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
    vector<int> result = solution.bfsTraversal(n, adj);
    
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bfsTraversal(n, adj) {
    //Implement here
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
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const m = parseInt(data[ptr++]);
  
  const adj = Array.from({ length: n }, () => []);

  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  // Sort neighbors for deterministic traversal
  for (let i = 0; i < n; i++) {
    adj[i].sort((a, b) => a - b);
  }

  const solution = new Solution();
  const result = solution.bfsTraversal(n, adj);
  console.log(result.join(" "));
});
```

