---
problem_id: GRP_ROBOTICS_BRIDGES__4172
display_id: GRP-013
slug: robotics-bridges
title: "Robotics Bridges"
difficulty: Medium
difficulty_score: 60
topics:
  - Graph Theory
  - Bridges
  - Tarjan's Algorithm
  - DFS
tags:
  - graph
  - bridges
  - tarjan
  - dfs
  - critical-edges
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-013: Robotics Bridges

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1), find all bridges in the graph.

A **bridge** (or cut edge) is an edge whose removal increases the number of connected components. In other words, removing a bridge disconnects the graph (or a component).

Return a list of all bridges as pairs of nodes.

![Problem Illustration](../images/GRP-013/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- First line: integer `k` (number of bridges)
- Next `k` lines: two integers `u v` representing a bridge edge (output each bridge in sorted order: smaller node first)
- Sort bridges lexicographically

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**
```
5
5
0 1
1 2
2 0
1 3
3 4
```

**Output:**
```
2
1 3
3 4
```

**Explanation:**

Graph structure:
- Nodes {0, 1, 2} form a cycle (triangle)
- Node 3 is connected to node 1
- Node 4 is connected to node 3

Bridges:
- Edge (1, 3): Removing it disconnects the triangle {0,1,2} from nodes {3,4}
- Edge (3, 4): Removing it disconnects node 4 from the rest

Edges (0,1), (1,2), (2,0) are NOT bridges because they're part of a cycle.

![Example Visualization](../images/GRP-013/example-1.png)

## Notes

- Use Tarjan's algorithm for finding bridges
- Maintain discovery time and low-link values for each node during DFS
- An edge (u, v) is a bridge if: `low[v] > discovery[u]` (where v is a child of u in DFS tree)
- Low-link value: minimum discovery time reachable from the subtree rooted at that node
- Time complexity: O(n + m)
- Space complexity: O(n)

## Related Topics

Bridges, Tarjan's Algorithm, DFS, Cut Edges, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<int[]> findBridges(int n, List<List<Integer>> adj) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
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
        List<int[]> bridges = solution.findBridges(n, adj);
        
        // Sort bridges
        bridges.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        
        System.out.println(bridges.size());
        for (int[] bridge : bridges) {
            System.out.println(bridge[0] + " " + bridge[1]);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def find_bridges(n: int, adj: List[List[int]]) -> List[tuple]:
    # Your implementation here
    return []

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    bridges = find_bridges(n, adj)
    bridges.sort()
    
    print(len(bridges))
    for u, v in bridges:
        print(f"{u} {v}")

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
public:
    vector<pair<int,int>> findBridges(int n, vector<vector<int>>& adj) {
        // Your implementation here
        return vector<pair<int,int>>();
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
    vector<pair<int,int>> bridges = solution.findBridges(n, adj);
    
    sort(bridges.begin(), bridges.end());
    
    cout << bridges.size() << "\n";
    for (auto [u, v] : bridges) {
        cout << u << " " << v << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findBridges(n, adj) {
    // Your implementation here
    return [];
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
  
  const solution = new Solution();
  const bridges = solution.findBridges(n, adj);
  
  bridges.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];
    return a[1] - b[1];
  });
  
  console.log(bridges.length);
  bridges.forEach(([u, v]) => console.log(``u`{v}`));
});
```