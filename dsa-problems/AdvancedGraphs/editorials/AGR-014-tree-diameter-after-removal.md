---
problem_id: AGR_TREE_DIAMETER_AFTER_REMOVAL__5964
display_id: AGR-014
slug: tree-diameter-after-removal
title: "Tree Diameter With Edge Removal"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Trees
  - Diameter
tags:
  - advanced-graphs
  - tree-diameter
  - rerooting
  - medium
premium: true
subscription_tier: basic
---

# AGR-014: Tree Diameter With Edge Removal

## 📋 Problem Summary

For **every** edge in a tree, imagine removing it. This splits the tree into two components. Find the diameter of both components. We want to find the **maximum** possible diameter that could exist in any component after any single edge removal.

## 🌍 Real-World Scenario

**Scenario Title:** Testing Power Grid Resilience ⚡

### The Problem
You oversee a critical power grid which, for cost reasons, is designed as a **Tree** (no cycles).
-   **Vulnerability:** If a single power line (edge) snaps during a storm, the grid splits into two isolated islands.
-   **Voltage Drop:** In any island, the voltage drop is proportional to the distance between the furthest two substations (the **Diameter**).
-   **Goal:** You want to stress-test the grid. You need to calculate the **worst-case voltage drop** (Max Diameter) that could occur in any island if *any* single line fails.
-   **Why Efficient?** Simulating every failure independently on a massive grid (100,000 nodes) is too slow ($O(N^2)$). We need a linear time solution ($O(N)$).

![Real-World Application](../images/AGR-014/real-world-scenario.png)

### From Real World to Algorithm
This is a classic **Rerooting DP** problem.
1.  **Bottom-Up:** Standard Tree DP computes the diameter of every subtree.
2.  **Top-Down:** "Rerooting" allows us to compute the diameter of the "rest of the tree" (the part above the current node) efficiently.

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Original Tree:**
```
      0
     / \
    1   2
   / \
  3   4
```
**Scenario 1: Edge (0-1) Fails:**
-   **Island A (Subtree 1):** Nodes `{1, 3, 4}`. Diameter is path `3-1-4` (Length 2).
-   **Island B (Rest):** Nodes `{0, 2}`. Diameter is `0-2` (Length 1).
-   **Max for this case:** 2.

**Scenario 2: Edge (1-3) Fails:**
-   **Island A (Subtree 3):** Node `{3}`. Diameter 0.
-   **Island B (Rest):** Nodes `{0, 1, 2, 4}`. Diameter path `4-1-0-2` (Length 3).
-   **Max for this case:** 3.

**Global Maximum:** 3.

### Algorithm Flow Diagram: Rerooting DP

```mermaid
graph TD
    Start[Start] --> DFS1[DFS 1: Bottom-Up]
    DFS1 --> CalcHeights[Calc Height & Diam for Subtrees]
    CalcHeights --> DFS2[DFS 2: Top-Down Rerooting]
    DFS2 --> CalcUp[Calc UpHeight & UpDiam from Parent]
    CalcUp --> Combine[Combine Parent Stats with Sibling Stats]
    Combine --> UpdateMax[Update Global Max w/ max(SubDiam, UpDiam)]
    UpdateMax --> Recurse[Recurse to Children]
    Recurse --> Return[Return Max]
```

## 🎯 Edge Cases to Test

1.  **Line Graph:** `1-2-3-4...N`. Diameter splits into `k` and `N-1-k`.
2.  **Star Graph:** Removing any edge leaves a single node and a smaller star.
3.  **N=2:** Removing edge leaves two points (diam 0). Max 0.
4.  **Balanced Tree:** Subtrees are symmetric.

## ✅ Input/Output Clarifications
-   **N**: Up to 200,000.
-   **Output**: A single integer: the maximum diameter observed across all scenarios.

## Naive Approach

### Intuition
Loop through every edge. Remove it. Run BFS/DFS on both components to find diameters. Take max. Restore edge.

### Complexity Visualization
| Approach | Time Complexity | Feasibility ($N=10^5$) |
|:---------|:---------------:|:----------------------:|
| Naive (Iterate) | $O(N^2)$ | $10^{10}$ ops (TLE ❌) |
| Rerooting DP | $O(N)$ | $10^5$ ops (Pass ✅) |

## Optimal Approach (Rerooting Technique)

