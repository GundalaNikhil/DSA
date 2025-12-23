---
problem_id: AGR_SCC_COMPRESSION__2659
display_id: AGR-008
slug: scc-compression
title: "Strongly Connected Components Compression"
difficulty: Easy
difficulty_score: 40
topics:
  - Graphs
  - SCC
  - Condensation Graph
tags:
  - advanced-graphs
  - scc
  - condensation
  - easy
premium: true
subscription_tier: basic
---

# AGR-008: Strongly Connected Components Compression

## 📋 Problem Summary

Decompose a directed graph into its **Strongly Connected Components (SCCs)**. Then, contract each SCC into a single node to form a **Condensation Graph**, which is always a Directed Acyclic Graph (DAG).

## 🌍 Real-World Scenario

**Scenario Title:** Software Module Dependencies

Consider a large software project with many modules (files/classes) that depend on each other.
-   **Cyclic Dependency:** If Module A depends on B, and B depends on A, they are tightly coupled and must be compiled/deployed together. They form an SCC.
-   **Condensation:** To understand the high-level architecture, we group these cyclic clusters into "super-modules".
-   **DAG:** The dependencies between these super-modules form a hierarchy (DAG), allowing us to determine a valid build order (Topological Sort).

![Real-World Application](../images/AGR-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Original Graph:**
```
    (0) <--> (1)
     |        |
     v        v
    (2) <--> (3) --> (4)
```
-   `0` and `1` form a cycle. SCC A = `{0, 1}`.
-   `2` and `3` form a cycle. SCC B = `{2, 3}`.
-   `4` is isolated. SCC C = `{4}`.
-   Edges:
    -   `0->2` becomes `A -> B`.
    -   `1->3` becomes `A -> B`.
    -   `3->4` becomes `B -> C`.

**Condensation Graph (DAG):**
```
    (A) ===> (B) ---> (C)
```
Note: Multiple edges between SCCs (like `0->2` and `1->3`) are merged into a single edge `A->B`.

### Algorithm: Tarjan's Algorithm

1.  **Find SCCs:**
    -   Use **Tarjan's Algorithm** (DFS with stack and low-link values).
    -   Maintain `tin` (discovery time), `low` (lowest reachable ancestor), and a `stack` of active nodes.
    -   When `low[u] == tin[u]`, pop from stack to form an SCC.
2.  **Build Condensation Graph:**
    -   Assign a component ID to each node.
    -   Iterate over all original edges `u -> v`.
    -   If `comp[u] != comp[v]`, add a directed edge `comp[u] -> comp[v]` to the new graph.
    -   Use a Set or sort+unique to remove duplicate edges between components.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Component IDs:** Can be any range `0` to `k-1`.
-   **Duplicate Edges:** The condensation graph should not have multi-edges. `A->B` should appear once even if there are 100 edges from nodes in A to nodes in B.
-   **Self-Loops:** The condensation graph is a DAG, so no self-loops `A->A` (edges within an SCC are ignored).

## Naive Approach

### Intuition

Run BFS/DFS from every node to check reachability to every other node.

### Time Complexity

-   **O(N * (N+M))**: Too slow for N=200,000.

## Optimal Approach (Tarjan's or Kosaraju's)

### Time Complexity

-   **O(N + M)**: Linear time to find SCCs and build the DAG.

### Space Complexity

-   **O(N + M)**: Storing the graph and auxiliary arrays.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] onStack;
    private Stack<Integer> stack;
    private List<List<Integer>> sccs;
    private List<List<Integer>> adj;

    public Object[] sccCompress(int n, List<List<Integer>> adjList) {
        this.adj = adjList;
        tin = new int[n];
        low = new int[n];
        Arrays.fill(tin, -1);
        onStack = new boolean[n];
        stack = new Stack<>();
        sccs = new ArrayList<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i);
            }
        }

        int k = sccs.size();
        int[] comp = new int[n];
        // Assign component IDs (reverse topological order usually, but here arbitrary 0..k-1)
        for (int i = 0; i < k; i++) {
            for (int node : sccs.get(i)) {
                comp[node] = i; // Or k - 1 - i for topo order
            }
        }

        // Build Condensation Graph
        Set<String> seenEdges = new HashSet<>();
        List<int[]> dagEdges = new ArrayList<>();

        for (int u = 0; u < n; u++) {
            for (int v : adj.get(u)) {
                if (comp[u] != comp[v]) {
                    String key = comp[u] + "," + comp[v];
                    if (!seenEdges.contains(key)) {
                        seenEdges.add(key);
                        dagEdges.add(new int[]{comp[u], comp[v]});
                    }
                }
            }
        }

        return new Object[]{k, comp, dagEdges};
    }

    private void dfs(int u) {
        tin[u] = low[u] = timer++;
        stack.push(u);
        onStack[u] = true;

        for (int v : adj.get(u)) {
            if (tin[v] == -1) {
                dfs(v);
                low[u] = Math.min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = Math.min(low[u], tin[v]);
            }
        }

        if (low[u] == tin[u]) {
            List<Integer> component = new ArrayList<>();
            while (true) {
                int v = stack.pop();
                onStack[v] = false;
                component.add(v);
                if (u == v) break;
            }
            sccs.add(component);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
        }

        Solution solution = new Solution();
        Object[] res = solution.sccCompress(n, adj);
        int k = (int) res[0];
        int[] comp = (int[]) res[1];
        @SuppressWarnings("unchecked")
        List<int[]> edges = (List<int[]>) res[2];

        StringBuilder sb = new StringBuilder();
        sb.append(k).append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        sb.append('\n').append(edges.size()).append('\n');
        for (int[] e : edges) sb.append(e[0]).append(' ').append(e[1]).append('\n');
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def scc_compress(n: int, adj: list[list[int]]):
    tin = [-1] * n
    low = [-1] * n
    on_stack = [False] * n
    stack = []
    timer = 0
    sccs = []
    
    def dfs(u):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        stack.append(u)
        on_stack[u] = True
        
        for v in adj[u]:
            if tin[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], tin[v])
                
        if low[u] == tin[u]:
            component = []
            while True:
                v = stack.pop()
                on_stack[v] = False
                component.append(v)
                if u == v:
                    break
            sccs.append(component)
            
    for i in range(n):
        if tin[i] == -1:
            dfs(i)
            
    k = len(sccs)
    comp = [0] * n
    # Tarjan finds SCCs in reverse topological order
    # Assign IDs 0 to k-1 based on discovery order (sccs list order)
    for i, component in enumerate(sccs):
        for node in component:
            comp[node] = i
            
    dag_edges = set()
    for u in range(n):
        for v in adj[u]:
            if comp[u] != comp[v]:
                dag_edges.add((comp[u], comp[v]))
                
    return k, comp, list(dag_edges)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            
        k, comp, edges = scc_compress(n, adj)
        
        out = [str(k), " ".join(map(str, comp)), str(len(edges))]
        for u, v in edges:
            out.append(f"{u} {v}")
            
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
#include <stack>
#include <algorithm>
#include <set>
#include <tuple>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, low;
    vector<bool> onStack;
    stack<int> st;
    vector<vector<int>> sccs;
    
    void dfs(int u, const vector<vector<int>>& adj) {
        tin[u] = low[u] = timer++;
        st.push(u);
        onStack[u] = true;

        for (int v : adj[u]) {
            if (tin[v] == -1) {
                dfs(v, adj);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], tin[v]);
            }
        }

        if (low[u] == tin[u]) {
            vector<int> component;
            while (true) {
                int v = st.top();
                st.pop();
                onStack[v] = false;
                component.push_back(v);
                if (u == v) break;
            }
            sccs.push_back(component);
        }
    }

