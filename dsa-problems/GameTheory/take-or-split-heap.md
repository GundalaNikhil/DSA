---
unique_problem_id: gametheory_009
display_id: GAMETHEORY-009
slug: take-or-split-heap
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Sprague-Grundy
  - Nim Variant
  - Dynamic Programming
  - Heap Splitting
---

# Take-or-Split Heap

## Problem Description

Single heap size `n`. Move: either take 1 stone, or split heap into two heaps of equal size (only if even). Player who takes last stone wins. Determine winner.

## Examples

- Example 1:
  - Input: n = 2
  - Output: `First`
  - Explanation: Split 2 into (1,1), or take 1 leaving 1. Either way, first player can win.

- Example 2:
  - Input: n = 1
  - Output: `First`
  - Explanation: Take the last stone. First player wins.

- Example 3:
  - Input: n = 4
  - Output: `First`
  - Explanation: Options: take 1 (leave 3), or split into (2,2). Analyze with Grundy values.

## Constraints

- `1 <= n <= 10^6`

## Function Signatures

### Java
```java
class Solution {
    public String takeOrSplitHeap(int n) {
        // Implementation here
    }
}
```

### Python
```python
def take_or_split_heap(n: int) -> str:
    """
    Determine winner of take-or-split heap game.
    
    Args:
        n: Initial heap size
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string takeOrSplitHeap(int n) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single integer n

### Sample Input
```
2
```

## Hints

Compute Grundy values. Split creates TWO heaps, so Grundy(split) = Grundy(n/2) XOR Grundy(n/2) = 0. So splitting is only useful to create a Grundy 0 state. Pattern: often depends on parity or power-of-2 structure.

## Quiz

### Question 1
What happens when you split an even heap?

A) Creates two independent heaps of size n/2  
B) Creates one heap of size n/2  
C) Removes all stones  
D) No effect

**Correct Answer:** A

**Explanation:** Splitting creates two heaps of equal size, which become independent games.

### Question 2
What is the Grundy value of two identical heaps?

A) 0 (XOR of same values)  
B) 2 times the Grundy value  
C) Sum of Grundy values  
D) Maximum of Grundy values

**Correct Answer:** A

**Explanation:** Grundy(a,a) = Grundy(a) XOR Grundy(a) = 0 for any value.

### Question 3
When is splitting strategically useful?

A) When it creates a losing position  
B) When current Grundy is already 0  
C) Never  
D) Always

**Correct Answer:** A

**Explanation:** Splitting gives Grundy 0 (if both halves are identical). It's useful when combined with other moves to reach a losing state for opponent.

### Question 4
For this game, n=1 is:

A) Losing  
B) Winning  
C) Draw  
D) Undefined

**Correct Answer:** B

**Explanation:** Taking the last stone wins. From n=1, first player takes and wins.
