# Grid Paths With Turn Limit

## Problem Metadata
- **unique_problem_id**: `dp_008`
- **display_id**: `DP-008`
- **slug**: `grid-paths-turn-limit`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Grid", "Combinatorics", "Path Counting"]`

## Problem Title
Grid Paths With Turn Limit

## Problem Description
Count the number of distinct paths from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1) of an `m × n` grid. You can only move right or down at each step.

The constraint is that you can make at most `T` turns (direction changes). A turn occurs when you switch from moving right to moving down, or vice versa.

Return the count of valid paths modulo 10^9 + 7.

## Examples

### Example 1
**Input:**
```
m = 2
n = 3
T = 1
```

**Output:**
```
2
```

**Explanation:**
- Path 1: Right → Right → Down (RRD): 1 turn (R to D)
- Path 2: Down → Right → Right (DRR): 1 turn (D to R)
- Path RDR would need 2 turns (R→D, D→R), exceeding limit
- Total: 2 paths with at most 1 turn

### Example 2
**Input:**
```
m = 3
n = 3
T = 2
```

**Output:**
```
6
```

**Explanation:** Various paths with at most 2 turns:
- RRDD: 1 turn
- RDRD: 3 turns (exceeds limit)
- RDDR: 2 turns ✓
- DRRD: 2 turns ✓
- DRDR: 3 turns (exceeds limit)
- DDRR: 1 turn ✓
- And more combinations with ≤ 2 turns

### Example 3
**Input:**
```
m = 1
n = 5
T = 0
```

**Output:**
```
1
```

**Explanation:** Only one path: RRRR (all right moves, no turns).

## Constraints
- `1 <= m, n <= 100`
- `0 <= T <= 50`
- Answer should be returned modulo 10^9 + 7

## Function Signatures

### Java
```java
class Solution {
    public int countPathsWithTurnLimit(int m, int n, int T) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def countPathsWithTurnLimit(self, m: int, n: int, T: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int countPathsWithTurnLimit(int m, int n, int T) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Three space-separated integers: m (rows), n (columns), T (max turns)
```

### Sample Input
```
2 3 1
```

## Hints
- Use 3D DP: dp[i][j][dir][turns] where:
  - (i, j) is current position
  - dir is last direction taken (0 = right, 1 = down)
  - turns is number of turns made so far
- Alternative state: dp[i][j][turns][lastDir]
- Base cases: Start position (0,0) with 0 turns, both directions possible
- Transition:
  - Moving in same direction: no turn added
  - Changing direction: increment turn count
- Sum all valid end states at (m-1, n-1) with turns ≤ T
- Remember to use modulo 10^9 + 7

## Related Topics Quiz

### Question 1
What is the time complexity of the DP solution?
- A) O(m × n)
- B) O(m × n × T)
- C) O(m × n × T × 2)
- D) O(m + n + T)

**Answer:** C) O(m × n × T × 2) - We have 4 dimensions: position (m×n), turns (T), and direction (2).

### Question 2
What constitutes a "turn" in this problem?
- A) Any move in the grid
- B) Moving diagonally
- C) Changing direction from right to down or vice versa
- D) Reaching a corner

**Answer:** C) Changing direction from right to down or vice versa - A turn is a direction change.

### Question 3
If T = 0, what is the answer?
- A) 0
- B) 1
- C) m + n
- D) m × n

**Answer:** B) 1 - Only one path possible: all moves in one direction first, then all in the other (but that's 1 turn!). Actually, T=0 means NO turns, so you go all right then... wait, you need both rights and downs to reach (m-1,n-1). If m=1, you go all right (0 turns). If n=1, you go all down (0 turns). Otherwise, you need at least 1 turn. So answer depends on whether m=1 or n=1.

**Corrected Answer:** B) 1 if m=1 or n=1, else 0 - No turns means all moves in one direction only.

### Question 4
What is the maximum number of turns possible in any path?
- A) m + n
- B) m + n - 1
- C) m + n - 2
- D) min(m, n)

**Answer:** C) m + n - 2 - Alternating directions: RDRDRD... gives maximum turns.

### Question 5
Why do we need to track the last direction in our DP state?
- A) To calculate distance
- B) To determine if the next move creates a turn
- C) To avoid revisiting cells
- D) For output formatting

**Answer:** B) To determine if the next move creates a turn - We need to know if we're changing direction.
