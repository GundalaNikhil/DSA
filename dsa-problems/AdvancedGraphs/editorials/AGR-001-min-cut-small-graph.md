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

**Scenario Title:** The Hostel LAN Party Disconnection 🎮

### The Problem
It's Friday night in the hostel, and the entire block is connected via a makeshift LAN network for a massive *Counter-Strike* or *Dota* tournament. Room 101, 102, 103... are all interconnected with ethernet cables. Some connections are direct cables (weight = link stability/bandwidth), while others go through switches.

You are the "Evil Warden" (or a prankster rival wing) planning to disrupt the tournament. You want to cut the **minimum total connection bandwidth** required to split the hostel gamers into two separate, isolated groups so they can no longer play together in a single lobby.

### Why This Matters
-   **Network Reliability**: If it takes just one loose cable (low weight) to split the hostel network in half, your network topology is weak.
-   **Redundancy**: You want to identify these bottlenecks to add backup cables (redundancy) so the game doesn't lag out or disconnect when someone trips over a wire.

### Constraints in Real World
-   **Scale**: A hostel wing might have 50-100 rooms (Nodes).
-   **Reliability**: Measuring the exact "cost" to cut the connection without actually cutting it.

![Real-World Application](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185634/dsa-problems/AGR-001/editorial/w5iuzwibb3qes3llp9ad.jpg)

### From Real World to Algorithm
Rooms are **Nodes**, Cables are **Edges**, and Cable Bandwidth/Strength is the **Weight**. We need to find the "Global Minimum Cut" to identify the weakest set of links.

## Detailed Explanation

### Concept Visualization

![Concept Graph Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186392/dsa-problems/AGR-001/editorial/ll6zm88un3k4cqwktayh.jpg)

### Algorithm: Stoer-Wagner

The Global Min-Cut problem differs from the $s-t$ Min-Cut problem (Max-Flow) because we don't fix source and sink nodes. The naive approach of running $s-t$ Min-Cut for all pairs is inefficient. **Stoer-Wagner** is a recursive algorithm that solves this efficiently.

#### Algorithm Flow Diagram

```mermaid
graph TD
    Start[Start: Graph G with N nodes] --> LoopCondition{Is N > 1?}
    LoopCondition -- Yes --> PhaseStart[Start MinimumCutPhase]
    PhaseStart --> SelectNode[Select arbitrary start node 'a']
    SelectNode --> GrowSet[Repeatedly add 'most tightly connected' node]
    GrowSet --> LastTwo[Identify last two nodes added: s, t]
    LastTwo --> UpdateMin[GlobalMinCut = min(GlobalMinCut, weight(t))]
    UpdateMin --> MergeNodes[Merge t into s]
    MergeNodes --> UpdateGraph[Remove t, update weights]
    UpdateGraph --> LoopCondition
    LoopCondition -- No --> End[Return GlobalMinCut]
```

### Core Logic (Minimum Cut Phase)
1.  **Maximum Adjacency Search**: Start with an arbitrary node. Greedily add the node most strongly connected to the current set.
2.  **Cut-of-the-Phase**: The total weight of edges connecting the *last* added node ($t$) to the rest of the graph is a candidate for the global min-cut.
3.  **Merge Step**: Contract nodes $s$ (second to last) and $t$ (last) into a single node. This reduces the problem size by 1.

## 🎯 Edge Cases to Test

1.  **Disconnected Graph**
    -   Input: Graph with 2 separate components.
    -   Expected: Result `0`.
2.  **Two Nodes**
    -   Input: `2` nodes connected by an edge weight `W`.
    -   Expected: `W`.
3.  **Complete Graph**
    -   Input: $K_N$ where all edges count.
    -   Expected: Correct minimum degree sum.
4.  **Star Graph**
    -   Input: Center connected to leaves with varying weights.
    -   Expected: Minimum leaf edge weight.
5.  **Large Weights**
    -   Input: Weights up to $1000$ or more.
    -   Expected: Correct sum without overflow (use long/long long).

