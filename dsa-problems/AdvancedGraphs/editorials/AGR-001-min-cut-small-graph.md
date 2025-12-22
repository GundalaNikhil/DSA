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

![Real-World Application](../images/AGR-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (2)
  A -------- B
  | \        |
  |  \ (3)   | (2)
(1)|   \      |
  |     \    |
  C -------- D
      (1)
```
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
3.  Return `min_cut`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Disconnected Graph:** If the graph is initially disconnected, the min cut is 0. Stoer-Wagner handles this naturally (a phase will find a 0-weight cut).
-   **Self-Loops:** Merging nodes creates self-loops. These must be ignored or removed.
-   **Adjacency Matrix:** Since N <= 200, an adjacency matrix `adj[N][N]` is efficient and simplifies merging.

## Naive Approach

### Intuition

Fix node 0 as source. Iterate all other nodes `i` as sink. Run Max-Flow Min-Cut (Dinic/Edmonds-Karp) for each pair `(0, i)`.

### Time Complexity

-   **O(N * MaxFlow)**: For N=200, this is roughly `200 * O(V^2 E)`. Might be too slow or barely pass. Stoer-Wagner is `O(N^3)` and simpler to implement for undirected graphs.

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
            // Wait, standard Stoer-Wagner: weights[curr] is sum of edges to PREVIOUS nodes in set.
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
-   Start with 0. `weights` from 0: `[0, 1, 0, 2]`.
-   Max is 3 (weight 2). Add 3. Set: `{0, 3}`.
-   Update weights from 3: `1->2` (dist 0), `2->1` (dist 1). `weights[2]` becomes `0+1=1`.
-   Wait, let's trace carefully.
-   Nodes: 0, 1, 2, 3.
-   Start 0. `inSet={0}`. `weights=[-, 1, 0, 2]`.
-   Pick max weight: 3 (val 2). `curr=3`. `inSet={0,3}`. `prev=0`.
-   Update neighbors of 3: `3-2` (w=1). `weights[2] += 1` -> 1.
-   Pick max weight: 1 (val 1) or 2 (val 1). Let's pick 1. `curr=1`. `inSet={0,3,1}`. `prev=3`.
-   Update neighbors of 1: `1-2` (w=2). `weights[2] += 2` -> 3.
-   Pick max weight: 2 (val 3). `curr=2`. `inSet={0,3,1,2}`. `prev=1`.
-   **Last added:** `t=2`, `s=1`.
-   **Cut of phase:** `weights[2] = 3`. `globalMin = 3`.
-   **Merge 2 into 1:**
    -   `adj[1][0] += adj[2][0]` (0) -> 1.
    -   `adj[1][3] += adj[2][3]` (1) -> 0+1=1.
    -   Remove 2.

**Phase 2:**
-   Nodes: 0, 1, 3. (2 is merged).
-   Start 0. `inSet={0}`. `weights=[-, 1, -, 2]`.
-   Pick 3 (val 2). `curr=3`. `inSet={0,3}`. `prev=0`.
-   Update neighbors of 3: `3-1` (w=1). `weights[1] += 1` -> 2.
-   Pick 1 (val 2). `curr=1`. `inSet={0,3,1}`. `prev=3`.
-   **Last added:** `t=1`, `s=3`.
-   **Cut of phase:** `weights[1] = 2`. `globalMin = min(3, 2) = 2`.
-   **Merge 1 into 3:**
    -   `adj[3][0] += adj[1][0]` (1) -> 2+1=3.
    -   Remove 1.

**Phase 3:**
-   Nodes: 0, 3.
-   Start 0. `inSet={0}`. `weights=[-, -, -, 3]`.
-   Pick 3. `curr=3`. `prev=0`.
-   **Last added:** `t=3`, `s=0`.
-   **Cut of phase:** 3. `globalMin = min(2, 3) = 2`.
-   Merge 3 into 0. Done.

**Result:** 2.
Wait, the example output says 3.
Let's re-read example.
`0-1 (1)`, `1-2 (2)`, `2-3 (1)`, `0-3 (2)`.
Cycle `0-1-2-3-0`.
Cut `{0}`: Edges `(0,1)` [1] + `(0,3)` [2] = 3.
Cut `{1}`: `(1,0)` [1] + `(1,2)` [2] = 3.
Cut `{2}`: `(2,1)` [2] + `(2,3)` [1] = 3.
Cut `{3}`: `(3,2)` [1] + `(3,0)` [2] = 3.
Cut `{0,1}` vs `{2,3}`: `(1,2)` [2] + `(0,3)` [2] = 4.
Cut `{0,3}` vs `{1,2}`: `(0,1)` [1] + `(3,2)` [1] = 2.
Ah! `{0,3}` vs `{1,2}` gives 2.
Why does example say 3?
"One minimum cut is {0} vs {1,2,3}, with crossing weight 1 + 2 = 3."
Is my manual trace wrong?
`0-3` is weight 2. `1-2` is weight 2.
`0-1` is 1. `3-2` is 1.
Cut `{0,3}` separates them from `{1,2}`.
Edges crossing: `(0,1)` [1] and `(3,2)` [1]. Total 2.
Is the example output wrong? Or did I misread the graph?
`0 1 1`
`1 2 2`
`2 3 1`
`0 3 2`
Yes, `0-1` (1), `1-2` (2), `2-3` (1), `3-0` (2).
If I cut `(0,1)` and `(2,3)`, cost is 1+1=2.
The graph falls into `{0,3}` and `{1,2}`.
Wait, `0` connected to `3` (cost 2). `1` connected to `2` (cost 2).
If I cut `(0,1)` and `(2,3)`, then `0` is connected to `3`, `1` is connected to `2`.
Is `{0,3}` connected to `{1,2}`?
Edges between `{0,3}` and `{1,2}` are `(0,1)` and `(3,2)`.
Yes, cost is 2.
So the Min Cut should be 2.
The example output says 3.
**CRITICAL:** The example output in the problem file might be wrong, or I am missing something.
Let me check the example explanation again.
"One minimum cut is {0} vs {1,2,3}, with crossing weight 1 + 2 = 3."
It says "One minimum cut". It implies 3 is the minimum.
But 2 is smaller.
Is there a constraint I missed? "Undirected weighted graph".
Maybe the graph is different?
`0 1 1`
`1 2 2`
`2 3 1`
`0 3 2`
Maybe I should check if `2` is a valid cut.
If I remove `(0,1)` and `(2,3)`, is the graph disconnected?
Yes. `{0,3}` and `{1,2}` are the components.
So 2 is definitely a cut.
If the example says 3, then the example is wrong.
**Action:** I must fix the problem file example first.
Wait, let me double check.
Maybe the edge `0 3 2` is `0 3 1`? No, it says 2.
Maybe `1 2 2` is `1 2 1`? No.
If the example output is 3, then maybe the edges are different.
If I change `0 3 2` to `0 3 1`, then cut `{0}` is `1+1=2`. Cut `{0,3}` is `1+1=2`.
If I change `0 1 1` to `0 1 2`, then cut `{0,3}` is `2+1=3`. Cut `{0}` is `2+2=4`.
Actually, if I strictly follow the "Review questions first" instruction, I should fix this.
The example output 3 is incorrect for the given input. The correct min cut is 2.
I will update the problem file to have a consistent example.
I'll change the edge `2 3 1` to `2 3 2`.
Then cut `{0,3}` vs `{1,2}` cost is `1 + 2 = 3`.
Cut `{0}` cost `1+2=3`.
Cut `{3}` cost `2+2=4`.
Cut `{1}` cost `1+2=3`.
Cut `{2}` cost `2+2=4`.
So min cut would be 3.
This seems like a good fix. Change `2 3 1` to `2 3 2`.
Or I can just change the output to 2 and explanation to match.
"One minimum cut is {0,3} vs {1,2}, with crossing weight 1 + 1 = 2."
This is better. Keep input simple.

**Plan Update:**
1.  **Fix AGR-001 Problem File**: Update example output to 2 and explanation.
2.  **Generate Editorial**: Proceed with the corrected example.

I will perform the fix now.
