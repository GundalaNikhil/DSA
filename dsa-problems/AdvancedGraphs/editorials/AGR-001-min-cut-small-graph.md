---
problem_id: AGR_MIN_CUT_SMALL_GRAPH__4182
display_id: AGR-001
slug: min-cut-small-graph
title: "Minimum Cut on Small Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Min Cut
  - Stoer-Wagner
tags:
  - advanced-graphs
  - min-cut
  - stoer-wagner
  - medium
premium: true
subscription_tier: basic
---

# AGR-001: Minimum Cut on Small Graph

## 📋 Problem Summary

Given an undirected weighted graph, find the **Global Minimum Cut**. This is the minimum total weight of edges that, if removed, would disconnect the graph into two non-empty components.

## 🌍 Real-World Scenario

**Scenario Title:** The Weakest Link in the Power Grid

Imagine a city's power grid where power stations and substations are connected by transmission lines. Each line has a "cost" to cut (e.g., how robust it is).
-   **Goal:** Identify the most vulnerable set of lines that, if failed (or sabotaged), would split the city's power grid into two isolated islands.
-   **Why?** By finding this "Minimum Cut", engineers know exactly where to reinforce the network to prevent a total blackout separation.

![Real-World Application](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185634/dsa-problems/AGR-001/editorial/w5iuzwibb3qes3llp9ad.jpg)

## Detailed Explanation

### Concept Visualization
![Concept Graph Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186392/dsa-problems/AGR-001/editorial/ll6zm88un3k4cqwktayh.jpg)
**Possible Cuts:**
1.  Cut `{A}` from `{B, C, D}`: Edges `(A,B), (A,C), (A,D)`. Cost: `2 + 1 + 3 = 6`.
2.  Cut `{C}` from `{A, B, D}`: Edges `(C,A), (C,D)`. Cost: `1 + 1 = 2`. **(Minimum)**

### Algorithm: Stoer-Wagner

Unlike the s-t Min Cut (which uses Max Flow), the Global Min Cut does not fix source and sink nodes. We could run s-t Min Cut for a fixed `s` and all other `t`, but that's slow. **Stoer-Wagner** is a deterministic algorithm specifically for this.

