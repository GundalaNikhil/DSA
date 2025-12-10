# Signal Strength Tracker

**Difficulty:** Medium
**Topic:** Stacks, Data Structure Design
**License:** Free to use for commercial purposes

## Problem Statement

A radio tower receives a stream of signal strength values. The system needs to efficiently track the history of signals and instantly report the minimum signal strength recorded in the current active session.

Design a `SignalTracker` class that supports:
- `record(strength)`: Add a new signal strength to the history.
- `ignore_last()`: Remove the most recently recorded signal.
- `get_last()`: Get the most recently recorded signal.
- `get_min_strength()`: Retrieve the minimum signal strength in the current history.

All operations must run in O(1) constant time.

## Constraints

- `-10000 <= strength <= 10000`
- Methods `ignore_last`, `get_last` and `get_min_strength` will always be called on non-empty history
- At most 30000 calls to each method

## Examples

### Example 1
```
Input:
tracker = new SignalTracker()
tracker.record(-2)
tracker.record(0)
tracker.record(-3)
tracker.get_min_strength() -> returns -3
tracker.ignore_last()      // removes -3
tracker.get_last()         -> returns 0
tracker.get_min_strength() -> returns -2
```

### Example 2
```
Input:
tracker = new SignalTracker()
tracker.record(10)
tracker.record(5)
tracker.record(20)
tracker.get_min_strength() -> returns 5
tracker.ignore_last()      // removes 20
tracker.get_min_strength() -> returns 5
tracker.ignore_last()      // removes 5
tracker.get_min_strength() -> returns 10
```

## Function Signature

### Python
```python
class SignalTracker:
    def __init__(self):
        pass

    def record(self, strength: int) -> None:
        pass

    def ignore_last(self) -> None:
        pass

    def get_last(self) -> int:
        pass

    def get_min_strength(self) -> int:
        pass
```

### JavaScript
```javascript
class SignalTracker {
    constructor() {
        // Your code here
    }

    record(strength) {
        // Your code here
    }

    ignoreLast() {
        // Your code here
    }

    getLast() {
        // Your code here
    }

    getMinStrength() {
        // Your code here
    }
}
```

### Java
```java
class SignalTracker {
    public SignalTracker() {
        // Your code here
    }

    public void record(int strength) {
        // Your code here
    }

    public void ignoreLast() {
        // Your code here
    }

    public int getLast() {
        // Your code here
    }

    public int getMinStrength() {
        // Your code here
    }
}
```

## Hints

1. Use two stacks: one for values, one for minimums
2. When recording, also push current minimum to min stack
3. When ignoring last, pop from both stacks
4. Minimum is always at top of min stack
5. Time complexity: O(1) for all operations, Space complexity: O(n)

## Tags
`stack` `design` `data-structure` `minimum` `medium`
