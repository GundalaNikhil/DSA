---
problem_id: AGR_DIRECTED_CYCLE_BASIS__8240
display_id: AGR-015
slug: directed-cycle-basis
title: "Directed Cycle Basis"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Cycle Basis
  - Spanning Forest
tags:
  - advanced-graphs
  - cycle-basis
  - directed
  - hard
premium: true
subscription_tier: basic
---

# AGR-015: Directed Cycle Basis

## 📋 Problem Summary

Find a **Cycle Basis** for a directed graph. A cycle basis is a minimal set of directed cycles such that any other directed cycle in the graph can be formed by a linear combination (XOR sum) of these basis cycles. The size of this basis is always $m - n + c$, where $m$ is edges, $n$ is nodes, and $c$ is connected components.

## 🌍 Real-World Scenario

**Scenario Title:** Electrical Circuit Analysis (Kirchhoff's Laws) 🔋

### The Problem
You are building a simulator for complex electrical circuits (like a chip design).
-   **Kirchhoff's Voltage Law (KVL):** The sum of voltage drops around any closed loop must be zero.
-   **Mesh Analysis:** To solve the circuit equations, you don't need *every* possible loop (which could be infinite or exponential). You only need a set of **Fundamental Loops** (start with minimal independent cycles).
-   **Goal:** Write a program that takes a circuit netlist (Directed Graph) and outputs a valid set of independent loops (Cycle Basis) that covers the entire circuit topology.

![Real-World Application](../images/AGR-015/real-world-scenario.png)

### From Real World to Algorithm
This is the **Minimum Cycle Basis** (or just Cycle Basis) problem.
-   **Independent:** Determining if a new cycle is "new" or just a combination of old ones is done using Linear Algebra (Gaussian Elimination over GF(2)).
-   **Vectors:** Each cycle is a bitmask of edges. $1$ if edge $i$ is in the cycle, $0$ otherwise.

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph Map:**
```
    0 --> 1
    ^     |
    |     v
    3 <-- 2
```
-   **Cycle:** `0->1`, `1->2`, `2->3`, `3->0`.
-   **Edges:** $e_0, e_1, e_2, e_3$.
-   **Vector:** `1111` (All edges present).
-   **Basis size:** $m - n + 1 = 4 - 4 + 1 = 1$. The basis is just this one cycle.

**Complex Case (Two Loops):**
```
   0 -> 1 -> 0  (Cycle A)
   1 -> 2 -> 1  (Cycle B)
   (Cycle C: 0->1->2->1->0 - Wait, simple cycles only?)
```
-   **Basis:** Cycle A and Cycle B.
-   Why? Any larger flow can be described as flowing around A and B.

### Algorithm Flow Diagram: Gaussian Elimination

```mermaid
graph TD
    Start[Start] --> CalcD[Calculate Basis Dimension D = M - N + C]
    CalcD --> InitBasis[Initialize Empty Basis]
    InitBasis --> LoopEdges[Iterate Over Every Edge (u,v)]
    LoopEdges --> FindPath[Find Shortest Path v -> u]
    FindPath -- No Path --> LoopEdges
    FindPath -- Path Found --> FormVector[Form Cycle Vector (Bitmask)]
    FormVector --> Gaussian[Gaussian Elimination Check]
    Gaussian -- Dependent (Reduces to 0) --> Update[Ignore]
    Gaussian -- Independent --> Insert[Add to Basis]
    Insert --> CheckCount{Basis Size == D?}
    CheckCount -- Yes --> ReturnBasis[Return Cycles]
    CheckCount -- No --> Update
    Update --> LoopEdges
```

## 🎯 Edge Cases to Test

1.  **Multiple Edges:** `0->1` (edge 1) and `0->1` (edge 2). Forms a cycle `0->1 (e1) -> 0 (implies 1->0 exists?)`.
    -   Wait, if directed graph has `0->1` and `0->1`, it's not a cycle unless `1->0` exists.
    -   If `0->1` and `1->0`, result `0->1->0`.
2.  **Disconnected Graph:** Algorithm handles components via `c` term.
3.  **No Cycles:** acyclic graph. Basis size 0.

## ✅ Input/Output Clarifications
-   **Input:** $N, M$, then edge list.
-   **Output:** Number of cycles, followed by length and vertices for each. Vertices must start and end with same node ($v_1 = v_k$).
-   **Cycle Validity:** Cycles must be simple (no repeated nodes except start/end). Our BFS find-path ensures simplicity if the shortest path is unique.

## Naive Approach
A naive DFS finds back-edges. For each back-edge `u->v`, the path in the DFS tree plus `u->v` forms a cycle.
-   **Flaw:** In directed graphs, "cross-edges" `u->v` (where `v` is visited but not ancestor) can also form cycles if a path `v ~> u` exists. DFS tree cycles are insufficient for directed graphs (unlike undirected).

## Optimal Approach (Horton's / Gaussian Elimination)

### Key Strategy
1.  **Generate Candidates:** For *every* edge $e = (u, v)$, try to close a cycle by finding the shortest path $v \to u$.
2.  **Filter Independence:** This generates many cycles (some redundant). Treat each cycle as a vector in $\{0, 1\}^M$.
3.  **Gaussian Elimination:** Use a basis (like a Linear Basis in competitive programming) to keep only independent vectors.
    -   If a new vector `X` can be XOR-ed to 0 using the current basis, it's dependent.
    -   Otherwise, add `X` to basis.

### Time Complexity
-   **Shortest Paths:** $M \times O(N+M)$ (BFS).
-   **Gaussian Elimination:** $O(M \times (\text{Basis Size}) \times \frac{M}{64})$.
-   **Total:** $O(M(N+M) + \frac{M^3}{64})$. With $N, M \approx 2000$, this passes.

### Space Complexity
-   **O(M^2 / 64)**: To store $M$ basis vectors of size $M$ bits.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public List<List<Integer>> cycleBasis(int n, int[][] edges) {
        int m = edges.length;
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(new int[]{edges[i][1], i});
        }

        // 1. Calculate Basis Dimension: D = m - n + c
        int c = 0;
        boolean[] visited = new boolean[n];
        List<List<Integer>> undirAdj = new ArrayList<>(); // For components
        for (int i = 0; i < n; i++) undirAdj.add(new ArrayList<>());
        for (int[] e : edges) {
            undirAdj.get(e[0]).add(e[1]);
            undirAdj.get(e[1]).add(e[0]);
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                c++;
                dfs(i, visited, undirAdj);
            }
        }
        int D = m - n + c;

        // 2. Candidate Cycles & Gaussian Elimination
        BitSet[] basis = new BitSet[m]; // Linear Basis
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            if (result.size() == D) break;
            
            int u = edges[i][0];
            int v = edges[i][1];
            
            // Find shortest path v -> u to close the cycle
            List<Integer> path = bfs(v, u, n, adj);
            if (path == null) continue;
            
            // Create vector
            BitSet vec = new BitSet(m);
            vec.set(i); // Include edge i (u->v)
            for (int eIdx : path) vec.set(eIdx); // Include path edges
            
            // Try to insert into basis
            if (insert(basis, vec)) {
                // Reconstruct cycle for output
                List<Integer> cycle = new ArrayList<>();
                cycle.add(u);
                int curr = v;
                cycle.add(curr);
                for (int eIdx : path) {
                    curr = edges[eIdx][1];
                    cycle.add(curr);
                }
                result.add(cycle);
            }
        }
        return result;
    }
    
    private void dfs(int u, boolean[] visited, List<List<Integer>> adj) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs(v, visited, adj);
        }
    }
    
    private List<Integer> bfs(int start, int target, int n, List<List<int[]>> adj) {
        if (start == target) return new ArrayList<>();
        int[] parentEdge = new int[n];
        int[] parentNode = new int[n];
        Arrays.fill(parentEdge, -1);
        Arrays.fill(parentNode, -1);
        
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        parentNode[start] = start;
        
        while (!q.isEmpty()) {
            int u = q.poll();
            if (u == target) break;
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int idx = edge[1];
                if (parentNode[v] == -1) {
                    parentNode[v] = u;
                    parentEdge[v] = idx;
                    q.add(v);
                }
            }
        }
        
        if (parentNode[target] == -1) return null;
        
        List<Integer> path = new ArrayList<>();
        int curr = target;
        while (curr != start) {
            path.add(parentEdge[curr]);
            curr = parentNode[curr];
        }
        Collections.reverse(path);
        return path;
    }
    
    private boolean insert(BitSet[] basis, BitSet vec) {
        for (int i = vec.nextSetBit(0); i >= 0; i = vec.nextSetBit(i + 1)) {
            if (basis[i] == null) {
                basis[i] = (BitSet) vec.clone();
                return true;
            }
            vec.xor(basis[i]);
        }
        return false;
    }
}
```

### Python
```python
import sys
from collections import deque

