---
problem_id: GRB_TWO_SAT_AMO__6607
display_id: GRB-013
slug: two-sat-amo
title: "2-SAT with At-Most-One Constraints"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - 2-SAT
  - Implication Graph
tags:
  - graphs-basics
  - 2-sat
  - implications
  - medium
premium: true
subscription_tier: basic
---

# GRB-013: 2-SAT with At-Most-One Constraints

## 📋 Problem Summary

You are given a boolean formula with two types of constraints:
1.  **2-SAT Clauses:** `(a OR b)`
2.  **At-Most-One (AMO) Groups:** For a given set of variables, at most one can be true.

Determine if the formula is satisfiable and provide a valid assignment.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Scheduling

Imagine you are scheduling talks for a conference.
-   **Variables:** `x_i` means "Talk i is scheduled in Slot A". `¬x_i` means "Talk i is scheduled in Slot B".
-   **2-SAT Constraints:** "Talk 1 and Talk 2 cannot both be in Slot A" -> `(¬x1 OR ¬x2)`. "Talk 3 must be in Slot B or Talk 4 in Slot A" -> `(¬x3 OR x4)`.
-   **AMO Constraints:** "Talks 5, 6, and 7 are by the same speaker, so at most one of them can be in Slot A (if Slot A is the morning session)".
-   Solving this ensures a conflict-free schedule.

