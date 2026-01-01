---
problem_id: TRE_CAMPUS_BST_INSERT_SEARCH__2824
display_id: TRE-014
slug: campus-bst-insert-search
title: "Campus BST Insert & Search"
difficulty: Easy
difficulty_score: 30
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - insertion
  - easy
premium: true
subscription_tier: basic
---

# TRE-014: Campus BST Insert & Search

## 📋 Problem Summary

You are given a sequence of numbers.
1.  **Build a Binary Search Tree (BST)** by inserting these numbers one by one in the given order.
2.  **Search** for a specific target value `x` in the constructed BST.
3.  Output the **Inorder Traversal** of the tree (which should be sorted) and the result of the search (`true` or `false`).

## 🌍 Real-World Scenario

**Scenario Title:** Library Book Cataloging

Imagine a librarian receiving a shipment of new books.
-   **Insertion:** As each book arrives, the librarian places it on the shelf. If the book's ID is smaller than the current one, they go left; if larger, they go right. This builds a structured organization (BST).
-   **Search:** A student asks for a specific book ID. The librarian uses the structure to quickly find it or confirm it's missing.
-   **Inorder:** Reading the shelf from left to right lists all book IDs in sorted order.

![Real-World Application](../images/TRE-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Input:** `4, 2, 6, 1, 3`

1.  **Insert 4:** Root is 4.
2.  **Insert 2:** 2 < 4. Left child of 4.
3.  **Insert 6:** 6 > 4. Right child of 4.
4.  **Insert 1:** 1 < 4 -> 1 < 2. Left child of 2.
5.  **Insert 3:** 3 < 4 -> 3 > 2. Right child of 2.

**Tree:**
```
      4
     / \
    2   6
   / \
  1   3
```

**Inorder:** `1 2 3 4 6` (Sorted).

**Search 5:**
-   5 > 4 (Go Right).
-   5 < 6 (Go Left).
-   Left of 6 is null. **Not Found**.

### Algorithm Steps

1.  **Node Class:** Define a simple `TreeNode` with `val`, `left`, `right`.
2.  **Insertion:**
    -   Start at root.
    -   If value < current.val, go left. If left is null, insert here.
    -   If value >= current.val, go right. If right is null, insert here. (Problem says duplicates to right).
3.  **Search:**
    -   Start at root.
    -   If current is null, return `false`.
    -   If val == target, return `true`.
    -   If target < val, recurse left.
    -   If target > val, recurse right.
4.  **Inorder:**
    -   Recurse left -> Visit node -> Recurse right.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Duplicates:** Problem statement says "Duplicates, if any, must be inserted into the right subtree." This implies `val >= node.val` goes right.
-   **Empty Input:** If `n=0`, output empty line and `false`.
-   **Output Format:** Space-separated integers for inorder.

## Naive Approach

### Intuition

Since the problem asks to simulate BST insertion, the "naive" approach is simply the standard iterative or recursive insertion. There isn't really a "worse" way unless you sort the array first (which changes the tree structure) or use an unbalanced structure when a balanced one isn't asked for.

### Time Complexity

-   **Insertion:** O(N) worst case (skewed tree), O(log N) average. Total for N nodes: O(N^2) worst case.
-   **Search:** O(N) worst case.

## Optimal Approach (Standard BST Operations)

We implement the standard recursive or iterative BST logic. Since the problem requires the specific tree structure resulting from the insertion order, we **cannot** balance the tree (e.g., AVL/Red-Black) as that would change the structure.

### Algorithm

1.  `root = null`.
2.  For each value `v`: `root = insert(root, v)`.
3.  `inorder(root)` -> print.
4.  `found = search(root, x)` -> print.

### Time Complexity

-   **O(N^2)** worst case (if input is sorted).
-   **O(N log N)** average case.

### Space Complexity

-   **O(N)** to store nodes.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
4 2 6 1 3
5
```

**Insertion:**
1.  **4**: Root.
2.  **2**: Left of 4.
3.  **6**: Right of 4.
4.  **1**: Left of 2.
5.  **3**: Right of 2.

**Inorder Traversal:**
-   Left of 4 -> (Left of 2 -> 1, Node 2, Right of 2 -> 3) -> `1 2 3`
-   Node 4
-   Right of 4 -> (6)
-   Result: `1 2 3 4 6`

**Search 5:**
-   Start 4. 5 > 4 -> Right.
-   Curr 6. 5 < 6 -> Left.
-   Left of 6 is null. Return `false`.

## ✅ Proof of Correctness

The algorithm directly implements the definition of BST insertion and search.
-   **Insertion:** Maintains the invariant `left < node <= right` at every step.
-   **Inorder:** By definition, inorder traversal of a BST yields sorted values.
-   **Search:** Uses the BST property to eliminate half the search space (ideally) at each step, guaranteeing correctness if the element exists.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Delete Node**
    -   Implement deletion (handling 0, 1, 2 children).
-   **Extension 2: Balance Tree**
    -   Convert the BST to a balanced AVL/Red-Black tree.
-   **Extension 3: LCA in BST**
    -   Find LCA (much easier in BST than generic tree).

### Common Mistakes to Avoid

1.  **Duplicate Handling:**
    -   ❌ Ignoring duplicates or putting them left.
    -   ✅ Problem specifies duplicates go to the right.
2.  **State Management:**
    -   ❌ Forgetting to reset root between test cases (if static).
3.  **Recursion Depth:**
    -   ❌ Stack overflow on sorted input (skewed tree) for large N. Iterative approach avoids this.

## Related Concepts

-   **BST Properties**
-   **Recursion vs Iteration**
-   **Tree Traversal**
