# Food Delivery Dispatcher

**Problem ID:** HEAP-003
**Display ID:** 86
**Question Name:** Food Delivery Dispatcher
**Slug:** food-delivery-dispatcher
**Title:** Nearest Available Driver
**Difficulty:** Easy
**Premium:** No
**Tags:** Heap, Math, Geometry, Priority Queue

## Problem Description

You are building a dispatch system for a food delivery service. When a customer places an order, you need to find the K nearest available drivers to assign the delivery. Each driver has a location represented by (x, y) coordinates on a 2D grid, and the restaurant is located at the origin (0, 0).

Calculate the Euclidean distance from the origin to each driver and return the K drivers who are closest to the restaurant.

## A Simple Scenario (Daily Life Usage)

Imagine you just ordered pizza through a delivery app. The restaurant is at position (0, 0), and there are multiple drivers scattered around the city. Driver A is 3 miles away, Driver B is 5 miles away, and Driver C is 2 miles away. The system should assign Driver C (closest) to pick up your order for fastest delivery. If you need to assign 2 drivers for multiple orders, it picks C and A.

## Your Task

Write a function that takes an array of driver locations `[[x1, y1], [x2, y2], ...]` and an integer K, then returns the K closest drivers to the origin (0, 0).

The distance from origin to point (x, y) is calculated as: `sqrt(x^2 + y^2)`

You may return the answer in any order. The answer is guaranteed to be unique (no two drivers are at the same distance).

## Why is it Important?

This problem teaches you:

- Using min heaps to find K smallest elements efficiently
- Applying geometric distance calculations
- Optimizing location-based queries common in mobile apps
- Understanding heap operations for nearest neighbor problems
- Time complexity: O(n log k) with heap vs O(n log n) with sorting

## Examples

### Example 1:

**Input:**
```
drivers = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
```

**Output:** `[[0, 1], [-2, 2]]`

**Explanation:**
- Distance to [1, 3] = sqrt(1 + 9) = sqrt(10) ≈ 3.16
- Distance to [-2, 2] = sqrt(4 + 4) = sqrt(8) ≈ 2.83
- Distance to [5, 8] = sqrt(25 + 64) = sqrt(89) ≈ 9.43
- Distance to [0, 1] = sqrt(0 + 1) = 1.0

Closest 2 are [0, 1] and [-2, 2].

### Example 2:

**Input:**
```
drivers = [[3, 3], [5, -1], [-2, 4]]
k = 1
```

**Output:** `[[3, 3]]`

**Explanation:**
- Distance to [3, 3] = sqrt(9 + 9) = sqrt(18) ≈ 4.24
- Distance to [5, -1] = sqrt(25 + 1) = sqrt(26) ≈ 5.10
- Distance to [-2, 4] = sqrt(4 + 16) = sqrt(20) ≈ 4.47

Closest is [3, 3].

### Example 3:

**Input:**
```
drivers = [[1, 1], [-1, -1], [2, 2]]
k = 2
```

**Output:** `[[1, 1], [-1, -1]]`

**Explanation:**
- Distance to [1, 1] = sqrt(2) ≈ 1.41
- Distance to [-1, -1] = sqrt(2) ≈ 1.41
- Distance to [2, 2] = sqrt(8) ≈ 2.83

Closest 2 are [1, 1] and [-1, -1] (both at same distance, but both closer than [2, 2]).

## Constraints

- 1 ≤ k ≤ drivers.length ≤ 10^4
- -10^4 ≤ x, y ≤ 10^4
- All driver locations are unique
- No driver is at the origin (0, 0)

## Asked by Companies

- DoorDash
- Uber Eats
- Grubhub
- Instacart
