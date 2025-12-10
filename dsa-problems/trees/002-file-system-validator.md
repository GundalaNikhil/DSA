# File System Validator

**Problem ID:** TREE-002
**Display ID:** 31
**Question Name:** File System Validator
**Slug:** file-system-validator
**Title:** Validate Binary Search Tree
**Difficulty:** Medium
**Premium:** No
**Tags:** Tree, Binary Search Tree, Depth-First Search, Recursion

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key
- The right subtree of a node contains only nodes with keys greater than the node's key
- Both the left and right subtrees must also be binary search trees

## A Simple Scenario (Daily Life Usage)

Imagine you're building a file management system that organizes files by size. Smaller files go to the left, larger files go to the right. You need to validate that the file tree structure is properly organized - ensuring every file in the left subtree is smaller than its parent, and every file in the right subtree is larger. This maintains efficient file searching and retrieval.

## Your Task

Write a function that takes the root of a binary tree and returns `true` if it's a valid BST, `false` otherwise.

## Why is it Important?

This problem teaches you:

- BST properties and validation
- Range-based tree validation
- Recursive constraint passing
- In-order traversal techniques
- Data structure integrity checking

## Examples

### Example 1:

**Input:** `root = [2,1,3]`
```
    2
   / \
  1   3
```
**Output:** `true`
**Explanation:** This is a valid BST. 1 < 2 < 3.

### Example 2:

**Input:** `root = [5,1,4,null,null,3,6]`
```
      5
     / \
    1   4
       / \
      3   6
```
**Output:** `false`
**Explanation:** The root's right child (4) is less than the root (5), but node 3 in the right subtree is also less than 5. This violates BST properties.

### Example 3:

**Input:** `root = [5,4,6,null,null,3,7]`
```
      5
     / \
    4   6
       / \
      3   7
```
**Output:** `false`
**Explanation:** Node 3 is in the right subtree of 5, but 3 < 5, which violates BST rules.

### Example 4:

**Input:** `root = [10,5,15,null,null,6,20]`
```
       10
      /  \
     5   15
        /  \
       6   20
```
**Output:** `false`
**Explanation:** Node 6 is in the right subtree of 10, but 6 < 10, violating BST properties.

## Constraints

- 0 <= Number of nodes <= 10^4
- -2^31 <= Node.val <= 2^31 - 1

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
