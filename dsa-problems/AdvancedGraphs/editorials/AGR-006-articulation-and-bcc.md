---
problem_id: AGR_ARTICULATION_AND_BCC__7358
display_id: AGR-006
slug: articulation-and-bcc
title: "Articulation Points and Biconnected Components"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - Articulation Points
  - Biconnected Components
tags:
  - advanced-graphs
  - articulation-points
  - bcc
  - medium
premium: true
subscription_tier: basic
---

# AGR-006: Articulation Points and Biconnected Components

## 📋 Problem Summary

Find all **Articulation Points** (vertices whose removal increases the number of connected components) and **Biconnected Components (BCCs)** (maximal subgraphs such that any two vertices in the subgraph can be connected by at least two vertex-disjoint paths).

## 🌍 Real-World Scenario

**Scenario Title:** Single Points of Failure in Networks

In a communication network:

- **Articulation Point:** A critical router or server. If it crashes, the network splits into disconnected parts. Identifying these is crucial for reliability engineering.
- **BCC:** A "safe zone". Within a BCC, even if one router fails (other than the source/destination), there is always an alternative path.
- **Goal:** Harden the network by adding links to eliminate articulation points.

![Real-World Application](../images/AGR-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**

```
    (0) --- (1) --- (3)
     |       |
     \       /
      \     /
        (2)
```

- **Triangle {0, 1, 2}:** Removing any single node (0, 1, or 2) leaves the other two connected. This is a BCC.
- **Edge {1, 3}:** Removing 1 disconnects 3. Removing 3 disconnects nothing. This edge forms a BCC `{1, 3}`.
- **Articulation Point:** Node 1. It connects the triangle to node 3.
- **Note:** Node 1 belongs to _both_ BCCs.

### Algorithm: Tarjan's / Hopcroft-Tarjan

1.  **DFS Traversal:** Maintain `tin` (discovery time) and `low` (lowest reachable ancestor).
2.  **Edge Stack:** Push every visited edge `(u, v)` onto a stack.
3.  **AP Condition:** For a tree edge `u -> v`:
    - If `low[v] >= tin[u]`, then `u` is an Articulation Point (unless `u` is root and has < 2 children).
    - **Extract BCC:** When `low[v] >= tin[u]`, pop edges from the stack until `(u, v)` is popped. All vertices in these edges form a BCC.
4.  **Root Case:** The root of the DFS tree is an AP if and only if it has more than one child in the DFS tree.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **BCC Format:** A BCC is a set of vertices. Since an edge belongs to exactly one BCC, but a vertex can belong to multiple, we extract BCCs as sets of edges and then collect unique vertices.
- **Output:** APs sorted. BCCs in any order.
- **Disconnected Graph:** Handle by running DFS on all unvisited nodes.

## Naive Approach

### Intuition

For each vertex, remove it and check connectivity (O(N\*(N+M))). For BCCs, iterate all pairs? Too slow.

## Optimal Approach (DFS with Stack)

### Time Complexity

- **O(N + M)**: Single DFS pass.

### Space Complexity

- **O(N + M)**: Recursion stack, edge stack, adjacency list.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
4 4
0 1
1 2
2 0
1 3
```

**DFS Trace:**

1.  Start 0. `tin[0]=0`. Stack: `[]`.
2.  Edge `0-1`. `tin[1]=1`. Stack: `[(0,1)]`.
3.  Edge `1-2`. `tin[2]=2`. Stack: `[(0,1), (1,2)]`.
4.  Edge `2-0`. Back-edge. `low[2]=0`. Stack: `[(0,1), (1,2), (2,0)]`.
5.  Return to 1. `low[1]=0`. `low[2] (0) < tin[1] (1)`, so 1 is NOT AP via 2.
6.  Edge `1-3`. `tin[3]=3`. Stack: `[..., (1,3)]`.
7.  Return to 1. `low[1]=0`. `low[3] (3) >= tin[1] (1)`. **AP Found: 1**.
    - Pop stack until `(1,3)`. BCC: `{1, 3}`.
8.  Return to 0. `low[0]=0`. `low[1] (0) >= tin[0] (0)`. **AP Check: 0**.
    - Pop stack until `(0,1)`. Stack has `(2,0), (1,2), (0,1)`.
    - BCC: `{0, 1, 2}`.
    - Is 0 AP? Root check. Children count = 1 (only went to 1). So 0 is NOT AP.

**Result:**

- APs: `{1}`.
- BCCs: `{1, 3}`, `{0, 1, 2}`.

## ✅ Proof of Correctness

- **AP:** `low[v] >= tin[u]` means there is no back-edge from `v` or its descendants to `u`'s ancestor. Removing `u` disconnects `v`.
- **BCC:** The stack ensures we collect all edges in the current biconnected component. Since we pop only when the AP condition is met (or at the end), we isolate maximal biconnected subgraphs.

## 💡 Interview Extensions (High-Value Add-ons)

- **Block-Cut Tree:** Construct a tree where nodes are original APs and BCCs. This allows solving path queries like "does path A->B pass through AP X?" efficiently.
- **Dynamic Connectivity:** Handling edge insertions/deletions is much harder (Holm-de Lichtenberg-Thorup).

### Common Mistakes to Avoid

1.  **Root Case:** Forget to check `children > 1` for root.
2.  **Stack Popping:** Pop edges, not vertices. A vertex can be in multiple BCCs, but an edge is in exactly one.
3.  **Back-Edges:** Push back-edges to stack too! They are part of the BCC.
