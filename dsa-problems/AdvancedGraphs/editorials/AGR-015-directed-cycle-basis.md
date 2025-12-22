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

Find a **Cycle Basis** of a directed graph consisting of `m - n + c` simple directed cycles, where `m` is edges, `n` is vertices, and `c` is connected components (in the underlying undirected sense).

## 🌍 Real-World Scenario

**Scenario Title:** Circuit Analysis (Kirchhoff's Laws)

In electrical circuits (or hydraulic networks), we analyze loops to apply Kirchhoff's Voltage Law (KVL).
-   **Mesh Analysis:** We need a set of independent loops (cycles) to write equations.
-   **Basis:** The fundamental cycles form a basis. Any other closed loop can be represented as a combination of these basis loops.
-   **Directed:** Current flows in a specific direction, so loops must be directed.

![Real-World Application](../images/AGR-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    0 --> 1
    ^     |
    |     v
    3 <-- 2
```
-   Edges: `0->1`, `1->2`, `2->3`, `3->0`.
-   Cycle: `0-1-2-3-0`.
-   `m=4, n=4, c=1`. Basis size `4-4+1 = 1`.
-   Output: `4 0 1 2 3 0`.

**Two Cycles:**
```
   0 -> 1 -> 0
   1 -> 2 -> 1
```
-   `m=4, n=3, c=1`. Basis size `4-3+1 = 2`.
-   Cycles: `0-1-0` and `1-2-1`.

### Algorithm: Horton's Algorithm (Simplified) or Gaussian Elimination

To find a basis of size `D = m - n + c`:
1.  **Candidate Cycles:** For every edge `u -> v`, find the shortest path from `v` to `u` (using BFS). If a path exists, `u -> v` + `path` forms a directed cycle.
2.  **Independence:** We need `D` linearly independent cycles.
    -   Represent each cycle as a vector in `GF(2)^m` (1 if edge is present, 0 otherwise).
    -   Use **Gaussian Elimination** to maintain a basis.
    -   Iterate through edges. For each edge, find the shortest cycle containing it. Try to add to basis.
    -   Stop when we have `D` cycles.

**Why Gaussian Elimination?**
-   Ensures linear independence.
-   With `M=2000`, `M^3` operations with bitsets is feasible.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Basis Size:** Strictly `m - n + c`. If the graph doesn't support this many directed cycles, the problem constraints/type usually ensure it (e.g., strongly connected components or specific structure).
-   **Output Format:** First line `b` (number of cycles). Then each cycle.
-   **Cycle Format:** `k v1 v2 ... vk` where `v1 == vk`.

## Naive Approach

### Intuition

DFS to find back-edges.

### Failure Case

DFS tree back-edges form a basis only for the cycle space of the *underlying undirected graph* if we treat them as undirected. In directed graphs, cross-edges can also form cycles. A simple DFS might miss some or pick dependent ones.

## Optimal Approach (Shortest Cycles + Gaussian Elimination)

### Time Complexity

-   **O(M * (N + M) + M^3 / 64)**:
    -   `M` BFS runs: `O(M * (N + M))`.
    -   Gaussian Elimination: `O(M * BasisSize * M / 64)`. Since BasisSize <= M, `O(M^3 / 64)`.
    -   For `M=2000`, `2000^3 / 64` is approx `1.25 * 10^8`, feasible.

### Space Complexity

-   **O(M^2 / 64)**: To store basis vectors.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> cycleBasis(int n, int[][] edges) {
        int m = edges.length;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(i); // Store edge index
        }

        // Calculate required basis size
        // m - n + c
        // Find c (connected components in undirected graph)
        int c = 0;
        boolean[] visited = new boolean[n];
        List<List<Integer>> undirAdj = new ArrayList<>();
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
        int basisSize = m - n + c;

        List<BitSet> basisVectors = new ArrayList<>();
        List<List<Integer>> resultCycles = new ArrayList<>();
        
        // Candidate cycles: Shortest cycle through each edge
        // We can just iterate edges and try to add.
        // Optimization: Sort edges? Not needed.
        
        for (int i = 0; i < m; i++) {
            if (resultCycles.size() == basisSize) break;
            
            int u = edges[i][0];
            int v = edges[i][1];
            
            // Find shortest path v -> u
            List<Integer> pathEdges = bfs(v, u, n, adj);
            if (pathEdges == null) continue;
            
            // Construct cycle vector
            BitSet vec = new BitSet(m);
            vec.set(i);
            for (int eIdx : pathEdges) vec.set(eIdx);
            
            // Check independence
            if (insert(basisVectors, vec)) {
                // Reconstruct cycle nodes
                List<Integer> cycle = new ArrayList<>();
                cycle.add(u);
                int curr = v;
                cycle.add(curr);
                for (int eIdx : pathEdges) {
                    // Edge eIdx is x->y. curr should be x.
                    int next = edges[eIdx][1];
                    cycle.add(next);
                    curr = next;
                }
                resultCycles.add(cycle);
            }
        }
        
        return resultCycles;
    }
    
    private void dfs(int u, boolean[] visited, List<List<Integer>> adj) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs(v, visited, adj);
        }
    }
    
    private List<Integer> bfs(int start, int target, int n, List<List<Integer>> adj) {
        if (start == target) return new ArrayList<>(); // Self loop handled
        
        int[] parentEdge = new int[n];
        int[] parentNode = new int[n];
        Arrays.fill(parentEdge, -1);
        Arrays.fill(parentNode, -1);
        
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        parentNode[start] = start; // Mark visited
        
        while (!q.isEmpty()) {
            int u = q.poll();
            if (u == target) break;
            
            for (int eIdx : adj.get(u)) {
                // Edge eIdx: u -> v
                // We need edges array to know v? 
                // Let's assume we can't access 'edges' easily inside bfs without passing.
                // But 'edges' is available in outer scope? No.
                // Let's fix adj to store (v, eIdx).
            }
        }
        return null; 
    }
    
    // Helper to insert into basis
    private boolean insert(List<BitSet> basis, BitSet vec) {
        for (BitSet b : basis) {
            int firstSet = b.nextSetBit(0);
            if (vec.get(firstSet)) {
                vec.xor(b);
            }
            if (vec.isEmpty()) return false;
        }
        // Add and maintain reduced row echelon form (optional, but good for stability/order)
        // Simple insert is fine for independence check if we process carefully.
        // Let's use a pivot array.
        return false; // Placeholder
    }
}
// Rewriting Solution for clarity and correctness
class SolutionReal {
    public List<List<Integer>> cycleBasis(int n, int[][] edges) {
        int m = edges.length;
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(new int[]{edges[i][1], i});
        }

        // Calc basis size
        int c = 0;
        boolean[] visited = new boolean[n];
        List<List<Integer>> undirAdj = new ArrayList<>();
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

        BitSet[] basis = new BitSet[m]; // basis[i] has pivot at i
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            if (result.size() == D) break;
            
            int u = edges[i][0];
            int v = edges[i][1];
            
            List<Integer> path = bfs(v, u, n, adj);
            if (path == null) continue;
            
            BitSet vec = new BitSet(m);
            vec.set(i);
            for (int eIdx : path) vec.set(eIdx);
            
            if (insert(basis, vec)) {
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

        SolutionReal solution = new SolutionReal();
        List<List<Integer>> cycles = solution.cycleBasis(n, edges);
        StringBuilder sb = new StringBuilder();
        sb.append(cycles.size()).append('\n');
        for (List<Integer> cyc : cycles) {
            sb.append(cyc.size());
            for (int v : cyc) sb.append(' ').append(v);
            sb.append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
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
        
    # Calc basis size
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
        
        # Vector
        vec = 0
        vec |= (1 << i)
        for idx in path:
            vec |= (1 << idx)
            
        # Insert
        temp_vec = vec
        inserted = False
        # Find pivot
        # We iterate bits from low to high or high to low?
        # Let's use low to high (0 to m-1)
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
                # Edge idx is x->y. curr is x.
                # We need y.
                next_node = edges[idx][1]
                cycle.append(next_node)
                curr = next_node
            result.append(cycle)
            
    return result

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
            
        cycles = cycle_basis(n, edges)
        out = [str(len(cycles))]
        for cyc in cycles:
            out.append(str(len(cyc)) + " " + " ".join(map(str, cyc)))
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
  const cycles = solution.cycleBasis(n, edges);
  const out = [cycles.length.toString()];
  for (const cyc of cycles) {
    out.push(`${cyc.length} ${cyc.join(" ")}`.trim());
  }
  console.log(out.join("\n").trim());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 5
0 1
1 2
2 0
1 3
3 1
```
-   `m=5, n=4, c=1`. D = 2.
-   Edges: `0:0->1, 1:1->2, 2:2->0, 3:1->3, 4:3->1`.
-   **Iterate:**
    -   `i=0 (0->1)`: Path `1->2->0`. Cycle `0-1-2-0`. Vec `11100`. Inserted.
    -   `i=1 (1->2)`: Path `2->0->1`. Cycle `1-2-0-1`. Vec `11100`. Dependent (XOR with basis[0] -> 0). Skip.
    -   `i=2 (2->0)`: Path `0->1->2`. Cycle `2-0-1-2`. Dependent.
    -   `i=3 (1->3)`: Path `3->1`. Cycle `1-3-1`. Vec `00011`. Inserted.
    -   Count = 2. Break.
-   **Output:** 2 cycles. Correct.

## ✅ Proof of Correctness

-   **Basis Size:** The dimension of the cycle space is `m - n + c`.
-   **Independence:** Gaussian Elimination ensures all selected cycles are linearly independent.
-   **Validity:** Each cycle is a valid directed cycle.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Minimum Cycle Basis:** Sort edges by weight? No, iterate all pairs `(u, v)`, find shortest path, form cycle, sort cycles by length, then insert. This gives the Minimum Cycle Basis (Horton's Algorithm).
-   **Undirected:** Same logic applies for undirected graphs (using GF(2)).

### Common Mistakes to Avoid

1.  **Bitset Size:** Ensure it covers `M`.
2.  **Independence Check:** Don't just check if cycle is unique; check linear independence.
3.  **Path Direction:** BFS from `v` to `u` for edge `u->v`.