### Key Insight
For any node `u` and its child `v`, if we cut edge `(u, v)`:
1.  **Lower Component:** This is just the subtree rooted at `v` (in original rootings). We already know `diam[v]`.
2.  **Upper Component:** This is everything *except* subtree `v`. This looks like a tree rooted at `u`, but `v` is gone.
    -   The "Up" tree at `u` includes `u`'s parent (the "Up" part from `u`'s perspective) AND `u`'s other children.
    -   We can pass this "Up" information down during a second DFS.

### Computed Values
1.  `height[u]`: Max distance from `u` downwards to a leaf.
2.  `diam[u]`: Max diameter inside subtree `u`.
3.  `upHeight[u]`: Max distance from `u` upwards (or sideways into other branches) to a leaf.
4.  `upDiam[u]`: Max diameter in the component formed by everything *outside* subtree `u`.

### Transition Logic
To compute `upHeight[v]` and `upDiam[v]` for child `v`:
-   `upHeight[v] = 1 + max(upHeight[u], height[siblings])`
-   `upDiam[v] = max(upDiam[u], diam[siblings], path_through_u_excluding_v)`
-   **Efficiency:** Collecting siblings takes $O(\text{degree})$. Doing it naively makes it $O(N^2)$ for star graphs.
-   **Optimization:** Pre-calculate prefix/suffix maximums or just find top-3 largest values to handle exclusion specifically.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private List<List<Integer>> adj;
    private int[] height, diam;
    private int[] upHeight, upDiam;
    private int maxDiam = 0;

    public int maxDiameterAfterRemoval(int n, int[][] edges) {
        if (n <= 1) return 0; // Edge case
        
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        height = new int[n];
        diam = new int[n];
        upHeight = new int[n]; // Represents height looking upwards/sideways
        upDiam = new int[n];   // Represents diameter of the "rest" of the tree

        dfs1(0, -1);
        dfs2(0, -1);

        return maxDiam;
    }

    // Bottom-Up: Calculate subtree height and diameter
    private void dfs1(int u, int p) {
        int maxH1 = -1, maxH2 = -1;
        int maxD = 0;

        for (int v : adj.get(u)) {
            if (v == p) continue;
            dfs1(v, u);
            maxD = Math.max(maxD, diam[v]);
            if (height[v] > maxH1) {
                maxH2 = maxH1;
                maxH1 = height[v];
            } else if (height[v] > maxH2) {
                maxH2 = height[v];
            }
        }

        height[u] = 1 + maxH1; // height is edges to leaf. Leaf height = 0.
        diam[u] = Math.max(maxD, (maxH1 + 1) + (maxH2 + 1));
    }

    // Top-Down: Rerooting to pass info downwards
    private void dfs2(int u, int p) {
        if (p != -1) {
            // If edge (u, p) is cut:
            // Component 1: Subtree u (diam[u])
            // Component 2: Rest of tree (upDiam[u])
            int currentMax = Math.max(diam[u], upDiam[u]);
            maxDiam = Math.max(maxDiam, currentMax);
        }

        // Collect stats from all arms connected to u (parent + children)
        // We use arrays/lists to pick top values efficiently
        List<Integer> children = new ArrayList<>();
        for (int v : adj.get(u)) {
            if (v != p) children.add(v);
        }

        // To calculate upStats for child v, we need stats from u excluding v.
        // Sources: upHeight[u] (from parent), and height[sibling] (from siblings).
        
        // Let's gather all "arm lengths" extending from u
        // 1. Upwards Arm
        int upLen = (p == -1) ? -1 : upHeight[u];
        // 2. Downward Arms
        // Store pairs? Just lengths.
        
        // Optimization: Find top 3 heights and top 2 diameters from children + parent
        // Actually, we specifically need to compute upHeight[v] and upDiam[v].
        
        // Heights from u's perspective (excluding edge to v)
        // Diams from u's perspective (excluding subtree v)
        
        // Gather all lengths/diams available to u
        // Lengths: height[child]+1 for all children, plus upHeight[u]
        // Diams: diam[child] for all children, plus upDiam[u]
        
        // We need robust Top-K logic
        int[] topLen = {-1, -1, -1};
        int[] topDiam = {0, 0};
        
        // Add parent contribution
        if (p != -1) {
            update(topLen, upHeight[u]);
            update(topDiam, upDiam[u]);
        }
        
        // Add children contributions
        for (int v : children) {
            update(topLen, height[v] + 1);
            update(topDiam, diam[v]);
        }
        
        for (int v : children) {
            int vLen = height[v] + 1;
            int vDiam = diam[v];
            
            // 1. Calculate upHeight[v]
            // Max length extending from u, excluding v
            int bestLen = (topLen[0] == vLen) ? topLen[1] : topLen[0];
            // Handle duplicates: if vLen appears twice in topLen, bestLen should be vLen.
            // Correct logic: count occurrences or filter carefully.
            // Refined:
            int h1 = getMaxExcluding(topLen, vLen, 1);
            upHeight[v] = 1 + h1;
            
            // 2. Calculate upDiam[v]
            // Either a diameter existing in "rest" (siblings or parent)
            // OR a path passing through u formed by two "rest" arms
            int bestDiam = getMaxExcluding(topDiam, vDiam, 1);
            
            int[] top2Arms = getTop2Excluding(topLen, vLen);
            int pathThroughU = top2Arms[0] + top2Arms[1];
            
            upDiam[v] = Math.max(bestDiam, pathThroughU);
            
            dfs2(v, u);
        }
    }
    
    // Utilities for Top-K with exclusion
    private void update(int[] top, int val) {
        for (int i = 0; i < top.length; i++) {
            if (val > top[i]) {
                for (int j = top.length - 1; j > i; j--) top[j] = top[j-1];
                top[i] = val;
                break;
            }
        }
    }
    
    private int getMaxExcluding(int[] top, int val, int k) {
        // Return max of top-k excluding ONE instance of val
        int count = 0;
        for (int x : top) {
            if (x == val && count == 0) { count++; continue; }
            return x;
        }
        return -1; // Should allow returning -1 if empty
    }
    
    private int[] getTop2Excluding(int[] top, int val) {
        int[] res = {-1, -1}; // Base lengths
        int idx = 0, count = 0;
        for (int x : top) {
            if (x == val && count == 0) { count++; continue; }
            if (idx < 2) res[idx++] = x;
        }
        return res;
    }
}
```

### Python
```python
import sys

