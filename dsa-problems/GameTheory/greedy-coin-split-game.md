---
unique_problem_id: gametheory_014
display_id: GAMETHEORY-014
slug: greedy-coin-split-game
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Interval DP
  - Competitive Game
  - Prefix/Suffix
  - Minimax
---

# Greedy Coin Split Game

## Problem Description

Coins in a line with values v[i]. On your turn, choose a prefix or suffix and remove it, gaining sum of removed coins. Opponent then moves on remaining line. Maximize your total vs optimal opponent; compute optimal first-player total.

## Examples

- Example 1:
  - Input: v = [1, 2, 3]
  - Output: 4
  - Explanation: Take suffix [3] (gain 3). Opponent takes [2] (gains 2). Take [1] (gain 1). Total: 3+1=4.

- Example 2:
  - Input: v = [5, 1, 5]
  - Output: 6
  - Explanation: Take prefix [5] or suffix [5]. Opponent gets remaining 1+5 or 5+1=6. Actually better: think of both sides.

- Example 3:
  - Input: v = [10]
  - Output: 10
  - Explanation: Take the only coin.

## Constraints

- `1 <= n <= 2000`

## Function Signatures

### Java
```java
class Solution {
    public int greedyCoinSplitGame(int[] v) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def greedy_coin_split_game(v: List[int]) -> int:
    """
    Compute optimal first-player score in coin split game.
    
    Args:
        v: Array of coin values
    
    Returns:
        Maximum score first player can achieve
    """
    pass
```

### C++
```cpp
class Solution {
public:
    int greedyCoinSplitGame(vector<int>& v) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n
- Second line: n coin values

### Sample Input
```
3
1 2 3
```

## Hints

Use interval DP: dp[i][j] = best score for player-to-move on subarray [i,j]. Try all prefix/suffix removals. Note: this is NOT impartial (different payoffs per player).

## Quiz

### Question 1
Why is this different from standard game theory?

A) It's not a game  
B) Players have different objectives (maximize own score)  
C) It's impartial  
D) No difference

**Correct Answer:** B

**Explanation:** This is a non-impartial competitive game where both players want to maximize their own score, not Sprague-Grundy style.

### Question 2
What is the recurrence structure?

A) dp[i][j] = max over prefixes/suffixes of (removed sum) + remainder after opponent plays  
B) Simple addition  
C) Minimum of all moves  
D) XOR of subproblems

**Correct Answer:** A

**Explanation:** For interval [i,j], try removing each prefix [i,k] or suffix [k,j]. After removal, opponent plays optimally on remaining, and we get total - opponent's score.

### Question 3
Time complexity of DP solution?

A) O(n)  
B) O(n²)  
C) O(n³)  
D) O(2^n)

**Correct Answer:** C

**Explanation:** O(n²) subproblems, each considering O(n) possible prefix/suffix removals.

### Question 4
Is greedy (always take largest end) optimal?

A) Yes  
B) No, DP is needed  
C) Sometimes  
D) For odd n only

**Correct Answer:** B

**Explanation:** Greedy fails because removing the largest immediate piece may leave a better position for opponent.