## ✅ Input/Output Clarifications
-   **Graph Type**: Undirected, Weighted.
-   **Zero-Weight Edges**: Possible, effectively non-existent for cut purposes.
-   **Output**: A single integer representing the minimum cut weight.

## Naive Approach

### Intuition
Fix node `0` as the source $s$. Iterate all other nodes $i$ as sink $t$. Run Max-Flow Min-Cut algorithm (like Dinic or Edmonds-Karp) for each pair $(0, i)$. The minimum of these Max-Flow values is the Global Min Cut.

### Complexity Visualization

| Approach | Time Complexity | Space Complexity | Feasibility for N=200 |
|:---------|:---------------:|:----------------:|:---------------------:|
| Naive ($N \times$ MaxFlow) | $O(N \cdot V^2 E)$ | $O(V+E)$ | ❌ Likely TLE (approx $200 \times 10^7$ ops) |
| Optimal (Stoer-Wagner) | $O(N^3)$ | $O(N^2)$ | ✅ Efficient (approx $8 \times 10^6$ ops) |

### Why This Fails
Running Max-Flow $N-1$ times is computationally expensive. For small graphs ($N \le 50$), it might pass, but for $N=200$, the cubic nature of Stoer-Wagner is significantly better than the potentially higher-order complexity of repeated Max-Flow.

## Optimal Approach (Stoer-Wagner)

### Key Insight
The algorithm avoids flow computations entirely. It relies on the property that for any two nodes $s$ and $t$, the global min-cut either separates $s$ and $t$ (computed by the "cut-of-the-phase") or keeps them together. If they stay together, we can merge them and recurse.

### Time Complexity
-   **O(N³)**: There are $N-1$ phases. Each phase performs a Maximum Adjacency Search taking $O(N^2)$ with a simple array or $O(E + N \log N)$ with a Fibonacci heap. Given $N \le 200$ and dense graphs, $O(N^3)$ is optimal.

### Space Complexity
-   **O(N²)**: To store the adjacency matrix and weight arrays.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public long minCut(int n, List<int[]> edges) {
        // Initialize adjacency matrix for O(1) edge lookups and updates
        long[][] adj = new long[n][n];
        for (int[] e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long globalMinCut = Long.MAX_VALUE;
        boolean[] merged = new boolean[n]; // Tracks nodes merged into others
        int nodesRemaining = n;

        // Run N-1 phases
        while (nodesRemaining > 1) {
            // Minimum Cut Phase (Maximum Adjacency Search)
            long[] weights = new long[n]; // Sum of weights to the "growing set"
            boolean[] inSet = new boolean[n]; // Nodes added to the current phase's set
            int prev = -1, curr = -1;

            // Add nodes one by one to the set based on max connectivity
            for (int step = 0; step < nodesRemaining; step++) {
                prev = curr;
                curr = -1;
                long maxWeight = -1;

                // Select node not in set with max weight connection to set
                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        if (weights[i] > maxWeight) {
                            maxWeight = weights[i];
                            curr = i;
                        }
                    }
                }

                if (curr == -1) break; 
                inSet[curr] = true;

                // Update weights of neighbors
                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            // The value of the cut separating 'curr' from the rest
            globalMinCut = Math.min(globalMinCut, weights[curr]);

            // Merge Step: Merge 'curr' (t) into 'prev' (s)
            for (int i = 0; i < n; i++) {
                if (i != curr && i != prev && !merged[i]) {
                    adj[prev][i] += adj[curr][i];
                    adj[i][prev] += adj[curr][i];
                }
            }
            // Mark 'curr' as effectively removed
            merged[curr] = true;
            nodesRemaining--;
        }

        return globalMinCut == Long.MAX_VALUE ? 0 : globalMinCut;
    }
}
```

### Python
```python
import sys

