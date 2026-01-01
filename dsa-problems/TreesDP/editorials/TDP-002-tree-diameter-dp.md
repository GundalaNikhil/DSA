---
problem_id: TDP_TREE_DIAMETER_DP__4829
display_id: TDP-002
slug: tree-diameter-dp
title: "Tree Diameter DP"
difficulty: Medium
difficulty_score: 40
topics:
  - Tree DP
  - DFS
  - Tree Diameter
tags:
  - tree-properties
  - dfs
  - longest-path
premium: true
subscription_tier: basic
---

# TDP-002: Tree Diameter DP

## 📋 Problem Summary

Find the diameter of a tree, which is the longest path between any two nodes, using dynamic programming with DFS traversal in O(n) time.

## 🌍 Real-World Scenario

**Scenario Title:** Network Latency Optimization in Data Centers

A major cloud computing company operates a vast data center network where servers are connected in a tree topology (no cycles to prevent broadcast storms). The network team needs to determine the maximum possible communication delay between any two servers to establish SLA (Service Level Agreement) guarantees.

The diameter of the network tree represents the worst-case communication path - the maximum number of hops required for any two servers to communicate. This critical metric helps engineers decide where to place cache servers, determine network upgrade priorities, and set realistic latency expectations for distributed applications. If the diameter is too large, it might indicate the need for network restructuring or additional cross-links (converting the tree to a more complex graph).

This concept is also used in biological phylogenetic trees to understand evolutionary distance, in social network analysis to measure the "small world" phenomenon, and in compiler design for dependency graph analysis.

**Why This Problem Matters:**

- **Network Planning:** Determines worst-case latency and helps optimize network topology
- **Scalability Analysis:** Identifies potential bottlenecks in hierarchical systems
- **Efficient Algorithm:** O(n) solution instead of O(n²) brute force saves computation for large networks

![Real-World Application](../images/TDP-002/real-world-scenario.png)

## Detailed Explanation

The diameter of a tree is the length of the longest path between any two nodes. A key insight is that this longest path must go through some node, and from that node, it extends to its two farthest descendant subtrees.

**Key Properties:**

1. The diameter is the maximum of all (height1 + height2 + 2) values, where height1 and height2 are the two largest heights of subtrees for any node
2. Alternatively, we can find the diameter using two BFS/DFS: first find the farthest node from any arbitrary node, then find the farthest node from that node

The DP approach computes for each node:

- The maximum depth in its subtree
- The potential diameter passing through that node (sum of two largest child depths)

## Naive Approach

**Intuition:**
Try all pairs of nodes and compute the distance between them using DFS or BFS. The maximum distance found is the diameter.

### Algorithm

```
function find_diameter_naive():
    max_distance = 0

    // Step 1: Try all pairs of nodes
    for u from 1 to n:
        for v from u+1 to n:
            // Step 2: BFS to find distance
            dist = bfs_distance(u, v)
            max_distance = max(max_distance, dist)

    return max_distance

function bfs_distance(start, end):
    queue = [start]
    visited = {start: 0}
    while queue not empty:
        node = queue.pop()
        if node == end: return visited[node]
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.push(neighbor)
```

### Complexity Analysis

| Phase           | Time      | Space    | Explanation                        |
| --------------- | --------- | -------- | ---------------------------------- |
| Node pairs      | O(n²)     | O(1)     | n(n-1)/2 pairs                     |
| BFS per pair    | O(n)      | O(n)     | Visit all nodes worst case         |
| **Naive Total** | **O(n³)** | **O(n)** | Or O(n²) with all-pairs precompute |

**Why This Complexity:**

- n² pairs × O(n) BFS each = O(n³)
- Can optimize to O(n²) by precomputing all distances, but still too slow
- For n = 200,000: ~8×10¹⁵ operations (infeasible)

**Limitations:**

- Extremely slow for large trees (n = 200,000 would require billions of operations)
- Redundant computation - most pairs aren't endpoints of the diameter
- Doesn't leverage tree structure properties

## Optimal Approach

**Key Insight:**
The diameter either passes through a node (connecting its two deepest subtrees) or is entirely within one subtree. By computing the two largest depths for each node during a single DFS, we can find the diameter in one pass.

