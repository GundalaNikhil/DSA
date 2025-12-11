---
unique_problem_id: gametheory_015
display_id: GAMETHEORY-015
slug: turning-turtles
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Sprague-Grundy
  - Flip Game
  - Prefix Operations
  - XOR
---

# Turning Turtles

## Problem Description

Array of turtles facing L/R. Move: choose a position i, flip all turtles from i to end (reverse direction). Player with all turtles facing R loses. Determine winner.

## Examples

- Example 1:
  - Input: "LR"
  - Output: `First`
  - Explanation: Flip from position 0: "LR" → "RL". Flip from 1: "RL"→"RR". First player can force second to "RR" state.

- Example 2:
  - Input: "RR"
  - Output: `Second`
  - Explanation: All R already. First player just took turn making all R, so first loses (or game already over).

- Example 3:
  - Input: "LLL"
  - Output: `First`
  - Explanation: Multiple moves possible. Analyze with Grundy.

## Constraints

- n <= 2000

## Function Signatures

### Java
```java
class Solution {
    public String turningTurtles(String s) {
        // Implementation here
    }
}
```

### Python
```python
def turning_turtles(s: str) -> str:
    """
    Determine winner of turning turtles game.
    
    Args:
        s: String of L/R directions
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string turningTurtles(string s) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single line: string of L and R characters

### Sample Input
```
LR
```

## Hints

Represent state as binary (L=1, R=0). Flipping suffix from i is like XORing with a mask. Use Sprague-Grundy with prefix parity or state encoding.

## Quiz

### Question 1
What is the losing condition?

A) All turtles facing L  
B) All turtles facing R after your move  
C) No moves available  
D) First turtle faces L

**Correct Answer:** B

**Explanation:** Player who makes all turtles face R loses (or equivalently, reaches the terminal "all R" state).

### Question 2
How does flipping work?

A) Flip one turtle  
B) Flip all turtles from position i to end  
C) Flip random turtles  
D) Flip first and last

**Correct Answer:** B

**Explanation:** Choosing position i flips all turtles from i to n-1 (inclusive).

### Question 3
Is "RRRR" a losing position for the player to move?

A) Yes, already all R  
B) No, game continues  
C) It's a draw  
D) Depends on who moved last

**Correct Answer:** A

**Explanation:** If it's your turn and all are already R, you made the last move to reach this (or it was already there), meaning you lose / previous player won.

### Question 4
Why is prefix parity relevant?

A) It's not  
B) Flip operations affect suffix, creating patterns based on prefix  
C) For counting moves  
D) To optimize space

**Correct Answer:** B

**Explanation:** The game state can be encoded by parity of L's, and flip operations have structured effects analyzable via parity.