def min_cut(n: int, edges: list[tuple[int, int, int]]) -> int:
    # Adjacency matrix is suitable for merging nodes
    adj = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        adj[u][v] += w
        adj[v][u] += w
        
    global_min_cut = float('inf')
    merged = [False] * n # To track merged nodes
    nodes_remaining = n
    
    # Stoer-Wagner Algorithm: N-1 phases
    while nodes_remaining > 1:
        # --- Minimum Cut Phase ---
        weights = [0] * n
        in_set = [False] * n
        prev = -1
        curr = -1
        
        # Grow the set by adding 'nodes_remaining' nodes
        for _ in range(nodes_remaining):
            prev = curr
            curr = -1
            max_w = -1
            
            # Find the most tightly connected node not yet in set
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    if weights[i] > max_w:
                        max_w = weights[i]
                        curr = i
            
            in_set[curr] = True
            
            # Update connection weights for neighbors
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    weights[i] += adj[curr][i]
                    
        # The cut value for the last added node (t)
        global_min_cut = min(global_min_cut, weights[curr])
        
        # --- Merge Step ---
        # Merge curr (t) into prev (s)
        for i in range(n):
            if i != curr and i != prev and not merged[i]:
                adj[prev][i] += adj[curr][i]
                adj[i][prev] += adj[curr][i]
                
        merged[curr] = True
        nodes_remaining -= 1
        
    return global_min_cut if global_min_cut != float('inf') else 0
