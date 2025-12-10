# Create Graph Copy

**Difficulty:** Medium
**Topic:** Graphs, DFS, Graph Cloning
**License:** Free to use for commercial purposes

## Problem Statement

You are given a reference to a node in a connected graph. Create a deep copy of the entire graph and return the reference to the copied version of the given node.

Each node has a value and a list of neighbors. The copy should be completely independent of the original graph.

## Constraints

- `1 <= number of nodes <= 100`
- `0 <= node.val <= 100`
- Node values are unique
- No self-loops or duplicate edges

## Examples

### Example 1
```
Input: node with value 1
Graph: 1 - 2
       |   |
       4 - 3

Output: Copy of the graph with same structure
Node 1' connects to 2' and 4'
Node 2' connects to 1' and 3'
Node 3' connects to 2' and 4'
Node 4' connects to 1' and 3'
```

### Example 2
```
Input: node with value 5
Graph: 5 (single node, no neighbors)

Output: Copy node 5' with no neighbors
```

### Example 3
```
Input: node with value 1
Graph: 1 - 2 - 3

Output: 1' - 2' - 3' (same linear structure)
```

### Example 4
```
Input: node with value 1
Graph: 1 - 2
       | X |
       3 - 4

Fully connected square where:
1 connects to 2, 3, 4
2 connects to 1, 3, 4
3 connects to 1, 2, 4
4 connects to 1, 2, 3

Output: Exact copy with same connections
```

## Function Signature

### Python
```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node: Node) -> Node:
    pass
```

### JavaScript
```javascript
class Node {
    constructor(val, neighbors = []) {
        this.val = val;
        this.neighbors = neighbors;
    }
}

function cloneGraph(node) {
    // Your code here
}
```

### Java
```java
class Node {
    int val;
    List<Node> neighbors;
    Node(int v) { this.val = v; this.neighbors = new ArrayList<>(); }
}

public Node cloneGraph(Node node) {
    // Your code here
}
```

## Hints

1. Use a hash map to store mapping from original node to cloned node
2. Use DFS or BFS to traverse the graph
3. When visiting a node, first clone it if not already cloned
4. Then clone all its neighbors recursively
5. The hash map prevents infinite loops and duplicate clones

## Tags
`graph` `dfs` `cloning` `hash-map` `medium`
