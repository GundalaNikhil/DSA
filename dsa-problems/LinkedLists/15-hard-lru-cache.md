# LRU Cache Implementation

**Difficulty:** Hard
**Topic:** Linked Lists, HashMap, Design
**License:** Free to use for commercial purposes

## Problem Statement

Design an LRU (Least Recently Used) cache using a doubly linked list and hash map. Support `get(key)` and `put(key, value)` operations in O(1) time.

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10000`
- `0 <= value <= 100000`
- At most `2 * 100000` calls to get and put

## Examples

### Example 1
```
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);    // returns 1
cache.put(3, 3); // evicts key 2
cache.get(2);    // returns -1 (not found)
cache.put(4, 4); // evicts key 1
cache.get(1);    // returns -1 (not found)
cache.get(3);    // returns 3
cache.get(4);    // returns 4
```

## Function Signature

### Python
```python
class LRUCache:
    def __init__(self, capacity: int):
        pass
    
    def get(self, key: int) -> int:
        pass
    
    def put(self, key: int, value: int) -> None:
        pass
```

### JavaScript
```javascript
class LRUCache {
    constructor(capacity) {}
    get(key) {}
    put(key, value) {}
}
```

### Java
```java
class LRUCache {
    public LRUCache(int capacity) {}
    public int get(int key) {}
    public void put(int key, int value) {}
}
```

## Hints

1. Use doubly linked list for order
2. Use hashmap for O(1) access
3. Most recent at head, least at tail
4. Move to head on access
5. Remove tail when capacity exceeded

## Tags
`linked-list` `hashmap` `design` `lru-cache` `hard`