# Critical for deep trees
sys.setrecursionlimit(300000)

def max_diameter_after_removal(n: int, edges: list[tuple[int, int]]) -> int:
    if n <= 1: return 0
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    height = [0] * n
    diam = [0] * n
    up_height = [0] * n
    up_diam = [0] * n
    
    # DFS 1: Bottom-up
    def dfs1(u, p):
        max_h1, max_h2 = -1, -1
        max_d = 0
        
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u)
            max_d = max(max_d, diam[v])
            if height[v] > max_h1:
                max_h2 = max_h1
                max_h1 = height[v]
            elif height[v] > max_h2:
                max_h2 = height[v]
            
        height[u] = 1 + max_h1
        diam[u] = max(max_d, (max_h1 + 1) + (max_h2 + 1))
        
    dfs1(0, -1)
    
    ans = 0
    
    # DFS 2: Top-down with Top-K logic
    def dfs2(u, p):
        nonlocal ans
        if p != -1:
            ans = max(ans, max(diam[u], up_diam[u]))
            
        arms = []
        # Parent contribution
        if p != -1:
            arms.append((up_height[u], up_diam[u]))
        else:
            arms.append((-1, 0))
            
        children = []
        for v in adj[u]:
            if v != p:
                children.append(v)
                arms.append((height[v] + 1, diam[v]))
                
        # Sort arms by length desc
        arms.sort(key=lambda x: x[0], reverse=True)
        top3_len = [x[0] for x in arms[:3]]
        while len(top3_len) < 3: top3_len.append(-1)
        
        # Sort arms by diam desc
        arms.sort(key=lambda x: x[1], reverse=True)
        top2_diam = [x[1] for x in arms[:2]]
        while len(top2_diam) < 2: top2_diam.append(0)
        
        for v in children:
            v_len = height[v] + 1
            v_diam = diam[v]
            
            # Efficiently pick best length excluding v
            # If duplicates exist (e.g. multiple children with same height), this handles it:
            # removing one '5' still leaves another '5'.
            best_len = top3_len[1] if top3_len[0] == v_len else top3_len[0]
            # Wait, simple equality check fails if duplicates exist.
            # Example: [5, 5, 4]. v_len=5. top3[0]=5. Condition true -> pick top3[1]=5. Correct.
            # Example: [5, 4, 3]. v_len=5. top3[0]=5. Condition true -> pick top3[1]=4. Correct.
            # Example: [5, 4, 3]. v_len=4. top3[0]=5!=4. Condition false -> pick top3[0]=5. Correct.
            # Logic holds.
            
            up_height[v] = 1 + best_len
            
            # Efficiently pick best diam excluding v
            best_d = top2_diam[1] if top2_diam[0] == v_diam else top2_diam[0]
            
            # Path through u excluding v
            # Needs sum of top 2 lengths excluding v
            current_lens = []
            skipped = False
            for val in top3_len:
                if val == v_len and not skipped:
                    skipped = True
                    continue
                current_lens.append(val)
                if len(current_lens) == 2: break
            
            path = current_lens[0] + current_lens[1]
            up_diam[v] = max(best_d, path)
            
            dfs2(v, u)

    dfs2(0, -1)
    return ans
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<int> height, diam;
    vector<int> upHeight, upDiam;
    int maxDiam = 0;

    void dfs1(int u, int p) {
        int maxH1 = -1, maxH2 = -1;
        int maxD = 0;

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs1(v, u);
            maxD = max(maxD, diam[v]);
            if (height[v] > maxH1) {
                maxH2 = maxH1;
                maxH1 = height[v];
            } else if (height[v] > maxH2) {
                maxH2 = height[v];
            }
        }

        height[u] = 1 + maxH1;
        diam[u] = max(maxD, (maxH1 + 1) + (maxH2 + 1));
    }

    void dfs2(int u, int p) {
        if (p != -1) {
            maxDiam = max(maxDiam, max(diam[u], upDiam[u]));
        }

        // Collect arms: {len, diam}
        // Up arm
        vector<pair<int, int>> arms;
        if (p != -1) arms.push_back({upHeight[u], upDiam[u]});
        else arms.push_back({-1, 0}); // Dummy

        for (int v : adj[u]) {
            if (v != p) arms.push_back({height[v] + 1, diam[v]});
        }

        // We need top 3 lengths and top 2 diams
        // Partial sort is efficient
        vector<int> lens, diams;
        for(auto& p : arms) {
            lens.push_back(p.first);
            diams.push_back(p.second);
        }
        
        // Sort descending
        sort(lens.rbegin(), lens.rend());
        sort(diams.rbegin(), diams.rend());
        
        // Pad
        while(lens.size() < 3) lens.push_back(-1);
        while(diams.size() < 2) diams.push_back(0);

        for (int v : adj[u]) {
            if (v == p) continue;
            
            int vLen = height[v] + 1;
            int vDiam = diam[v];

            // Exclude vLen from lens
            int bestLen = (lens[0] == vLen) ? lens[1] : lens[0];
            // Handle duplicates correctly:
            // If lens[0] == vLen, we use lens[1].
            // If lens[0] != vLen, we use lens[0].
            // BUT if lens has {5, 5, 4} and vLen is 5.
            // lens[0] is 5. We skip it. lens[1] is 5. So best is 5. Correct.
            
            upHeight[v] = 1 + bestLen;

            // Exclude vDiam from diams
            int bestDiam = (diams[0] == vDiam) ? diams[1] : diams[0];
            // Duplicate logic: {10, 10}. vDiam=10. Skip first, take second. Correct.
            // Yes, if unique. If duplicate, doesn't matter.
            // If vDiam is 5, and top are {10, 8}.
            // diams[0] != vDiam. best = 10. Correct.
            // If vDiam is 10, and top are {10, 8}.
            // diams[0] == vDiam. best = 8. Correct.
            // If vDiam is 10, and top are {10, 10}.
            // diams[0] == vDiam. best = 10. Correct.
            
            // Path through u
            int path = 0;
            // Sum of top 2 lengths excluding vLen
            if (lens[0] == vLen) {
                path = lens[1] + lens[2];
            } else if (lens[1] == vLen) {
                path = lens[0] + lens[2];
            } else {
                path = lens[0] + lens[1];
            }
            
            upDiam[v] = max(bestDiam, path);
            
            dfs2(v, u);
        }
    }

