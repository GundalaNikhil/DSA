---
problem_id: CON_DEADLOCK_WFG__7D1C
display_id: CON-006
slug: deadlock-detection-resource-graph
title: "Deadlock Detection in Wait-For Graph"
difficulty: Medium
difficulty_score: 57
topics:
  - Concurrency
  - Deadlocks
  - Graphs
  - Cycle Detection
tags:
  - concurrency
  - deadlock
  - graph
  - cycle-detection
  - medium
premium: true
subscription_tier: basic
---

# Deadlock Detection in Wait-For Graph

## Problem summary

You are given a directed graph representing “who waits for whom”.

Deadlock exists if and only if there is a directed cycle.

So the task reduces to: detect a cycle in a directed graph with up to `10^5` nodes and `2*10^5` edges.

## Why this is a concurrency problem (not just graphs)

In OS / databases, deadlock detection runs periodically:

- Each thread/transaction is a node.
- An edge forms when you wait for a lock held by someone else.

### Correct approaches

### Approach 1: DFS with colors (classic)

Maintain a state per node:

- 0 = unvisited
- 1 = visiting (in recursion stack)
- 2 = done

When DFS explores an edge to a node with state 1, you found a back edge ⇒ cycle ⇒ deadlock.

Complexity: O(n + m).

Important for large input:

- recursion depth can overflow in Java/Python; use iterative DFS or increase recursion limit carefully (still risky).

### Approach 2: Kahn’s algorithm (topological sort)

If the graph is acyclic, it has a topological ordering.

- compute indegree for each node
- push all indegree-0 nodes into queue
- pop and reduce indegrees

If you process all nodes, no cycle.
If some nodes remain, they are in cycles (or reachable only from cycles).

Complexity: O(n + m).
Memory: O(n + m) for adjacency.

This is often easier to implement iteratively and avoids recursion issues.

### Common mistakes

- Using union-find: does not detect cycles in directed graphs.
- Forgetting that the graph can be disconnected.
- Missing large constraints: O(n*m) is impossible here.

## Interview note

If asked “how to find which threads are deadlocked”, you can:

- return nodes that remain unprocessed in Kahn’s algorithm, or
- extract the cycle using parent pointers in DFS.

But this problem only asks for detection, so a boolean is enough.

## Implementations

### Java


### Python


### C++


### JavaScript

