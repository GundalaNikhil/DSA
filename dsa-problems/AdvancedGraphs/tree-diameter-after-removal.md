---
unique_problem_id: advgraph_016
display_id: ADVGRAPH-016
slug: tree-diameter-after-removal
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Trees
  - Tree Diameter
  - Dynamic Programming on Trees
  - DFS
  - Re-rooting Technique
---

# Tree Diameter After Edge Removal

## Problem Description

Given tree, compute diameter after removing each edge (for all edges separately).

## Examples

- Example 1:
  - Input: `n=5`, `edges=[(0,1),(1,2),(1,3),(3,4)]`
  - Output: After removing edge  (0,1): max(diameter of component with 0, diameter of component with 1,2,3,4) = max(0, 3) = 3
  - Full output: [3, 2, 3, 2] for removing edges in order given
- Example 2:
  - Input: `n=4`, `edges=[(0,1),(1,2),(2,3)]` (path graph)
  - Output: [2, 1, 2] (removing each edge creates two components)

## Constraints

- `2 <= n <= 100,000` (number of vertices, where 1e5 means 1 × 10^5)
- `n-1` edges (tree structure)
- Vertices are 0-indexed: `0 <= u, v < n`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int[] treeDiameterAfterRemoval(int n, int[][] edges) {
        // For each edge, return max diameter among resulting components
        // Use DP on trees and re-rooting technique
    }
}
```

### Python
```python
from typing import List, Tuple

def tree_diameter_after_removal(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """
    Compute diameter after removing each edge.
    
    Args:
        n: Number of vertices
        edges: Tree edges
    
    Returns:
        List of diameters, one for each edge removal
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> treeDiameterAfterRemoval(int n, const vector<pair<int,int>>& edges) {
        // Precompute diameters/depths using DFS
        // For each edge (u,v), compute max of diameters in two components
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer `n` (vertices)
- Next `n-1` lines: Two integers `u v` representing tree edge

### Sample Input
```
5
0 1
1 2
1 3
3 4
```

## Hints

Precompute subtree information; for each edge, consider the two resulting components.

## Quiz

### Question 1
What is the tree diameter?

A) The longest edge  
B) The longest path (in number of edges) between any two vertices  
C) The degree of the root  
D) The number of leaves

**Correct Answer:** B

**Explanation:** The diameter of a tree is the length of the longest path between any two vertices in the tree.

### Question 2
How can we efficiently compute the diameter of a tree?

A) Try all pairs of vertices  
B) Two DFS/BFS passes: find farthest node from any node, then find farthest from that  
C) Sort vertices  
D) Use Dijkstra

**Correct Answer:** B

**Explanation:** Run BFS/DFS from any node to find the farthest node u, then run BFS/DFS from u to find the farthest node v. The distance from u to v is the diameter.

### Question 3
After removing an edge, the tree splits into how many connected components?

A) 1  
B) 2  
C) n  
D) n-1

**Correct Answer:** B

**Explanation:** Removing one edge from a tree always splits it into exactly two connected components (subtrees).

### Question 4
What is an efficient approach to solve this problem for all edges?

A) Recompute diameter from scratch for each edge removal  
B) Precompute subtree diameters and heights, then for each edge combine information from both sides  
C) Use binary search  
D) Random sampling

**Correct Answer:** B

**Explanation:** Precompute for each subtree its diameter and maximum depth. When removing an edge, the answer is the maximum of the diameters of the two resulting components, which can be computed using precomputed values.
