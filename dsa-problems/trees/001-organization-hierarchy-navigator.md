# Organization Hierarchy Navigator

**Problem ID:** TREE-001
**Display ID:** 30
**Question Name:** Organization Hierarchy Navigator
**Slug:** organization-hierarchy-navigator
**Title:** Binary Tree Maximum Depth
**Difficulty:** Easy
**Premium:** No
**Tags:** Tree, Depth-First Search, Binary Tree, Recursion

## Problem Description

Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## A Simple Scenario (Daily Life Usage)

Imagine you're analyzing a company's organizational chart. The CEO is at the top, and below them are various levels of management down to individual contributors. You need to find how many levels deep the organization goes - from the CEO to the lowest-level employee. This helps HR understand the hierarchy complexity and identify potential management bottlenecks.

## Your Task

Write a function that takes the root of a binary tree and returns the maximum depth (number of levels) in the tree.

## Why is it Important?

This problem teaches you:

- Tree traversal fundamentals (DFS)
- Recursive thinking and base cases
- Understanding tree depth and height
- Foundation for more complex tree algorithms
- Analyzing hierarchical data structures

## Examples

### Example 1:

**Input:** `root = [3,9,20,null,null,15,7]`
```
    3
   / \
  9  20
    /  \
   15   7
```
**Output:** `3`
**Explanation:** The maximum depth is 3, going from 3 -> 20 -> 15 (or 7).

### Example 2:

**Input:** `root = [1,null,2]`
```
  1
   \
    2
```
**Output:** `2`
**Explanation:** The tree has 2 levels: root (1) and its right child (2).

### Example 3:

**Input:** `root = []`
**Output:** `0`
**Explanation:** An empty tree has depth 0.

### Example 4:

**Input:** `root = [1]`
**Output:** `1`
**Explanation:** A single node tree has depth 1.

## Constraints

- 0 <= Number of nodes <= 10^4
- -100 <= Node.val <= 100

## Asked by Companies

- LinkedIn
- Microsoft
- Oracle
- SAP
