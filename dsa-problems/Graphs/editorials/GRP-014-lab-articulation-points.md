---
problem_id: GRP_LAB_ARTICULATION_POINTS__5694
display_id: GRP-014
slug: lab-articulation-points
title: Lab Articulation Points
difficulty: Medium
difficulty_score: 60
topics:
- Graph Theory
- Tarjan's Algorithm
- Articulation Points
tags:
- graph
- tarjan
- articulation-points
- cut-vertices
- hard
premium: true
subscription_tier: premium
---
# GRP-014: Lab Articulation Points

## 📋 Problem Summary

Find all articulation points (cut vertices) in an undirected graph using Tarjan's algorithm. An articulation point is a vertex whose removal increases the number of connected components.

## 🌍 Real-World Scenario

**Scenario Title:** Key Person Identification in Organizations

Imagine analyzing an organizational network where people are nodes and collaborations are edges. An articulation point represents a key person whose departure would fragment the organization into disconnected teams.

Identifying these critical individuals helps with succession planning, team restructuring, and understanding organizational vulnerabilities. Tarjan's algorithm efficiently finds all such key people in a single traversal.

**Why This Problem Matters:**

- **Organizational Analysis:** Identifying key personnel
- **Network Security:** Finding critical routers/servers
- **Social Networks:** Detecting influential connectors
- **Infrastructure:** Identifying critical junctions

![Real-World Application](../images/GRP-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Articulation Points

```
Graph:
    0 --- 1 --- 2
          |     |
          3 --- 4

Articulation Points: 1, 2

Why?
- Removing 1: {0} and {2,3,4} become disconnected
- Removing 2: {0,1,3} and {4} become disconnected
- Removing 0, 3, or 4: Graph stays connected
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Articulation point:** Vertex whose removal increases component count
- **Root special case:** Root is articulation point iff it has ≥2 children in DFS tree
- **Non-root condition:** `low[v] >= disc[u]` for edge (u,v)
- **Discovery/Low:** Same as bridge algorithm

## Optimal Approach

### Algorithm (Tarjan's Articulation Points)

```
find_articulation_points(n, adj):
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    ap = set()
    time = [0]
    
    def dfs(u):
        children = 0
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in adj[u]:
            if disc[v] == -1:
                children += 1
                parent[v] = u
                dfs(v)
                
                low[u] = min(low[u], low[v])
                
                // Non-root: check if v cannot reach above u
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
                
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        
        // Root: articulation point if ≥2 children
        if parent[u] == -1 and children > 1:
            ap.add(u)
    
    for i in 0 to n-1:
        if disc[i] == -1:
            dfs(i)
    
    return list(ap)
```

### Time Complexity: **O(V + E)**
### Space Complexity: **O(V)**

![Algorithm Visualization](../images/GRP-014/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Graph: 0-1, 1-2, 2-3, 3-1 (cycle), 2-4

| Node | disc | low | Parent | Children | AP Check | Result |
|-----:|:----:|:---:|:------:|:--------:|:---------|:-------|
| 0 | 0 | 0 | -1 | 1 | Root with 1 child | Not AP |
| 1 | 1 | 1 | 0 | 2 | low[2]=1 >= disc[1]=1 | AP (node 1) |
| 2 | 2 | 2 | 1 | 2 | low[3]=2 >= disc[2]=2, low[4]=4 >= disc[2]=2 | AP (node 2) |
| 3 | 3 | 1 | 2 | 0 | Back edge to 1 | Not AP |
| 4 | 4 | 4 | 2 | 0 | Leaf | Not AP |

Articulation Points: [1, 2]

![Example Visualization](../images/GRP-014/example-1.png)

## ✅ Proof of Correctness

**Theorem:** Tarjan's algorithm correctly identifies all articulation points.

**Proof:** A non-root vertex u is an articulation point iff it has a child v such that no vertex in v's subtree has a back edge to u's ancestors (`low[v] >= disc[u]`). A root is an articulation point iff it has ≥2 children in the DFS tree.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Find biconnected components
- **Extension 2:** Count components after removing each articulation point
- **Extension 3:** Find all bridges (similar algorithm)
- **Extension 4:** Handle directed graphs (find strongly connected components)

### Common Mistakes to Avoid

1. **Wrong Articulation Point Condition**
   - ❌ Wrong: `low[v] > disc[u]` (bridge condition)
   - ✅ Correct: `low[v] >= disc[u]` for articulation points
   - **Impact:** Misses some articulation points

2. **Forgetting Root Special Case**
   - ❌ Wrong: Using same condition for root and non-root
   - ✅ Correct: Root is AP iff children > 1
   - **Description:** Root has no parent, needs different check

3. **Not Counting Children**
   - ❌ Wrong: Not tracking number of DFS tree children
   - ✅ Correct: Count children for root check
   - **Prevention:** Increment children counter for each unvisited neighbor

4. **Adding Articulation Point Multiple Times**
   - ❌ Wrong: Adding u to list for each child satisfying condition
   - ✅ Correct: Use set to avoid duplicates
   - **Description:** A vertex can be AP due to multiple children

5. **Checking Parent Incorrectly**
   - ❌ Wrong: `parent[u] == -1` vs `parent[u] != -1` confusion
   - ✅ Correct: Non-root check requires `parent[u] != -1`
   - **Description:** Root check requires `parent[u] == -1`

## Related Concepts

- **Bridges:** Edges whose removal disconnects graph
- **Biconnected Components:** Maximal subgraphs with no articulation points
- **Strongly Connected Components:** Directed graph variant
- **Cut Vertices:** Another name for articulation points
- **Block-Cut Tree:** Tree representation of biconnected components
