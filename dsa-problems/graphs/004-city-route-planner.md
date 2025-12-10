# City Route Planner

**Problem ID:** GRP-004
**Display ID:** 51
**Question Name:** City Route Planner
**Slug:** city-route-planner
**Title:** Clone Graph
**Difficulty:** Medium
**Premium:** No
**Tags:** Graph, Depth-First Search, Breadth-First Search

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Create a deep copy of an undirected graph where each node contains a value and a list of neighbors.

## A Simple Scenario (Daily Life Usage)

You have a city map showing neighborhoods and their connections. You want to make a backup copy for disaster recovery. Each neighborhood (node) knows its neighbors. You need to duplicate the entire network structure perfectly, creating new nodes with same connections.

## Your Task

Given a reference to a node in a connected undirected graph, return a deep copy of the graph.

## Why is it Important?

This problem teaches you:

- Graph cloning techniques
- Hash map for tracking copies
- DFS/BFS with state
- Deep copy vs shallow copy

## Examples

### Example 1:

**Input:** `adjList = [[2,4],[1,3],[2,4],[1,3]]`
**Output:** `[[2,4],[1,3],[2,4],[1,3]]`
**Explanation:** 4-node graph with connections: 1-2, 1-4, 2-3, 3-4.

### Example 2:

**Input:** `adjList = [[]]`
**Output:** `[[]]`
**Explanation:** Single node with no neighbors.

### Example 3:

**Input:** `adjList = []`
**Output:** `[]`
**Explanation:** Empty graph.

## Constraints

- Number of nodes is in range [0, 100]
- 1 ≤ Node.val ≤ 100
- Node.val is unique for each node
- No repeated edges and no self-loops
- Graph is connected

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Google
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
