# Birthday Candle Distribution

**Difficulty:** Easy
**Topic:** Math, Modulo, Division
**License:** Free to use for commercial purposes

## Problem Statement

For a birthday party, you have `totalCandles` candles to distribute equally among `cakes`. Each cake should receive the same number of candles. Determine how many candles each cake gets and how many candles will be left over.

Return an array `[candlesPerCake, leftoverCandles]`.

## Constraints

- `1 <= totalCandles <= 10000`
- `1 <= cakes <= 1000`
- `cakes <= totalCandles`

## Examples

### Example 1
```
Input: totalCandles = 25, cakes = 4
Output: [6, 1]
Explanation: 25 ÷ 4 = 6 remainder 1. Each cake gets 6 candles, 1 candle left over.
```

### Example 2
```
Input: totalCandles = 100, cakes = 10
Output: [10, 0]
Explanation: 100 ÷ 10 = 10 exactly. Each cake gets 10 candles, no leftovers.
```

### Example 3
```
Input: totalCandles = 17, cakes = 5
Output: [3, 2]
Explanation: 17 ÷ 5 = 3 remainder 2. Each cake gets 3 candles, 2 candles left over.
```

### Example 4
```
Input: totalCandles = 7, cakes = 7
Output: [1, 0]
Explanation: Each cake gets exactly 1 candle.
```

## Function Signature

### Python
```python
def distribute_candles(totalCandles: int, cakes: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function distributeCandles(totalCandles, cakes) {
    // Your code here
}
```

### Java
```java
public int[] distributeCandles(int totalCandles, int cakes) {
    // Your code here
}
```

## Hints

1. Use integer division to find candles per cake
2. Use modulo operator (%) to find leftover candles
3. In most languages: `candlesPerCake = totalCandles // cakes` or `totalCandles / cakes`
4. Leftover: `totalCandles % cakes`
5. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `division` `modulo` `remainder` `easy`
