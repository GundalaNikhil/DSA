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

**Scenario Title:** The Project Dependency Game

Imagine a project management tool where tasks are nodes and dependencies are edges. You and a colleague are assigning tasks. The rule is: you pick a task, then your colleague must pick a task that depends on yours, and so on. The person who picks the final task (completing the chain) wins the "efficiency bonus" (or in this game, the person who *cannot* pick loses, so the last person to pick wins).

**Why This Problem Matters:**

- **State Space Search:** It models decision-making in environments with irreversible actions (DAGs).
- **Backward Induction:** The core logic is working backwards from terminal states to determine the value of earlier states.

![Real-World Application](../images/GMT-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Winning/Losing Propagation

```
Graph: 0 -> 1 -> 2 <- 3
       |
       v
       4

Analysis:
- Node 2: No outgoing edges. Terminal. -> LOSING (L)
- Node 4: No outgoing edges. Terminal. -> LOSING (L)
- Node 1: Edge to 2 (L). Can move to L. -> WINNING (W)
- Node 3: Edge to 2 (L). Can move to L. -> WINNING (W)
- Node 0: Edges to 1 (W) and 4 (L).
  - Move to 1 gives opponent W (Bad).
  - Move to 4 gives opponent L (Good).
  - Since there is a move to L, 0 is -> WINNING (W)
```

## ✅ Input/Output Clarifications

- **Losing State:** A node with `out_degree = 0`.
- **Winning State:** A node with at least one neighbor that is a Losing State.
- **Losing State (Recursive):** A node where ALL neighbors are Winning States.

## Optimal Approach

### Key Insight

Since the graph is a DAG, there are no cycles. We can use **Memoization** (DFS) or **Topological Sort** (reverse order) to compute the state of each node.
Memoization is often easier to implement.

State Logic:
- `solve(u)`:
  - If `u` has no neighbors, return `False` (Losing).
  - Iterate through all neighbors `v` of `u`.
  - If `!solve(v)` (i.e., moving to `v` forces opponent to lose), then return `True` (Winning).
  - If all neighbors return `True` (all moves lead to opponent winning), return `False`.

### Algorithm

1.  Build adjacency list `adj`.
2.  Initialize a `memo` array with -1 (unknown).
3.  For each node `i` from 0 to `n-1`, call `dfs(i)`.
4.  `dfs(u)`:
    - If `memo[u]` != -1, return it.
    - `is_winning = False`
    - For `v` in `adj[u]`:
        - If `!dfs(v)`:
            - `is_winning = True`
            - Break
    - `memo[u] = is_winning`
    - Return `is_winning`

### Time Complexity

- **O(N + M)**: Each node and edge is visited once.

### Space Complexity

- **O(N + M)**: For adjacency list and recursion stack/memoization.

![Algorithm Visualization](../images/GMT-002/algorithm-visualization.png)

## Implementations

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

public class Main {
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

### Python

```python
from typing import List
import sys

# Increase recursion depth for deep DAGs
sys.setrecursionlimit(200005)

def determine_winning_nodes(n: int, edges: List[List[int]]) -> List[str]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    
    memo = {}

    def dfs(u):
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

## 🧪 Test Case Walkthrough

**Input:** `3 nodes, 0->1, 1->2`

1.  `dfs(2)`: No neighbors. Returns `False` (Losing).
2.  `dfs(1)`: Neighbor 2. `dfs(2)` is `False`. Since neighbor is Losing, `dfs(1)` returns `True` (Winning).
3.  `dfs(0)`: Neighbor 1. `dfs(1)` is `True`. All neighbors are Winning. `dfs(0)` returns `False` (Losing).

Result: `Losing Winning Losing`

If the user prompt example `0->1, 1->2` output `node0 winning`, then the graph must be different or I misunderstood.
However, for `0->1->2`, 0 is definitely Losing.
If the graph was `0->1, 0->2`, then:
- 2: L
- 1: L
- 0: moves to 1(L) or 2(L). Since it can move to L, it is W.
So `Winning Losing Losing`.
I will stick to the logic `Losing Winning Losing` for `0->1->2` as it is mathematically correct.

## ✅ Proof of Correctness

- **Base Case:** Terminal nodes are Losing (no moves).
- **Inductive Step:**
  - If a node has a move to a Losing node, the current player takes that move, forcing the opponent into a Losing state. Thus, current is Winning.
  - If all moves lead to Winning nodes, the opponent will always receive a Winning state. Thus, current is Losing.
This covers all cases for a finite DAG.

## 💡 Interview Extensions

- **Extension 1:** What if the graph has cycles?
  - *Answer:* The game might not end (Draw). We need to handle cycles (states that are neither W nor L).
- **Extension 2:** What if we want to calculate the Grundy number (Mex)?
  - *Answer:* `G(u) = mex({G(v) for v in adj[u]})`. Useful if playing sums of games.

### Common Mistakes

1.  **Confusing W/L:**
    - ❌ Wrong: "If I can move to a Winning node, I win."
    - ✅ Correct: "If I can move to a *Losing* node (for the opponent), I win."

2.  **Not handling disconnected components:**
    - The problem asks for the status of *each* node as a starting point, so we iterate all nodes.

## Related Concepts

- **Minimax**
- **Topological Sort**
- **Memoization**
