---
problem_id: GRB_DFS_CONNECTED_COMPONENTS__5190
display_id: GRB-002
slug: dfs-connected-components
title: "DFS Connected Components"
difficulty: Easy
difficulty_score: 28
topics:
  - Graphs
  - DFS
  - Components
tags:
  - graphs-basics
  - dfs
  - components
  - easy
premium: true
subscription_tier: basic
---
# GRB-002: DFS Connected Components

## 📋 Problem Summary

You are given an undirected graph.
Your task is to count how many connected components it has.
You must also assign a 1-based component id to every node.

## 🌍 Real-World Scenario

**Scenario Title:** Island Hopping Registry

A coastal planning team models islands and bridges as a graph.
Each island is a node.
Each bridge is an undirected edge.
If you can walk between two islands by traversing bridges, they must be in the same cluster.

The registry must label every island with a cluster id.
Cluster ids are used by emergency services to know which islands can share resources.
If a bridge fails, only islands in the same cluster remain mutually reachable.

The dataset is large, with up to one hundred thousand islands and bridges.
So the registry cannot afford expensive pairwise checks.
It needs a linear traversal that touches each island and bridge only a few times.

**Why This Problem Matters:**

- It models real connectivity in networks like roads, social graphs, and LANs.
- It is a core building block for higher-level graph algorithms.
- It is the simplest test of whether your traversal is correct and efficient.

![Real-World Application](../images/GRB-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Connected Components in an Undirected Graph

```
Component 1:         Component 2:

0 ---- 1             2 ---- 3
                      \
                       4
```

Legend:

- Each line is an undirected edge.
- Nodes connected by any path belong to the same component.

In the diagram:

- Component 1 is {0, 1}.
- Component 2 is {2, 3, 4}.

## ✅ Input/Output Clarifications (Read This Before Coding)

- Component ids must be 1-based, assigned in discovery order.
- Isolated nodes still form a component of size 1.
- The graph is undirected, so each edge is bidirectional.

Common interpretation mistake:

- ❌ Assume the graph is connected and skip the outer loop.
- ✅ Always iterate over all nodes and start a new DFS on each unvisited node.

### Core Concept: Flood Fill on Graphs

Connected components in an undirected graph are exactly the sets of nodes reachable from each other.
DFS is a graph flood fill.
Starting DFS from an unvisited node marks its entire component.
Then you move to the next unvisited node and repeat.

### Why a Naive Approach is too slow

A naive approach could test reachability between every pair of nodes.
That would run a BFS or DFS many times.
In the worst case it costs O(N * (N + M)) which is too large for N=100000.
We need a method that runs only a constant number of traversals.

## Naive Approach

### Intuition

If two nodes are reachable, they belong to the same component.
So you could test reachability repeatedly.

### Algorithm

1. For each node u:
2. Run a traversal to mark all nodes reachable from u.
3. Use this reachability to build components.

### Time Complexity

- O(N * (N + M)) in the worst case.

### Space Complexity

- O(N + M) for adjacency storage.

### Why This Works

Reachability defines the component relation.
The traversal correctly identifies all reachable nodes.

### Limitations

- Too slow for large graphs.
- Repeats work by exploring the same edges many times.

## Optional: BFS Alternative Approach

### Intuition

BFS can replace DFS without changing correctness.
It still visits all nodes in a component in one traversal.

### Algorithm

1. Initialize comp array with 0s.
2. For each node i:
3. If comp[i] is 0, increment component counter.
4. Run BFS from i and mark all reachable nodes with that id.

### Time Complexity

- O(N + M)

### Space Complexity

- O(N + M)

### Decision Tree

```
For each node i:
|
|-- Is comp[i] already set?
|      |
|      |-- YES: skip
|      |
|      |-- NO: start traversal
|                 |
|                 |-- Explore neighbors
|                 |-- Mark comp for each visited node
```

## Optimal Approach

### Key Insight

Each node belongs to exactly one component.
So we only need to start a traversal when we find an unvisited node.
Every traversal covers one full component.
The total work across all traversals is linear.

### Algorithm

1. Build adjacency list.
2. Initialize comp array to 0.
3. Initialize `count = 0`.
4. For each node i from 0 to n-1:
5. If comp[i] == 0:
6.   count++
7.   Run DFS from i and mark all reachable nodes with id = count.
8. Output count and comp array.

### Time Complexity

- O(N + M)

### Space Complexity

- O(N + M)

### Why This Is Optimal

Every node is visited once.
Every edge is processed at most twice (once from each endpoint).
Any algorithm must at least read the full input, so O(N + M) is optimal.

![Algorithm Visualization](../images/GRB-002/algorithm-visualization.png)
![Algorithm Steps](../images/GRB-002/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:

- Nodes: `0..3`
- Edges: (0,1) and (2,3)
- Graph is disconnected

We maintain:

- `comp` = component id per node
- `count` = number of components found

Initialize:

- `comp = [0, 0, 0, 0]`
- `count = 0`

Now iterate:

| Step | Node | Action | comp after step | count | Notes |
| ---: | :--: | ------ | --------------- | ----: | ----- |
| 1 | 0 | start DFS | [1,1,0,0] | 1 | visits 0,1 |
| 2 | 1 | skip | [1,1,0,0] | 1 | already set |
| 3 | 2 | start DFS | [1,1,2,2] | 2 | visits 2,3 |
| 4 | 3 | skip | [1,1,2,2] | 2 | already set |

Observations from table:

- Every node is labeled exactly once.
- Each DFS produces one component.

Answer is `2` with ids `1 1 2 2`.

![Example Visualization](../images/GRB-002/example-1.png)

## ✅ Proof of Correctness

### Invariant

When DFS starts from node `u` with id `c`, it marks exactly the set of nodes reachable from `u` with id `c`.

### Why the approach is correct

1. DFS explores all nodes reachable from the start node in an undirected graph.
2. Therefore every node reachable from `u` is assigned id `c`.
3. No node outside the component is reachable from `u`, so none are assigned id `c`.
4. The outer loop starts DFS only from unassigned nodes, so each component is discovered once.

Thus, every node is assigned the correct component id, and the count is exact.

## 💡 Interview Extensions (High-Value Add-ons)

- **Component Sizes:** Return the size of each component in addition to ids.
- **DSU Alternative:** Replace DFS with disjoint set union for batch edge processing.
- **Largest Component:** Track and output the maximum component size.

### Common Mistakes to Avoid

1. **Skipping the outer loop**

   - Description: Only running DFS from node 0 fails on disconnected graphs.
   - ❌ Wrong: Assume the graph is connected.
   - ✅ Correct: Always scan all nodes and start DFS when unvisited.

2. **Recursion depth overflow**

   - Description: Deep recursion can crash on long chains.
   - ❌ Wrong: Unbounded recursive DFS in Python without increasing limits.
   - ✅ Correct: Use an iterative stack or raise recursion limit safely.

3. **Wrong component numbering**

   - Description: Outputting 0-based ids violates the statement.
   - ❌ Wrong: Use ids 0..k-1.
   - ✅ Correct: Use ids 1..k.

4. **Not adding both directions**

   - Description: Treating the undirected graph as directed changes connectivity.
   - ❌ Wrong: Only add `u -> v`.
   - ✅ Correct: Add both `u -> v` and `v -> u`.

## Related Concepts

- Graph traversal (DFS/BFS)
- Disjoint set union (union-find)
- Connected components in directed graphs (SCC)
- Graph coloring as a traversal side effect
