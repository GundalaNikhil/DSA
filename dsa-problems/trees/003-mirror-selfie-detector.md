# Mirror Selfie Detector

**Problem ID:** TREE-003
**Display ID:** 32
**Question Name:** Mirror Selfie Detector
**Slug:** mirror-selfie-detector
**Title:** Symmetric Tree
**Difficulty:** Easy
**Premium:** No
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## A Simple Scenario (Daily Life Usage)

Think of a butterfly - its left wing is a perfect mirror image of its right wing. Photo editing apps like Photoshop, Snapchat, and Instagram use symmetry detection to apply mirror filters and effects. When you take a selfie with a symmetry filter, the app checks if your face is symmetric. Similarly, this algorithm checks if a tree structure is symmetric.

## Your Task

Write a function that takes the root of a binary tree and returns `true` if the tree is symmetric, `false` otherwise.

## Why is it Important?

This problem teaches you:

- Tree comparison techniques
- Recursive mirroring logic
- Simultaneous tree traversal
- Understanding structural symmetry
- Both iterative and recursive approaches

## Examples

### Example 1:

**Input:** `root = [1,2,2,3,4,4,3]`
```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```
**Output:** `true`
**Explanation:** The tree is symmetric - left side mirrors the right side perfectly.

### Example 2:

**Input:** `root = [1,2,2,null,3,null,3]`
```
      1
     / \
    2   2
     \   \
      3   3
```
**Output:** `false`
**Explanation:** The tree is not symmetric. The right children of both 2's are on the same side.

### Example 3:

**Input:** `root = [1]`
**Output:** `true`
**Explanation:** A single node is always symmetric.

### Example 4:

**Input:** `root = [1,2,3]`
```
    1
   / \
  2   3
```
**Output:** `true`
**Explanation:** The tree is symmetric at the first level below root.

## Constraints

- 0 <= Number of nodes <= 1000
- -100 <= Node.val <= 100

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Adobe Photoshop
- Snapchat
- Instagram
- TikTok

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
