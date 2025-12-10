# Simplify Unix File Path

**Difficulty:** Medium
**Topic:** Stacks, String Processing
**License:** Free to use for commercial purposes

## Problem Statement

Given an absolute Unix file path, simplify it by resolving `.` (current directory) and `..` (parent directory).

Rules:
- `.` means stay in current directory (ignore it)
- `..` means go up one directory
- Multiple slashes should be treated as single slash
- Result should start with `/`

Return the simplified path.

## Constraints

- `1 <= path.length <= 3000`
- Path consists of English letters, digits, '.', '/', and '-'
- Path starts with '/'

## Examples

### Example 1
```
Input: path = "/home/user/documents/../pictures"
Output: "/home/user/pictures"
Explanation: Go to documents, then back up to user, then to pictures
```

### Example 2
```
Input: path = "/a/./b/../../c/"
Output: "/c"
Explanation:
- /a: go to a
- /./: stay in a
- /b: go to b
- /..: back to a
- /..: back to root
- /c/: go to c
```

### Example 3
```
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: Multiple slashes treated as one
```

### Example 4
```
Input: path = "/../"
Output: "/"
Explanation: Cannot go above root
```

## Function Signature

### Python
```python
def simplify_path(path: str) -> str:
    pass
```

### JavaScript
```javascript
function simplifyPath(path) {
    // Your code here
}
```

### Java
```java
public String simplifyPath(String path) {
    // Your code here
}
```

## Hints

1. Split path by '/' to get components
2. Use stack to track valid directory names
3. Skip empty strings and '.'
4. For '..', pop from stack if not empty
5. For valid names, push to stack
6. Join stack with '/' and prepend '/'
7. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `string` `path-processing` `medium`
