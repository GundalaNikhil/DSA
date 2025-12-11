---
unique_problem_id: gametheory_002
display_id: GAMETHEORY-002
slug: token-walk-directed-graph
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - DAG
  - Sprague-Grundy
  - Topological Sort
  - Win-Lose Analysis
---

# Token Walk on Directed Graph

## Problem Description

Token on node s of a finite directed acyclic graph. Players alternate moving token along outgoing edge; player unable to move loses. For each node, determine if it is winning or losing.

## Examples

- Example 1:
  - Input: edges 0→1, 1→2, n=3
  - Output: `[Win, Win, Lose]`
  - Explanation: Node 2 has no outgoing edges (losing). Node 1 can move to 2 (win). Node 0 can move to 1 (win).

- Example 2:
  - Input: edges 0→1, 0→2, 1→2, n=3
  - Output: `[Win, Win, Lose]`
  - Explanation: Node 2 is sink (losing). Nodes 0,1 can reach node 2 (winning).

- Example 3:
  - Input: edges 0→1, 1→2, 2→3, n=4
  - Output: `[Lose, Win, Lose, Lose]`
  - Explanation: 3 loses (sink), 2 moves to losing position (wins), 1 moves to winning (loses), 0 moves to losing (wins). Wait - recalculate: 3=Lose, 2→3 so 2=Win, 1→2 so 1=Lose (can only go to Win), 0→1 so 0=Win.

## Constraints

- `1 <= n <= 2 * 10^5`
- edges <= 2 * 10^5

## Function Signatures

### Java
```java
class Solution {
    public String[] tokenWalkDirectedGraph(int n, int[][] edges) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def token_walk_directed_graph(n: int, edges: List[Tuple[int, int]]) -> List[str]:
    """
    Determine win/lose status for each node.
    
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
    vector<string> tokenWalkDirectedGraph(int n, vector<pair<int,int>>& edges) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (nodes), m (edges)
- Next m lines: from to (edge)

### Sample Input
```
3 2
0 1
1 2
```

## Hints

Use topological order. A node is losing if it has no outgoing edges or all outgoing edges lead to winning positions. A node is winning if at least one outgoing edge leads to a losing position.

## Quiz

### Question 1
What is the win/lose rule for DAG games?

A) A node is winning if it has many edges  
B) A node is winning if it can move to at least one losing position  
C) A node is losing if it can move to any position  
D) Both players always win

**Correct Answer:** B

**Explanation:** In DAG games, if you can force your opponent into a losing position, you win. A node is losing only if ALL moves lead to winning positions for the opponent.

### Question 2
Why is topological sort useful here?

A) It's faster  
B) It processes nodes in reverse order of reachability, so we know outcomes of successors first  
C) It removes cycles  
D) It's not useful

**Correct Answer:** B

**Explanation:** Processing in reverse topological order ensures that when we evaluate a node, all its successors' win/lose statuses are already computed.

### Question 3
What is the status of a sink node (no outgoing edges)?

A) Win  
B) Lose  
C) Draw  
D) Undefined

**Correct Answer:** B

**Explanation:** A sink node has no moves available. The player to move from a sink loses.

### Question 4
What is the time complexity of this algorithm?

A) O(n)  
B) O(n + m) where m is edge count  
C) O(n²)  
D) O(m²)

**Correct Answer:** B

**Explanation:** We visit each node and edge once during topological sort and win/lose propagation.
