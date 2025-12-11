---
unique_problem_id: gametheory_004
display_id: GAMETHEORY-004
slug: circular-nim-variant
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Sprague-Grundy
  - Nim Variant
  - Circular Structure
  - State Space Search
---

# Circular Nim Variant

## Problem Description

Stones in a circle of piles. A move: pick a pile with >0 stones, remove any positive number, and also must add 1 stone to each adjacent pile (if present). Player unable to move loses. Determine winner for small n via Grundy up to `n<=20` and pile sizes <= 15.

## Examples

- Example 1:
  - Input: piles = [1, 0, 1]
  - Output: `First`
  - Explanation: First player can remove 1 from pile 0, adding 1 to piles 1 and 2. State becomes [0,1,2]. Analysis continues with Grundy.

- Example 2:
  - Input: piles = [0, 0, 0]
  - Output: `Second`
  - Explanation: No stones to remove. First player cannot move and loses.

- Example 3:
  - Input: piles = [2, 0]
  - Output: `First`
  - Explanation: Two piles in circle. Remove 2 from pile 0, add 1 to pile 1. State [0,1]. Now pile 1 has 1, remove it adding to pile 0. Continues until a player can't move.

## Constraints

- n <= 20
- pile[i] <= 15

## Function Signatures

### Java
```java
class Solution {
    public String circularNimVariant(int[] piles) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def circular_nim_variant(piles: List[int]) -> str:
    """
    Determine winner of circular Nim variant.
    
    Args:
        piles: Array of pile sizes arranged in a circle
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string circularNimVariant(vector<int>& piles) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (number of piles)
- Second line: n space-separated pile sizes

### Sample Input
```
3
1 0 1
```

## Hints

Due to small constraints (n<=20, pile<=15), state space is bounded. Use memoization with state encoding. Compute Grundy values via DFS with mex over reachable states.

## Quiz

### Question 1
Why does removing stones also add to neighbors?

A) To make the game harder  
B) It's a variant rule that creates interesting game dynamics  
C) To prevent the game from ending  
D) It's a bug in the problem

**Correct Answer:** B

**Explanation:** This variant rule creates complex interactions where reducing one pile affects adjacent piles, making Grundy analysis non-trivial.

### Question 2
What makes circular structure special?

A) Every pile has exactly 2 neighbors  
B) The first and last piles are adjacent  
C) Both A and B  
D) It has no effect

**Correct Answer:** C

**Explanation:** In a circular arrangement, pile[0] is adjacent to pile[n-1], and every pile has exactly 2 neighbors (except when n=1).

### Question 3
What is the state space size upper bound?

A) O(n)  
B) O(16^n)  
C) O(n!)  
D) O(2^n)

**Correct Answer:** B

**Explanation:** Each of n piles can have 0-15 stones, giving up to 16^n states. For n=20, this is large but manageable with memoization and pruning.

### Question 4
When is a state losing?

A) When total stones is 0  
B) When Grundy value is 0  
C) When no valid moves exist  
D) Both B and C (they're equivalent)

**Correct Answer:** D

**Explanation:** A position with no valid moves has Grundy value 0 by definition (mex of empty set). Both conditions indicate a losing position.
