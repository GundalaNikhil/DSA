# Flight Route Optimizer

**Problem ID:** GRP-005
**Display ID:** 52
**Question Name:** Flight Route Optimizer
**Slug:** flight-route-optimizer
**Title:** Cheapest Flights Within K Stops
**Difficulty:** Medium
**Premium:** Yes
**Tags:** Graph, Shortest Path, Breadth-First Search

## Problem Description

Find the cheapest flight from source to destination with at most k stops. If no such route exists, return -1.

## A Simple Scenario (Daily Life Usage)

Flying from NYC to LA with at most 1 stop. Direct flight: $500. Via Chicago: $200 + $150 = $350 (cheaper!). Via Miami: $180 + $180 = $360. Best option: NYC → Chicago → LA = $350. Airlines use this to find optimal routes for passengers.

## Your Task

Given flights [from, to, price], source, destination, and k stops, find minimum cost.

## Why is it Important?

This problem teaches you:

- Shortest path with constraints
- Modified Dijkstra's algorithm
- BFS with pruning
- Travel optimization

## Examples

### Example 1:

**Input:** `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1`
**Output:** `200`
**Explanation:** 0 → 1 → 2 costs 200 (within 1 stop).

### Example 2:

**Input:** `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0`
**Output:** `500`
**Explanation:** Direct flight only (no stops allowed).

### Example 3:

**Input:** `n = 4, flights = [[0,1,100],[1,2,100],[2,3,100]], src = 0, dst = 3, k = 1`
**Output:** `-1`
**Explanation:** Need 2 stops minimum, but k=1.

## Constraints

- 1 ≤ n ≤ 100
- 0 ≤ flights.length ≤ n * (n - 1) / 2
- flights[i].length == 3
- 0 ≤ from, to < n
- 1 ≤ price ≤ 10^4
- 0 ≤ k ≤ n

## Asked by Companies

- Google Flights
- Expedia
- Kayak
- Skyscanner