```

### C++
```cpp
class Solution {
public:
    long long minCut(int n, const vector<array<int, 3>>& edges) {
        // Use adjacency matrix for O(1) merging updates
        vector<vector<long long>> adj(n, vector<long long>(n, 0));
        for (const auto& e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long long globalMinCut = LLONG_MAX;
        vector<bool> merged(n, false); // Mark merged nodes
        int nodesRemaining = n;

        // Perform N-1 phases
        while (nodesRemaining > 1) {
            vector<long long> weights(n, 0); // Connection strength to current set
            vector<bool> inSet(n, false);
            int prev = -1, curr = -1;

            // Repeatedly add heaviest connected node
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

                // Update weights for next iteration
                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            // 'weights[curr]' is the min-cut of this phase
            globalMinCut = min(globalMinCut, weights[curr]);

            // Merge curr (last) into prev (second last)
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
```

### JavaScript
```javascript
class Solution {
  minCut(n, edges) {
    // Initialize adjacency matrix
    const adj = Array.from({ length: n }, () => new Array(n).fill(0));
    for (const [u, v, w] of edges) {
      adj[u][v] += w;
      adj[v][u] += w;
    }

    let globalMinCut = Infinity;
    const merged = new Int8Array(n).fill(0); // Efficient boolean tracking
    let nodesRemaining = n;

    // Run phases until only 1 super-node remains
    while (nodesRemaining > 1) {
      const weights = new Array(n).fill(0);
      const inSet = new Int8Array(n).fill(0);
      let prev = -1;
      let curr = -1;

      // Build the Maximum Adjacency ordering
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

        // Update weights
        for (let i = 0; i < n; i++) {
          if (!merged[i] && !inSet[i]) {
            weights[i] += adj[curr][i];
          }
        }
      }

      // Potentially update global minimum
      globalMinCut = Math.min(globalMinCut, weights[curr]);

      // Merge curr (t) into prev (s)
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
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
4 4
0 1 1
1 2 2
2 3 1
0 3 2
```

### Execution Table

| Phase | Active Nodes | Search Order | Last Pair ($s, t$) | Cut Value ($w(t)$) | Update MinCut | Action |
|-----:|:------------:|:------------------------:|:------------------:|:------------------:|:-------------:|:-------|
| 1 | {0,1,2,3} | $0 \to 3 \to 1 \to 2$ | $s=1, t=2$ | $3$ (Edges: 1-2, 2-3) | $\infty \to 3$ | Merge $2 \to 1$ |
| 2 | {0,1,3} (2 merged) | $0 \to 3 \to 1$ | $s=3, t=1$ | $2$ (Edges: 1-0, 1-2(merged)) | $3 \to 2$ | Merge $1 \to 3$ |
| 3 | {0,3} (1,2 merged) | $0 \to 3$ | $s=0, t=3$ | $3$ (Edges: 0-3, 0-1(merged)) | $2$ (no change) | Merge $3 \to 0$ |

**Final Result:** 2

### State Diagram (Phase 1 Detailed)

1.  **Initial**: Set $A = \{0\}$. Weights: $[0, 1, 0, 2]$.
2.  **Pick 3**: $A = \{0, 3\}$. Weights update ($3$'s neighbor is $2$, wt 1). New weights: $[0, 1, 1, 2]$.
3.  **Pick 1**: $A = \{0, 3, 1\}$. Weights update ($1$'s neighbor is $2$, wt 2). New weight for $2$: $1+2=3$.
4.  **Pick 2**: $A = \{0, 3, 1, 2\}$. $t=2$, $w(t)=3$.
5.  **Merge**: $2$ merges into $1$. New edges for $1$ include old edges of $2$.

![Phase 1 Sketch](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186725/dsa-problems/AGR-001/editorial/khw2mvggwyqbimgsgokd.jpg)

## ✅ Proof of Correctness

### Invariant
The "Maximum Adjacency Search" (finding $s$ and $t$) guarantees that the weight of the cut separating $t$ from the rest of the graph is exactly equal to the $s-t$ minimum cut in the current graph.

### Why It Works
Stoer and Wagner proved that for any phase, the cut value of the last node $t$ is effectively a valid specific $s-t$ cut. By iteratively storing this generic cut and then merging $s$ and $t$ (effectively saying "assume $s$ and $t$ are on the same side of the cut"), we explore all possibilities:
1.  Either the global min cut splits $s$ and $t$.
2.  Or it doesn't (loop continues with $s, t$ merged).

The global minimum of all "phase cuts" covers the actual global min cut.

## ⚠️ Common Mistakes to Avoid

1.   **Confusing with s-t Min Cut**
    -   ❌ Trying to run Max-Flow once from node 0 to node N-1.
    -   ✅ This is *Global* Min Cut. Max-Flow must be run for *all pairs* (or at least $N-1$ times) to work.
2.  **Incorrect Merging logic**
    -   ❌ Forgetting to add weights of edges from $t$ to $s$ when merging.
    -   ✅ Edges connected to $t$ must be essentially "transferred" to $s$.
3.  **Self-Loops Calculation**
    -   ❌ Including self-loops in weight calculations.
    -   ✅ `adj[i][i]` should generally be 0 or ignored, as cutting a self-loop doesn't separate the graph.
4.  **Integer Overflow**
    -   ❌ Using `int` for sums of weights.
    -   ✅ Use `long` (Java/C++) as total weight can exceed $2^{31}-1$.
5.  **Graph Modification**
    -   ❌ Modifying the original input edges list directly.
    -   ✅ Use an adjacency matrix or adjacency lists that support dynamic updates (merging).

## 💡 Interview Extensions

1.  **What if edges are directed?**
    -   Stoer-Wagner only works for **undirected** graphs. For directed graphs, you generally need $O(N)$ Max-Flow computations.
2.  **Can we output the actual cut partitions?**
    -   Yes, instead of just tracking the minimum value, track the set of nodes merged into the final "super-node" that gave the minimum cut.
3.  **Sparse Graph Optimization?**
    -   Using a Fibonacci Heap or balanced BST for the "Maximum Adjacency Search" phase improves the phase complexity to $O(E + N \log N)$, making the total time $O(NE + N^2 \log N)$.
4.  **Relationship to Karger's Algorithm?**
    -   Karger's is a randomized algorithm ($O(N^2 \log^3 N)$ or similar) that contracts random edges. Stoer-Wagner is deterministic.

## Related Concepts
-   **Max-Flow Min-Cut Theorem**: The basis for the $s-t$ cut approach.
-   **Prim's Algorithm**: The "Maximum Adjacency Search" is nearly identical to Prim's MST algorithm, but maximizing weights instead of minimizing.
-   **Union-Find**: Used in Karger's, concept of merging sets.
