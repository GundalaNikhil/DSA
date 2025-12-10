# Robot Navigation Command Simplification

**Difficulty:** Medium
**Topic:** Stacks, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

A robot receives navigation commands as a path string. The path consists of directional moves separated by slashes `/`.
- `.` means "stay in current position" (no-op).
- `..` means "move back to previous position" (parent node).
- Directory names (e.g., `room1`) mean "move into that room".
- Multiple slashes `//` should be treated as a single slash.

Given an absolute path string starting with `/`, simplify it to the shortest canonical path.

## Constraints

- `1 <= path.length <= 3000`
- Path consists of English letters, digits, '.', '/', and '_'
- Path starts with '/'

## Examples

### Example 1
```
Input: path = "/hallway/room1/../kitchen"
Output: "/hallway/kitchen"
Explanation: Go to room1, then back to hallway, then to kitchen.
```

### Example 2
```
Input: path = "/start/./checkpoint/../../end/"
Output: "/end"
Explanation:
- /start: at start
- /./: stay at start
- /checkpoint: at checkpoint
- /..: back to start
- /..: back to root
- /end/: at end
```

### Example 3
```
Input: path = "/sector//A/"
Output: "/sector/A"
Explanation: Double slash treated as single.
```

### Example 4
```
Input: path = "/../"
Output: "/"
Explanation: Cannot go back past the starting point (root).
```

## Function Signature

### Python
```python
def simplify_navigation(path: str) -> str:
    pass
```

### JavaScript
```javascript
function simplifyNavigation(path) {
    // Your code here
}
```

### Java
```java
public String simplifyNavigation(String path) {
    // Your code here
}
```

## Hints

1. Split path by '/' to get components
2. Use stack to track valid locations
3. Skip empty strings and '.'
4. For '..', pop from stack if not empty
5. For valid names, push to stack
6. Join stack with '/' and prepend '/'
7. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `string` `path-processing` `medium`
