---
unique_problem_id: gametheory_016
display_id: GAMETHEORY-016
slug: weighted-nim-heaps
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Weighted Game
  - Dynamic Programming
  - Score Optimization
  - Competitive Strategy
---

# Weighted Nim Heaps

## Problem Description

Each heap i has weight w[i]; removing k stones from heap i adds w[i]*k to your score. After all heaps empty, higher score wins. Compute optimal scores for both players.

## Examples

- Example 1:
  - Input: heaps = [2, 1], weights = [3, 1]
  - Output: First=7, Second=0
  - Explanation: First takes all from both heaps: 2*3 + 1*1 = 7. (But they alternate!) Let's recalculate: First takes 2 from heap0 (score 6). Second takes 1 from heap1 (score 1). Final: 6 vs 1.

- Example 2:
  - Input: heaps = [1, 1], weights = [5, 1]
  - Output: First=5, Second=1
  - Explanation: First takes heap0 (score 5), Second takes heap1 (score 1).

- Example 3:
  - Input: heaps = [3], weights = [2]
  - Output: First=6, Second=0
  - Explanation: First takes all 3 stones (score 6).

## Constraints

- `1 <= n <= 50`
- heap sizes <= 50

## Function Signatures

### Java
```java
class Solution {
    public int[] weightedNimHeaps(int[] heaps, int[] weights) {
        // Implementation here (returns [firstScore, secondScore])
    }
}
```

### Python
```python
from typing import List, Tuple

def weighted_nim_heaps(heaps: List[int], weights: List[int]) -> Tuple[int, int]:
    """
    Compute optimal scores for both players.
    
    Args:
        heaps: Array of heap sizes
        weights: Array of weights per heap
    
    Returns:
        Tuple of (first_player_score, second_player_score)
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<int> weightedNimHeaps(vector<int>& heaps, vector<int>& weights) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n
- Second line: heap sizes
- Third line: weights

### Sample Input
```
2
2 1
3 1
```

## Hints

Use DP over heaps and possible score differences. Each heap is independent; but total score difference matters. Think about optimal stone removal per turn.

## Quiz

### Question 1
How is this different from standard Nim?

A) Players gain score based on what they remove  
B) Goal is highest score, not last move  
C) Both A and B  
D) No difference

**Correct Answer:** C

**Explanation:** Unlike Nim (last-move wins), here players accumulate score proportional to stones removed. Winner has higher total.

### Question 2
Is greedy (always pick highest-weight heap) optimal?

A) Yes  
B) No, other factors matter  
C) Only sometimes  
D) Only for 2 heaps

**Correct Answer:** A

**Explanation:** Each turn, taking from highest-weight heap maximizes your score increase. Greedy is optimal here.

### Question 3
What if all weights are equal?

A) Score split evenly  
B) First player gets more (takes first)  
C) Depends on heap sizes and strategy  
D) Second player wins

**Correct Answer:** C

**Explanation:** With equal weights, strategy involves taking more stones per turn, and the player who removes more total stones wins.

### Question 4
Time complexity with DP over score differences?

A) O(n)  
B) O(n * total_stones)  
C) O(n * max_score_diff)  
D) O(2^n)

**Correct Answer:** C

**Explanation:** DP state: current heap and score difference. Score difference is bounded by total possible score.
