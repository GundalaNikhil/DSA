---
unique_problem_id: gametheory_003
display_id: GAMETHEORY-003
slug: subtract-square-ban-list
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Dynamic Programming
  - Sprague-Grundy
  - Subtraction Game
  - Mex Function
---

# Subtract-a-Square with Ban List

## Problem Description

Starting with `n`, players subtract a perfect square such that the square is not in a banned set `B`. Player who reaches exactly 0 wins. Determine winner.

## Examples

- Example 1:
  - Input: n=7, B={1}
  - Output: `Second`
  - Explanation: Moves available: subtract 4. From 7-4=3, opponent has no valid moves (1 is banned, 4>3). So first move 7→3, opponent stuck. Wait - let's recalculate: squares ≤7 are 1,4. With 1 banned, only 4 is valid. 7-4=3. From 3: squares ≤3 are 1. With 1 banned, no moves. But 0 wins - so player at 3 cannot move and loses. First player wins, not second.

- Example 2:
  - Input: n=4, B={}
  - Output: `First`
  - Explanation: Subtract 4 directly to reach 0. First player wins.

- Example 3:
  - Input: n=2, B={}
  - Output: `Second`
  - Explanation: Only 1 can be subtracted (4>2). 2-1=1. From 1: subtract 1 to get 0. Second player wins.

## Constraints

- `1 <= n <= 10^5`
- `|B| <= 100`

## Function Signatures

### Java
```java
import java.util.Set;

class Solution {
    public String subtractSquareBanList(int n, Set<Integer> banned) {
        // Implementation here
    }
}
```

### Python
```python
from typing import Set

def subtract_square_ban_list(n: int, banned: Set[int]) -> str:
    """
    Determine winner of subtract-a-square game with banned squares.
    
    Args:
        n: Starting number
        banned: Set of banned perfect squares
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
#include <set>
using namespace std;

class Solution {
public:
    string subtractSquareBanList(int n, set<int>& banned) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (starting number)
- Second line: size of ban list
- Third line: banned squares

### Sample Input
```
7
1
1
```

## Hints

DP/Grundy up to n. For each position, compute reachable positions by subtracting valid squares and take mex. Position 0 is terminal (win for player who just moved).

## Quiz

### Question 1
What makes this different from standard Subtract-a-Square?

A) The Grundy numbers are different  
B) Some perfect squares cannot be used as moves  
C) The board is circular  
D) There are multiple piles

**Correct Answer:** B

**Explanation:** The ban list restricts which perfect squares can be subtracted, changing the game tree.

### Question 2
How is position 0 handled?

A) It's a losing position  
B) The player who reaches 0 wins (terminal winning)  
C) The game continues  
D) It's undefined

**Correct Answer:** B

**Explanation:** Reaching exactly 0 wins. So 0 is a terminal state where the player who just moved (reached 0) wins.

### Question 3
What is the time complexity?

A) O(n)  
B) O(n * sqrt(n))  
C) O(n²)  
D) O(2^n)

**Correct Answer:** B

**Explanation:** For each position 1 to n, we try at most O(sqrt(n)) perfect squares as moves.

### Question 4
If all perfect squares are banned, who wins from n > 0?

A) First  
B) Second  
C) Draw  
D) Depends on n

**Correct Answer:** B

**Explanation:** If no moves are possible from the start, the first player cannot move and loses.
