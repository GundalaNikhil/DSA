---
unique_problem_id: gametheory_008
display_id: GAMETHEORY-008
slug: kayles-on-graph
version: 1.0.0
difficulty: Hard
topic_tags:
  - Game Theory
  - Kayles
  - Sprague-Grundy
  - Graph Theory
  - Independent Set
---

# Kayles on Graph

## Problem Description

Undirected graph. Move: choose a vertex, remove it and its neighbors. Player unable to move loses. Determine winner using Sprague-Grundy (connected components).

## Examples

- Example 1:
  - Input: Path of 3 nodes: 0-1-2
  - Output: `First`
  - Explanation: Remove node 1 (also removes 0 and 2). All nodes gone. Second player has no moves.

- Example 2:
  - Input: Single edge: 0-1
  - Output: `First`
  - Explanation: Remove either node, its neighbor is also removed. Second player loses.

- Example 3:
  - Input: Triangle: 0-1, 1-2, 2-0
  - Output: `First`
  - Explanation: Remove any node, all three are removed. Second player loses.

## Constraints

- n <= 100
- m <= 300

## Function Signatures

### Java
```java
class Solution {
    public String kaylesOnGraph(int n, int[][] edges) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def kayles_on_graph(n: int, edges: List[Tuple[int, int]]) -> str:
    """
    Determine winner of Kayles game on a graph.
    
    Args:
        n: Number of vertices
        edges: List of (u, v) edges
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string kaylesOnGraph(int n, vector<pair<int,int>>& edges) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (vertices), m (edges)
- Next m lines: u v (edge)

### Sample Input
```
3 2
0 1
1 2
```

## Hints

Each connected component is an independent game. Compute Grundy for each component, XOR them. For trees/paths, closed-form Grundy may exist. For general graphs, use memoization over subgraph states.

## Quiz

### Question 1
How does removing a vertex affect the graph?

A) Only that vertex is removed  
B) The vertex and all its neighbors are removed  
C) The vertex and its edges are removed  
D) Half the graph is removed

**Correct Answer:** B

**Explanation:** In Kayles on graphs, selecting a vertex removes it AND all adjacent vertices, similar to removing a pin in the original Kayles.

### Question 2
Why can we XOR Grundy values of connected components?

A) They're independent games  
B) Sprague-Grundy theorem for disjoint games  
C) Both A and B  
D) We can't XOR them

**Correct Answer:** C

**Explanation:** Connected components don't interact, so they're independent games. The Sprague-Grundy theorem states that the Grundy value of independent games is the XOR of individual values.

### Question 3
What is the Grundy value of an empty graph?

A) 0  
B) 1  
C) -1  
D) Undefined

**Correct Answer:** A

**Explanation:** An empty graph (no vertices) has no moves. The mex of an empty set is 0.

### Question 4
Why is this problem Hard difficulty?

A) Large state space for general graphs  
B) No closed-form solution for arbitrary graphs  
C) Requires complex memoization  
D) All of the above

**Correct Answer:** D

**Explanation:** General graphs don't have simple Grundy formulas like paths/cycles. State enumeration with memoization is needed, and the state space can be exponential.
