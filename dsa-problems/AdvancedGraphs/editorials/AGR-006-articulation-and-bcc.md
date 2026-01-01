---
problem_id: AGR_ARTICULATION_AND_BCC__7358
display_id: AGR-006
slug: articulation-and-bcc
title: "Articulation Points and Biconnected Components"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - Articulation Points
  - Biconnected Components
tags:
  - advanced-graphs
  - articulation-points
  - bcc
  - medium
premium: true
subscription_tier: basic
---

# AGR-006: Articulation Points and Biconnected Components

## 📋 Problem Summary

Find all **Articulation Points** (vertices whose removal increases the number of connected components) and **Biconnected Components (BCCs)** (maximal subgraphs such that any two vertices in the subgraph can be connected by at least two vertex-disjoint paths).

## 🌍 Real-World Scenario

**Scenario Title:** The Critical Network Router (SPOF) 🚨

### The Problem
You are auditing a university campus network.
-   **Nodes:** Routers, Switches, and Firewalls.
-   **Edges:** Ethernet or Optical links.
-   **Articulation Point (Cut Vertex):** A "Single Point of Failure" (SPOF). If this specific router crashes (e.g., due to power failure), the network splits into isolated islands. For example, the Main Library might become disconnected from the Internet.
-   **Biconnected Component:** A "Resilient Cluster". Within this cluster, even if any single router fails (unless it effectively disconnects the cluster from the outside), the devices *inside* the cluster can still talk to each other via alternate paths (cycles).

### Why This Matters
-   **Resilience:** Network Architects aim to design topologies with **zero** articulation points (2-connected graphs) so that maintenance on one device doesn't cause an outage.
-   **Maintenance:** Knowing the BCCs allows you to perform upgrades on a router without bringing down the entire subnet, provided you have redundancy.

### Constraints in Real World
-   **Dynamic Changes:** Networks change (link flap). We need a fast static analysis first.
-   **Scale:** ISP backbones have thousands of nodes. A linear time algorithm is essential.

![Real-World Application](../images/AGR-006/real-world-scenario.png)

### From Real World to Algorithm
We need to identify these critical SPOFs (Articulation Points) and the resilient sub-groups (BCCs) using Tarjan's linear time DFS algorithm.

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph Topology:**
```
      (0)
     /   \
   (1)---(2)
    |
    |  <-- Articulation Point (1)
    |
   (3)---(4)
```

-   **Triangle {0, 1, 2}**: If Node 0 fails, 1 & 2 are still connected. If Node 2 fails, 0 & 1 are connected. This is a **BCC**.
-   **Node 1**: Connects the {0,1,2} cluster to the {3,4} cluster. If Node 1 fails, {0,2} cannot reach {3,4}. **Node 1 is an Articulation Point.**
-   **Edge (1, 3)**: A bridge, also forms a BCC of size 2 (just the edge itself).
-   **Line {3, 4}**: Another BCC.

### Algorithm Flow Diagram

```mermaid
graph TD
    Start[Start DFS] --> Visit[Visit Node u]
    Visit --> SetTime[Set tin = low = timer]
    SetTime --> Iterate[Iterate Child v]
    Iterate --> CheckVisited{Is v visited?}
    CheckVisited -- No (Tree Edge) --> PushStack[Push (u,v) to Stack]
    PushStack --> Recurse[DFS(v)]
    Recurse --> UpdateLow[low_u = min(low_u, low_v)]
    UpdateLow --> CheckAP{low_v >= tin_u?}
    CheckAP -- Yes --> FoundAP[Mark u as AP]
    FoundAP --> ExtractBCC[Pop Stack until (u,v) -> New BCC]
    CheckAP -- No --> Continue
    CheckVisited -- Yes (Back Edge) --> UpdateLowBack[low_u = min(low_u, tin_v)]
    UpdateLowBack --> PushStackBack[Push (u,v) to Stack]
    PushStackBack --> Continue
```

## 🎯 Edge Cases to Test

1.  **Star Graph**
    -   Input: Center connected to leaves.
    -   Expected: Center is the *only* AP. Each spoke is a BCC.
2.  **Simple Cycle**
    -   Input: Ring.
    -   Expected: 0 APs. 1 BCC (the whole ring).
3.  **Two Nodes Connected**
    -   Input: `0-1`.
    -   Expected: 0 APs (removing 0 or 1 leaves an empty/connected component). 1 BCC.
4.  **Dumbbell Graph**
    -   Input: Two triangles connected by a bridge.
    -   Expected: The two endpoints of the bridge are APs.

