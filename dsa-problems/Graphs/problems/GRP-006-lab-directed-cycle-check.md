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

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        // Your implementation here
        return false;
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
        }
        
        Solution solution = new Solution();
        System.out.println(solution.hasCycle(n, adj));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def has_cycle(n: int, adj: List[List[int]]) -> bool:
    # Your implementation here
    return False

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    
    result = has_cycle(n, adj)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool hasCycle(int n, vector<vector<int>>& adj) {
        // Your implementation here
        return false;
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
    }
    
    Solution solution;
    cout << (solution.hasCycle(n, adj) ? "true" : "false") << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasCycle(n, adj) {
    // Your implementation here
    return false;
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
  }
  
  const solution = new Solution();
  console.log(solution.hasCycle(n, adj) ? "true" : "false");
});
```
