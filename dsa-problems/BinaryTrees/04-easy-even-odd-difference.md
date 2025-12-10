# Alternating Current Voltage Check

**Difficulty:** Easy
**Topic:** Binary Trees, Tree Traversal
**License:** Free to use for commercial purposes

## Problem Statement

An electrical circuit is modeled as a binary tree where each node has a voltage value. Due to the nature of the alternating current, even voltage values contribute positively to one phase, while odd voltage values contribute to another.

The engineer needs to calculate the "phase difference", which is defined as:
(Sum of all even voltage values) - (Sum of all odd voltage values).

Given the root of the circuit tree, return this difference.

## Constraints

- `1 <= number of nodes <= 3500`
- `1 <= node.val <= 200`

## Examples

### Example 1
```
Input: root = [13, 8, 19, 6, 11]
         13
        /  \
       8   19
      / \
     6  11

Even voltages: 8, 6 → sum = 14
Odd voltages: 13, 19, 11 → sum = 43
Output: 14 - 43 = -29
```

### Example 2
```
Input: root = [24, 16, 32, 8]
         24
        /  \
      16   32
      /
     8

Even voltages: 24, 16, 32, 8 → sum = 80
Odd voltages: none → sum = 0
Output: 80 - 0 = 80
```

### Example 3
```
Input: root = [7, 3, 9, 1, 5]
Even voltages: none → sum = 0
Odd voltages: 7, 3, 9, 1, 5 → sum = 25
Output: 0 - 25 = -25
```

## Function Signature

### Python
```python
def voltage_phase_difference(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
function voltagePhaseDifference(root) {
    // Your code here
}
```

### Java
```java
public int voltagePhaseDifference(TreeNode root) {
    // Your code here
}
```

## Hints

1. Visit all nodes and check if value is even or odd
2. Keep two running sums: one for even, one for odd
3. Check if number is even using modulo: num % 2 == 0
4. Return even_sum - odd_sum at the end
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-traversal` `even-odd` `easy`
