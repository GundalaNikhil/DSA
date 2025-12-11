---
unique_problem_id: gametheory_001
display_id: GAMETHEORY-001
slug: pile-split-choice
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Sprague-Grundy
  - Nim Variant
  - Combinatorial Game
  - Mex Function
---

# Pile Split Choice

## Problem Description

A pile of `n` stones; on each turn a player may split one pile into two non-empty piles of different sizes. Player who cannot move loses. Determine the winner with optimal play for given `n`.

## Examples

- Example 1:
  - Input: `n = 3`
  - Output: `First`
  - Explanation: Split 3 into (1,2). Opponent cannot split 1 or 2 into different-sized piles. First player wins.

- Example 2:
  - Input: `n = 4`
  - Output: `First`
  - Explanation: Split 4 into (1,3). Opponent has moves from pile of 3. Continue analysis with Grundy values.

- Example 3:
  - Input: `n = 2`
  - Output: `Second`
  - Explanation: Cannot split 2 into two different-sized non-empty piles (only 1+1, which is same size). First player cannot move.

## Constraints

- `1 <= n <= 10^5`

## Function Signatures

### Java
```java
class Solution {
    public String pileSplitChoice(int n) {
        // Implementation here
    }
}
```

### Python
```python
def pile_split_choice(n: int) -> str:
    """
    Determine winner of pile split game.
    
    Args:
        n: Initial pile size
    
    Returns:
        "First" or "Second" indicating winner with optimal play
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string pileSplitChoice(int n) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single integer n (initial pile size)

### Sample Input
```
3
```

## Hints

Compute Grundy values for small n using mex of splits. Note the pattern: a pile can only be split if n >= 3 and into piles of different sizes (a, n-a) where a != n-a.

## Quiz

### Question 1
What does the mex function compute in Sprague-Grundy theory?

A) Maximum value  
B) Minimum excludant (smallest non-negative integer not in the set)  
C) Average value  
D) Median value

**Correct Answer:** B

**Explanation:** Mex (minimum excludant) returns the smallest non-negative integer not present in the set of reachable Grundy values.

### Question 2
When is a position losing in this game?

A) When Grundy value is 0  
B) When Grundy value is positive  
C) When pile size is odd  
D) When pile size is even

**Correct Answer:** A

**Explanation:** A Grundy value of 0 means the current player loses with optimal play. Any non-zero Grundy value means the current player can win.

### Question 3
What are the valid splits for n = 5?

A) (1,4), (2,3)  
B) (1,4), (2,3), (5,0)  
C) Only (2,3)  
D) (1,1,3)

**Correct Answer:** A

**Explanation:** Valid splits must be into exactly two non-empty piles of different sizes. (1,4) and (2,3) are the only valid options for n=5.

### Question 4
What is the time complexity of precomputing Grundy values up to n?

A) O(n)  
B) O(n²)  
C) O(n log n)  
D) O(2^n)

**Correct Answer:** B

**Explanation:** For each value 1 to n, we may need to consider O(n) possible splits to compute the mex.
