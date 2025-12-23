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

For every edge in a tree, if we remove it, the tree splits into two components. Calculate the diameter of each component, take the maximum of these two, and find the maximum such value over all possible edge removals.

## 🌍 Real-World Scenario

**Scenario Title:** Power Grid Resilience

Consider a power grid structured as a tree.
-   **Edge Removal:** Represents a power line failure.
-   **Components:** The grid splits into two isolated islands.
-   **Diameter:** Represents the "span" or worst-case transmission distance within an island.
-   **Goal:** We want to know the *worst-case* scenario (maximum diameter) among all possible single-line failures to ensure voltage stability protocols can handle the longest possible transmission path in any island configuration.

![Real-World Application](../images/AGR-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      0
     / \
    1   2
   / \
  3   4
```
**Remove Edge (0, 1):**
-   Component 1 (Subtree 1): `{1, 3, 4}`. Diameter: `3-1-4` (length 2).
-   Component 2 (Rest): `{0, 2}`. Diameter: `0-2` (length 1).
-   Max: 2.

**Remove Edge (1, 3):**
-   Component 1 (Subtree 3): `{3}`. Diameter: 0.
-   Component 2 (Rest): `{0, 1, 2, 4}`. Diameter: `4-1-0-2` (length 3).
-   Max: 3.

**Result:** Max over all edges is 3.

### Algorithm: Rerooting DP

1.  **Standard DP (Bottom-Up):**
    -   Root at 0.
    -   For each node `u`, compute `height[u]` (max distance to leaf) and `diam[u]` (diameter of subtree).
    -   `height[u] = 1 + max(height[v])`.
    -   `diam[u] = max(max(diam[v]), height[v1] + height[v2] + 2)`.
    -   This gives the diameter of the "lower" component when edge `(u, parent)` is removed.
2.  **Rerooting (Top-Down):**
    -   Compute `up_diam[u]` (diameter of the tree *excluding* subtree `u`) and `up_height[u]` (longest path starting at `parent` going upwards or into other branches).
    -   To compute for child `v` of `u`:
        -   `up_height[v] = 1 + max(up_height[u], height[other_child] + 1)`.
        -   `up_diam[v] = max(up_diam[u], diam[other_child], up_height[u] + height[other_child] + 1, height[other1] + height[other2] + 2)`.
    -   Use prefix/suffix arrays of children's heights/diameters to efficiently query "other children".

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **N:** Up to 200,000. `O(N)` required.
-   **Edges:** Unweighted (length 1).
-   **Output:** Max of (diam(comp1), diam(comp2)) over all edges.

## Naive Approach

### Intuition

Iterate all edges, remove, run BFS twice to find diameter.

### Time Complexity

-   **O(N^2)**: Too slow.

## Optimal Approach (Rerooting)

### Time Complexity

-   **O(N)**: Two DFS passes.

### Space Complexity

-   **O(N)**: DP arrays.

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
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        height = new int[n];
        diam = new int[n];
        upHeight = new int[n];
        upDiam = new int[n];

        dfs1(0, -1);
        dfs2(0, -1);

        return maxDiam;
    }

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

        height[u] = 1 + maxH1; // -1 if leaf -> 0
        diam[u] = Math.max(maxD, (maxH1 + 1) + (maxH2 + 1));
    }

    private void dfs2(int u, int p) {
        if (p != -1) {
            // Calculate answer for edge (u, p)
            // Component 1: Subtree u -> diam[u]
            // Component 2: Rest -> upDiam[u]
            maxDiam = Math.max(maxDiam, Math.max(diam[u], upDiam[u]));
        }

        int k = adj.get(u).size();
        // Collect children data
        List<Integer> children = new ArrayList<>();
        for (int v : adj.get(u)) {
            if (v != p) children.add(v);
        }

        int m = children.size();
        int[] prefH = new int[m + 1];
        int[] suffH = new int[m + 1];
        int[] prefD = new int[m + 1];
        int[] suffD = new int[m + 1];

        Arrays.fill(prefH, -1); Arrays.fill(suffH, -1);
        
        for (int i = 0; i < m; i++) {
            int v = children.get(i);
            prefH[i + 1] = Math.max(prefH[i], height[v]);
            prefD[i + 1] = Math.max(prefD[i], diam[v]);
        }
        for (int i = m - 1; i >= 0; i--) {
            int v = children.get(i);
            suffH[i] = Math.max(suffH[i + 1], height[v]);
            suffD[i] = Math.max(suffD[i + 1], diam[v]);
        }

        // To compute diam passing through u from children
        // We need top 2 heights from prefix and suffix
        // This is tricky with just max.
        // Better: Precompute top 2 heights for u excluding v?
        // Or just use the prefix/suffix max height logic.
        // 1. upDiam[u]
        // 2. diam[other_child]
        // 3. upHeight[u] + 1 + height[other_child] + 1
        // 4. height[other_a] + 1 + height[other_b] + 1 (path through u)
        
        // Refine.
        // For child v at index i:
        // Max height among others: max(prefH[i], suffH[i+1])
        // Max diam among others: max(prefD[i], suffD[i+1])
        // Path through u using up: upHeight[u] + 1 + (max height among others) + 1
        // Path through u using two others: We need top 2 heights among others.
        // Prefix/Suffix only gives max.
        
        // Alternative: Just find top 3 heights and top 2 diams of all children + up.
        // Since degree can be large, we can't iterate all pairs.
        // But we only need to exclude 'v'.
        // So finding top 3 is enough.
        
        // Gather all "arms" from u:
        // 1. Upwards: len = upHeight[u] + 1, diam = upDiam[u]
        // 2. Children: len = height[child] + 1, diam = diam[child]
        
        // We want to form upDiam[v] using these, excluding v's arm.
        // New upDiam[v] = max(
        //    max(diam of other arms),
        //    sum of top 2 lengths of other arms
        // )
        // New upHeight[v] = 1 + max(length of other arms)
        
        // Collect all arms
        // Arm: {len, diam}
        // Child arm: {height[child], diam[child]} (height is length starting u going down)

        // height[u] represents max distance to leaf. The arm length is height[child] + 1.
        // upHeight[u] represents max distance from u upwards.
        
        List<int[]> arms = new ArrayList<>();
        if (p != -1) arms.add(new int[]{upHeight[u], upDiam[u]}); // Up arm
        
        for (int v : children) {
            arms.add(new int[]{height[v] + 1, diam[v]});
        }
        
        // Find top 3 lengths and top 2 diams
        // We need to pass this info to each child efficiently.
        // Prefix/Suffix is best.
        
        // Simplify.
        // upDiam[v] depends on:
        // 1. upDiam[u]
        // 2. diam[siblings]
        // 3. Longest path through u formed by (up + sibling) or (sibling + sibling).
        
        // Use the prefix/suffix approach for "path through u using siblings".
        // Max path through u using siblings = max(prefH[i] + suffH[i+1] + 2) ?? No.
        // We need max(height[a] + height[b] + 2) where a, b != v.
        
        // Compute top 3 heights and top 2 diams for every node in O(deg).
        // Then for each child, pick the best ones that are not it.
        
        int[] topHeights = {-1, -1, -1}; // values
        int[] topDiams = {-1, -1};
        
        // Include Up
        update(topHeights, upHeight[u]);
        update(topDiams, upDiam[u]);
        
        for (int v : children) {
            update(topHeights, height[v] + 1);
            update(topDiams, diam[v]);
        }
        
        for (int v : children) {
            // upHeight[v] = 1 + max(others height)
            int h1 = getMaxExcluding(topHeights, height[v] + 1);
            upHeight[v] = 1 + h1;
            
            // upDiam[v]
            int d1 = getMaxExcluding(topDiams, diam[v]); // Max diam of others
            
            // Path through u
            // Top 2 heights excluding v
            int[] h2 = getTop2Excluding(topHeights, height[v] + 1);
            int pathThroughU = h2[0] + h2[1]; // lengths are already from u
            
            upDiam[v] = Math.max(d1, pathThroughU);
            
            dfs2(v, u);
        }
    }
    
    private void update(int[] top, int val) {
        for (int i = 0; i < top.length; i++) {
            if (val > top[i]) {
                for (int j = top.length - 1; j > i; j--) {
                    top[j] = top[j-1];
                }
                top[i] = val;
                break;
            }
        }
    }
    
    private int getMaxExcluding(int[] top, int val) {
        if (top[0] == val) return top[1];
        return top[0];
    }
    
    private int[] getTop2Excluding(int[] top, int val) {
        int[] res = new int[2];
        int idx = 0;
        int count = 0;
        for (int x : top) {
            if (x == val && count == 0) { // Skip first occurrence
                count++;
                continue;
            }
            if (idx < 2) res[idx++] = x;
        }
        return res;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxDiameterAfterRemoval(n, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def max_diameter_after_removal(n: int, edges: list[tuple[int, int]]) -> int:
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
    
    # DFS 2: Top-down
    def dfs2(u, p):
        nonlocal ans
        if p != -1:
            ans = max(ans, max(diam[u], up_diam[u]))
            
        # Collect arms: (length_from_u, diam_of_component)
        # Up arm
        arms = []
        if p != -1:
            arms.append((up_height[u], up_diam[u]))
        else:
            arms.append((-1, 0)) # Dummy for root
            
        children = []
        for v in adj[u]:
            if v != p:
                children.append(v)
                arms.append((height[v] + 1, diam[v]))
                
        # We need top 3 lengths and top 2 diams
        # Sort is O(deg log deg). Total O(N log N). Acceptable.
        # Or O(deg) with selection.
        
        # Sort arms by length descending
        arms.sort(key=lambda x: x[0], reverse=True)
        top3_len = [x[0] for x in arms[:3]]
        while len(top3_len) < 3: top3_len.append(-1)
        
        # Sort arms by diam descending
        arms.sort(key=lambda x: x[1], reverse=True)
        top2_diam = [x[1] for x in arms[:2]]
        while len(top2_diam) < 2: top2_diam.append(0)
        
        # Map for quick lookup? No, duplicate lengths possible.
        # Just filter.
        
        for v in children:
            v_len = height[v] + 1
            v_diam = diam[v]
            
            # up_height[v] = 1 + max(other lengths)
            best_len = top3_len[0] if top3_len[0] != v_len else top3_len[1]
            # Handle duplicates: if v_len appears multiple times, we can pick it.
            # If top3_len has [5, 5, 4] and v_len is 5, remaining is 5.
            
            # Robust way:
            current_lens = []
            count = 0
            for l in top3_len:
                if l == v_len and count == 0:
                    count += 1
                    continue
                current_lens.append(l)
            
            up_height[v] = 1 + current_lens[0]
            
            # up_diam[v]
            # 1. Max diam of others
            best_diam = top2_diam[0]
            if best_diam == v_diam:
                # Check if unique
                # Count occurrences in top2
                c = 0
                for d in top2_diam:
                    if d == v_diam: c += 1
                
                # We need to check if v is the ONLY source of this diam.
                # This is tricky if multiple children have same diam.
                # Use a rescan to handle duplicates safely.
                pass
                
            # Re-scanning top 2 diams excluding v
            # Since we sorted arms by diam, we can just pick.
            # We need original arms list or similar.
            
            # Avoid per-child O(deg^2); use top-k logic efficiently.
            # We have sorted lists.
            
            # Max diam excluding v
            d_excl = -1
            c = 0
            for val in top2_diam:
                if val == v_diam and c == 0:
                    c += 1
                    continue
                d_excl = val
                break
            if d_excl == -1: d_excl = 0 # Should not happen if padded
            
            # Path through u excluding v
            # Sum of top 2 lengths in current_lens
            path_excl = current_lens[0] + current_lens[1]
            
            up_diam[v] = max(d_excl, path_excl)
            
            dfs2(v, u)

    dfs2(0, -1)
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print(max_diameter_after_removal(n, edges))
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
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
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

**Input:**
```
4
0 1
1 2
1 3
```
**Tree:** `2-1-0` and `3-1`. 1 is center.
**DFS 1 (Root 0):**
-   `height`: `2:0, 3:0, 1:1, 0:2`.
-   `diam`: `2:0, 3:0, 1:2 (2-1-3), 0:3 (2-1-0)`.
**DFS 2 (Root 0):**
-   `u=0`. `upHeight[0]=-1`, `upDiam[0]=0`.
-   Child 1. `vLen=2`. `lens=[-1, 2] -> [2, -1, -1]`. `diams=[0, 2] -> [2, 0]`.
-   `upHeight[1] = 1 + (-1) = 0`. (Path 0->nothing).
-   `upDiam[1] = max(0, -1 + -1) = 0`.
-   Edge `(1, 0)` removed.
    -   Comp 1 (Subtree 1): `diam[1]=2`.
    -   Comp 2 (Rest 0): `upDiam[1]=0`.
    -   Max: 2. `maxDiam=2`.
-   Recurse `dfs2(1, 0)`.
    -   `u=1`. `upHeight[1]=0, upDiam[1]=0`.
    -   Children 2, 3.
    -   Arms: `Up(0,0)`, `2(1,0)`, `3(1,0)`.
    -   `lens=[1, 1, 0]`. `diams=[0, 0, 0]`.
    -   Child 2: `vLen=1`.
        -   `bestLen` (excl 1) = 1. `upHeight[2]=2`.
        -   `path` (excl 1) = 1 + 0 = 1.
        -   `upDiam[2] = max(0, 1) = 1`.
        -   Edge `(2, 1)` removed. `diam[2]=0`, `upDiam[2]=1`. Max 1.
    -   Child 3: Same. Max 1.
**Result:** 2. Correct.

## ✅ Proof of Correctness

-   **Rerooting:** Correctly computes the diameter of the "rest of the tree" for every node.
-   **Cases:** Considers max diameter in the rest (from other subtrees) AND max path passing through parent (combining two other arms).

## 💡 Interview Extensions (High-Value Add-ons)

-   **Min Diameter:** Find edge to remove to *minimize* the max diameter. (Center finding).
-   **Weighted Tree:** Same logic, just sum weights.
-   **Centroid Decomposition:** Another way to handle path problems.

### Common Mistakes to Avoid

1.  **Top-K Logic:** Correctly excluding the current child's contribution is tricky. Sorting is easiest.
2.  **Base Cases:** Leaves have height 0 (or -1 depending on definition).
3.  **Recursion Depth:** Python needs `sys.setrecursionlimit`.
