# Copy List with Random Pointer

**Difficulty:** Hard
**Topic:** Linked Lists, HashMap, Deep Copy
**License:** Free to use for commercial purposes

## Problem Statement

A graph serializer needs to clone complex structures. Given a linked list where each node has a `next` pointer and a `random` pointer (pointing to any node or null), create a deep copy.

Return the head of the copied list.

## Constraints

- `0 <= number of nodes <= 1000`
- `-10000 <= node.val <= 10000`
- Random pointer can point to any node or null

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

def copy_random_list(head: Node) -> Node:
    pass
```

### JavaScript
```javascript
function copyRandomList(head) {
    // Your code here
}
```

### Java
```java
public Node copyRandomList(Node head) {
    // Your code here
}
```

## Hints

1. Use hashmap to map old → new nodes
2. First pass: create all nodes
3. Second pass: set next and random
4. Time: O(n), Space: O(n)

## Tags
`linked-list` `hashmap` `deep-copy` `random-pointer` `hard`
