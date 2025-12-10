# Stock Price Span Calculator

**Problem ID:** STK-006
**Display ID:** 23
**Question Name:** Stock Price Span Calculator
**Slug:** stock-price-span-calculator
**Title:** Daily Stock Price Span
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Stack, Monotonic Stack, Design

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

Implement the StockSpanner class:
- `StockSpanner()` initializes the object
- `int next(int price)` returns the span of the stock's price given that today's price is price

## A Simple Scenario (Daily Life Usage)

You're building a trading platform like Robinhood or E*TRADE. Traders want to see "momentum indicators" - how many consecutive days the stock has been performing at or below today's level. If today's price is $100 and the previous 3 days were $95, $90, $85, then the span is 4 (today + 3 previous days). This helps traders identify bullish trends.

## Your Task

Design a data structure that efficiently calculates the price span for each new day's stock price.

## Why is it Important?

This problem teaches you:

- Monotonic stack pattern
- Efficient span calculation
- Financial algorithm design
- Real-time data processing

## Examples

### Example 1:

**Input:**
```
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
```

**Output:**
```
[null, 1, 1, 1, 2, 1, 4, 6]
```

**Explanation:**
```
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1 (just today)
stockSpanner.next(80);  // return 1 (80 < 100, so span is 1)
stockSpanner.next(60);  // return 1 (60 < 80, so span is 1)
stockSpanner.next(70);  // return 2 (70 >= 60, span includes day 3 and 4)
stockSpanner.next(60);  // return 1 (60 < 70, so span is 1)
stockSpanner.next(75);  // return 4 (75 >= 60, 70, 60, so span is days 5,4,3,2)
stockSpanner.next(85);  // return 6 (85 >= all previous prices, span is all 6 days)
```

### Example 2:

**Input:**
```
["StockSpanner", "next", "next", "next"]
[[], [50], [60], [70]]
```

**Output:**
```
[null, 1, 2, 3]
```

**Explanation:**
- Day 1: price = 50, span = 1
- Day 2: price = 60 (>= 50), span = 2
- Day 3: price = 70 (>= 60, 50), span = 3

## Constraints

- 1 ≤ price ≤ 100,000
- At most 10,000 calls will be made to next

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Robinhood
- E*TRADE
- TD Ameritrade
- Interactive Brokers

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