def cycle_basis(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    m = len(edges)
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        
    # 1. Calc basis size D = M - N + C
    undir_adj = [[] for _ in range(n)]
    for u, v in edges:
        undir_adj[u].append(v)
        undir_adj[v].append(u)
        
    visited = [False] * n
    c = 0
    for i in range(n):
        if not visited[i]:
            c += 1
            q = [i]
            visited[i] = True
            while q:
                u = q.pop()
                for v in undir_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
    
    D = m - n + c
    
    # 2. Gaussian Elimination
    basis = [None] * m
    result = []
    
    def get_path(start, target):
        if start == target: return []
        parent = [-1] * n
        parent_edge = [-1] * n
        q = deque([start])
        parent[start] = start
        
        while q:
            u = q.popleft()
            if u == target: break
            for v, idx in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    parent_edge[v] = idx
                    q.append(v)
        
        if parent[target] == -1: return None
        
        path = []
        curr = target
        while curr != start:
            path.append(parent_edge[curr])
            curr = parent[curr]
        return path[::-1]

    for i in range(m):
        if len(result) == D: break
        
        u, v = edges[i]
        path = get_path(v, u)
        if path is None: continue
        
        # Vector construction (using Python big integers as bitsets)
        vec = (1 << i)
        for idx in path:
            vec |= (1 << idx)
            
        # Gaussian Elimination Insert
        temp_vec = vec
        inserted = False
        
        # Iterate bits (simple loop is fine for Python ints, but finding MSB/LSB efficiently is better)
        # We process from 0 to m-1
        for bit in range(m):
            if (temp_vec >> bit) & 1:
                if basis[bit] is None:
                    basis[bit] = temp_vec
                    inserted = True
                    break
                else:
                    temp_vec ^= basis[bit]
        
        if inserted:
            cycle = [u, v]
            curr = v
            for idx in path:
                next_node = edges[idx][1]
                cycle.append(next_node)
                curr = next_node
            result.append(cycle)
            
    return result
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <bitset>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> cycleBasis(int n, const vector<pair<int, int>>& edges) {
        int m = edges.size();
        vector<vector<pair<int, int>>> adj(n);
        for (int i = 0; i < m; i++) {
            adj[edges[i].first].push_back({edges[i].second, i});
        }

        // Calc basis size
        int c = 0;
        vector<bool> visited(n, false);
        vector<vector<int>> undirAdj(n);
        for (const auto& e : edges) {
            undirAdj[e.first].push_back(e.second);
            undirAdj[e.second].push_back(e.first);
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                c++;
                queue<int> q;
                q.push(i);
                visited[i] = true;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : undirAdj[u]) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }
            }
        }
        int D = m - n + c;

        // Basis using bitset
        // M <= 2000. bitset<2000>
        vector<bitset<2000>> basis(m);
        vector<bool> hasBasis(m, false);
        vector<vector<int>> result;

        for (int i = 0; i < m; i++) {
            if (result.size() == D) break;

            int u = edges[i].first;
            int v = edges[i].second;

            // BFS v -> u
            vector<int> parentEdge(n, -1);
            vector<int> parentNode(n, -1);
            queue<int> q;
            q.push(v);
            parentNode[v] = v;

            bool found = false;
            while (!q.empty()) {
                int curr = q.front(); q.pop();
                if (curr == u) {
                    found = true;
                    break;
                }
                for (auto& edge : adj[curr]) {
                    int next = edge.first;
                    int idx = edge.second;
                    if (parentNode[next] == -1) {
                        parentNode[next] = curr;
                        parentEdge[next] = idx;
                        q.push(next);
                    }
                }
            }

            if (!found) continue;

            bitset<2000> vec;
            vec[i] = 1;
            
            vector<int> path;
            int curr = u;
            while (curr != v) {
                int idx = parentEdge[curr];
                vec[idx] = 1;
                path.push_back(idx);
                curr = parentNode[curr];
            }
            // Path is u <- ... <- v. Reverse to get v -> ... -> u
            reverse(path.begin(), path.end());

            // Insert
            bool inserted = false;
            for (int j = 0; j < m; j++) {
                if (vec[j]) {
                    if (!hasBasis[j]) {
                        basis[j] = vec;
                        hasBasis[j] = true;
                        inserted = true;
                        break;
                    } else {
                        vec ^= basis[j];
                    }
                }
            }

            if (inserted) {
                vector<int> cycle;
                cycle.push_back(u);
                cycle.push_back(v);
                for (int idx : path) {
                    cycle.push_back(edges[idx].second);
                }
                result.push_back(cycle);
            }
        }

        return result;
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
    vector<vector<int>> cycles = solution.cycleBasis(n, edges);
    cout << cycles.size() << "\n";
    for (const auto& cyc : cycles) {
        cout << cyc.size();
        for (int v : cyc) cout << ' ' << v;
        cout << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  cycleBasis(n, edges) {
    const m = edges.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < m; i++) {
      adj[edges[i][0]].push({ to: edges[i][1], idx: i });
    }

    // Calc basis size
    let c = 0;
    const visited = new Int8Array(n).fill(0);
    const undirAdj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      undirAdj[u].push(v);
      undirAdj[v].push(u);
    }

    const dfs = (u) => {
      visited[u] = 1;
      for (const v of undirAdj[u]) {
        if (!visited[v]) dfs(v);
      }
    };

    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        c++;
        dfs(i);
      }
    }
    const D = m - n + c;

    // Basis using BigInt for bitsets
    const basis = new Array(m).fill(null);
    const result = [];

    for (let i = 0; i < m; i++) {
      if (result.length === D) break;

      const u = edges[i][0];
      const v = edges[i][1];

      // BFS v -> u
      const parentNode = new Int32Array(n).fill(-1);
      const parentEdge = new Int32Array(n).fill(-1);
      const q = [v];
      parentNode[v] = v;
      
      let found = false;
      let head = 0;
      while (head < q.length) {
        const curr = q[head++];
        if (curr === u) {
          found = true;
          break;
        }
        for (const edge of adj[curr]) {
          if (parentNode[edge.to] === -1) {
            parentNode[edge.to] = curr;
            parentEdge[edge.to] = edge.idx;
            q.push(edge.to);
          }
        }
      }

      if (!found) continue;

      let vec = 0n;
      vec |= (1n << BigInt(i));
      
      const path = [];
      let curr = u;
      while (curr !== v) {
        const idx = parentEdge[curr];
        vec |= (1n << BigInt(idx));
        path.push(idx);
        curr = parentNode[curr];
      }
      path.reverse();

      // Insert
      let tempVec = vec;
      let inserted = false;
      for (let j = 0; j < m; j++) {
        if ((tempVec >> BigInt(j)) & 1n) {
          if (basis[j] === null) {
            basis[j] = tempVec;
            inserted = true;
            break;
          } else {
            tempVec ^= basis[j];
          }
        }
      }

      if (inserted) {
        const cycle = [u, v];
        for (const idx of path) {
          cycle.push(edges[idx][1]);
        }
        result.push(cycle);
      }
    }
    return result;
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
  const cycles = solution.cycleBasis(n, edges);
  const out = [cycles.length.toString()];
  for (const cyc of cycles) {
    out.push(`${cyc.length} ${cyc.join(" ")}`.trim());
  }
  console.log(out.join("\n").trim());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
