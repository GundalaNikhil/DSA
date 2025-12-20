---
problem_id: GRP_LAB_ARTICULATION_POINTS__5694
display_id: GRP-014
slug: lab-articulation-points
title: "Lab Articulation Points"
difficulty: Medium
difficulty_score: 60
topics:
  - Graph Theory
  - Articulation Points
  - Tarjan's Algorithm
  - DFS
tags:
  - graph
  - articulation-points
  - tarjan
  - dfs
  - cut-vertices
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-014: Lab Articulation Points

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1), find all articulation points (also called cut vertices) in the graph.

An **articulation point** is a node whose removal increases the number of connected components. In other words, removing an articulation point disconnects the graph (or a component).

Return a list of all articulation points in sorted order.

![Problem Illustration](../images/GRP-014/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- First line: integer `k` (number of articulation points)
- Second line: `k` space-separated integers representing articulation points in sorted order

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
```

**Explanation:**

Graph structure:
- Nodes {0, 1, 2} form a cycle (triangle)
- Node 3 is connected to node 1
- Node 4 is connected to node 3

Articulation points:
- Node 1: Removing it disconnects the triangle {0,2} from nodes {3,4}
- Node 3: Removing it disconnects node 4 from the rest of the graph

Nodes 0, 2, and 4 are NOT articulation points:
- Removing 0: Nodes still connected via 1-2 path
- Removing 2: Nodes still connected via 0-1 path
- Removing 4: Only isolates itself, doesn't increase components

![Example Visualization](../images/GRP-014/example-1.png)

## Notes

- Use Tarjan's algorithm for finding articulation points
- Maintain discovery time and low-link values for each node during DFS
- A node `u` is an articulation point if:
  - **Root case**: u is the DFS root and has 2+ children in DFS tree
  - **Non-root case**: u has a child `v` where `low[v] >= discovery[u]`
- Low-link value: minimum discovery time reachable from the subtree rooted at that node
- Time complexity: O(n + m)
- Space complexity: O(n)

## Related Topics

Articulation Points, Cut Vertices, Tarjan's Algorithm, DFS, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> findArticulationPoints(int n, List<List<Integer>> adj) {
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
        List<Integer> articulationPoints = solution.findArticulationPoints(n, adj);
        
        Collections.sort(articulationPoints);
        
        System.out.println(articulationPoints.size());
        if (!articulationPoints.isEmpty()) {
            for (int i = 0; i < articulationPoints.size(); i++) {
                System.out.print(articulationPoints.get(i));
                if (i < articulationPoints.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def find_articulation_points(n: int, adj: List[List[int]]) -> List[int]:
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
    
    articulation_points = find_articulation_points(n, adj)
    articulation_points.sort()
    
    print(len(articulation_points))
    if articulation_points:
        print(' '.join(map(str, articulation_points)))

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
    vector<int> findArticulationPoints(int n, vector<vector<int>>& adj) {
        // Your implementation here
        return vector<int>();
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
    vector<int> articulationPoints = solution.findArticulationPoints(n, adj);
    
    sort(articulationPoints.begin(), articulationPoints.end());
    
    cout << articulationPoints.size() << "\n";
    if (!articulationPoints.empty()) {
        for (int i = 0; i < articulationPoints.size(); i++) {
            cout << articulationPoints[i];
            if (i < articulationPoints.size() - 1) cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findArticulationPoints(n, adj) {
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
  const articulationPoints = solution.findArticulationPoints(n, adj);
  
  articulationPoints.sort((a, b) => a - b);
  
  console.log(articulationPoints.length);
  if (articulationPoints.length > 0) {
    console.log(articulationPoints.join(" "));
  }
});
```