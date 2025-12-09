# Family Tree Path Finder

**Problem ID:** TREE-004
**Display ID:** 33
**Question Name:** Family Tree Path Finder
**Slug:** family-tree-path-finder
**Title:** Binary Tree Paths
**Difficulty:** Easy
**Premium:** No
**Tags:** Tree, Depth-First Search, Backtracking, String

## Problem Description

Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.

## A Simple Scenario (Daily Life Usage)

Imagine you're working on a genealogy website like Ancestry.com. You want to show all possible lineages from a common ancestor down to their descendants who have no children (leaf nodes). Each path represents a unique family line - from great-great-grandfather down through the generations to a specific descendant. This helps users trace their family heritage.

## Your Task

Write a function that takes the root of a binary tree and returns an array of strings, where each string represents a path from root to leaf.

## Why is it Important?

This problem teaches you:

- Root-to-leaf path traversal
- Backtracking techniques
- String building during recursion
- DFS with path tracking
- Complete tree exploration

## Examples

### Example 1:

**Input:** `root = [1,2,3,null,5]`
```
    1
   / \
  2   3
   \
    5
```
**Output:** `["1->2->5", "1->3"]`
**Explanation:** There are two paths from root to leaves: 1->2->5 and 1->3.

### Example 2:

**Input:** `root = [1]`
**Output:** `["1"]`
**Explanation:** Single node is both root and leaf.

### Example 3:

**Input:** `root = [1,2,3,4,5,6,7]`
```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```
**Output:** `["1->2->4", "1->2->5", "1->3->6", "1->3->7"]`
**Explanation:** Four complete paths from root to all leaf nodes.

### Example 4:

**Input:** `root = [5,3,8,1,null,7,9]`
```
      5
     / \
    3   8
   /   / \
  1   7   9
```
**Output:** `["5->3->1", "5->8->7", "5->8->9"]`
**Explanation:** Three paths to the three leaf nodes (1, 7, 9).

## Constraints

- 1 <= Number of nodes <= 100
- -100 <= Node.val <= 100

## Asked by Companies

- Ancestry.com
- MyHeritage
- FamilySearch
- Geni
