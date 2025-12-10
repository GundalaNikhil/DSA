# Investment Growth Calculator

**Difficulty:** Medium
**Topic:** Math, Compound Interest, Exponentiation
**License:** Free to use for commercial purposes

## Problem Statement

An investor deposits `principal` dollars in a savings account that offers `annualRate` percent interest compounded monthly. Calculate the total amount in the account after `years` years.

Use the compound interest formula:
A = P × (1 + r/n)^(n×t)

Where:
- A = final amount
- P = principal (initial deposit)
- r = annual interest rate (as decimal)
- n = number of times interest is compounded per year (12 for monthly)
- t = time in years

Return the final amount rounded to 2 decimal places.

## Constraints

- `1 <= principal <= 1000000`
- `0.1 <= annualRate <= 20.0` (percentage, e.g., 5.0 means 5%)
- `1 <= years <= 50`

## Examples

### Example 1
```
Input: principal = 1000, annualRate = 5.0, years = 1
Output: 1051.16
Explanation:
  Monthly rate = 5.0 / 100 / 12 = 0.004167
  A = 1000 × (1 + 0.004167)^12 = 1000 × 1.05116 ≈ 1051.16
```

### Example 2
```
Input: principal = 5000, annualRate = 3.5, years = 10
Output: 7072.68
Explanation:
  Monthly rate = 3.5 / 100 / 12
  A = 5000 × (1 + monthly_rate)^120 ≈ 7072.68
```

### Example 3
```
Input: principal = 10000, annualRate = 7.2, years = 5
Output: 14312.47
Explanation:
  A = 10000 × (1 + 0.072/12)^60 ≈ 14312.47
```

### Example 4
```
Input: principal = 2500, annualRate = 4.0, years = 3
Output: 2817.76
Explanation:
  A = 2500 × (1 + 0.04/12)^36 ≈ 2817.76
```

## Function Signature

### Python
```python
def calculate_investment_growth(principal: float, annualRate: float, years: int) -> float:
    pass
```

### JavaScript
```javascript
function calculateInvestmentGrowth(principal, annualRate, years) {
    // Your code here
}
```

### Java
```java
public double calculateInvestmentGrowth(double principal, double annualRate, int years) {
    // Your code here
}
```

## Hints

1. Convert annual rate from percentage to decimal: r = annualRate / 100
2. Monthly compounding means n = 12
3. Use exponentiation: most languages have a pow() or ** operator
4. Formula: A = principal × (1 + r/12)^(12 × years)
5. Round to 2 decimal places: round(value, 2) or similar
6. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `compound-interest` `exponentiation` `financial-calculations` `medium`
