---
problem_id: TRE_CAMPUS_DIRECTORY_MULTI_TREE__4813
display_id: TRE-001
slug: campus-directory-multi-tree
title: "Campus Directory Multi-Tree Comparison"
difficulty: Easy
difficulty_score: 28
topics:
  - Trees
  - Traversal
  - Comparison
tags:
  - trees
  - traversal
  - comparison
  - easy
premium: true
subscription_tier: basic
---

# TRE-001: Campus Directory Multi-Tree Comparison

## 📋 Problem Summary

You are given two binary trees. For each tree, you need to generate its **preorder**, **inorder**, and **postorder** traversals. Additionally, you must determine if the two trees are **structurally identical** (having the exact same shape, regardless of node values) and identify which traversal sequences are exactly the same between the two trees.

## 🌍 Real-World Scenario

**Scenario Title:** Organizational Chart Merger

Imagine two companies are merging, and their HR departments need to compare their organizational structures. Each employee is a node in a tree.
1.  **Traversals:** Listing employees in different orders (e.g., by rank, by department) helps in generating different types of reports.
2.  **Structural Identity:** HR wants to know if the *hierarchy* of roles is the same in both companies (e.g., does every Manager have exactly two Team Leads?), even if the people (values) filling those roles are different.
3.  **Matching Traversals:** If the list of employee IDs matches exactly in a specific order, it might indicate that one department was copied from another or that there's a data duplication issue.

![Real-World Application](../images/TRE-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree 1:**
```
    1
   / \
  2   3
```
Traversals:
- Pre: 1 2 3
- In: 2 1 3
- Post: 2 3 1

**Tree 2:**
```
    1
   / \
  3   2
```
Traversals:
- Pre: 1 3 2
- In: 3 1 2
- Post: 3 2 1

**Comparison:**
- **Structure:** Both have a root with left and right children. **Identical**.
- **Traversals:** None match.

### Algorithm Steps

1.  **Traversals:**
    *   **Preorder:** Visit Root -> Left -> Right.
    *   **Inorder:** Visit Left -> Root -> Right.
    *   **Postorder:** Visit Left -> Right -> Root.
    *   Store these sequences for both trees.
2.  **Structural Identity:**
    *   Traverse both trees simultaneously.
    *   At each step, check:
        *   If both nodes are null: Match.
        *   If one is null and the other isn't: Mismatch.
        *   If both exist: Recursively check left children AND right children.
    *   Note: We do **not** compare node values for structural identity.
3.  **Matching Traversals:**
    *   Compare the lists generated in step 1.
    *   If `pre1 == pre2`, add "preorder".
    *   If `in1 == in2`, add "inorder".
    *   If `post1 == post2`, add "postorder".

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Input Format:** Trees are given as an array of nodes. Node `0` is always the root. Children are indices into this array. `-1` means no child.
-   **Empty Tree:** If `n=0`, the tree is empty. Traversals are empty lists. Structural identity with another empty tree is `true`.
-   **Output:** Print lists space-separated. Structural identity is `true`/`false`. Matches are space-separated names or `NONE`.

## Naive Approach

### Intuition

The problem asks for standard traversals and a comparison. Since we have to visit every node to generate traversals, we can't do better than linear time. The "naive" approach is simply the direct implementation of the requirements.

### Algorithm

1.  Implement recursive functions for `preorder`, `inorder`, `postorder`.
2.  Implement a recursive function `isStructurallySame(node1, node2)`.
3.  Run these on the input trees and compare the results.

### Time Complexity

-   **O(N1 + N2)**: We visit every node a constant number of times.

### Space Complexity

-   **O(H1 + H2)**: Recursion stack depth, where H is the height of the tree. In worst case (skewed tree), H=N.

## Optimal Approach

The naive approach is already optimal in terms of time complexity because we must process every node. We can optimize space slightly by using iterative traversals, but recursion is cleaner and standard for this problem.

### Key Insight

For structural identity, ensure you check the *existence* of children, not their values.
`if (node1.left == null && node2.left != null)` -> Different structure.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
2 1 2
1 -1 -1
3 -1 -1
3
1 -1 1
2 -1 2
3 -1 -1
```

**Tree 1:**
- Node 0: val 2, left 1, right 2
- Node 1: val 1, leaf
- Node 2: val 3, leaf
- Structure: Root(2) -> Left(1), Right(3)

**Tree 2:**
- Node 0: val 1, left -1, right 1
- Node 1: val 2, left -1, right 2
- Node 2: val 3, leaf
- Structure: Root(1) -> Right(2) -> Right(3) (Skewed right)

**Traversals T1:**
- Pre: 2 1 3
- In: 1 2 3
- Post: 1 3 2

**Traversals T2:**
- Pre: 1 2 3
- In: 1 2 3
- Post: 3 2 1

**Comparison:**
- **Structure:** T1 has left child, T2 does not. `structural_identity = false`.
- **Matches:**
  - Pre: `2 1 3` vs `1 2 3` (No)
  - In: `1 2 3` vs `1 2 3` (Yes)
  - Post: `1 3 2` vs `3 2 1` (No)
  - Result: `inorder`

**Output:**
```
2 1 3
1 2 3
1 3 2
1 2 3
1 2 3
3 2 1
false
inorder
```

## ✅ Proof of Correctness

### Correctness of Traversals
The recursive definitions (e.g., Preorder = Root, Left, Right) are standard and directly implemented. Since the input guarantees valid trees (no cycles, valid indices), the recursion will terminate and visit every node exactly once.

### Correctness of Structural Check
The function `checkStructure` returns true if and only if:
1.  Both current nodes are null (base case match).
2.  Both current nodes exist AND their left children have matching existence AND their right children have matching existence AND their subtrees recursively match.
This covers all conditions for structural identity.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Symmetric Tree**
    -   Check if a tree is a mirror of itself. (Compare `left` of T1 with `right` of T1).
-   **Extension 2: Subtree Check**
    -   Check if T2 is a subtree of T1. (Requires matching structure and values starting from some node in T1).
-   **Extension 3: Serialize/Deserialize**
    -   How to store a tree in a file so it can be reconstructed? (Preorder + Inorder, or Preorder with null markers).

### Common Mistakes to Avoid

1.  **Comparing Values for Structure:**
    -   ❌ `if (t1[u].val != t2[u].val) return false;` inside `structuralIdentical`.
    -   ✅ Structural identity only cares about shape, not values.
2.  **Null Pointer Exceptions:**
    -   ❌ Accessing `t1[u]` when `u == -1`.
    -   ✅ Always check `u == -1` base case.
3.  **Empty Tree Handling:**
    -   ❌ Forgetting `n=0` case.
    -   ✅ Handle `n=0` explicitly or ensure recursion handles it gracefully.

## Related Concepts

-   **Graph Isomorphism:** A more general version of structural identity.
-   **Tree Serialization:** Converting tree to string.
