---
problem_id: GRP_LAB_NETWORK_DFS__5729
display_id: GRP-002
slug: lab-network-dfs
title: "Lab Network DFS"
difficulty: Easy
difficulty_score: 25
topics:
  - Graph Traversal
  - Depth-First Search
  - Recursion
tags:
  - graph
  - dfs
  - traversal
  - recursion
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-002: Lab Network DFS

## Problem Statement

Given an undirected graph represented by `n` nodes (numbered from 0 to n-1) and an adjacency list, perform a Depth-First Search (DFS) in preorder starting from node 0 and return the visited nodes in the order they were first encountered.

DFS explores as far as possible along each branch before backtracking. The preorder means we record a node when we first visit it, not when we backtrack from it.

![Problem Illustration](../images/GRP-002/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single line with space-separated integers representing the preorder DFS traversal starting from node 0

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- The graph may be disconnected
- There are no self-loops or multiple edges

## Example

**Input:**
```
5
3
0 1
0 2
1 4
```

**Output:**
```
0 1 4 2
```

**Explanation:**

Starting from node 0:
- Visit node 0 (record it)
- Go to neighbor 1 (first neighbor in adjacency list)
- Visit node 1 (record it)
- Go to neighbor 4 (only unvisited neighbor of 1)
- Visit node 4 (record it)
- Backtrack to 1, then to 0
- Go to neighbor 2 (next unvisited neighbor of 0)
- Visit node 2 (record it)

The DFS preorder traversal is: 0 → 1 → 4 → 2

![Example Visualization](../images/GRP-002/example-1.png)

## Notes

- Can be implemented recursively (using call stack) or iteratively (using explicit stack)
- Use a visited array/set to track which nodes have been explored
- If the graph is disconnected, only nodes reachable from node 0 will be visited
- The order of neighbors in the adjacency list determines which branch to explore first
- Preorder means recording the node when first visited, not during backtracking

## Related Topics

Graph Traversal, DFS, Recursion, Stack, Backtracking

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private List<Integer> result;
    private boolean[] visited;
    
    public List<Integer> dfsTraversal(int n, List<List<Integer>> adj) {
        return null;
    }
    
    private void dfs(int node, List<List<Integer>> adj) {
        // Mark as visited and add to result (preorder)
        visited[node] = true;
        result.add(node);
        
        // Recursively visit all unvisited neighbors
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj);
            }
        }
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
        List<Integer> result = solution.dfsTraversal(n, adj);
        
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
sys.setrecursionlimit(200000)
from typing import List

def dfs_traversal(n: int, adj: List[List[int]]) -> List[int]:
    return []
def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    result = dfs_traversal(n, adj)
    print(' '.join(map(str, result)))

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
    vector<int> result;
    vector<bool> visited;
    
    void dfs(int node, vector<vector<int>>& adj) {
    }
    
public:
    vector<int> dfsTraversal(int n, vector<vector<int>>& adj) {
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
    vector<int> result = solution.dfsTraversal(n, adj);
    
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
  dfsTraversal(n, adj) {
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
  const result = solution.dfsTraversal(n, adj);
  console.log(result.join(" "));
});
```

