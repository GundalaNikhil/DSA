# Word Search Puzzle

**Problem ID:** BACK-005
**Display ID:** 64
**Question Name:** Word Search Puzzle
**Slug:** word-search-puzzle
**Title:** Word Search
**Difficulty:** Medium
**Premium:** No
**Tags:** Backtracking, Array, Matrix, DFS

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## A Simple Scenario (Daily Life Usage)

Remember those word search puzzles in newspapers and puzzle books? You're given a grid of letters and need to find if a specific word exists by connecting adjacent letters (up, down, left, right). For example, finding "SEARCH" in a letter grid where each letter must be adjacent to the next, and you can't reuse the same cell twice.

## Your Task

Write a function that searches for a word in a 2D grid. The word must be formed by adjacent cells, and each cell can only be used once in the word path.

## Why is it Important?

This problem teaches you how to:

- Implement depth-first search (DFS) with backtracking
- Track visited cells during exploration
- Handle 4-directional grid traversal
- Manage state restoration (backtracking)
- Optimize with early termination

## Examples

### Example 1:

**Input:**
```
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
```
**Output:** `true`
**Explanation:** Starting at (0,0) 'A', we can form: A → B → C → C → E → D

### Example 2:

**Input:**
```
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"
```
**Output:** `true`
**Explanation:** Starting at (1,3) 'S', we can form: S → E → E

### Example 3:

**Input:**
```
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"
```
**Output:** `false`
**Explanation:** Cannot form "ABCB" because we can't reuse the cell at (0,1) 'B'.

### Example 4:

**Input:**
```
board = [["A"]]
word = "A"
```
**Output:** `true`
**Explanation:** Single cell matches single letter word.

## Constraints

- m == board.length
- n = board[i].length
- 1 ≤ m, n ≤ 6
- 1 ≤ word.length ≤ 15
- board and word consists of only lowercase and uppercase English letters

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Bloomberg
- Facebook
- Google
- Apple

## Hints

1. Try starting the search from each cell in the grid
2. Use DFS to explore all 4 directions (up, down, left, right)
3. Mark cells as visited (modify in place or use a visited set)
4. Don't forget to unmark cells when backtracking
5. Base cases: found all letters (return true), out of bounds, or wrong letter (return false)
6. Optimization: check if the board has all required letters before starting

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
