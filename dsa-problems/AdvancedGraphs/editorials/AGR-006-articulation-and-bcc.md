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

**Scenario Title:** Single Points of Failure in Networks

In a communication network:

- **Articulation Point:** A critical router or server. If it crashes, the network splits into disconnected parts. Identifying these is crucial for reliability engineering.
- **BCC:** A "safe zone". Within a BCC, even if one router fails (other than the source/destination), there is always an alternative path.
- **Goal:** Harden the network by adding links to eliminate articulation points.

![Real-World Application](../images/AGR-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**

```
    (0) --- (1) --- (3)
     |       |
     \       /
      \     /
        (2)
```

- **Triangle {0, 1, 2}:** Removing any single node (0, 1, or 2) leaves the other two connected. This is a BCC.
- **Edge {1, 3}:** Removing 1 disconnects 3. Removing 3 disconnects nothing. This edge forms a BCC `{1, 3}`.
- **Articulation Point:** Node 1. It connects the triangle to node 3.
- **Note:** Node 1 belongs to _both_ BCCs.

### Algorithm: Tarjan's / Hopcroft-Tarjan

1.  **DFS Traversal:** Maintain `tin` (discovery time) and `low` (lowest reachable ancestor).
2.  **Edge Stack:** Push every visited edge `(u, v)` onto a stack.
3.  **AP Condition:** For a tree edge `u -> v`:
    - If `low[v] >= tin[u]`, then `u` is an Articulation Point (unless `u` is root and has < 2 children).
    - **Extract BCC:** When `low[v] >= tin[u]`, pop edges from the stack until `(u, v)` is popped. All vertices in these edges form a BCC.
4.  **Root Case:** The root of the DFS tree is an AP if and only if it has more than one child in the DFS tree.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **BCC Format:** A BCC is a set of vertices. Since an edge belongs to exactly one BCC, but a vertex can belong to multiple, we extract BCCs as sets of edges and then collect unique vertices.
- **Output:** APs sorted. BCCs in any order.
- **Disconnected Graph:** Handle by running DFS on all unvisited nodes.

## Naive Approach

### Intuition

For each vertex, remove it and check connectivity (O(N\*(N+M))). For BCCs, iterate all pairs? Too slow.

## Optimal Approach (DFS with Stack)

### Time Complexity

- **O(N + M)**: Single DFS pass.

### Space Complexity

- **O(N + M)**: Recursion stack, edge stack, adjacency list.

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
        articulationPoints = new TreeSet<>(); // Sorted
        bccs = new ArrayList<>();
        edgeStack = new Stack<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, -1);
                // If stack not empty after DFS (e.g. isolated edge or component), pop remaining
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
                low[u] = Math.min(low[u], tin[v]);
                if (tin[v] < tin[u]) { // Back-edge
                    edgeStack.push(new int[]{u, v});
                }
            } else {
                edgeStack.push(new int[]{u, v});
                children++;
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);

                if ((p != -1 && low[v] >= tin[u]) || (p == -1 && children > 1)) {
                    articulationPoints.add(u);
                }

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
        Object[] res = solution.articulationAndBcc(n, edges);
        int[] aps = (int[]) res[0];
        @SuppressWarnings("unchecked")
        List<List<Integer>> bccs = (List<List<Integer>>) res[1];

        StringBuilder sb = new StringBuilder();
        sb.append(aps.length);
        if (aps.length > 0) {
            sb.append('\n');
            for (int i = 0; i < aps.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(aps[i]);
            }
        }
        sb.append('\n').append(bccs.size());
        for (List<Integer> bcc : bccs) {
            sb.append('\n').append(bcc.size());
            for (int v : bcc) sb.append(' ').append(v);
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
                low[u] = min(low[u], tin[v])
                if tin[v] < tin[u]: # Back-edge
                    stack.append((u, v))
            else:
                stack.append((u, v))
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if (p != -1 and low[v] >= tin[u]) or (p == -1 and children > 1):
                    aps.add(u)

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
            if stack: # Should be empty if logic is correct, but for safety
                bcc = set()
                while stack:
                    edge = stack.pop()
                    bcc.add(edge[0])
                    bcc.add(edge[1])
                if bcc:
                    bccs.append(list(bcc))

    return sorted(list(aps)), bccs

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

        aps, bccs = articulation_and_bcc(n, edges)

        out = [str(len(aps))]
        if aps:
            out.append(" ".join(map(str, aps)))
        else:
            out.append("")
        out.append(str(len(bccs)))
        for b in bccs:
            out.append(f"{len(b)} " + " ".join(map(str, b)))

        # Clean up empty line if aps is empty
        if not aps:
            # Remove the empty string added
            out.pop(1)
            pass

        sys.stdout.write("\n".join(out).strip())
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
                        aps.add(p);
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
  const [aps, bccs] = solution.articulationAndBcc(n, edges);

  const out = [aps.length.toString()];
  if (aps.length > 0) out.push(aps.join(" "));
  else out.push("");

  out.push(bccs.length.toString());
  for (const b of bccs) {
    out.push(``b.length`{b.join(" ")}`.trim());
  }

  // Handle empty line logic for aps
  if (aps.length === 0) {
      // out has ["0", "", "numBCC", ...]
      // join("\n") gives "0\n\nnumBCC..."
      // This is correct.
  }

  console.log(out.join("\n").trim());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
4 4
0 1
1 2
2 0
1 3
```

**DFS Trace:**

1.  Start 0. `tin[0]=0`. Stack: `[]`.
2.  Edge `0-1`. `tin[1]=1`. Stack: `[(0,1)]`.
3.  Edge `1-2`. `tin[2]=2`. Stack: `[(0,1), (1,2)]`.
4.  Edge `2-0`. Back-edge. `low[2]=0`. Stack: `[(0,1), (1,2), (2,0)]`.
5.  Return to 1. `low[1]=0`. `low[2] (0) < tin[1] (1)`, so 1 is NOT AP via 2.
6.  Edge `1-3`. `tin[3]=3`. Stack: `[..., (1,3)]`.
7.  Return to 1. `low[1]=0`. `low[3] (3) >= tin[1] (1)`. **AP Found: 1**.
    - Pop stack until `(1,3)`. BCC: `{1, 3}`.
8.  Return to 0. `low[0]=0`. `low[1] (0) >= tin[0] (0)`. **AP Check: 0**.
    - Pop stack until `(0,1)`. Stack has `(2,0), (1,2), (0,1)`.
    - BCC: `{0, 1, 2}`.
    - Is 0 AP? Root check. Children count = 1 (only went to 1). So 0 is NOT AP.

**Result:**

- APs: `{1}`.
- BCCs: `{1, 3}`, `{0, 1, 2}`.

## ✅ Proof of Correctness

- **AP:** `low[v] >= tin[u]` means there is no back-edge from `v` or its descendants to `u`'s ancestor. Removing `u` disconnects `v`.
- **BCC:** The stack ensures we collect all edges in the current biconnected component. Since we pop only when the AP condition is met (or at the end), we isolate maximal biconnected subgraphs.

## 💡 Interview Extensions (High-Value Add-ons)

- **Block-Cut Tree:** Construct a tree where nodes are original APs and BCCs. This allows solving path queries like "does path A->B pass through AP X?" efficiently.
- **Dynamic Connectivity:** Handling edge insertions/deletions is much harder (Holm-de Lichtenberg-Thorup).

### Common Mistakes to Avoid

1.  **Root Case:** Forget to check `children > 1` for root.
2.  **Stack Popping:** Pop edges, not vertices. A vertex can be in multiple BCCs, but an edge is in exactly one.
3.  **Back-Edges:** Push back-edges to stack too! They are part of the BCC.
