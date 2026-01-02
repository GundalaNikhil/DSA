---
problem_id: AGR_BRIDGES_AND_2ECC__3471
display_id: AGR-005
slug: bridges-and-2ecc
title: "Bridges and 2-Edge-Connected Components"
difficulty: Medium
difficulty_score: 54
topics:
  - Graphs
  - Bridges
  - Components
tags:
  - advanced-graphs
  - bridges
  - components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-005: Bridges and 2-Edge-Connected Components
## Problem Statement
Given an undirected graph, find all bridges and compute the 2-edge-connected components (2ECCs). A 2ECC is a maximal set of nodes that stays connected after removing any single edge.
![Problem Illustration](../images/AGR-005/problem-illustration.png)
## Input Format
- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge
## Output Format
- Line 1: integer `b`, number of bridges
- Next `b` lines: each bridge edge `u v` in input order
- Last line: `n` integers `comp[i]` (1-based component id)
## Constraints
- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
## Example
**Input:**
```
4 4
0 1
1 2
2 0
2 3
```
**Output:**
```
1
2 3
1 1 1 2
```
**Explanation:**
Edge (2,3) is a bridge. Nodes {0,1,2} form one 2ECC, node {3} is another.
![Example Visualization](../images/AGR-005/example-1.png)
## Notes
- Use DFS low-link to detect bridges.
- Build components by unioning all non-bridge edges.
- Output bridge edges in their input order.
## Related Topics
Bridges, 2-Edge-Connected Components, DFS
---
## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] visited;
    private int[] bridgeFlags; // 1 if edge i is bridge
    private List<List<int[]>> adj; // {neighbor, edgeIndex}

    public int[][] bridgesAndComponents(int n, int[][] edges) {
        return null;
    }

    private void dfsBridges(int u, int pEdgeIndex) {
    }

    private void dfsComponents(int u, int c, int[] comp) {
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[][] result = solution.bridgesAndComponents(n, edges);
        int[] bridgeFlags = result[0];
        int[] comp = result[1];

        int bridgeCount = 0;
        for (int f : bridgeFlags) bridgeCount += f;

        StringBuilder sb = new StringBuilder();
        sb.append(bridgeCount).append('\n');
        for (int i = 0; i < m; i++) {
            if (bridgeFlags[i] == 1) {
                sb.append(edges[i][0]).append(' ').append(edges[i][1]).append('\n');
            }
        }
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def bridges_and_components(n: int, edges: list[tuple[int, int]]):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        bridge_flags, comp = bridges_and_components(n, edges)
        
        out = [str(sum(bridge_flags))]
        for i, f in enumerate(bridge_flags):
            if f:
                out.append(f"{edges[i][0]} {edges[i][1]}")
        out.append(" ".join(map(str, comp)))
        sys.stdout.write("\n".join(out))
    except StopIteration:
        pass

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
    int timer;
    vector<int> tin, low;
    vector<int> bridgeFlags;
    vector<vector<pair<int, int>>> adj; // {neighbor, edgeIndex}
    vector<int> comp;
    vector<bool> visited;

    void dfsBridges(int u, int pEdgeIndex) {
    }

    void dfsComponents(int u, int c) {
    }

public:
    pair<vector<int>, vector<int>> bridgesAndComponents(int n, const vector<pair<int, int>>& edges) {
        int m = edges.size();
        adj.assign(n, vector<pair<int, int>>());
        for (int i = 0; i < m; i++) {
            adj[edges[i].first].push_back({edges[i].second, i});
            adj[edges[i].second].push_back({edges[i].first, i});
        }

        tin.assign(n, -1);
        low.assign(n, -1);
        visited.assign(n, false);
        bridgeFlags.assign(m, 0);
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfsBridges(i, -1);
            }
        }

        comp.assign(n, 0);
        int compCount = 0;
        for (int i = 0; i < n; i++) {
            if (comp[i] == 0) {
                compCount++;
                dfsComponents(i, compCount);
            }
        }

        return {bridgeFlags, comp};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    auto res = solution.bridgesAndComponents(n, edges);
    const vector<int>& bridgeFlags = res.first;
    const vector<int>& comp = res.second;

    int bridgeCount = 0;
    for (int f : bridgeFlags) bridgeCount += f;

    cout << bridgeCount << "\n";
    for (int i = 0; i < m; i++) {
        if (bridgeFlags[i]) {
            cout << edges[i].first << ' ' << edges[i].second << "\n";
        }
    }
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bridgesAndComponents(n, edges) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const [bridgeFlags, comp] = solution.bridgesAndComponents(n, edges);
  
  let bridgeCount = 0;
  for (let i = 0; i < m; i++) bridgeCount += bridgeFlags[i];
  
  const out = [bridgeCount.toString()];
  for (let i = 0; i < m; i++) {
    if (bridgeFlags[i]) out.push(`${edges[i][0]} ${edges[i][1]}`);
  }
  out.push(comp.join(" "));
  console.log(out.join("\n"));
});
```