### Algorithm

**Method 1: Single DFS with DP**

```
function find_diameter():
    diameter = 0

    function dfs(node, parent):
        max1 = max2 = 0  // Two largest child depths

        for each child of node (except parent):
            child_depth = dfs(child, node)

            // Track two largest depths
            if child_depth > max1:
                max2 = max1
                max1 = child_depth
            else if child_depth > max2:
                max2 = child_depth

        // Path through this node = max1 + max2
        diameter = max(diameter, max1 + max2)

        return max1 + 1  // Depth of this subtree

    dfs(1, -1)
    return diameter
```

**Method 2: Two BFS/DFS**

```
function find_diameter_two_bfs():
    // Step 1: Find farthest node from arbitrary start
    u = bfs_farthest(node=1)

    // Step 2: Find farthest from u (this is diameter endpoint)
    v, distance = bfs_farthest_with_distance(u)

    return distance
```

### Complexity Analysis

| Phase                    | Time          | Space    | Explanation                    |
| ------------------------ | ------------- | -------- | ------------------------------ |
| **Method 1: Single DFS** |               |          |                                |
| DFS traversal            | O(n)          | O(h)     | Visit each node once           |
| Track max depths         | O(1) per node | O(1)     | Constant work                  |
| **Total**                | **O(n)**      | **O(h)** | h = height ≤ n                 |
| **Method 2: Two BFS**    |               |          |                                |
| First BFS                | O(n)          | O(n)     | Find one endpoint              |
| Second BFS               | O(n)          | O(n)     | Find other endpoint + distance |
| **Total**                | **O(n)**      | **O(n)** | Linear                         |

**Why This Is Optimal:**

- Each edge is visited exactly once (or twice in two-BFS method)
- No redundant computation
- Linear time is optimal since we must visit all nodes
- For n = 200,000: ~200K operations vs ~40B naive

![Algorithm Visualization](../images/TDP-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


---

## 🧪 Test Case Walkthrough (Dry Run)

### Input

```
5
1 2
1 3
2 4
2 5
```

### Visual Representation

```
Tree Structure:
        1
       / \
      2   3
     / \
    4   5

Edges: 1-2, 1-3, 2-4, 2-5
```

### DFS Walkthrough (rooted at 1)

| Node | Children | Depths from children | max1 | max2 | Diameter candidate | Return |
| ---- | -------- | -------------------- | ---- | ---- | ------------------ | ------ |
| 4    | none     | []                   | 0    | 0    | 0                  | 1      |
| 5    | none     | []                   | 0    | 0    | 0                  | 1      |
| 2    | 4, 5     | [1, 1]               | 1    | 1    | **2**              | 2      |
| 3    | none     | []                   | 0    | 0    | 0                  | 1      |
| 1    | 2, 3     | [2, 1]               | 2    | 1    | **3**              | 3      |

**Diameter = max(0, 2, 3) = 3** (path: 4→2→1→3 or 5→2→1→3)

**Output:** `3`

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                  | ❌ Wrong                        | ✅ Correct                                      |
| --- | ------------------------ | ------------------------------- | ----------------------------------------------- |
| 1   | **Track only one depth** | `diameter = max1`               | `diameter = max1 + max2`                        |
| 2   | **Wrong return value**   | `return max1 + max2` (diameter) | `return max1 + 1` (depth for parent)            |
| 3   | **Forget base case**     | No handling for leaves          | `return 1` for leaf nodes                       |
| 4   | **Off-by-one in edges**  | `diameter = max1 + max2 + 2`    | `diameter = max1 + max2` (depths include edges) |

### Detailed Example:

**Mistake 2: Returning Diameter Instead of Depth**


---

## Related Concepts

- **Tree Height:** Maximum depth from root (special case of diameter)
- **Tree Center:** Node(s) minimizing maximum distance to all other nodes
- **Tree Centroid:** Node whose removal creates most balanced subtrees
- **All-Pairs Shortest Paths:** General problem tree diameter is a special case of


## Constraints

- `2 ≤ n ≤ 2 × 10^5`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree (connected, acyclic)
- All edge lengths are 1