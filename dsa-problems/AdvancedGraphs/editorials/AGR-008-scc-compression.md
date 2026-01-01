---
problem_id: AGR_SCC_COMPRESSION__2659
display_id: AGR-008
slug: scc-compression
title: "Strongly Connected Components Compression"
difficulty: Easy
difficulty_score: 40
topics:
  - Graphs
  - SCC
  - Condensation Graph
tags:
  - advanced-graphs
  - scc
  - condensation
  - easy
premium: true
subscription_tier: basic
---

# AGR-008: Strongly Connected Components Compression

## 📋 Problem Summary

Decompose a directed graph into its **Strongly Connected Components (SCCs)**. Then, contract each SCC into a single node to form a **Condensation Graph**, which is always a Directed Acyclic Graph (DAG).

## 🌍 Real-World Scenario

**Scenario Title:** Software Module Dependencies

Consider a large software project with many modules (files/classes) that depend on each other.

- **Cyclic Dependency:** If Module A depends on B, and B depends on A, they are tightly coupled and must be compiled/deployed together. They form an SCC.
- **Condensation:** To understand the high-level architecture, we group these cyclic clusters into "super-modules".
- **DAG:** The dependencies between these super-modules form a hierarchy (DAG), allowing us to determine a valid build order (Topological Sort).

![Real-World Application](../images/AGR-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Original Graph:**

```
    (0) <--> (1)
     |        |
     v        v
    (2) <--> (3) --> (4)
```

- `0` and `1` form a cycle. SCC A = `{0, 1}`.
- `2` and `3` form a cycle. SCC B = `{2, 3}`.
- `4` is isolated. SCC C = `{4}`.
- Edges:
  - `0->2` becomes `A -> B`.
  - `1->3` becomes `A -> B`.
  - `3->4` becomes `B -> C`.

**Condensation Graph (DAG):**

```
    (A) ===> (B) ---> (C)
```

Note: Multiple edges between SCCs (like `0->2` and `1->3`) are merged into a single edge `A->B`.

### Algorithm: Tarjan's Algorithm

1.  **Find SCCs:**
    - Use **Tarjan's Algorithm** (DFS with stack and low-link values).
    - Maintain `tin` (discovery time), `low` (lowest reachable ancestor), and a `stack` of active nodes.
    - When `low[u] == tin[u]`, pop from stack to form an SCC.
2.  **Build Condensation Graph:**
    - Assign a component ID to each node.
    - Iterate over all original edges `u -> v`.
    - If `comp[u] != comp[v]`, add a directed edge `comp[u] -> comp[v]` to the new graph.
    - Use a Set or sort+unique to remove duplicate edges between components.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Component IDs:** Can be any range `0` to `k-1`.
- **Duplicate Edges:** The condensation graph should not have multi-edges. `A->B` should appear once even if there are 100 edges from nodes in A to nodes in B.
- **Self-Loops:** The condensation graph is a DAG, so no self-loops `A->A` (edges within an SCC are ignored).

## Naive Approach

### Intuition

Run BFS/DFS from every node to check reachability to every other node.

### Time Complexity

- **O(N \* (N+M))**: Too slow for N=200,000.

## Optimal Approach (Tarjan's or Kosaraju's)

### Time Complexity

- **O(N + M)**: Linear time to find SCCs and build the DAG.

### Space Complexity

- **O(N + M)**: Storing the graph and auxiliary arrays.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
3 3
0 1
1 0
1 2
```

**Trace:**

1.  Start DFS(0). `tin[0]=0`. Stack `[0]`.
2.  Edge `0->1`. DFS(1). `tin[1]=1`. Stack `[0, 1]`.
3.  Edge `1->0`. `0` on stack. `low[1] = min(1, tin[0]=0) = 0`.
4.  Edge `1->2`. DFS(2). `tin[2]=2`. Stack `[0, 1, 2]`.
5.  Node 2 done. `low[2]=2`. `low[2]==tin[2]`. **SCC Found: {2}**. Pop 2.
6.  Back to 1. `low[1] = min(0, low[2]=2) = 0`.
7.  Node 1 done. `low[1]=0`. Back to 0. `low[0] = min(0, low[1]=0) = 0`.
8.  Node 0 done. `low[0]=0`. `low[0]==tin[0]`. **SCC Found: {1, 0}**. Pop 1, 0.

**Components:**

- SCC 0: `{2}`. ID=0.
- SCC 1: `{1, 0}`. ID=1.
- `comp = [1, 1, 0]`.

**Edges:**

- `0->1`: Same comp (1->1). Ignore.
- `1->0`: Same comp (1->1). Ignore.
- `1->2`: Diff comp (1->0). Add edge `1->0`.

**Output:**

- K=2.
- Comp: `1 1 0`.
- Edges: `1 0`.
  (Matches logic, IDs can differ but structure is correct).

## ✅ Proof of Correctness

- **SCC:** Tarjan's algorithm correctly identifies SCCs in linear time.
- **Condensation:** By contracting each SCC into a node, any cycle would be contained within a node. Thus, the remaining edges form a DAG.

## 💡 Interview Extensions (High-Value Add-ons)

- **2-SAT:** 2-SAT problems are solved by finding SCCs in the implication graph. If `x` and `!x` are in the same SCC, it's unsatisfiable.
- **Reachability:** In a DAG, reachability can be solved using bitsets or topological sort DP.
- **Semi-Connected:** A graph is semi-connected if for every pair `(u, v)`, there is a path `u->v` OR `v->u`. This is true iff the condensation DAG is a single path (Hamiltonian path in DAG).

### Common Mistakes to Avoid

1.  **Stack Check:** Only update `low[u]` using `tin[v]` if `v` is currently on the stack. If `v` is visited but not on stack, it belongs to an already completed SCC.
2.  **Duplicate Edges:** The condensation graph is a simple graph. Use a Set to avoid adding `A->B` multiple times.
3.  **Recursion Limit:** For N=200,000, use iterative DFS or increase recursion limit.
