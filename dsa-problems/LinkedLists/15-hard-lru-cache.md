# Browser History Manager

**Difficulty:** Hard
**Topic:** Linked Lists, HashMap, Design
**License:** Free to use for commercial purposes

## Problem Statement

A web browser needs to manage its history of visited pages efficiently. To save memory, it only keeps a limited number of recently visited pages. When the limit is reached, the least recently visited page is removed.

Design a `BrowserHistory` class (LRU Cache) that supports:
- `visit(url, page_data)`: Adds a page to history. If capacity is full, remove the least recently visited page.
- `get_page(url)`: Retrieves page data. This marks the page as most recently used.

Implement the class using a doubly linked list and hash map for O(1) time complexity.

## Constraints

- `1 <= capacity <= 3000`
- `0 <= url <= 10000` (represented as ID)
- `0 <= page_data <= 100000`
- At most `2 * 100000` calls to visit and get_page

## Examples

### Example 1
```
Input:
["BrowserHistory", "visit", "visit", "get_page", "visit", "get_page", "visit", "get_page", "get_page", "get_page"]
[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
BrowserHistory history = new BrowserHistory(2);
history.visit(1, 1);
history.visit(2, 2);
history.get_page(1);    // returns 1
history.visit(3, 3);    // evicts url 2
history.get_page(2);    // returns -1 (not found)
history.visit(4, 4);    // evicts url 1
history.get_page(1);    // returns -1 (not found)
history.get_page(3);    // returns 3
history.get_page(4);    // returns 4
```

## Function Signature

### Python
```python
class BrowserHistory:
    def __init__(self, capacity: int):
        pass
    
    def get_page(self, url: int) -> int:
        pass
    
    def visit(self, url: int, page_data: int) -> None:
        pass
```

### JavaScript
```javascript
class BrowserHistory {
    constructor(capacity) {}
    getPage(url) {}
    visit(url, pageData) {}
}
```

### Java
```java
class BrowserHistory {
    public BrowserHistory(int capacity) {}
    public int getPage(int url) {}
    public void visit(int url, int pageData) {}
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
