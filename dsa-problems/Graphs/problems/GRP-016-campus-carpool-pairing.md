---
problem_id: GRP_CAMPUS_CARPOOL_PAIRING__2914
display_id: GRP-016
slug: campus-carpool-pairing
title: "Campus Carpool Pairing"
difficulty: Medium
difficulty_score: 45
topics:
  - Graph Theory
  - Cycle Detection
  - Union-Find
  - Forest
tags:
  - graph
  - cycle-detection
  - union-find
  - forest
  - tree
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-016: Campus Carpool Pairing

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1) and `m` edges, determine if the graph is a **forest**.

A **forest** is a graph with no cycles. Equivalently, it's a collection of trees where each tree is a connected acyclic graph. An isolated node (with no edges) is considered a tree of size 1.

Return `true` if the graph is a forest (has no cycles), `false` otherwise.

![Problem Illustration](../images/GRP-016/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single word: `true` if the graph is a forest (no cycles), `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**
```
3
2
0 1
1 2
```

**Output:**
```
true
```

**Explanation:**

Graph structure:
```
0 --- 1 --- 2
```

This is a simple path (a tree) with no cycles, so it's a forest.

Output: `true`

![Example Visualization](../images/GRP-016/example-1.png)

## Notes

- A forest has no cycles
- For a graph to be a forest, it must satisfy: `m < n` (number of edges < number of nodes)
- If `m >= n`, at least one cycle must exist (pigeonhole principle)
- Use Union-Find (DSU) to detect cycles:
  - Process each edge (u, v)
  - If u and v are already in the same component, adding this edge creates a cycle
  - If they're in different components, union them
- Alternatively, use DFS with parent tracking (same as undirected cycle detection)
- Time complexity: O(m × α(n)) for Union-Find, O(n + m) for DFS

## Related Topics

Forest, Trees, Cycle Detection, Union-Find, DFS, Acyclic Graph

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean isForest(int n, List<int[]> edges) {
        // Your implementation here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            edges.add(new int[]{u, v});
        }
        
        Solution solution = new Solution();
        System.out.println(solution.isForest(n, edges));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def is_forest(n: int, edges: List[tuple]) -> bool:
    # Your implementation here
    return False

def main():
    n = int(input())
    m = int(input())
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    result = is_forest(n, edges)
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
    bool isForest(int n, vector<pair<int,int>>& edges) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<pair<int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }
    
    Solution solution;
    cout << (solution.isForest(n, edges) ? "true" : "false") << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  isForest(n, edges) {
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
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    edges.push([u, v]);
  }
  
  const solution = new Solution();
  console.log(solution.isForest(n, edges) ? "true" : "false");
});
```