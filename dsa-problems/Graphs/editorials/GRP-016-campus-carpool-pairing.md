---
problem_id: GRP_CAMPUS_CARPOOL_PAIRING__2914
display_id: GRP-016
slug: campus-carpool-pairing
title: Campus Carpool Pairing
difficulty: Medium
difficulty_score: 45
topics:
- Union-Find
- Cycle Detection
- Forest
tags:
- graph
- union-find
- cycle-detection
- forest
- medium
premium: true
subscription_tier: basic
---
# GRP-016: Campus Carpool Pairing

## 📋 Problem Summary

Determine if adding a new edge creates a cycle in an undirected graph using Union-Find. A graph is a forest (acyclic) if no cycles exist. Return true if the graph remains a forest after adding the edge.

## 🌍 Real-World Scenario

**Scenario Title:** Network Connection Validation

Imagine building a computer network where you want to avoid redundant connections (cycles) to minimize cost while maintaining connectivity. Before adding a new cable, you need to verify it won't create a cycle.

Union-Find efficiently detects if two nodes are already connected. If they are, adding an edge between them creates a cycle. This is crucial for network design, spanning tree construction, and resource optimization.

**Why This Problem Matters:**

- **Network Design:** Avoiding redundant connections
- **Spanning Tree Construction:** Building minimal connected graphs
- **Resource Optimization:** Minimizing infrastructure costs
- **Kruskal's MST:** Core component of the algorithm

![Real-World Application](../images/GRP-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Cycle Detection with Union-Find

```
Current graph (forest):
    0 --- 1
    
    2 --- 3

Adding edge (1, 2):
    0 --- 1
          |
    2 --- 3

Result: Still a forest (no cycle)

Adding edge (0, 3):
    0 --- 1
    |     |
    2 --- 3

Result: Cycle detected! (0-1-2-3-0)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Forest:** Graph with no cycles (collection of trees)
- **Cycle detection:** If find(u) == find(v), adding (u,v) creates cycle
- **Union-Find:** Efficiently tracks connected components
- **Return:** true if remains forest, false if cycle created

## Optimal Approach

### Algorithm

```
is_forest_after_adding(n, existing_edges, new_edge):
    uf = UnionFind(n)
    
    // Build current graph
    for (u, v) in existing_edges:
        if uf.find(u) == uf.find(v):
            return false  // Already has cycle
        uf.union(u, v)
    
    // Check new edge
    (u, v) = new_edge
    if uf.find(u) == uf.find(v):
        return false  // Would create cycle
    
    return true  // Remains a forest
```

### Time Complexity: **O(E × α(n))** where α is inverse Ackermann
### Space Complexity: **O(n)**

![Algorithm Visualization](../images/GRP-016/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

n=4, existing_edges=[(0,1), (2,3)], new_edge=(1,2)

1. Union(0,1): {0,1}, {2}, {3} ✓
2. Union(2,3): {0,1}, {2,3} ✓
3. Check new_edge(1,2): find(1)=0, find(2)=2, different roots ✓

Result: Remains a forest

![Example Visualization](../images/GRP-016/example-1.png)

## ✅ Proof of Correctness

**Theorem:** Union-Find correctly detects cycles in undirected graphs.

**Proof:** If find(u) == find(v), u and v are already connected. Adding edge (u,v) creates a cycle. Union-Find maintains disjoint sets, ensuring correct connectivity tracking.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Return which edge to remove to break cycle
- **Extension 2:** Count number of trees in forest
- **Extension 3:** Find all edges that would create cycles
- **Extension 4:** Implement Kruskal's MST algorithm

### Common Mistakes to Avoid

1. **Not Checking Existing Edges**
   - ❌ Wrong: Only checking new edge
   - ✅ Correct: Build graph first, then check new edge
   - **Impact:** Misses existing cycles

2. **Using Union Return Value Incorrectly**
   - ❌ Wrong: Ignoring union's return value
   - ✅ Correct: Return false if union fails (cycle detected)
   - **Description:** Union returns false when roots are same

3. **Forgetting Path Compression**
   - ❌ Wrong: Simple find without optimization
   - ✅ Correct: Implement path compression
   - **Prevention:** Ensures O(α(n)) amortized time

4. **Not Using Rank/Size**
   - ❌ Wrong: Always attaching to first root
   - ✅ Correct: Union by rank or size
   - **Description:** Prevents tree degradation

5. **Directed vs Undirected Confusion**
   - ❌ Wrong: Treating edges as directed
   - ✅ Correct: Undirected edges (u,v) same as (v,u)
   - **Description:** Union-Find works for undirected graphs

## Related Concepts

- **Kruskal's MST:** Uses Union-Find for cycle detection
- **Cycle Detection in Undirected Graphs:** Core application
- **Minimum Spanning Tree:** Forest with minimum total weight
- **Dynamic Connectivity:** Online Union-Find queries
