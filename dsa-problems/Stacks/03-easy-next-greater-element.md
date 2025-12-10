# Next Greater Element

**Difficulty:** Easy
**Topic:** Stacks, Array
**License:** Free to use for commercial purposes

## Problem Statement

Given an array of integers, for each element find the next greater element to its right. If no greater element exists, use -1.

Return an array where each position contains the next greater element.

## Constraints

- `1 <= array.length <= 3000`
- `-10000 <= array[i] <= 10000`

## Examples

### Example 1
```
Input: arr = [4, 7, 3, 9, 2]
Output: [7, 9, 9, -1, -1]
Explanation:
- 4: next greater is 7
- 7: next greater is 9
- 3: next greater is 9
- 9: no greater element, -1
- 2: no greater element, -1
```

### Example 2
```
Input: arr = [13, 8, 11, 6, 15]
Output: [15, 11, 15, 15, -1]
Explanation:
- 13: next greater is 15
- 8: next greater is 11
- 11: next greater is 15
- 6: next greater is 15
- 15: no greater, -1
```

### Example 3
```
Input: arr = [5, 4, 3, 2, 1]
Output: [-1, -1, -1, -1, -1]
Explanation: Descending array, no next greater for any
```

### Example 4
```
Input: arr = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, -1]
Explanation: Each element's next is greater
```

## Function Signature

### Python
```python
from typing import List

def next_greater_elements(arr: List[int]) -> List[int]:
    pass
```

### JavaScript
```javascript
function nextGreaterElements(arr) {
    // Your code here
}
```

### Java
```java
public int[] nextGreaterElements(int[] arr) {
    // Your code here
}
```

## Hints

1. Use stack to keep track of elements waiting for their next greater
2. Traverse array from right to left
3. For each element, pop from stack while top is smaller
4. Top of stack is the next greater element
5. Push current element to stack
6. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `array` `monotonic-stack` `easy`
