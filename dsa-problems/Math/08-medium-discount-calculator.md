# Multi-Tier Discount Calculator

**Difficulty:** Medium
**Topic:** Math, Percentages, Conditional Logic
**License:** Free to use for commercial purposes

## Problem Statement

An online store offers tiered discounts based on cart value:
- If cart value < $100: No discount (0%)
- If cart value >= $100 and < $500: 10% discount
- If cart value >= $500 and < $1000: 15% discount
- If cart value >= $1000: 20% discount

Additionally, if the customer has a loyalty membership, they get an extra 5% off the already discounted price.

Given the `cartValue` (in dollars) and `hasLoyalty` (boolean), calculate the final price the customer pays after all applicable discounts. Round the result to 2 decimal places.

## Constraints

- `1 <= cartValue <= 10000`
- `hasLoyalty` is either `true` or `false`

## Examples

### Example 1
```
Input: cartValue = 150, hasLoyalty = false
Output: 135.00
Explanation: Cart value $150 gets 10% discount: $150 × 0.90 = $135.00
```

### Example 2
```
Input: cartValue = 150, hasLoyalty = true
Output: 128.25
Explanation:
  - Base discount (10%): $150 × 0.90 = $135
  - Loyalty discount (5% of discounted): $135 × 0.95 = $128.25
```

### Example 3
```
Input: cartValue = 1200, hasLoyalty = true
Output: 912.00
Explanation:
  - Base discount (20%): $1200 × 0.80 = $960
  - Loyalty discount (5%): $960 × 0.95 = $912.00
```

### Example 4
```
Input: cartValue = 75, hasLoyalty = true
Output: 71.25
Explanation:
  - No base discount (cart < $100)
  - Loyalty discount (5%): $75 × 0.95 = $71.25
```

### Example 5
```
Input: cartValue = 500, hasLoyalty = false
Output: 425.00
Explanation: Cart value $500 gets 15% discount: $500 × 0.85 = $425.00
```

## Function Signature

### Python
```python
def calculate_final_price(cartValue: float, hasLoyalty: bool) -> float:
    pass
```

### JavaScript
```javascript
function calculateFinalPrice(cartValue, hasLoyalty) {
    // Your code here
}
```

### Java
```java
public double calculateFinalPrice(double cartValue, boolean hasLoyalty) {
    // Your code here
}
```

## Hints

1. Determine which tier discount applies based on cart value
2. Apply tier discount first
3. If loyalty member, apply additional 5% on discounted price
4. Round to 2 decimal places at the end
5. Use conditional statements or a mapping structure
6. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `percentage` `conditional` `pricing` `medium`