![Real-World Application](../images/GRB-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Implication Graph:**
Clause `(A OR B)` is equivalent to:
-   `¬A => B` (If A is false, B must be true)
-   `¬B => A` (If B is false, A must be true)

**AMO Constraint:** `{x1, x2, x3}`
-   If `x1` is true, `x2` must be false (`x1 => ¬x2`).
-   If `x1` is true, `x3` must be false (`x1 => ¬x3`).
-   If `x2` is true, `x3` must be false (`x2 => ¬x3`).
-   ...and so on for all pairs.

**Graph Structure:**
Nodes `1..N` (True literals) and `N+1..2N` (False literals).
Edges represent implications.
If `x` and `¬x` are in the same Strongly Connected Component (SCC), it's **UNSAT**.

### Algorithm Steps

1.  **Build Graph:**
    -   Nodes `1..N` represent `x_i`. Nodes `N+1..2N` represent `¬x_i`.
    -   For each clause `(a OR b)`: Add edges `¬a -> b` and `¬b -> a`.
    -   For each AMO group `{v1, v2, ..., vk}`: Add edges `vi -> ¬vj` for all pairs `(i, j)`.
2.  **Find SCCs:** Use Tarjan's or Kosaraju's algorithm.
3.  **Check Satisfiability:**
    -   For every `i`, if `SCC[x_i] == SCC[¬x_i]`, return **UNSAT**.
4.  **Construct Assignment:**
    -   If `SCC[x_i] > SCC[¬x_i]` (in topological order), set `x_i = true`.
    -   Else `x_i = false`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Literals:** Input uses `1..N` and `-1..-N`. Map `-i` to node `N+i`.
-   **AMO Size:** Sum of group sizes is small (200,000), but naive pairwise edges for a large group is O(K^2).
    -   **Optimization:** For large groups, O(K^2) is too slow. We need the **Commander Variable** or **Prefix/Suffix** optimization.
    -   **Note:** The problem statement says "Total size of all groups <= 200,000". This refers to sum of K. If one group has K=200,000, K^2 edges is 4*10^10, which will cause TLE.
    -   **Optimization Required:** We must use auxiliary variables to encode AMO in O(K) edges.

### AMO Optimization (Prefix/Suffix Method)
For group `{x1, ... xk}`, we want `xi -> ¬xj` for all `i != j`.
Introduce prefix variables `p1...pk`.
-   `pi` implies "at least one of x1...xi is true".
-   `pi -> pi+1`
-   `xi -> pi`
-   `pi-1 -> ¬xi` (If any of 1..i-1 is true, xi must be false).
Total edges: O(K).

## Naive Approach

### Intuition

Add pairwise edges for AMO constraints.

### Time Complexity

-   **O(N + M + Σ K^2)**: Worst case O(N^2). Fails for large groups.

## Optimal Approach (2-SAT + AMO Optimization)

Use auxiliary variables to reduce AMO constraints to linear size.

### Prefix Optimization Logic
For group `x1, ..., xk`:
Create `k` prefix nodes `P1, ..., Pk`.
1.  **Definition:** `Pi` is true if any of `x1...xi` is true.
2.  **Chain:** `P1 -> P2 -> ... -> Pk`. (If prefix i is true, prefix i+1 is true).
3.  **Variable to Prefix:** `xi -> Pi`. (If xi is true, prefix i is true).
4.  **Exclusion:** `Pi-1 -> ¬xi`. (If prefix i-1 is true, xi must be false).

This enforces that if `xi` is true, `Pi` becomes true, which forces `Pi+1...Pk` true. Also `Pi-1` being true forces `xi` false. This ensures at most one `x` is true.

### Time Complexity

-   **O(N + M + Σ K)**: Linear in input size.

### Space Complexity

-   **O(N + M + Σ K)**.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private List<List<Integer>> adj;
    private List<List<Integer>> revAdj;
    private List<Integer> order;
    private boolean[] visited;
    private int[] component;
    private int numVars;

    public int[] solveTwoSat(int n, int[][] clauses, List<int[]> groups) {
        // Estimate total nodes needed including auxiliary
        // Base: 2*n nodes (1..n and n+1..2n for negations)
        // Aux: For each group of size k, we add k prefix variables.
        // Each prefix var has a negation. So 2*k aux nodes per group.
        
        int totalGroupSize = 0;
        for (int[] g : groups) totalGroupSize += g.length;
        
        int baseVars = n;
        int auxStart = n + 1;
        int totalVars = n + totalGroupSize;
        int totalNodes = 2 * totalVars + 2; // +2 for 1-based indexing safety
        
        adj = new ArrayList<>();
        revAdj = new ArrayList<>();
        for (int i = 0; i < totalNodes; i++) {
            adj.add(new ArrayList<>());
            revAdj.add(new ArrayList<>());
        }

        // Helper to get node index
        // x_i (1..n) -> i
        // ¬x_i -> i + totalVars
        // aux_j -> j
        // ¬aux_j -> j + totalVars
        int N = totalVars;
        
        // Add Clauses
        for (int[] clause : clauses) {
            addClause(clause[0], clause[1], N);
        }

        // Add AMO Constraints with Prefix Optimization
        int currentAux = auxStart;
        for (int[] group : groups) {
            int k = group.length;
            if (k <= 1) continue;
            
            // Prefix variables: currentAux ... currentAux + k - 1
            // P_i corresponds to variable group[i]
            
            for (int i = 0; i < k; i++) {
                int x = group[i]; // Literal index (could be negative? Problem says indices 1-based, usually positive for AMO)
                // Assuming AMO inputs are variable indices (positive).
                // If input can be literals, we handle sign.
                // Problem says "integer k followed by k variable indices". Indices usually mean x_i.
                
                int p = currentAux + i;
                
                // 1. x_i -> P_i
                addImplication(x, p, N);
                
                // 2. P_i -> P_{i+1}
                if (i < k - 1) {
                    addImplication(p, p + 1, N);
                }
                
                // 3. P_{i-1} -> ¬x_i
                if (i > 0) {
                    addImplication(p - 1, -x, N);
                }
            }
            currentAux += k;
        }

        // SCC (Kosaraju's)
        order = new ArrayList<>();
        visited = new boolean[totalNodes];
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) dfs1(i);
            if (!visited[i + N]) dfs1(i + N);
        }
        
        Collections.reverse(order);
        component = new int[totalNodes];
        Arrays.fill(component, -1);
        int compCount = 0;
        
        for (int u : order) {
            if (component[u] == -1) {
                dfs2(u, compCount++);
            }
        }

        // Check Satisfiability
        int[] result = new int[n];
        for (int i = 1; i <= n; i++) {
            if (component[i] == component[i + N]) return null;
            result[i - 1] = component[i] > component[i + N] ? 1 : 0;
        }
        
        return result;
    }

    private void addClause(int a, int b, int N) {
        // a OR b  <=>  ¬a -> b  AND  ¬b -> a
        addEdge(neg(a, N), map(b, N));
        addEdge(neg(b, N), map(a, N));
    }
    
    private void addImplication(int a, int b, int N) {
        // a -> b  <=>  ¬b -> ¬a
        addEdge(map(a, N), map(b, N));
        addEdge(neg(b, N), neg(a, N));
    }

    private void addEdge(int u, int v) {
        adj.get(u).add(v);
        revAdj.get(v).add(u);
    }

    private int map(int literal, int N) {
        if (literal > 0) return literal;
        return -literal + N;
    }

    private int neg(int literal, int N) {
        if (literal > 0) return literal + N;
        return -literal;
    }

    private void dfs1(int u) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs1(v);
        }
        order.add(u);
    }

    private void dfs2(int u, int c) {
        component[u] = c;
        for (int v : revAdj.get(u)) {
            if (component[v] == -1) dfs2(v, c);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] clauses = new int[m][2];
        for (int i = 0; i < m; i++) {
            clauses[i][0] = sc.nextInt();
            clauses[i][1] = sc.nextInt();
        }
        int g = sc.nextInt();
        List<int[]> groups = new ArrayList<>();
        for (int i = 0; i < g; i++) {
            int k = sc.nextInt();
            int[] vars = new int[k];
            for (int j = 0; j < k; j++) vars[j] = sc.nextInt();
            groups.add(vars);
        }

        Solution solution = new Solution();
        int[] assign = solution.solveTwoSat(n, clauses, groups);
        if (assign == null) {
            System.out.print("UNSAT");
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("SAT\n");
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(assign[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(400000)

def solve_two_sat(n: int, clauses: list[tuple[int, int]], groups: list[list[int]]):
    total_group_size = sum(len(g) for g in groups)
    N = n + total_group_size
    
    adj = [[] for _ in range(2 * N + 2)]
    rev_adj = [[] for _ in range(2 * N + 2)]
    
    def add_edge(u, v):
        adj[u].append(v)
        rev_adj[v].append(u)
        
    def get_node(lit):
        if lit > 0: return lit
        return -lit + N
        
    def get_neg(lit):
        if lit > 0: return lit + N
        return -lit
        
    def add_implication(a, b):
        u, v = get_node(a), get_node(b)
        not_b, not_a = get_neg(b), get_neg(a)
        add_edge(u, v)
        add_edge(not_b, not_a)
        
    def add_clause(a, b):
        # a or b <=> -a -> b
        add_implication(-a, b)
        
    # Add Clauses
    for a, b in clauses:
        add_clause(a, b)
        
    # Add AMO
    current_aux = n + 1
    for group in groups:
        k = len(group)
        if k <= 1: continue
        
        for i in range(k):
            x = group[i]
            p = current_aux + i
            
            # x -> P_i
            add_implication(x, p)
            
            # P_i -> P_{i+1}
            if i < k - 1:
                add_implication(p, p + 1)
                
            # P_{i-1} -> -x
            if i > 0:
                add_implication(p - 1, -x)
                
        current_aux += k
        
    # SCC (Kosaraju)
    visited = [False] * (2 * N + 2)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(1, 2 * N + 1):
        if not visited[i]:
            dfs1(i)
            
    component = [-1] * (2 * N + 2)
    comp_count = 0
    
    def dfs2(u, c):
        component[u] = c
        for v in rev_adj[u]:
            if component[v] == -1:
                dfs2(v, c)
                
    for i in range(len(order) - 1, -1, -1):
        u = order[i]
        if component[u] == -1:
            dfs2(u, comp_count)
            comp_count += 1
            
    # Check
    result = []
    for i in range(1, n + 1):
        if component[i] == component[i + N]:
            return None
        result.append(1 if component[i] > component[i + N] else 0)
        
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
        clauses = []
        for _ in range(m):
            a = int(next(iterator))
            b = int(next(iterator))
            clauses.append((a, b))
            
        g = int(next(iterator))
        groups = []
        for _ in range(g):
            k = int(next(iterator))
            vars_list = [int(next(iterator)) for _ in range(k)]
            groups.append(vars_list)
            
        assign = solve_two_sat(n, clauses, groups)
        if assign is None:
            print("UNSAT")
        else:
            print("SAT")
            print(" ".join(map(str, assign)))
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
    vector<vector<int>> adj, revAdj;
    vector<int> order, component;
    vector<bool> visited;
    int N;

    int map(int literal) {
        if (literal > 0) return literal;
        return -literal + N;
    }

    int neg(int literal) {
        if (literal > 0) return literal + N;
        return -literal;
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        revAdj[v].push_back(u);
    }

    void addImplication(int a, int b) {
        // a -> b  <=>  ¬b -> ¬a
        addEdge(map(a), map(b));
        addEdge(neg(b), neg(a));
    }

    void dfs1(int u) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) dfs1(v);
        }
        order.push_back(u);
    }

    void dfs2(int u, int c) {
        component[u] = c;
        for (int v : revAdj[u]) {
            if (component[v] == -1) dfs2(v, c);
        }
    }

public:
    vector<int> solveTwoSat(int n, const vector<pair<int, int>>& clauses,
                            const vector<vector<int>>& groups) {
        int totalGroupSize = 0;
        for (const auto& g : groups) totalGroupSize += g.size();

        N = n + totalGroupSize;
        int totalNodes = 2 * N + 2;

        adj.assign(totalNodes, vector<int>());
        revAdj.assign(totalNodes, vector<int>());

        // Clauses
        for (const auto& p : clauses) {
            // a OR b <=> ¬a -> b
            addImplication(-p.first, p.second);
        }

        // AMO
        int currentAux = n + 1;
        for (const auto& group : groups) {
            int k = group.size();
            if (k <= 1) continue;

            for (int i = 0; i < k; i++) {
                int x = group[i];
                int p = currentAux + i;

                // x -> P_i
                addImplication(x, p);

                // P_i -> P_{i+1}
                if (i < k - 1) {
                    addImplication(p, p + 1);
                }

                // P_{i-1} -> ¬x
                if (i > 0) {
                    addImplication(p - 1, -x);
                }
            }
            currentAux += k;
        }

        // SCC
        visited.assign(totalNodes, false);
        order.clear();
        for (int i = 1; i <= 2 * N; i++) {
            if (!visited[i]) dfs1(i);
        }

        reverse(order.begin(), order.end());
        component.assign(totalNodes, -1);
        int compCount = 0;

        for (int u : order) {
            if (component[u] == -1) {
                dfs2(u, compCount++);
            }
        }

        vector<int> result;
        for (int i = 1; i <= n; i++) {
            if (component[i] == component[i + N]) return {};
            result.push_back(component[i] > component[i + N] ? 1 : 0);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> clauses(m);
    for (int i = 0; i < m; i++) {
        cin >> clauses[i].first >> clauses[i].second;
    }
    int g;
    cin >> g;
    vector<vector<int>> groups(g);
    for (int i = 0; i < g; i++) {
        int k;
        cin >> k;
        groups[i].resize(k);
        for (int j = 0; j < k; j++) cin >> groups[i][j];
    }

    Solution solution;
    vector<int> assign = solution.solveTwoSat(n, clauses, groups);
    if (assign.empty()) {
        cout << "UNSAT";
    } else {
        cout << "SAT\n";
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << assign[i];
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solveTwoSat(n, clauses, groups) {
    let totalGroupSize = 0;
    for (const g of groups) totalGroupSize += g.length;

    const N = n + totalGroupSize;
    const totalNodes = 2 * N + 2;
    const adj = Array.from({ length: totalNodes }, () => []);
    const revAdj = Array.from({ length: totalNodes }, () => []);

    const getNode = (lit) => (lit > 0 ? lit : -lit + N);
    const getNeg = (lit) => (lit > 0 ? lit + N : -lit);

    const addEdge = (u, v) => {
      adj[u].push(v);
      revAdj[v].push(u);
    };

    const addImplication = (a, b) => {
      addEdge(getNode(a), getNode(b));
      addEdge(getNeg(b), getNeg(a));
    };

    // Clauses
    for (const [a, b] of clauses) {
      addImplication(-a, b);
    }

    // AMO
    let currentAux = n + 1;
    for (const group of groups) {
      const k = group.length;
      if (k > 1) {
        for (let i = 0; i < k; i++) {
          const x = group[i];
          const p = currentAux + i;

          addImplication(x, p);
          if (i < k - 1) addImplication(p, p + 1);
          if (i > 0) addImplication(p - 1, -x);
        }
        currentAux += k;
      }
    }

    // SCC
    const visited = new Int8Array(totalNodes).fill(0);
    const order = [];

    const dfs1 = (u) => {
      visited[u] = 1;
      for (const v of adj[u]) {
        if (!visited[v]) dfs1(v);
      }
      order.push(u);
    };

    // Use iterative DFS if stack depth is an issue, but standard recursion usually fits 10^5 in Node
    // For safety with 4*10^5 nodes, increasing stack size or iterative is better.
    // Here we use recursive for clarity.
    
    try {
        for (let i = 1; i <= 2 * N; i++) {
          if (!visited[i]) dfs1(i);
        }
    } catch(e) {
        // Fallback or error handling
        return null;
    }

    const component = new Int32Array(totalNodes).fill(-1);
    let compCount = 0;

    const dfs2 = (u, c) => {
      component[u] = c;
      for (const v of revAdj[u]) {
        if (component[v] === -1) dfs2(v, c);
      }
    };

    for (let i = order.length - 1; i >= 0; i--) {
      const u = order[i];
      if (component[u] === -1) {
        dfs2(u, compCount++);
      }
    }

    const result = [];
    for (let i = 1; i <= n; i++) {
      if (component[i] === component[i + N]) return null;
      result.push(component[i] > component[i + N] ? 1 : 0);
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
  const clauses = [];
  for (let i = 0; i < m; i++) {
    const a = parseInt(data[idx++], 10);
    const b = parseInt(data[idx++], 10);
    clauses.push([a, b]);
  }
  const g = parseInt(data[idx++], 10);
  const groups = [];
  for (let i = 0; i < g; i++) {
    const k = parseInt(data[idx++], 10);
    const varsList = [];
    for (let j = 0; j < k; j++) varsList.push(parseInt(data[idx++], 10));
    groups.push(varsList);
  }

  const solution = new Solution();
  const assign = solution.solveTwoSat(n, clauses, groups);
  if (assign === null) {
    console.log("UNSAT");
  } else {
    console.log("SAT");
    console.log(assign.join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 1
1 2
1
2 1 2
```
**Clauses:** `(1 OR 2)`
**AMO:** `{1, 2}`

**Graph Construction:**
-   Clause: `¬1 -> 2`, `¬2 -> 1`.
-   AMO (Prefix `P1, P2` for `1, 2`):
    -   `1 -> P1`
    -   `2 -> P2`
    -   `P1 -> P2`
    -   `P1 -> ¬2`

**Implications:**
-   If `1` is True:
    -   `1 -> P1` (True)
    -   `P1 -> ¬2` (True) -> `2` is False.
    -   Clause `1 OR 2` is satisfied (True OR False).
    -   Consistent.
-   If `2` is True:
    -   `2 -> P2` (True)
    -   From clause: `¬1 -> 2`.
    -   From AMO: `P1 -> ¬2`. Contrapositive `2 -> ¬P1`.
    -   `¬P1 -> ¬1`. So `2 -> ¬1`.
    -   Consistent.

**Result:** `SAT`. Assignment `1 0` or `0 1`.

## ✅ Proof of Correctness

The prefix optimization correctly encodes "At Most One":
-   If `xi` is true, `Pi` is true.
-   `Pi` implies `Pj` for all `j > i`.
-   `Pj-1` implies `¬xj`.
-   So if `xi` is true, `Pi` is true -> `Pi+1` true -> ...
-   Also `Pi` true implies `¬xi+1` true.
-   Thus `xi` true forces all subsequent `x` to be false.
-   Topological sort on SCC graph guarantees a valid truth assignment if no contradictions exist.

## 💡 Interview Extensions (High-Value Add-ons)

-   **3-SAT:** NP-Complete. 2-SAT is P.
-   **Max 2-SAT:** Finding assignment satisfying *maximum* clauses is NP-Hard.
-   **Commander Variable:** Another AMO optimization using a tree structure.

### Common Mistakes to Avoid

1.  **O(K^2) Edges:** Naively adding edges for every pair in an AMO group will TLE.
2.  **Indexing:** Mapping `¬x` to `x + N` requires careful offset management, especially with auxiliary variables.
3.  **SCC Order:** In Kosaraju's algorithm, components are found in reverse topological order. Higher component ID indicates earlier position in topological order. When `comp[x] > comp[¬x]`, variable `x` is upstream of `¬x`, implying `x -> ¬x`. To avoid contradiction (True -> True), set `x` to False. The correct assignment is `comp[x] > comp[¬x] ? 0 : 1`.
