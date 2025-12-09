# Game Level Progression Tracker

**Problem ID:** TREE-006
**Display ID:** 35
**Question Name:** Game Level Progression Tracker
**Slug:** game-level-progression-tracker
**Title:** Binary Tree Level Order Traversal
**Difficulty:** Medium
**Premium:** No
**Tags:** Tree, Breadth-First Search, Binary Tree, Queue

## Problem Description

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## A Simple Scenario (Daily Life Usage)

Think about video game progression systems in games like Mario, Zelda, or RPGs. Each level of the game unlocks new stages that you can play. Level 1 might have stages A and B, Level 2 might have stages C, D, and E. Game developers at Unity, Epic Games, and Nintendo use level-order traversal to track player progression through the game - completing all stages in Level 1 before moving to Level 2, and so on. This is exactly what BFS (Breadth-First Search) does with trees.

## Your Task

Write a function that takes the root of a binary tree and returns an array of arrays, where each inner array contains all node values at that level.

## Why is it Important?

This problem teaches you:

- Breadth-First Search (BFS) algorithm
- Queue data structure usage
- Level-by-level tree processing
- Understanding tree height and width
- Foundation for many graph algorithms

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
**Output:** `[[3], [9,20], [15,7]]`
**Explanation:** Level 0: [3], Level 1: [9,20], Level 2: [15,7]

### Example 2:

**Input:** `root = [1]`
**Output:** `[[1]]`
**Explanation:** Only one level with one node.

### Example 3:

**Input:** `root = []`
**Output:** `[]`
**Explanation:** Empty tree returns empty array.

### Example 4:

**Input:** `root = [1,2,3,4,5,6,7]`
```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```
**Output:** `[[1], [2,3], [4,5,6,7]]`
**Explanation:** Three levels: root, two middle nodes, four leaf nodes.

## Constraints

- 0 <= Number of nodes <= 2000
- -1000 <= Node.val <= 1000

## Asked by Companies

- Unity Technologies
- Epic Games
- Blizzard Entertainment
- Nintendo
