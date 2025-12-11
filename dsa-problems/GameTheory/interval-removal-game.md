---
unique_problem_id: gametheory_005
display_id: GAMETHEORY-005
slug: interval-removal-game
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Nim
  - XOR Sum
  - Interval Game
  - Sprague-Grundy
---

# Interval Removal Game

## Problem Description

Given disjoint intervals on a line. A move: choose an interval and remove any positive length sub-interval from it; remaining pieces stay. Player unable to move loses. For each interval, Grundy = length (as positions), game Nim-sum decides winner.

## Examples

- Example 1:
  - Input: intervals = [[0,2], [5,6]]
  - Output: `First`
  - Explanation: Interval lengths are 2 and 1. XOR = 2 ⊕ 1 = 3 ≠ 0. First player wins.

- Example 2:
  - Input: intervals = [[0,3], [5,8]]
  - Output: `Second`
  - Explanation: Lengths are 3 and 3. XOR = 3 ⊕ 3 = 0. Second player wins.

- Example 3:
  - Input: intervals = [[0,5]]
  - Output: `First`
  - Explanation: Single interval of length 5. XOR = 5 ≠ 0. First player wins.

## Constraints

- Up to 10^5 intervals
- Lengths <= 10^9

## Function Signatures

### Java
```java
class Solution {
    public String intervalRemovalGame(int[][] intervals) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def interval_removal_game(intervals: List[List[int]]) -> str:
    """
    Determine winner of interval removal game.
    
    Args:
        intervals: List of [start, end] intervals
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string intervalRemovalGame(vector<vector<int>>& intervals) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (number of intervals)
- Next n lines: start end (interval endpoints)

### Sample Input
```
2
0 2
5 6
```

## Hints

This is essentially multi-pile Nim. Each interval acts as a Nim pile with size = length. XOR all lengths; non-zero XOR means first player wins.

## Quiz

### Question 1
Why does Nim-sum (XOR) determine the winner?

A) XOR is fast to compute  
B) Sprague-Grundy theorem: XOR of Grundy values determines game outcome  
C) It's a coincidence  
D) XOR represents total stones

**Correct Answer:** B

**Explanation:** By Sprague-Grundy, independent games combine via XOR of their Grundy values. XOR ≠ 0 means winning; XOR = 0 means losing.

### Question 2
What is the Grundy number of an interval of length L?

A) 0  
B) 1  
C) L  
D) 2^L

**Correct Answer:** C

**Explanation:** An interval behaves like a Nim pile. Removing a sub-interval effectively reduces the total length, similar to removing stones from a pile.

### Question 3
What happens when an interval is split?

A) Game ends  
B) It becomes two separate intervals/games  
C) Player loses immediately  
D) The split is not allowed

**Correct Answer:** B

**Explanation:** Removing a middle portion splits the interval into two. These become independent games whose Grundy values XOR together.

### Question 4
Time complexity to determine winner?

A) O(n) where n is number of intervals  
B) O(n log n)  
C) O(n²)  
D) O(max length)

**Correct Answer:** A

**Explanation:** Just compute the XOR of all interval lengths - one pass through the intervals.