## ✅ Input/Output Clarifications
-   **BCC Definition**: Output BCCs as a list of vertices. Note that vertices like APs will appear in *multiple* BCC lists.
-   **Root Node**: Special case. Root is an AP iff it has **more than 1 child** in the DFS tree (not just graph structure, but the traversal tree).
-   **Order**: APs sorted asc. BCCs can be any order, but internal nodes sorted.

## Naive Approach

### Intuition
Iterate through every vertex $v$. Temporarily remove $v$ and its incident edges. Run BFS/DFS to count connected components. If components > 1 (or > original), $v$ is an AP.

### Complexity Visualization
| Approach | Time Complexity | Feasibility ($N=10^5$) |
|:---------|:---------------:|:----------------------:|
| Naive ($N \times (N+M)$) | $O(N(N+M))$ | $\approx 10^{10}$ ops (TLE ❌) |
| Tarjan's (DFS) | $O(N+M)$ | $\approx 3 \cdot 10^5$ ops (Pass ✅) |

## Optimal Approach (Tarjan's / Hopcroft-Tarjan)

### Key Insight
-   **Low-Link Value**: `low[u]` tracks the highest ancestor reachable via a back-edge from `u`'s subtree.
-   **Condition**: If a child `v` cannot reach back to `u` or above (`low[v] >= tin[u]`), then `u` is the only path for `v` to reach the rest of the graph. Hence, `u` is an AP.
-   **BCC Extraction**: Store edges in a stack. When an AP condition (`low[v] >= tin[u]`) is met, "pop" all edges down to `(u, v)`. These forming a BCC.

### Time Complexity
-   **O(N + M)**: Single pass DFS.

### Space Complexity
-   **O(N + M)**: Stack depth and graph storage.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] visited;
    private List<List<Integer>> adj;
    private Set<Integer> articulationPoints;
    private List<List<Integer>> bccs;
    private Stack<int[]> edgeStack;

    public Object[] articulationAndBcc(int n, int[][] edges) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        tin = new int[n];
        low = new int[n];
        visited = new boolean[n];
        articulationPoints = new TreeSet<>(); // Sorted automatically
        bccs = new ArrayList<>();
        edgeStack = new Stack<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, -1);
                // Pop remaining edges (e.g., if root was part of a BCC)
                if (!edgeStack.isEmpty()) {
                    Set<Integer> component = new HashSet<>();
                    while (!edgeStack.isEmpty()) {
                        int[] e = edgeStack.pop();
                        component.add(e[0]);
                        component.add(e[1]);
                    }
                    bccs.add(new ArrayList<>(component));
                }
            }
        }

        int[] aps = new int[articulationPoints.size()];
        int idx = 0;
        for (int ap : articulationPoints) aps[idx++] = ap;

        return new Object[]{aps, bccs};
    }

    private void dfs(int u, int p) {
        visited[u] = true;
        tin[u] = low[u] = timer++;
        int children = 0;

        for (int v : adj.get(u)) {
            if (v == p) continue;

            if (visited[v]) {
                // Back-edge
                low[u] = Math.min(low[u], tin[v]);
                if (tin[v] < tin[u]) { 
                    edgeStack.push(new int[]{u, v});
                }
            } else {
                // Tree-edge
                edgeStack.push(new int[]{u, v});
                children++;
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);

                // AP Check
                if ((p != -1 && low[v] >= tin[u]) || (p == -1 && children > 1)) {
                    articulationPoints.add(u);
                }
                
                // BCC Extraction
                if (low[v] >= tin[u]) {
                    Set<Integer> bccNodes = new HashSet<>();
                    while (true) {
                        int[] e = edgeStack.pop();
                        bccNodes.add(e[0]);
                        bccNodes.add(e[1]);
                        if (e[0] == u && e[1] == v) break;
                    }
                    bccs.add(new ArrayList<>(bccNodes));
                }
            }
        }
    }
}
```

### Python
```python
import sys

# Increase recursion for deep graphs
sys.setrecursionlimit(300000)

