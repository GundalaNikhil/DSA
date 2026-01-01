---
problem_id: GMT_TOKEN_WALK_DAG__2847
display_id: GMT-002
slug: token-walk-directed-graph
title: "Token Walk on Directed Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
tags:
  - dag
  - topological-sort
  - memoization
premium: true
subscription_tier: basic
---

# GMT-002: Token Walk on Directed Graph

## 📋 Problem Summary

Given a Directed Acyclic Graph (DAG), determine for every node whether the first player wins or loses if the game starts at that node. Players take turns moving a token along directed edges. A player who cannot move loses.

## 🌍 Real-World Scenario

**Scenario Title:** The Career Path Game

Imagine you and your friend are planning career moves in a company. The company has a hierarchy (DAG) where each position can lead to specific higher positions. You start at a position and take turns "promoting" to the next role.

**Real-Life Example:**
- Positions: Intern → Junior Dev → Senior Dev → Team Lead
- You start as Intern
- Player 1 moves to Junior Dev
- Player 2 moves to Senior Dev  
- Player 1 moves to Team Lead
- Player 2 is stuck (Team Lead has no further promotions) → Player 2 loses!

**Why This Matters:**
- **Decision Trees:** Models sequential decision-making with no loops
- **Backward Induction:** Solving from end states backward
- **Strategic Planning:** Understanding which starting positions are advantageous

![Real-World Application](../images/GMT-002/real-world-scenario.png)

## Detailed Explanation

### Concept: Winning vs Losing Positions

In game theory:
- **Losing Position (L)**: No matter what you do, your opponent can win
- **Winning Position (W)**: You have at least one move that puts your opponent in a losing position

### Algorithm Flow Diagram

```
┌─────────────────────────────────┐
│  Start: Analyze all nodes       │
└──────────────┬──────────────────┘
               │
               ▼
       ┌───────────────────┐
       │ Build adjacency   │
       │ list from edges   │
       └───────┬───────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ For each node i:          │
       │   Compute dfs(i)          │
       └───────┬───────────────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ dfs(u):                   │
       │   Already computed?       │
       └───────┬───────────────────┘
               │
        ┌──────┴──────┐
       YES            NO
        │              │
        ▼              ▼
    Return      ┌─────────────────┐
    memo[u]     │ Check neighbors │
                └─────┬───────────┘
                      │
                      ▼
              ┌───────────────────┐
              │ Any neighbor is   │
              │ Losing?           │
              └───────┬───────────┘
                      │
               ┌──────┴──────┐
              YES            NO
               │              │
               ▼              ▼
           Winning        Losing
           (return T)     (return F)
```

### Graph State Propagation Example

```
Graph:  0 → 1 → 2
        ↓
        3

Step 1: Analyze terminal nodes (no outgoing edges)
  Node 2: No moves → LOSING (L)
  Node 3: No moves → LOSING (L)

Step 2: Analyze nodes with edges to terminals
  Node 1: Can move to 2 (L) → WINNING (W)
  
Step 3: Analyze remaining nodes
  Node 0: Can move to 1 (W) or 3 (L)
          Has move to L → WINNING (W)

Final: [W, W, L, L]
```

## ✅ Input/Output Clarifications

- **DAG Guarantee:** No cycles exist, game always terminates
- **Terminal Nodes:** Nodes with no outgoing edges are always Losing
- **Output Format:** Space-separated "Winning" or "Losing" for each node 0 to n-1
- **Optimal Play:** Both players always make the best possible move

## Naive Approach

### Intuition

For each node, recursively check all possible game paths without memoization.

### Algorithm

```
function isWinning(node):
    if no neighbors:
        return false  // Losing position
    
    for each neighbor:
        if not isWinning(neighbor):  // Found a losing move for opponent
            return true
    
    return false  // All moves lead to opponent winning
```

### Time Complexity

- **O(N × 2^M)**: Without memoization, we may recompute the same node exponentially many times
- For dense graphs, this becomes impractical

### Space Complexity

- **O(N)**: Recursion depth

### Limitations

- **Redundant Computation:** Same nodes computed multiple times
- **Too Slow:** For large graphs with many paths

## Optimal Approach

### Key Insight

Use **memoization** to store the result for each node. Since the graph is a DAG:
1. Each node's state depends only on its neighbors
2. No cycles mean we can compute states without infinite loops
3. Once computed, a node's state never changes

