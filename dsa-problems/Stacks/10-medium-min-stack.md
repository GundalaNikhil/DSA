# Min Stack with Constant Time

**Difficulty:** Medium
**Topic:** Stacks, Data Structure Design
**License:** Free to use for commercial purposes

## Problem Statement

Design a stack that supports push, pop, top, and getting the minimum element in constant time O(1).

Implement class MinStack with these operations:
- `push(val)`: push element onto stack
- `pop()`: remove top element
- `top()`: get top element
- `get_min()`: get minimum element in the stack

All operations must be O(1) time complexity.

## Constraints

- `-10000 <= val <= 10000`
- Methods `pop`, `top` and `get_min` will always be called on non-empty stack
- At most 30000 calls to each method

## Examples

### Example 1
```
Input:
MinStack stack = new MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.get_min()   → returns -3
stack.pop()
stack.top()       → returns 0
stack.get_min()   → returns -2
```

### Example 2
```
Input:
MinStack stack = new MinStack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.get_min()   → returns 3
stack.pop()
stack.get_min()   → returns 3
stack.pop()
stack.get_min()   → returns 5
```

### Example 3
```
Input:
MinStack stack = new MinStack()
stack.push(10)
stack.get_min()   → returns 10
stack.push(8)
stack.get_min()   → returns 8
stack.push(12)
stack.get_min()   → returns 8
```

### Example 4
```
Input:
MinStack stack = new MinStack()
stack.push(2)
stack.push(1)
stack.push(3)
stack.pop()
stack.pop()
stack.get_min()   → returns 2
```

## Function Signature

### Python
```python
class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass
```

### JavaScript
```javascript
class MinStack {
    constructor() {
        // Your code here
    }

    push(val) {
        // Your code here
    }

    pop() {
        // Your code here
    }

    top() {
        // Your code here
    }

    getMin() {
        // Your code here
    }
}
```

### Java
```java
class MinStack {
    public MinStack() {
        // Your code here
    }

    public void push(int val) {
        // Your code here
    }

    public void pop() {
        // Your code here
    }

    public int top() {
        // Your code here
    }

    public int getMin() {
        // Your code here
    }
}
```

## Hints

1. Use two stacks: one for values, one for minimums
2. When pushing, also push current minimum to min stack
3. When popping, pop from both stacks
4. Minimum is always at top of min stack
5. Alternative: store (value, min) pairs in single stack
6. Time complexity: O(1) for all operations, Space complexity: O(n)

## Tags
`stack` `design` `data-structure` `minimum` `medium`
