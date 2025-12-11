---
unique_problem_id: gametheory_007
display_id: GAMETHEORY-007
slug: grid-chomp-poison
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Chomp
  - Sprague-Grundy
  - Grid Game
  - Memoization
---

# Grid Chomp with Poisoned Cells

## Problem Description

m x n grid; some cells are walls, one cell is poisoned. A move: pick any edible cell (not wall, not poison) and remove it plus all cells with row>=i and col>=j. If a player is forced to take the poisoned cell, they lose immediately. Determine winner for grids up to 10x10 via Grundy.

## Examples

- Example 1:
  - Input: 2x2 grid, poison at (1,1)
  - Output: `First`
  - Explanation: First player can take (0,0), removing all cells but poison. Second player forced to take poison and loses.

- Example 2:
  - Input: 2x2 grid, poison at (0,0)
  - Output: `Second`
  - Explanation: Any cell first player takes will remove poison. First player takes poison and loses.

- Example 3:
  - Input: 3x3 grid, poison at (2,2), no walls
  - Output: `First`
  - Explanation: First player has winning strategy to force opponent to take poison.

## Constraints

- m, n <= 10

## Function Signatures

### Java
```java
class Solution {
    public String gridChompPoison(int m, int n, int[] poison, int[][] walls) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def grid_chomp_poison(m: int, n: int, poison: Tuple[int, int], walls: List[Tuple[int, int]]) -> str:
    """
    Determine winner of Chomp game with poison cell.
    
    Args:
        m: Grid rows
        n: Grid columns
        poison: (row, col) of poisoned cell
        walls: List of (row, col) wall positions
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string gridChompPoison(int m, int n, vector<int>& poison, vector<vector<int>>& walls) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: m n (grid dimensions)
- Second line: poison row col
- Third line: number of walls
- Following lines: wall positions

### Sample Input
```
2 2
1 1
0
```

## Hints

Classic Chomp: poison at (0,0) makes first player lose (strategy stealing argument). With poison elsewhere, compute Grundy via DFS with memoization over grid states.

## Quiz

### Question 1
What is the classic Chomp result for poison at (0,0)?

A) First player wins  
B) First player loses (Second wins)  
C) Draw  
D) Random outcome

**Correct Answer:** B

**Explanation:** By strategy stealing: if Second had a winning response to any First move, First could just make that move first. But First must make some move, and any move from full grid is losing.

### Question 2
How does removing a cell affect the grid?

A) Only that cell is removed  
B) All cells with row >= r and col >= c are removed (inclusive)  
C) Random cells are removed  
D) Adjacent cells are removed

**Correct Answer:** B

**Explanation:** Chomp rule: taking cell (r,c) removes the entire "down-right" rectangle, similar to breaking off a corner of a chocolate bar.

### Question 3
Why is state space manageable for small grids?

A) There are few states  
B) Grid states can be encoded efficiently; 10x10 with binary has 2^100 but valid Chomp states are much fewer  
C) Memoization reuses computations  
D) Both B and C

**Correct Answer:** D

**Explanation:** Valid Chomp states (monotonic staircase patterns) are far fewer than arbitrary grids, and memoization avoids recomputation.

### Question 4
What role do walls play?

A) They're always removed first  
B) They cannot be selected and block movement  
C) They act as additional poison  
D) They have no effect

**Correct Answer:** B

**Explanation:** Wall cells cannot be chosen as a move and aren't removed by other moves, potentially blocking certain strategies.
