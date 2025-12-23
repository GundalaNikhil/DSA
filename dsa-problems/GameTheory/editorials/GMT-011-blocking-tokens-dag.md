---
problem_id: GMT_BLOCKING_TOKENS__5821
display_id: GMT-011
slug: blocking-tokens-dag
title: "Blocking Tokens on DAG"
difficulty: Medium
difficulty_score: 55
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
tags:
  - impartial-game
  - memoization
  - dag
premium: true
subscription_tier: basic
---

# GMT-011: Blocking Tokens on DAG

## 📋 Problem Summary

Two tokens start on distinct nodes of a DAG. On each turn, choose one token and
move it along a directed edge to an unoccupied node. If no legal move exists,
the current player loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Narrow Corridors.

Imagine two robots navigating a facility with one-way corridors.
- They cannot occupy the same room (collision).
- They must keep moving to stay powered.
- If a robot cannot move (dead end or blocked by the other), the system fails.
- You want to force the system into a state where the opponent has no valid moves.

![Real-World Application](../images/GMT-011/real-world-scenario.png)

## Detailed Explanation

### State Representation

The state is defined by the positions of the two tokens: `(u, v)`.
Since the tokens are identical (or players can pick either), the state `(u, v)` is equivalent to `(v, u)`.
However, it's easier to implement as `(u, v)` where order doesn't matter for logic but matters for storage (e.g., store `min(u,v), max(u,v)`).

### Transitions

From state `(u, v)`:
1.  **Move u:** To any neighbor `u'` of `u`.
    - Valid only if `u' != v`.
    - New state: `(u', v)`.
2.  **Move v:** To any neighbor `v'` of `v`.
    - Valid only if `v' != u`.
    - New state: `(u, v')`.

### Winning/Losing Positions

- **Losing:** No valid moves exist.
- **Winning:** There exists at least one move to a **Losing** state.
- **Losing:** All reachable states are **Winning**.

Since it's a DAG, there are no cycles, so we can use Memoization or simple recursion.

### Complexity

- **States:** `N * N`.
- **Transitions per state:** `deg(u) + deg(v)`.
- **Total Complexity:** `O(N * (N + M))`.
- With `N=100`, this is roughly `100 * 2100 = 2.1 * 10^5` operations. Very fast.

