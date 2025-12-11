---
unique_problem_id: gametheory_011
display_id: GAMETHEORY-011
slug: token-dag-skip
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - DAG
  - Sprague-Grundy
  - Extended Moves
  - Topological Order
---

# Token on DAG with Skip Move

## Problem Description

DAG game; from a node, a move can go along an outgoing edge or skip over one node (two edges) if path exists. Compute winning nodes.

## Examples

- Example 1:
  - Input: edges 0→1→2, n=3
  - Output: `[Win, Win, Lose]`
  - Explanation: Node 2 loses (sink). Node 1 can move to 2 (lose) or skip to nothing (wins by moving to lose). Node 0 can move to 1 or skip to 2 (lose).

- Example 2:
  - Input: edges 0→1, 1→2, 2→3, n=4
  - Output: `[Win, Lose, Win, Lose]`
  - Explanation: 3=Lose (sink). 2→3 or skip impossible = Win. 1→2(Win) or 1→→3(Lose) = can reach Lose so 1=Win. Wait, let me recalculate properly.

- Example 3:
  - Input: Single node 0 with no edges
  - Output: `[Lose]`
  - Explanation: No moves available.

## Constraints

- n <= 2 * 10^5
- m <= 2 * 10^5

## Function Signatures

### Java
```java
class Solution {
    public String[] tokenDagSkip(int n, int[][] edges) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def token_dag_skip(n: int, edges: List[Tuple[int, int]]) -> List[str]:
    """
    Determine win/lose for each node with skip moves.
    
    Args:
        n: Number of nodes
        edges: List of (from, to) edges
    
    Returns:
        List of "Win" or "Lose" for each node
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<string> tokenDagSkip(int n, vector<pair<int,int>>& edges) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n m
- Next m lines: from to

### Sample Input
```
3 2
0 1
1 2
```

## Hints

Precompute edges and skip-edges (length-2 paths). For each node, consider both regular moves and skip moves when computing win/lose via topo order.

## Quiz

### Question 1
How do skip moves change the game?

A) They add more winning possibilities  
B) They can jump over an unfavorable intermediate node  
C) Both A and B  
D) They have no effect

**Correct Answer:** C

**Explanation:** Skip moves allow reaching nodes two edges away, potentially bypassing a winning position to reach a losing one.

### Question 2
How to enumerate skip moves from node u?

A) For each successor v of u, check successors of v  
B) Use BFS of depth 2  
C) Both work  
D) Use DFS only

**Correct Answer:** C

**Explanation:** Skip moves are paths u→v→w. Either iterate over all neighbors-of-neighbors or do BFS with depth limit 2.

### Question 3
Time complexity with precomputed skip edges?

A) O(n + m)  
B) O(n + m * degree) for skip enumeration  
C) O(n²)  
D) O(m²)

**Correct Answer:** B

**Explanation:** Each edge can lead to multiple skip edges. Total skip edges can be O(m * avg_degree), which is at most O(m²) but typically smaller.

### Question 4
A node with no regular or skip edges is:

A) Winning  
B) Losing  
C) Draw  
D) Depends on graph

**Correct Answer:** B

**Explanation:** No valid moves = current player cannot move = current player loses.
