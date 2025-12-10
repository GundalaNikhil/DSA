# Population Growth Model

**Difficulty:** Medium
**Topic:** Math, Compound Growth
**License:** Free to use for commercial purposes

## Problem Statement

A city's population grows at a `growthRate` percent annually. Given an `initialPopulation`, calculate the projected population after `years`.

Formula: P_final = P_initial * (1 + rate/100)^years

Return result rounded down to nearest integer (people are whole units).

## Constraints

- `1000 <= initialPopulation <= 10^7`
- `0.1 <= growthRate <= 10.0`
- `1 <= years <= 100`

## Examples

### Example 1
```
Input: initialPopulation = 10000, growthRate = 5.0, years = 2
Output: 11025
Explanation:
Year 1: 10000 * 1.05 = 10500
Year 2: 10500 * 1.05 = 11025
```

### Example 2
```
Input: initialPopulation = 1000, growthRate = 10.0, years = 3
Output: 1331
Explanation: 1000 * 1.1^3 = 1331.
```

### Example 3
```
Input: initialPopulation = 5000, growthRate = 2.5, years = 1
Output: 5125
```

## Function Signature

### Python
```python
def predict_population(initialPopulation: int, growthRate: float, years: int) -> int:
    pass
```

### JavaScript
```javascript
function predictPopulation(initialPopulation, growthRate, years) {
    // Your code here
}
```

### Java
```java
public int predictPopulation(int initialPopulation, double growthRate, int years) {
    // Your code here
}
```

## Hints
1. Use power function
2. Cast to integer at end

## Tags
`math` `growth` `medium`
