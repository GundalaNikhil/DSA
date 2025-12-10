# Halloween Candy Distribution

**Difficulty:** Easy
**Topic:** Math, Modulo, Division
**License:** Free to use for commercial purposes

## Problem Statement

You have a bag of `totalCandy` pieces to distribute equally among `kids` trick-or-treaters. Determine how many pieces each kid gets and how many are left over for yourself.

Return `[candyPerKid, leftover]`.

## Constraints

- `1 <= totalCandy <= 10000`
- `1 <= kids <= 1000`

## Examples

### Example 1
```
Input: totalCandy = 50, kids = 7
Output: [7, 1]
Explanation: 50 / 7 = 7 with remainder 1.
```

### Example 2
```
Input: totalCandy = 20, kids = 5
Output: [4, 0]
Explanation: Exact division.
```

### Example 3
```
Input: totalCandy = 5, kids = 10
Output: [0, 5]
Explanation: Not enough candy for everyone to get even 1.
```

## Function Signature

### Python
```python
def distribute_candy(totalCandy: int, kids: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function distributeCandy(totalCandy, kids) {
    // Your code here
}
```

### Java
```java
public int[] distributeCandy(int totalCandy, int kids) {
    // Your code here
}
```

## Hints
1. Integer division for per-kid amount
2. Modulo for remainder

## Tags
`math` `modulo` `division` `easy`