**State Logic:**
- If a node has **no neighbors** → Losing (can't move)
- If a node can reach **at least one Losing neighbor** → Winning (force opponent to lose)
- If **all neighbors are Winning** → Losing (opponent always gets winning position)

### Algorithm Steps

1. **Build adjacency list** from edges
2. **Initialize memo array** with -1 (unknown state)
3. **For each node** 0 to n-1, call `dfs(node)`
4. **DFS Logic:**
   - If already computed, return memoized result
   - Check all neighbors
   - If any neighbor is Losing, current node is Winning
   - If all neighbors are Winning, current node is Losing
   - Memoize and return result

### Time Complexity

- **O(N + M)**: Each node visited once, each edge checked once
- Memoization ensures no redundant computation

### Space Complexity

- **O(N + M)**: Adjacency list + memo array + recursion stack

### Complexity Visualization

| Graph Size | Naive (worst case) | Optimal O(N+M) | Speedup |
|-----------:|-------------------:|---------------:|--------:|
| N=100, M=200 | ~2^200 | 300 | Massive |
| N=1000, M=2000 | Impossible | 3,000 | ✅ |
| N=10^5, M=2×10^5 | Impossible | 300,000 | ✅ |

![Algorithm Visualization](../images/GMT-002/algorithm-visualization.png)

## Implementations

### Python

```python
from typing import List
import sys

# Increase recursion depth for deep DAGs
sys.setrecursionlimit(200005)

def determine_winning_nodes(n: int, edges: List[List[int]]) -> List[str]:
    """
    Determine winning/losing status for each node in a DAG.
    
    Args:
        n: Number of nodes
        edges: List of directed edges [u, v]
    
    Returns:
        List of "Winning" or "Losing" for each node
    """
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    
    memo = {}

    def dfs(u):
        """Returns True if node u is a winning position"""
        if u in memo:
            return memo[u]
        
        # Default is Losing (if no moves)
        is_winning = False
        for v in adj[u]:
            # If any neighbor is Losing, then u is Winning
            if not dfs(v):
                is_winning = True
                break
        
        memo[u] = is_winning
        return is_winning

    result = []
    for i in range(n):
        if dfs(i):
            result.append("Winning")
        else:
            result.append("Losing")
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
            edges.append([u, v])
            
        result = determine_winning_nodes(n, edges)
        print(" ".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### Java

```java
import java.util.*;

class Solution {
    List<Integer>[] adj;
    int[] memo; // -1: unknown, 0: Losing, 1: Winning

    public List<String> determineWinningNodes(int n, int[][] edges) {
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
        }

        memo = new int[n];
        Arrays.fill(memo, -1);

        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (dfs(i)) result.add("Winning");
            else result.add("Losing");
        }
        return result;
    }

    private boolean dfs(int u) {
        if (memo[u] != -1) return memo[u] == 1;

        boolean canReachLosing = false;
        for (int v : adj[u]) {
            if (!dfs(v)) { // If v is Losing
                canReachLosing = true;
                break;
            }
        }

        memo[u] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] edges = new int[m][2];
            for (int i = 0; i < m; i++) {
                edges[i][0] = sc.nextInt();
                edges[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            List<String> result = solution.determineWinningNodes(n, edges);
            
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<int> memo; // -1: unknown, 0: Losing, 1: Winning

    bool dfs(int u) {
        if (memo[u] != -1) return memo[u] == 1;

        bool canReachLosing = false;
        for (int v : adj[u]) {
            if (!dfs(v)) {
                canReachLosing = true;
                break;
            }
        }

        memo[u] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }

public:
    vector<string> determineWinningNodes(int n, vector<vector<int>>& edges) {
        adj.assign(n, vector<int>());
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
        }

        memo.assign(n, -1);
        vector<string> result;
        for (int i = 0; i < n; i++) {
            if (dfs(i)) result.push_back("Winning");
            else result.push_back("Losing");
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<vector<int>> edges(m, vector<int>(2));
        for (int i = 0; i < m; i++) {
            cin >> edges[i][0] >> edges[i][1];
        }
        
        Solution solution;
        vector<string> result = solution.determineWinningNodes(n, edges);
        
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  determineWinningNodes(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
    }

    const memo = new Int8Array(n).fill(-1); // -1: unknown, 0: Losing, 1: Winning

    const dfs = (u) => {
      if (memo[u] !== -1) return memo[u] === 1;

      let canReachLosing = false;
      for (const v of adj[u]) {
        if (!dfs(v)) {
          canReachLosing = true;
          break;
        }
      }

      memo[u] = canReachLosing ? 1 : 0;
      return canReachLosing;
    };

    const result = [];
    for (let i = 0; i < n; i++) {
      result.push(dfs(i) ? "Winning" : "Losing");
    }
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  // Flatten data
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const m = parseInt(flatData[idx++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
      const u = parseInt(flatData[idx++]);
      const v = parseInt(flatData[idx++]);
      edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.determineWinningNodes(n, edges);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** 
```
3 2
0 1
1 2
```

### Step-by-Step Execution Table

| Step | Node | Neighbors | DFS Calls | Neighbor States | Result | Explanation |
|-----:|:----:|:----------|:----------|:----------------|:------:|:------------|
| 1    | 2    | []        | -         | -               | L      | No moves, terminal node |
| 2    | 1    | [2]       | dfs(2)    | 2 is L          | W      | Can move to Losing node |
| 3    | 0    | [1]       | dfs(1)    | 1 is W          | L      | All moves lead to Winning |

### State Propagation Visualization

```
Initial Graph:
  0 → 1 → 2

Step 1: Terminal Analysis
  Node 2: [] → LOSING
  
  0 → 1 → [2:L]

Step 2: Backward Propagation
  Node 1: Can reach 2(L) → WINNING
  
  0 → [1:W] → [2:L]

Step 3: Final Propagation
  Node 0: Can only reach 1(W) → LOSING
  
  [0:L] → [1:W] → [2:L]

Output: "Losing Winning Losing"
```

**Conclusion:** Starting from node 0 is Losing, node 1 is Winning, node 2 is Losing.

## ⚠️ Common Mistakes to Avoid

### 1. Confusing Winning/Losing Logic

**❌ Wrong Approach:**
```python
# Incorrect: thinking if I can move to Winning, I win
for v in adj[u]:
    if dfs(v):  # WRONG! This checks if neighbor is Winning
        is_winning = True
```

**✅ Correct Approach:**
```python
# Correct: if I can move to Losing, I win
for v in adj[u]:
    if not dfs(v):  # Correct! Check if neighbor is Losing
        is_winning = True
        break
```

**Why it matters:** You want to force your opponent into a Losing position, not a Winning one!

**Example:** If node 1 is Winning and you move there, your opponent is now in a Winning position (bad for you!).

### 2. Forgetting Memoization

**❌ Wrong Approach:**
```python
def dfs(u):
    # No memoization check!
    is_winning = False
    for v in adj[u]:
        if not dfs(v):
            is_winning = True
    return is_winning
```

**✅ Correct Approach:**
```python
def dfs(u):
    if u in memo:  # Check memo first!
        return memo[u]
    # ... compute ...
    memo[u] = is_winning
    return is_winning
```

**Why it matters:** Without memoization, you recompute the same nodes exponentially many times, causing TLE.

**Example:** In a graph where many nodes point to the same node, that node gets recomputed for each parent.

### 3. Not Handling Isolated Nodes

**❌ Wrong Approach:**
```python
# Assuming all nodes have edges
for u, v in edges:
    adj[u].append(v)
# What if a node has no outgoing edges?
```

**✅ Correct Approach:**
```python
# Initialize adjacency list for ALL nodes
adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)
# Now isolated nodes have empty lists
```

**Why it matters:** Nodes with no outgoing edges are terminal (Losing) nodes. Missing initialization causes errors.

**Example:** Node 5 exists but has no edges → should be Losing, not undefined.

### 4. Incorrect Output Format

**❌ Wrong Approach:**
```python
# Printing each result on new line
for i in range(n):
    print("Winning" if dfs(i) else "Losing")
```

**✅ Correct Approach:**
```python
# Space-separated on single line
result = []
for i in range(n):
    result.append("Winning" if dfs(i) else "Losing")
print(" ".join(result))
```

**Why it matters:** Problem expects space-separated output on one line.

**Example:** Expected: `"Losing Winning Losing"`, not three separate lines.

## 💡 Interview Extensions

### 1. What if the graph has cycles?

**Question:** How would you handle a graph with cycles?

**Answer:** Cycles introduce the possibility of **draws** (infinite games). You'd need to:
```python
# Track nodes currently in recursion stack
in_stack = set()

def dfs(u):
    if u in in_stack:
        return "Draw"  # Cycle detected
    if u in memo:
        return memo[u]
    
    in_stack.add(u)
    # ... compute ...
    in_stack.remove(u)
    memo[u] = result
    return result
```

A node in a cycle that can only reach itself or other cycle nodes is a Draw.

### 2. Can we compute Grundy numbers instead?

**Question:** How would you compute Grundy numbers for each node?

**Answer:**
```python
def compute_grundy(u):
    if u in memo:
        return memo[u]
    
    # Collect Grundy numbers of all neighbors
    reachable = set()
    for v in adj[u]:
        reachable.add(compute_grundy(v))
    
    # Compute mex
    mex = 0
    while mex in reachable:
        mex += 1
    
    memo[u] = mex
    return mex
```

Grundy number 0 = Losing, >0 = Winning. Useful for combining multiple games.

### 3. What about undirected graphs?

**Question:** How does the problem change for undirected graphs?

**Answer:** Undirected graphs are much more complex:
- Need to track which node you came from to avoid immediate backtracking
- May have cycles (draws possible)
- State becomes (current_node, previous_node)
- Memoization becomes 2D: `memo[u][parent]`

### 4. Can we use topological sort instead of DFS?

**Question:** Can we solve this iteratively using topological sort?

**Answer:** Yes! Process nodes in reverse topological order:
```python
# Compute in-degrees and topological order
topo_order = topological_sort(adj, n)

# Process in reverse order
for u in reversed(topo_order):
    is_winning = False
    for v in adj[u]:
        if not state[v]:  # v is Losing
            is_winning = True
            break
    state[u] = is_winning
```

This avoids recursion and is sometimes clearer.