def articulation_and_bcc(n: int, edges: list[tuple[int, int]]):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    tin = [-1] * n
    low = [-1] * n
    timer = 0
    aps = set()
    bccs = []
    stack = []

    def dfs(u, p):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        children = 0

        for v in adj[u]:
            if v == p:
                continue

            if tin[v] != -1:
                # Back-edge
                low[u] = min(low[u], tin[v])
                if tin[v] < tin[u]: 
                    stack.append((u, v))
            else:
                # Tree-edge
                stack.append((u, v))
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])

                # Check AP Condition
                if (p != -1 and low[v] >= tin[u]) or (p == -1 and children > 1):
                    aps.add(u)

                # Check BCC Condition
                if low[v] >= tin[u]:
                    bcc = set()
                    while stack:
                        edge = stack.pop()
                        bcc.add(edge[0])
                        bcc.add(edge[1])
                        if edge == (u, v):
                            break
                    bccs.append(list(bcc))

    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
            # Empty stack for isolated components
            if stack:
                bcc = set()
                while stack:
                    edge = stack.pop()
                    bcc.add(edge[0])
                    bcc.add(edge[1])
                if bcc:
                    bccs.append(list(bcc))

    return sorted(list(aps)), bccs
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <stack>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, low;
    vector<vector<int>> adj;
    set<int> articulationPoints;
    vector<vector<int>> bccs;
    stack<pair<int, int>> edgeStack;

    void dfs(int u, int p) {
        tin[u] = low[u] = timer++;
        int children = 0;

        for (int v : adj[u]) {
            if (v == p) continue;

            if (tin[v] != -1) {
                low[u] = min(low[u], tin[v]);
                if (tin[v] < tin[u]) {
                    edgeStack.push({u, v});
                }
            } else {
                edgeStack.push({u, v});
                children++;
                dfs(v, u);
                low[u] = min(low[u], low[v]);

                if ((p != -1 && low[v] >= tin[u]) || (p == -1 && children > 1)) {
                    articulationPoints.insert(u);
                }

                if (low[v] >= tin[u]) {
                    vector<int> bcc;
                    set<int> uniqueNodes;
                    while (true) {
                        pair<int, int> e = edgeStack.top();
                        edgeStack.pop();
                        uniqueNodes.insert(e.first);
                        uniqueNodes.insert(e.second);
                        if (e == make_pair(u, v)) break;
                    }
                    for (int node : uniqueNodes) bcc.push_back(node);
                    bccs.push_back(bcc);
                }
            }
        }
    }