public:
    tuple<int, vector<int>, vector<pair<int, int>>> sccCompress(int n, const vector<vector<int>>& adj) {
        tin.assign(n, -1);
        low.assign(n, -1);
        onStack.assign(n, false);
        while (!st.empty()) st.pop();
        sccs.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i, adj);
            }
        }

        int k = sccs.size();
        vector<int> comp(n);
        for (int i = 0; i < k; i++) {
            for (int node : sccs[i]) {
                comp[node] = i;
            }
        }

        set<pair<int, int>> dagEdges;
        for (int u = 0; u < n; u++) {
            for (int v : adj[u]) {
                if (comp[u] != comp[v]) {
                    dagEdges.insert({comp[u], comp[v]});
                }
            }
        }

        return {k, comp, vector<pair<int, int>>(dagEdges.begin(), dagEdges.end())};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    Solution solution;
    auto [k, comp, edges] = solution.sccCompress(n, adj);

    cout << k << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    cout << "\n" << edges.size() << "\n";
    for (auto& e : edges) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  sccCompress(n, adj) {
    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const onStack = new Int8Array(n).fill(0);
    const stack = [];
    const sccs = [];
    let timer = 0;

    // Iterative Tarjan using explicit stack
    // Frame: { u, iterIndex }
    
    const runDFS = (startNode) => {
        const callStack = [{ u: startNode, idx: 0 }];
        tin[startNode] = low[startNode] = timer++;
        stack.push(startNode);
        onStack[startNode] = 1;

        while (callStack.length > 0) {
            const frame = callStack[callStack.length - 1];
            const u = frame.u;
            
            if (frame.idx < adj[u].length) {
                const v = adj[u][frame.idx];
                frame.idx++;
                
                if (tin[v] === -1) {
                    tin[v] = low[v] = timer++;
                    stack.push(v);
                    onStack[v] = 1;
                    callStack.push({ u: v, idx: 0 });
                } else if (onStack[v]) {
                    low[u] = Math.min(low[u], tin[v]);
                }
            } else {
                // Post-order
                callStack.pop();
                if (callStack.length > 0) {
                    const p = callStack[callStack.length - 1].u;
                    low[p] = Math.min(low[p], low[u]);
                }
                
                if (low[u] === tin[u]) {
                    const component = [];
                    while (true) {
                        const v = stack.pop();
                        onStack[v] = 0;
                        component.push(v);
                        if (u === v) break;
                    }
                    sccs.push(component);
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (tin[i] === -1) runDFS(i);
    }

    const k = sccs.length;
    const comp = new Int32Array(n);
    // Assign IDs
    // sccs are found in reverse topological order
    // Reverse sccs to get topological order (Source -> Sink)
    // Though problem doesn't require specific order.
    // Use index.
    
    // Note: Tarjan's naturally produces reverse topological order of SCCs.
    // sccs[0] is a sink SCC.
    // If we want comp[u] to be somewhat topological, we can assign k-1-i.
    // But simple 0..k-1 is fine.
    
    for (let i = 0; i < k; i++) {
        for (const node of sccs[i]) {
            comp[node] = i;
        }
    }

    const dagEdges = new Set();
    const edgesList = [];
    
    for (let u = 0; u < n; u++) {
        for (const v of adj[u]) {
            if (comp[u] !== comp[v]) {
                const key = ``comp[u],`{comp[v]}`;
                if (!dagEdges.has(key)) {
                    dagEdges.add(key);
                    edgesList.push([comp[u], comp[v]]);
                }
            }
        }
    }

    return [k, comp, edgesList];
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  const [k, comp, edges] = solution.sccCompress(n, adj);
  
  const out = [k.toString(), comp.join(" "), edges.length.toString()];
  for (const [a, b] of edges) out.push(``a`{b}`);
  console.log(out.join("\n").trim());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1
1 0
1 2
```
**Trace:**
1.  Start DFS(0). `tin[0]=0`. Stack `[0]`.
2.  Edge `0->1`. DFS(1). `tin[1]=1`. Stack `[0, 1]`.
3.  Edge `1->0`. `0` on stack. `low[1] = min(1, tin[0]=0) = 0`.
4.  Edge `1->2`. DFS(2). `tin[2]=2`. Stack `[0, 1, 2]`.
5.  Node 2 done. `low[2]=2`. `low[2]==tin[2]`. **SCC Found: {2}**. Pop 2.
6.  Back to 1. `low[1] = min(0, low[2]=2) = 0`.
7.  Node 1 done. `low[1]=0`. Back to 0. `low[0] = min(0, low[1]=0) = 0`.
8.  Node 0 done. `low[0]=0`. `low[0]==tin[0]`. **SCC Found: {1, 0}**. Pop 1, 0.

**Components:**
-   SCC 0: `{2}`. ID=0.
-   SCC 1: `{1, 0}`. ID=1.
-   `comp = [1, 1, 0]`.

**Edges:**
-   `0->1`: Same comp (1->1). Ignore.
-   `1->0`: Same comp (1->1). Ignore.
-   `1->2`: Diff comp (1->0). Add edge `1->0`.

**Output:**
-   K=2.
-   Comp: `1 1 0`.
-   Edges: `1 0`.
(Matches logic, IDs can differ but structure is correct).

## ✅ Proof of Correctness

-   **SCC:** Tarjan's algorithm correctly identifies SCCs in linear time.
-   **Condensation:** By contracting each SCC into a node, any cycle would be contained within a node. Thus, the remaining edges form a DAG.

## 💡 Interview Extensions (High-Value Add-ons)

-   **2-SAT:** 2-SAT problems are solved by finding SCCs in the implication graph. If `x` and `!x` are in the same SCC, it's unsatisfiable.
-   **Reachability:** In a DAG, reachability can be solved using bitsets or topological sort DP.
-   **Semi-Connected:** A graph is semi-connected if for every pair `(u, v)`, there is a path `u->v` OR `v->u`. This is true iff the condensation DAG is a single path (Hamiltonian path in DAG).

### Common Mistakes to Avoid

1.  **Stack Check:** Only update `low[u]` using `tin[v]` if `v` is currently on the stack. If `v` is visited but not on stack, it belongs to an already completed SCC.
2.  **Duplicate Edges:** The condensation graph is a simple graph. Use a Set to avoid adding `A->B` multiple times.
3.  **Recursion Limit:** For N=200,000, use iterative DFS or increase recursion limit.
