# Cloning a Neural Network

**Difficulty:** Hard
**Topic:** Linked Lists, HashMap, Deep Copy
**License:** Free to use for commercial purposes

## Problem Statement

A scientist is simulating a neural network where each neuron is linked to the next neuron in a sequence, and also has a "random" connection to any other neuron in the network (or null). To run parallel simulations, the scientist needs to create an exact deep copy of this network structure.

Given a linked list where each node represents a neuron with a `next` pointer and a `random` pointer, create a deep copy.

Return the head of the cloned network.

## Constraints

- `0 <= number of neurons <= 1000`
- `-10000 <= neuron.val <= 10000`
- Random pointer can point to any neuron or null

## Examples

### Example 1
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Explanation: Deep copy with same structure.
```

### Example 2
```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

### Example 3
```
Input: head = []
Output: []
```

## Function Signature

### Python
```python
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def clone_neural_network(head: Node) -> Node:
    pass
```

### JavaScript
```javascript
function cloneNeuralNetwork(head) {
    // Your code here
}
```

### Java
```java
public Node cloneNeuralNetwork(Node head) {
    // Your code here
}
```

## Hints

1. Use hashmap to map old neurons → new neurons
2. First pass: create all new neurons
3. Second pass: set next and random connections
4. Time: O(n), Space: O(n)

## Tags
`linked-list` `hashmap` `deep-copy` `random-pointer` `hard`