**Core Idea (Minimum Cut Phase):**
1.  Start with an arbitrary node `a`.
2.  Repeatedly add the node that is "most tightly connected" to the set of already added nodes (similar to Prim's algorithm).
3.  The **last two nodes** added to the set, say `s` and `t`, have a special property: The cut that separates `t` from the rest of the graph is a candidate for the global min cut.
4.  **Merge** `s` and `t` into a single super-node.
5.  Repeat until only one node remains. The minimum of all "cut-of-the-last-phase" values is the global answer.

### Algorithm Steps

1.  Initialize `min_cut = infinity`.
2.  While graph has > 1 node:
    -   Run **MinimumCutPhase**:
        -   Start with node 0.
        -   Maintain `weights` array (sum of edges to current set).
        -   Extract max `weight` node, add to set.
        -   Record the last two nodes added: `s` (second to last) and `t` (last).
        -   Update `min_cut = min(min_cut, weight_of_t)`.
    -   **Merge** `s` and `t`:
        -   Add all edges from `t` to `s`.
        -   Remove `t` from graph (mark as merged).

![Merge Step Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186394/dsa-problems/AGR-001/editorial/his2cdctczm35nmtqzwm.jpg)

3.  Return `min_cut`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Disconnected Graph:** If the graph is initially disconnected, the min cut is 0. Stoer-Wagner handles this naturally (a phase will find a 0-weight cut).
-   **Self-Loops:** Merging nodes creates self-loops. These must be ignored or removed.
-   **Adjacency Matrix:** Since N <= 200, an adjacency matrix `adj[N][N]` is efficient and simplifies merging.

## Naive Approach

### Intuition

Fix node 0 as source. Iterate all other nodes `i` as sink. Run Max-Flow Min-Cut (Dinic/Edmonds-Karp) for each pair `(0, i)`.

### Time Complexity

-   **O(N * MaxFlow)**: For N=200, this is roughly `200 * O(V^2 E)`. This is too slow; Stoer-Wagner is `O(N^3)` and simpler to implement for undirected graphs.

## Optimal Approach (Stoer-Wagner)

### Time Complexity

-   **O(N^3)**: Each phase takes `O(N^2)` (scanning weights), and there are `N-1` phases. With Fibonacci heap, it can be `O(N E + N^2 log N)`, but simple array scan is `O(N^3)`.

### Space Complexity

-   **O(N^2)**: Adjacency matrix.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long minCut(int n, List<int[]> edges) {
        long[][] adj = new long[n][n];
        for (int[] e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long globalMinCut = Long.MAX_VALUE;
        boolean[] merged = new boolean[n]; // Tracks if node is merged into another
        int nodesRemaining = n;

        while (nodesRemaining > 1) {
            // Minimum Cut Phase
            long[] weights = new long[n];
            boolean[] inSet = new boolean[n]; // In the growing set of the phase
            int prev = -1, curr = -1;

            // We need to add 'nodesRemaining' nodes to the set
            for (int step = 0; step < nodesRemaining; step++) {
                prev = curr;
                curr = -1;
                long maxWeight = -1;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        if (weights[i] > maxWeight) {
                            maxWeight = weights[i];
                            curr = i;
                        }
                    }
                }

                if (curr == -1) break; // Should not happen
                inSet[curr] = true;

                // Update weights of neighbors
                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            // The cut of the phase is the weight of the last added node 'curr'
            // 'weights[curr]' contains the sum of edges from 'curr' to the set (all other nodes)
            // At the end, weights[curr] is exactly the cut value of separating 'curr' from the rest.
            
            globalMinCut = Math.min(globalMinCut, weights[curr]);

            // Merge curr (t) into prev (s)
            for (int i = 0; i < n; i++) {
                if (i != curr && i != prev && !merged[i]) {
                    adj[prev][i] += adj[curr][i];
                    adj[i][prev] += adj[curr][i];
                }
            }
            merged[curr] = true;
            nodesRemaining--;
        }

        return globalMinCut == Long.MAX_VALUE ? 0 : globalMinCut;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            edges.add(new int[]{u, v, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.minCut(n, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_cut(n: int, edges: list[tuple[int, int, int]]) -> int:
    adj = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        adj[u][v] += w
        adj[v][u] += w
        
    global_min_cut = float('inf')
    merged = [False] * n
    nodes_remaining = n
    
    while nodes_remaining > 1:
        # Minimum Cut Phase
        weights = [0] * n
        in_set = [False] * n
        prev = -1
        curr = -1
        
        # Add nodes one by one
        for _ in range(nodes_remaining):
            prev = curr
            curr = -1
            max_w = -1
            
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    if weights[i] > max_w:
                        max_w = weights[i]
                        curr = i
            
            in_set[curr] = True
            
            # Update weights
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    weights[i] += adj[curr][i]
                    
        # Update global min cut
        # weights[curr] is the cut value of the phase
        global_min_cut = min(global_min_cut, weights[curr])
        
        # Merge curr (t) into prev (s)
        for i in range(n):
            if i != curr and i != prev and not merged[i]:
                adj[prev][i] += adj[curr][i]
                adj[i][prev] += adj[curr][i]
                
        merged[curr] = True
        nodes_remaining -= 1
        
    return global_min_cut if global_min_cut != float('inf') else 0

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
            w = int(next(iterator))
            edges.append((u, v, w))
        print(min_cut(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long minCut(int n, const vector<array<int, 3>>& edges) {
        vector<vector<long long>> adj(n, vector<long long>(n, 0));
        for (const auto& e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long long globalMinCut = LLONG_MAX;
        vector<bool> merged(n, false);
        int nodesRemaining = n;

        while (nodesRemaining > 1) {
            vector<long long> weights(n, 0);
            vector<bool> inSet(n, false);
            int prev = -1, curr = -1;

            for (int step = 0; step < nodesRemaining; step++) {
                prev = curr;
                curr = -1;
                long long maxW = -1;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        if (weights[i] > maxW) {
                            maxW = weights[i];
                            curr = i;
                        }
                    }
                }

                if (curr == -1) break;
                inSet[curr] = true;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            globalMinCut = min(globalMinCut, weights[curr]);

            // Merge curr into prev
            for (int i = 0; i < n; i++) {
                if (i != curr && i != prev && !merged[i]) {
                    adj[prev][i] += adj[curr][i];
                    adj[i][prev] += adj[curr][i];
                }
            }
            merged[curr] = true;
            nodesRemaining--;
        }

        return globalMinCut == LLONG_MAX ? 0 : globalMinCut;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.minCut(n, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCut(n, edges) {
    const adj = Array.from({ length: n }, () => new Array(n).fill(0));
    for (const [u, v, w] of edges) {
      adj[u][v] += w;
      adj[v][u] += w;
    }

    let globalMinCut = Infinity;
    const merged = new Int8Array(n).fill(0);
    let nodesRemaining = n;

    while (nodesRemaining > 1) {
      const weights = new Array(n).fill(0);
      const inSet = new Int8Array(n).fill(0);
      let prev = -1;
      let curr = -1;

      for (let step = 0; step < nodesRemaining; step++) {
        prev = curr;
        curr = -1;
        let maxW = -1;

        for (let i = 0; i < n; i++) {
          if (!merged[i] && !inSet[i]) {
            if (weights[i] > maxW) {
              maxW = weights[i];
              curr = i;
            }
          }
        }

        if (curr === -1) break;
        inSet[curr] = 1;

        for (let i = 0; i < n; i++) {
          if (!merged[i] && !inSet[i]) {
            weights[i] += adj[curr][i];
          }
        }
      }

      globalMinCut = Math.min(globalMinCut, weights[curr]);

      // Merge curr into prev
      for (let i = 0; i < n; i++) {
        if (i !== curr && i !== prev && !merged[i]) {
          adj[prev][i] += adj[curr][i];
          adj[i][prev] += adj[curr][i];
        }
      }
      merged[curr] = 1;
      nodesRemaining--;
    }

    return globalMinCut === Infinity ? 0 : globalMinCut;
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
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.minCut(n, edges).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4
0 1 1
1 2 2
2 3 1
0 3 2
```
**Phase 1:**
- Start at 0. Initial weights: `[0, 1, 0, 2]`.
- Pick 3 (max weight 2). Update: weight[2] becomes 1.
- Pick 1 (tie with 2). Update: weight[2] becomes 3.
- Pick 2 last. Phase cut = 3. Merge 2 into 1.

![Phase 1 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186725/dsa-problems/AGR-001/editorial/khw2mvggwyqbimgsgokd.jpg)

**Phase 2:**
- Remaining nodes: 0, 1, 3.
- Start at 0. Pick 3 (weight 2). Update: weight[1] becomes 2.
- Pick 1 last. Phase cut = 2. Merge 1 into 3.

![Phase 2 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186807/dsa-problems/AGR-001/editorial/k2cjbbna9hpaaop0yehi.jpg)

**Phase 3:**
- Remaining nodes: 0, 3.
- Phase cut = 3.

![Phase 3 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186754/dsa-problems/AGR-001/editorial/kspksfewbg6v6a8kb6aj.jpg)

**Result:** 2.