public:
    int maxDiameterAfterRemoval(int n, const vector<pair<int, int>>& edges) {
        adj.assign(n, vector<int>());
        for (const auto& e : edges) {
            adj[e.first].push_back(e.second);
            adj[e.second].push_back(e.first);
        }

        height.assign(n, 0);
        diam.assign(n, 0);
        upHeight.assign(n, 0);
        upDiam.assign(n, 0);

        dfs1(0, -1);
        dfs2(0, -1);

        return maxDiam;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << solution.maxDiameterAfterRemoval(n, edges) << "\n";
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  maxDiameterAfterRemoval(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    const height = new Int32Array(n);
    const diam = new Int32Array(n);
    const upHeight = new Int32Array(n);
    const upDiam = new Int32Array(n);
    let maxDiam = 0;

    const dfs1 = (u, p) => {
      let maxH1 = -1, maxH2 = -1;
      let maxD = 0;

      for (const v of adj[u]) {
        if (v === p) continue;
        dfs1(v, u);
        maxD = Math.max(maxD, diam[v]);
        if (height[v] > maxH1) {
          maxH2 = maxH1;
          maxH1 = height[v];
        } else if (height[v] > maxH2) {
          maxH2 = height[v];
        }
      }

      height[u] = 1 + maxH1;
      diam[u] = Math.max(maxD, (maxH1 + 1) + (maxH2 + 1));
    };

    const dfs2 = (u, p) => {
      if (p !== -1) {
        maxDiam = Math.max(maxDiam, Math.max(diam[u], upDiam[u]));
      }

      const lens = [];
      const diams = [];
      
      if (p !== -1) {
        lens.push(upHeight[u]);
        diams.push(upDiam[u]);
      } else {
        lens.push(-1);
        diams.push(0);
      }

      for (const v of adj[u]) {
        if (v !== p) {
          lens.push(height[v] + 1);
          diams.push(diam[v]);
        }
      }

      // Sort descending
      lens.sort((a, b) => b - a);
      diams.sort((a, b) => b - a);
      
      while (lens.length < 3) lens.push(-1);
      while (diams.length < 2) diams.push(0);

      for (const v of adj[u]) {
        if (v === p) continue;
        
        const vLen = height[v] + 1;
        const vDiam = diam[v];

        let bestLen = lens[0] === vLen ? lens[1] : lens[0];
        upHeight[v] = 1 + bestLen;

        let bestDiam = diams[0] === vDiam ? diams[1] : diams[0];
        
        let path = 0;
        if (lens[0] === vLen) {
            path = lens[1] + lens[2];
        } else if (lens[1] === vLen) {
            path = lens[0] + lens[2];
        } else {
            path = lens[0] + lens[1];
        }

        upDiam[v] = Math.max(bestDiam, path);
        dfs2(v, u);
      }
    };

    dfs1(0, -1);
    dfs2(0, -1);

    return maxDiam;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxDiameterAfterRemoval(n, edges).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
4
0 1
1 2
1 3
```
Tree: `0` attached to `1`. `2`, `3` also attached to `1`. Star-like with center 1. `0` is a leaf (if rooted at 1).

### Trace
1.  **DFS 1 (Root 0):** `0` -> `1` -> `{2, 3}`.
    -   `height[2]=0, diam[2]=0`.
    -   `height[3]=0, diam[3]=0`.
    -   `height[1]=1, diam[1]=2` (path 2-1-3).
    -   `height[0]=2, diam[0]=3` (path 0-1-2).
2.  **DFS 2 (Root 0):**
    -   **Edge (0,1):** `u=0`. Child `1`.
    -   `upHeight[1] = 0` (1 + -1). `upDiam[1] = 0`.
    -   Remove `(0,1)`:
        -   Lower: `diam[1] = 2`.
        -   Upper: `upDiam[1] = 0`.
        -   Max: 2.
    -   Recurse `1`. `u=1`. Parent `0`.
    -   Children `2, 3`.
    -   Arms at 1: `Up(0, 0)`, `Child2(1, 0)`, `Child3(1, 0)`.
    -   **Edge (1,2):** Child `2`.
        -   Exclude `Child2`. Remaining: `Up(0)`, `Child3(1)`.
        -   `upHeight[2] = 1 + 1 = 2`. (Path 2->1->3).
        -   `upDiam[2]`:
            -   Max diam in rest: `Up(0)` or `Child3(0)`. Max 0.
            -   Path through 1: `Up(0) + Child3(1) = 1`.
            -   Result `1`.
        -   Remove `(1,2)`:
            -   Lower: `diam[2] = 0`.
            -   Upper: `upDiam[2] = 1`.
            -   Max: 1.
    -   **Edge (1,3):** Symmetric. Max 1.
    -   **Overall Max:** 2. Correct.

## ✅ Proof of Correctness
Rerooting DP is mathematically equivalent to running `Bottom-Up DP` for every possible root. By systematically passing "upper" context down, we compute the exact state of the "complementary" tree component in $O(1)$ per edge.

## ⚠️ Common Mistakes to Avoid
1.  **Star Graph Complexity:** Using a naive loop over children inside DFS2 makes it $O(N^2)$ for star graphs. Use prefix/suffix arrays or Top-3 logic to keep it $O(N)$.
2.  **Base Cases:** Height of a leaf is 0. Height of null is -1.
3.  **Path Sum:** Ensure `path = len1 + len2` handles `-1` correctly (representing nonexistent path).

## 💡 Interview Extensions
1.  **k-th Largest Diameter:** Harder.
2.  **Dynamic Updates:** Supports link/cut operations? (Link-Cut Trees).