![Algorithm Visualization](../images/GMT-011/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private List<Integer>[] adj;
    private int[][] memo; // 0: unknown, 1: losing, 2: winning

    private boolean canWin(int u, int v) {
        if (memo[u][v] != 0) return memo[u][v] == 2;

        boolean canReachLosing = false;

        // Try moving u
        for (int nextU : adj[u]) {
            if (nextU == v) continue; // Blocked
            if (!canWin(nextU, v)) {
                canReachLosing = true;
                break;
            }
        }

        // Try moving v
        if (!canReachLosing) {
            for (int nextV : adj[v]) {
                if (nextV == u) continue; // Blocked
                if (!canWin(u, nextV)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[u][v] = canReachLosing ? 2 : 1;
        return canReachLosing;
    }

    public String blockingTokens(int n, int[][] edges, int u, int v) {
        adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
        }

        memo = new int[n + 1][n + 1];
        return canWin(u, v) ? "First" : "Second";
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
            int u = sc.nextInt();
            int v = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(solution.blockingTokens(n, edges, u, v));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def blocking_tokens(n: int, edges: List[List[int]], u: int, v: int) -> str:
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
    
    # memo[u][v] stores result: None=unknown, False=Losing, True=Winning
    memo = {}

    def can_win(curr_u, curr_v):
        state = (curr_u, curr_v)
        if state in memo:
            return memo[state]
        
        # Try moving u
        for next_u in adj[curr_u]:
            if next_u == curr_v: continue
            if not can_win(next_u, curr_v):
                memo[state] = True
                return True
        
        # Try moving v
        for next_v in adj[curr_v]:
            if next_v == curr_u: continue
            if not can_win(curr_u, next_v):
                memo[state] = True
                return True
                
        memo[state] = False
        return False

    return "First" if can_win(u, v) else "Second"

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
            u_edge = int(next(iterator))
            v_edge = int(next(iterator))
            edges.append([u_edge, v_edge])
        u = int(next(iterator))
        v = int(next(iterator))
            
        print(blocking_tokens(n, edges, u, v))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<vector<int>> memo; // 0: unknown, 1: losing, 2: winning

    bool canWin(int u, int v) {
        if (memo[u][v] != 0) return memo[u][v] == 2;

        bool canReachLosing = false;

        // Try moving u
        for (int nextU : adj[u]) {
            if (nextU == v) continue;
            if (!canWin(nextU, v)) {
                canReachLosing = true;
                break;
            }
        }

        // Try moving v
        if (!canReachLosing) {
            for (int nextV : adj[v]) {
                if (nextV == u) continue;
                if (!canWin(u, nextV)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[u][v] = canReachLosing ? 2 : 1;
        return canReachLosing;
    }

public:
    string blockingTokens(int n, vector<vector<int>>& edges, int u, int v) {
        adj.assign(n + 1, vector<int>());
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
        }

        memo.assign(n + 1, vector<int>(n + 1, 0));
        return canWin(u, v) ? "First" : "Second";
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
        int u, v;
        cin >> u >> v;
        
        Solution solution;
        cout << solution.blockingTokens(n, edges, u, v) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  blockingTokens(n, edges, u, v) {
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edges) {
      adj[a].push(b);
    }

    // memo[u][v]: 0=unknown, 1=losing, 2=winning
    const memo = Array.from({ length: n + 1 }, () => new Int8Array(n + 1));

    const canWin = (currU, currV) => {
      if (memo[currU][currV] !== 0) return memo[currU][currV] === 2;

      let canReachLosing = false;

      // Try moving u
      for (const nextU of adj[currU]) {
        if (nextU === currV) continue;
        if (!canWin(nextU, currV)) {
          canReachLosing = true;
          break;
        }
      }

      // Try moving v
      if (!canReachLosing) {
        for (const nextV of adj[currV]) {
          if (nextV === currU) continue;
          if (!canWin(currU, nextV)) {
            canReachLosing = true;
            break;
          }
        }
      }

      memo[currU][currV] = canReachLosing ? 2 : 1;
      return canReachLosing;
    };

    return canWin(u, v) ? "First" : "Second";
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
      edges.push([parseInt(flatData[idx++]), parseInt(flatData[idx++])]);
  }
  const u = parseInt(flatData[idx++]);
  const v = parseInt(flatData[idx++]);

  const solution = new Solution();
  console.log(solution.blockingTokens(n, edges, u, v));
});
```

## 🧪 Test Case Walkthrough

**Input:** 4 nodes, edges 1->2, 2->3, 1->3. Tokens at 1, 2.
1.  State (1, 2).
2.  P1 moves 1->3. New state (3, 2).
3.  P2 at (3, 2).
    - Token at 3: No moves.
    - Token at 2: Move to 3? Blocked.
4.  P2 has no moves. P2 loses.
5.  P1 wins.

## ✅ Proof of Correctness

- **Impartial Game:** Moves depend only on state.
- **Finite:** DAG ensures no infinite play.
- **Memoization:** Correctly computes Win/Loss values.

## 💡 Interview Extensions

- **Extension 1:** What if graph has cycles?
  - *Answer:* Can have draws. Use iterative updates or graph coloring.
- **Extension 2:** What if we have K tokens?
  - *Answer:* State space `N^K`. Exponential.

### Common Mistakes

1.  **Ignoring Blocking:**
    - ❌ Wrong: Treating tokens as independent games.
    - ✅ Correct: Checking `next != other_pos`.
2.  **Order Matters:**
    - ❌ Wrong: Assuming `(u, v)` is different from `(v, u)` in logic (it's symmetric, but implementation usually handles ordered pair).
    - ✅ Correct: Since players can pick *either* token, `(u, v)` is effectively the same set as `(v, u)`.

## Related Concepts

- **Graph Games**
- **Memoization**
