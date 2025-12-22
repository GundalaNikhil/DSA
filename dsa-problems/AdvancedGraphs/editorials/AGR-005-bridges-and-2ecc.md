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
---

# AGR-005: Bridges and 2-Edge-Connected Components

## 📋 Problem Summary

Identify all **bridges** in a graph and partition the vertices into **2-Edge-Connected Components (2ECCs)**. A 2ECC is a subgraph where removing any single edge does not disconnect the subgraph.

## 🌍 Real-World Scenario

**Scenario Title:** Critical Infrastructure Links

Imagine a network of islands connected by bridges.
-   **Bridge (Graph Term):** A literal bridge that, if destroyed, makes it impossible to travel between two parts of the map.
-   **2ECC:** A group of islands that are "robustly" connected. Even if one bridge within the group fails, there's always an alternative route (a cycle) to keep them connected.
-   **Goal:** Identify the critical vulnerabilities (bridges) and the safe zones (2ECCs).

![Real-World Application](../images/AGR-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    (0) --- (1)
     |       |
     \       /
      \     /
        (2)
         |
         |  <-- Bridge
         |
        (3) --- (4)
```
-   **Cycle:** 0-1-2-0. No single edge removal disconnects {0, 1, 2}.
-   **Bridge:** Edge (2, 3). Removing it separates {0, 1, 2} from {3, 4}.
-   **Edge (3, 4):** Is it a bridge? Yes, removing it isolates 4.
-   **2ECCs:**
    1.  `{0, 1, 2}` (Robust)
    2.  `{3}` (Single node)
    3.  `{4}` (Single node)

### Algorithm: Tarjan's Bridge-Finding + Component Labeling

1.  **Find Bridges:**
    -   Use **DFS** with `tin` (time of insertion) and `low` (lowest `tin` reachable via back-edge).
    -   For edge `u -> v`:
        -   If `v` is parent, ignore.
        -   If `v` visited, `low[u] = min(low[u], tin[v])`.
        -   If `v` unvisited:
            -   DFS(v).
            -   `low[u] = min(low[u], low[v])`.
            -   If `low[v] > tin[u]`, then `(u, v)` is a **bridge**.
2.  **Find 2ECCs:**
    -   Remove all bridges from the graph.
    -   Run a traversal (DFS/BFS) or use DSU on the remaining edges.
    -   All nodes in a connected component form a 2ECC.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Parallel Edges:** The problem doesn't explicitly forbid them. If parallel edges exist between `u` and `v`, `(u, v)` is NOT a bridge (unless all but one are removed, but here we consider the static graph). Standard logic: pass edge index to DFS to distinguish parallel edges.
-   **Output Order:** Bridges must be printed in the order they appear in the input. Store `is_bridge[edge_index]`.
-   **Component IDs:** 1-based.

## Naive Approach

### Intuition

For every edge, remove it, run BFS to check connectivity. If disconnected, it's a bridge.

### Time Complexity

-   **O(M * (N + M))**: Too slow for M=200,000.

## Optimal Approach (DFS Low-Link)

### Time Complexity

-   **O(N + M)**: One DFS pass for bridges, one pass for components.

### Space Complexity

-   **O(N + M)**: Recursion stack and adjacency list.

## Implementations

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
        int m = edges.length;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(new int[]{edges[i][1], i});
            adj.get(edges[i][1]).add(new int[]{edges[i][0], i});
        }

        tin = new int[n];
        low = new int[n];
        visited = new boolean[n];
        bridgeFlags = new int[m];
        timer = 0;

        // 1. Find Bridges
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfsBridges(i, -1);
            }
        }

        // 2. Find Components (DFS ignoring bridges)
        int[] comp = new int[n];
        int compCount = 0;
        Arrays.fill(visited, false); // Reuse visited array

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                compCount++;
                dfsComponents(i, compCount, comp);
            }
        }

        return new int[][]{bridgeFlags, comp};
    }

    private void dfsBridges(int u, int pEdgeIndex) {
        visited[u] = true;
        tin[u] = low[u] = timer++;
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int idx = edge[1];
            if (idx == pEdgeIndex) continue; // Don't go back through same edge

            if (visited[v]) {
                low[u] = Math.min(low[u], tin[v]);
            } else {
                dfsBridges(v, idx);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > tin[u]) {
                    bridgeFlags[idx] = 1;
                }
            }
        }
    }

    private void dfsComponents(int u, int c, int[] comp) {
        visited[u] = true;
        comp[u] = c;
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int idx = edge[1];
            if (bridgeFlags[idx] == 1) continue; // Don't cross bridges
            if (!visited[v]) {
                dfsComponents(v, c, comp);
            }
        }
    }
}

public class Main {
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
    m = len(edges)
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        
    tin = [-1] * n
    low = [-1] * n
    bridge_flags = [0] * m
    timer = 0
    
    def dfs_bridges(u, p_edge_idx):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        
        for v, idx in adj[u]:
            if idx == p_edge_idx:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs_bridges(v, idx)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridge_flags[idx] = 1
                    
    for i in range(n):
        if tin[i] == -1:
            dfs_bridges(i, -1)
            
    # Find components
    comp = [0] * n
    comp_count = 0
    visited = [False] * n
    
    def dfs_comp(u, c):
        visited[u] = True
        comp[u] = c
        for v, idx in adj[u]:
            if bridge_flags[idx]:
                continue
            if not visited[v]:
                dfs_comp(v, c)
                
    for i in range(n):
        if not visited[i]:
            comp_count += 1
            dfs_comp(i, comp_count)
            
    return bridge_flags, comp

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
        visited[u] = true;
        tin[u] = low[u] = timer++;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int idx = edge.second;
            if (idx == pEdgeIndex) continue;
            if (visited[v]) {
                low[u] = min(low[u], tin[v]);
            } else {
                dfsBridges(v, idx);
                low[u] = min(low[u], low[v]);
                if (low[v] > tin[u]) {
                    bridgeFlags[idx] = 1;
                }
            }
        }
    }

    void dfsComponents(int u, int c) {
        comp[u] = c;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int idx = edge.second;
            if (bridgeFlags[idx]) continue;
            if (comp[v] == 0) {
                dfsComponents(v, c);
            }
        }
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
    const m = edges.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < m; i++) {
      const [u, v] = edges[i];
      adj[u].push({ to: v, idx: i });
      adj[v].push({ to: u, idx: i });
    }

    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const bridgeFlags = new Int8Array(m).fill(0);
    let timer = 0;

    // Use iterative DFS to avoid stack overflow
    const parentEdge = new Int32Array(n).fill(-1);
    const stack = [];
    
    // Recursive is cleaner for logic, but JS stack is small.
    // Let's use recursion but warn about stack size? 
    // N=200,000 requires iterative.
    
    // Iterative DFS for Bridges
    // We need to process node in post-order to update low-link.
    // Stack stores {u, iter_index}
    
    const visited = new Int8Array(n).fill(0);
    
    const runDFS = (startNode) => {
        const stack = [startNode];
        const iterIndex = new Int32Array(n).fill(0);
        visited[startNode] = 1;
        tin[startNode] = low[startNode] = timer++;
        
        while (stack.length > 0) {
            const u = stack[stack.length - 1];
            const children = adj[u];
            
            if (iterIndex[u] < children.length) {
                const { to: v, idx } = children[iterIndex[u]];
                iterIndex[u]++;
                
                if (idx === parentEdge[u]) continue;
                
                if (visited[v]) {
                    low[u] = Math.min(low[u], tin[v]);
                } else {
                    visited[v] = 1;
                    tin[v] = low[v] = timer++;
                    parentEdge[v] = idx;
                    stack.push(v);
                }
            } else {
                // Post-order processing
                stack.pop();
                if (parentEdge[u] !== -1) {
                    // We came from some parent via parentEdge[u]
                    // We need to find who is the parent node.
                    // But simpler: we need to update parent's low.
                    // In iterative DFS, parent is now at top of stack (if stack not empty)
                    if (stack.length > 0) {
                        const p = stack[stack.length - 1];
                        low[p] = Math.min(low[p], low[u]);
                        if (low[u] > tin[p]) {
                            bridgeFlags[parentEdge[u]] = 1;
                        }
                    }
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (!visited[i]) runDFS(i);
    }

    // Components
    const comp = new Int32Array(n).fill(0);
    let compCount = 0;
    
    const runCompDFS = (startNode, c) => {
        const stack = [startNode];
        comp[startNode] = c;
        while(stack.length > 0) {
            const u = stack.pop();
            for(const {to: v, idx} of adj[u]) {
                if(bridgeFlags[idx]) continue;
                if(comp[v] === 0) {
                    comp[v] = c;
                    stack.push(v);
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (comp[i] === 0) {
            compCount++;
            runCompDFS(i, compCount);
        }
    }

    return [bridgeFlags, comp];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4
0 1
1 2
2 0
2 3
```
**DFS Trace:**
1.  Start at 0. `tin[0]=0`.
2.  Go to 1. `tin[1]=1`.
3.  Go to 2. `tin[2]=2`.
4.  From 2, see 0 (visited). `low[2] = min(2, tin[0]=0) = 0`.
5.  From 2, see 3. `tin[3]=3`.
6.  From 3, no neighbors. Return. `low[3]=3`.
7.  Back at 2. `low[2] = min(0, 3) = 0`. Check bridge: `low[3] (3) > tin[2] (2)`? Yes. **(2,3) is Bridge**.
8.  Back at 1. `low[1] = min(1, low[2]=0) = 0`. Check bridge: `low[2] (0) > tin[1] (1)`? No.
9.  Back at 0. `low[0] = min(0, low[1]=0) = 0`. Check bridge: `low[1] (0) > tin[0] (0)`? No.

**Components:**
-   Remove (2,3).
-   Start BFS at 0 -> 1 -> 2. Comp 1.
-   Start BFS at 3. Comp 2.
-   Result: `1 1 1 2`.

## ✅ Proof of Correctness

-   **Bridges:** An edge `(u, v)` is a bridge iff there is no back-edge from the subtree of `v` to `u` or an ancestor of `u`. This is captured by `low[v] > tin[u]`.
-   **2ECC:** By definition, 2ECCs are components formed by removing all bridges. Our algorithm does exactly this.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Bridge Tree:** If we contract each 2ECC into a single node, the resulting structure is a tree (the Bridge Tree). This is useful for path queries.
-   **Articulation Points:** Similar logic (`low[v] >= tin[u]`), but for vertices.
-   **Dynamic Bridges:** Maintaining bridges under edge insertions/deletions (fully dynamic graph algorithms).

### Common Mistakes to Avoid

1.  **Parent Edge:** In undirected graphs, do not go back to the parent immediately. Pass `parentEdgeIndex` to distinguish parallel edges.
2.  **Disconnected Graph:** The graph might not be connected. Run DFS on all unvisited nodes.
3.  **Output Order:** Bridges must be printed in input order. Don't just print `u v` as you find them; store flags.
