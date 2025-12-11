---
unique_problem_id: gametheory_012
display_id: GAMETHEORY-012
slug: rectangular-chocolate-cut
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Sprague-Grundy
  - 2D State Space
  - Memoization
  - Grid Game
---

# Rectangular Chocolate Cut

## Problem Description

Rect chocolate bar w x h. Move: cut along grid line into two rectangles; remove one of the resulting pieces of area <= K. Player unable to move loses.

## Examples

- Example 1:
  - Input: w=2, h=2, K=2
  - Output: `First`
  - Explanation: Cut 2x2 into two 1x2 pieces. Each has area 2 <= K. Remove one, leaving 1x2.

- Example 2:
  - Input: w=1, h=1, K=0
  - Output: `Second`
  - Explanation: Cannot cut 1x1. Cannot remove piece of area <= 0. No moves.

- Example 3:
  - Input: w=3, h=1, K=1
  - Output: `First`
  - Explanation: Cut into 1x1 and 2x1. Remove 1x1 (area 1 <= K). Continue with 2x1.

## Constraints

- w, h <= 30
- K <= 20

## Function Signatures

### Java
```java
class Solution {
    public String rectangularChocolateCut(int w, int h, int K) {
        // Implementation here
    }
}
```

### Python
```python
def rectangular_chocolate_cut(w: int, h: int, K: int) -> str:
    """
    Determine winner of chocolate cutting game.
    
    Args:
        w: Width of chocolate
        h: Height of chocolate
        K: Maximum area that can be removed
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string rectangularChocolateCut(int w, int h, int K) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single line: w h K

### Sample Input
```
2 2 2
```

## Hints

States are rectangles (w,h). Cut horizontally or vertically; one piece must have area <= K to be removed. Use memoization on (w,h) states. Symmetric: (w,h) ≡ (h,w).

## Quiz

### Question 1
When can a cut be made?

A) Anytime  
B) Only if one resulting piece has area <= K  
C) Only if both pieces have area <= K  
D) Only if total area > K

**Correct Answer:** B

**Explanation:** A valid move requires cutting AND removing one piece. The removed piece must have area <= K.

### Question 2
How many states are there?

A) O(w + h)  
B) O(w * h)  
C) O(w * h * K)  
D) O(2^(w*h))

**Correct Answer:** B

**Explanation:** States are just rectangle dimensions (w,h). With symmetry, effectively O(w*h/2) but O(w*h) without.

### Question 3
A 1x1 chocolate with K=1:

A) First wins by removing it  
B) Cannot cut, but can remove entire piece? Depends on rules  
C) Second wins (no cut possible)  
D) Draw

**Correct Answer:** C

**Explanation:** Cannot cut a 1x1. If we interpret "cut then remove" strictly, no valid move exists.

### Question 4
How does K affect complexity?

A) Larger K means more valid moves, potentially faster winning  
B) Larger K means fewer valid moves  
C) K doesn't affect complexity  
D) K exponentially increases states

**Correct Answer:** A

**Explanation:** Larger K allows removing bigger pieces, creating more options per state. But state count stays O(w*h).
