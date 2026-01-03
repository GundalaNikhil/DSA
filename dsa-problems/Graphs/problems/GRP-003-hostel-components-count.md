---
problem_id: GRP_HOSTEL_COMPONENTS_COUNT__3184
display_id: GRP-003
slug: hostel-components-count
title: "Hostel Components Count"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - Connected Components
  - Union-Find
tags:
  - graph
  - connected-components
  - bfs
  - dfs
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-003: Hostel Components Count

## Problem Statement

Given an undirected graph with `n` nodes (numbered from 0 to n-1) and an adjacency list, count the number of connected components in the graph.

A connected component is a maximal set of nodes where every pair of nodes is connected by a path. Two nodes are in the same component if and only if there exists a path between them.

![Problem Illustration](../images/GRP-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single integer representing the number of connected components

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
2
0 1
2 3
```

**Output:**

```
3
```

**Explanation:**

The graph has 5 nodes and 2 edges:

- Component 1: {0, 1} - connected by edge (0,1)
- Component 2: {2, 3} - connected by edge (2,3)
- Component 3: {4} - isolated node

Total: 3 connected components

![Example Visualization](../images/GRP-003/example-1.png)

## Notes

- A single isolated node (with no edges) forms its own connected component
- Can be solved using BFS, DFS, or Union-Find (Disjoint Set Union)
- Iterate through all nodes; for each unvisited node, start a BFS/DFS to mark all reachable nodes
- Each time you start a new BFS/DFS, increment the component count
- Time complexity: O(n + m) for BFS/DFS approach

## Related Topics

Connected Components, Graph Traversal, BFS, DFS, Union-Find, Disjoint Set Union

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countComponents(int n, List<List<Integer>> adj) {
        //Implement here
        return 0;
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
        System.out.println(solution.countComponents(n, adj));
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

def count_components(n: int, adj: List[List[int]]) -> int:
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
    
    result = count_components(n, adj)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    public: int countComponents(int n, vector<vector<int>>& adj) {
        //Implement here
        return 0;
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
    
    Solution solution;
    cout << solution.countComponents(n, adj) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countComponents(n, adj) {
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
  console.log(solution.countComponents(n, adj));
});
```

