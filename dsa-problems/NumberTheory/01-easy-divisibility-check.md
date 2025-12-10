# Prize Distribution Fairness

**Difficulty:** Easy
**Topic:** Number Theory, Divisibility
**License:** Free to use for commercial purposes

## Problem Statement

A teacher has `totalPrizes` identical prizes to distribute equally among `students` students. Determine if the prizes can be distributed fairly (each student gets the same number of prizes with no prizes left over).

Return `true` if fair distribution is possible, `false` otherwise.

## Constraints

- `1 <= totalPrizes <= 100000`
- `1 <= students <= 10000`

## Examples

### Example 1
```
Input: totalPrizes = 20, students = 5
Output: true
Explanation: 20 ÷ 5 = 4 exactly. Each student gets 4 prizes, none left over.
```

### Example 2
```
Input: totalPrizes = 25, students = 6
Output: false
Explanation: 25 ÷ 6 = 4 remainder 1. Cannot distribute fairly.
```

### Example 3
```
Input: totalPrizes = 100, students = 10
Output: true
Explanation: Each student gets exactly 10 prizes.
```

### Example 4
```
Input: totalPrizes = 7, students = 7
Output: true
Explanation: Each student gets exactly 1 prize.
```

### Example 5
```
Input: totalPrizes = 1, students = 2
Output: false
Explanation: Cannot split 1 prize fairly between 2 students.
```

## Function Signature

### Python
```python
def can_distribute_fairly(totalPrizes: int, students: int) -> bool:
    pass
```

### JavaScript
```javascript
function canDistributeFairly(totalPrizes, students) {
    // Your code here
}
```

### Java
```java
public boolean canDistributeFairly(int totalPrizes, int students) {
    // Your code here
}
```

## Hints

1. Check if totalPrizes is divisible by students
2. A number is divisible by another if remainder is 0
3. Use modulo operator: totalPrizes % students == 0
4. Time complexity: O(1), Space complexity: O(1)

## Tags
`number-theory` `divisibility` `modulo` `easy`