4 5
0 1
1 2
2 0
1 3
3 1
```
-   **Graph:** Triangle `0-1-2` and Path `1-3-1`.
-   **Edges:**
    -   0: `0->1`
    -   1: `1->2`
    -   2: `2->0`
    -   3: `1->3`
    -   4: `3->1`
-   **Basis size D:** $5 (M) - 4 (N) + 1 (C) = 2$.
-   **Iteration:**
    -   Edge 0 (`0->1`): Path `1->2->0` found. Cycle C1: `0-1-2-0`. Bits: `{0, 1, 2}`. Independent. **Add.**
    -   Edge 1 (`1->2`): Path `2->0->1` found. Cycle `1-2-0-1`. Bits `{0, 1, 2}`. Duplicate of C1. **Skip.**
    -   ...
    -   Edge 3 (`1->3`): Path `3->1`. Cycle C2: `1-3-1`. Bits `{3, 4}`. Independent. **Add.**
-   **Result:** 2 Cycles. C1 and C2. Independent.

## ✅ Proof of Correctness
-   **Dimension:** The number of fundamental cycles is strictly fixed by topological properties.
-   **Span:** By checking every edge's ability to close a cycle, we ensure we consider all "Shortest" cycles.
-   **Basis:** Gaussian elimination guarantees the chosen set is a basis (minimal and spanning).

## ⚠️ Common Mistakes to Avoid

1.  **Undirected Logic:** Do not use `m - n + c` logic for undirected graphs on a *directed* graph unless you understand the cycle space difference. (Here the formula is actually the same for the dimension of the cycle space).
2.  **Modifying Graph:** Don't delete edges.
3.  **Bitset Indices:** Ensure edge indices `0..m-1` are consistent across BFS and bitsets.

## 💡 Interview Extensions
1.  **Minimum Weight Basis:** If edges have weights, sort edges by weight? No, Horton's algorithm generates $O(MN)$ candidates and sorts *cycles* by weight, then greedily adds.
2.  **Fundamental Cycles:** If we just want *any* basis, we can use a Spanning Tree. For every non-tree edge $e$, tree path + $e$ is a cycle. Is this minimal? Yes. But for **Shortest** cycles or specific properties, Gaussian is better.
    -   *Note:* In directed graphs, a spanning tree (arborescence) doesn't guarantee back-edges cover all cycles (cross edges matter). So Spanning Tree approach is strictly for Undirected graphs. For directed, we *must* use something like this candidate generation.