public:
    pair<vector<int>, vector<vector<int>>> articulationAndBcc(int n, const vector<pair<int, int>>& edges) {
        adj.assign(n, vector<int>());
        for (const auto& e : edges) {
            adj[e.first].push_back(e.second);
            adj[e.second].push_back(e.first);
        }

        tin.assign(n, -1);
        low.assign(n, -1);
        articulationPoints.clear();
        bccs.clear();
        while (!edgeStack.empty()) edgeStack.pop();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i, -1);
                if (!edgeStack.empty()) {
                    vector<int> bcc;
                    set<int> uniqueNodes;
                    while (!edgeStack.empty()) {
                        pair<int, int> e = edgeStack.top();
                        edgeStack.pop();
                        uniqueNodes.insert(e.first);
                        uniqueNodes.insert(e.second);
                    }
                    for (int node : uniqueNodes) bcc.push_back(node);
                    bccs.push_back(bcc);
                }
            }
        }

        vector<int> aps(articulationPoints.begin(), articulationPoints.end());
        return {aps, bccs};
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
    auto res = solution.articulationAndBcc(n, edges);
    const vector<int>& aps = res.first;
    const vector<vector<int>>& bccs = res.second;

    cout << aps.size();
    if (aps.size() > 0) {
        cout << "\n";
        for (int i = 0; i < (int)aps.size(); i++) {
            if (i) cout << ' ';
            cout << aps[i];
        }
    }
    cout << "\n" << bccs.size();
    for (const auto& bcc : bccs) {
        cout << "\n" << bcc.size();
        for (int v : bcc) cout << ' ' << v;
    }
    cout << "\n";
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  articulationAndBcc(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    let timer = 0;
    const aps = new Set();
    const bccs = [];
    const stack = [];

    // Iterative DFS is hard for Tarjan's because we need to process after returning.
    // Given N=200,000, recursion can overflow.
    // However, implementing iterative Tarjan is complex.
    // Use a custom stack to simulate recursion.

    // Frame: { u, p, iterIndex, children }

    const runDFS = (startNode) => {
        const callStack = [{ u: startNode, p: -1, idx: 0, children: 0 }];
        tin[startNode] = low[startNode] = timer++;

        while (callStack.length > 0) {
            const frame = callStack[callStack.length - 1];
            const u = frame.u;
            const p = frame.p;

            if (frame.idx < adj[u].length) {
                const v = adj[u][frame.idx];
                frame.idx++;

                if (v === p) continue;

                if (tin[v] !== -1) {
                    low[u] = Math.min(low[u], tin[v]);
                    if (tin[v] < tin[u]) {
                        stack.push([u, v]);
                    }
                } else {
                    stack.push([u, v]);
                    frame.children++;
                    // Push new frame
                    tin[v] = low[v] = timer++;
                    callStack.push({ u: v, p: u, idx: 0, children: 0 });
                }
            } else {
                // Post-order
                callStack.pop();
                if (p !== -1) {
                    // Update parent
                    const parentFrame = callStack[callStack.length - 1];
                    low[p] = Math.min(low[p], low[u]);

                    if (low[u] >= tin[p]) {
                        if (p !== startNode) aps.add(p);
                        const bcc = new Set();
                        while (stack.length > 0) {
                            const edge = stack.pop();
                            bcc.add(edge[0]);
                            bcc.add(edge[1]);
                            if (edge[0] === p && edge[1] === u) break;
                        }
                        bccs.push(Array.from(bcc));
                    }
                } else {
                    // Root
                    if (frame.children > 1) {
                        aps.add(startNode);
                    }
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (tin[i] === -1) {
            runDFS(i);
            if (stack.length > 0) {
                const bcc = new Set();
                while (stack.length > 0) {
                    const edge = stack.pop();
                    bcc.add(edge[0]);
                    bcc.add(edge[1]);
                }
                bccs.push(Array.from(bcc));
            }
        }
    }

    const sortedAps = Array.from(aps).sort((a, b) => a - b);
    return [sortedAps, bccs];
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
  const [aps, bccs] = solution.articulationAndBcc(n, edges);

  const out = [aps.length.toString()];
  if (aps.length > 0) out.push(aps.join(" "));

  out.push(bccs.length.toString());
  for (const b of bccs) {
    b.sort((p, q) => p - q);
    out.push(`${b.length} ${b.join(" ")}`.trim());
  }

  // Handle empty line logic for aps
  if (aps.length === 0) {
      // 0 APs, output starts with "0", then BCC count line immediately
  }

  console.log(out.join("\n").trim());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
4 4
0 1
1 2
2 0
1 3
```

### Execution Table

| Step | Node | Event | Stack State | `tin`/`low` | Logic |
|-----:|:----:|:------|:------------|:------------|:------|
| 1 | 0 | Visit | | `0/0` | Start Root |
| 2 | 1 | Visit | `(0,1)` | `1/1` | Tree Edge |
| 3 | 2 | Visit | `(0,1),(1,2)` | `2/2` | Tree Edge |
| 4 | 0 | Back-edge | `(0,1),(1,2),(2,0)` | `0/0` | `low[2]=0` |
| 5 | 2 | Return | | | `low[1] = min(1, 0) = 0` |
| 6 | 3 | Visit | `..,(1,3)` | `3/3` | Tree Edge |
| 7 | 3 | Return | | | `low[3]=3` |
| 8 | 1 | Check(3) | | | `low[3] (3) >= tin[1] (1)`. **AP: 1**. Pop BCC `{1,3}`. |
| 9 | 1 | Return | | | `low[0] = min(0, 0) = 0` |
| 10 | 0 | Check(1) | | | `low[1] (0) >= tin[0] (0)`. Root Check: Children=1. Not AP. Pop BCC `{0,1,2}`. |

**Output:**
APs: `1`
BCCs: `{1, 3}`, `{0, 1, 2}`

## ✅ Proof of Correctness

### Articulation Points
The DFS tree property ensures that for any node $u$ and its child $v$, if there is no back-edge from $v$'s subtree to $u$'s ancestor, then removing $u$ disconnects $v$ from the "upper" part of the tree. `low[v] >= tin[u]` precisely checks this condition.

### Biconnected Components
Edges are stored on a stack in visitation order. When an AP is identified at `u` due to child `v`, all edges pushed since `(u, v)` (inclusive) belong to the BCC "below" `v`. Popping them isolates this component correctly.

## ⚠️ Common Mistakes to Avoid

1.  **Wrong Root Logic**: Root is an AP only if `children > 1`. `low[v] >= tin[u]` is always true for root children, so standard check fails.
2.  **Outputting Edges instead of Nodes**: BCCs are edge sets, but problem asks for node sets. Use a Set/Hash to collect unique nodes from popped edges.
3.  **Forgetting Back-Edges**: Back-edges are vital parts of BCCs. Push them to the stack too!
4.  **Handling Disconnected Graphs**: Always loop `0..N-1` to cover forests.

## 💡 Interview Extensions

1.  **Block-Cut Tree**: Using BCCs and APs, you can build a new tree where nodes are either original APs or BCC "super-nodes". This tree captures the connectivity structure.
2.  **Edge-Biconnectivity (2-ECC)**: Related but different. 2-ECC relates to bridges, BCC relates to APs. A graph can be 2-edge-connected but not biconnected (e.g., dumbbell graph).
3.  **Strongly Connected Components (SCC)**: Directed graph version (Tarjan’s/Kosaraju).

## Related Concepts
-   **Bridges**: Similar `low` link logic. `low[v] > tin[u]`.
-   **Tarjan's SCC**: Also uses `low` link but for directed cyclic components.
-   **Spanning Trees**: DFS tree is a spanning tree.
