# Digital Twin Simulation

**Difficulty:** Medium
**Topic:** Graphs, DFS, Graph Cloning
**License:** Free to use for commercial purposes

## Problem Statement

A smart city project requires creating a "digital twin" of a sensor network. The network is a connected graph where each node represents a sensor with a unique ID and a list of connected neighbors.

Given a reference to a sensor node in the physical network, create a deep copy (clone) of the entire network structure for simulation purposes. The clone must be independent of the original.

## Constraints

- `1 <= number of sensors <= 100`
- `1 <= sensor.id <= 100`
- Sensor IDs are unique
- No self-loops or duplicate connections

## Examples

### Example 1
```
Input: sensor 10 connected to 20
       sensor 20 connected to 10, 30
       sensor 30 connected to 20

Output: A new graph where node 10' connects to 20', 20' connects to 10' and 30', 30' connects to 20'.
```

### Example 2
```
Input: sensor 5 connected to 15, 25
       sensor 15 connected to 5, 25
       sensor 25 connected to 5, 15

Output: A complete triangle graph copy with IDs 5, 15, 25.
```

### Example 3
```
Input: sensor 99 (isolated)
Output: sensor 99' (isolated)
```

## Function Signature

### Python
```python
class SensorNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def create_digital_twin(node: SensorNode) -> SensorNode:
    pass
```

### JavaScript
```javascript
class SensorNode {
    constructor(val, neighbors = []) {
        this.val = val;
        this.neighbors = neighbors;
    }
}

function createDigitalTwin(node) {
    // Your code here
}
```

### Java
```java
class SensorNode {
    int val;
    List<SensorNode> neighbors;
    SensorNode(int v) { this.val = v; this.neighbors = new ArrayList<>(); }
}

public SensorNode createDigitalTwin(SensorNode node) {
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
