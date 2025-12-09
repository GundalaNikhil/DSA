# Social Network Friend Connections

**Problem ID:** GRP-001
**Display ID:** 48
**Question Name:** Social Network Friend Connections
**Slug:** social-network-friend-connections
**Title:** Number of Connected Components
**Difficulty:** Medium
**Premium:** No
**Tags:** Graph, Union Find, Depth-First Search

## Problem Description

Given n people and a list of friend connections, find how many separate friend groups exist (connected components).

## A Simple Scenario (Daily Life Usage)

In your class of 5 students: Alice-Bob are friends, Carol-David are friends, Emma is alone. That's 3 separate friend groups (components). At a party, these groups would naturally cluster together. This helps organize team-building activities!

## Your Task

Given n nodes and edge list, return the number of connected components.

## Why is it Important?

This problem teaches you:

- Graph connectivity
- Union-Find algorithm
- DFS/BFS traversal
- Community detection

## Examples

### Example 1:

**Input:** `n = 5, edges = [[0,1], [1,2], [3,4]]`
**Output:** `2`
**Explanation:** Nodes {0,1,2} form one component, {3,4} form another.

### Example 2:

**Input:** `n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]`
**Output:** `1`
**Explanation:** All nodes are connected in one component.

### Example 3:

**Input:** `n = 4, edges = []`
**Output:** `4`
**Explanation:** No connections, so 4 separate components.

## Constraints

- 1 ≤ n ≤ 2000
- 0 ≤ edges.length ≤ 5000
- edges[i].length == 2
- 0 ≤ edges[i][0], edges[i][1] < n
- No duplicate edges

## Asked by Companies

- Facebook
- LinkedIn
- Twitter
- Instagram
