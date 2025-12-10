# Social Network Common Friend Finder

**Problem ID:** TREE-005
**Display ID:** 34
**Question Name:** Social Network Common Friend Finder
**Slug:** social-network-common-friend-finder
**Title:** Lowest Common Ancestor
**Difficulty:** Medium
**Premium:** No
**Tags:** Tree, Depth-First Search, Binary Tree

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. The lowest common ancestor is defined as the lowest node that has both nodes as descendants (where we allow a node to be a descendant of itself).

## A Simple Scenario (Daily Life Usage)

Imagine you're building a "mutual connections" feature for LinkedIn or Facebook. When viewing two users, you want to find their closest shared connection in the social network tree. For example, if Alice and Bob both know Charlie, but Charlie knows someone higher up who knows both of them, you want to find the closest person in the network who connects to both Alice and Bob. This is their "lowest common ancestor" in the social graph.

## Your Task

Write a function that takes the root of a binary tree and two nodes p and q, and returns their lowest common ancestor.

## Why is it Important?

This problem teaches you:

- Tree ancestry and relationships
- Path-based reasoning in trees
- Recursive tree search strategies
- Finding intersections in tree paths
- Fundamental graph theory concepts

## Examples

### Example 1:

**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
```
         3
       /   \
      5     1
     / \   / \
    6   2 0   8
       / \
      7   4
```
**Output:** `3`
**Explanation:** The LCA of nodes 5 and 1 is 3 (the root), as it's the lowest node that has both as descendants.

### Example 2:

**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
```
         3
       /   \
      5     1
     / \   / \
    6   2 0   8
       / \
      7   4
```
**Output:** `5`
**Explanation:** The LCA of nodes 5 and 4 is 5, since node 5 is an ancestor of itself (by definition).

### Example 3:

**Input:** `root = [1,2], p = 1, q = 2`
```
    1
   /
  2
```
**Output:** `1`
**Explanation:** The LCA of nodes 1 and 2 is 1.

### Example 4:

**Input:** `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4`
```
         6
       /   \
      2     8
     / \   / \
    0   4 7   9
       / \
      3   5
```
**Output:** `2`
**Explanation:** Both nodes are in the left subtree, and 2 is their lowest common ancestor.

## Constraints

- 2 <= Number of nodes <= 10^5
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q will exist in the tree

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Facebook
- LinkedIn
- Twitter
- Instagram

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
