---
problem_id: GMT_KAYLES_GRAPH__8203
display_id: GMT-008
slug: kayles-on-graph
title: "Kayles on Graph"
difficulty: Hard
difficulty_score: 65
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
  - Bitmask
tags:
  - impartial-game
  - sprague-grundy
  - state-compression
premium: true
subscription_tier: basic
---

# GMT-008: Kayles on Graph

## 📋 Problem Summary

Pick a node `u` in a graph. Remove `u` and all its neighbors. Last player to move wins.

## 🌍 Real-World Scenario

**Scenario Title:** The Network Disruption

Imagine a network of servers. You launch a virus at a server `u`. The virus destroys `u` and spreads to all directly connected servers, destroying them too. You and an opponent take turns launching viruses. The one who clears the last server wins (or the one who cannot find a target loses).

**Why This Problem Matters:**

- **Dominating Set:** The game is related to finding independent sets and dominating sets.
- **Bitmask DP:** Essential technique for small constraint problems involving subsets.

![Real-World Application](../images/GMT-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Move Effect

```
Graph: 0 -- 1 -- 2
       |
       3

Move: Pick 1.
- Removes 1.
- Removes neighbors of 1: 0, 2.
- Remaining: 3 (since 3 is connected to 0, not 1? Wait. 0 is removed. 3 is connected to 0. Is 3 removed?)
  - Rule: "Removes u and all its neighbors".
  - Neighbors of 1 are 0, 2.
  - So 1, 0, 2 are removed.
  - 3 is NOT a neighbor of 1.
  - So 3 remains.
```

## ✅ Input/Output Clarifications

- **Available Node:** A node not yet removed.
- **Neighbors:** Neighbors in the original graph (or current? Neighbors are defined by edges. If `v` is removed, edge `u-v` is gone. But "neighbors" usually refers to the set of nodes adjacent to `u` in the current graph. Since we remove `u` and neighbors simultaneously, it's the same).

## Optimal Approach

### Key Insight

Since `n <= 15`, we can use a **Bitmask** to represent the set of available nodes.
`mask` has bit `i` set if node `i` is available.
We can compute `Win/Loss` (or Grundy numbers) for each mask.
Since it's a single game (not sum of games), boolean Win/Loss is sufficient.
`dp[mask] = True` if there exists a move `u` (where `mask & (1<<u)`) such that `dp[next_mask]` is False.
`next_mask = mask & ~((1<<u) | neighbors_mask[u])`.

### Algorithm

1.  Precompute `adj[u]` as a bitmask for each node `u`.
2.  Initialize `memo` array of size `2^n` with -1.
3.  `solve(mask)`:
    - If `mask == 0`, return False (Losing).
    - If `memo[mask]` != -1, return it.
    - Iterate `u` from 0 to `n-1`.
    - If `(mask >> u) & 1`:
        - `remove_mask = (1 << u) | adj[u]`.
        - `next_mask = mask & ~remove_mask`.
        - If `!solve(next_mask)`:
            - `memo[mask] = True`.
            - Return True.
    - `memo[mask] = False`.
    - Return False.

### Time Complexity

- **O(2^N * N)**: There are `2^N` states. For each state, we try `N` moves.
- `2^15 * 15 ≈ 32768 * 15 ≈ 5 * 10^5`. Very fast.

### Space Complexity

- **O(2^N)**: For memoization array.

![Algorithm Visualization](../images/GMT-008/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    int[] adjMask;
    int[] memo; // -1: unknown, 0: Losing, 1: Winning

    public String kaylesOnGraph(int n, int[][] edges) {
        adjMask = new int[n];
        for (int[] e : edges) {
            adjMask[e[0]] |= (1 << e[1]);
            adjMask[e[1]] |= (1 << e[0]);
        }

        memo = new int[1 << n];
        Arrays.fill(memo, -1);

        return canWin((1 << n) - 1, n) ? "First" : "Second";
    }

    private boolean canWin(int mask, int n) {
        if (mask == 0) return false;
        if (memo[mask] != -1) return memo[mask] == 1;

        boolean canReachLosing = false;
        for (int u = 0; u < n; u++) {
            if ((mask & (1 << u)) != 0) {
                int removeMask = (1 << u) | adjMask[u];
                int nextMask = mask & ~removeMask;
                if (!canWin(nextMask, n)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[mask] = canReachLosing ? 1 : 0;
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
            System.out.println(solution.kaylesOnGraph(n, edges));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def kayles_on_graph(n: int, edges: List[List[int]]) -> str:
    adj_mask = [0] * n
    for u, v in edges:
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    memo = {}

    def can_win(mask):
        if mask == 0:
            return False
        if mask in memo:
            return memo[mask]
        
        for u in range(n):
            if (mask >> u) & 1:
                remove_mask = (1 << u) | adj_mask[u]
                next_mask = mask & ~remove_mask
                if not can_win(next_mask):
                    memo[mask] = True
                    return True
        
        memo[mask] = False
        return False

    return "First" if can_win((1 << n) - 1) else "Second"

def main():
    import sys
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
            
        print(kayles_on_graph(n, edges))
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
    vector<int> adjMask;
    vector<int> memo; // -1: unknown, 0: Losing, 1: Winning

    bool canWin(int mask, int n) {
        if (mask == 0) return false;
        if (memo[mask] != -1) return memo[mask] == 1;

        bool canReachLosing = false;
        for (int u = 0; u < n; u++) {
            if ((mask >> u) & 1) {
                int removeMask = (1 << u) | adjMask[u];
                int nextMask = mask & ~removeMask;
                if (!canWin(nextMask, n)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[mask] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }

public:
    string kaylesOnGraph(int n, vector<vector<int>>& edges) {
        adjMask.assign(n, 0);
        for (const auto& e : edges) {
            adjMask[e[0]] |= (1 << e[1]);
            adjMask[e[1]] |= (1 << e[0]);
        }

        memo.assign(1 << n, -1);
        return canWin((1 << n) - 1, n) ? "First" : "Second";
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
        cout << solution.kaylesOnGraph(n, edges) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kaylesOnGraph(n, edges) {
    const adjMask = new Int32Array(n);
    for (const [u, v] of edges) {
      adjMask[u] |= (1 << v);
      adjMask[v] |= (1 << u);
    }

    const memo = new Int8Array(1 << n).fill(-1); // -1: unknown, 0: Losing, 1: Winning

    const canWin = (mask) => {
      if (mask === 0) return false;
      if (memo[mask] !== -1) return memo[mask] === 1;

      let canReachLosing = false;
      for (let u = 0; u < n; u++) {
        if ((mask & (1 << u)) !== 0) {
          const removeMask = (1 << u) | adjMask[u];
          const nextMask = mask & ~removeMask;
          if (!canWin(nextMask)) {
            canReachLosing = true;
            break;
          }
        }
      }

      memo[mask] = canReachLosing ? 1 : 0;
      return canReachLosing;
    };

    return canWin((1 << n) - 1) ? "First" : "Second";
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
      const u = parseInt(flatData[idx++]);
      const v = parseInt(flatData[idx++]);
      edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.kaylesOnGraph(n, edges));
});
```

## 🧪 Test Case Walkthrough

**Input:** `3 nodes, 0-1, 1-2`

1.  Start `mask = 111` (binary 7).
2.  Moves:
    - Pick 0: Remove 0, 1. `next = 100` (4). `solve(4)` (Node 2 left).
      - From 4: Pick 2. `next = 0`. `solve(0)` is False.
      - So `solve(4)` is True.
    - Pick 1: Remove 1, 0, 2. `next = 0`.
      - `solve(0)` is False.
      - So `solve(7)` sees move to False. Returns True.
3.  Result: First.

## ✅ Proof of Correctness

- **Small N:** Allows full state exploration.
- **Bitmask:** Correctly tracks available nodes.
- **Impartial:** Standard W/L logic applies.

## 💡 Interview Extensions

- **Extension 1:** What if `N` is larger but graph is a tree?
  - *Answer:* Use Tree DP. `dp[u][state]` where state indicates if `u` or parent is removed.
- **Extension 2:** What if we calculate Grundy numbers?
  - *Answer:* Needed if graph is disconnected and we treat components as subgames.

### C++ommon Mistakes

1.  **Removing wrong nodes:**
    - ❌ Wrong: Removing only `u`.
    - ✅ Correct: Remove `u` AND neighbors.
2.  **Bitwise precedence:**
    - ❌ Wrong: `mask & 1 << u` (might be interpreted as `(mask & 1) << u`).
    - ✅ Correct: `mask & (1 << u)`.

## Related Concepts

- **Bitmask DP**
- **Independent Set**
