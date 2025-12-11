---
unique_problem_id: gametheory_013
display_id: GAMETHEORY-013
slug: bimatrix-zero-sum-variant
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Zero-Sum Game
  - Linear Programming
  - Mixed Strategy
  - Nash Equilibrium
---

# Bimatrix Zero-Sum Variant

## Problem Description

Two players choose actions A_i and B_j with payoff matrix P (can be asymmetric). Find the value of the zero-sum game using linear programming or simplex; for small n,m brute force mixed strategies.

## Examples

- Example 1:
  - Input: P = [[1,-1],[-2,2]]
  - Output: Game value = 0
  - Explanation: Minimax analysis shows balanced strategies leading to value 0.

- Example 2:
  - Input: P = [[3,0,2],[1,2,1]]
  - Output: Game value computed via LP

- Example 3:
  - Input: P = [[1]] (1x1)
  - Output: Game value = 1
  - Explanation: Only one action each. Value is the single entry.

## Constraints

- n, m <= 50

## Function Signatures

### Java
```java
class Solution {
    public double bimatrixZeroSumVariant(int[][] P) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def bimatrix_zero_sum_variant(P: List[List[int]]) -> float:
    """
    Compute the value of a zero-sum game.
    
    Args:
        P: Payoff matrix for row player
    
    Returns:
        Game value (expected payoff under optimal mixed strategies)
    """
    pass
```

### C++
```cpp
class Solution {
public:
    double bimatrixZeroSumVariant(vector<vector<int>>& P) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n m (matrix dimensions)
- Next n lines: m integers (payoff values)

### Sample Input
```
2 2
1 -1
-2 2
```

## Hints

For zero-sum games, solve the LP: max v subject to sum(p_j * A_ij) >= v for all j, sum(p_j)=1, p_j>=0. Column player's strategy is the dual.

## Quiz

### Question 1
What is the minimax theorem guarantee?

A) There's always a pure strategy solution  
B) max_row min_col = min_col max_row for mixed strategies  
C) Games always end in draw  
D) Randomness is unnecessary

**Correct Answer:** B

**Explanation:** Von Neumann's minimax theorem: in zero-sum games, optimal mixed strategies achieve maximin = minimax, defining the game value.

### Question 2
What is a mixed strategy?

A) Playing randomly without thought  
B) Probability distribution over pure strategies  
C) Using multiple payoff matrices  
D) Alternating strategies

**Correct Answer:** B

**Explanation:** A mixed strategy assigns probabilities to pure strategies, randomizing over actions.

### Question 3
Why use Linear Programming?

A) It's the only way  
B) Finding optimal mixed strategies reduces to LP  
C) LP is always fast  
D) Required by problem

**Correct Answer:** B

**Explanation:** Optimal mixed strategy for row player can be found by LP maximizing game value subject to constraints for each column action.

### Question 4
For a 2x2 matrix, can we solve without LP?

A) No  
B) Yes, closed-form formulas exist  
C) Sometimes  
D) Only for symmetric matrices

**Correct Answer:** B

**Explanation:** 2x2 zero-sum games have closed-form solutions using saddle point analysis or simple algebra.
