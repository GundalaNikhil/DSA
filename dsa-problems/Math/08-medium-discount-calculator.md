# Wholesale Bulk Pricing

**Difficulty:** Medium
**Topic:** Math, Percentages, Conditional Logic
**License:** Free to use for commercial purposes

## Problem Statement

A wholesaler offers discounts based on order quantity:
- < 50 units: 0% off
- 50-199 units: 5% off
- 200-499 units: 10% off
- 500+ units: 15% off

Additionally, "Premium" partners get an extra flat $50 discount on the final total (if total > $50).

Given `quantity`, `unitPrice`, and `isPremium`, calculate final cost rounded to 2 decimals.

## Constraints

- `1 <= quantity <= 10000`
- `1.0 <= unitPrice <= 1000.0`

## Examples

### Example 1
```
Input: quantity = 100, unitPrice = 10.0, isPremium = false
Output: 950.00
Explanation:
Base cost: 1000.
Discount 5%: 50.
Final: 950.
```

### Example 2
```
Input: quantity = 600, unitPrice = 2.0, isPremium = true
Output: 970.00
Explanation:
Base: 1200.
Discount 15%: 180.
Subtotal: 1020.
Premium discount: 50.
Final: 970.
```

### Example 3
```
Input: quantity = 10, unitPrice = 5.0, isPremium = true
Output: 0.00
Explanation:
Base: 50. No % discount.
Premium discount 50.
Final: 0.
```

## Function Signature

### Python
```python
def calculate_wholesale_cost(quantity: int, unitPrice: float, isPremium: bool) -> float:
    pass
```

### JavaScript
```javascript
function calculateWholesaleCost(quantity, unitPrice, isPremium) {
    // Your code here
}
```

### Java
```java
public double calculateWholesaleCost(int quantity, double unitPrice, boolean isPremium) {
    // Your code here
}
```

## Hints
1. Calculate base total
2. Apply percentage discount
3. Subtract flat discount if applicable

## Tags
`math` `percentage` `medium`
