---
problem_id: GRP_BATTERY_ARCHIPELAGO__3928
display_id: GRP-010
slug: battery-archipelago-analyzer
title: "Battery Archipelago Analyzer"
difficulty: Medium-Hard
difficulty_score: 65
topics:
  - Shortest Path
  - Dijkstra Variant
  - Custom Constraints
tags:
  - graph
  - dijkstra
  - shortest-path
  - constraints
  - hard
premium: true
subscription_tier: premium
time_limit: 2000
memory_limit: 256
---

# GRP-010: Battery Archipelago Analyzer

## Problem Statement

Given a weighted undirected graph with `n` nodes and a battery constraint, find the shortest path from source `s` to destination `d` such that no single edge weight exceeds the battery capacity `B`.

Each edge has a weight representing the energy/distance required. You can only traverse an edge if its weight is <= B. Among all valid paths (paths where every edge weight <= B), find the one with minimum total cost.

Return the minimum total cost, or `-1` if no valid path exists.

![Problem Illustration](../images/GRP-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of undirected edges)
- Next `m` lines: three integers `u v w` representing an undirected edge between `u` and `v` with weight `w`
- Last line: three integers `s d B` (source, destination, battery capacity)

## Output Format

- Single integer: minimum cost from `s` to `d` using only edges with weight <= B, or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `1 <= w <= 10^6`
- `0 <= s, d < n`
- `1 <= B <= 10^6`

## Example

**Input:**
```
4
5
0 1 10
0 2 50
1 2 20
1 3 30
2 3 5
0 3 25
```

**Output:**
```
35
```

**Explanation:**

Battery capacity B = 25

Available paths from 0 to 3:
- Direct 0→3: NOT VALID (edge weight 30 > 25)
- Path 0→1→3: cost = 10+30 = NOT VALID (edge 1→3 has weight 30 > 25)
- Path 0→2→3: NOT VALID (edge 0→2 has weight 50 > 25)
- Path 0→1→2→3: cost = 10+20+5 = 35 (all edges <= 25) ✓
- Path 0→1→3: cost = 10+30 = 40 (edge 1→3 has weight 30 > 25) ❌
- Path 0→2→3: cost = 50+5 = 55 (edge 0→2 has weight 50 > 25) ❌

The minimum valid path with all edges <= 25 has total cost 35.

![Example Visualization](../images/GRP-010/example-1.png)

## Notes

- Modified Dijkstra: only consider edges with weight <= B
- Filter the adjacency list before running Dijkstra to exclude heavy edges
- Alternatively, modify Dijkstra to skip edges with weight > B during relaxation
- Time complexity: O((n + m) log n)
- This is a constrained shortest path problem

## Related Topics

Dijkstra's Algorithm, Constrained Shortest Path, Graph Filtering, Weighted Graph

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int shortestPathWithBattery(int n, List<int[]> edges, int source, int dest, int battery) {
        // Your implementation here
        return -1;
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
            int w = sc.nextInt();
            edges.add(new int[]{u, v, w});
        }
        
        int source = sc.nextInt();
        int dest = sc.nextInt();
        int battery = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.shortestPathWithBattery(n, edges, source, dest, battery));
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def shortest_path_with_battery(n: int, edges: List[Tuple[int, int, int]], 
                                source: int, dest: int, battery: int) -> int:
    # Your implementation here
    return -1

def main():
    n = int(input())
    m = int(input())
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    s, d, B = map(int, input().split())
    
    result = shortest_path_with_battery(n, edges, s, d, B)
    print(result)

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
    int shortestPathWithBattery(int n, vector<vector<int>>& edges, int source, int dest, int battery) {
        // Your implementation here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }
    
    int source, dest, battery;
    cin >> source >> dest >> battery;
    
    Solution solution;
    cout << solution.shortestPathWithBattery(n, edges, source, dest, battery) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestPathWithBattery(n, edges, source, dest, battery) {
    // Your implementation here
    return -1;
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
    const [u, v, w] = data[ptr++].split(" ").map(Number);
    edges.push([u, v, w]);
  }
  
  const [source, dest, battery] = data[ptr++].split(" ").map(Number);
  
  const solution = new Solution();
  console.log(solution.shortestPathWithBattery(n, edges, source, dest, battery));
});
```
