# Stock Market Median Tracker

**Problem ID:** HEAP-004
**Display ID:** 87
**Question Name:** Stock Market Median Tracker
**Slug:** stock-market-median-tracker
**Title:** Running Median of Stock Prices
**Difficulty:** Hard
**Premium:** No
**Tags:** Heap, Design, Data Stream, Two Heaps

## Problem Description

Design a system that tracks the median stock price in real-time as new prices stream in. The median is the middle value in an ordered list of numbers. If the list has an even number of elements, the median is the average of the two middle values.

Implement the `StockMedianTracker` class:

- `StockMedianTracker()` - initializes the object
- `void addPrice(int price)` - adds a stock price to the data stream
- `double findMedian()` - returns the median of all prices added so far

## A Simple Scenario (Daily Life Usage)

You're a day trader monitoring stock prices throughout the trading day. Prices fluctuate constantly: $100, $102, $98, $105, etc. You want to know the median price at any moment to understand if the current price is above or below the typical value. After 3 trades at [$100, $102, $98], the median is $100. After a 4th trade at $105, the median becomes $101 (average of $100 and $102). This helps you make informed trading decisions.

## Your Task

Implement an efficient system that can:
1. Add new prices as they come in (one at a time)
2. Calculate the median of all prices seen so far in O(log n) time

The key insight is using two heaps:
- A max heap for the lower half of prices
- A min heap for the upper half of prices
This keeps the data balanced so the median is always at the top(s) of the heaps.

## Why is it Important?

This problem teaches you:

- Advanced heap techniques using two heaps simultaneously
- Balancing data structures for optimal performance
- Handling streaming data with constant-time median access
- Real-world applications in financial technology
- Trade-offs between insertion time and query time

## Examples

### Example 1:

**Input:**
```
["StockMedianTracker", "addPrice", "findMedian", "addPrice", "findMedian", "addPrice", "findMedian"]
[[], [100], [], [95], [], [110], []]
```

**Output:** `[null, null, 100.0, null, 97.5, null, 100.0]`

**Explanation:**
```
StockMedianTracker tracker = new StockMedianTracker();
tracker.addPrice(100);   // prices = [100]
tracker.findMedian();    // return 100.0
tracker.addPrice(95);    // prices = [95, 100]
tracker.findMedian();    // return 97.5 (average of 95 and 100)
tracker.addPrice(110);   // prices = [95, 100, 110]
tracker.findMedian();    // return 100.0
```

### Example 2:

**Input:**
```
["StockMedianTracker", "addPrice", "addPrice", "addPrice", "addPrice", "findMedian"]
[[], [50], [60], [55], [65], []]
```

**Output:** `[null, null, null, null, null, 57.5]`

**Explanation:**
```
tracker.addPrice(50);    // prices = [50]
tracker.addPrice(60);    // prices = [50, 60]
tracker.addPrice(55);    // prices = [50, 55, 60]
tracker.addPrice(65);    // prices = [50, 55, 60, 65]
tracker.findMedian();    // return 57.5 (average of 55 and 60)
```

### Example 3:

**Input:**
```
["StockMedianTracker", "addPrice", "addPrice", "addPrice", "addPrice", "addPrice", "findMedian"]
[[], [10], [20], [30], [40], [50], []]
```

**Output:** `[null, null, null, null, null, null, 30.0]`

**Explanation:**
```
Prices = [10, 20, 30, 40, 50]
Median is the middle element: 30.0
```

## Constraints

- 1 ≤ price ≤ 10^5
- At most 5 × 10^4 calls will be made to addPrice and findMedian
- findMedian will only be called after at least one price has been added
- All prices are positive integers

## Follow-up Questions

1. If all prices from the stream are in the range [0, 100], how would you optimize it?
2. If 99% of all prices are in the range [0, 100], how would you optimize it?

## Asked by Companies

- Bloomberg
- Robinhood
- Citadel
- Two Sigma
